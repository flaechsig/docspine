# Risiken und technische Schulden

| Risiko | Wirkung | Umgang |
|---|---|---|
| Claude Code liest `.agents/skills/` nicht von selbst | Ohne den symbolischen Link `.claude/skills` findet Claude die Skills nicht. Unter Windows braucht der Link `core.symlinks=true` | Die Auslieferung legt den Link an. Liest Claude Code den Ordner künftig selbst, entfällt er (ADR-0009) |
| Skills sind Anweisungen an ein Sprachmodell | Ihr Verhalten ist nicht deterministisch und wird nicht automatisch getestet | Regeln stehen im Standard und werden von der Prüfung durchgesetzt; Skills führen nur. Einmal belegt durch den Kaltstart-Test (US-0011) |
| Abhängigkeit von GitHub | Installation, Update und `version` brauchen den Zweig `dist` auf GitHub | Die Prüfung selbst läuft ohne Netz; `version` endet ohne Netz ohne Fehler (REQ-0044) |
| Eingebettetes PyYAML | Fehlerbehebungen kommen nicht von selbst, die Aktualisierung ist Handarbeit mit einer lokalen Änderung | Anleitung in `cli/docspine/_vendor/README.md` |
| Übersetzte README | Fehler 14 prüft nur, aus welcher Version übersetzt wurde, nicht ob der Inhalt stimmt | `docspine-update` übersetzt nach jeder Änderung der Quelle neu |

_(confidence: verified — cli/build.py, cli/docspine/version.py, cli/docspine/_vendor/README.md,
cli/docspine/check.py, ADR-0009, US-0011)_
