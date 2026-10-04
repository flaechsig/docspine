from __future__ import annotations

import ast
import contextlib
import io
import subprocess
import sys
import tempfile
from pathlib import Path

from support import STORY, ProjectTest, replace, req

from docspine import project, render
from docspine.__main__ import main

CLI = Path(__file__).resolve().parents[1]


def run_main(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(list(args))
    return code, out.getvalue(), err.getvalue()


@req("REQ-0012")
class ExitStatus(ProjectTest):
    def test_errors_give_non_zero_exit(self):
        self.write({"docs/01-goals/stories/US-0001.md": replace(STORY, "epic: E-CORE", "epic: E-X")})
        code, out, _ = run_main("--root", str(self.root), "check")
        self.assertEqual(code, 1)
        self.assertIn("error 3", out)

    def test_no_errors_give_zero_exit(self):
        self.write({})
        run_main("--root", str(self.root), "render")
        code, out, _ = run_main("--root", str(self.root), "check")
        self.assertEqual((code, out.strip()), (0, "OK"))


@req("REQ-0013")
class StatusOverview(ProjectTest):
    def test_status_region_written(self):
        self.write({"docs/01-goals/stories/US-0002.md":
                    STORY.replace("US-0001", "US-0002").replace("status: open", "status: verified")
                    .replace("[REQ-0001]", "[]") + "evidence: []\n"})
        render.run(project.load(self.root))
        text = (self.root / "docs/01-goals/README.md").read_text(encoding="utf-8")
        self.assertIn("<!-- generated:status -->", text)
        self.assertIn("**2 Stories:** ⚪ open 1 · ✅ verified 1", text)
        self.assertIn("## [E-CORE](epics/E-CORE.md) — Core", text)
        self.assertIn("Status: 🟡 in progress", text)
        self.assertIn("| [US-0001](stories/US-0001.md) | First story | ⚪ open |", text)

    def test_hand_written_text_is_kept(self):
        self.write({"docs/01-goals/README.md": "# Goals\n\nIntro.\n\n<!-- generated:status -->\nold\n<!-- /generated -->\n"})
        render.run(project.load(self.root))
        text = (self.root / "docs/01-goals/README.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Goals\n\nIntro.\n"))
        self.assertNotIn("old", text)

    def test_project_language(self):
        self.write({"docs/PROFILE.md": "---\ndocspine: 0.1\nlanguage: de\n---\n"})
        render.run(project.load(self.root))
        self.assertIn("⚪ offen", (self.root / "docs/01-goals/README.md").read_text(encoding="utf-8"))

    def test_render_is_stable(self):
        self.write({})
        render.run(project.load(self.root))
        self.assertEqual(render.run(project.load(self.root)), [])


@req("REQ-0014")
class EpicStories(ProjectTest):
    def test_stories_region_written(self):
        self.write({})
        render.run(project.load(self.root))
        text = (self.root / "docs/01-goals/epics/E-CORE.md").read_text(encoding="utf-8")
        self.assertIn("<!-- generated:stories -->\n- [US-0001](../stories/US-0001.md) — First story\n<!-- /generated -->", text)

    def test_region_added_if_missing(self):
        self.write({"docs/01-goals/epics/E-CORE.md": "---\nid: E-CORE\ntitle: Core\n---\n\n# E-CORE\n"})
        render.run(project.load(self.root))
        text = (self.root / "docs/01-goals/epics/E-CORE.md").read_text(encoding="utf-8")
        self.assertIn("## Stories\n\n<!-- generated:stories -->", text)


@req("REQ-0015")
class SingleFile(ProjectTest):
    def test_runs_as_single_file_without_installed_packages(self):
        sys.path.insert(0, str(CLI))
        import build
        self.write({})
        with tempfile.TemporaryDirectory() as tmp:
            pyz = build.build(Path(tmp) / "docspine.pyz")
            # -I: isolated, -S: no site-packages, so a system-wide PyYAML is not visible
            cmd = [sys.executable, "-I", "-S", str(pyz), "--root", str(self.root)]
            subprocess.run(cmd + ["render"], capture_output=True, text=True, check=True)
            proc = subprocess.run(cmd + ["check"], capture_output=True, text=True)
        self.assertEqual((proc.returncode, proc.stdout.strip()), (0, "OK"), proc.stderr)

    def test_syntax_is_python_3_9(self):
        for path in sorted((CLI / "docspine").rglob("*.py")):
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path), feature_version=(3, 9))
