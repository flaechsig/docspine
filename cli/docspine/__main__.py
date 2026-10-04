"""Command line: `docspine [--root DIR] check|render`."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from . import __version__, check, project, render


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="docspine", description="Check and render docspine documentation.")
    parser.add_argument("--root", default=".", help="repository root containing .docspine/PROFILE.md (default: .)")
    parser.add_argument("--version", action="version", version=f"docspine {__version__}")
    parser.add_argument("command", choices=["check", "render"])
    parser.add_argument("--without-tests", action="store_true",
                        help="check: skip what needs test results (errors 8, 9, 10)")
    args = parser.parse_args(argv)
    with_tests = not args.without_tests

    try:
        proj = project.load(Path(args.root), with_tests=with_tests)
    except project.ProjectError as exc:
        print(f"docspine: {exc}", file=sys.stderr)
        return 2

    if args.command == "render":
        for path in render.run(proj):
            print(f"written: {path}")
        return 0

    findings = check.run(proj, with_tests=with_tests)
    for finding in findings:
        print(finding)
    if findings:
        print(f"{len(findings)} error(s)", file=sys.stderr)
        return 1
    print("OK" if with_tests else "OK (without test results: errors 8, 9 and 10 not checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
