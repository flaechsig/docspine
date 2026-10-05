# Changelog

What changed in what docspine delivers to projects (`.docspine/`, `.agents/skills/spine-*`).
The newest version comes first. `spine-update` shows the entries between the installed and
the new version.

## 0.9

- **`spine-gate` also sets up a new build,** connected from the start, when the project
  has none yet; it picks the integration from the tool chain named in the constraints.
  The Maven integration has a tested minimal `pom.xml` for this.
- **`spine-gate` proposes the status change** for requirements whose tests already pass,
  in the same step, because a passing test on a `planned` requirement fails the build
  (error 9).
- **`spine-init`** recommends `spine-gate` before the first build file or test, also in
  `AGENTS.md`.
- **Specifying and building are separate.** `proposed` means described, `planned` means
  released for building; a person decides the release. Specification skills write no
  code; new requirements are always `proposed`; building works only on `planned`
  requirements. `spine-require` suggests the next story by default instead of building.
- **Git is a prerequisite** (standard 2.6), like Python. `spine-init` checks it, offers
  `git init` for a new folder, and offers the first commit at the end.
- **Positioning:** docspine is a way of developing with the documentation as its spine,
  from vision to code and proof. Designed for one person; small teams follow in 0.10.

## 0.8

- **New skill `spine-gate`:** recognises the tool chain, applies the matching integration
  step by step with explanations, and checks the result. The integrations travel with it
  in `.agents/skills/spine-gate/integrations/`.

## 0.7

- **Integration contract** in the standard (section 11): deliver test results, run
  `check` after the tests and fail the build on errors, keep `render` outside the build.
  `render` may run any time before `check`.
- **Integrations per tool chain** in the docspine repository under `integrations/`. First:
  `maven-junit5`, now including `check` in the Maven build (`exec-maven-plugin`).

## 0.6

- **Stricter proof.** An implemented requirement needs a passing test result or a proof
  by hand: `evidence` **and** `verification`. Implementation paths alone no longer count.
  Requirements proven by hand without `verification` now report error 8.
- **`check --without-tests`** checks the documentation without test results.
- **Order:** run the tests, then `render`, then `check`. `spine-init` writes this order
  into `AGENTS.md`, with the project's test command first.

## 0.5

- **Test results from JUnit XML reports.** The checker reads the reports named in the
  new profile field `test_reports`; each test case counts for every `REQ-NNNN` in its
  name or class name. For JUnit 5, put the ID in `@DisplayName`. Example for Maven:
  `examples/maven-junit5/` in the docspine repository. `req-results.json` still works.

## 0.4

- **New skill `spine-require`:** turns a need into a story with requirements (EARS), in
  dialogue, and checks the result.

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
