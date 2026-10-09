---
title: Umnummerieren
path: [cli/docspine/renumber.py]
---

# Umnummerieren

**Verantwortung.** Der Befehl `renumber OLD NEW`: gibt einem Artefakt eine neue ID und
ändert jeden Verweis darauf unter `docs/`. Gebraucht wird das, wenn zwei Branches
dieselbe Nummer vergeben haben (Standard 2.7, ADR-0021). Fundstellen außerhalb von
`docs/`, etwa Testnamen, werden nur gemeldet, nicht geändert. _(confidence: verified —
cli/docspine/renumber.py, REQ-0034, REQ-0035, REQ-0036)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0034](../01-goals/requirements/REQ-0034.md) WHEN renumber runs with an existing ID and a free ID of the same kind, the checker shall rename the artifact's file and replace the old ID by the new one in every file under docs/.
- [REQ-0035](../01-goals/requirements/REQ-0035.md) IF renumber is given an ID that does not exist, a new ID that already exists, or two IDs of different kinds, THEN the checker shall change nothing and exit with a non-zero status.
- [REQ-0036](../01-goals/requirements/REQ-0036.md) WHEN renumber has run, the checker shall list the files outside docs/ that still contain the old ID, without changing them.
- [REQ-0051](../01-goals/requirements/REQ-0051.md) IF renumber is asked to give a risk an ID with a different prefix, THEN the CLI shall refuse and change nothing.
<!-- /generated -->
