from __future__ import annotations

import json

from support import EPIC, REQUIREMENT, STORY, ProjectTest, replace, req


class ValidProject(ProjectTest):
    def test_valid_project_has_no_findings(self):
        self.assertEqual(self.findings(), [])


@req("REQ-0001")
class Schema(ProjectTest):
    def test_missing_required_field(self):
        story = replace(STORY, "title: First story\n", "")
        findings = self.findings({"docs/01-goals/stories/US-0001.md": story})
        self.assertEqual([f.code for f in findings], [1])
        self.assertIn("'title'", findings[0].message)
        self.assertEqual(findings[0].path, "docs/01-goals/stories/US-0001.md")

    def test_value_not_permitted(self):
        story = replace(STORY, "status: open", "status: done")
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": story}), [1])

    def test_obligation_not_permitted(self):
        r = replace(REQUIREMENT, "obligation: MUST", "obligation: MUSS")
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": r}), [1])

    def test_missing_front_matter(self):
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": "no front matter\n"}), [1])

    def test_invalid_yaml(self):
        story = replace(STORY, "title: First story", "title: [unclosed")
        self.assertIn(1, self.codes({"docs/01-goals/stories/US-0001.md": story}))

    def test_values_are_read_as_text(self):
        # 0.10 stays "0.10", a date stays a string, NO stays "NO": no YAML 1.1 surprises
        adr = "---\nid: ADR-0001\ntitle: NO\nstatus: accepted\ndate: 2026-10-04\n---\n"
        self.write({"docs/01-goals/stories/US-0001.md": replace(STORY, "title: First story", "title: 0.10"),
                    "docs/09-decisions/ADR-0001.md": adr})
        from docspine import project
        proj = project.load(self.root)
        self.assertEqual(proj.by_id()["US-0001"].fm["title"], "0.10")
        self.assertEqual(proj.by_id()["ADR-0001"].fm["date"], "2026-10-04")
        self.assertEqual(proj.by_id()["ADR-0001"].fm["title"], "NO")


@req("REQ-0002")
class Ids(ProjectTest):
    def test_id_does_not_match_file_name(self):
        story = replace(STORY, "id: US-0001", "id: US-0002")
        self.assertIn(2, self.codes({"docs/01-goals/stories/US-0001.md": story}))

    def test_id_used_twice(self):
        story = replace(STORY, "id: US-0001", "id: US-0002")
        findings = self.findings({"docs/01-goals/stories/US-0002.md": STORY.replace("US-0001", "US-0002"),
                                  "docs/01-goals/stories/US-0003.md": story.replace("First", "Second")})
        self.assertIn(2, [f.code for f in findings])

    def test_id_scheme(self):
        story = replace(STORY, "id: US-0001", "id: US-1")
        self.assertIn(2, self.codes({"docs/01-goals/stories/US-1.md": story,
                                     "docs/01-goals/stories/US-0001.md": None}, base=True))


@req("REQ-0003")
class References(ProjectTest):
    def test_unknown_epic(self):
        story = replace(STORY, "epic: E-CORE", "epic: E-OTHER")
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": story}), [3])

    def test_unknown_requirement(self):
        story = replace(STORY, "[REQ-0001]", "[REQ-0001, REQ-0099]")
        findings = self.findings({"docs/01-goals/stories/US-0001.md": story})
        self.assertEqual([f.code for f in findings], [3])
        self.assertIn("REQ-0099", findings[0].message)

    def test_unknown_superseded_by(self):
        r = replace(REQUIREMENT, "status: planned", "status: superseded\nsuperseded_by: REQ-0099")
        self.assertIn(3, self.codes({"docs/01-goals/requirements/REQ-0001.md": r}))


@req("REQ-0004")
class Sources(ProjectTest):
    def test_source_not_in_profile(self):
        r = replace(REQUIREMENT, "source:\n", "source: ISO 9999\n")
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": r}), [4])

    def test_source_in_profile(self):
        r = replace(REQUIREMENT, "source:\n", "source: RFC 6749\n")
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": r}), [])


@req("REQ-0005")
class StoryProof(ProjectTest):
    def test_verified_without_requirements_and_evidence(self):
        story = replace(replace(STORY, "[REQ-0001]", "[]"), "status: open", "status: verified")
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": story}), [5])

    def test_verified_with_evidence(self):
        story = replace(replace(STORY, "[REQ-0001]", "[]"), "status: open", "status: verified\nevidence: [a.md]")
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": story, "a.md": ""}), [])


@req("REQ-0006")
class StoryRequirements(ProjectTest):
    def test_verified_story_with_planned_requirement(self):
        story = replace(STORY, "status: open", "status: verified")
        findings = self.findings({"docs/01-goals/stories/US-0001.md": story})
        self.assertEqual([f.code for f in findings], [6])
        self.assertIn("REQ-0001", findings[0].message)

    def test_verified_story_with_implemented_requirement(self):
        story = replace(STORY, "status: open", "status: verified")
        r = replace(REQUIREMENT, "status: planned", "status: implemented\nevidence: [x.py]")
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": story,
                                     "docs/01-goals/requirements/REQ-0001.md": r, "x.py": ""}), [])


@req("REQ-0007")
class Superseded(ProjectTest):
    def test_superseded_without_successor(self):
        r = replace(REQUIREMENT, "status: planned", "status: superseded")
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": r}), [7])

    def test_retired_story_without_successor(self):
        story = replace(STORY, "status: open", "status: retired")
        self.assertEqual(self.codes({"docs/01-goals/stories/US-0001.md": story}), [7])


def results(*entries):
    return json.dumps({"results": [{"req": r, "result": res, "test": "t"} for r, res in entries]})


@req("REQ-0008")
class ImplementedProof(ProjectTest):
    implemented = replace(REQUIREMENT, "status: planned", "status: implemented")

    def test_implemented_without_proof(self):
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": self.implemented}), [8])

    def test_implemented_with_passing_result(self):
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": self.implemented,
                                     "build/req-results.json": results(("REQ-0001", "passed"))}), [])

    def test_failed_result_does_not_count(self):
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": self.implemented,
                                     "build/req-results.json": results(("REQ-0001", "passed"),
                                                                       ("REQ-0001", "failed"))}), [8])

    def test_implemented_with_evidence(self):
        r = self.implemented.replace("source:\n", "source:\nevidence: [src/x.py]\n")
        self.assertEqual(self.codes({"docs/01-goals/requirements/REQ-0001.md": r, "src/x.py": ""}), [])


@req("REQ-0009")
class StatusBehindResult(ProjectTest):
    def test_planned_with_passing_result(self):
        self.assertEqual(self.codes({"a/req-results.json": results(("REQ-0001", "passed"))}), [9])

    def test_planned_with_failing_result(self):
        self.assertEqual(self.codes({"a/req-results.json": results(("REQ-0001", "failed"))}), [])


@req("REQ-0010")
class UnknownResults(ProjectTest):
    def test_result_for_unknown_requirement(self):
        findings = self.findings({"a/req-results.json": results(("REQ-0042", "passed"))})
        self.assertEqual([(f.code, f.path) for f in findings], [(10, "a/req-results.json")])

    def test_unreadable_results(self):
        self.assertEqual(self.codes({"a/req-results.json": "{not json"}), [10])


@req("REQ-0011")
class Links(ProjectTest):
    def test_broken_link(self):
        epic = EPIC + "\nSee [missing](nowhere.md).\n"
        findings = self.findings({"docs/01-goals/epics/E-CORE.md": epic})
        self.assertEqual([f.code for f in findings], [13])
        self.assertIn("nowhere.md", findings[0].message)

    def test_valid_links_and_ignored_targets(self):
        epic = EPIC + ("\n[story](../stories/US-0001.md) [anchor](#x) [web](https://example.org)"
                       " [with anchor](../stories/US-0001.md#top)\n")
        self.assertEqual(self.codes({"docs/01-goals/epics/E-CORE.md": epic}), [])

    def test_links_in_code_are_ignored(self):
        epic = EPIC + "\n```\n[x](nowhere.md)\n```\n\n1. item\n   ```md\n   [y](gone.md)\n   ```\n\n`[z](no.md)`\n"
        self.assertEqual(self.codes({"docs/01-goals/epics/E-CORE.md": epic}), [])
