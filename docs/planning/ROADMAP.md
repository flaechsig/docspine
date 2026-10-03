# Offene Punkte (Übergang)

Diese Datei gibt es nur, bis docspine sich selbst nach dem eigenen Standard eine
Vision und Stories gegeben hat (ADR-0008). Ohne Priorisierung.

## Standard

- **`STANDARD.md` schreiben:** Kern und Module als eine Datei, aus den ADRs und den
  bestehenden `CONVENTIONS.md` (ADR-0004, ADR-0006).
- **Regeln aus den Skills herauslösen:** EARS-Muster, Status-Wahl, Ablöseverfahren
  aus `anforderung`, `adr`, `arc42` usw. nach `STANDARD.md` (ADR-0009).
- **JSON Schema** für das Frontmatter aller Artefakte (ADR-0009).
- **ADR-Nummern:** einheitlich `ADR-NNNN`. tarifnova und blocpress nutzen `ADR-001`.

## Generator

- Implementierungssprache der CLI festlegen (ADR-0012).
- Kern aus `tarifnova-req-check` herauslösen und vom Package entkoppeln.
- Neu: Frontmatter für ADRs und Kapitel, generierte Bereiche (ADR-0003), Nähte
  `path:`/`stories:`/`requires:` (ADR-0007), Kap. 10 aus Qualitäts-Requirements,
  abgeleiteter Epic-Status und `confidence` (ADR-0005), Übersetzungen `de`/`en`
  (ADR-0011), Prüfung „SVG älter als Quelle“ (ADR-0002), PDF bei Bedarf.
- Maven-Plugin und JUnit-5-Adapter für die Build-Anbindung.

## Skills

- `spine-init` schreiben (ADR-0010).
- `spine-require`, `-impact`, `-decide`, `-build`, `-prove` aus den tarifnova- und
  blocpress-Fassungen zusammenführen, Regeln nach `STANDARD.md` auslagern.
- `spine-adopt` und `spine-gate` neu schreiben.
- Kaltstart-Test: ein Agent ohne Skills, nur mit Repo und Gate (ADR-0009).

## Migration

- **3dPacMan zuerst** als kleinster Fall: Frontmatter statt Aufzählungspunkten, Status
  nach ADR-0005, neue Gliederung, `make check`. Danach die ADRs auf `accepted`.
- **tarifnova:** `.adoc` → `.md`, neue Gliederung, Rückverweise „Teil von US-…“
  entfernen, Inhalte aus `CLAUDE.md` in das Dokument überführen, `AGENTS.md` von
  GSD-Inhalten trennen.
- **blocpress:** wie tarifnova, AsciiDoc-Altbestand bleibt bis zum Retirement.
