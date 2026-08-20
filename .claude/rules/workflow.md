# Workflow

## Project scope

Not every project deserves the same ceremony. A throwaway script and a product other people
depend on need the same *guardrails*, but not the same amount of *writing*.

`/bootstrap` asks which of three the project is and records the answer as `project_scope` in
`.claude/hooks/config.json`. The **reason** for the choice goes into the Projektzuschnitt
section of `knowledge/05-requirements/baseline.md` — a scope with no recorded reason is an
excuse, not a decision. Unknown or missing value means `produkt`: the fallback buys more
ceremony, never less.

| Scope | What it is | Elicitation | Documentation |
| --- | --- | --- | --- |
| `skript` | throwaway, personal, no second user | all six categories still asked; a one-line „trifft hier nicht zu" is a fine answer | vision three lines; ADR only for decisions that are hard to undo; progress entries one line; troubleshooting notes still mandatory |
| `werkzeug` | passed on to others, small surface | real answers for `funktional`, `technisch`, `sicherheit`, `recht`; the rest may be dismissed with a reason | vision, glossary and risks; ADR for every real alternative weighed |
| `produkt` | maintained over time, more than one contributor | every category answered with an agreed requirement | everything in `.claude/rules/knowledge-base.md`, without reduction |

**What scope never touches:**

- **Requirements themselves.** Every scope passes through the start gate, and every category
  is asked in every scope. What shrinks is the length of the answer, not the list of questions.
- **Rigid guardrails.** Secrets, contract blocks, task traceability, destructive git, the
  start gate — identical in all three. See `.claude/rules/guardrails.md`.
- **TDD.** A failing test first, in every scope.

Only flexible guardrails and documentation duties scale. If you find yourself arguing that a
small scope should switch something off, you have found either a rule that was never worth
having, or a rule you are about to break — say which.

Changing scope later is a normal decision: change the config value, and write the new reason
into `baseline.md` next to the old one. Never delete the old reason.

## Before the board exists

Nothing is built until the framework is agreed. `knowledge/05-requirements/baseline.md`
must read `baseline_status: vereinbart` before the first line of production code.
See `.claude/rules/requirements.md`.

Per development stage afterwards: `/req-elicit` for that stage's detail requirements,
then tasks. Never tasks first.

## Before the first code task

Between the open gate and the first line of code sits one more question: **does this already
exist?** `/solution-scan` measures open-source candidates against the agreed requirements —
licence, maintenance, and per requirement whether it is fulfilled, partly fulfilled or not.

The offer is mandatory, the search is not. Both answers are legitimate; an unanswered one is
not, and `check_gate.py` refuses production code while
`knowledge/05-requirements/fremdloesungen.md` reads `scan_status: offen` or is missing.
`gesucht` and `uebersprungen` — the latter with the user's reason — both open it.

The timing is the point. Earlier there is no yardstick to measure a candidate against; later
the home-made version wins because it exists, not because it is better. If a candidate is
adopted, its legal obligations run through the register of third-party components.

## Task lifecycle

A task is a file in `knowledge/10-pm/tasks/` and a card in `knowledge/10-pm/board.md`.
Nothing else counts as work in progress.

Every task names the requirement it serves in `implements:`. The only exception is
infrastructure and maintenance work, which states its reason in `infrastruktur:`.
A hook enforces this on write, `tools/check_traceability.py` re-checks it in CI.

Lanes: `Backlog` → `Ready` → `Doing` → `Review` → `Done`.

- **Backlog** — captured, not yet refined. May be vague.
- **Ready** — has acceptance criteria and an owner-agent recommendation. Can be picked up.
- **Doing** — exactly one agent owns it. Set `owner` in the task frontmatter.
- **Review** — code complete, awaiting verification (tests green, review pass, human sign-off).
- **Done** — Definition of Done met.

Move a card by editing exactly one line in `board.md`. Cards are wikilinks only —
never put task detail on the card.

## Definition of Done

A task may only move to `Done` when all of these hold:

1. All acceptance criteria in the task file are checked off.
2. The **Abnahme** of the requirement it implements is satisfied — not just the task's own
   criteria. Diverging criteria mean the task was scoped wrong; say so instead of hiding it.
3. Tests exist that fail without the change and pass with it. Full suite is green.
   Every error path the change **handles** has a test that triggers it — a handled failure
   without a test is an assumption (`.claude/rules/robustness.md`).
4. Linter and type checker (per the active stack profile) report no new findings.
5. `@contract` blocks of every touched file are accurate and dated today.
6. Every consumer affected by a contract change is either updated, or has a follow-up
   task in `Ready` linked from this task. Never `Backlog` — contract debt is urgent.
7. `tools/check_traceability.py` reports no errors, and the requirement moves to
   `umgesetzt` once all of its tasks are done.
8. Anything learned that is worth knowing again is in `knowledge/` (see `knowledge-base.md`).
9. Progress log entry appended in `knowledge/10-pm/progress/`.

## Parallel work

Multiple agents may work at once. To stay conflict-free:

- Claim a task by setting `owner` and `status` in the **task file** first, then move the board card.
- Never edit a task file you do not own.
- `board.md` is the only shared file. Touch one line per move. If you hit a conflict,
  re-read the file and re-apply your single line — never overwrite the whole board.
- Run `/board-sync` if board and task frontmatter disagree.

## Commits

- One task per branch: `task/T-XXXX-short-slug`.
- Conventional commit subjects: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:`.
- Reference the task: `feat: add token refresh (T-0042)`.
- Commit only when the user asks. Never push to the default branch directly.
