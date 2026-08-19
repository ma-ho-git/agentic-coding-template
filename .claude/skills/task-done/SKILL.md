---
description: Close a task properly - verify the Definition of Done, update the board and task file, capture what was learned in the knowledge base, and log progress. Use when the work on a task looks finished.
allowed-tools: Read, Glob, Grep, Edit, Write, Bash
---

# Finish a task

Do not skip a step because it feels obvious. Report honestly if a check fails —
a task that is not done stays not done.

## 1. Verify the Definition of Done

Walk the list in `.claude/rules/workflow.md` and state the result of each item:

1. Every acceptance criterion in the task file checked off.
2. The requirement's **Abnahme** is actually satisfied — not the task's criteria, the
   requirement's. If they diverge, the task was scoped wrong; say so rather than papering
   over it.
3. Tests: run the full suite from `stacks/active.md`. Green, no skips added.
4. Linter and type checker: no new findings.
5. `@contract` blocks of all touched files accurate and dated today.
6. Contract consumers: updated, or a follow-up task exists in `Ready` and is linked.
7. Traceability: `tools/check_traceability.py` reports no errors.
8. Knowledge captured (step 2 below).
9. Progress logged (step 4 below).

Any failure → fix it, or move the card to `Review` with a note. Not to `Done`.

## 2. Capture what was learned

Ask yourself, and answer in writing:

- Did I research anything outside the repo? → `/kb-capture` as `knowledge`
- Did I choose between real alternatives? → ADR in `knowledge/10-pm/decisions/`
- Did anything take more than one attempt? → `/kb-capture` as `troubleshooting`
- Did I use a subagent? → append the outcome to `knowledge/90-meta/subagent-decisions.md`

"Nothing worth writing down" is a valid answer, but say it explicitly.

## 3. Update task, requirement and board

- Task file: `status: done`, `finished: <today>`, criteria checked, links to any note written.
- Board: move the one card line to the `Done` lane and change `- [ ]` to `- [x]`.
- Requirement: when **every** task in its `tasks:` list is now done, set it to
  `status: umgesetzt` and `updated:` to today. While any task is open, leave it
  `vereinbart` — `tools/check_traceability.py` reports the mismatch otherwise.
- Learned something that sharpens the requirement without changing its statement? Record it
  under `Präzisierungen` there. A changed statement is not a sharpening — that is
  `/req-change`.

## 4. Log progress

Append to the current month's file in `knowledge/10-pm/progress/`:

```
## 2026-08-19 — T-0042 Token-Refresh
- Ergebnis: <ein Satz>
- Entscheidungen: [[ADR-0003 ...]]
- Neu gelernt: [[...]]
- Offene Folgeaufgaben: [[T-0051 ...]]
```

## 5. Report

Two or three sentences: what is now true, what is still open, what the user should decide next.
