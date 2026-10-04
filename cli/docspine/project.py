"""Loading a project: profile, artifacts and test results."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from . import frontmatter

# Artifact kinds and the folder (below docs/) they live in.
KINDS = {
    "epic": "01-goals/epics",
    "story": "01-goals/stories",
    "requirement": "01-goals/requirements",
    "adr": "09-decisions",
    "block": "05-building-blocks",
    "scenario": "06-runtime",
}
ID_KINDS = ("epic", "story", "requirement", "adr")

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}
RESULTS_FILE = "req-results.json"
CONFIG = ".docspine"  # configuration: STANDARD.md, PROFILE.md, the checker


@dataclass
class Finding:
    code: int
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}: error {self.code}: {self.message}"


@dataclass
class Artifact:
    kind: str
    path: Path
    fm: dict
    body: str

    @property
    def id(self) -> Optional[str]:
        value = self.fm.get("id")
        return str(value) if value is not None else None

    def get(self, key: str, default=None):
        value = self.fm.get(key, default)
        return default if value is None else value

    def list(self, key: str) -> List[str]:
        value = self.fm.get(key)
        if value is None:
            return []
        if isinstance(value, list):
            return [str(v) for v in value]
        return [str(value)]


@dataclass
class Result:
    req: str
    result: str
    test: str
    path: str


@dataclass
class Project:
    root: Path
    profile: dict
    artifacts: List[Artifact] = field(default_factory=list)
    results: List[Result] = field(default_factory=list)
    findings: List[Finding] = field(default_factory=list)

    @property
    def docs(self) -> Path:
        return self.root / "docs"

    @property
    def config(self) -> Path:
        return self.root / CONFIG

    @property
    def language(self) -> str:
        return str(self.profile.get("language") or "en")

    def rel(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def of_kind(self, kind: str) -> List[Artifact]:
        return [a for a in self.artifacts if a.kind == kind]

    def by_id(self, kind: Optional[str] = None) -> Dict[str, Artifact]:
        return {a.id: a for a in self.artifacts if a.id and (kind is None or a.kind == kind)}

    def passed(self) -> Dict[str, bool]:
        """Requirement ID -> passed (at least one passed and none failed)."""
        outcome: Dict[str, List[str]] = {}
        for r in self.results:
            outcome.setdefault(r.req, []).append(r.result)
        return {req: ("passed" in res and "failed" not in res) for req, res in outcome.items()}


class ProjectError(Exception):
    pass


def load(root: Path) -> Project:
    root = root.resolve()
    profile_path = root / CONFIG / "PROFILE.md"
    if not profile_path.is_file():
        raise ProjectError(f"no {CONFIG}/PROFILE.md below {root}; run spine-init to set up the documentation")
    project = Project(root=root, profile={})
    try:
        profile, _ = frontmatter.parse(profile_path.read_text(encoding="utf-8"))
    except frontmatter.FrontMatterError as exc:
        project.findings.append(Finding(1, project.rel(profile_path), str(exc)))
        profile = None
    project.profile = profile or {}

    for kind, folder in KINDS.items():
        directory = project.docs / folder
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            try:
                fm, body = frontmatter.parse(path.read_text(encoding="utf-8"))
            except frontmatter.FrontMatterError as exc:
                project.findings.append(Finding(1, project.rel(path), str(exc)))
                continue
            if fm is None:
                project.findings.append(Finding(1, project.rel(path), "front matter missing"))
                continue
            project.artifacts.append(Artifact(kind, path, fm, body))

    for path in _find_results(root):
        _load_results(project, path)
    return project


def _find_results(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        if RESULTS_FILE in filenames:
            yield Path(dirpath) / RESULTS_FILE


def _load_results(project: Project, path: Path) -> None:
    rel = project.rel(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        entries = data["results"]
        for entry in entries:
            project.results.append(Result(
                req=str(entry["req"]),
                result=str(entry["result"]),
                test=str(entry.get("test", "")),
                path=rel,
            ))
    except (ValueError, KeyError, TypeError) as exc:
        project.findings.append(Finding(10, rel, f"test results cannot be read: {exc}"))
