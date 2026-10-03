# docspine — Dokumentation

Das Eingangstor. Es erklärt, *warum* es docspine gibt und *wo* du weiterliest.

## Warum es das gibt

tarifnova, blocpress und 3dPacMan folgen derselben Doku-Methodik. Bisher wird
sie kopiert, und die Kopien laufen auseinander:

- `CONVENTIONS.md` existiert dreimal mit abweichenden Status-Werten und ADR-Nummern.
- Der Generator (`*-req-check`, 1166 Zeilen) liegt in tarifnova und blocpress
  identisch vor, nur mit anderem Package. 3dPacMan hat gar keinen.
- Die Skills (`adr`, `anforderung`, `arc42`, …) sind kopiert und leicht verschieden.

Dazu kommt das Ziel, die Doku in einer standardisierten Form im Repo abzulegen, die
jede KI und jeder Mensch aufgreifen kann, statt sie in einem Werkzeug zu verstecken.

docspine macht daraus **einen** versionierten Standard: Regeln, Generator und Skills
an einer Stelle, als Kopie in jedem Projekt, plus ein kurzes Profil pro Projekt.

## Stand

Alle Entscheidungen stehen auf `proposed`, bis die Migration von 3dPacMan sie
bestätigt. Solange dürfen sie direkt geändert werden.

## Entscheidungen

| ADR | Thema |
|---|---|
| [ADR-0001](09-decisions/ADR-0001.md) | Markdown mit Frontmatter als einziges Quellformat |
| [ADR-0002](09-decisions/ADR-0002.md) | Diagramme als Textquelle |
| [ADR-0003](09-decisions/ADR-0003.md) | Beziehungen nur nach unten, alles andere generiert |
| [ADR-0004](09-decisions/ADR-0004.md) | Standard als versioniertes Paket, als Kopie im Projekt |
| [ADR-0005](09-decisions/ADR-0005.md) | Ein Status-Vokabular je Artefakt, Prüfstand als eigene Achse |
| [ADR-0006](09-decisions/ADR-0006.md) | Schnitt zwischen Kernstandard, Modulen und Projektprofil |
| [ADR-0007](09-decisions/ADR-0007.md) | Ein Dokument nach arc42-Gerüst |
| [ADR-0008](09-decisions/ADR-0008.md) | Artefakte verschlanken |
| [ADR-0009](09-decisions/ADR-0009.md) | Steuernde Artefakte und die Grenze zu KI-Werkzeugen |
| [ADR-0010](09-decisions/ADR-0010.md) | Skill-Familie spine-* |
| [ADR-0011](09-decisions/ADR-0011.md) | Projektsprache und englisches Maschinenvokabular |
| [ADR-0012](09-decisions/ADR-0012.md) | Generator-Kern als eigenständige CLI |

## Offene Punkte

Übergangsweise in [planning/ROADMAP.md](planning/ROADMAP.md). Nach ADR-0008 gibt es
keine ROADMAP mehr. Sie entfällt, sobald docspine sich selbst mit `spine-init` eine
Vision und Stories gegeben hat.
