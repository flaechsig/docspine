# docspine

docspine ist eine Arbeitsweise für die Entwicklung, bei der die Dokumentation das
Rückgrat bildet: von der Vision über Anforderungen und Entscheidungen bis zu Code und
Nachweis, verbunden über feste IDs und vom Build geprüft. **Spezifizieren und Bauen**
lassen sich getrennt nutzen: Man kann sich erst durch die ganze Spezifikation arbeiten
und dann in Schüben bauen, oder jedes Requirement gleich umsetzen.

Ausgelegt ist docspine für eine Person oder ein kleines Team bis etwa fünf Personen:
Jede Änderung entsteht auf einem eigenen Branch, IDs werden erst auf dem Hauptzweig
endgültig, und gleichzeitig vergebene Nummern löst ein Befehl auf, der alle Verweise
mitzieht.

docspine dokumentiert sich selbst in Anlehnung an arc42, so wie es das für jedes
Projekt vorsieht. Einstieg: **[docs/README.md](docs/README.md)**.

## Quickstart

Im Verzeichnis des Projekts ausführen:

```
curl -fsSL https://github.com/flaechsig/docspine/archive/refs/heads/dist.tar.gz | tar -xz --strip-components=1
```

Für den ersten Durchlauf, von der Installation bis zum ersten geprüften Requirement,
etwa 30 Minuten einplanen.

Danach Claude Code im Projekt starten und aufrufen:

```
/spine-init
```

`spine-init` fragt nach der Sprache der Dokumentation und nach einer kurzen Beschreibung
des Projekts, zum Beispiel:

```
Ich möchte ein Programm (Java) erstellen,
das die Nachricht "Hello World!" ausgibt.
Damit möchte ich Nutzern von docspine zeigen,
wie es verwendet wird.
```

Daraus schlägt der Skill Vision, Themen und erste Stories vor und legt nach deiner
Freigabe die Dokumentation unter `docs/` an.

**Lesen:** Die Doku ist Markdown mit Mermaid-Diagrammen. Gut lesen lässt sie sich auf
GitHub, in der Markdown-Vorschau einer IDE oder in einem Markdown-Leser wie
[Obsidian](https://obsidian.md): dort den Ordner `docs/` als Vault öffnen und
`docs/.obsidian/` in die `.gitignore` eintragen.

**Bestehendes Projekt:** Hat das Projekt schon Code oder Doku, nach der Installation
`/spine-adopt` statt `/spine-init` aufrufen. Der Skill nimmt den Bestand auf, schlägt für
jeden Teil ein Ziel vor und zieht die Doku nach deiner Freigabe auf einem eigenen Branch
um; danach bindet `/spine-gate` Build und Tests an. Liegen schon eigene Skills unter
`.claude/skills/`, vor der Installation `git mv .claude/skills .agents/skills` ausführen,
damit die Installation dort ihren Verweis anlegen kann.

**Aktualisieren:** dieselbe `curl`-Zeile erneut ausführen, danach `/spine-update` aufrufen.
Ob es eine neuere Version gibt, zeigt `python3 .docspine/docspine.pyz version`; die
Skills sehen damit höchstens einmal am Tag von selbst nach.

**Anbindung an Build und Tests:** je Werkzeugkette in [integrations/](integrations/),
zuerst [Maven mit JUnit 5](integrations/maven-junit5.md).

**Voraussetzungen:** Git und Python 3.9 oder neuer (für das Prüfwerkzeug); für die
Installation `curl` und `tar` (unter Linux, macOS und Windows 10/11 vorhanden).
Wer DOT- oder PlantUML-Diagramme ändert, braucht zusätzlich Graphviz bzw. PlantUML
(Befehl `diagram`). Alle Abhängigkeiten: [docs/02-constraints.md](docs/02-constraints.md).
`spine-init` legt das Git-Repository an, falls es noch keins gibt. Die Skills liegen nach der Installation unter
`.agents/skills/` und folgen dem offenen Agent-Skills-Standard, auch für andere
KI-Werkzeuge.

## Lizenz

[0BSD](LICENSE): Jeder darf docspine ohne Bedingungen nutzen, kopieren, ändern und
weitergeben. Das eingebettete PyYAML steht unter seiner eigenen MIT-Lizenz
([cli/docspine/_vendor/PyYAML-LICENSE](cli/docspine/_vendor/PyYAML-LICENSE)).
