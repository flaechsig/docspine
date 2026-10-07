"""The checks of `docspine check`, one function per error class (STANDARD.md section 11)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Optional
from urllib.parse import unquote

from . import diagram, render
from .project import ID_KINDS, Artifact, Finding, Project
from .text import strip_code

STORY_STATUS = {"open", "in-progress", "verified", "superseded", "retired"}
REQ_STATUS = {"proposed", "planned", "implemented", "rejected", "superseded"}
ADR_STATUS = {"proposed", "accepted", "rejected", "superseded"}
OBLIGATION = {"MUST", "SHOULD", "WILL"}
CONFIDENCE = {"verified", "unverified", "contradicted"}
CATEGORY = {"quality"}

# kind -> (required fields, {field: permitted values}, list fields)
SCHEMA = {
    "epic": (["id", "title"], {}, []),
    "story": (["id", "title", "epic", "requirements", "status"],
              {"status": STORY_STATUS}, ["requirements", "evidence"]),
    "requirement": (["id", "statement", "obligation", "status", "rationale"],
                    {"obligation": OBLIGATION, "status": REQ_STATUS,
                     "confidence": CONFIDENCE, "category": CATEGORY}, ["evidence"]),
    "adr": (["id", "title", "status", "date"], {"status": ADR_STATUS}, ["requires"]),
    "block": (["title", "path"], {}, []),
    "scenario": (["title"], {}, ["stories"]),
}
ID_PATTERN = {
    "epic": re.compile(r"^E-[A-Z0-9][A-Z0-9-]*$"),
    "story": re.compile(r"^US-\d{4}$"),
    "requirement": re.compile(r"^REQ-\d{4}$"),
    "adr": re.compile(r"^ADR-\d{4}$"),
}


TEST_CHECKS = ("implemented_proof", "status_behind_result", "unknown_results")


def run(project: Project, with_tests: bool = True) -> List[Finding]:
    """All checks. Without tests, the checks that need test results (errors 8–10) are skipped."""
    findings = list(project.findings)
    for check in (schema, ids, references, sources, story_proof, story_requirements,
                  superseded, implemented_proof, status_behind_result, unknown_results,
                  stale_regions, diagram_images, links, readme_version, evidence_paths):
        if not with_tests and check.__name__ in TEST_CHECKS:
            continue
        findings.extend(check(project))
    return sorted(findings, key=lambda f: (f.path, f.code, f.message))


def _f(project: Project, code: int, artifact: Artifact, message: str) -> Finding:
    return Finding(code, project.rel(artifact.path), message)


def schema(project: Project) -> List[Finding]:
    """Error 1: required field missing or value not permitted."""
    out = []
    required = ["language"]
    profile_rel = project.rel(project.config / "PROFILE.md")
    for key in required:
        if not project.profile.get(key):
            out.append(Finding(1, profile_rel, f"required field '{key}' missing"))
    for key in ("sources", "test_reports"):
        if project.profile.get(key) is not None and not isinstance(project.profile[key], list):
            out.append(Finding(1, profile_rel, f"field '{key}' must be a list"))

    for a in project.artifacts:
        fields, permitted, lists = SCHEMA[a.kind]
        for key in fields:
            if key not in a.fm or a.fm[key] is None or a.fm[key] == "":
                out.append(_f(project, 1, a, f"required field '{key}' missing"))
        for key, values in permitted.items():
            value = a.fm.get(key)
            if value is not None and str(value) not in values:
                allowed = ", ".join(sorted(values))
                out.append(_f(project, 1, a, f"field '{key}' has value '{value}', permitted: {allowed}"))
        for key in lists:
            if key in a.fm and a.fm[key] is not None and not isinstance(a.fm[key], list):
                out.append(_f(project, 1, a, f"field '{key}' must be a list"))
    return out


def ids(project: Project) -> List[Finding]:
    """Error 2: ID does not match the file name, or is used twice."""
    out = []
    seen = {}
    for a in project.artifacts:
        if a.kind not in ID_KINDS or a.id is None:
            continue
        if a.id != a.path.stem:
            out.append(_f(project, 2, a, f"id '{a.id}' does not match file name '{a.path.name}'"))
        elif not ID_PATTERN[a.kind].match(a.id):
            out.append(_f(project, 2, a, f"id '{a.id}' does not follow the ID scheme for {a.kind}"))
        if a.id in seen:
            out.append(_f(project, 2, a, f"id '{a.id}' is also used by {project.rel(seen[a.id].path)}"))
        else:
            seen[a.id] = a
    return out


def references(project: Project) -> List[Finding]:
    """Error 3: reference to an ID that does not exist."""
    out = []
    epics = project.by_id("epic")
    stories = project.by_id("story")
    reqs = project.by_id("requirement")
    every = project.by_id()

    def need(a: Artifact, key: str, targets: dict, what: str):
        for ref in a.list(key):
            if ref not in targets:
                out.append(_f(project, 3, a, f"'{key}' refers to {what} '{ref}', which does not exist"))

    for a in project.artifacts:
        if a.kind == "story":
            need(a, "epic", epics, "epic")
            need(a, "requirements", reqs, "requirement")
        elif a.kind == "scenario":
            need(a, "stories", stories, "story")
        elif a.kind == "adr":
            need(a, "requires", reqs, "requirement")
        need(a, "supersedes", every, "artifact")
        need(a, "superseded_by", every, "artifact")
    return out


def sources(project: Project) -> List[Finding]:
    """Error 4: source not listed in the profile."""
    permitted = project.profile.get("sources") or []
    permitted = {str(s) for s in permitted} if isinstance(permitted, list) else set()
    out = []
    for a in project.of_kind("requirement"):
        source = a.get("source")
        if source and str(source) not in permitted:
            out.append(_f(project, 4, a, f"source '{source}' is not listed in the profile"))
    return out


def story_proof(project: Project) -> List[Finding]:
    """Error 5: story verified without requirements and without evidence."""
    return [_f(project, 5, a, "story is verified without requirements and without evidence")
            for a in project.of_kind("story")
            if a.get("status") == "verified" and not a.list("requirements") and not a.list("evidence")]


def story_requirements(project: Project) -> List[Finding]:
    """Error 6: verified story refers to a requirement that is not implemented."""
    reqs = project.by_id("requirement")
    out = []
    for a in project.of_kind("story"):
        if a.get("status") != "verified":
            continue
        for ref in a.list("requirements"):
            req = reqs.get(ref)
            if req is not None and req.get("status") != "implemented":
                out.append(_f(project, 6, a, f"story is verified, but {ref} is {req.get('status')}"))
    return out


def superseded(project: Project) -> List[Finding]:
    """Error 7: superseded or retired without superseded_by."""
    return [_f(project, 7, a, f"status is {a.get('status')}, but 'superseded_by' is missing")
            for a in project.artifacts
            if a.kind in ID_KINDS and a.get("status") in ("superseded", "retired")
            and not a.list("superseded_by")]


def implemented_proof(project: Project) -> List[Finding]:
    """Error 8: requirement implemented without a passing test result and without a proof by hand.

    A proof by hand is `evidence` together with `verification`. Implementation paths alone prove nothing.
    """
    passed = project.passed()
    return [_f(project, 8, a, "requirement is implemented without a passing test result and without "
                              "a proof by hand (evidence and verification)")
            for a in project.of_kind("requirement")
            if a.get("status") == "implemented" and not passed.get(a.id)
            and not (a.list("evidence") and a.get("verification"))]


def status_behind_result(project: Project) -> List[Finding]:
    """Error 9: requirement planned or proposed, but a passing test result exists."""
    passed = project.passed()
    return [_f(project, 9, a, f"requirement is {a.get('status')}, but a passing test result exists")
            for a in project.of_kind("requirement")
            if a.get("status") in ("planned", "proposed") and passed.get(a.id)]


def unknown_results(project: Project) -> List[Finding]:
    """Error 10: test result for a requirement that does not exist."""
    reqs = project.by_id("requirement")
    seen = set()
    out = []
    for r in project.results:
        if r.req not in reqs and (r.path, r.req) not in seen:
            seen.add((r.path, r.req))
            out.append(Finding(10, r.path, f"test result for '{r.req}', which does not exist"))
    return out


_LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
_SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def links(project: Project) -> List[Finding]:
    """Error 13: broken relative link (outside code blocks and code spans)."""
    files = sorted(project.docs.rglob("*.md"))
    agents = project.root / "AGENTS.md"
    if agents.is_file():
        files.append(agents)
    out = []
    for path in files:
        if any(part in ("node_modules", ".git") for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        text = strip_code(text)
        for match in _LINK.finditer(text):
            target = match.group(1)
            if target.startswith("#") or _SCHEME.match(target):
                continue
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            base = project.root if target.startswith("/") else path.parent
            if not (base / target.lstrip("/")).exists():
                out.append(Finding(13, project.rel(path), f"link '{match.group(1)}' points to nothing"))
    return out


def stale_regions(project: Project) -> List[Finding]:
    """Error 11: generated region or view differs from what render would write."""
    return [Finding(11, project.rel(path), "generated content is out of date, run 'docspine render'")
            for path in render.stale(project)]


_DIAGRAM_REASON = {
    "missing": "has no SVG next to it",
    "unstamped": "has an SVG that was not produced with 'docspine diagram'",
    "outdated": "has an SVG produced from an older version of the source",
}


def diagram_images(project: Project) -> List[Finding]:
    """Error 12: diagram image not produced from the current version of its source."""
    return [Finding(12, project.rel(source),
                    f"diagram source {_DIAGRAM_REASON[state]}; run 'docspine diagram {project.rel(source)}'")
            for source, state in diagram.stale(project)]


_README_VERSION = re.compile(r"^<!--\s*docspine\s+(\S+)")


def _version(path: Path) -> Optional[str]:
    first = path.read_text(encoding="utf-8").lstrip().splitlines()[:1]
    match = _README_VERSION.match(first[0]) if first else None
    return match.group(1) if match else None


def readme_version(project: Project) -> List[Finding]:
    """Error 14: README.md was translated from a different docspine version than the installed STANDARD.md."""
    standard, readme = project.config / "STANDARD.md", project.docs / "README.md"
    for path in (standard, readme):
        if not path.is_file():
            return [Finding(14, project.rel(path), f"{path.name} from docspine is missing")]
    installed, translated = _version(standard), _version(readme)
    if installed is None:
        return [Finding(14, project.rel(standard), "first line does not name the docspine version")]
    if translated is None:
        return [Finding(14, project.rel(readme),
                        "first line does not name the docspine version (<!-- docspine X · … -->)")]
    if translated != installed:
        return [Finding(14, project.rel(readme), f"README was translated from docspine {translated}, "
                                                 f"installed is {installed}; run docspine-update")]
    return []


def evidence_paths(project: Project) -> List[Finding]:
    """Error 15: an evidence path does not exist."""
    out = []
    for a in project.artifacts:
        for path in a.list("evidence"):
            if not (project.root / path.lstrip("/")).exists():
                out.append(_f(project, 15, a, f"evidence path '{path}' does not exist"))
    return out
