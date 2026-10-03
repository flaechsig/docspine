<!-- docspine 0.1 · Übersetzung von standard/en/STANDARD.md · in Projekten nicht editieren -->

# docspine-Standard

Version 0.1 (Entwurf)

Dieses Dokument legt die Regeln für eine Dokumentation nach docspine fest. Es gilt für
Menschen und KI-Agenten gleichermaßen. `README.md` erklärt, wie man mit der
Dokumentation arbeitet; diese Datei legt fest, was gilt. Die Werte des Projekts und
etwaige Abweichungen stehen in `PROFILE.md`.

Die Wörter **muss**, **darf nicht**, **soll** und **darf** werden im üblichen
normativen Sinn verwendet.

## 1 Prinzipien

1. **Eine Quelle pro Aussage.** Jede Aussage steht in genau einer Quelldatei. Andere
   Stellen verweisen über die ID darauf oder zeigen sie in einem generierten Bereich
   (Abschnitt 4). Kopierter Text ist ein Fehler.
2. **IDs sind unveränderlich.** Eine ID wird nie umnummeriert, wiederverwendet oder
   gelöscht. Der Status ändert sich, die Nummer nicht.
3. **Die Begründung zuerst.** Was das System tut, wird im Code sichtbar sein. Warum es
   so entschieden wurde, steht nur hier.
4. **Beobachtung ist nicht Absicht.** Aus dem Code abgeleitetes Verhalten ist eine
   Beschreibung, keine Anforderung. Requirements sagen, was gewollt ist;
   Beschreibungen sagen, was ist.
5. **Der Mensch entscheidet, was gilt.** Werkzeuge und KI-Agenten schlagen vor;
   geschrieben wird nach Freigabe durch einen Menschen.
6. **Nichts wird erfunden.** Was niemand weiß, bleibt `UNKNOWN`, zusammen mit der
   offenen Frage: `UNKNOWN — offene Frage: …`.
7. **Ob etwas umgesetzt ist, entscheidet das Prüfwerkzeug**, nicht ein Mensch und nicht
   ein KI-Agent (Abschnitt 11).
8. **Die Dokumentation wächst mit den Änderungen.** Nichts wird auf Vorrat
   dokumentiert. Ein Kapitel existiert erst, wenn es Inhalt hat.

## 2 Aufbau

### 2.1 Gliederung

Die Dokumentation ist ein Dokument, verteilt auf viele Dateien. Die Gliederung ist an
die zwölf Kapitel von arc42 angelehnt, mit vier Abweichungen: Kapitel 1 enthält
zusätzlich die ganze Spezifikation, Kapitel 9 besteht nur aus den einzelnen
Entscheidungen, Kapitel 10 wird erzeugt, und ein Kapitel existiert erst, wenn es
Inhalt hat.

```
AGENTS.md                     Einstieg für KI-Agenten (projektspezifisch)
docs/
  README.md                   wie man mit dieser Dokumentation arbeitet (aus docspine)
  STANDARD.md                 diese Datei (aus docspine)
  PROFILE.md                  Projektwerte und Abweichungen
  STATUS.md                   Zahlen, Lücken, Widersprüche, offene Fragen (generiert)

  01-goals/                   Kapitel 1: Einführung und Ziele
    README.md                 Epics und Stories mit Status (generiert)
    vision.md
    epics/E-<NAME>.md
    stories/US-NNNN.md
    requirements/REQ-NNNN.md
  02-constraints.md           Kapitel 2: Randbedingungen
  03-context.md               Kapitel 3: Kontextabgrenzung
  04-strategy.md              Kapitel 4: Lösungsstrategie
  05-building-blocks/<name>.md  Kapitel 5: Bausteinsicht, ein Baustein je Datei
  06-runtime/<name>.md        Kapitel 6: Laufzeitsicht, ein Szenario je Datei
  07-deployment.md            Kapitel 7: Verteilungssicht
  08-concepts/<name>.md       Kapitel 8: fachliche und technische Konzepte
  09-decisions/ADR-NNNN.md    Kapitel 9: Architekturentscheidungen
  10-quality.md               Kapitel 10: Qualitätsanforderungen (generiert)
  11-risks.md                 Kapitel 11: Risiken und technische Schulden
  12-glossary.md              Kapitel 12: Glossar
  diagrams/                   Quellen und Bilder großer Diagramme
  legacy/                     importierte alte Dokumentation, vorübergehend (Abschnitt 10)
```

Ein Kapitel darf eine einzelne Datei oder ein Ordner sein; für die Kapitel, die oben
als Ordner stehen, ist die Gliederung verbindlich. Projekte dürfen eigene Ordner unter
`docs/` anlegen (zum Beispiel `docs/guides/`). Sie werden nicht geprüft, außer dass
Links dorthin auflösen müssen.

### 2.2 Steuernde Dateien

| Datei | Wofür | von Hand ändern |
|---|---|---|
| `docs/README.md` | wie man mit der Dokumentation arbeitet | nein, aus docspine |
| `docs/STANDARD.md` | die Regeln | nein, aus docspine |
| `docs/PROFILE.md` | Projektwerte und begründete Abweichungen | ja |
| `AGENTS.md` | Einstieg für KI-Agenten: wo was steht, wie geprüft wird | ja |
| `.agents/skills/spine-*` | geführte Abläufe für KI-Agenten | nein, aus docspine |
| `.agents/skills/<andere>` | projekteigene Abläufe | ja |
| `.claude/` und ähnliche | werkzeugspezifische Einstellungen; verweisen nur auf `AGENTS.md` | ja |

Was aus docspine kommt, wird beim Aktualisieren des Standards überschrieben.
Änderungen daran gehören nach docspine, nicht ins Projekt.

Alle Regeln stehen in Dateien im Repository. Werkzeugspezifische Dateien dürfen ihre
Nutzung erleichtern, aber keine eigenen Regeln enthalten. Probe: Wird ein
werkzeugspezifischer Ordner gelöscht, darf keine Regel verloren gehen.

`AGENTS.md` darf keine Architekturinhalte enthalten. Es verweist in das Dokument.

### 2.3 Profil

`PROFILE.md` hat dieses Frontmatter:

```yaml
---
docspine: 0.1               # Version des Standards
language: de                # Sprache aller Dokumente
statement_language: en      # Sprache der Requirement-Statements, Standard en
sources:                    # zulässige Werte für die Quelle eines Requirements
  - BiPRO 421 TAA v2.x
---
```

Unter dem Frontmatter stehen die Abweichungen von diesem Standard, jede mit Begründung.
Eine leere Liste ist der Normalfall.

### 2.4 Sprache

| Was | Sprache |
|---|---|
| Texte, Überschriften, `title`, `rationale` | `language` |
| generierte Bereiche und Ansichten | `language` |
| `statement` eines Requirements | `statement_language` (Standard `en`, weil WHEN und IF in vielen Sprachen verschwimmen) |
| Ordner- und Dateinamen | Englisch |
| Frontmatter-Schlüssel und -Werte | Englisch |

### 2.5 IDs

| Artefakt | ID | Datei |
|---|---|---|
| Epic | `E-<NAME>`, Großbuchstaben, sprechend, nicht nummeriert | `01-goals/epics/E-<NAME>.md` |
| Story | `US-NNNN` | `01-goals/stories/US-NNNN.md` |
| Requirement | `REQ-NNNN` | `01-goals/requirements/REQ-NNNN.md` |
| Entscheidung | `ADR-NNNN` | `09-decisions/ADR-NNNN.md` |

`NNNN` sind vier Ziffern mit führenden Nullen. Ein neues Artefakt bekommt die nächste
freie Nummer. Die `id` im Frontmatter muss zum Dateinamen passen.

## 3 Artefakte

Alle Quelldateien sind Markdown. Artefakte mit ID haben YAML-Frontmatter.

### 3.1 Vision

`01-goals/vision.md`, ohne Frontmatter. Abschnitte:

| Abschnitt | Pflicht |
|---|---|
| Kernsatz: die Vision in einem Satz | ja |
| Problem | nein |
| Zielgruppe und Stakeholder | nein |
| Erfolg: woran wir erkennen, dass es funktioniert | nein |
| Nicht-Ziele: was bewusst nicht dazugehört | nein |
| Qualitätsziele | nein |
| Themen: Link auf `01-goals/README.md` | nein |

Fehlende Antworten werden als `UNKNOWN — offene Frage: …` geschrieben. Die Vision ist
stabiler Text und enthält keine Statusangaben.

### 3.2 Epic

```yaml
---
id: E-NAME
title: <Kurztitel>
---
```

Inhalt: was das Thema umfasst und warum. Ein Epic hat kein Feld `status`; sein Status
wird aus seinen Stories abgeleitet (Abschnitt 3.3). Die Liste seiner Stories ist ein
generierter Bereich.

### 3.3 Story

```yaml
---
id: US-NNNN
title: <Kurztitel>
epic: E-NAME                  # muss existieren
requirements: [REQ-NNNN]      # jedes muss existieren; [] ist erlaubt
status: open
evidence: []                  # optional: Pfade, die die Story belegen
superseded_by: ADR-NNNN       # nur bei superseded oder retired
---
```

Inhalt: `Als <Rolle> möchte ich <Ziel>, damit <Nutzen>.`, dann das Warum, dann die
Akzeptanz in der Sprache der Nutzer. Eine Story enthält keine Entscheidungen (das sind
ADRs) und keine normativen Kriterien ohne Requirement.

| `status` | Bedeutung | Belegpflicht |
|---|---|---|
| `open` | Kandidat, nicht zugesagt | keine |
| `in-progress` | Kern gebaut, Teile offen | keine |
| `verified` | vollständig umgesetzt und bestätigt | `requirements` oder `evidence`; jedes aufgeführte Requirement ist `implemented` |
| `superseded` | durch eine Entscheidung abgelöst, wird so nicht gebaut | `superseded_by` |
| `retired` | war umgesetzt, entfernt | `superseded_by` |

Eine Story ohne Requirements ist erlaubt. Sie wird über `evidence` belegt, zum Beispiel
durch einen UI-Test, den der Requirement-Mechanismus nicht abdeckt.

Der abgeleitete Status eines Epics: `verified`, wenn alle seine Stories `verified`
sind, `open`, wenn keine begonnen ist, sonst `in-progress`. Stories mit `superseded`
oder `retired` zählen dabei nicht.

### 3.4 Requirement

```yaml
---
id: REQ-NNNN
statement: <genau ein EARS-Muster, in statement_language>
obligation: MUST | SHOULD | WILL
status: proposed
category: quality             # optional: kennzeichnet eine Qualitätsanforderung
source: <externe Norm, leer bei Eigenanforderung>   # muss im Profil stehen
confidence: unverified        # nur ohne Testergebnisse, siehe unten
evidence: []                  # Pfade zu Umsetzung und Nachweis
verification: <wie die Erfüllung geprüft wird>      # optional
supersedes: REQ-NNNN          # optional
superseded_by: REQ-NNNN | ADR-NNNN   # nur bei superseded
rationale: >-
  <warum, in language>
---
```

Inhalt: eine Überschrift mit ID und Kurztitel, dann ein bis drei Sätze Kontext.

**EARS-Muster.** Das Statement folgt genau einem Muster:

| Muster | Form |
|---|---|
| immer gültig | `The <system> shall <response>.` |
| ereignisgesteuert | `WHEN <trigger>, the <system> shall <response>.` |
| zustandsgesteuert | `WHILE <state>, the <system> shall <response>.` |
| unerwünschtes Verhalten | `IF <condition>, THEN the <system> shall <response>.` |
| optionales Merkmal | `WHERE <feature>, the <system> shall <response>.` |

**Verbindlichkeit.** `MUST` ist zwingend, `SHOULD` empfohlen, `WILL` eine erklärte
Absicht. EARS kennt keine Verbindlichkeitsstufe, deshalb das eigene Feld. In
deutschsprachigen Ansichten erscheinen die Werte als MUSS, SOLLTE und WIRD.

**Quelle.** Externe Normen ändern sich unabhängig. Ändert sich eine, müssen alle
betroffenen Requirements in einer Minute zu finden sein.

| `status` | Bedeutung | Regel |
|---|---|---|
| `proposed` | Kandidat, nicht zugesagt | keine |
| `planned` | zugesagt, nicht (vollständig) gebaut | kein bestandenes Testergebnis |
| `implemented` | gebaut | bestandenes Testergebnis **oder** `evidence` |
| `rejected` | verworfen, nie gebaut | keine |
| `superseded` | durch ein Requirement oder eine Entscheidung abgelöst | `superseded_by` |

Ein Requirement ist atomar; es gibt kein `in-progress`. Teilweise gebaut heißt
`planned`. Kommt das oft vor, ist das Requirement zu grob geschnitten.

Ein neues Requirement ist nie `implemented`.

**Konfidenz.** Ist die Aussage gegen das laufende System geprüft?
`verified | unverified | contradicted`.
- Gibt es Testergebnisse zum Requirement (Abschnitt 8.1), wird `confidence` nicht
  gepflegt; das Prüfwerkzeug leitet sie ab.
- Sonst wird sie von Hand gepflegt. `verified` verlangt dann `evidence` und
  `verification`.

**Qualitätsanforderungen** tragen `category: quality`. Kapitel 10 wird aus ihnen
erzeugt.

### 3.5 Entscheidung (ADR)

```yaml
---
id: ADR-NNNN
title: <Kurztitel>
status: proposed | accepted | rejected | superseded
date: JJJJ-MM-TT              # Datum der Entscheidung
supersedes: ADR-NNNN          # optional
superseded_by: ADR-NNNN       # nur bei superseded
requires: [REQ-NNNN]          # optional: prüfbare Folgen
---
```

Abschnitte:

| Abschnitt | Pflicht |
|---|---|
| Kontext: das Problem, die Zwänge, der Ist-Zustand | ja |
| Entscheidung: was gilt; verworfene Alternativen mit kurzem Grund, falls es welche gab | ja |
| Begründung: warum diese Option | nein, darf in Kontext oder Entscheidung stehen |
| Konsequenzen: auch die unbequemen | ja |

Ein ADR auf `proposed` ist in Diskussion und darf direkt geändert werden. Ab
`accepted` ist er unveränderlich und wird nur noch abgelöst.

### 3.6 Baustein

`05-building-blocks/<name>.md`:

```yaml
---
title: <Name des Bausteins>
path: [<Code-Pfad>, …]        # wo der Baustein im Code liegt
---
```

Inhalt: Verantwortung, Schnittstellen, wichtige Interna. Die Requirements, die der
Baustein umsetzt, sind ein generierter Bereich (Abschnitt 4).

### 3.7 Laufzeitszenario

`06-runtime/<name>.md`:

```yaml
---
title: <Name des Szenarios>
stories: [US-NNNN]            # optional: Stories, die das Szenario umsetzt
---
```

### 3.8 Übrige Kapitel

Kein Pflicht-Frontmatter. Ein Kapitel, das nur teilweise gefüllt ist, trägt
`arc42_status: PARTIAL` im Frontmatter. Eine fehlende Datei bedeutet, das Kapitel ist
`UNKNOWN`.

## 4 Beziehungen und generierte Bereiche

Beziehungen stehen **nur im Frontmatter, in einer Richtung**:

| Von | Feld | Nach |
|---|---|---|
| Story | `epic` | Epic |
| Story | `requirements` | Requirements |
| Laufzeitszenario | `stories` | Stories |
| ADR | `requires` | Requirements |
| Baustein | `path` | Code; Requirements werden über ihre `evidence`-Pfade zugeordnet |
| Requirement, Story, ADR | `superseded_by` | Nachfolger |

Jede andere Richtung und jeder Inhalt, der an mehr als einer Stelle erscheint, wird in
einen **generierten Bereich** innerhalb einer handgeschriebenen Datei erzeugt:

```markdown
<!-- generated:<typ> -->
…
<!-- /generated -->
```

| Typ | In | Zeigt |
|---|---|---|
| `status` | `01-goals/README.md` | Epics und Stories mit Status |
| `stories` | Epic | seine Stories mit Status |
| `requirements` | Story | Statements und Status ihrer Requirements |
| `context` | Requirement | Epic und Story, zu denen es gehört, ADRs, die es verlangen |
| `realized` | Baustein | Requirements, deren Belege unter seinem Pfad liegen |
| `scenarios` | Story | Laufzeitszenarien, die sie umsetzen |

Generierte Bereiche dürfen nicht von Hand geändert werden. Ein Bereich, der von dem
abweicht, was das Prüfwerkzeug erzeugen würde, ist ein Fehler. Bei Merge-Konflikten in
einem Bereich: den Bereich verwerfen und neu erzeugen.

Handgeschriebene Rückverweise (zum Beispiel „Teil von US-0042“) dürfen nicht
geschrieben werden.

## 5 Ändern statt umschreiben

**Requirement.** Eine inhaltliche Änderung erzeugt ein neues Requirement:
1. `REQ-MMMM` mit `supersedes: REQ-NNNN` anlegen.
2. In `REQ-NNNN` nur `status: superseded` und `superseded_by: REQ-MMMM` setzen.
   Statement und Begründung bleiben als Historie stehen.

**Story.** Eine Story, die so nicht gebaut wird, geht auf `superseded`; eine, die
gebaut war und entfernt wird, auf `retired`. Beide nennen die Entscheidung in
`superseded_by`.

**ADR.** Eine angenommene Entscheidung wird nicht geändert. Ein neuer ADR nennt den
alten in `supersedes`; der alte bekommt `status: superseded` und `superseded_by`.

## 6 Architekturwirkung

Bei jedem neuen Requirement und jeder Änderung lautet die Frage: Muss die Architektur
etwas berücksichtigen, ändern oder entscheiden? Es gilt genau ein Verdikt:

| Verdikt | Bedeutung | Folge |
|---|---|---|
| trägt schon | die bestehende Architektur deckt es ab | nichts ändern; eine Randbedingung nennen, die die Umsetzung einhalten muss |
| berührt Kapitel | die Architektur ändert sich | das Kapitel ändern, mit Beleg und Konfidenz |
| Entscheidung fällig | es steckt eine Architekturentscheidung darin | einen ADR schreiben |
| keine Wirkung | lokal in einem Element, unterhalb der Architektur | nichts zu dokumentieren |

**Was Architektur ist:** Bausteine und ihre Abhängigkeiten, Laufzeit-Interaktionen,
Verteilung und Betrieb, Querschnittskonzepte (Sicherheit, Caching, Persistenz, …),
Qualitätsanforderungen, Risiken und alles, was eine Entscheidung ist.

**Was es meist nicht ist:** ein einzelner Endpunkt, eine UI-Komponente, ein Feld an
einer bestehenden Entität, eine Regel, eine Vorlage — solange kein Baustein, keine
Abhängigkeit, kein Konzept und keine Entscheidung berührt ist.

Die Wirkung prüfen, nicht die Größe. Ein kleines Feld kann ein Querschnittskonzept
berühren; ein großes Feature kann ganz lokal sein.

## 7 Aussagen über den Ist-Zustand

Beschreibende Aussagen in den Kapiteln 2–8 und 11 tragen ihre Konfidenz im Text:

```markdown
_(confidence: verified — OrchestratorService, REQ-0006)_
```

| Wert | Bedeutung |
|---|---|
| `verified` | gegen Code, Konfiguration oder ein belegtes Requirement geprüft |
| `unverified` | übernommen, nicht geprüft |
| `aspirational` | Zielbild, nicht gebaut |
| `contradicted` | Doku und Code widersprechen sich |

Ein Widerspruch bleibt sichtbar und wird nie still aufgelöst:

```markdown
> [!CAUTION]
> Die Doku sagt X, der Code macht Y. (contradiction)
```

Das Prüfwerkzeug listet jeden mit `(contradiction)` markierten Block in `STATUS.md`.
Wie er aufgelöst wird, entscheidet ein Mensch.

## 8 Nachweis

### 8.1 Testergebnisse

Projekte mit automatisierten Tests liefern Ergebnisse in diesem Format, in beliebig
vielen Dateien namens `req-results.json`:

```json
{
  "results": [
    { "req": "REQ-0014", "result": "passed", "test": "ProtocolInvocationServiceTest" }
  ]
}
```

`result` ist `passed`, `failed` oder `skipped`. Ein Requirement gilt als bestanden,
wenn mindestens ein Ergebnis `passed` ist und keines `failed`. Wie die Datei entsteht,
ist Sache des Projekts.

### 8.2 Statuswechsel

Wenn ein Requirement besteht: `status: implemented` setzen und die Pfade zu Umsetzung
und Test in `evidence` ergänzen. Die Story auf `verified` setzen, sobald alle ihre
Requirements `implemented` sind. Statement, Begründung und Titel bleiben unverändert.

Ohne Testergebnisse belegen `evidence` und `verification` das Requirement, und
`confidence` wird von Hand gesetzt.

### 8.3 Ist der Nachweis ehrlich?

Ein bestandener Test ist die Eintrittskarte, nicht der Nachweis. Für jedes umgesetzte
Requirement: das Statement in seine Klauseln zerlegen (Auslöser oder Bedingung, und
Reaktion) und prüfen, welche Klauseln die Assertions des Tests tatsächlich ausüben.

| Verdikt | Bedeutung |
|---|---|
| voll | jede Klausel wird gegen echtes Verhalten ausgeübt |
| teil | der Kern läuft, eine Klausel oder die eigentliche Akzeptanz wird nicht ausgeübt |
| hohl | der Test trägt die ID, übt das Verhalten aber nicht aus |

Ein Fund ist entweder eine **Test-Lücke** (Test nachschärfen) oder ein
**Requirement-Defekt** (falscher Akteur, nicht prüfbar, überladene Klausel). Ein
Requirement-Defekt wird durch Ablösen des Requirements behoben, nicht durch einen
Test, der eine falsche Aussage festschreibt.

## 9 Diagramme

Diagramme liegen immer als Textquelle im Repository, nie nur als Bild.

- **ASCII** in einem Codeblock auf Einstiegsseiten (`README.md`, Übersichten), die als
  Erstes und in jeder Umgebung geöffnet werden.
- **Mermaid** in den Kapiteln, für Abläufe, Klassen- und Domänenmodelle,
  Zustandsautomaten.
- **DOT oder PlantUML mit eingechecktem SVG** unter `docs/diagrams/` für große
  Übersichten, bei denen das Layout von Mermaid nicht reicht. Das SVG darf nicht älter
  sein als seine Quelle.
- **Bilder ohne Quelle** nur, wo es keine geben kann, etwa bei Screenshots.

## 10 Altbestand

Gilt nur, solange `docs/legacy/` existiert.

- Aussagen aus dem Altbestand kommen mit `confidence: unverified` und
  `derived_from: <Pfad und Zeilenbereich>` in die Doku.
- Drei Quellen, drei Geltungsgrade: Der **Code** sagt, was passiert, der
  **Altbestand**, was einmal gedacht war, ein **Mensch**, was gilt.
- Ein Dokument oder Abschnitt des Altbestands darf erst entfernt werden, wenn alle vier
  Bedingungen erfüllt sind:
  1. Sein Inhalt ist übernommen: jede tragende Aussage steht in der neuen Struktur.
  2. Seine Verweise sind umgehängt: kein `derived_from` zeigt mehr darauf.
  3. Er ist nicht die einzige Quelle: der Inhalt existiert nachweislich anderswo.
  4. Ein Mensch hat das Entfernen freigegeben.
- Beim Entfernen wird `derived_from` durch `<name>-Altbestand (Git-History)` ersetzt.

## 11 Prüfwerkzeug

Das Prüfwerkzeug ist ein Kommandozeilenwerkzeug, das ohne Build-System läuft:

- `check` — prüft alles Folgende und bricht bei jedem Fehler ab.
- `render` — schreibt generierte Bereiche und Ansichten.

**Fehler:**

| # | Fehler |
|---|---|
| 1 | Pflichtfeld im Frontmatter fehlt, oder Wert nicht zulässig |
| 2 | ID passt nicht zum Dateinamen oder ist doppelt vergeben |
| 3 | Verweis auf eine ID, die es nicht gibt |
| 4 | `source` steht nicht im Profil |
| 5 | Story `verified` ohne `requirements` und ohne `evidence` |
| 6 | Story `verified` verweist auf ein Requirement, das nicht `implemented` ist |
| 7 | `superseded` oder `retired` ohne `superseded_by` |
| 8 | Requirement `implemented` ohne bestandenes Testergebnis und ohne `evidence` |
| 9 | Requirement `planned` oder `proposed`, aber ein bestandenes Testergebnis existiert |
| 10 | Testergebnis zu einem Requirement, das es nicht gibt |
| 11 | generierter Bereich weicht vom erzeugten Stand ab |
| 12 | Diagrammbild älter als seine Quelle |
| 13 | relativer Link führt ins Leere |

**Generierte Ansichten:**

| Datei | Inhalt |
|---|---|
| `01-goals/README.md` | Epics und Stories mit Status |
| `STATUS.md` | Zahlen, offene Kapitel, Widersprüche, offene Fragen (`UNKNOWN`) |
| `10-quality.md` | alle Requirements mit `category: quality` |

## 12 Begriffe

Übersetzungen dieses Standards verwenden diese Begriffe.

| English | Deutsch |
|---|---|
| acceptance | Akzeptanz |
| architecture impact | Architekturwirkung |
| building block | Baustein |
| checker | Prüfwerkzeug |
| confidence | Konfidenz |
| controlling files | steuernde Dateien |
| core statement | Kernsatz |
| decision (ADR) | Entscheidung (ADR) |
| epic | Epic |
| evidence | Beleg |
| generated region | generierter Bereich |
| legacy documentation | Altbestand |
| non-goal | Nicht-Ziel |
| obligation | Verbindlichkeit |
| open question | offene Frage |
| profile | Profil |
| proof | Nachweis |
| proof required | Belegpflicht |
| rationale | Begründung |
| requirement | Requirement, Anforderung |
| requirement defect | Requirement-Defekt |
| runtime scenario | Laufzeitszenario |
| source (norm) | Quelle |
| story | Story |
| supersede | ablösen |
| test gap | Test-Lücke |
| test result | Testergebnis |
| verdict: full / partial / hollow | Verdikt: voll / teil / hohl |
