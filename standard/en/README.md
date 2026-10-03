<!-- docspine 0.1 · source: standard/en/README.md · do not edit in projects -->

# Documentation according to docspine

This documentation follows the [docspine](https://github.com/flaechsig/docspine)
standard: requirements, architecture and decisions form **one document**, spread across
many small files, connected by fixed IDs and controlled by a checker. This page explains
the structure and the way of working. What applies in detail is in
[STANDARD.md](STANDARD.md), this project's values are in [PROFILE.md](PROFILE.md).

- **What it is about:** [Vision](01-goals/vision.md)
- **Where things stand:** [Epics, stories and their status](01-goals/README.md)

## Structure

The outline is based on the twelve chapters of [arc42](https://arc42.org), with four
deviations:

- Chapter 1 also holds the complete specification, so that requirements and
  architecture do not drift apart in two documents.
- Chapter 9 consists only of the individual decisions (ADRs).
- Chapter 10 is generated from the quality requirements.
- A chapter exists only once it has content.

```
docs/
  README.md                   this page (translated from docspine)
  STANDARD.md                 the rules of the standard, in English (do not edit)
  PROFILE.md                  this project's values: language, sources, deviations
  STATUS.md                   figures, gaps, contradictions, open questions (generated)

  01-goals/                   ch. 1 — introduction and goals
    README.md                 overview: epics, stories, status (generated)
    vision.md                 why it exists, for whom, how success is measured
    epics/E-<NAME>.md         themes
    stories/US-NNNN.md        benefit from the users' point of view
    requirements/REQ-NNNN.md  individual testable requirements
  02-constraints.md           ch. 2 — constraints
  03-context.md               ch. 3 — context and scope: neighbouring systems and users
  04-strategy.md              ch. 4 — solution strategy
  05-building-blocks/         ch. 5 — building block view, one block per file
  06-runtime/                 ch. 6 — runtime view, one scenario per file
  07-deployment.md            ch. 7 — deployment view
  08-concepts/                ch. 8 — domain and technical concepts
  09-decisions/ADR-NNNN.md    ch. 9 — architecture decisions
  10-quality.md               ch. 10 — quality requirements (generated)
  11-risks.md                 ch. 11 — risks and technical debt
  12-glossary.md              ch. 12 — glossary
  diagrams/                   sources and images of large diagrams
```

Folders, file names and metadata are in English; the content is in the project
language.

## Controlling files

Some files do not describe the project but how its documentation is worked on. They
guide people and AI agents alike; only `AGENTS.md` and the skills are aimed at AI
agents alone.

| File | Purpose | Edit by hand? |
|---|---|---|
| `docs/README.md` | this page: structure and way of working | no, translated from docspine |
| `docs/STANDARD.md` | the rules that apply to all content | no, comes from docspine |
| `docs/PROFILE.md` | this project's values (language, sources) and justified deviations from the standard | yes |
| `AGENTS.md` (repository root) | entry point for AI agents: where things are, how to check | yes |
| `.agents/skills/spine-*` | guided workflows for AI agents | no, comes from docspine |
| `.agents/skills/<other>` | project-specific workflows | yes |
| `.claude/` and similar | tool-specific settings, refer to `AGENTS.md` only | yes |

Whatever comes from docspine is overwritten when the standard is updated. Changes to it
belong in docspine, not in the project.

## How the parts fit together

```
Vision → Epic → Story → Requirement ← Test
                  ↑          ↑
   Runtime scenario     Building block (via the code path)
                             ↑
                            ADR (decision → testable consequence)
```

- Every statement has **exactly one source file**. Other places refer to it by ID or
  show its content in a generated region (`<!-- generated:… -->`). Never edit such
  regions by hand.
- **IDs are immutable.** If a requirement changes in content, a new one is created and
  the old one is superseded.
- **The checker decides whether something is implemented**, not a person and not an
  AI: a requirement counts as implemented when a test or a piece of evidence proves it.

## Way of working

Work runs as a cycle. Each step has a skill (`spine-*`) that guides through it. The
skills follow the open Agent Skills standard and work with various AI tools. Without
skills it works just the same; the rules are in `STANDARD.md`.

```
  Start: Vision
       │
       ▼
  ┌─► Require ────────► Check impact ────┬─► Decide (ADR) ─────────────┐
  │   Epic · Story · REQ                 ├─► Update architecture ──────┤
  │        ▲                             └─► no impact ────────────────┤
  │        │                                                           ▼
  │        └───────────── gap found ────────────────────────────── Build ◄─────┐
  │                                                       Code · Test · Status │
  │                                                                 │          │
  │                                                                 ▼          │
  │                                                               Prove        │ no
  │                                                                 │          │
  │                            yes                                  ▼          │
  └─────────────────────────────────────────────────────────── Checker green? ─┘
```

| Step | What happens | Skill |
|---|---|---|
| **Start** | A first description turns into vision, themes and constraints. Whatever is open stays as a question. | `spine-init` |
| **Require** | A need becomes a story and a requirement: who, what, why, how to check. | `spine-require` |
| **Check impact** | Must the architecture take something into account, change or decide something? | `spine-impact` |
| **Decide** | A due decision is recorded with alternatives and rationale. | `spine-decide` |
| **Build** | Code and test are written; the test carries the requirement ID. Once it passes, the status changes. | `spine-build` |
| **Prove** | Does the test really check what the requirement demands, or does it only carry the ID? | `spine-prove` |

Three rules apply in every step:

- **People decide what applies.** Skills and AIs propose; files are written after
  approval.
- **Nothing is invented.** What nobody knows stays `UNKNOWN`, with the open question.
- **Gaps lead back.** If building shows that a requirement is missing or the
  architecture does not hold, go back to the matching step instead of bridging the gap
  in code.

Instructions for wiring the checker into a build or adopting an existing project, and
for installation, are on the [docspine page](https://github.com/flaechsig/docspine).

## Acknowledgements

docspine invents little; it combines proven work:

- **[arc42](https://arc42.org)** by Gernot Starke and Peter Hruschka: the outline of
  this document and the idea of documenting architecture pragmatically and step by step.
- **[IREB](https://www.ireb.org)** (International Requirements Engineering Board) with
  the CPRE syllabus: the terms and principles of requirements engineering on which
  vision, story and requirement build.
- **[EARS](https://alistairmavin.com/ears/)** (Easy Approach to Requirements Syntax) by
  Alistair Mavin and colleagues: the sentence structure that makes requirements
  unambiguous and testable.
- **[Architecture Decision Records](https://adr.github.io)**, described by Michael
  Nygard: record decisions with their rationale, never rewrite them, only supersede.
- **[Mermaid](https://mermaid.js.org)** by Knut Sveidqvist and the community: diagrams
  as text.
- **[Agent Skills](https://agentskills.io)**, published by Anthropic as an open
  standard, and **[AGENTS.md](https://agents.md)**: tool-independent ways to give AI
  agents workflows and an entry point.
- The **docs-as-code** movement: keep, check and version documentation in the
  repository like code.
