from __future__ import annotations

import json
import os
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

from support import req
from test_cli import run_main

from docspine import version

CHANGELOG = """\
# Changelog

## Unreleased

- not yet released

## 0.19

- nineteen

## 0.18

- eighteen

## 0.17

- seventeen
"""


class VersionTest(unittest.TestCase):
    """A project with docspine 0.17, a changelog behind a file URL and a private cache."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        self.root = tmp / "project"
        (self.root / ".docspine").mkdir(parents=True)
        (self.root / ".docspine" / "STANDARD.md").write_text(
            "<!-- docspine 0.17 · source: standard/en/STANDARD.md · do not edit in projects -->\n", encoding="utf-8")
        self.changelog = tmp / "CHANGELOG.md"
        self.changelog.write_text(CHANGELOG, encoding="utf-8")
        self.cache = tmp / "cache"
        self._env = mock.patch.dict(os.environ, {
            "XDG_CACHE_HOME": str(self.cache),
            "DOCSPINE_CHANGELOG_URL": self.changelog.as_uri(),
        })
        self._env.start()

    def tearDown(self):
        self._env.stop()
        self._tmp.cleanup()

    def run_version(self, *args):
        return run_main("--root", str(self.root), "version", *args)

    def offline(self):
        os.environ["DOCSPINE_CHANGELOG_URL"] = (Path(self._tmp.name) / "missing.md").as_uri()

    def age_cache(self, seconds):
        path = self.cache / "docspine" / "latest.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["checked"] = time.time() - seconds
        path.write_text(json.dumps(data), encoding="utf-8")


@req("REQ-0042")
class ReportsNewerVersion(VersionTest):
    def test_newer_version_with_notes_in_between(self):
        code, out, _ = self.run_version()
        self.assertEqual(code, 0)
        self.assertIn("docspine 0.19 is available, installed is 0.17", out)
        self.assertIn("- nineteen", out)
        self.assertIn("- eighteen", out)
        self.assertNotIn("seventeen", out)
        self.assertNotIn("not yet released", out)
        self.assertIn("spine-update", out)

    def test_current_version(self):
        self.changelog.write_text("# Changelog\n\n## Unreleased\n\n## 0.17\n\n- seventeen\n", encoding="utf-8")
        code, out, _ = self.run_version()
        self.assertEqual((code, out.strip()), (0, "docspine 0.17 is current"))

    def test_versions_compare_as_numbers(self):
        self.changelog.write_text("## 0.9\n\n- nine\n", encoding="utf-8")
        _, out, _ = self.run_version()
        self.assertIn("0.17 is current", out)

    def test_no_installation(self):
        (self.root / ".docspine" / "STANDARD.md").unlink()
        code, _, err = self.run_version()
        self.assertEqual(code, 2)
        self.assertIn("not found", err)


@req("REQ-0043")
class FetchesAtMostOnceADay(VersionTest):
    def test_answer_from_cache_within_a_day(self):
        self.run_version()
        self.offline()
        self.age_cache(23 * 60 * 60)
        _, out, _ = self.run_version()
        self.assertIn("0.19 is available", out)
        self.assertNotIn("could not check", out)

    def test_fetches_again_after_a_day(self):
        self.run_version()
        self.changelog.write_text("## 0.20\n\n- twenty\n", encoding="utf-8")
        self.age_cache(25 * 60 * 60)
        _, out, _ = self.run_version()
        self.assertIn("0.20 is available", out)

    def test_now_fetches_at_once(self):
        self.run_version()
        self.changelog.write_text("## 0.20\n\n- twenty\n", encoding="utf-8")
        _, out, _ = self.run_version("--now")
        self.assertIn("0.20 is available", out)

    def test_cache_lives_outside_the_project(self):
        self.run_version()
        self.assertTrue((self.cache / "docspine" / "latest.json").is_file())
        self.assertEqual(sorted(p.name for p in (self.root / ".docspine").iterdir()), ["STANDARD.md"])


@req("REQ-0044")
class OfflineDoesNotFail(VersionTest):
    def test_without_network_and_without_cache(self):
        self.offline()
        code, out, _ = self.run_version()
        self.assertEqual(code, 0)
        self.assertIn("docspine 0.17 installed; could not check for a newer version", out)

    def test_without_network_falls_back_to_cache(self):
        self.run_version()
        self.offline()
        code, out, _ = self.run_version("--now")
        self.assertEqual(code, 0)
        self.assertIn("0.19 is available", out)
        self.assertIn("could not check now, last checked", out)

    def test_timeout_is_short(self):
        self.assertLessEqual(version.TIMEOUT, 5)
        with mock.patch("urllib.request.urlopen", side_effect=TimeoutError("timed out")) as urlopen:
            code, out, _ = self.run_version()
        self.assertEqual(code, 0)
        self.assertIn("could not check", out)
        self.assertEqual(urlopen.call_args.kwargs.get("timeout"), version.TIMEOUT)


if __name__ == "__main__":
    unittest.main()
