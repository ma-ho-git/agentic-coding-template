# Workflow

## Before the board exists

Nothing is built until the framework is agreed. `knowledge/05-requirements/baseline.md`
must read `baseline_status: vereinbart` before the first line of production code.
See `.claude/rules/requirements.md`.

Per development stage afterwards: `/req-elicit` for that stage's detail requirements,
then tasks. Never tasks first.

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
