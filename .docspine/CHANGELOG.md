# Changelog

What changed in what docspine delivers to projects (`.docspine/`, `.agents/skills/spine-*`).
The newest version comes first. `spine-update` shows the entries between the installed and
the new version.

## 0.3

- **No more `docs/STATUS.md`.** Counts, open questions, contradictions and chapters
  without content now appear in `docs/01-goals/README.md`, below the epics and stories.
  `spine-update` removes the old `docs/STATUS.md`.

## 0.2

- **Configuration moved to `.docspine/`.** `STANDARD.md` and `PROFILE.md` now live in
  `.docspine/`; `docs/` contains only documentation. `spine-update` moves an existing
  `docs/PROFILE.md` and removes `docs/STANDARD.md`.
- **No version in the profile.** The field `docspine:` in `PROFILE.md` is no longer used;
  `spine-update` removes it. Error 14 now compares the README with the installed standard.
- **New skill `spine-update`** to finish an update. `spine-init` only sets up.
- **`spine-init` writes first stories** for each theme.
- **The README** is based on arc42 and mentions the configuration files instead of
  linking them. Its English source is `.docspine/README.en.md`.
- **New:** `.docspine/MANIFEST` (delivered files), `.docspine/CHANGELOG.md` (this file),
  `.docspine/LICENSE` (0BSD).

## 0.1

First delivered version: standard, checker (`check`, `render`), skill `spine-init`.
