from __future__ import annotations

import json

from support import REQUIREMENT, STORY, ProjectTest, replace, req

from docspine import project

STORY_PATH = "docs/01-goals/stories/US-0001.md"


def with_acceptance(*items: str, heading: str = "## Acceptance") -> str:
    return STORY + "\n" + heading + "\n\n" + "\n".join(items) + "\n"


@req("REQ-0052")
class AcceptanceItems(ProjectTest):
    def test_every_item_with_requirement(self):
        story = with_acceptance("- The order shows up in the list (REQ-0001).",
                                "- UNKNOWN — open question: who sees cancelled orders?")
        self.assertEqual(self.findings({STORY_PATH: story}), [])

    def test_item_without_requirement(self):
        story = with_acceptance("- The order shows up in the list (REQ-0001).",
                                "- The customer gets an e-mail.")
        findings = self.findings({STORY_PATH: story})
        self.assertEqual([(f.code, f.path) for f in findings], [(17, STORY_PATH)])
        self.assertIn("e-mail", findings[0].message)

    def test_continuation_line_counts(self):
        story = with_acceptance("- The order shows up in the list",
                                "  of open orders (REQ-0001).")
        self.assertEqual(self.codes({STORY_PATH: story}), [])

    def test_numbered_items(self):
        story = with_acceptance("1. Shows up (REQ-0001).", "2. Mails the customer.")
        self.assertEqual(self.codes({STORY_PATH: story}), [17])

    def test_requirement_in_code_span_counts(self):
        self.assertEqual(self.codes({STORY_PATH: with_acceptance("- Shows up (`REQ-0001`).")}), [])

    def test_section_in_project_language(self):
        profile = "---\nlanguage: de\n---\n"
        story = with_acceptance("- Kunde bekommt eine Mail.", heading="## Akzeptanz")
        self.assertEqual(self.codes({STORY_PATH: story, ".docspine/PROFILE.md": profile}), [17])

    def test_story_without_section_is_valid(self):
        self.assertEqual(self.findings(), [])

    def test_other_sections_are_not_checked(self):
        story = with_acceptance("- Shows up (REQ-0001).") + "\n## Notes\n\n- anything at all\n"
        self.assertEqual(self.codes({STORY_PATH: story}), [])

    def test_list_in_code_block_is_not_an_item(self):
        story = with_acceptance("- Shows up (REQ-0001).", "", "```", "- not an item", "```")
        self.assertEqual(self.codes({STORY_PATH: story}), [])

    def test_open_question_is_listed(self):
        self.findings({STORY_PATH: with_acceptance("- UNKNOWN — open question: who is notified?")})
        text = (self.root / "docs/01-goals/README.md").read_text(encoding="utf-8")
        self.assertIn("who is notified?", text)


@req("REQ-0053")
class AcceptanceReferences(ProjectTest):
    def test_unknown_requirement(self):
        findings = self.findings({STORY_PATH: with_acceptance("- Shows up (REQ-0009).")})
        self.assertEqual([f.code for f in findings], [3])
        self.assertIn("REQ-0009", findings[0].message)

    def test_requirement_of_another_story_is_allowed(self):
        other = replace(STORY, "US-0001", "US-0002").replace("requirements: [REQ-0001]", "requirements: []")
        story = replace(with_acceptance("- Shows up (REQ-0001)."), "requirements: [REQ-0001]", "requirements: []")
        self.assertEqual(self.codes({STORY_PATH: story, "docs/01-goals/stories/US-0002.md": other}), [])


REPORT = """<testsuite name="e2e">
  <testcase classname="OrderFlow" name="{name}">{body}</testcase>
</testsuite>
"""


@req("REQ-0054")
class AcceptanceTests(ProjectTest):
    def report(self, name: str, failed: bool = False):
        body = "<failure message='x'/>" if failed else ""
        return {"e2e/report.xml": REPORT.format(name=name, body=body)}

    def test_story_test_does_not_prove_requirement(self):
        files = self.report("US-0001 REQ-0001: order flow")
        self.write(files)
        proj = project.load(self.root)
        self.assertEqual(proj.results, [])
        self.assertEqual([(a.story, a.result) for a in proj.acceptance], [("US-0001", "passed")])

    def test_failed_story_test_does_not_break_requirement(self):
        r = replace(REQUIREMENT, "status: planned", "status: implemented")
        files = self.report("US-0001 REQ-0001: order flow", failed=True)
        files.update({"docs/01-goals/requirements/REQ-0001.md": r,
                      "req-results.json": json.dumps({"results": [{"req": "REQ-0001", "result": "passed"}]})})
        self.assertEqual(self.codes(files), [])

    def test_failed_story_test_is_no_error(self):
        self.assertEqual(self.codes(self.report("US-0001: order flow", failed=True)), [])

    def test_story_entry_in_results_file(self):
        self.write({"req-results.json": json.dumps({"results": [{"story": "US-0001", "result": "failed"}]})})
        proj = project.load(self.root)
        self.assertEqual(proj.results, [])
        self.assertEqual([a.story for a in proj.acceptance], ["US-0001"])


@req("REQ-0055")
class UnknownStoryResult(ProjectTest):
    def test_unknown_story_in_report(self):
        files = {"e2e/report.xml": REPORT.format(name="US-0009: order flow", body="")}
        findings = self.findings(files)
        self.assertEqual([(f.code, f.path) for f in findings], [(10, "e2e/report.xml")])
        self.assertIn("US-0009", findings[0].message)

    def test_unknown_story_in_results_file(self):
        files = {"req-results.json": json.dumps({"results": [{"story": "US-0009", "result": "passed"}]})}
        self.assertEqual(self.codes(files), [10])

