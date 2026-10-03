# docspine — Dokumentation

> Ein Dokumentationsstandard mit Prüfwerkzeug, der Anforderungen, Architektur und
> Entscheidungen als ein nachprüfbares Dokument im Repo hält, lesbar für jede KI und
> jeden Menschen.

**Einstieg in den Inhalt: [Vision](01-goals/vision.md).** Von dort führen die Epics
weiter zu Stories und Requirements.

Diese Seite erklärt, wie die Doku aufgebaut ist und auf welchen Standards sie beruht.

## Aufbau

Die Doku ist **ein Dokument**, verteilt auf viele Dateien. Die Gliederung folgt
[arc42](https://arc42.org), der Vorlage für Architekturdokumentation mit zwölf
Kapiteln. Kapitel 1 trägt zusätzlich die ganze Spezifikation, damit Anforderungen und
Architektur nicht in zwei Dokumenten auseinanderlaufen
([ADR-0007](09-decisions/ADR-0007.md)).

Ein Kapitel existiert nur, wenn es Inhalt hat. Fehlt eine Datei, ist das Kapitel noch
offen ([ADR-0008](09-decisions/ADR-0008.md)).

```
docs/
  README.md                 diese Seite
  PROFILE.md                Projektwerte (Sprache, Module) und Abweichungen vom Standard
  STANDARD.md               die Regeln (Kopie aus docspine, nicht editieren) *

  01-goals/                 arc42 Kap. 1 — Einführung und Ziele
    vision.md               warum es das gibt, für wen, woran sich Erfolg misst
    epics/E-<NAME>.md       Themen
    stories/US-NNNN.md      Nutzen aus Sicht der Nutzer, verweist auf Requirements
    requirements/REQ-NNNN.md  einzelne prüfbare Anforderungen *
  02-constraints.md         Kap. 2 — Randbedingungen *
  03-context.md             Kap. 3 — Kontextabgrenzung: Nachbarsysteme und Nutzer
  04-strategy.md            Kap. 4 — Lösungsstrategie *
  05-building-blocks/       Kap. 5 — Bausteinsicht, ein Baustein je Datei *
  06-runtime/               Kap. 6 — Laufzeitsicht, ein Szenario je Datei *
  07-deployment.md          Kap. 7 — Verteilungssicht *
  08-concepts/              Kap. 8 — fachliche und technische Konzepte *
  09-decisions/ADR-NNNN.md  Kap. 9 — Architekturentscheidungen
  10-quality.md             Kap. 10 — Qualitätsanforderungen, generiert *
  11-risks.md               Kap. 11 — Risiken und technische Schulden *
  12-glossary.md            Kap. 12 — Glossar *
  diagrams/                 Quellen und SVGs großer Diagramme *

  * noch nicht vorhanden
```

Ordner, Dateinamen und Frontmatter sind englisch, die Inhalte deutsch
([ADR-0011](09-decisions/ADR-0011.md)).

## Wie die Teile zusammenhängen

```
Vision → Epic → Story → Requirement ← Test
                  ↑          ↑
       Laufzeitszenario   Baustein (über den Code-Pfad)
                             ↑
                            ADR (Entscheidung → prüfbare Folge)
```

- Jede Aussage hat **genau eine Quelldatei**. Andere Stellen verweisen über die ID
  (`REQ-0042`, `ADR-0007`) oder blenden sie in einem generierten Bereich ein
  (`<!-- generated:… -->`). Solche Bereiche nicht von Hand ändern
  ([ADR-0003](09-decisions/ADR-0003.md)).
- IDs sind unveränderlich. Ändert sich eine Anforderung inhaltlich, entsteht eine neue,
  die alte wird abgelöst.

## Standards, auf denen die Doku beruht

| Standard | wofür | hier |
|---|---|---|
| [arc42](https://arc42.org) | Gliederung des Dokuments | die Kapitelordner `01-…` bis `12-…` |
| [EARS](https://alistairmavin.com/ears/) | Satzbau für Anforderungen (`WHEN … the system shall …`) | `statement` in jedem Requirement |
| [ADR](https://adr.github.io) | Architekturentscheidungen festhalten | `09-decisions/` |
| Markdown mit YAML-Frontmatter | Format aller Dateien, Metadaten maschinenlesbar | überall ([ADR-0001](09-decisions/ADR-0001.md)) |
| [Mermaid](https://mermaid.js.org) | Diagramme als Text, von GitHub direkt dargestellt | in den Kapiteln ([ADR-0002](09-decisions/ADR-0002.md)) |
| [Agent Skills](https://agentskills.io) | geführte Abläufe für KI-Agenten | `.agents/skills/` ([ADR-0009](09-decisions/ADR-0009.md)) |
| [AGENTS.md](https://agents.md) | Einstieg für KI-Agenten | `AGENTS.md` im Repo-Root |

## Status

Alle Entscheidungen stehen auf `proposed`, bis die Migration von 3dPacMan sie
bestätigt. Solange dürfen sie direkt geändert werden. Eine Übersicht aller
Entscheidungen steht in [09-decisions/](09-decisions/).
