# Ziele und Anforderungen

Kapitel 1 des Dokuments: warum es das Projekt gibt ([Vision](vision.md)) und was es
leisten soll, heruntergebrochen in Epics, Stories und Requirements.

<!-- generated:status -->
| | Anzahl |
|---|---|
| Stories | ⚪ offen 1 · ✅ verifiziert 20 · ⛔ abgelöst 1 |
| Requirements | geplant 6 · umgesetzt 48 · abgelöst 7 |
| [Entscheidungen](../09-decisions/) | angenommen 28 · verworfen 1 · abgelöst 1 |

## [E-GENERATOR](epics/E-GENERATOR.md) — Prüfen und Erzeugen per CLI

Status: 🟡 in Arbeit

| Story | Titel | Status |
|---|---|---|
| [US-0004](stories/US-0004.md) | CLI-Kern mit check und render | ✅ verifiziert |
| [US-0005](stories/US-0005.md) | Neue Prüfungen und generierte Bereiche | ✅ verifiziert |
| [US-0006](stories/US-0006.md) | Testergebnisse anbinden, Beispiel Maven und JUnit 5 | ✅ verifiziert |
| [US-0015](stories/US-0015.md) | Veraltete Diagrammbilder erkennen | ✅ verifiziert |
| [US-0019](stories/US-0019.md) | Bausteine zeigen nur gültige Requirements | ✅ verifiziert |
| [US-0020](stories/US-0020.md) | Risiken und Schulden mit ID | ✅ verifiziert |
| [US-0021](stories/US-0021.md) | Akzeptanz als Vollständigkeitsprobe | ✅ verifiziert |
| [US-0022](stories/US-0022.md) | Requirements nennen ihre Entscheidung | ⚪ offen |

## [E-MIGRATION](epics/E-MIGRATION.md) — Die bestehenden Projekte umstellen

Status: ✅ verifiziert

| Story | Titel | Status |
|---|---|---|
| [US-0012](stories/US-0012.md) | 3dPacMan migrieren | ✅ verifiziert |
| [US-0013](stories/US-0013.md) | Ursprungsprojekt migrieren | ✅ verifiziert |
| [US-0014](stories/US-0014.md) | blocpress migrieren | ✅ verifiziert |

## [E-SKILLS](epics/E-SKILLS.md) — Geführte Abläufe als Skills

Status: ✅ verifiziert

| Story | Titel | Status |
|---|---|---|
| [US-0007](stories/US-0007.md) | docspine-init | ✅ verifiziert |
| [US-0008](stories/US-0008.md) | Methodik-Skills zusammenführen | ✅ verifiziert |
| [US-0009](stories/US-0009.md) | docspine-adopt | ✅ verifiziert |
| [US-0010](stories/US-0010.md) | docspine-gate | ✅ verifiziert |
| [US-0011](stories/US-0011.md) | Kaltstart-Test | ✅ verifiziert |
| [US-0016](stories/US-0016.md) | docspine-update | ✅ verifiziert |
| [US-0018](stories/US-0018.md) | Über neue Versionen informiert werden | ✅ verifiziert |

## [E-STANDARD](epics/E-STANDARD.md) — Der Standard als lesbares Regelwerk

Status: ✅ verifiziert

| Story | Titel | Status |
|---|---|---|
| [US-0001](stories/US-0001.md) | STANDARD.md schreiben | ✅ verifiziert |
| [US-0002](stories/US-0002.md) | Regeln aus den Skills in den Standard verlagern | ✅ verifiziert |
| [US-0003](stories/US-0003.md) | Frontmatter als JSON Schema | ⛔ abgelöst |
| [US-0017](stories/US-0017.md) | Arbeiten im kleinen Team | ✅ verifiziert |

## Offene Fragen

- [01-goals/stories/US-0022.md](stories/US-0022.md): UNKNOWN — offene Frage: Braucht die Migration bestehender Projekte ein eigenes Requirement (etwa einen Befehl im Prüfwerkzeug), oder genügt der Skill `docspine-update`?
- [09-decisions/ADR-0030.md](../09-decisions/ADR-0030.md): UNKNOWN — offene Frage: Darf ein Punkt der Akzeptanz ein Requirement einer anderen Story nennen, oder nur die in `requirements` der eigenen Story? Vorläufig ist jedes vorhandene Requirement erlaubt; die Erfahrung in Projekten soll es klären.
- [09-decisions/ADR-0030.md](../09-decisions/ADR-0030.md): UNKNOWN — offene Frage: Soll eine Story mit einem `UNKNOWN` in der Akzeptanz `verified` sein dürfen? Bisher blockiert `UNKNOWN` nie etwas; vorläufig bleibt es dabei.

## Offene Entscheidungen

_keine_

## Widersprüche

_keine_

## Kapitel ohne Inhalt

_keine_

## Teilweise gefüllte Kapitel

_keine_
<!-- /generated -->
