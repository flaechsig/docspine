# Eingebettete Bibliotheken

docspine liefert seine Abhängigkeiten mit, damit die CLI ohne Installation läuft
(ADR-0012, REQ-0015).

| Bibliothek | Version | Quelle | Lizenz |
|---|---|---|---|
| PyYAML | 6.0.1 | `lib/yaml/` aus dem sdist `PyYAML-6.0.1.tar.gz` (PyPI) | MIT, siehe `PyYAML-LICENSE` |

Nur der reine Python-Teil ist enthalten, ohne die C-Erweiterung.

**Eine Änderung gegenüber dem Original:** In `yaml/cyaml.py` ist der Import
`from yaml._yaml import …` relativ gemacht (`from ._yaml import …`). Sonst würde ein
systemweit installiertes PyYAML mit seiner C-Erweiterung nachgeladen und mit dieser
Fassung vermischt.

Aktualisieren: neues sdist laden, `lib/yaml/` hierher kopieren, Lizenz ersetzen, die
Änderung oben erneut anwenden, Tabelle anpassen.
