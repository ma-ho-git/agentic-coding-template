---
name: task-handoff
description: Hand work over to Claude Code by writing a complete task file and placing it on the kanban board, instead of attempting code work in Cowork where the project's checks do not run. Use when a task needs code changes, tests, builds, linters, or git operations.
license: MIT
---

# Hand off to Claude Code

For projects built from the agentic-coding-template.

## Why

Cowork does not load the repository's `.claude/` configuration. Hooks, rules and subagents
do not apply here, so code written in Cowork bypasses every check the project relies on.
Code work goes to Claude Code. Your job is to make that handover so complete that the other
agent needs no conversation history to start.

## 1. Recognise the handover

Hand over when the task needs: writing or refactoring code, running tests, linters, type checks
or builds, git operations, or anything the hooks are meant to guard.

Keep it here when the task is research, synthesis, documents, spreadsheets, triage of outside
material, or knowledge base maintenance.

## 2. Write the task file

`knowledge/10-pm/tasks/T-XXXX <kurzer-titel>.md`, from
`knowledge/90-meta/templates/task.md`. ID = highest existing plus one, four digits.

German. It must stand on its own:

- **Ziel** — one sentence: what is true afterwards that is not true now.
- **Akzeptanzkriterien** — checkbox list, each one testable. If you cannot say how it would be
  verified, it is not a criterion yet.
- **Kontext** — everything you found out that the other agent would otherwise re-derive:
  file paths, error messages verbatim, links to knowledge notes and ADRs, dead ends you
  already ruled out. This is the most valuable part of the handover.
- **Agent** — `claude-code`, with the reason in half a line.
- **Abhängigkeiten** — blocking tasks as wikilinks, or "keine".

Frontmatter: `status: ready`, `priority`, `agent: claude-code`, empty `owner`, `created`, `tags`.

## 3. Place the card

Add one line to the `Ready` lane of `knowledge/10-pm/board.md`:

```
- [ ] [[T-0042 Token-Refresh]]
```

Only that line. Do not reformat the board or reorder other cards.

## 4. Tell the user

One or two sentences: what you handed over, and that it should be picked up in Claude Code.
Do not start the code work "just a little bit" first.
