---
title: Skills und Integrationen
path: [skills/, integrations/]
---

# Skills und Integrationen

**Verantwortung.** Die Skills `docspine-*` führen durch die Arbeit mit dem Standard: Start
und Übernahme (`docspine-init`, `docspine-adopt`), der Kreislauf vom Requirement bis zum
Nachweis (`docspine-require`, `-impact`, `-decide`, `-build`, `-prove`), die Anbindung an
den Build (`docspine-gate`) und das Update (`docspine-update`). Sie enthalten keine eigenen
Regeln, sondern verweisen auf Abschnitte des Standards. _(confidence: verified —
skills/, ADR-0009, ADR-0026, US-0011)_

**Integrationen.** Je Werkzeugkette eine Beschreibung, wie der Vertrag aus Standard 11
erfüllt wird, heute Maven mit JUnit 5. Sie liegen einmal unter `integrations/` und
werden mit `docspine-gate` ausgeliefert. _(confidence: verified — integrations/,
cli/build.py, ADR-0019)_

**Schnittstelle.** Agent-Skills-Standard: ein Ordner je Skill mit `SKILL.md`, im
Frontmatter nur Felder des offenen Standards. _(confidence: verified — skills/)_

## Umgesetzte Requirements

<!-- generated:realized -->
_keine_
<!-- /generated -->
