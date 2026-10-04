---
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
  `.docspine/STANDARD.md` ist eine Kopie, `docs/README.md` eine von Hand erstellte
  Übersetzung. Die CLI wird hier direkt aus `cli/` aufgerufen, nicht als
  `.docspine/docspine.pyz`.
- **Fehlerklasse 12 wird noch nicht geprüft.** Diagrammprüfung folgt mit US-0015.
  docspine hat bisher keine Diagrammbilder.
