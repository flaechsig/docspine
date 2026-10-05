# Ziele und Anforderungen

Kapitel 1 des Dokuments: warum es das Projekt gibt ([Vision](vision.md)) und was es
leisten soll, heruntergebrochen in Epics, Stories und Requirements.

<!-- generated:status -->
| | Anzahl |
|---|---|
| Stories | ⚪ offen 8 · 🟡 in Arbeit 4 · ✅ verifiziert 5 |
| Requirements | umgesetzt 32 · abgelöst 5 |
| [Entscheidungen](../09-decisions/) | vorgeschlagen 21 |

## [E-GENERATOR](epics/E-GENERATOR.md) — Prüfen und Erzeugen per CLI

Status: 🟡 in Arbeit

| Story | Titel | Status |
|---|---|---|
| [US-0004](stories/US-0004.md) | CLI-Kern mit check und render | ✅ verifiziert |
| [US-0005](stories/US-0005.md) | Neue Prüfungen und generierte Bereiche | ✅ verifiziert |
| [US-0006](stories/US-0006.md) | Testergebnisse anbinden, Beispiel Maven und JUnit 5 | ✅ verifiziert |
| [US-0015](stories/US-0015.md) | Diagramme prüfen und PDF erzeugen | ⚪ offen |

## [E-MIGRATION](epics/E-MIGRATION.md) — Die bestehenden Projekte umstellen

Status: ⚪ offen

| Story | Titel | Status |
|---|---|---|
| [US-0012](stories/US-0012.md) | 3dPacMan migrieren | ⚪ offen |
| [US-0013](stories/US-0013.md) | Ursprungsprojekt migrieren | ⚪ offen |
| [US-0014](stories/US-0014.md) | blocpress migrieren | ⚪ offen |

## [E-SKILLS](epics/E-SKILLS.md) — Geführte Abläufe als Skills

Status: 🟡 in Arbeit

| Story | Titel | Status |
|---|---|---|
| [US-0007](stories/US-0007.md) | spine-init | 🟡 in Arbeit |
| [US-0008](stories/US-0008.md) | Methodik-Skills zusammenführen | 🟡 in Arbeit |
| [US-0009](stories/US-0009.md) | spine-adopt | ⚪ offen |
| [US-0010](stories/US-0010.md) | spine-gate | 🟡 in Arbeit |
| [US-0011](stories/US-0011.md) | Kaltstart-Test | ⚪ offen |
| [US-0016](stories/US-0016.md) | spine-update | 🟡 in Arbeit |

## [E-STANDARD](epics/E-STANDARD.md) — Der Standard als lesbares Regelwerk

Status: 🟡 in Arbeit

| Story | Titel | Status |
|---|---|---|
| [US-0001](stories/US-0001.md) | STANDARD.md schreiben | ✅ verifiziert |
| [US-0002](stories/US-0002.md) | Regeln aus den Skills in den Standard verlagern | ⚪ offen |
| [US-0003](stories/US-0003.md) | Frontmatter als JSON Schema | ⚪ offen |
| [US-0017](stories/US-0017.md) | Arbeiten im kleinen Team | ✅ verifiziert |

## Offene Fragen

_keine_

## Offene Entscheidungen

- [ADR-0001](../09-decisions/ADR-0001.md) — Markdown mit Frontmatter als einziges Quellformat
- [ADR-0002](../09-decisions/ADR-0002.md) — Diagramme als Textquelle
- [ADR-0003](../09-decisions/ADR-0003.md) — Beziehungen nur nach unten, alles andere generiert
- [ADR-0004](../09-decisions/ADR-0004.md) — Standard als versioniertes Paket, als Kopie im Projekt
- [ADR-0005](../09-decisions/ADR-0005.md) — Ein Status-Vokabular je Artefakt, Prüfstand als eigene Achse
- [ADR-0006](../09-decisions/ADR-0006.md) — Schnitt zwischen Kernstandard und Projektprofil
- [ADR-0007](../09-decisions/ADR-0007.md) — Ein Dokument nach arc42-Gerüst
- [ADR-0008](../09-decisions/ADR-0008.md) — Artefakte verschlanken
- [ADR-0009](../09-decisions/ADR-0009.md) — Steuernde Artefakte und die Grenze zu KI-Werkzeugen
- [ADR-0010](../09-decisions/ADR-0010.md) — Skill-Familie spine-*
- [ADR-0011](../09-decisions/ADR-0011.md) — Projektsprache und englisches Maschinenvokabular
- [ADR-0012](../09-decisions/ADR-0012.md) — Generator-Kern als eigenständige CLI
- [ADR-0013](../09-decisions/ADR-0013.md) — Testergebnisse als Schnittstelle, keine Module
- [ADR-0014](../09-decisions/ADR-0014.md) — Konfiguration englisch, Dokumentation in der Projektsprache
- [ADR-0015](../09-decisions/ADR-0015.md) — Konfiguration unter .docspine/, docs/ nur Dokumentation
- [ADR-0016](../09-decisions/ADR-0016.md) — Update mit spine-update, Version nur in den ausgelieferten Dateien
- [ADR-0017](../09-decisions/ADR-0017.md) — Versionsregel für das, was docspine ausliefert
- [ADR-0018](../09-decisions/ADR-0018.md) — Testergebnisse aus JUnit-XML-Berichten, REQ-ID im Testnamen
- [ADR-0019](../09-decisions/ADR-0019.md) — Anbindung an Build und Tests als Vertrag, Integrationen je Werkzeug
- [ADR-0020](../09-decisions/ADR-0020.md) — Spezifizieren und Bauen getrennt, Freigabe über den Status
- [ADR-0021](../09-decisions/ADR-0021.md) — Kleine Teams über Branches, IDs werden auf dem Hauptzweig endgültig

## Widersprüche

_keine_

## Kapitel ohne Inhalt

- 02-constraints
- 04-strategy
- 05-building-blocks
- 06-runtime
- 07-deployment
- 08-concepts
- 11-risks
- 12-glossary

## Teilweise gefüllte Kapitel

_keine_
<!-- /generated -->
