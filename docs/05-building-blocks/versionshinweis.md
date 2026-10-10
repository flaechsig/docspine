---
title: Versionshinweis
path: [cli/docspine/version.py]
---

# Versionshinweis

**Verantwortung.** Der Befehl `version`: vergleicht die installierte Version (erste
Zeile von `.docspine/STANDARD.md`) mit der neuesten im Changelog des Zweigs `dist` und
zeigt bei einer neueren die Einträge dazwischen und die Installationszeile.
_(confidence: verified — cli/docspine/version.py, REQ-0042)_

**Innen.** Das Ergebnis liegt im Cache-Ordner des Nutzers und wird höchstens einmal am
Tag neu abgerufen. Ohne Netz gilt nach 5 Sekunden das letzte Ergebnis; der Befehl endet
nie mit Fehler, weil die Skills ihn bei jedem Start aufrufen
([Versionshinweis beim Start eines Skills](../06-runtime/versionshinweis.md)).
_(confidence: verified — cli/docspine/version.py, REQ-0043, REQ-0044, ADR-0025)_

## Umgesetzte Requirements

<!-- generated:realized -->
- [REQ-0042](../01-goals/requirements/REQ-0042.md) WHEN the command `version` is run, the CLI shall report the installed version and the newest released version and, if the newest is newer, the changelog entries of the versions in between.
- [REQ-0043](../01-goals/requirements/REQ-0043.md) WHILE the last successful lookup is less than one day old, the CLI shall answer the command `version` from a cache in the user's cache folder without network access, unless the option `--now` is given.
- [REQ-0044](../01-goals/requirements/REQ-0044.md) IF the newest version cannot be fetched within 5 seconds, THEN the CLI shall report that it could not check, show the last cached result if there is one, and exit with code 0.
- [REQ-0067](../01-goals/requirements/REQ-0067.md) WHEN the version command answers from its cache, the CLI shall name the date and time of the last check.
<!-- /generated -->
