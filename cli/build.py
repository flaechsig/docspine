"""Build docspine for delivery.

    python3 cli/build.py          builds cli/dist/docspine.pyz
    python3 cli/build.py dist     also commits the delivery tree to the branch `dist`

The branch `dist` contains only the files docspine owns, at their paths in a project.
Projects install or update with:

    git init -q && git fetch -q --depth 1 <docspine repository> dist && git checkout FETCH_HEAD -- .
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipapp
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BRANCH = "dist"
FIXED_TIME = 315532800  # 1980-01-01, the earliest time a ZIP file can store


def build(target: Path) -> Path:
    """The CLI as one file, including its embedded libraries."""
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        staging = Path(tmp)
        shutil.copytree(HERE / "docspine", staging / "docspine",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        (staging / "__main__.py").write_text(
            "from docspine.__main__ import main\nraise SystemExit(main())\n", encoding="utf-8")
        # fixed timestamps, so that the same sources always give the same file
        for path in staging.rglob("*"):
            os.utime(path, (FIXED_TIME, FIXED_TIME))
        zipapp.create_archive(staging, target, interpreter="/usr/bin/env python3", compressed=True)
    return target


def version() -> str:
    first = (REPO / "standard/en/STANDARD.md").read_text(encoding="utf-8").splitlines()[0]
    match = re.match(r"<!--\s*docspine\s+(\S+)", first)
    if not match:
        raise SystemExit("standard/en/STANDARD.md does not name its version in the first line")
    return match.group(1)


def delivery_tree(root: Path) -> None:
    """Write the files docspine delivers into a project, at their paths there."""
    (root / ".docspine").mkdir(parents=True)
    shutil.copy(REPO / "standard/en/STANDARD.md", root / ".docspine/STANDARD.md")
    skills = root / ".agents/skills"
    for skill in sorted((REPO / "skills").iterdir()):
        if (skill / "SKILL.md").is_file():
            shutil.copytree(skill, skills / skill.name)
    shutil.copy(REPO / "standard/en/README.md", skills / "spine-init/README.en.md")
    build(root / ".docspine/docspine.pyz")
    shutil.copy(REPO / "LICENSE", root / ".docspine/LICENSE")
    (root / ".claude").mkdir()
    os.symlink("../.agents/skills", root / ".claude/skills")


def _git(*args: str, env=None, input=None) -> str:
    return subprocess.run(["git", *args], cwd=REPO, check=True, capture_output=True, text=True,
                          env=env, input=input).stdout.strip()


def commit_dist() -> str:
    """Commit the delivery tree to the branch `dist` without touching the working tree."""
    ver = version()
    with tempfile.TemporaryDirectory() as tmp:
        tree_dir = Path(tmp) / "tree"
        delivery_tree(tree_dir)
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(tmp) / "index"))
        _git("--work-tree", str(tree_dir), "add", "-A", ".", env=env)
        tree = _git("write-tree", env=env)
    parent = subprocess.run(["git", "rev-parse", "--verify", "-q", f"refs/heads/{BRANCH}"],
                            cwd=REPO, capture_output=True, text=True).stdout.strip()
    if parent and _git("rev-parse", f"{parent}^{{tree}}") == tree:
        return parent
    source = _git("rev-parse", "--short", "HEAD")
    args = ["commit-tree", tree] + (["-p", parent] if parent else [])
    commit = _git(*args, input=f"docspine {ver} (from {source})\n")
    _git("update-ref", f"refs/heads/{BRANCH}", commit)
    return commit


if __name__ == "__main__":
    out = build(HERE / "dist" / "docspine.pyz")
    print(f"built {out.relative_to(REPO)}", file=sys.stderr)
    if sys.argv[1:] == ["dist"]:
        commit = commit_dist()
        print(f"branch {BRANCH} at {commit[:10]} (docspine {version()})", file=sys.stderr)
