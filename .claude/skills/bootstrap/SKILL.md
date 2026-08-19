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
4. Seed the board: create the first tasks the project needs with `/task-new`.

## Step 3 — Orient the user

Then, and only then, tell the user — **short, three headings, no preamble**:

**Was das Projekt macht** — one or two sentences.

**Erste Schritte** — the three next concrete actions, in order.

**Deine Aufgaben** — what only the human can do. Typically:
- decide scope and priorities, approve the board
- provide credentials and access (never paste secrets into the chat)
- review and merge; the agents do not merge on their own
- answer the questions agents raise instead of letting them guess

Write this part in German. Keep it under 20 lines total.

## Step 4 — Record it

Append a progress entry to `knowledge/10-pm/progress/` naming what you verified,
what changed, and what you set up.
