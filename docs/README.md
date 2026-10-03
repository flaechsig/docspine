# Dokumentation nach docspine

Diese Dokumentation folgt dem Standard [docspine](https://github.com/flaechsig/docspine):
Anforderungen, Architektur und Entscheidungen bilden **ein Dokument**, verteilt auf
viele kleine Dateien, verbunden über feste IDs und von einem Prüfwerkzeug kontrolliert.
Diese Seite erklärt den Aufbau und die Arbeitsweise. Was im Einzelnen gilt, steht in
[STANDARD.md](STANDARD.md), die Werte dieses Projekts in [PROFILE.md](PROFILE.md).

- **Worum es geht:** [Vision](01-goals/vision.md)
- **Wo es steht:** [Epics, Stories und ihr Status](01-goals/README.md)

## Aufbau

Die Gliederung ist an die zwölf Kapitel von [arc42](https://arc42.org) angelehnt, mit
vier Abweichungen:

- Kapitel 1 enthält zusätzlich die ganze Spezifikation, damit Anforderungen und
  Architektur nicht in zwei Dokumenten auseinanderlaufen.
- Kapitel 9 besteht nur aus den einzelnen Entscheidungen (ADRs).
- Kapitel 10 wird aus den Qualitätsanforderungen erzeugt.
- Ein Kapitel existiert erst, wenn es Inhalt hat.

```
docs/
  README.md                   diese Seite
  STANDARD.md                 die Regeln des Standards (nicht editieren)
  PROFILE.md                  Werte dieses Projekts: Sprache, Module, Abweichungen

  01-goals/                   Kap. 1 — Einführung und Ziele
    README.md                 Übersicht: Epics, Stories, Status (generiert)
    vision.md                 warum es das gibt, für wen, woran sich Erfolg misst
    epics/E-<NAME>.md         Themen
    stories/US-NNNN.md        Nutzen aus Sicht der Nutzer
    requirements/REQ-NNNN.md  einzelne prüfbare Anforderungen
  02-constraints.md           Kap. 2 — Randbedingungen
  03-context.md               Kap. 3 — Kontextabgrenzung: Nachbarsysteme und Nutzer
  04-strategy.md              Kap. 4 — Lösungsstrategie
  05-building-blocks/         Kap. 5 — Bausteinsicht, ein Baustein je Datei
  06-runtime/                 Kap. 6 — Laufzeitsicht, ein Szenario je Datei
  07-deployment.md            Kap. 7 — Verteilungssicht
  08-concepts/                Kap. 8 — fachliche und technische Konzepte
  09-decisions/ADR-NNNN.md    Kap. 9 — Architekturentscheidungen
  10-quality.md               Kap. 10 — Qualitätsanforderungen (generiert)
  11-risks.md                 Kap. 11 — Risiken und technische Schulden
  12-glossary.md              Kap. 12 — Glossar
  diagrams/                   Quellen und Bilder großer Diagramme
```

Ordner, Dateinamen und Metadaten sind englisch, die Inhalte stehen in der
Projektsprache.

## Steuernde Dateien

Einige Dateien beschreiben nicht das Projekt, sondern wie mit seiner Doku gearbeitet
wird. Sie steuern Menschen und KI-Agenten gleichermaßen, nur `AGENTS.md` und die
Skills richten sich ausschließlich an KI-Agenten.

| Datei | Wofür | von Hand ändern? |
|---|---|---|
| `docs/README.md` | diese Seite: Aufbau und Arbeitsweise | nein, kommt aus docspine |
| `docs/STANDARD.md` | die Regeln, die für alle Inhalte gelten | nein, kommt aus docspine |
| `docs/PROFILE.md` | Werte dieses Projekts (Sprache, Module, Normquellen) und begründete Abweichungen vom Standard | ja |
| `AGENTS.md` (Repo-Root) | Einstieg für KI-Agenten: wo was steht, wie geprüft wird | ja |
| `.agents/skills/spine-*` | geführte Abläufe für KI-Agenten | nein, kommt aus docspine |
| `.agents/skills/<andere>` | projekteigene Abläufe | ja |
| `.claude/` und ähnliche | werkzeugspezifische Einstellungen, verweisen nur auf `AGENTS.md` | ja |

Was aus docspine kommt, wird beim Aktualisieren des Standards überschrieben. Änderungen
daran gehören nach docspine, nicht ins Projekt.

## Wie die Teile zusammenhängen

```
Vision → Epic → Story → Requirement ← Test
                  ↑          ↑
       Laufzeitszenario   Baustein (über den Code-Pfad)
                             ↑
                            ADR (Entscheidung → prüfbare Folge)
```

- Jede Aussage hat **genau eine Quelldatei**. Andere Stellen verweisen über die ID oder
  blenden den Inhalt in einem generierten Bereich ein (`<!-- generated:… -->`). Solche
  Bereiche nie von Hand ändern.
- **IDs sind unveränderlich.** Ändert sich eine Anforderung inhaltlich, entsteht eine
  neue, und die alte wird abgelöst.
- **Ob etwas umgesetzt ist, entscheidet das Prüfwerkzeug**, nicht ein Mensch und nicht
  eine KI: Ein Requirement gilt als umgesetzt, wenn ein Test oder ein Beleg es nachweist.

## Arbeitsweise

Die Arbeit läuft als Kreislauf. Jeder Schritt hat einen Skill (`spine-*`), der durch ihn
führt. Die Skills folgen dem offenen Agent-Skills-Standard und funktionieren mit
verschiedenen KI-Werkzeugen. Ohne Skills geht es genauso, die Regeln stehen in
`STANDARD.md`.

```
  Start: Vision
       │
       ▼
  ┌─► Anfordern ──────► Wirkung prüfen ──┬─► Entscheiden (ADR) ────────┐
  │   Epic · Story · REQ                 ├─► Architektur nachziehen ───┤
  │        ▲                             └─► kein Impact ──────────────┤
  │        │                                                           ▼
  │        └───────────── Lücke entdeckt ──────────────────────── Umsetzen ◄───┐
  │                                                       Code · Test · Status │
  │                                                                 │          │
  │                                                                 ▼          │
  │                                                            Nachweisen      │ nein
  │                                                                 │          │
  │                            ja                                   ▼          │
  └────────────────────────────────────────────────────── Prüfwerkzeug grün? ──┘
```

| Schritt | Was passiert | Skill |
|---|---|---|
| **Start** | Aus einer ersten Beschreibung entstehen Vision, Themen und Randbedingungen. Offenes bleibt als Frage stehen. | `spine-init` |
| **Anfordern** | Ein Bedürfnis wird zu Story und Requirement: wer, was, warum, woran prüfbar. | `spine-require` |
| **Wirkung prüfen** | Muss die Architektur etwas berücksichtigen, ändern oder entscheiden? | `spine-impact` |
| **Entscheiden** | Eine fällige Entscheidung wird mit Alternativen und Begründung festgehalten. | `spine-decide` |
| **Umsetzen** | Code und Test entstehen, der Test trägt die Requirement-ID. Ist er grün, wechselt der Status. | `spine-build` |
| **Nachweisen** | Prüft der Test wirklich, was das Requirement fordert, oder trägt er nur die ID? | `spine-prove` |

Drei Regeln gelten in jedem Schritt:

- **Der Mensch sagt, was gilt.** Skills und KIs schlagen vor, geschrieben wird nach
  Freigabe.
- **Nichts erfinden.** Was niemand weiß, bleibt `UNKNOWN` mit der offenen Frage dazu.
- **Lücken führen zurück.** Zeigt sich beim Umsetzen, dass eine Anforderung fehlt oder
  die Architektur nicht trägt, geht es zurück zum passenden Schritt, statt die Lücke im
  Code zu überbrücken.

Wer das Prüfwerkzeug in den Build einbinden oder ein bestehendes Projekt übernehmen will,
findet Anleitung und Installation auf der [docspine-Seite](https://github.com/flaechsig/docspine).

## Dank

docspine erfindet wenig neu, sondern verbindet bewährte Arbeiten:

- **[arc42](https://arc42.org)** von Gernot Starke und Peter Hruschka: die Gliederung
  dieses Dokuments und der Gedanke, Architektur pragmatisch und schrittweise zu
  dokumentieren.
- **[IREB](https://www.ireb.org)** (International Requirements Engineering Board) mit
  dem CPRE-Lehrplan: die Begriffe und Grundsätze des Requirements Engineering, auf
  denen Vision, Story und Requirement aufbauen.
- **[EARS](https://alistairmavin.com/ears/)** (Easy Approach to Requirements Syntax) von
  Alistair Mavin und Kollegen: der Satzbau, der Anforderungen eindeutig und prüfbar macht.
- **[Architecture Decision Records](https://adr.github.io)**, beschrieben von Michael
  Nygard: Entscheidungen samt Begründung festhalten und nie umschreiben, nur ablösen.
- **[Mermaid](https://mermaid.js.org)** von Knut Sveidqvist und der Community:
  Diagramme als Text.
- **[Agent Skills](https://agentskills.io)**, von Anthropic als offener Standard
  veröffentlicht, und **[AGENTS.md](https://agents.md)**: werkzeugübergreifende Wege,
  KI-Agenten Abläufe und Einstieg mitzugeben.
- Die **Docs-as-Code**-Bewegung: Dokumentation wie Code im Repo führen, prüfen und
  versionieren.
