---
description: Create a new task correctly - task file, frontmatter, acceptance criteria, agent routing recommendation, and the card on the kanban board. Use when work is identified that is not yet on the board, including follow-up work from a contract change.
argument-hint: [short title]
allowed-tools: Read, Glob, Grep, Write, Edit
---

# New task

## 1. Pick the ID

Highest existing `T-XXXX` in `knowledge/10-pm/tasks/` plus one. Four digits, zero padded.

## 2. Name the requirement it serves

Before anything else. A task without a requirement is work nobody asked for.

Find the agreed requirement in `knowledge/05-requirements/` and put it in the frontmatter:

```yaml
implements: ["[[REQ-0001 Titel]]"]
```

- The requirement must be `status: vereinbart`. A task on a draft requirement is premature —
  finish the discussion first.
- No fitting requirement exists → run `/req-elicit`. Do **not** invent one to unblock
  yourself, and do not fall back to the infrastructure exception.
- **Infrastructure and maintenance only** — tooling, CI, dependency bumps, repo chores —
  may go without, and then the reason is mandatory:

  ```yaml
  implements: []
  infrastruktur: <why this serves no product requirement>
  ```

A hook blocks the file otherwise, and `tools/check_traceability.py` re-checks it in CI.

## 3. Write the task file

`knowledge/10-pm/tasks/T-XXXX <kurzer-titel>.md`, from
`knowledge/90-meta/templates/task.md`. German. Required:

- **Anforderung** — which requirement, and which part of it this task delivers.
- **Ziel** — one sentence: what is true afterwards that is not true now.
- **Akzeptanzkriterien** — checkbox list, each one testable. If you cannot say how it would be
  verified, it is not a criterion yet.
- **Kontext** — wikilinks to related tasks, ADRs, knowledge notes. At least one.
- **Agent** — `claude-code` or `cowork`, with a half-line reason (routing table in `CLAUDE.md` §6).
- **Abhängigkeiten** — blocking tasks, as wikilinks.

Frontmatter: `implements`, `status`, `priority`, `agent`, `owner` (empty until claimed),
`created`, `tags`.

## 4. Place the card

Add one line to the correct lane in `knowledge/10-pm/board.md`:

```
- [ ] [[T-0042 Token-Refresh]]
```

Lane rules:
- Acceptance criteria written and dependencies clear → **Ready**
- Still vague → **Backlog**
- Follow-up from a contract change → **Ready**, never Backlog

Only add the line. Do not reformat the board, do not reorder other cards.

## 5. Link back

If this task came from another task, add the wikilink to both files.

Add the task to the requirement's `tasks:` list as well. Both directions, same edit —
a one-sided link is what `tools/check_traceability.py` reports as an error.
