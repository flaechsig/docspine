from __future__ import annotations

import os
import shutil
import stat
import tempfile
import unittest
from pathlib import Path

from support import ProjectTest, req
from test_cli import run_main

from docspine import diagram

DOT = "digraph G { a -> b }\n"
SVG = '<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg"></svg>\n'


class StubTools(ProjectTest):
    """Puts stand-ins for dot and plantuml on PATH that write a fixed SVG."""

    def setUp(self):
        super().setUp()
        self._bin = tempfile.TemporaryDirectory()
        self.bin = Path(self._bin.name)
        self._path = os.environ.get("PATH", "")

    def tearDown(self):
        os.environ["PATH"] = self._path
        self._bin.cleanup()
        super().tearDown()

    def tool(self, name: str, script: str = None):
        body = script or f"#!/bin/sh\ncat > /dev/null\nprintf '%s' '{SVG}'\n"
        path = self.bin / name
        path.write_text(body, encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)

    def only_stub_tools(self):
        os.environ["PATH"] = str(self.bin)

    def stub_tools_first(self):
        os.environ["PATH"] = str(self.bin) + os.pathsep + self._path


@req("REQ-0039")
class StaleImages(StubTools):
    def test_source_without_svg(self):
        findings = self.findings({"docs/diagrams/context.dot": DOT})
        self.assertEqual([(f.code, f.path) for f in findings], [(12, "docs/diagrams/context.dot")])
        self.assertIn("docspine diagram docs/diagrams/context.dot", findings[0].message)

    def test_svg_not_produced_by_docspine(self):
        findings = self.findings({"docs/diagrams/context.dot": DOT, "docs/diagrams/context.svg": SVG})
        self.assertEqual([f.code for f in findings], [12])
        self.assertIn("not produced with 'docspine diagram'", findings[0].message)

    def test_source_changed_after_rendering(self):
        self.tool("dot")
        self.stub_tools_first()
        self.write({"docs/diagrams/context.dot": DOT})
        diagram.render(self.root / "docs/diagrams/context.dot")
        self.assertEqual(self.findings(), [])
        findings = self.findings({"docs/diagrams/context.dot": "digraph G { a -> c }\n"})
        self.assertEqual([f.code for f in findings], [12])
        self.assertIn("older version", findings[0].message)

    def test_line_endings_do_not_count(self):
        self.tool("dot")
        self.stub_tools_first()
        self.write({"docs/diagrams/context.dot": DOT})
        diagram.render(self.root / "docs/diagrams/context.dot")
        (self.root / "docs/diagrams/context.dot").write_bytes(DOT.replace("\n", "\r\n").encode())
        self.assertEqual(self.findings(), [])

    def test_plantuml_and_legacy(self):
        findings = self.findings({"docs/08-concepts/flow.puml": "@startuml\n@enduml\n",
                                  "docs/legacy/old.dot": DOT})
        self.assertEqual([(f.code, f.path) for f in findings], [(12, "docs/08-concepts/flow.puml")])


@req("REQ-0040")
class DiagramCommand(StubTools):
    def test_renders_and_records_checksum(self):
        self.tool("dot")
        self.stub_tools_first()
        self.write({"docs/diagrams/context.dot": DOT})
        code, out, _ = run_main("--root", str(self.root), "diagram", "docs/diagrams/context.dot")
        self.assertEqual((code, out.strip()), (0, "written: docs/diagrams/context.svg"))
        svg = (self.root / "docs/diagrams/context.svg").read_text(encoding="utf-8")
        self.assertTrue(svg.startswith('<?xml version="1.0" encoding="UTF-8"?>\n<!-- docspine-source sha256:'))
        self.assertIn(diagram.checksum(self.root / "docs/diagrams/context.dot"), svg)
        self.assertEqual(svg.count("docspine-source"), 1)

    def test_without_arguments_renders_every_stale_image(self):
        self.tool("dot")
        self.tool("plantuml")
        self.stub_tools_first()
        self.write({"docs/diagrams/a.dot": DOT, "docs/diagrams/b.puml": "@startuml\n@enduml\n"})
        code, out, _ = run_main("--root", str(self.root), "diagram")
        self.assertEqual(code, 0)
        self.assertEqual(sorted(out.split()), sorted(["written:", "docs/diagrams/a.svg",
                                                      "written:", "docs/diagrams/b.svg"]))
        code, out, _ = run_main("--root", str(self.root), "diagram")
        self.assertEqual((code, out.strip()), (0, "all diagram images are current"))

    def test_rendering_again_replaces_the_checksum(self):
        self.tool("dot")
        self.stub_tools_first()
        self.write({"docs/diagrams/context.dot": DOT})
        source = self.root / "docs/diagrams/context.dot"
        diagram.render(source)
        source.write_text("digraph G { x }\n", encoding="utf-8")
        diagram.render(source)
        svg = (self.root / "docs/diagrams/context.svg").read_text(encoding="utf-8")
        self.assertEqual(svg.count("docspine-source"), 1)
        self.assertEqual(diagram.state(source), "current")

    @unittest.skipUnless(shutil.which("dot"), "Graphviz not installed")
    def test_with_real_graphviz(self):
        self.write({"docs/diagrams/context.dot": DOT})
        code, _, err = run_main("--root", str(self.root), "diagram")
        self.assertEqual(code, 0, err)
        svg = (self.root / "docs/diagrams/context.svg").read_text(encoding="utf-8")
        self.assertIn("<svg", svg)
        self.assertEqual(self.findings(), [])


@req("REQ-0041")
class MissingTool(StubTools):
    def test_missing_tool_is_named_and_nothing_is_written(self):
        self.only_stub_tools()
        self.write({"docs/diagrams/context.dot": DOT})
        code, out, err = run_main("--root", str(self.root), "diagram", "docs/diagrams/context.dot")
        self.assertEqual(code, 2)
        self.assertIn("'dot' not found: Graphviz is needed", err)
        self.assertFalse((self.root / "docs/diagrams/context.svg").exists())

    def test_failing_tool_is_reported(self):
        self.tool("dot", "#!/bin/sh\necho 'syntax error in line 1' >&2\nexit 1\n")
        self.stub_tools_first()
        self.write({"docs/diagrams/context.dot": "digraph {\n"})
        code, _, err = run_main("--root", str(self.root), "diagram")
        self.assertEqual(code, 2)
        self.assertIn("Graphviz could not render context.dot: syntax error in line 1", err)
        self.assertFalse((self.root / "docs/diagrams/context.svg").exists())
