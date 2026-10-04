from __future__ import annotations

from support import EPIC, README, REQUIREMENT, STANDARD, STORY, VALID, ProjectTest, replace, req

from docspine import project, render

STORY_PATH = "docs/01-goals/stories/US-0001.md"
REQ_PATH = "docs/01-goals/requirements/REQ-0001.md"


class RenderTest(ProjectTest):
    def render(self, files=None):
        self.write(files or {})
        render.run(project.load(self.root))

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")


@req("REQ-0016")
class StaleRegions(RenderTest):
    def test_unrendered_project_is_stale(self):
        findings = self.findings(rendered=False)
        self.assertEqual({f.code for f in findings}, {11})
        self.assertIn("docs/STATUS.md", [f.path for f in findings])

    def test_hand_edit_in_region_is_stale(self):
        self.render()
        path = self.root / STORY_PATH
        path.write_text(path.read_text(encoding="utf-8").replace("The system shall do something.", "edited"),
                        encoding="utf-8")
        findings = self.findings(rendered=False, base=False)
        self.assertEqual([(f.code, f.path) for f in findings], [(11, STORY_PATH)])

    def test_rendered_project_is_not_stale(self):
        self.assertEqual(self.codes(), [])


@req("REQ-0017")
class ReadmeVersion(ProjectTest):
    def test_missing_readme(self):
        files = {k: v for k, v in VALID.items() if k != "docs/README.md"}
        self.assertEqual(self.codes(files, base=False), [14])

    def test_other_version(self):
        self.assertEqual(self.codes({"docs/README.md": README.replace("docspine 0.1", "docspine 0.2")}), [14])

    def test_no_version_line(self):
        self.assertEqual(self.codes({"docs/README.md": "# Documentation\n"}), [14])

    @req("REQ-0026")
    def test_standard_newer_than_profile(self):
        findings = self.findings({".docspine/STANDARD.md": STANDARD.replace("docspine 0.1", "docspine 0.2")})
        self.assertEqual([(f.code, f.path) for f in findings], [(14, ".docspine/STANDARD.md")])
        self.assertIn("spine-init", findings[0].message)


@req("REQ-0018")
class EvidencePaths(ProjectTest):
    def test_missing_evidence_path(self):
        r = replace(REQUIREMENT, "source:\n", "source:\nevidence: [src/gone.py]\n")
        findings = self.findings({REQ_PATH: r})
        self.assertEqual([f.code for f in findings], [15])
        self.assertIn("src/gone.py", findings[0].message)

    def test_existing_evidence_path(self):
        r = replace(REQUIREMENT, "source:\n", "source:\nevidence: [src/here.py]\n")
        self.assertEqual(self.codes({REQ_PATH: r, "src/here.py": ""}), [])


@req("REQ-0019")
class StoryRequirements(RenderTest):
    def test_requirements_region(self):
        self.render()
        text = self.read(STORY_PATH)
        self.assertIn("<!-- generated:requirements -->", text)
        self.assertIn("| [REQ-0001](../requirements/REQ-0001.md) | MUST | The system shall do something. | planned |",
                      text)

    def test_project_language(self):
        self.render({".docspine/PROFILE.md": "---\ndocspine: 0.1\nlanguage: de\n---\n"})
        self.assertIn("| MUSS | The system shall do something. | geplant |", self.read(STORY_PATH))

    def test_no_region_without_requirements(self):
        self.render({STORY_PATH: replace(STORY, "[REQ-0001]", "[]")})
        self.assertNotIn("generated:requirements", self.read(STORY_PATH))


@req("REQ-0020")
class RequirementContext(RenderTest):
    def test_context_region(self):
        self.render()
        self.assertIn("**Context:** Story [US-0001](../stories/US-0001.md) — First story"
                      " · Epic [E-CORE](../epics/E-CORE.md) — Core", self.read(REQ_PATH))

    def test_required_by_adr(self):
        adr = ("---\nid: ADR-0001\ntitle: A decision\nstatus: accepted\ndate: 2026-10-04\n"
               "requires: [REQ-0001]\n---\n\n## Kontext\n")
        self.render({"docs/09-decisions/ADR-0001.md": adr})
        self.assertIn("required by: [ADR-0001](../../09-decisions/ADR-0001.md)", self.read(REQ_PATH))


@req("REQ-0021")
class BlockRequirements(RenderTest):
    BLOCK = "docs/05-building-blocks/orders.md"

    def test_realized_region(self):
        r = replace(REQUIREMENT, "source:\n", "source:\nevidence: [src/orders/service.py]\n")
        other = replace(r, "src/orders/service.py", "src/billing/x.py").replace("REQ-0001", "REQ-0002")
        block = "---\ntitle: Orders\npath: [src/orders]\n---\n\n# Orders\n"
        self.render({REQ_PATH: r, "docs/01-goals/requirements/REQ-0002.md": other, self.BLOCK: block})
        text = self.read(self.BLOCK)
        self.assertIn("- [REQ-0001](../01-goals/requirements/REQ-0001.md) The system shall do something.", text)
        self.assertNotIn("REQ-0002", text)

    def test_path_prefix_is_not_enough(self):
        r = replace(REQUIREMENT, "source:\n", "source:\nevidence: [src/orders-old/x.py]\n")
        self.render({REQ_PATH: r, self.BLOCK: "---\ntitle: Orders\npath: src/orders\n---\n"})
        self.assertNotIn("REQ-0001", self.read(self.BLOCK))


@req("REQ-0022")
class StoryScenarios(RenderTest):
    def test_scenarios_region(self):
        scenario = "---\ntitle: Checkout\nstories: [US-0001]\n---\n\n# Checkout\n"
        self.render({"docs/06-runtime/checkout.md": scenario})
        self.assertIn("<!-- generated:scenarios -->\n- [Checkout](../../06-runtime/checkout.md)\n",
                      self.read(STORY_PATH))

    def test_no_region_without_scenarios(self):
        self.render()
        self.assertNotIn("generated:scenarios", self.read(STORY_PATH))


@req("REQ-0023")
class StatusView(RenderTest):
    def test_counts_and_missing_chapters(self):
        self.render()
        text = self.read("docs/STATUS.md")
        self.assertIn("| Stories | ⚪ open 1 |", text)
        self.assertIn("| Requirements | planned 1 |", text)
        self.assertIn("- 03-context", text)
        self.assertNotIn("- 01-goals", text)

    def test_open_questions_and_contradictions(self):
        epic = EPIC + ("\n- UNKNOWN — open question: who pays\n  for it?\n"
                       "\nThe rule says `UNKNOWN` is allowed.\n"
                       "\n> [!CAUTION]\n> Docs say X, code does Y. (contradiction)\n")
        self.render({"docs/01-goals/epics/E-CORE.md": epic})
        text = self.read("docs/STATUS.md")
        self.assertIn("01-goals/epics/E-CORE.md): UNKNOWN — open question: who pays for it?", text)
        self.assertEqual(text.count("UNKNOWN"), 1)
        self.assertIn("): Docs say X, code does Y. (contradiction)", text)

    def test_partial_chapter(self):
        self.render({"docs/03-context.md": "---\narc42_status: PARTIAL\n---\n\n# Context\n"})
        text = self.read("docs/STATUS.md")
        self.assertIn("## Partly filled chapters\n\n- 03-context", text)


@req("REQ-0024")
class QualityChapter(RenderTest):
    def test_quality_chapter(self):
        r = replace(REQUIREMENT, "status: planned", "status: planned\ncategory: quality\nverification: Load test.")
        self.render({REQ_PATH: r})
        text = self.read("docs/10-quality.md")
        self.assertIn("| [REQ-0001](01-goals/requirements/REQ-0001.md) | The system shall do something. "
                      "| planned | Load test. |", text)
        self.assertNotIn("- 10-quality", self.read("docs/STATUS.md"))

    def test_no_chapter_without_quality_requirements(self):
        self.render()
        self.assertFalse((self.root / "docs/10-quality.md").exists())
