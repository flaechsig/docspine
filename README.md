# docspine

docspine ist eine Arbeitsweise für die Entwicklung, bei der die Dokumentation das
Rückgrat bildet: von der Vision über Anforderungen und Entscheidungen bis zu Code und
Nachweis, verbunden über feste IDs und vom Build geprüft. **Spezifizieren und Bauen**
lassen sich getrennt nutzen: Man kann sich erst durch die ganze Spezifikation arbeiten
und dann in Schüben bauen, oder jedes Requirement gleich umsetzen.

Ausgelegt ist docspine derzeit für eine Person. Kleine Teams bis etwa fünf Personen
folgen mit Version 0.10 (Arbeit auf Branches, Umgang mit gleichzeitig vergebenen IDs).

docspine dokumentiert sich selbst in Anlehnung an arc42, so wie es das für jedes
Projekt vorsieht. Einstieg: **[docs/README.md](docs/README.md)**.

## Quickstart

Im Verzeichnis des Projekts ausführen:

```
curl -fsSL https://github.com/flaechsig/docspine/archive/refs/heads/dist.tar.gz | tar -xz --strip-components=1
```

Danach Claude Code im Projekt starten und aufrufen:

```
/spine-init
```

`spine-init` fragt nach der Sprache der Dokumentation und nach einer kurzen Beschreibung
des Projekts, zum Beispiel:

```
Ich möchte ein Programm (Java) erstellen, das die Nachricht "Hello World!" ausgibt. Damit möchte ich Nutzern von docspine zeigen, wie es verwendet wird.
```

Daraus schlägt der Skill Vision, Themen und erste Stories vor und legt nach deiner
Freigabe die Dokumentation unter `docs/` an.

**Aktualisieren:** dieselbe `curl`-Zeile erneut ausführen, danach `/spine-update` aufrufen.

**Anbindung an Build und Tests:** je Werkzeugkette in [integrations/](integrations/),
zuerst [Maven mit JUnit 5](integrations/maven-junit5.md).

**Voraussetzungen:** Git und Python 3.9 oder neuer (für das Prüfwerkzeug); für die
Installation `curl` und `tar` (unter Linux, macOS und Windows 10/11 vorhanden).
`spine-init` legt das Git-Repository an, falls es noch keins gibt. Die Skills liegen nach der Installation unter
`.agents/skills/` und folgen dem offenen Agent-Skills-Standard, auch für andere
KI-Werkzeuge.

## Lizenz

[0BSD](LICENSE): Jeder darf docspine ohne Bedingungen nutzen, kopieren, ändern und
weitergeben. Das eingebettete PyYAML steht unter seiner eigenen MIT-Lizenz
([cli/docspine/_vendor/PyYAML-LICENSE](cli/docspine/_vendor/PyYAML-LICENSE)).
