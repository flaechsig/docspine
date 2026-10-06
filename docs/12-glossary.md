# Glossar

Begriffe, die nicht jeder kennt, kurz erklärt. Die Regeln dazu stehen im Standard; welche
englischen Begriffe welchen deutschen entsprechen, regelt Standard 12.

| Begriff | Bedeutung |
|---|---|
| ADR | Architecture Decision Record: eine Entscheidung mit Kontext, Alternativen und Begründung, eine Datei je Entscheidung (Standard 3.5) |
| Agent Skills | offener Standard für Anleitungen an KI-Agenten, ein Ordner mit `SKILL.md` je Skill; von vielen KI-Werkzeugen gelesen |
| `AGENTS.md` | werkzeugübergreifender Einstieg für KI-Agenten im Wurzelverzeichnis eines Repos |
| Altbestand | übernommene alte Doku unter `docs/legacy/`, bis sie überführt ist (Standard 10) |
| arc42 | verbreitete Gliederung für Architekturdoku in zwölf Kapiteln; docspine folgt ihr (ADR-0007) |
| Beleg | Pfad, der zeigt, wo etwas umgesetzt oder nachgewiesen ist (Feld `evidence`) |
| EARS | Easy Approach to Requirements Syntax: wenige Satzmuster (WHEN, WHILE, IF … THEN, WHERE), mit denen ein Requirement eindeutig und prüfbar wird (Standard 3.4) |
| Epic, Story, Requirement | die Beschreibungshierarchie: Thema, Bedürfnis eines Nutzers, prüfbare Einzelaussage (Standard 3.2 bis 3.4) |
| Frontmatter | YAML-Block zwischen `---` am Anfang einer Markdown-Datei mit ID, Status und Beziehungen |
| Generierter Bereich | markierter Abschnitt in einer Datei, den `render` schreibt und `check` vergleicht; nie von Hand ändern ([Konzept](08-concepts/generierte-bereiche.md)) |
| Hohler Test | Test, der die Requirement-ID im Namen trägt, aber nicht prüft, was das Requirement fordert (Verdikt „hohl“, Standard 8.3) |
| JUnit-XML | Format für Testberichte, das fast jedes Test-Framework schreiben kann; daraus liest die Prüfung die Testergebnisse ([Konzept](08-concepts/nachweis.md)) |
| Kaltstart | Ein Agent ohne Skills und Vorwissen bekommt nur Repo und Aufgabe; belegt, dass die Regeln in normalen Dateien stehen (US-0011) |
| Konfidenz | wie sicher eine Aussage über den Ist-Stand ist: `verified`, `unverified`, `aspirational`, `contradicted` (Standard 7) |
| Nachweis | Beleg, dass ein Requirement erfüllt ist: ein bestandener Test oder ein Beleg von Hand (Standard 8) |
| Profil | `.docspine/PROFILE.md`: die Werte eines Projekts und seine begründeten Abweichungen vom Standard (Standard 2.3) |
| Prüfwerkzeug | `docspine.pyz`: prüft die Doku (`check`), erzeugt generierte Bereiche (`render`) und mehr ([Bausteine](05-building-blocks/kommandozeile.md)) |
| Verbindlichkeit | wie bindend ein Requirement ist: `MUST` (bindend), `SHOULD` (empfohlen), `WILL` (erklärte Absicht) (Standard 3.4) |
| Zweig `dist` | Git-Zweig, der nur die ausgelieferten Dateien enthält; daraus installieren Projekte ([Verteilung](07-deployment.md)) |
