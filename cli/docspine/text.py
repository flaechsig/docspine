"""Fixed texts in the project language, and helpers for reading Markdown."""

from __future__ import annotations

import re
from typing import Dict

TEXTS: Dict[str, Dict[str, str]] = {
    "en": {
        "story.open": "⚪ open", "story.in-progress": "🟡 in progress", "story.verified": "✅ verified",
        "story.superseded": "⛔ superseded", "story.retired": "⚰️ retired",
        "req.proposed": "proposed", "req.planned": "planned", "req.implemented": "implemented",
        "req.rejected": "rejected", "req.superseded": "superseded",
        "adr.proposed": "proposed", "adr.accepted": "accepted", "adr.rejected": "rejected",
        "adr.superseded": "superseded",
        "obligation.MUST": "MUST", "obligation.SHOULD": "SHOULD", "obligation.WILL": "WILL",
        "stories": "Stories", "title": "Title", "status": "Status", "obligation": "Obligation",
        "goals": "Goals and requirements", "context": "Context", "required_by": "required by",
        "scenarios": "Scenarios", "realized": "Realized requirements", "none": "none",
        "status_title": "Status", "count": "Count", "decisions": "Decisions",
        "missing_chapters": "Chapters without content", "partial_chapters": "Partly filled chapters",
        "contradictions": "Contradictions", "open_questions": "Open questions",
        "open_decisions": "Open decisions",
        "quality_title": "Quality requirements", "verification": "Verification",
        "risk.open": "open", "risk.accepted": "accepted", "risk.closed": "closed",
        "risk.superseded": "superseded",
        "severity.low": "low", "severity.medium": "medium", "severity.high": "high",
        "severity.critical": "critical", "severity": "Severity",
        "risks_title": "Risks and technical debt", "group.R": "Architecture risks",
        "group.SEC": "Security risks", "group.TD": "Technical debt", "acceptance": "Acceptance",
    },
    "de": {
        "story.open": "⚪ offen", "story.in-progress": "🟡 in Arbeit", "story.verified": "✅ verifiziert",
        "story.superseded": "⛔ abgelöst", "story.retired": "⚰️ stillgelegt",
        "req.proposed": "vorgeschlagen", "req.planned": "geplant", "req.implemented": "umgesetzt",
        "req.rejected": "verworfen", "req.superseded": "abgelöst",
        "adr.proposed": "vorgeschlagen", "adr.accepted": "angenommen", "adr.rejected": "verworfen",
        "adr.superseded": "abgelöst",
        "obligation.MUST": "MUSS", "obligation.SHOULD": "SOLLTE", "obligation.WILL": "WIRD",
        "stories": "Stories", "title": "Titel", "status": "Status", "obligation": "Verbindlichkeit",
        "goals": "Ziele und Anforderungen", "context": "Kontext", "required_by": "verlangt von",
        "scenarios": "Szenarien", "realized": "Umgesetzte Requirements", "none": "keine",
        "status_title": "Status", "count": "Anzahl", "decisions": "Entscheidungen",
        "missing_chapters": "Kapitel ohne Inhalt", "partial_chapters": "Teilweise gefüllte Kapitel",
        "contradictions": "Widersprüche", "open_questions": "Offene Fragen",
        "open_decisions": "Offene Entscheidungen",
        "quality_title": "Qualitätsanforderungen", "verification": "Prüfung",
        "risk.open": "offen", "risk.accepted": "hingenommen", "risk.closed": "behoben",
        "risk.superseded": "abgelöst",
        "severity.low": "niedrig", "severity.medium": "mittel", "severity.high": "hoch",
        "severity.critical": "kritisch", "severity": "Schwere",
        "risks_title": "Risiken und technische Schulden", "group.R": "Architekturrisiken",
        "group.SEC": "Security-Risiken", "group.TD": "Technische Schulden", "acceptance": "Akzeptanz",
    },
}

_FENCE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[^\n]*$", re.M | re.S)
_CODE_SPAN = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and code spans; examples there are not content."""
    return _CODE_SPAN.sub("", _FENCE.sub("", text))


def blank(text: str, pattern: re.Pattern) -> str:
    """Replace what `pattern` matches with spaces, keeping lines and positions."""
    return pattern.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def blank_fences(text: str) -> str:
    """Blank fenced code blocks only, keeping lines; code spans stay, IDs in them count."""
    return blank(text, _FENCE)


def blank_code(text: str) -> str:
    """Like `strip_code`, but keeps lines and positions, so a hit maps back to the text."""
    return blank(blank(text, _FENCE), _CODE_SPAN)
