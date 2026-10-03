"""`docspine render`: writes generated regions (STANDARD.md section 4)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

from .project import Artifact, Project

TEXTS: Dict[str, Dict[str, str]] = {
    "en": {
        "open": "⚪ open", "in-progress": "🟡 in progress", "verified": "✅ verified",
        "superseded": "⛔ superseded", "retired": "⚰️ retired",
        "stories": "Stories", "title": "Title", "status": "Status",
        "goals": "Goals and requirements",
    },
    "de": {
        "open": "⚪ offen", "in-progress": "🟡 in Arbeit", "verified": "✅ verifiziert",
        "superseded": "⛔ abgelöst", "retired": "⚰️ stillgelegt",
        "stories": "Stories", "title": "Titel", "status": "Status",
        "goals": "Ziele und Anforderungen",
    },
}
STATUS_ORDER = ("open", "in-progress", "verified", "superseded", "retired")


def texts(project: Project) -> Dict[str, str]:
    return TEXTS.get(project.language, TEXTS["en"])


def epic_status(stories: List[Artifact]) -> str:
    """verified if all stories are verified, open if none has started, else in-progress.

    Stories that are superseded or retired do not count.
    """
    active = {s.get("status") for s in stories if s.get("status") not in ("superseded", "retired")}
    if active == {"verified"}:
        return "verified"
    if active <= {"open"}:
        return "open"
    return "in-progress"


def _stories_of(project: Project, epic_id: str) -> List[Artifact]:
    return [s for s in project.of_kind("story") if s.get("epic") == epic_id]


def status_region(project: Project) -> str:
    t = texts(project)
    stories = project.of_kind("story")
    counts = [(t[k], sum(1 for s in stories if s.get("status") == k)) for k in STATUS_ORDER]
    lines = [f"**{len(stories)} {t['stories']}:** " + " · ".join(f"{label} {n}" for label, n in counts if n), ""]
    for epic in sorted(project.of_kind("epic"), key=lambda e: e.id or ""):
        own = _stories_of(project, epic.id)
        lines += [f"## [{epic.id}](epics/{epic.path.name}) — {epic.get('title')}", "",
                  f"{t['status']}: {t[epic_status(own)]}", "",
                  f"| Story | {t['title']} | {t['status']} |", "|---|---|---|"]
        lines += [f"| [{s.id}](stories/{s.path.name}) | {s.get('title')} | {t.get(s.get('status'), s.get('status'))} |"
                  for s in own]
        lines.append("")
    return "\n".join(lines).rstrip("\n")


def stories_region(project: Project, epic: Artifact) -> str:
    return "\n".join(f"- [{s.id}](../stories/{s.path.name}) — {s.get('title')}"
                     for s in _stories_of(project, epic.id))


def _region(kind: str) -> re.Pattern:
    return re.compile(r"(<!-- generated:" + kind + r" -->\n)(.*?)(<!-- /generated -->)", re.S)


def _write_region(path: Path, kind: str, content: str, heading: str) -> bool:
    """Replace the region's content, or append the region. Returns True if the file changed."""
    block = f"<!-- generated:{kind} -->\n{content}\n<!-- /generated -->"
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old is None:
        new = f"{heading}\n\n{block}\n"
    elif _region(kind).search(old):
        new = _region(kind).sub(lambda m: block, old, count=1)
    else:
        new = old.rstrip("\n") + f"\n\n{block}\n"
    if new == old:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def run(project: Project) -> List[str]:
    """Write all generated regions. Returns the files that changed."""
    t = texts(project)
    changed = []
    goals = project.docs / "01-goals"
    if goals.is_dir():
        readme = goals / "README.md"
        if _write_region(readme, "status", status_region(project), f"# {t['goals']}"):
            changed.append(project.rel(readme))
    for epic in project.of_kind("epic"):
        path = epic.path
        text = path.read_text(encoding="utf-8")
        if not _region("stories").search(text):
            path.write_text(text.rstrip("\n") + f"\n\n## {t['stories']}\n", encoding="utf-8")
        if _write_region(path, "stories", stories_region(project, epic), ""):
            changed.append(project.rel(path))
    return changed
