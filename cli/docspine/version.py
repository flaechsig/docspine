"""Command `version`: is a newer docspine available? (STANDARD.md section 11)

The newest version and its notes come from the changelog on the branch the installation
command reads. The answer is kept in the user's cache folder and fetched again at most
once a day, so the skills may call this on every start.
"""

from __future__ import annotations

import json
import os
import re
import time
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple

CHANGELOG_URL = "https://raw.githubusercontent.com/flaechsig/docspine/dist/.docspine/CHANGELOG.md"
INSTALL = "curl -fsSL https://github.com/flaechsig/docspine/archive/refs/heads/dist.tar.gz | tar -xz --strip-components=1"
INTERVAL = 24 * 60 * 60
TIMEOUT = 5

_HEADER = re.compile(r"<!--\s*docspine\s+(\S+)")
_SECTION = re.compile(r"^## (\S+)\s*$", re.MULTILINE)


class VersionError(Exception):
    pass


def installed(root: Path) -> str:
    standard = root / ".docspine" / "STANDARD.md"
    try:
        first = standard.read_text(encoding="utf-8").split("\n", 1)[0]
    except OSError:
        raise VersionError(f"{standard} not found; is docspine installed here?")
    match = _HEADER.search(first)
    if not match:
        raise VersionError(f"no version in the first line of {standard}")
    return match.group(1)


def _key(version: str) -> Tuple[int, ...]:
    return tuple(int(part) for part in re.findall(r"\d+", version))


def sections(changelog: str) -> List[Tuple[str, str]]:
    """Released versions with their notes, newest first; 'Unreleased' is left out."""
    heads = list(_SECTION.finditer(changelog))
    result = []
    for i, head in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(changelog)
        if re.fullmatch(r"\d+(\.\d+)*", head.group(1)):
            result.append((head.group(1), changelog[head.end():end].strip()))
    return result


def _cache_file() -> Path:
    base = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
    return Path(base) / "docspine" / "latest.json"


def _read_cache() -> Optional[dict]:
    try:
        return json.loads(_cache_file().read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _write_cache(changelog: str) -> None:
    path = _cache_file()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"checked": time.time(), "changelog": changelog}), encoding="utf-8")
    except OSError:
        pass  # without a cache the next call simply fetches again


def _fetch() -> str:
    url = os.environ.get("DOCSPINE_CHANGELOG_URL", CHANGELOG_URL)
    with urllib.request.urlopen(url, timeout=TIMEOUT) as response:
        return response.read().decode("utf-8")


def report(root: Path, now: bool = False) -> List[str]:
    """Lines to print. Never raises for network problems: working offline must not fail."""
    mine = installed(root)
    cache = _read_cache()
    note = ""
    if not now and cache and time.time() - cache.get("checked", 0) < INTERVAL:
        changelog = cache["changelog"]
    else:
        try:
            changelog = _fetch()
            _write_cache(changelog)
        except Exception as exc:  # no network, DNS, timeout, HTTP error
            if not cache:
                return [f"docspine {mine} installed; could not check for a newer version ({exc})"]
            changelog = cache["changelog"]
            checked = time.strftime("%Y-%m-%d %H:%M", time.localtime(cache.get("checked", 0)))
            note = f" (could not check now, last checked {checked})"

    released = sections(changelog)
    if not released:
        return [f"docspine {mine} installed; the changelog names no version{note}"]
    newest = released[0][0]
    if _key(newest) <= _key(mine):
        return [f"docspine {mine} is current{note}"]
    lines = [f"docspine {newest} is available, installed is {mine}{note}", ""]
    for version, notes in released:
        if _key(version) <= _key(mine):
            break
        lines += [f"## {version}", "", notes, ""]
    lines += ["To update, run in the repository root:", "", f"    {INSTALL}", "",
              "then the skill docspine-update."]
    return lines
