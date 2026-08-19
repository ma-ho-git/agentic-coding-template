# Agentic Coding Template — Agent Instructions

Structured vibe-coding for Claude Code and Claude Cowork. This file is the entry point.
Read it fully. It is short on purpose; detail lives in `.claude/rules/` and `.claude/skills/`.

## 0. First run after cloning

If `knowledge/90-meta/environment-manifest.md` has no verified entry from the last 30 days,
run `/bootstrap` before anything else. Do not skip it, do not do it silently.

## 1. Non-negotiables

1. **Test-driven.** Failing test first, then the code that makes it pass, then refactor.
   No production code without a test that demanded it.
2. **Contract comments.** Every source file starts with an `@contract` block. Keep it current.
   See `.claude/rules/contracts.md`.
3. **Knowledge base is part of the work, not paperwork.** Research, decisions, and any
   problem that took more than one attempt get written down. See `.claude/rules/knowledge-base.md`.
4. **The board is the truth.** No work outside a task in `knowledge/10-pm/board.md`.
5. **Never endanger the project.** No destructive git operations, no force-push, no rewriting
   published history, no spending on paid services, no touching anything outside this repo.

## 2. Where things live

| Path | Purpose |
| --- | --- |
| `.claude/rules/` | Coding and conduct rules. Loaded automatically, some scoped by file path. |
| `.claude/skills/` | Workflows. Invoke with `/name`. Loaded on demand. |
| `.claude/agents/` | Subagent definitions. |
| `.claude/hooks/` | Deterministic checks. These run whether or not you agree with them. |
| `knowledge/` | Obsidian vault: project management, knowledge, troubleshooting. German. |
| `stacks/` | Stack profiles (test runner, linter, docstring standard). Pick one at bootstrap. |
| `cowork/` | Setup material for Claude Cowork, which cannot read this repo's `.claude/`. |

## 3. The work cycle

```
/task-next     pick the next task, get an agent-routing recommendation
   ↓
   write the failing test
   ↓
   write the code (contract comment first, then the body)
   ↓
   /contract-sync   find and handle consumers affected by the change
   ↓
/task-done     verify Definition of Done, update board + knowledge base
```

Full detail: `.claude/rules/workflow.md`.

## 4. Code rules in one screen

- Functions: **≤ 20 lines**, **≤ 3 parameters**, **one responsibility**. Over the limit, split it —
  unless splitting genuinely hurts readability, and then say why in the code.
- Names: **≤ 3 words**, meaningful to a human, no abbreviations nobody outside this repo knows.
- Check for an applicable **design pattern before writing**. If one fits, use it and name it
  in the contract comment. If none fits, do not force one.
- No known or obvious security holes. See `.claude/rules/security.md`.
- Document to the **dominant standard of the language** (recorded in the active stack profile),
  plus the `@contract` block. Telegraphic style, no filler words, no full sentences.

Detail and rationale: `.claude/rules/code-quality.md`.

## 5. Subagents

Allowed for well-scoped subtasks — after a cost/benefit check that is either done now and
written to `knowledge/90-meta/subagent-decisions.md`, or already recorded there as positive
for this kind of task. Never spawn a subagent to avoid thinking about a problem yourself.

## 6. Agent routing: Claude Code or Cowork

Before starting a task, decide which agent should do it:

| Use **Claude Code** for | Use **Cowork** for |
| --- | --- |
| Writing, refactoring, testing code | Research and synthesis into the knowledge base |
| Anything that touches git | Documents, spreadsheets, presentations |
| Running builds, linters, test suites | Reading and triaging material from outside the repo |
| Work that needs the hooks in `.claude/` | Long unattended tasks, scheduled runs |

If the current agent is the wrong one, say so and state what the other should do — do not
push through with the wrong tool. Cowork does not load this repo's `.claude/` configuration;
see `cowork/README.md`.

## 7. Language

- Everything under `.claude/` and all code, comments and commit messages: **English**.
- Everything under `knowledge/` and the top-level `README.md`: **German**.

## 8. When rules collide

Order of precedence: safety > correctness > the rules above > speed.
If a rule blocks you and you believe it is wrong, do not silently work around it —
create a task, write down the reasoning, and ask.
