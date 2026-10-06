---
title: Kommandozeile
path: [cli/docspine/__main__.py]
---

# Kommandozeile

**Verantwortung.** Nimmt die Befehle `check`, `render`, `renumber`, `diagram` und
`version` entgegen, ruft den zuständigen Baustein auf und setzt den Exit-Code: 0 bei
Erfolg, 1 bei Fehlern der Prüfung, 2 bei falscher Bedienung oder fehlendem Projekt.
_(confidence: verified — cli/docspine/__main__.py, REQ-0012)_

**Schnittstelle.** `python3 .docspine/docspine.pyz [--root DIR] <befehl>`. Die Option
`--without-tests` lässt die Prüfungen weg, die Testergebnisse brauchen, `--now` lässt
`version` sofort nachsehen. _(confidence: verified — cli/docspine/__main__.py, REQ-0033)_

**Innen.** `version` läuft ohne das Laden des Projekts, weil es nur die installierte
Version braucht. Alle anderen Befehle laden zuerst das Projekt
([Projekt laden](projekt-laden.md)). _(confidence: verified — cli/docspine/__main__.py)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0012](../01-goals/requirements/REQ-0012.md) WHEN check finds at least one error, the checker shall exit with a non-zero status.
- [REQ-0033](../01-goals/requirements/REQ-0033.md) WHERE check runs with --without-tests, the checker shall skip the checks that need test results (errors 8, 9 and 10) and say so in its result.
- [REQ-0035](../01-goals/requirements/REQ-0035.md) IF renumber is given an ID that does not exist, a new ID that already exists, or two IDs of different kinds, THEN the checker shall change nothing and exit with a non-zero status.
- [REQ-0036](../01-goals/requirements/REQ-0036.md) WHEN renumber has run, the checker shall list the files outside docs/ that still contain the old ID, without changing them.
- [REQ-0040](../01-goals/requirements/REQ-0040.md) WHEN the diagram command runs for a DOT or PlantUML source, the CLI shall render the source to an SVG next to it with Graphviz or PlantUML and record the checksum of the source in the SVG.
<!-- /generated -->
