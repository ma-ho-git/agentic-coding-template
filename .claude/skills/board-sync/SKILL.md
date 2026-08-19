---
description: Check the kanban board against the task files and repair inconsistencies - cards in the wrong lane, missing cards, orphaned cards, tasks with no card. Use when the board looks wrong, after a merge conflict, or when several agents worked in parallel.
allowed-tools: Read, Glob, Grep, Edit
---

# Board sync

The task file's `status` frontmatter is the source of truth. The board is a view of it.

## 1. Collect both sides

- Every file in `knowledge/10-pm/tasks/` → id, title, `status`, `owner`, `priority`.
- Every card in `knowledge/10-pm/board.md` → lane, wikilink target.

## 2. Find the mismatches

| Finding | Repair |
| --- | --- |
| Task has no card | Add a card to the lane matching its `status`. |
| Card points at a non-existent task | Remove the card. Report it — it may be a lost file. |
| Lane and `status` disagree | Move the card. The frontmatter wins. |
| Card appears in two lanes | Keep the one matching `status`, delete the other. |
| `status: doing` with no `owner` | Move to `Ready`, clear `started`, report it as abandoned. |
| Card carries text instead of a wikilink | Convert it; move the text into the task file. |

## 3. Check board hygiene

- Lanes are exactly: `Backlog`, `Ready`, `Doing`, `Review`, `Done`.
- The `Done` lane keeps the `**Complete**` marker as its first line.
- The `%% kanban:settings` block at the end of the file is intact.
- Done cards use `- [x]`, all others `- [ ]`.

## 4. Report

Name every repair. If you found more than two mismatches, say what process step is being
skipped — that is the actual problem, not the board.
