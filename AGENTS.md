# AGENTS.md

Einstieg für KI-Agenten in dieses Repo.

## Was das hier ist

docspine ist ein Dokumentationsstandard mit Prüfwerkzeug und Skills. Das Repo enthält
die Quelle des Standards und dokumentiert sich selbst danach.

## Wo was steht

- `docs/README.md`: Aufbau, Arbeitsweise und zugrunde liegende Standards
- `docs/PROFILE.md`: Projektwerte und Abweichungen vom Standard
- `docs/01-goals/README.md`: Übersicht aller Epics und Stories mit Status
- `docs/01-goals/`: Vision, Epics, Stories, Requirements
- `docs/STANDARD.md`: die Regeln, die für diese Doku gelten (englisch)
- `docs/09-decisions/`: Entscheidungen (ADRs), warum die Regeln so sind
- `standard/en/`: die Quellen dessen, was docspine ausliefert (`STANDARD.md`,
  `README.md`), nur auf Englisch. `docs/STANDARD.md` ist eine unveränderte Kopie,
  `docs/README.md` eine deutsche Übersetzung nach der Begriffstabelle in Abschnitt 12.

## Regeln für Änderungen

- Sprache aller Dokumente: Deutsch. Ordner, Dateinamen und Frontmatter: Englisch.
- IDs (`ADR-NNNN`, `US-NNNN`, `REQ-NNNN`, `E-<NAME>`) sind unveränderlich.
- Ein ADR auf `proposed` darf geändert werden, ab `accepted` nur noch abgelöst.
- Jede Änderung auf einem eigenen Branch (`docs/…`, `feat/…`, `fix/…`), Merge nach
  `main` mit `--no-ff`.
- Vor jedem Commit prüfen:
  ```
  python3 cli/run_tests.py                          # Tests, schreibt cli/req-results.json
  PYTHONPATH=cli python3 -m docspine render         # generierte Bereiche erneuern
  PYTHONPATH=cli python3 -m docspine check          # muss "OK" melden
  ```
- `cli/`: die CLI in Python (nur Standardbibliothek, PyYAML eingepackt unter
  `cli/docspine/_vendor/`). `python3 cli/build.py` baut `cli/dist/docspine.pyz`.
- `skills/`: die Quellen der Skills (englisch), die docspine ausliefert.
- `python3 cli/build.py dist` schreibt den Zweig `dist`: nur die Dateien, die ein Projekt
  bekommt, an ihren Zielpfaden. Projekte installieren und aktualisieren daraus.
