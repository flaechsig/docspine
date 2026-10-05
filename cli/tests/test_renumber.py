from __future__ import annotations

from support import REQUIREMENT, STORY, ProjectTest, req

from docspine import check, project, render, renumber
from test_cli import run_main

REQ = "docs/01-goals/requirements/REQ-0001.md"


class RenumberTest(ProjectTest):
    def renumber(self, old, new, files=None):
        self.write(files or {})
        render.run(project.load(self.root))
        return renumber.run(project.load(self.root), old, new)

    def read(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")


@req("REQ-0034")
class Renumbers(RenumberTest):
    def test_file_id_and_references(self):
        changed, _ = self.renumber("REQ-0001", "REQ-0007")
        self.assertFalse((self.root / REQ).exists())
        new = self.read("docs/01-goals/requirements/REQ-0007.md")
        self.assertIn("id: REQ-0007", new)
        self.assertIn("## REQ-0007 — Something", new)
        self.assertIn("requirements: [REQ-0007]", self.read("docs/01-goals/stories/US-0001.md"))
        self.assertIn("docs/01-goals/stories/US-0001.md", changed)

    def test_result_passes_the_check(self):
        self.renumber("REQ-0001", "REQ-0007")
        render.run(project.load(self.root))
        self.assertEqual(check.run(project.load(self.root)), [])

    def test_whole_ids_only(self):
        other = REQUIREMENT.replace("REQ-0001", "REQ-0010")
        story = STORY.replace("[REQ-0001]", "[REQ-0001, REQ-0010]")
        self.renumber("REQ-0001", "REQ-0007", {"docs/01-goals/requirements/REQ-0010.md": other,
                                              "docs/01-goals/stories/US-0001.md": story})
        self.assertIn("requirements: [REQ-0007, REQ-0010]", self.read("docs/01-goals/stories/US-0001.md"))
        self.assertIn("id: REQ-0010", self.read("docs/01-goals/requirements/REQ-0010.md"))

    def test_story(self):
        self.renumber("US-0001", "US-0004")
        self.assertIn("id: US-0004", self.read("docs/01-goals/stories/US-0004.md"))


@req("REQ-0035")
class Refuses(RenumberTest):
    def test_old_missing(self):
        with self.assertRaises(renumber.RenumberError):
            self.renumber("REQ-0009", "REQ-0010")

    def test_new_exists(self):
        other = REQUIREMENT.replace("REQ-0001", "REQ-0002")
        with self.assertRaises(renumber.RenumberError):
            self.renumber("REQ-0001", "REQ-0002", {"docs/01-goals/requirements/REQ-0002.md": other})

    def test_different_kinds(self):
        with self.assertRaises(renumber.RenumberError):
            self.renumber("REQ-0001", "US-0009")

    def test_cli_exit_code(self):
        self.write({})
        code, _, err = run_main("--root", str(self.root), "renumber", "REQ-0009", "REQ-0010")
        self.assertEqual(code, 2)
        self.assertIn("does not exist", err)


@req("REQ-0036")
class ReportsElsewhere(RenumberTest):
    def test_test_names_are_reported_not_changed(self):
        test = 'class T { @DisplayName("REQ-0001: prints") void t() {} }\n'
        _, elsewhere = self.renumber("REQ-0001", "REQ-0007", {"src/test/java/T.java": test})
        self.assertEqual(elsewhere, ["src/test/java/T.java"])
        self.assertEqual(self.read("src/test/java/T.java"), test)

    def test_cli_output(self):
        self.write({"src/test/java/T.java": '@DisplayName("REQ-0001: x")\n'})
        code, out, _ = run_main("--root", str(self.root), "renumber", "REQ-0001", "REQ-0007")
        self.assertEqual(code, 0)
        self.assertIn("adjust by hand: src/test/java/T.java", out)
