---
title: Versionshinweis beim Start eines Skills
stories: [US-0018]
---

# Versionshinweis beim Start eines Skills

```mermaid
sequenceDiagram
    participant S as Skill
    participant V as docspine version
    participant C as Cache
    participant G as GitHub, Zweig dist
    S->>V: version
    V->>C: Ergebnis jünger als ein Tag?
    alt ja
        C-->>V: Changelog
    else nein oder --now
        V->>G: CHANGELOG.md abrufen, höchstens 5 s
        G-->>V: Changelog
        V->>C: speichern
    end
    V-->>S: aktuell oder neuere Version mit Einträgen
    S->>S: bei neuerer Version anbieten einzuspielen
```

1. Die Arbeits-Skills (`spine-require`, `-impact`, `-decide`, `-build`, `-prove`,
   `-gate`) rufen den Befehl als Erstes auf.
2. Ist eine neuere Version da, nennt der Skill sie mit der Release-Note und bietet an,
   sie auf einem eigenen Branch einzuspielen ([Installation und Update](installation-und-update.md)).
   Er fragt vorher, weil Dateien von außen geholt werden.
3. Ohne Netz meldet der Befehl, dass er nicht prüfen konnte, und der Skill arbeitet
   weiter.

_(confidence: verified — cli/docspine/version.py, skills/spine-require/SKILL.md,
REQ-0042, REQ-0043, REQ-0044, ADR-0025)_
