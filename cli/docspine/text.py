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
        "quality_title": "Quality requirements", "verification": "Verification",
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
        "quality_title": "Qualitätsanforderungen", "verification": "Prüfung",
    },
}

_FENCE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[^\n]*$", re.M | re.S)
_CODE_SPAN = re.compile(r"`[^`\n]*`")


def strip_code(text: str) -> str:
    """Remove fenced code blocks and code spans; examples there are not content."""
    return _CODE_SPAN.sub("", _FENCE.sub("", text))
