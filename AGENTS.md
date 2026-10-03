# AGENTS.md

Einstieg für KI-Agenten in dieses Repo.

## Was das hier ist

docspine ist ein Dokumentationsstandard mit Prüfwerkzeug und Skills. Das Repo enthält
die Quelle des Standards und dokumentiert sich selbst danach.

## Wo was steht

- `docs/README.md`: Deckblatt und Inhaltsverzeichnis, Lesereihenfolge
- `docs/PROFILE.md`: Projektwerte und Abweichungen vom Standard
- `docs/01-goals/`: Vision, Epics, Stories, Requirements
- `docs/09-decisions/`: Entscheidungen (ADRs). Solange es keine `STANDARD.md` gibt,
  sind sie die Regeln.

## Regeln für Änderungen

- Sprache aller Dokumente: Deutsch. Ordner, Dateinamen und Frontmatter: Englisch.
- IDs (`ADR-NNNN`, `US-NNNN`, `REQ-NNNN`, `E-<NAME>`) sind unveränderlich.
- Ein ADR auf `proposed` darf geändert werden, ab `accepted` nur noch abgelöst.
- Jede Änderung auf einem eigenen Branch (`docs/…`, `feat/…`, `fix/…`), Merge nach
  `main` mit `--no-ff`.
- Ein Gate gibt es noch nicht. Verweise und Frontmatter von Hand prüfen.
