---
title: Skills und Integrationen
path: [skills/, integrations/]
---

# Skills und Integrationen

**Verantwortung.** Die Skills `spine-*` führen durch die Arbeit mit dem Standard: Start
und Übernahme (`spine-init`, `spine-adopt`), der Kreislauf vom Requirement bis zum
Nachweis (`spine-require`, `-impact`, `-decide`, `-build`, `-prove`), die Anbindung an
den Build (`spine-gate`) und das Update (`spine-update`). Sie enthalten keine eigenen
Regeln, sondern verweisen auf Abschnitte des Standards. _(confidence: verified —
skills/, ADR-0009, ADR-0010, US-0011)_

**Integrationen.** Je Werkzeugkette eine Beschreibung, wie der Vertrag aus Standard 11
erfüllt wird, heute Maven mit JUnit 5. Sie liegen einmal unter `integrations/` und
werden mit `spine-gate` ausgeliefert. _(confidence: verified — integrations/,
cli/build.py, ADR-0019)_

**Schnittstelle.** Agent-Skills-Standard: ein Ordner je Skill mit `SKILL.md`, im
Frontmatter nur Felder des offenen Standards. _(confidence: verified — skills/)_

## Umgesetzte Requirements

<!-- generated:realized -->
_keine_
<!-- /generated -->
