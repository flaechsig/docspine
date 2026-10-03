---
docspine: 0.1
language: de
statement_language: en
sources: []
---

# Profil

Die Werte dieses Projekts für den Standard (Frontmatter oben) und die begründeten
Abweichungen davon (unten). Diese Datei wird von Hand gepflegt. Menschen und KI-Agenten
lesen sie zusammen mit `STANDARD.md`, um zu wissen, was in diesem Projekt gilt.

docspine ist die Quelle des Standards und nutzt ihn zugleich für die eigene Doku.

## Abweichungen vom Standard

- **Quelle und Kopie im selben Repo.** Die Quellen liegen unter `standard/en/`.
  `docs/STANDARD.md` ist eine Kopie, `docs/README.md` eine von Hand erstellte
  Übersetzung, bis `spine-init` und die CLI das übernehmen.
- **Kein Gate.** Die CLI gibt es noch nicht (US-0004). Bis dahin werden die Regeln von
  Hand eingehalten.
- **Keine `STATUS.md`.** Sie entsteht erst mit der CLI (US-0004, US-0005).
- **Generierte Bereiche ohne Generator.** Die Übersicht in `01-goals/README.md` und die
  Story-Listen in den Epics sind per Hand-Skript erzeugt, bis die CLI sie schreibt.
