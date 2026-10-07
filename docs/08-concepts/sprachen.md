# Sprachen

**Regel.** Welche Teile in der Projektsprache und welche englisch geschrieben werden,
legt Standard 2.4 fest (ADR-0011, ADR-0014). Kurz: Text in der Projektsprache;
Frontmatter, Datei- und Ordnernamen englisch; Statements in `statement_language`.

**Umsetzung im Prüfwerkzeug.** Feste Texte der generierten Bereiche (Überschriften,
Statusnamen, Spaltenköpfe) stehen in einer Tabelle je Sprache, heute Deutsch und
Englisch. Für jede andere Projektsprache nimmt `render` die englischen Texte.
_(confidence: verified — cli/docspine/text.py, cli/docspine/render.py)_

Meldungen der Prüfung sind immer englisch: Sie gehören zum Werkzeug, nicht zur Doku.
_(confidence: verified — cli/docspine/check.py)_

**Umsetzung in den Skills.** Die Skills sind englisch geschrieben und sprechen mit der
Person in der Projektsprache (`language` im Profil). Die README übersetzt jedes Projekt
einmal aus der englischen Quelle; Fehler 14 meldet, wenn die Übersetzung zu einer
anderen Version gehört. _(confidence: verified — skills/docspine-require/SKILL.md,
cli/docspine/check.py, REQ-0027)_

**Folge.** Eine weitere Sprache für die generierten Bereiche braucht einen Eintrag in
`cli/docspine/text.py`.
