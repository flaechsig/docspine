"""Test helpers: requirement tags and a small project builder."""

from __future__ import annotations

import tempfile
import textwrap
import unittest
from pathlib import Path
from typing import Dict, Optional

from docspine import check, project


def req(*ids: str):
    """Tag a test method or class with the requirement IDs it proves."""
    def mark(obj):
        obj._reqs = tuple(getattr(obj, "_reqs", ())) + ids
        return obj
    return mark


PROFILE = """\
---
docspine: 0.1
language: en
sources:
  - RFC 6749
---
"""
EPIC = """\
---
id: E-CORE
title: Core
---

# E-CORE

<!-- generated:stories -->
<!-- /generated -->
"""
STORY = """\
---
id: US-0001
title: First story
epic: E-CORE
requirements: [REQ-0001]
status: open
---

As a user I want something so that it helps.
"""
REQUIREMENT = """\
---
id: REQ-0001
statement: The system shall do something.
obligation: MUST
status: planned
source:
rationale: >-
  Because.
---

## REQ-0001 — Something
"""

VALID = {
    "docs/PROFILE.md": PROFILE,
    "docs/01-goals/epics/E-CORE.md": EPIC,
    "docs/01-goals/stories/US-0001.md": STORY,
    "docs/01-goals/requirements/REQ-0001.md": REQUIREMENT,
}


class ProjectTest(unittest.TestCase):
    """Builds a temporary project from VALID plus overrides."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, files: Dict[str, Optional[str]], base: bool = True) -> Path:
        content = dict(VALID) if base else {}
        content.update(files)
        for rel, text in content.items():
            if text is None:
                continue
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(textwrap.dedent(text), encoding="utf-8")
        return self.root

    def findings(self, files: Dict[str, Optional[str]] = None, base: bool = True):
        self.write(files or {}, base)
        return check.run(project.load(self.root))

    def codes(self, files: Dict[str, Optional[str]] = None, base: bool = True):
        return sorted({f.code for f in self.findings(files, base)})


def replace(text: str, old: str, new: str) -> str:
    assert old in text, old
    return text.replace(old, new)
