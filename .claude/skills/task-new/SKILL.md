---
description: Create a new task correctly - task file, frontmatter, acceptance criteria, agent routing recommendation, and the card on the kanban board. Use when work is identified that is not yet on the board, including follow-up work from a contract change.
argument-hint: [short title]
allowed-tools: Read, Glob, Grep, Write, Edit
---

# New task

## 1. Pick the ID

Highest existing `T-XXXX` in `knowledge/10-pm/tasks/` plus one. Four digits, zero padded.

## 2. Write the task file

`knowledge/10-pm/tasks/T-XXXX <kurzer-titel>.md`, from
`knowledge/90-meta/templates/task.md`. German. Required:

- **Ziel** — one sentence: what is true afterwards that is not true now.
- **Akzeptanzkriterien** — checkbox list, each one testable. If you cannot say how it would be
  verified, it is not a criterion yet.
- **Kontext** — wikilinks to related tasks, ADRs, knowledge notes. At least one.
- **Agent** — `claude-code` or `cowork`, with a half-line reason (routing table in `CLAUDE.md` §6).
- **Abhängigkeiten** — blocking tasks, as wikilinks.

Frontmatter: `status`, `priority`, `agent`, `owner` (empty until claimed), `created`, `tags`.

## 3. Place the card

Add one line to the correct lane in `knowledge/10-pm/board.md`:

```
- [ ] [[T-0042 Token-Refresh]]
```

Lane rules:
- Acceptance criteria written and dependencies clear → **Ready**
- Still vague → **Backlog**
- Follow-up from a contract change → **Ready**, never Backlog

Only add the line. Do not reformat the board, do not reorder other cards.

## 4. Link back

If this task came from another task, add the wikilink to both files.
