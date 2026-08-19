---
description: A requirement changed - find the affected tasks, tests and code through the traceability chain, update what can be updated now, and turn the rest into follow-up tasks. Use whenever a requirement's statement, acceptance or priority changes, or one is withdrawn.
argument-hint: [REQ-XXXX]
allowed-tools: Read, Glob, Grep, Edit, Write
---

# Requirement change

The counterpart to `/contract-sync`, one level up. There the `consumers:` list carries the
blast radius; here it is the requirement's `tasks:` list.

Rules: `.claude/rules/requirements.md`.

## 1. Sharpening or change?

Decide first, they are not handled the same way.

| | Meaning | Handling |
| --- | --- | --- |
| **Sharpening** | same statement, more precise. "fast" → "p95 under 200 ms" | Record under `Präzisierungen` with today's date. No follow-up needed unless a test contradicts it. |
| **Change** | different statement, different acceptance, changed priority, withdrawal | Full run of this skill. |

When unsure, treat it as a change. The cheap error is one follow-up task too many.

## 2. Determine the blast radius

1. Read the requirement's `tasks:` list. That is the primary radius — trust it first.
2. Verify it is not lying: grep the repository for the requirement ID. Every task carrying
   it in `implements:` but missing from `tasks:` is a **defect in the requirement file**.
   Add it, and say the list was stale.
3. For a **framework** requirement, also check what it shaped: ADRs referencing it, and
   detail requirements refining it. A changed framework requirement usually invalidates
   design decisions, not just tasks.

## 3. Classify each affected item

| Situation | Action |
| --- | --- |
| Task not started | Update its acceptance criteria now |
| Task in progress, small adjustment | Adjust now, tell the owner |
| Task done, code still correct | Nothing to change; note it |
| Task done, code now wrong | New task, lane **Ready**, linked from both files |
| ADR rests on the old requirement | Add a re-check section to the ADR, or supersede it |
| Detail requirement now contradicts the framework | Surface the conflict; do not resolve it alone |

Follow-up work goes to `Ready`, never `Backlog`. A requirement the code no longer satisfies
is urgent by definition — the same reasoning as contract debt.

## 4. Withdrawal

A withdrawn requirement gets `status: verworfen` and a reason. **Never delete it** — the
same rule as deprecated knowledge notes. Then check every task that implemented it: is the
code now unnecessary? Unnecessary code that stays is the expensive kind of debt.

## 5. Update both sides

- Requirement: statement, acceptance, `tasks:`, `updated:` to today
- Every task touched: `implements:` and its acceptance criteria
- `baseline.md` if a framework requirement's category coverage changed

Both directions, one commit. A one-sided update is how these lists decay.

## 6. Report

Name: what changed, which tasks were adjusted, which follow-ups were created, and which
stale links you repaired. Stale links are worth a line in the progress log — they say the
discipline is slipping, and that is more useful to know than the individual fix.
