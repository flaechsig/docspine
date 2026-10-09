"""`docspine renumber OLD NEW`: give an artifact a new ID and update every reference in docs/.

On a branch, a new ID is a reservation; it becomes final once it is on the main branch
(STANDARD 2.7). When two branches took the same number, the later one renumbers its own.
Occurrences outside docs/ (for example test names) are reported, not changed.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import List, Tuple

from .check import ID_PATTERN
from .project import KINDS, SKIP_DIRS, Project

PREFIX_KIND = {"E-": "epic", "US-": "story", "REQ-": "requirement", "ADR-": "adr",
               "R-": "risk", "SEC-": "risk", "TD-": "risk"}
SKIP_OUTSIDE = SKIP_DIRS | {"target", "build", "dist", ".docspine", "docs"}


class RenumberError(Exception):
    pass


def _kind(artifact_id: str) -> str:
    for prefix, kind in PREFIX_KIND.items():
        if artifact_id.startswith(prefix) and ID_PATTERN[kind].match(artifact_id):
            return kind
    raise RenumberError(f"'{artifact_id}' is not a valid ID")


def run(project: Project, old: str, new: str) -> Tuple[List[str], List[str]]:
    """Returns (changed files, files outside docs/ that still contain the old ID)."""
    kind = _kind(old)
    if _kind(new) != kind:
        raise RenumberError(f"'{old}' and '{new}' are different kinds of artifact")
    if old.split("-", 1)[0] != new.split("-", 1)[0]:
        # the kind of a risk changes by superseding it, not by renumbering (ADR-0029)
        raise RenumberError(f"'{old}' and '{new}' have different prefixes; supersede the risk instead")
    ids = project.by_id()
    if old not in ids:
        raise RenumberError(f"'{old}' does not exist")
    if new in ids or (project.docs / KINDS[kind] / f"{new}.md").exists():
        raise RenumberError(f"'{new}' already exists")

    word = re.compile(r"(?<![\w-])" + re.escape(old) + r"(?![\w])")
    changed = []
    source = ids[old].path
    target = source.with_name(f"{new}.md")
    source.rename(target)
    changed.append(project.rel(target))
    for path in sorted(project.docs.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        updated = word.sub(new, text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            rel = project.rel(path)
            if rel not in changed:
                changed.append(rel)

    elsewhere = []
    for dirpath, dirnames, filenames in os.walk(project.root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_OUTSIDE)
        for name in sorted(filenames):
            path = Path(dirpath) / name
            try:
                if word.search(path.read_text(encoding="utf-8")):
                    elsewhere.append(project.rel(path))
            except (UnicodeDecodeError, OSError):
                continue
    return changed, elsewhere
