---
description: After changing a function's or file's public surface, find every affected call site via the contract comments, update what can be updated now, and turn the rest into follow-up tasks. Use whenever a signature, return type, error behaviour or invariant changes.
allowed-tools: Read, Glob, Grep, Edit, Write
---

# Contract sync

The point of the `@contract` block is that you do **not** have to search the whole codebase.
Trust it first, then verify it.

## 1. Determine the blast radius

For every file you changed:

1. Read its `@contract` block. The `consumers:` list is the primary blast radius.
2. Read the `consumers:` of every public symbol you touched inside the file.
3. Now verify the list is not lying: grep for the changed symbol names across the repo.
   Any call site not in `consumers:` is a **defect in the contract block** — add it,
   and note that the block was stale.

## 2. Classify each consumer

| Situation | Action |
| --- | --- |
| Still compiles and still correct | update `depends-on:` only |
| Breaks, small fix | fix it now, in this task |
| Breaks, large fix or other agent's area | `/task-new`, lane **Ready**, link both tasks |
| Out of scope but silently still correct | leave it, note it in the task file |

Contract debt goes to `Ready`, never `Backlog`. It is urgent by definition.

## 3. Update both sides of every link

Each changed relationship touches two blocks:

- callee's `consumers:` — who calls me
- caller's `depends-on:` — what I call

Both in the same commit. A one-sided update is how these lists decay.

## 4. Refresh metadata

Set `updated:` to today on every block you verified — not just the ones you changed.
The date means "checked against the code on this day".

## 5. Report

List: files changed, consumers updated, follow-up tasks created, stale contract blocks
you found and repaired. If you found stale blocks, that is worth a line in the progress log —
it tells the team the discipline is slipping.
