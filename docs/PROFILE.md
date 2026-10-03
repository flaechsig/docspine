---
docspine: 0.1
language: de
statement_language: en
modules: [git-workflow]
sources: []
---

# Profil

docspine ist die Quelle des Standards und nutzt ihn zugleich für die eigene Doku.

## Abweichungen vom Kern

- **Keine `STANDARD.md`.** Der Standard entsteht gerade in diesem Repo (US-0001).
  Bis dahin gelten die ADRs in `09-decisions/`.
- **Kein Gate.** Die CLI gibt es noch nicht (US-0004). Bis dahin werden die Regeln von
  Hand eingehalten.
- **Generierte Bereiche ohne Generator.** Die Übersicht in `01-goals/README.md` und die
  Story-Listen in den Epics sind per Hand-Skript erzeugt, bis die CLI sie schreibt.
- **`docs/README.md` ist hier die Quelle,** nicht die Kopie. Der Link auf
  `STANDARD.md` zeigt ins Leere, bis US-0001 erledigt ist.
