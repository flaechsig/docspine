# Generierte Bereiche

**Problem.** Eine Story nennt ihre Requirements, ein Requirement soll aber auch zeigen,
zu welcher Story es gehört. Von Hand gepflegt, laufen solche Rückverweise und Übersichten
auseinander (ADR-0003).

**Lösung.** Beziehungen stehen nur in eine Richtung im Frontmatter (Standard 4). Alles
andere schreibt `render` in markierte Bereiche innerhalb der von Hand geschriebenen
Dateien. Ein Bereich, der fehlt, wird angehängt. _(confidence: verified —
cli/docspine/render.py, REQ-0013, REQ-0014, REQ-0019, REQ-0020, REQ-0021, REQ-0022)_

**Ein Plan für beide Befehle.** `render.plan()` berechnet für jede verwaltete Datei den
vollständigen Soll-Text. `render` schreibt die Abweichungen, `check` meldet sie als
Fehler 11. Es gibt also keine zweite Implementierung der Regeln, die von der ersten
abweichen könnte. _(confidence: verified — cli/docspine/render.py, cli/docspine/check.py,
REQ-0016)_

**Folgen.**
- Nach jeder Änderung an Frontmatter oder Kapiteln läuft erst `render`, dann `check`.
- Konflikte beim Mergen innerhalb eines Bereichs löst man nicht von Hand: Bereich
  verwerfen, `render` laufen lassen.
- `render` gehört nicht in den Build, weil es Dateien ändert ([Prüfung im Build](../06-runtime/pruefung-im-build.md)).
