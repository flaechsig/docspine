---
name: spine-init
description: >-
  Start a project's documentation according to docspine: agree on the project language,
  draft the vision with the user, and write profile, vision, themes, README and AGENTS.md.
  Also run it again after updating docspine, to take over the new version. Use when the
  user wants to set up docspine, start the documentation of a new project, or calls
  /spine-init.
---

# spine-init

You set up the documentation of a project according to docspine. The rules are in
`docs/STANDARD.md`; read sections 1–3 before you write anything. You work in dialogue:
you propose, the person decides, and you write only after approval.

## Rules for the whole run

- **Propose instead of interrogating.** Turn what the person says into concrete drafts
  they can confirm or correct. Ask at most two rounds; never push.
- **Nothing is invented.** What the person does not know stays
  `UNKNOWN — <open question in the project language>`, at the start of a line or list item.
- **Only the core statement of the vision is required.** Everything else may stay open.
- **Never overwrite existing files without asking.** Show what you would change.
- **Write only after explicit approval.**

## Step 0 — Check the installation (silently)

1. Run from the repository root. `docs/STANDARD.md` and `.docspine/docspine.pyz` must
   exist; they come from the installation one-liner. If they are missing, tell the person
   and show the one-liner from the docspine quickstart.
2. Read the docspine version from the first line of `docs/STANDARD.md`
   (`<!-- docspine X · … -->`).
3. Check that `python3 --version` works. If it does not, tell the person that the checker
   needs Python 3.9 or later, and continue with everything except the check in step 6.

## Step 1 — Language

Ask in English, with a suggestion derived from the person's first message:

> Which language should the project documentation use? Suggested: German (de). OK?

Use the answer as `language` (ISO 639-1 code). From now on, talk to the person in that
language.

## Step 2 — Situation

- **`docs/PROFILE.md` exists and names an older docspine version** → this is an update.
  Go to "Update" at the end and do nothing else.
- **`docs/PROFILE.md` exists with the current version** → the project is already set up.
  Say so and suggest the next skill (`spine-require`).
- **The repository already contains code or documentation** (beyond the files from the
  installation) → say that `spine-adopt` is meant for existing projects. Continue only if
  the person explicitly wants to start the documentation fresh.
- **Otherwise** → new project, continue.

## Step 3 — Vision in dialogue

If the person has not described the project yet, ask for two or three sentences.

From that description, propose drafts for all of the following in one message, in the
project language, numbered so the person can answer briefly:

1. **Core statement** — the vision in one sentence, for example "For <target group> who
   <need>, <product> is a <category> that <benefit>. Unlike <alternative>, …"
2. **Problem** — what is bad today, and for whom
3. **Target group and stakeholders**
4. **Success** — how we will know it works, measurable where possible
5. **Non-goals** — what deliberately does not belong
6. **Quality goals** — at most three
7. **Themes** — three to seven epics, each with an ID `E-<NAME>` (upper case, descriptive)
   and a one-line description
8. **Constraints** — technology, platform, norms, budget, time
9. **Decisions already made** — for example language or platform

Mark every draft that you derived rather than heard as a suggestion. For anything you
cannot derive, write `UNKNOWN` with the open question.

The person confirms, corrects or says "don't know yet". Incorporate the answers. Then
show the complete result once more and ask for approval to write.

## Step 4 — Write (after approval)

Write in the project language; folder and file names and front-matter keys stay English
(`docs/STANDARD.md` section 2.4).

| File | Content |
|---|---|
| `docs/PROFILE.md` | front matter `docspine`, `language`, `statement_language: en`, `sources: []`; below, the heading for deviations with an empty list |
| `docs/01-goals/vision.md` | core statement, problem, target group and stakeholders, success, non-goals, quality goals, and a section "Themes" that links to `README.md` (STANDARD 3.1) |
| `docs/01-goals/epics/E-<NAME>.md` | one per theme: front matter `id`, `title`; heading; what the theme covers and why |
| `docs/02-constraints.md` | only if constraints are known |
| `docs/09-decisions/ADR-NNNN.md` | one per decision already made, `status: proposed`, sections context, decision, consequences (STANDARD 3.5) |
| `docs/01-goals/requirements/REQ-NNNN.md` | only for measurable quality goals: `category: quality`, `status: proposed`, EARS statement in English (STANDARD 3.4) |
| `docs/README.md` | the translated README, see below |
| `AGENTS.md` | see below |
| `.claude/CLAUDE.md` | only if neither `CLAUDE.md` nor `.claude/CLAUDE.md` exists: the single line `@../AGENTS.md` |

Do not create empty chapters.

### The README

Translate `.agents/skills/spine-init/README.en.md` into the project language and write it
to `docs/README.md`.

- The first line is `<!-- docspine X · from standard/en/README.md -->` with the version
  from step 0. For `language: en`, copy the file unchanged.
- Use the terms from the terminology table in `docs/STANDARD.md` section 12.
- Keep every link and anchor target unchanged; translate only the visible text.
- The workflow diagram is ASCII art. After translating its labels, the box-drawing
  characters (`│ ┐ ┤ ┘ ┬ ├ └ ┌ ▼ ▲ ◄`) must stay in the same columns as in the English
  original. Measure the columns of each line before and after (count characters, not
  bytes), and shorten or pad labels until they match.

### AGENTS.md

If `AGENTS.md` does not exist, create it. If it exists, add a section "Documentation
(docspine)" and leave everything else unchanged. Content, in the project language:

- one sentence on what the project is (from the core statement)
- where things are: `docs/README.md` (how the documentation works), `docs/STANDARD.md`
  (the rules), `docs/PROFILE.md` (project values), `docs/01-goals/README.md` (overview with
  status)
- how to check, before every commit:
  ```
  python3 .docspine/docspine.pyz render
  python3 .docspine/docspine.pyz check
  ```
- no architecture content (STANDARD 2.2)

## Step 5 — Check

Run `python3 .docspine/docspine.pyz render`, then `python3 .docspine/docspine.pyz check`.
The check must report `OK`. Fix errors in the files you wrote; if an error points to
something you cannot decide, ask.

## Step 6 — Close

Summarise in a few lines what was written, list the open questions (they also appear in
`docs/STATUS.md`), and suggest:

- reviewing the changes with `git status` and committing them
- `spine-require` for the most important theme as the next step

## Update

Run when `docs/PROFILE.md` names an older docspine version than `docs/STANDARD.md`.

1. Tell the person which version was installed and which is now present.
2. Translate `.agents/skills/spine-init/README.en.md` again into `docs/README.md`, as in
   step 4, with the new version in the first line.
3. Set `docspine:` in `docs/PROFILE.md` to the new version. Change nothing else.
4. Run step 5, then summarise and suggest committing.
