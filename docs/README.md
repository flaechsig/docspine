# docspine — Dokumentation

Das Eingangstor. Es erklärt, *warum* es docspine gibt und *wo* du weiterliest.

## Warum es das gibt

tarifnova, blocpress und 3dPacMan folgen derselben Doku-Methodik. Bisher wird
sie kopiert, und die Kopien laufen auseinander:

- `CONVENTIONS.md` existiert dreimal mit abweichenden Status-Werten und ADR-Nummern.
- Der Generator (`*-req-check`, 1166 Zeilen) liegt in tarifnova und blocpress
  identisch vor, nur mit anderem Package. 3dPacMan hat gar keinen.
- Die Skills (`adr`, `anforderung`, `arc42`, …) sind kopiert und leicht verschieden.

Innerhalb eines Projekts fehlt dazu ein Weg, Inhalte einzublenden statt sie zu
kopieren. So zeigt eine Story heute nur die IDs ihrer Requirements, und Rückverweise
werden von Hand doppelt gepflegt.

docspine macht daraus **einen** versionierten Standard: einen Kern, den alle Projekte
teilen, und ein kurzes Profil pro Projekt.

## Der rote Faden

| Du willst wissen …                        | … dann hier                                              |
| ----------------------------------------- | -------------------------------------------------------- |
| **Die tragenden Entscheidungen**          | [architecture/decisions/](architecture/decisions/)       |
| **Was offen ist / was als Nächstes kommt** | [planning/ROADMAP.md](planning/ROADMAP.md)               |

Die Spec-Schicht (`spec/`) und arc42 (`architecture/`) werden gefüllt, sobald die
offenen Punkte der Roadmap entschieden sind.

## Entscheidungen bisher

- [ADR-0001](architecture/decisions/ADR-0001.md): Markdown mit Frontmatter als einziges Quellformat
- [ADR-0002](architecture/decisions/ADR-0002.md): Diagramme als Textquelle
- [ADR-0003](architecture/decisions/ADR-0003.md): Beziehungen nur nach unten, alles andere generiert
- [ADR-0004](architecture/decisions/ADR-0004.md): Standard als versioniertes Paket mit Projektprofil
