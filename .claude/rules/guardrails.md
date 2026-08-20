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
| Production code before the framework is agreed | rigid | `check_gate.py`, `deny` |
| Production code before the existing-solutions decision | rigid | `check_gate.py`, `deny` |
| Registered component without its licence text | CI | `check_licenses.py`, error in CI |
| Assignments, parameters, name length | flexible | `check_quality.py`, hint |
| Nesting depth, file length | flexible | `check_quality.py`, hint |
| Exception dropped without a reason | flexible | `check_quality.py`, hint |
| Stale `updated:` in a contract block | flexible | `check_contract.py`, hint |

Thresholds for the flexible ones live in `.claude/hooks/config.json` and are meant to be
tuned per project. The rigid ones are not thresholds; they are boundaries.

The start gate deserves a note: it is the one boundary that protects decisions reserved for
the human, and `check_gate.py` refuses writes to product source while either of its two
conditions is unmet — the framework is agreed, and the existing-solutions question is
answered (`ADR-0011`). Tooling,
tests, examples and everything that is not a source file stay writable — otherwise you could
not build the machinery that lets the framework be agreed in the first place. A missing
`baseline.md` counts as closed: fail closed, per `.claude/rules/security.md`.

## Visibility is part of the design

Every message carries its class. Without it a user cannot tell a wall from a hint, and
whatever cannot be told apart is eventually treated the same — as noise. `block()`, `deny()` and
`advise()` in `_common.py` prepend the label, so a new hook inherits it by using them.

## Project scope never moves a rigid guardrail

`project_scope` (`.claude/rules/workflow.md`) scales how much gets *written* — elicitation
depth, ADR duty, progress detail. It does not scale what is *enforced*. Every check in
the table above behaves identically in `skript`, `werkzeug` and `produkt`, and no scope
exempts a path, lowers a threshold to zero, or opens the start gate.

This is deliberate. „Ist doch nur ein kleines Skript" is exactly the argument under which a
secret reaches the history or a task loses its requirement — and those are the violations
that cannot be repaired afterwards, which is what made them rigid in the first place. A
scope that could switch them off would make the class meaningless.

An unknown or missing scope is read as `produkt`: falling back costs ceremony, never safety.

## A third place: the CI check

Two classes cover what a hook can decide at write time. The licence register is neither:
the damage from an unfulfilled licence obligation happens at **distribution**, not at
writing, and a write hook would block the wrong moment — you would be refused a source file
because of a component the file has nothing to do with.

So `check_licenses.py` runs in CI, which is the last gate before a change is merged and
published. It fails the run like an error, not like a hint. That is deliberate and it is
recorded here so nobody later "fixes" it into a hook.

The same reasoning applies to `check_traceability.py`. Both are boundaries; they simply sit
at the moment where the boundary is actually crossed.

`check_placeholders.py` sits at a third moment again — `/bootstrap`, the one point at which a
clone stops being a template. In this repository it reports twelve documents and exits 1, and
that is the correct answer: the placeholders belong here. A check whose correct result is
"red" must never run in CI.

## What this does not cover

Guardrails constrain **how** work is done. They say nothing about **whether** it is worth
doing — that is what requirements are for (`.claude/rules/requirements.md`), and no
guardrail substitutes for them.
