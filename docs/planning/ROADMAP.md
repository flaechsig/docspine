# Roadmap

Handgepflegter Anker für offene Fäden, noch ohne Priorisierung.

## Kernstandard festlegen

- **ADR-Nummern vereinheitlichen.** 3dPacMan nutzt `ADR-0001`, tarifnova und blocpress
  `ADR-001` (obwohl tarifnovas CONVENTIONS `ADR-NNNN` verlangt). docspine nutzt
  `ADR-NNNN`, passend zu `REQ-NNNN` und `US-NNNN`.
- **Status-Vokabular für Requirements.** 3dPacMan: `proposed → accepted → implemented
  → verified | dropped`. tarifnova/blocpress: `implemented | planned | proposed |
  rejected | superseded` plus eigene Achse `confidence`. Kernvokabular festlegen.
- **Kern vs. Projektprofil schneiden.** Was aus `CONVENTIONS.md` ist allgemein, was
  gehört ins Profil?
- **Optionale Module definieren:** DEVLOG, guides/measurements, Betriebs-Runbooks, …
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
- **3dPacMan:** kein Trace-Adapter, Generator nur für Konsistenz und Ansichten.
- Reihenfolge festlegen (Vorschlag: 3dPacMan als kleinster Testfall zuerst).

## Offene Fragen

- Soll die Doku jemals als Site oder PDF veröffentlicht werden?
