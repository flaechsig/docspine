# docspine

> Ein Dokumentationsstandard mit Prüfwerkzeug, der Anforderungen, Architektur und
> Entscheidungen als ein nachprüfbares Dokument im Repo hält, lesbar für jede KI und
> jeden Menschen.

Dies ist das Deckblatt. Das Inhaltsverzeichnis unten ist die Lesereihenfolge.

**Stand:** Alle Entscheidungen stehen auf `proposed`, bis die Migration von 3dPacMan
sie bestätigt (US-0012). Solange dürfen sie direkt geändert werden.

## Inhalt

<!-- generated:toc -->
### 1 Ziele

- [Vision](01-goals/vision.md)

| Epic | Stories |
|---|---|
| [E-STANDARD](01-goals/epics/E-STANDARD.md) — Der Standard als lesbares Regelwerk | ⚪ [US-0001](01-goals/stories/US-0001.md) STANDARD.md schreiben · ⚪ [US-0002](01-goals/stories/US-0002.md) Regeln aus den Skills verlagern · ⚪ [US-0003](01-goals/stories/US-0003.md) JSON Schema |
| [E-GENERATOR](01-goals/epics/E-GENERATOR.md) — Prüfen und Erzeugen per CLI | ⚪ [US-0004](01-goals/stories/US-0004.md) CLI-Kern · ⚪ [US-0005](01-goals/stories/US-0005.md) Neue Prüfungen · ⚪ [US-0006](01-goals/stories/US-0006.md) Maven-Anbindung |
| [E-SKILLS](01-goals/epics/E-SKILLS.md) — Geführte Abläufe als Skills | ⚪ [US-0007](01-goals/stories/US-0007.md) spine-init · ⚪ [US-0008](01-goals/stories/US-0008.md) Methodik-Skills · ⚪ [US-0009](01-goals/stories/US-0009.md) spine-adopt · ⚪ [US-0010](01-goals/stories/US-0010.md) spine-gate · ⚪ [US-0011](01-goals/stories/US-0011.md) Kaltstart-Test |
| [E-MIGRATION](01-goals/epics/E-MIGRATION.md) — Die bestehenden Projekte umstellen | ⚪ [US-0012](01-goals/stories/US-0012.md) 3dPacMan · ⚪ [US-0013](01-goals/stories/US-0013.md) tarifnova · ⚪ [US-0014](01-goals/stories/US-0014.md) blocpress |

### 3 Kontext

- [Kontext](03-context.md)

### 9 Entscheidungen

| ADR | Thema |
|---|---|
| [ADR-0001](09-decisions/ADR-0001.md) | Markdown mit Frontmatter als einziges Quellformat |
| [ADR-0002](09-decisions/ADR-0002.md) | Diagramme als Textquelle |
| [ADR-0003](09-decisions/ADR-0003.md) | Beziehungen nur nach unten, alles andere generiert |
| [ADR-0004](09-decisions/ADR-0004.md) | Standard als versioniertes Paket, als Kopie im Projekt |
| [ADR-0005](09-decisions/ADR-0005.md) | Ein Status-Vokabular je Artefakt, Prüfstand als eigene Achse |
| [ADR-0006](09-decisions/ADR-0006.md) | Schnitt zwischen Kernstandard, Modulen und Projektprofil |
| [ADR-0007](09-decisions/ADR-0007.md) | Ein Dokument nach arc42-Gerüst |
| [ADR-0008](09-decisions/ADR-0008.md) | Artefakte verschlanken |
| [ADR-0009](09-decisions/ADR-0009.md) | Steuernde Artefakte und die Grenze zu KI-Werkzeugen |
| [ADR-0010](09-decisions/ADR-0010.md) | Skill-Familie spine-* |
| [ADR-0011](09-decisions/ADR-0011.md) | Projektsprache und englisches Maschinenvokabular |
| [ADR-0012](09-decisions/ADR-0012.md) | Generator-Kern als eigenständige CLI |
<!-- /generated -->

Die übrigen Kapitel (2, 4–8, 10–12) haben noch keinen Inhalt und existieren daher
nicht (ADR-0008).

---

Projektwerte und Abweichungen vom Standard: [PROFILE.md](PROFILE.md).
