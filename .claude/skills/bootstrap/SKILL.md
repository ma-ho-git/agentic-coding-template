---
description: First run after cloning this template. Verifies that the template's assumptions about Claude Code, Cowork, GitHub and the chosen stack still hold, adapts the repo where they do not, then gives the user a short orientation. Use on the first request in a freshly cloned repository, or when the environment manifest is older than 30 days.
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Edit, Bash
---

# Bootstrap

Run this before any other work in a fresh clone. Do it visibly, not silently.

## Step 1 — Verify the template's assumptions

`knowledge/90-meta/environment-manifest.md` lists every external assumption this template
depends on, with the date it was last verified and the source URL.

For each entry whose `verified` date is older than 30 days, or which has no date:

1. Fetch the source and compare against the `assumption` text.
2. Mark the entry `ok`, `changed`, or `unknown`, and set `verified` to today.
3. If `changed`: fix the affected file in this repo **now**, and note what you changed
   in the entry's `action` field. If the fix is larger than a few lines, create a task
   instead and put it in the `Ready` lane.

Check at minimum:

- Claude Code configuration surfaces — `CLAUDE.md`, `.claude/rules/`, `.claude/skills/`,
  `.claude/agents/`, hook event names and the settings schema.
- Whether Cowork can now read repository configuration directly. If yes, `cowork/` becomes
  redundant — say so.
- The hook payload fields used in `.claude/hooks/` (`tool_input.file_path`, `tool_input.command`,
  `permissionDecision`, `additionalContext`).
- The obsidian-kanban board file format used by `knowledge/10-pm/board.md`.
- The active stack profile in `stacks/`: current stable versions, test runner, linter,
  and the dominant docstring standard.

Do not rewrite entries you did not verify. An honest `unknown` beats a guessed `ok`.

## Step 2 — Set up the project

1. Ask the user for the project name and one-sentence purpose if `knowledge/00-index.md`
   still contains the placeholder.
2. Ask which stack profile applies. Copy the chosen file from `stacks/` to `stacks/active.md`
   and fill in the concrete commands.
3. Replace the template placeholders in `knowledge/00-index.md` and `README.md`.
4. Delete `examples/` — it demonstrates the workflow and is not part of a real project.
5. **Install the commit choke point:** `python3 tools/install_hooks.py`. From then on
   every commit runs every rule check (`tools/check_all.py --staged`) - including files
   written through Bash or another editor, which the Write|Edit hooks never see. An
   existing pre-commit hook of the user's own is left alone and reported.
6. Determine the **project scope**. See Step 2a.

## Step 2a — Determine the project scope

The scope decides how much gets written down, and nothing else. Ask it here, before
eliciting requirements — it sets how deep Step 3 goes.

Explain before asking, then propose. Do not make the user guess what the words mean:

> Wie groß ist das hier gedacht? Das ändert nur, wie viel dokumentiert wird — geprüft wird
> in allen drei Fällen dasselbe.
>
> - **skript** — einmalige Sache, nur für dich, niemand pflegt das weiter
> - **werkzeug** — du gibst es weiter, aber es bleibt überschaubar
> - **produkt** — wird über längere Zeit gepflegt, mehrere Leute arbeiten daran
>
> Nach dem, was du bisher beschrieben hast, würde ich **werkzeug** nehmen. Passt das?

Then do both of these, in the same step:

1. Write the value into `.claude/hooks/config.json` as `project_scope`
   (`skript` | `werkzeug` | `produkt`). It is what hooks and skills read.
2. Write the **reason** into the Projektzuschnitt section of
   `knowledge/05-requirements/baseline.md`, in the user's own words. A scope without a
   recorded reason is an excuse rather than a decision, and the next agent cannot tell
   which it was.

Unsure, or the user does not care → `produkt`. Falling back costs writing, never safety.

Say plainly what the scope does **not** change: requirements are elicited in every scope,
all six categories are asked in every scope, TDD holds in every scope, and every rigid
guardrail stays armed (`.claude/rules/guardrails.md`). Only documentation duty and the
depth of the answers scale (`.claude/rules/workflow.md`).

## Step 3 — Elicit the framework, before any task

This comes **before** the board, not after. A task without a requirement is work nobody
asked for, and a board seeded ahead of the requirements invites exactly that.

0. **Offer the scenario first** — `/szenario`. Optional, asked once: the user describes the
   project in their own words, and the elicitation derives from that instead of starting
   cold. A beginner can narrate a plan long before they can answer six requirement
   categories. A no is a complete answer; the scenario can be added later.
1. Run `/req-elicit` in framework mode. It clarifies what is being built and walks all six
   categories: functional, technical, organisational, security, legal, quality.
2. Run `/req-validate` and report the findings.
3. Ask the user to set `baseline_status: vereinbart` in
   `knowledge/05-requirements/baseline.md`. **Never set it yourself** — an agent proposes
   the framework, the human agrees it.
4. Only then seed the board with `/task-new`, each task naming the requirement it serves.

If the user wants to postpone this, say plainly what it costs: without an agreed framework
the target artefact stays vague, and architecture-shaping constraints surface after work is
already finished. Then let them decide.

## Step 4 — Orient the user

Then, and only then, tell the user — **short, three headings, no preamble**:

**Was das Projekt macht** — one or two sentences.

**Erste Schritte** — the three next concrete actions, in order.

**Deine Aufgaben** — what only the human can do. Typically:
- decide scope and priorities, approve the board
- provide credentials and access (never paste secrets into the chat)
- review and merge; the agents do not merge on their own
- answer the questions agents raise instead of letting them guess

Write this part in German. Keep it under 20 lines total.

## Step 4a — Check for leftovers

Run `python3 tools/check_placeholders.py`. It lists every document that still carries the
template's own placeholder text. The four core documents — `README.md`,
`knowledge/00-index.md`, `vision.md`, `baseline.md` — must come back clean; the rest may keep
their notes if the user wants them.

Deliberately **not** a CI check: in the template repository the placeholders belong there, so
CI would be red forever. It belongs here, at the one moment a clone stops being a template.

## Step 5 — Record it

Append a progress entry to `knowledge/10-pm/progress/` naming what you verified,
what changed, and what you set up.
