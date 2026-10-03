"""Build dist/docspine.pyz: the package including its embedded libraries, as one file."""

from __future__ import annotations

import shutil
import sys
import tempfile
import zipapp
from pathlib import Path

HERE = Path(__file__).resolve().parent


def build(target: Path) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        staging = Path(tmp)
        shutil.copytree(HERE / "docspine", staging / "docspine",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        (staging / "__main__.py").write_text(
            "from docspine.__main__ import main\nraise SystemExit(main())\n", encoding="utf-8")
        zipapp.create_archive(staging, target, interpreter="/usr/bin/env python3", compressed=True)
    return target


if __name__ == "__main__":
    out = build(HERE / "dist" / "docspine.pyz")
    print(f"built {out.relative_to(HERE)}", file=sys.stderr)
