# Nachweis über Testergebnisse

**Problem.** Ob ein Requirement umgesetzt ist, soll nicht von einer Behauptung abhängen,
sondern von einem Test, der läuft (ADR-0005, Standard 8).

**Lösung.** Testergebnisse sind die einzige Schnittstelle zwischen Projekt und
Prüfwerkzeug (ADR-0013). docspine bindet keine Test-Frameworks ein, sondern liest
Ergebnisse in zwei Formen:

| Form | Woher | Wie die ID zugeordnet wird |
|---|---|---|
| JUnit-XML-Bericht | fast jedes Test-Framework schreibt ihn | `REQ-NNNN` im Namen des Testfalls (ADR-0018) |
| `req-results.json` | eigenes Skript, wenn es keine JUnit-Berichte gibt | ein Eintrag je Requirement und Test |

_(confidence: verified — cli/docspine/project.py, REQ-0029, REQ-0030, REQ-0038)_

**docspine selbst** nutzt die zweite Form: Die Tests in `cli/tests/` tragen ihre
Requirements mit dem Dekorator `@req`, und `cli/run_tests.py` schreibt daraus
`cli/req-results.json`. _(confidence: verified — cli/run_tests.py, cli/tests/support.py)_

**Ohne Tests.** Ein Requirement, das sich nicht automatisch testen lässt, belegt man von
Hand mit `evidence` und `verification` (Standard 8.1). Wer nur die Doku prüfen will,
lässt mit `--without-tests` die Fehler 8 bis 10 weg. _(confidence: verified —
cli/docspine/check.py, REQ-0032, REQ-0033)_
