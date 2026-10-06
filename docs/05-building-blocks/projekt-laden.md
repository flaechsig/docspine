---
title: Projekt laden
path: [cli/docspine/project.py, cli/docspine/frontmatter.py, cli/docspine/_vendor/]
---

# Projekt laden

**Verantwortung.** Liest Profil, alle Artefakte unter `docs/` und die Testergebnisse in
ein gemeinsames Modell, auf dem Prüfung und Erzeugung arbeiten. Probleme beim Lesen
werden als Befund gesammelt, nicht als Abbruch. _(confidence: verified —
cli/docspine/project.py)_

**Frontmatter.** Alle Werte werden als Text gelesen. YAML 1.1 würde sonst `0.1` zur Zahl,
`2026-10-03` zum Datum und `NO` zu `False` machen. PyYAML liegt eingepackt unter
`_vendor/`, damit keine Installation nötig ist. _(confidence: verified —
cli/docspine/frontmatter.py, REQ-0015)_

**Testergebnisse.** Zwei Quellen, beide in dasselbe Modell:
- `req-results.json` (Standard 8.1), überall im Repository gesucht
- JUnit-XML-Berichte: aus den Orten in `test_reports` des Profils oder, wenn dort nichts
  steht, aus jeder XML-Datei mit `<testsuite`. `docs/`, `.docspine/`, `.agents/` und
  `.claude/` werden dabei übersprungen. Die Requirement-ID steht im Testnamen.

_(confidence: verified — cli/docspine/project.py, REQ-0029, REQ-0030, REQ-0031, REQ-0038)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0001](../01-goals/requirements/REQ-0001.md) IF a required front-matter field is missing or holds a value that is not permitted, THEN the checker shall report error 1 with file and field.
- [REQ-0008](../01-goals/requirements/REQ-0008.md) IF a requirement is implemented without a passing test result and without evidence, THEN the checker shall report error 8.
- [REQ-0010](../01-goals/requirements/REQ-0010.md) IF a test result names a requirement that does not exist, THEN the checker shall report error 10.
- [REQ-0015](../01-goals/requirements/REQ-0015.md) The checker shall run as a single file with Python 3.9 or later without installing further packages.
- [REQ-0029](../01-goals/requirements/REQ-0029.md) WHEN the profile names locations in test_reports, the checker shall read every JUnit XML report there and count each test case for every requirement ID in its name or class name.
- [REQ-0030](../01-goals/requirements/REQ-0030.md) IF a test case in a JUnit XML report contains a failure or an error, THEN the checker shall count it as failed for its requirements, and IF it contains skipped, THEN as skipped.
- [REQ-0031](../01-goals/requirements/REQ-0031.md) IF a location in test_reports does not exist or a report there cannot be parsed, THEN the checker shall report error 10.
- [REQ-0038](../01-goals/requirements/REQ-0038.md) WHERE the profile names no test_reports, the checker shall read every XML file in the repository whose root is a test suite, outside .git, docs, .docspine and the skill folders.
<!-- /generated -->
