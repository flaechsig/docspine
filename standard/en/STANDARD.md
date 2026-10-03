<!-- docspine 0.1 · source: standard/en/STANDARD.md · do not edit in projects -->

# docspine Standard

Version 0.1 (draft)

This document defines the rules for documentation that follows docspine. It applies
equally to people and AI agents. `README.md` explains how to work with the
documentation; this file defines what applies. The project's own values and any
deviations are in `PROFILE.md`.

The words **must**, **must not**, **should** and **may** are used in their usual
normative sense.

## 1 Principles

1. **One source per statement.** Every statement lives in exactly one source file.
   Other places refer to it by ID or show it in a generated region (section 4).
   Copied text is an error.
2. **IDs are immutable.** An ID is never renumbered, reused or deleted. Status
   changes; the number does not.
3. **The rationale comes first.** What the system does will be visible in the code.
   Why it was decided that way is recorded only here.
4. **Observation is not intention.** Behaviour derived from code is a description,
   not a requirement. Requirements state what is wanted; descriptions state what is.
5. **People decide what applies.** Tools and AI agents propose; files are written
   after a person has approved.
6. **Nothing is invented.** What nobody knows stays `UNKNOWN`, together with the open
   question: `UNKNOWN — open question: …`.
7. **The checker decides what is implemented**, not a person and not an AI agent
   (section 11).
8. **Documentation grows with the changes.** Nothing is documented in advance. A
   chapter exists only once it has content.

## 2 Structure

### 2.1 Layout

The documentation is one document, spread across many files. Its outline is based on
the twelve chapters of arc42, with four deviations: chapter 1 also holds the complete
specification, chapter 9 consists only of the individual decisions, chapter 10 is
generated, and a chapter exists only once it has content.

```
AGENTS.md                     entry point for AI agents (project-specific)
docs/
  README.md                   how to work with this documentation (translated from docspine)
  STANDARD.md                 this file (from docspine)
  PROFILE.md                  project values and deviations
  STATUS.md                   figures, gaps, contradictions, open questions (generated)

  01-goals/                   chapter 1: introduction and goals
    README.md                 epics and stories with status (generated)
    vision.md
    epics/E-<NAME>.md
    stories/US-NNNN.md
    requirements/REQ-NNNN.md
  02-constraints.md           chapter 2: constraints
  03-context.md               chapter 3: context and scope
  04-strategy.md              chapter 4: solution strategy
  05-building-blocks/<name>.md  chapter 5: building block view, one block per file
  06-runtime/<name>.md        chapter 6: runtime view, one scenario per file
  07-deployment.md            chapter 7: deployment view
  08-concepts/<name>.md       chapter 8: domain and technical concepts
  09-decisions/ADR-NNNN.md    chapter 9: architecture decisions
  10-quality.md               chapter 10: quality requirements (generated)
  11-risks.md                 chapter 11: risks and technical debt
  12-glossary.md              chapter 12: glossary
  diagrams/                   sources and images of large diagrams
  legacy/                     imported old documentation, temporary (section 10)
```

A chapter may be a single file or a folder; the layout above is binding for the
chapters it lists as folders. Projects may add their own folders under `docs/`
(for example `docs/guides/`). They are not checked, except that links into them must
resolve.

### 2.2 Controlling files

| File | Purpose | Edited by hand |
|---|---|---|
| `docs/README.md` | how to work with the documentation | no, translated from docspine |
| `docs/STANDARD.md` | the rules | no, from docspine |
| `docs/PROFILE.md` | project values and justified deviations | yes |
| `AGENTS.md` | entry point for AI agents: where things are, how to check | yes |
| `.agents/skills/spine-*` | guided workflows for AI agents | no, from docspine |
| `.agents/skills/<other>` | project-specific workflows | yes |
| `.claude/` and similar | tool-specific settings; refer to `AGENTS.md` only | yes |

Everything that comes from docspine is overwritten when the standard is updated.
Changes to it belong in docspine, not in the project.

All rules are in files in the repository. Tool-specific files may make them easier to
use but must not contain rules of their own. Test: deleting a tool-specific folder
must not lose any rule.

`AGENTS.md` must not contain architecture content. It points into the document.

### 2.3 Profile

`PROFILE.md` has this front matter:

```yaml
---
docspine: 0.1               # version of the standard
language: de                # language of all documents
statement_language: en      # language of requirement statements, default en
sources:                    # permitted values for a requirement's source
  - GDPR Art. 32
  - RFC 6749 (OAuth 2.0)
---
```

Below the front matter, the file lists deviations from this standard, each with a
reason. An empty list is the normal case.

### 2.4 Language

Configuration is in English; documentation is in the project language.

| What | Language |
|---|---|
| `STANDARD.md`, skills | English, copied unchanged |
| `README.md` | `language`, translated from docspine's English source |
| text, headings, `title`, `rationale` | `language` |
| generated regions and views | `language` |
| requirement `statement` | `statement_language` (default `en`, because WHEN and IF blur in many languages) |
| folder and file names | English |
| front-matter keys and values | English |

The translated `README.md` starts with the version of its source:
`<!-- docspine 0.1 · from standard/en/README.md -->`. When docspine has a newer
version, the README is translated again. Translations use the terms in section 12.

### 2.5 IDs

| Artifact | ID | File |
|---|---|---|
| Epic | `E-<NAME>`, upper case, descriptive, not numbered | `01-goals/epics/E-<NAME>.md` |
| Story | `US-NNNN` | `01-goals/stories/US-NNNN.md` |
| Requirement | `REQ-NNNN` | `01-goals/requirements/REQ-NNNN.md` |
| Decision | `ADR-NNNN` | `09-decisions/ADR-NNNN.md` |

`NNNN` is four digits with leading zeros. A new artifact takes the next free number.
The `id` in the front matter must match the file name.

## 3 Artifacts

All source files are Markdown. Artifacts with an ID have YAML front matter.

### 3.1 Vision

`01-goals/vision.md`, no front matter. Sections:

| Section | Required |
|---|---|
| Core statement: the vision in one sentence | yes |
| Problem | no |
| Target group and stakeholders | no |
| Success: how we know it works | no |
| Non-goals: what deliberately does not belong | no |
| Quality goals | no |
| Themes: link to `01-goals/README.md` | no |

Missing answers are written as `UNKNOWN — open question: …`. The vision is stable
text and contains no status information.

### 3.2 Epic

```yaml
---
id: E-NAME
title: <short title>
---
```

Body: what the theme covers and why. An epic has no `status` field; its status is
derived from its stories (section 3.3). The list of its stories is a generated region.

### 3.3 Story

```yaml
---
id: US-NNNN
title: <short title>
epic: E-NAME                  # must exist
requirements: [REQ-NNNN]      # each must exist; [] is allowed
status: open
evidence: []                  # optional: paths that prove the story
superseded_by: ADR-NNNN       # only with superseded or retired
---
```

Body: `As <role> I want <goal> so that <benefit>.`, then why, then acceptance in the
users' terms. A story contains no decisions (those are ADRs) and no normative criteria
without a requirement.

| `status` | Meaning | Proof required |
|---|---|---|
| `open` | candidate, not committed | none |
| `in-progress` | core built, parts open | none |
| `verified` | fully implemented and confirmed | `requirements` or `evidence`; every listed requirement is `implemented` |
| `superseded` | replaced by a decision, will not be built this way | `superseded_by` |
| `retired` | was implemented, removed | `superseded_by` |

A story without requirements is allowed. It is proven through `evidence`, for example
a UI test that the requirement mechanism does not cover.

The derived status of an epic: `verified` if all its stories are `verified`, `open`
if none has started, otherwise `in-progress`. Stories with `superseded` or `retired`
are ignored for this.

### 3.4 Requirement

```yaml
---
id: REQ-NNNN
statement: <exactly one EARS pattern, in statement_language>
obligation: MUST | SHOULD | WILL
status: proposed
category: quality             # optional: marks a quality requirement
source: <external norm, or empty for own requirement>   # must be listed in the profile
confidence: unverified        # only without test results, see below
evidence: []                  # paths to implementation and proof
verification: <how fulfilment is checked>               # optional
supersedes: REQ-NNNN          # optional
superseded_by: REQ-NNNN | ADR-NNNN   # only with superseded
rationale: >-
  <why, in language>
---
```

Body: a heading with ID and short title, then one to three sentences of context.

**EARS patterns.** The statement follows exactly one pattern:

| Pattern | Form |
|---|---|
| ubiquitous | `The <system> shall <response>.` |
| event-driven | `WHEN <trigger>, the <system> shall <response>.` |
| state-driven | `WHILE <state>, the <system> shall <response>.` |
| unwanted behaviour | `IF <condition>, THEN the <system> shall <response>.` |
| optional feature | `WHERE <feature>, the <system> shall <response>.` |

**Obligation.** `MUST` is binding, `SHOULD` recommended, `WILL` a stated intention.
EARS has no level of obligation, hence the separate field. Views in other languages
show translated values (in German: MUSS, SOLLTE, WIRD).

**Source.** External norms change independently. When one changes, it must be possible
to find all affected requirements in a minute.

| `status` | Meaning | Rule |
|---|---|---|
| `proposed` | candidate, not committed | none |
| `planned` | committed, not (fully) built | no passing test result |
| `implemented` | built | passing test result **or** `evidence` |
| `rejected` | discarded, never built | none |
| `superseded` | replaced by a requirement or a decision | `superseded_by` |

A requirement is atomic; there is no `in-progress`. Partly built means `planned`. If
that happens often, the requirement is cut too coarsely.

A new requirement is never `implemented`.

**Confidence.** Has the statement been checked against the running system?
`verified | unverified | contradicted`.
- If test results exist for the requirement (section 8.1), `confidence` is not
  maintained; the checker derives it.
- Otherwise it is maintained by hand. `verified` then requires `evidence` and
  `verification`.

**Quality requirements** carry `category: quality`. Chapter 10 is generated from them.

### 3.5 Decision (ADR)

```yaml
---
id: ADR-NNNN
title: <short title>
status: proposed | accepted | rejected | superseded
date: YYYY-MM-DD              # date of the decision
supersedes: ADR-NNNN          # optional
superseded_by: ADR-NNNN       # only with superseded
requires: [REQ-NNNN]          # optional: testable consequences
---
```

Sections:

| Section | Required |
|---|---|
| Context: the problem, the forces, the current state | yes |
| Decision: what applies; rejected alternatives with a short reason, if there were any | yes |
| Rationale: why this option | no, may be part of context or decision |
| Consequences: including the inconvenient ones | yes |

An ADR with `proposed` is under discussion and may be edited directly. From `accepted`
on it is immutable and can only be superseded.

### 3.6 Building block

`05-building-blocks/<name>.md`:

```yaml
---
title: <name of the block>
path: [<code path>, …]        # where the block lives in the code
---
```

Body: responsibility, interfaces, important internals. The requirements the block
realises are a generated region (section 4).

### 3.7 Runtime scenario

`06-runtime/<name>.md`:

```yaml
---
title: <name of the scenario>
stories: [US-NNNN]            # optional: stories the scenario realises
---
```

### 3.8 Other chapters

No required front matter. A chapter that is only partly filled carries
`arc42_status: PARTIAL` in its front matter. A missing file means the chapter is
`UNKNOWN`.

## 4 Relations and generated regions

Relations are stated **only in the front matter, in one direction**:

| From | Field | To |
|---|---|---|
| Story | `epic` | Epic |
| Story | `requirements` | Requirements |
| Runtime scenario | `stories` | Stories |
| ADR | `requires` | Requirements |
| Building block | `path` | Code; requirements are matched through their `evidence` paths |
| Requirement, story, ADR | `superseded_by` | successor |

Every other direction, and every piece of content shown in more than one place, is
generated into a **generated region** inside a hand-written file:

```markdown
<!-- generated:<type> -->
…
<!-- /generated -->
```

| Type | In | Shows |
|---|---|---|
| `status` | `01-goals/README.md` | epics and stories with status |
| `stories` | epic | its stories with status |
| `requirements` | story | statements and status of its requirements |
| `context` | requirement | epic and story it belongs to, ADRs that require it |
| `realized` | building block | requirements whose evidence lies under its path |
| `scenarios` | story | runtime scenarios that realise it |

Generated regions must not be edited by hand. A region that differs from what the
checker would generate is an error. On merge conflicts inside a region, discard the
region and regenerate.

Hand-written back references (for example "part of US-0042") must not be written.

## 5 Changing instead of rewriting

**Requirement.** A change in content creates a new requirement:
1. Create `REQ-MMMM` with `supersedes: REQ-NNNN`.
2. In `REQ-NNNN`, set only `status: superseded` and `superseded_by: REQ-MMMM`.
   Statement and rationale stay as history.

**Story.** A story that will not be built as described goes to `superseded`; one that
was built and is removed goes to `retired`. Both name the decision in `superseded_by`.

**ADR.** An accepted decision is not edited. A new ADR names the old one in
`supersedes`; the old one gets `status: superseded` and `superseded_by`.

## 6 Architecture impact

For every new requirement or change, the question is: must the architecture take
something into account, change, or decide something? Exactly one verdict applies:

| Verdict | Meaning | Consequence |
|---|---|---|
| already covered | the existing architecture covers it | nothing changes; name any constraint the implementation must respect |
| affects chapter | the architecture changes | edit the chapter, with evidence and confidence |
| decision due | an architecture decision is contained | write an ADR |
| no impact | local to an element, below architecture level | nothing to document |

**What is architecture level:** building blocks and their dependencies, runtime
interactions, deployment and operation, cross-cutting concepts (security, caching,
persistence, …), quality requirements, risks, and anything that is a decision.

**What usually is not:** a single endpoint, a UI component, a field on an existing
entity, a rule, a template — as long as no block, dependency, concept or decision is
affected.

Check the effect, not the size. A small field can affect a cross-cutting concept; a
large feature can be entirely local.

## 7 Statements about the current state

Descriptive statements in chapters 2–8 and 11 carry their confidence inline:

```markdown
_(confidence: verified — src/orders/OrderService.java, REQ-0012)_
```

| Value | Meaning |
|---|---|
| `verified` | checked against code, configuration or a proven requirement |
| `unverified` | taken over, not checked |
| `aspirational` | target state, not built |
| `contradicted` | documentation and code disagree |

A contradiction stays visible and is never resolved silently:

```markdown
> [!CAUTION]
> The documentation says X, the code does Y. (contradiction)
```

The checker lists every block marked `(contradiction)` in `STATUS.md`. A person
decides how it is resolved.

## 8 Proof

### 8.1 Test results

Projects with automated tests deliver results in this format, in any number of files
named `req-results.json`:

```json
{
  "results": [
    { "req": "REQ-0012", "result": "passed", "test": "OrderServiceTest.rejectsEmptyCart" }
  ]
}
```

`result` is `passed`, `failed` or `skipped`. A requirement counts as passed if at
least one result is `passed` and none is `failed`. How the file is produced is up to
the project.

### 8.2 Status change

When a requirement passes: set `status: implemented` and add implementation and test
paths to `evidence`. Set the story to `verified` once all its requirements are
`implemented`. Statement, rationale and title stay unchanged.

Without test results, `evidence` and `verification` prove the requirement, and
`confidence` is set by hand.

### 8.3 Is the proof honest?

A passing test is the entry ticket, not the proof. For each implemented requirement:
split the statement into its clauses (trigger or condition, and response) and check
which clauses the test's assertions actually exercise.

| Verdict | Meaning |
|---|---|
| full | every clause is exercised against real behaviour |
| partial | the core runs, a clause or the actual acceptance is not exercised |
| hollow | the test carries the ID but does not exercise the behaviour |

A finding is either a **test gap** (sharpen the test) or a **requirement defect**
(wrong actor, untestable, overloaded clause). A requirement defect is fixed by
superseding the requirement, not by a test that cements a wrong statement.

## 9 Diagrams

Diagrams are always kept as text source in the repository, never only as images.

- **ASCII** in a code block on entry pages (`README.md`, overviews), which are opened
  first and in any environment.
- **Mermaid** in chapters, for sequences, class and domain models, state machines.
- **DOT or PlantUML with a committed SVG** under `docs/diagrams/` for large overviews
  where Mermaid's layout is not enough. The SVG must not be older than its source.
- **Images without a source** only where none can exist, such as screenshots.

## 10 Legacy

Applies only while `docs/legacy/` exists.

- Statements taken from legacy documentation enter with `confidence: unverified` and
  `derived_from: <path and line range>`.
- Three sources, three degrees of validity: the **code** says what happens, the
  **legacy documentation** what was once intended, a **person** what applies.
- A legacy document or section may be removed only when all four conditions hold:
  1. Its content is taken over: every relevant statement is in the new structure.
  2. Its references are moved: no `derived_from` points to it any more.
  3. It is not the only source: the content demonstrably exists elsewhere.
  4. A person has approved the removal.
- On removal, `derived_from` is replaced by `<name> legacy (git history)`.

## 11 Checker

The checker is a command-line tool that runs without a build system:

- `check` — validates everything below and fails on any error.
- `render` — writes generated regions and views.

**Errors:**

| # | Error |
|---|---|
| 1 | required front-matter field missing, or value not permitted |
| 2 | ID does not match the file name, or is used twice |
| 3 | reference to an ID that does not exist |
| 4 | `source` not listed in the profile |
| 5 | story `verified` without `requirements` and without `evidence` |
| 6 | story `verified` refers to a requirement that is not `implemented` |
| 7 | `superseded` or `retired` without `superseded_by` |
| 8 | requirement `implemented` without a passing test result and without `evidence` |
| 9 | requirement `planned` or `proposed`, but a passing test result exists |
| 10 | test result for a requirement that does not exist |
| 11 | generated region differs from what would be generated |
| 12 | diagram image older than its source |
| 13 | broken relative link |
| 14 | `README.md` was translated from a different docspine version than the profile states |

**Generated views:**

| File | Content |
|---|---|
| `01-goals/README.md` | epics and stories with status |
| `STATUS.md` | figures, open chapters, contradictions, open questions (`UNKNOWN`) |
| `10-quality.md` | all requirements with `category: quality` |

## 12 Terminology

Documentation in other languages (`README.md`, generated regions and views) uses these
terms. The German column is binding for projects with `language: de`.

| English | Deutsch |
|---|---|
| acceptance | Akzeptanz |
| architecture impact | Architekturwirkung |
| building block | Baustein |
| checker | Prüfwerkzeug |
| confidence | Konfidenz |
| controlling files | steuernde Dateien |
| core statement | Kernsatz |
| decision (ADR) | Entscheidung (ADR) |
| epic | Epic |
| evidence | Beleg |
| generated region | generierter Bereich |
| legacy documentation | Altbestand |
| non-goal | Nicht-Ziel |
| obligation | Verbindlichkeit |
| open question | offene Frage |
| profile | Profil |
| proof | Nachweis |
| proof required | Belegpflicht |
| rationale | Begründung |
| requirement | Requirement, Anforderung |
| requirement defect | Requirement-Defekt |
| runtime scenario | Laufzeitszenario |
| source (norm) | Quelle |
| story | Story |
| supersede | ablösen |
| test gap | Test-Lücke |
| test result | Testergebnis |
| verdict: full / partial / hollow | Verdikt: voll / teil / hohl |
