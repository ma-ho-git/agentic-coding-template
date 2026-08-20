# Guardrails

Agents are fast and tireless and have no instinct for which rule matters right now. Two
classes give them one: what must never bend, and what is merely usually better.

Decision and rationale: `knowledge/10-pm/decisions/ADR-0006 …`.
German terms used with the user: **starre Leitplanke** = rigid, **flexible Leitplanke** =
flexible. The messages are English because everything under `.claude/` is.

## Rigid — `[RIGID]`

For decisions whose violation **cannot be healed by fixing it later**, or that damage the
project, its surroundings, or its traceability outright.

- **Machine-enforced.** Exit code 2, or `permissionDecision: deny`.
- **A rigid guardrail that is not machine-enforced is not rigid.** Written only in prose, it
  is a flexible one wearing the wrong label.
- The agent cannot override it. The human overrides it by changing the rule.

## Flexible — `[FLEXIBLE]`

For **optimisation decisions**: one answer is better, but the case at hand may justify the
worse one.

- Produces a hint. Never blocks.
- Whoever exceeds it **writes the reason into the code**. The deviation becomes visible, not
  forbidden.

## Which class does a new rule belong to?

Rigid if **any** of these holds:

1. The violation cannot be undone — a secret in the git history stays there.
2. It endangers the project, its surroundings or its data.
3. It destroys traceability for good — work with no requirement, code with no contract.
4. It bypasses a decision reserved for the human — the start gate.

Otherwise flexible. **In doubt, flexible.** A wrongly rigid guardrail costs more trust than
a wrongly flexible one costs quality.

## The current assignment

| Check | Class | Enforced by |
| --- | --- | --- |
| Credentials in a write | rigid | `check_secrets.py`, exit 2 |
| Missing `@contract` block | rigid | `check_contract.py`, exit 2 |
| Task without a requirement | rigid | `check_task.py`, exit 2 |
| Destructive git commands | rigid | `git_guard.py`, `deny` |
| Production code before the start gate opens | rigid | **not yet enforced** — T-0020 |
| Assignments, parameters, name length | flexible | `check_quality.py`, hint |
| Nesting depth, file length | flexible | `check_quality.py`, hint |
| Stale `updated:` in a contract block | flexible | `check_contract.py`, hint |

Thresholds for the flexible ones live in `.claude/hooks/config.json` and are meant to be
tuned per project. The rigid ones are not thresholds; they are boundaries.

One row is honest about itself: the start gate is classified rigid but is still only carried
by skills and a session-start notice, which is prose. By this file's own definition it is
therefore not yet rigid. `T-0020` closes that gap.

## Visibility is part of the design

Every message carries its class. Without it a user cannot tell a wall from a hint, and
whatever cannot be told apart is eventually treated the same — as noise. `block()` and
`advise()` in `_common.py` prepend the label, so a new hook inherits it by using them.

## What this does not cover

Guardrails constrain **how** work is done. They say nothing about **whether** it is worth
doing — that is what requirements are for (`.claude/rules/requirements.md`), and no
guardrail substitutes for them.
