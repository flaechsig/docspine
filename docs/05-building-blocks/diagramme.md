---
title: Diagramme
path: [cli/docspine/diagram.py]
---

# Diagramme

**Verantwortung.** Der Befehl `diagram`: rendert DOT-Quellen mit Graphviz und
PlantUML-Quellen mit PlantUML zum SVG daneben und trägt einen Prüfwert der Quelle ins
SVG ein. Die [Prüfung](pruefung.md) vergleicht ihn mit der Quelle (Fehler 12).
_(confidence: verified — cli/docspine/diagram.py, REQ-0039, REQ-0040)_

**Innen.** Der Prüfwert ist SHA-256 über die Quelle mit vereinheitlichten Zeilenenden,
damit ein Checkout unter Windows nicht als Änderung gilt. Fehlt das Werkzeug, bricht der
Befehl mit Namen des Werkzeugs ab und lässt das alte SVG stehen. `docs/legacy/` ist
ausgenommen. _(confidence: verified — cli/docspine/diagram.py, REQ-0041, ADR-0024)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0039](../01-goals/requirements/REQ-0039.md) IF a DOT or PlantUML source under docs, outside docs/legacy, has no SVG next to it, or its SVG does not carry the checksum of the current source, THEN the checker shall report error 12.
- [REQ-0040](../01-goals/requirements/REQ-0040.md) WHEN the diagram command runs for a DOT or PlantUML source, the CLI shall render the source to an SVG next to it with Graphviz or PlantUML and record the checksum of the source in the SVG.
- [REQ-0041](../01-goals/requirements/REQ-0041.md) IF the tool needed to render a diagram source is not installed or reports an error, THEN the CLI shall stop with a message naming the tool and leave the SVG unchanged.
<!-- /generated -->
