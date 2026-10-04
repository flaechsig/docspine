# Kontext

```mermaid
flowchart LR
    dev([Projektverantwortlicher])
    ai([KI-Agenten<br/>Claude Code, Codex, Cursor, …])
    ds[docspine<br/>Standard · CLI · Skills]
    p1[Ursprungsprojekt]
    p2[blocpress]
    p3[3dPacMan]

    ds -- STANDARD.md, Skills als Kopie --> p1 & p2 & p3
    ds -- CLI prüft und erzeugt --> p1 & p2 & p3
    dev -- pflegt Doku --> p1 & p2 & p3
    ai -- lesen AGENTS.md, Skills --> p1 & p2 & p3
    dev -- entwickelt --> ds
```

| Nachbar | Beziehung zu docspine |
|---|---|
| Ursprungsprojekt | Ursprung der Methodik, nicht öffentlich, Java mit Maven, eigenes Gate |
| blocpress | übernommene Methodik, Java mit Maven, AsciiDoc-Altbestand |
| 3dPacMan | 6502-Assembler, kein Maven, Doku bisher ohne Frontmatter und ohne Gate |
| KI-Agenten | lesen `AGENTS.md`, `STANDARD.md` und Skills nach dem Agent-Skills-Standard |
| GitHub | Hosting der Projekte, stellt Markdown und Mermaid direkt dar |
