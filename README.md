# docspine

Ein gemeinsamer Dokumentationsstandard mit Traceability-Gate für Projekte, die
ihre Doku als Code führen: **Vision → Epic → Story → Requirement**, arc42 und
ADRs, verbunden über unveränderliche IDs und vom Build geprüft.

docspine dokumentiert sich selbst in Anlehnung an arc42, so wie es das für jedes
Projekt vorsieht. Einstieg: **[docs/README.md](docs/README.md)**.

## Quickstart

Im Verzeichnis des Projekts ausführen:

```
curl -fsSL https://github.com/flaechsig/docspine/archive/refs/heads/dist.tar.gz | tar -xz --strip-components=1
```

Danach Claude Code im Projekt starten und das Projekt in ein, zwei Sätzen beschreiben:

```
/spine-init Ich möchte ein Programm (Java) erstellen, das die Nachricht "Hello World!" ausgibt. Damit möchte ich Nutzern von docspine zeigen, wie es verwendet wird.
```

`spine-init` fragt nach der Sprache der Dokumentation, schlägt Vision, Themen und erste
Stories vor und legt nach deiner Freigabe die Dokumentation unter `docs/` an.

**Aktualisieren:** dieselbe `curl`-Zeile erneut ausführen, danach `/spine-init` aufrufen.

**Voraussetzungen:** `curl` und `tar` (unter Linux, macOS und Windows 10/11 vorhanden),
Python 3.9 oder neuer für das Prüfwerkzeug. Die Skills liegen nach der Installation unter
`.agents/skills/` und folgen dem offenen Agent-Skills-Standard, auch für andere
KI-Werkzeuge.

## Lizenz

[0BSD](LICENSE): Jeder darf docspine ohne Bedingungen nutzen, kopieren, ändern und
weitergeben. Das eingebettete PyYAML steht unter seiner eigenen MIT-Lizenz
([cli/docspine/_vendor/PyYAML-LICENSE](cli/docspine/_vendor/PyYAML-LICENSE)).
