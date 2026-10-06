"""Diagram images (STANDARD.md section 9): render DOT and PlantUML sources to SVG and
record a checksum of the source in the SVG, so that the checker can tell whether an
image was produced from the current version of its source (error 12)."""

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple

from .project import Project

# source suffix -> (tool, program name for messages)
TOOLS = {
    ".dot": ("dot", "Graphviz"),
    ".gv": ("dot", "Graphviz"),
    ".puml": ("plantuml", "PlantUML"),
    ".plantuml": ("plantuml", "PlantUML"),
}
_STAMP = re.compile(r"<!--\s*docspine-source sha256:([0-9a-f]{64})\s*-->\n?")
_XML_DECL = re.compile(r"^\s*<\?xml[^>]*\?>\n?")


class DiagramError(Exception):
    pass


def checksum(source: Path) -> str:
    """SHA-256 of the source, independent of line endings (a Windows checkout gives CRLF)."""
    data = source.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def sources(project: Project) -> List[Path]:
    """Every diagram source under docs/, except the temporary legacy folder."""
    legacy = project.docs / "legacy"
    return sorted(p for p in project.docs.rglob("*")
                  if p.suffix in TOOLS and p.is_file() and legacy not in p.parents)


def image(source: Path) -> Path:
    return source.with_suffix(".svg")


def state(source: Path) -> str:
    """'current', 'missing' (no SVG), 'unstamped' (SVG without checksum) or 'outdated'."""
    svg = image(source)
    if not svg.is_file():
        return "missing"
    match = _STAMP.search(svg.read_text(encoding="utf-8", errors="replace"))
    if not match:
        return "unstamped"
    return "current" if match.group(1) == checksum(source) else "outdated"


def stale(project: Project) -> List[Tuple[Path, str]]:
    return [(src, s) for src in sources(project) for s in [state(src)] if s != "current"]


def _stamp(svg: str, digest: str) -> str:
    svg = _STAMP.sub("", svg)
    stamp = f"<!-- docspine-source sha256:{digest} -->\n"
    decl = _XML_DECL.match(svg)
    if decl:
        head = decl.group(0) if decl.group(0).endswith("\n") else decl.group(0) + "\n"
        return head + stamp + svg[decl.end():]
    return stamp + svg


def render(source: Path) -> Path:
    """Render one source to the SVG next to it and record the source's checksum in it."""
    if source.suffix not in TOOLS:
        raise DiagramError(f"{source}: not a diagram source ({', '.join(sorted(TOOLS))})")
    if not source.is_file():
        raise DiagramError(f"{source}: file not found")
    tool, program = TOOLS[source.suffix]
    if shutil.which(tool) is None:
        raise DiagramError(f"'{tool}' not found: {program} is needed to render {source.name}; "
                           f"install {program} and run again")
    data = source.read_bytes()
    if tool == "dot":
        cmd = [tool, "-Tsvg"]
    else:
        cmd = [tool, "-tsvg", "-pipe"]
    result = subprocess.run(cmd, input=data, capture_output=True)
    if result.returncode != 0 or not result.stdout.strip():
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise DiagramError(f"{program} could not render {source.name}" + (f": {detail}" if detail else ""))
    svg = result.stdout.decode("utf-8")
    target = image(source)
    target.write_text(_stamp(svg, checksum(source)), encoding="utf-8")
    return target
