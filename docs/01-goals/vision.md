# Vision

## Kernsatz

Für Entwickler und kleine Teams, die mit KI-Agenten Software entwickeln, ist docspine
eine Arbeitsweise, bei der die Dokumentation das Rückgrat bildet: Anforderungen,
Architektur und Entscheidungen bilden ein nachprüfbares Dokument im Repo, mit dem Code
und Tests verbunden sind. Anders als eine Methodik, die in Skills oder Plugins eines
Werkzeugs steckt, kann jede KI und jeder Mensch sie allein aus dem Repo aufgreifen.

## Problem

Drei Projekte (ein nicht öffentliches Ursprungsprojekt, blocpress, 3dPacMan) folgen derselben Doku-Methodik, aber
jedes hat eine eigene Kopie: Konventionen, Generator und Skills laufen auseinander.
Ein Teil der Regeln steht nur in Claude-spezifischen Skills und ist für andere
Werkzeuge unsichtbar. Spezifikation und Architektur sind getrennte Dokumente, die sich
an mehreren Stellen doppeln.

## Zielgruppe und Stakeholder

- **Projektverantwortliche**, die Doku als Code führen und mit KI-Agenten arbeiten.
  Heute: der Autor dieser drei Projekte.
- **Kleine Teams** bis etwa fünf Personen, etwa ein Scrum-Team. Mit KI-Agenten werden
  Teams kleiner; docspine soll zu dieser Arbeitsweise passen. Unterstützt ab Version 0.10.
- **KI-Agenten** (Claude Code und andere), die die Doku lesen, ergänzen und prüfen.
- **Weitere Nutzer:** docspine ist öffentlich auf GitHub, unter 0BSD. Jeder darf es
  ohne Bedingungen nutzen.

## Erfolg

- Alle drei Projekte nutzen docspine, und ihr Gate ist grün.
- Eine Änderung am Standard entsteht an einer Stelle und erreicht die Projekte über
  eine neue Version.
- Ein Agent ohne Skills erledigt eine Doku-Aufgabe allein mit Repo und Gate
  (Kaltstart-Test, ADR-0009).

## Nicht-Ziele

- Kein Generator für Websites oder Handbücher. Ein PDF ist möglich, aber nur bei Bedarf.
- Keine Bindung an ein KI-Werkzeug. Werkzeugspezifisches ist Komfort, nie
  Voraussetzung.
- Keine vollständige Doku auf Vorrat. Kapitel entstehen, wenn sie Inhalt haben.
- Keine Unterstützung großer Teams mit vielen parallelen Spezifikationen.

## Qualitätsziele

- **Portabilität:** Regeln und Inhalte sind ohne docspine-Werkzeuge lesbar und von
  jeder KI nutzbar.
- **Nachprüfbarkeit:** Was als umgesetzt gilt, entscheidet das Gate, kein Modell.

## Themen

Die Vision bricht sich in Epics herunter. Übersicht mit Stories und Status:
[01-goals](README.md).
