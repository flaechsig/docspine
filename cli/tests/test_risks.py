from __future__ import annotations

from support import STORY, ProjectTest, replace, req

from docspine import project, renumber

STORY_PATH = "docs/01-goals/stories/US-0001.md"
RISK = """\
---
id: SEC-0001
title: Import without authentication
status: open
severity: medium
---

Anyone who reaches the service can replace templates.
"""
RISK_PATH = "docs/11-risks/SEC-0001.md"
ADDRESSING = replace(STORY, "requirements: [REQ-0001]\n", "requirements: [REQ-0001]\naddresses: [SEC-0001]\n")


@req("REQ-0046")
class RiskArtifact(ProjectTest):
    def test_valid_risk(self):
        self.assertEqual(self.findings({RISK_PATH: RISK}), [])

    def test_all_prefixes(self):
        files = {f"docs/11-risks/{i}.md": replace(RISK, "SEC-0001", i) for i in ("R-0001", "SEC-0001", "TD-0001")}
        self.assertEqual(self.findings(files), [])

    def test_unknown_prefix(self):
        self.assertIn(2, self.codes({"docs/11-risks/RISK-0001.md": replace(RISK, "SEC-0001", "RISK-0001")}))

    def test_id_does_not_match_file_name(self):
        self.assertIn(2, self.codes({"docs/11-risks/SEC-0002.md": RISK}))

    def test_status_not_permitted(self):
        self.assertIn(1, self.codes({RISK_PATH: replace(RISK, "status: open", "status: fixed")}))

    def test_severity_not_permitted(self):
        self.assertIn(1, self.codes({RISK_PATH: replace(RISK, "severity: medium", "severity: mittel")}))

    def test_readme_is_not_a_risk(self):
        self.write({RISK_PATH: RISK, "docs/11-risks/README.md": "# Risks\n"})
        self.assertEqual([a.id for a in project.load(self.root).of_kind("risk")], ["SEC-0001"])

    def test_superseded_needs_successor(self):
        self.assertIn(7, self.codes({RISK_PATH: replace(RISK, "status: open", "status: superseded")}))


@req("REQ-0047")
class Addresses(ProjectTest):
    def test_existing_risk(self):
        self.assertEqual(self.findings({RISK_PATH: RISK, STORY_PATH: ADDRESSING}), [])

    def test_missing_risk(self):
        findings = self.findings({STORY_PATH: ADDRESSING})
        self.assertEqual([f.code for f in findings], [3])
        self.assertIn("SEC-0001", findings[0].message)


@req("REQ-0048")
class ClosedRisk(ProjectTest):
    CLOSED = replace(RISK, "status: open", "status: closed")

    def test_closed_with_open_story(self):
        findings = self.findings({RISK_PATH: self.CLOSED, STORY_PATH: ADDRESSING})
        self.assertEqual([(f.code, f.path) for f in findings], [(16, RISK_PATH)])

    def test_closed_with_verified_story(self):
        story = replace(ADDRESSING, "status: open", "status: verified")
        story = replace(story, "requirements: [REQ-0001]", "requirements: []\nevidence: [docs/README.md]")
        self.assertEqual(self.codes({RISK_PATH: self.CLOSED, STORY_PATH: story}), [])

    def test_closed_with_superseded_story(self):
        self.write({"docs/09-decisions/ADR-0001.md":
                    "---\nid: ADR-0001\ntitle: X\nstatus: accepted\ndate: 2026-10-09\n---\n"})
        story = replace(ADDRESSING, "status: open", "status: superseded\nsuperseded_by: ADR-0001")
        self.assertEqual(self.codes({RISK_PATH: self.CLOSED, STORY_PATH: story}), [])

    def test_open_risk_with_open_story(self):
        self.assertEqual(self.codes({RISK_PATH: RISK, STORY_PATH: ADDRESSING}), [])


@req("REQ-0049")
class RiskStoriesRegion(ProjectTest):
    def test_region_lists_story(self):
        self.findings({RISK_PATH: RISK, STORY_PATH: ADDRESSING})
        text = (self.root / RISK_PATH).read_text(encoding="utf-8")
        self.assertIn("## Stories", text)
        self.assertIn("| [US-0001](../01-goals/stories/US-0001.md) | First story | ⚪ open |", text)

    def test_region_without_stories(self):
        self.findings({RISK_PATH: RISK})
        self.assertIn("_none_", (self.root / RISK_PATH).read_text(encoding="utf-8"))

    def test_hand_edit_is_stale(self):
        self.findings({RISK_PATH: RISK, STORY_PATH: ADDRESSING})
        path = self.root / RISK_PATH
        path.write_text(path.read_text(encoding="utf-8").replace("First story", "Edited"), encoding="utf-8")
        self.assertEqual(self.codes(rendered=False), [11])


@req("REQ-0050", "REQ-0066")
class RisksOverview(ProjectTest):
    README = "docs/11-risks/README.md"

    def test_grouped_overview(self):
        files = {RISK_PATH: RISK, STORY_PATH: ADDRESSING,
                 "docs/11-risks/R-0001.md": replace(replace(RISK, "SEC-0001", "R-0001"), "severity: medium\n", ""),
                 "docs/11-risks/TD-0001.md": replace(RISK, "SEC-0001", "TD-0001")}
        self.assertEqual(self.findings(files), [])
        text = (self.root / self.README).read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Risks and technical debt"))
        groups = [text.index(h) for h in ("## Architecture risks", "## Security risks", "## Technical debt")]
        self.assertEqual(groups, sorted(groups))
        self.assertIn("| [SEC-0001](SEC-0001.md) | Import without authentication | open | medium | "
                      "[US-0001](../01-goals/stories/US-0001.md) ⚪ open |", text)
        self.assertIn("| [R-0001](R-0001.md) | Import without authentication | open | — | — |", text)

    def test_hand_written_readme_keeps_its_text(self):
        self.findings({RISK_PATH: RISK, self.README: "# Risiken\n\nEinleitung.\n"})
        text = (self.root / self.README).read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Risiken\n\nEinleitung.\n"))
        self.assertEqual(text.count("\n# "), 0)
        self.assertNotIn("# Risks and technical debt", text)
        self.assertIn("<!-- generated:risks -->", text)

    def test_no_overview_without_risks(self):
        self.findings()
        self.assertFalse((self.root / self.README).exists())

    def test_empty_group_is_left_out(self):
        self.findings({RISK_PATH: RISK})
        text = (self.root / self.README).read_text(encoding="utf-8")
        self.assertNotIn("## Architecture risks", text)


@req("REQ-0051")
class RenumberRisk(ProjectTest):
    def test_same_prefix(self):
        self.write({RISK_PATH: RISK, STORY_PATH: ADDRESSING})
        renumber.run(project.load(self.root), "SEC-0001", "SEC-0002")
        self.assertTrue((self.root / "docs/11-risks/SEC-0002.md").exists())
        self.assertIn("addresses: [SEC-0002]", (self.root / STORY_PATH).read_text(encoding="utf-8"))

    def test_other_prefix_is_refused(self):
        self.write({RISK_PATH: RISK, STORY_PATH: ADDRESSING})
        with self.assertRaises(renumber.RenumberError):
            renumber.run(project.load(self.root), "SEC-0001", "R-0001")
        self.assertTrue((self.root / RISK_PATH).exists())
        self.assertIn("addresses: [SEC-0001]", (self.root / STORY_PATH).read_text(encoding="utf-8"))
