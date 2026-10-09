---
title: Erzeugung
path: [cli/docspine/render.py, cli/docspine/text.py]
---

# Erzeugung

**Verantwortung.** Der Befehl `render`: schreibt die generierten Bereiche (Standard 4)
und die Sicht `10-quality.md`. _(confidence: verified — cli/docspine/render.py)_

**Innen.** `plan()` berechnet den vollständigen neuen Text jeder Datei, die `render`
verwaltet. `run()` schreibt nur die Dateien, die sich unterscheiden; die
[Prüfung](pruefung.md) nutzt denselben Plan. _(confidence: verified —
cli/docspine/render.py, REQ-0016)_

**Sprache.** Überschriften und feste Texte der generierten Bereiche kommen aus einer
Tabelle je Projektsprache ([Sprachen](../08-concepts/sprachen.md)). Statements erscheinen
so, wie sie geschrieben sind. _(confidence: verified — cli/docspine/text.py)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0013](../01-goals/requirements/REQ-0013.md) WHEN render runs, the checker shall write the status region of 01-goals/README.md with every epic, its derived status and the status of each of its stories.
- [REQ-0014](../01-goals/requirements/REQ-0014.md) WHEN render runs, the checker shall write the stories region of every epic.
- [REQ-0016](../01-goals/requirements/REQ-0016.md) IF a generated region or view differs from what render would write, THEN the checker shall report error 11.
- [REQ-0019](../01-goals/requirements/REQ-0019.md) WHEN render runs, the checker shall write the requirements region of every story that has requirements, with obligation, statement and status of each.
- [REQ-0022](../01-goals/requirements/REQ-0022.md) WHEN render runs, the checker shall write the scenarios region of every story that a runtime scenario refers to.
- [REQ-0024](../01-goals/requirements/REQ-0024.md) WHEN render runs and quality requirements exist, the checker shall write docs/10-quality.md listing them with statement, status and verification.
- [REQ-0028](../01-goals/requirements/REQ-0028.md) WHEN render runs, the checker shall write into the status region of docs/01-goals/README.md the counts per status, the open questions, the contradictions, the chapters without content and the partly filled chapters, without searching generated regions.
- [REQ-0037](../01-goals/requirements/REQ-0037.md) WHEN render runs, the checker shall link the count of decisions in the status region of docs/01-goals/README.md to the decisions folder and list every decision with status proposed under open decisions.
- [REQ-0045](../01-goals/requirements/REQ-0045.md) WHEN render runs, the checker shall write the realized region of every building block with the requirements whose evidence lies under the block's path, leaving out requirements that are superseded or rejected.
- [REQ-0049](../01-goals/requirements/REQ-0049.md) WHEN render runs, the checker shall write the stories region of every risk with the stories that list it in addresses and their status.
- [REQ-0050](../01-goals/requirements/REQ-0050.md) WHEN render runs and the project has risks, the checker shall write the risks region of docs/11-risks/README.md with every risk, grouped into architecture risks, security risks and technical debt.
- [REQ-0052](../01-goals/requirements/REQ-0052.md) WHEN a story has an acceptance section, the checker shall report error 17 for every top-level list item in it that names no requirement ID and does not start with UNKNOWN.
- [REQ-0059](../01-goals/requirements/REQ-0059.md) WHEN render runs, the checker shall write the context region of every requirement with its stories, their epics and the ADRs listed in its decisions.
- [REQ-0060](../01-goals/requirements/REQ-0060.md) WHEN render runs, the checker shall write the requirements region of every ADR with the requirements that list it in decisions and their status.
<!-- /generated -->
