---
title: Auslieferung
path: [cli/build.py]
---

# Auslieferung

**Verantwortung.** Baut das Prüfwerkzeug als eine Datei `docspine.pyz` und stellt
zusammen, was ein Projekt bekommt. _(confidence: verified — cli/build.py, REQ-0015)_

**Schnittstelle.**

| Aufruf | Wirkung |
|---|---|
| `python3 cli/build.py` | baut `cli/dist/docspine.pyz` |
| `python3 cli/build.py dist` | schreibt die Auslieferung als Commit auf den Zweig `dist` und setzt den Tag `v<version>` |
| `python3 cli/build.py install <projekt>` | schreibt den Stand der Arbeitskopie in ein Projekt, zum Erproben vor einem Release |

**Innen.** Die Datei `docspine.pyz` hat feste Zeitstempel, damit dieselben Quellen immer
dieselbe Datei ergeben. Vor einem Commit auf `dist` prüft der Baustein, dass Standard,
README und Prüfwerkzeug dieselbe Version nennen und dass eine geänderte Auslieferung
eine neue Version hat (ADR-0017). Was ausgeliefert wird, steht in
[Verteilung](../07-deployment.md). _(confidence: verified — cli/build.py)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0015](../01-goals/requirements/REQ-0015.md) The checker shall run as a single file with Python 3.9 or later without installing further packages.
<!-- /generated -->
