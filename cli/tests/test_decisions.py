from __future__ import annotations

from support import REQUIREMENT, ProjectTest, replace, req

REQ_PATH = "docs/01-goals/requirements/REQ-0001.md"
ADR_PATH = "docs/09-decisions/ADR-0001.md"


def adr(status: str = "accepted", extra: str = "", adr_id: str = "ADR-0001") -> str:
    return f"---\nid: {adr_id}\ntitle: A decision\nstatus: {status}\ndate: 2026-10-09\n{extra}---\n\n## Kontext\n"


def requirement(status: str = "planned", decisions: str = "[ADR-0001]") -> str:
    r = replace(REQUIREMENT, "status: planned", f"status: {status}")
    return replace(r, "source:\n", f"source:\ndecisions: {decisions}\n")


@req("REQ-0056")
class DecisionReference(ProjectTest):
    def test_existing_decision(self):
        self.assertEqual(self.findings({ADR_PATH: adr(), REQ_PATH: requirement()}), [])

    def test_missing_decision(self):
        findings = self.findings({REQ_PATH: requirement()})
        self.assertEqual([(f.code, f.path) for f in findings], [(3, REQ_PATH)])
        self.assertIn("ADR-0001", findings[0].message)

    def test_must_be_a_list(self):
        self.assertIn(1, self.codes({ADR_PATH: adr(), REQ_PATH: requirement(decisions="ADR-0001")}))


@req("REQ-0057")
class OpenDecision(ProjectTest):
    def test_planned_against_proposed(self):
        findings = self.findings({ADR_PATH: adr("proposed"), REQ_PATH: requirement("planned")})
        self.assertEqual([(f.code, f.path) for f in findings], [(18, REQ_PATH)])

    def test_planned_against_rejected(self):
        self.assertEqual(self.codes({ADR_PATH: adr("rejected"), REQ_PATH: requirement("planned")}), [18])

    def test_proposed_against_proposed_is_fine(self):
        self.assertEqual(self.codes({ADR_PATH: adr("proposed"), REQ_PATH: requirement("proposed")}), [])

    def test_planned_against_accepted_is_fine(self):
        self.assertEqual(self.codes({ADR_PATH: adr("accepted"), REQ_PATH: requirement("planned")}), [])

    def test_planned_against_superseded_is_fine(self):
        files = {ADR_PATH: adr("superseded", "superseded_by: ADR-0002\n"),
                 "docs/09-decisions/ADR-0002.md": adr("accepted", "supersedes: ADR-0001\n", "ADR-0002"),
                 REQ_PATH: requirement("planned")}
        self.assertEqual(self.codes(files), [])


@req("REQ-0058")
class RequiresField(ProjectTest):
    def test_requires_is_reported(self):
        findings = self.findings({ADR_PATH: adr(extra="requires: [REQ-0001]\n")})
        self.assertEqual([(f.code, f.path) for f in findings], [(1, ADR_PATH)])
        self.assertIn("decisions", findings[0].message)


@req("REQ-0060")
class AdrRequirementsRegion(ProjectTest):
    def test_region_lists_requirement(self):
        self.findings({ADR_PATH: adr(), REQ_PATH: requirement()})
        text = (self.root / ADR_PATH).read_text(encoding="utf-8")
        self.assertIn("## Requirements", text)
        self.assertIn("| [REQ-0001](../01-goals/requirements/REQ-0001.md) | The system shall do something. | planned |", text)

    def test_no_region_without_requirements(self):
        self.findings({ADR_PATH: adr()})
        self.assertNotIn("generated:requirements", (self.root / ADR_PATH).read_text(encoding="utf-8"))

    def test_hand_edit_is_stale(self):
        self.findings({ADR_PATH: adr(), REQ_PATH: requirement()})
        path = self.root / ADR_PATH
        path.write_text(path.read_text(encoding="utf-8").replace("| planned |", "| implemented |"), encoding="utf-8")
        self.assertEqual(self.codes(rendered=False), [11])


@req("REQ-0061")
class SupersedingDecision(ProjectTest):
    def files(self, old_status: str) -> dict:
        return {ADR_PATH: adr(old_status),
                "docs/09-decisions/ADR-0002.md": adr("proposed", "supersedes: ADR-0001\n", "ADR-0002")}

    def test_supersedes_accepted(self):
        self.assertEqual(self.codes(self.files("accepted")), [])

    def test_supersedes_proposed(self):
        findings = self.findings(self.files("proposed"))
        self.assertEqual([(f.code, f.path) for f in findings], [(19, "docs/09-decisions/ADR-0002.md")])

    def test_supersedes_rejected(self):
        self.assertEqual(self.codes(self.files("rejected")), [19])
