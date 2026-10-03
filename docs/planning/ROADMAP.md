# Roadmap

Handgepflegter Anker für offene Fäden, noch ohne Priorisierung.

## Kernstandard festlegen

- **ADR-Nummern vereinheitlichen.** 3dPacMan nutzt `ADR-0001`, tarifnova und blocpress
  `ADR-001` (obwohl tarifnovas CONVENTIONS `ADR-NNNN` verlangt). docspine nutzt
  `ADR-NNNN`, passend zu `REQ-NNNN` und `US-NNNN`.
- ~~Status-Vokabular für Requirements~~ → [ADR-0005](../architecture/decisions/ADR-0005.md)
- ~~Kern vs. Projektprofil schneiden, optionale Module definieren~~ →
  [ADR-0006](../architecture/decisions/ADR-0006.md)
- **Kernstandard schreiben** (`standard/` in diesem Repo) und versionieren.

## Generator

- Auslieferungsform entscheiden: CLI, Maven-Plugin oder beides.
- Kern aus `tarifnova-req-check` herauslösen und vom Package entkoppeln.
- Verwaltete Bereiche nach [ADR-0003](../architecture/decisions/ADR-0003.md)
  umsetzen: Marker-Syntax, Neuschreiben, Fehlerklasse „Bereich veraltet“.
- Frontmatter für ADRs und arc42-Kapitel lesen
  ([ADR-0001](../architecture/decisions/ADR-0001.md)).
- Prüfung „SVG älter als DOT/PlantUML-Quelle“
  ([ADR-0002](../architecture/decisions/ADR-0002.md)).
- JUnit-5-Trace-Adapter als eigenes Artefakt.

## Plugin

- Allgemeine Skills aus tarifnova und blocpress zusammenführen (Unterschiede sichten).
- Als Claude-Code-Plugin paketieren.

## Migration der Projekte

- **tarifnova:** `.adoc` → `.md` (ADRs, arc42), Rückverweise „Teil von US-…“ entfernen,
  Profil anlegen.
- **blocpress:** wie tarifnova. AsciiDoc-Altbestand bleibt bis zum Retirement.
- **3dPacMan:** Metadaten von Aufzählungspunkten auf Frontmatter umstellen, Status
  nach ADR-0005 abbilden (13× `accepted` → `planned`, 9× `in-progress` prüfen),
  Stories und Epics bekommen einen Status. Kein Trace-Adapter, `evidence` und
  `verification` von Hand.
- Reihenfolge festlegen (Vorschlag: 3dPacMan als kleinster Testfall zuerst).

## Offene Fragen

- Soll die Doku jemals als Site oder PDF veröffentlicht werden?
