---
title: Prüfung
path: [cli/docspine/check.py]
---

# Prüfung

**Verantwortung.** Der Befehl `check`: eine Funktion je Fehlerklasse aus Standard 11,
jede liefert Befunde mit Nummer, Datei und Text. Ohne Testergebnisse entfallen die
Fehler 8 bis 10. _(confidence: verified — cli/docspine/check.py, REQ-0033)_

**Innen.** Für Fehler 11 (veraltete generierte Bereiche) rechnet die Prüfung nicht selbst
nach, sondern fragt die [Erzeugung](erzeugung.md), was sie schreiben würde, und
vergleicht. Für Fehler 12 fragt sie den Baustein [Diagramme](diagramme.md). So können
Prüfung und Erzeugung nicht auseinanderlaufen ([Generierte Bereiche](../08-concepts/generierte-bereiche.md)).
_(confidence: verified — cli/docspine/check.py, REQ-0016, REQ-0039)_

Links und Beispiele in Codeblöcken und Code-Spans gelten nicht als Inhalt und werden
nicht geprüft. _(confidence: verified — cli/docspine/text.py, REQ-0011)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0001](../01-goals/requirements/REQ-0001.md) IF a required front-matter field is missing or holds a value that is not permitted, THEN the checker shall report error 1 with file and field.
- [REQ-0002](../01-goals/requirements/REQ-0002.md) IF an artifact's id does not match its file name or is used by more than one file, THEN the checker shall report error 2.
- [REQ-0003](../01-goals/requirements/REQ-0003.md) IF a front-matter reference names an ID that does not exist, THEN the checker shall report error 3.
- [REQ-0004](../01-goals/requirements/REQ-0004.md) IF a requirement's source is not listed in the profile, THEN the checker shall report error 4.
- [REQ-0005](../01-goals/requirements/REQ-0005.md) IF a story is verified without requirements and without evidence, THEN the checker shall report error 5.
- [REQ-0006](../01-goals/requirements/REQ-0006.md) IF a verified story refers to a requirement that is not implemented, THEN the checker shall report error 6.
- [REQ-0007](../01-goals/requirements/REQ-0007.md) IF an artifact is superseded or retired without superseded_by, THEN the checker shall report error 7.
- [REQ-0009](../01-goals/requirements/REQ-0009.md) IF a requirement is planned or proposed and a passing test result exists, THEN the checker shall report error 9.
- [REQ-0010](../01-goals/requirements/REQ-0010.md) IF a test result names a requirement that does not exist, THEN the checker shall report error 10.
- [REQ-0011](../01-goals/requirements/REQ-0011.md) IF a relative Markdown link outside code blocks points to a file that does not exist, THEN the checker shall report error 13.
- [REQ-0016](../01-goals/requirements/REQ-0016.md) IF a generated region or view differs from what render would write, THEN the checker shall report error 11.
- [REQ-0018](../01-goals/requirements/REQ-0018.md) IF an evidence path does not exist, THEN the checker shall report error 15.
- [REQ-0027](../01-goals/requirements/REQ-0027.md) IF docs/README.md was translated from a docspine version other than the one named in .docspine/STANDARD.md, or either file names none, THEN the checker shall report error 14.
- [REQ-0032](../01-goals/requirements/REQ-0032.md) IF a requirement is implemented without a passing test result and without both evidence and verification, THEN the checker shall report error 8.
- [REQ-0033](../01-goals/requirements/REQ-0033.md) WHERE check runs with --without-tests, the checker shall skip the checks that need test results (errors 8, 9 and 10) and say so in its result.
- [REQ-0039](../01-goals/requirements/REQ-0039.md) IF a DOT or PlantUML source under docs, outside docs/legacy, has no SVG next to it, or its SVG does not carry the checksum of the current source, THEN the checker shall report error 12.
- [REQ-0046](../01-goals/requirements/REQ-0046.md) WHEN the checker loads a project, it shall read every Markdown file in docs/11-risks/ except README.md as a risk, and report error 1 or 2 if its id is not of the form R-NNNN, SEC-NNNN or TD-NNNN matching the file name, or its status is not open, accepted, closed or superseded.
- [REQ-0047](../01-goals/requirements/REQ-0047.md) IF a story lists an ID in addresses that is not a risk of the project, THEN the checker shall report error 3.
- [REQ-0048](../01-goals/requirements/REQ-0048.md) IF a risk has the status closed and a story that lists it in addresses is neither verified nor superseded, THEN the checker shall report error 16.
- [REQ-0053](../01-goals/requirements/REQ-0053.md) IF an item of a story's acceptance section names a requirement ID that does not exist, THEN the checker shall report error 3.
- [REQ-0055](../01-goals/requirements/REQ-0055.md) IF a test result names a story that does not exist, THEN the checker shall report error 10.
- [REQ-0056](../01-goals/requirements/REQ-0056.md) IF a requirement lists an ID in decisions that is not an ADR of the project, THEN the checker shall report error 3.
- [REQ-0057](../01-goals/requirements/REQ-0057.md) IF a requirement is planned or implemented and lists in decisions an ADR that is proposed or rejected, THEN the checker shall report error 18.
- [REQ-0058](../01-goals/requirements/REQ-0058.md) IF an ADR has the field requires, THEN the checker shall report error 1 and name decisions in the requirements as its replacement.
- [REQ-0061](../01-goals/requirements/REQ-0061.md) IF an ADR lists in supersedes an ADR that is neither accepted nor superseded, THEN the checker shall report error 19.
<!-- /generated -->
