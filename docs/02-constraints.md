# Randbedingungen

Was docspine voraussetzt und wovon es abhängt.

## Werkzeuge

| Werkzeug | Wofür | Pflicht | Festgelegt in |
|---|---|---|---|
| Git | Branches, unveränderliche IDs, Nachweis über die History | ja | Standard 2.6 |
| Python 3.9 oder neuer, nur Standardbibliothek | das Prüfwerkzeug `docspine.pyz` | ja | Standard 2.6, ADR-0012, REQ-0015 |
| PyYAML | Frontmatter lesen | eingepackt, keine Installation | ADR-0012, REQ-0015 |
| `curl` und `tar` | Installation und Update von docspine | ja, für die Installation | README |
| Graphviz (`dot`) | Befehl `diagram` für DOT-Quellen | nur wer DOT-Diagramme ändert | ADR-0024 |
| PlantUML | Befehl `diagram` für PlantUML-Quellen | nur wer PlantUML-Diagramme ändert | ADR-0024 |
| KI-Werkzeug mit Agent Skills, z. B. Claude Code | geführte Abläufe `spine-*` | nein, Repo und Prüfung genügen | ADR-0009 |

Werkzeuge einer Werkzeugkette (etwa JDK und Maven) setzt nicht docspine voraus, sondern
die jeweilige Integration; sie stehen im Feld `requires` ihres Kopfes
(`integrations/*.md`, ADR-0019).

## Technik

- Prüfwerkzeug als eine Datei `docspine.pyz`, ohne Build-System lauffähig (ADR-0012).
- Doku in Markdown mit Mermaid; nur große Übersichten als DOT oder PlantUML mit
  eingechecktem SVG (ADR-0002, ADR-0024).
- Skills nach dem offenen Agent-Skills-Standard (ADR-0009).
