"""Run the tests and write req-results.json (STANDARD.md section 8.1).

Each test that carries requirement IDs (see tests/support.py, @req) contributes one result
per ID. Usage: python3 run_tests.py
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE / "tests")]


class TracingResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.traced = []

    def _trace(self, test, outcome):
        method = getattr(test, getattr(test, "_testMethodName", ""), None)
        reqs = tuple(getattr(type(test), "_reqs", ())) + tuple(getattr(method, "_reqs", ()))
        for req in dict.fromkeys(reqs):
            self.traced.append({"req": req, "result": outcome, "test": test.id()})

    def addSuccess(self, test):
        super().addSuccess(test)
        self._trace(test, "passed")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._trace(test, "failed")

    def addError(self, test, err):
        super().addError(test, err)
        self._trace(test, "failed")

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._trace(test, "skipped")


def main() -> int:
    suite = unittest.defaultTestLoader.discover(str(HERE / "tests"), top_level_dir=str(HERE / "tests"))
    runner = unittest.TextTestRunner(resultclass=TracingResult, verbosity=1)
    result = runner.run(suite)
    out = HERE / "req-results.json"
    out.write_text(json.dumps({"results": result.traced}, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(HERE)} ({len(result.traced)} results)", file=sys.stderr)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
