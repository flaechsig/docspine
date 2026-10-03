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
- **Prüfwerkzeug unvollständig.** Die CLI prüft die Fehlerklassen 1–10 und 13 und
  erzeugt Status-Übersicht und Story-Listen. Fehlerklassen 11, 12, 14, die übrigen
  generierten Bereiche und `STATUS.md` folgen mit US-0005.
