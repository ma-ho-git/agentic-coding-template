---
paths:
  - "**/*.{py,pyi,ts,tsx,js,jsx,mjs,cjs,go,rs,java,kt,rb,php,cs,swift,c,h,cpp,hpp,scala,ex,exs,sh}"
---

# Robustness

The difference between a demo and something that runs is what happens when things go wrong.
A beginner cannot ask for this — they do not know the question exists. That makes it the
agent's job, not theirs.

Scope: failures **without** an attacker. Attacks are `.claude/rules/security.md`; the two
overlap only at *fail closed*, which holds in both.

## Every failure gets one of four answers

Not "handled" in the abstract — one of these, chosen on purpose:

| Answer | When | Looks like |
| --- | --- | --- |
| **Prevent** | the failure is avoidable by construction | validate at the boundary, make the bad state unrepresentable |
| **Handle** | the failure is expected and there is a sensible response | retry with a budget, fall back, degrade, queue |
| **Propagate** | the caller knows more than you do | raise with context, do not log-and-swallow |
| **Crash on purpose** | it is a programmer error, not a runtime condition | fail fast and loudly; a corrupt process must not continue |

"Crash on purpose" is a legitimate answer and often the right one. Silence never is.

## The four classes to walk

Walk all four before calling a unit done. Most units have nothing to do in two of them —
say so, do not skip them.

**1. Input and boundaries.** Empty, zero, one, maximum, malformed, wrong encoding, duplicate,
out of order, absent. Validate on entry, not at the point of use.

**2. Exception paths.** What can throw here, and who is supposed to catch it? Catch narrow,
never bare. An exception caught and dropped is the single worst line in this file — if a
failure is genuinely ignorable, write *why* in the code, or a reader will read it as a bug.
A hook flags the silent case (`[FLEXIBLE]`): a comment in the block clears it, because the
point is not to forbid ignoring a failure but to make the decision visible.
When you re-raise, keep the cause. Distinguish an expected outcome (a return value) from a
defect (an exception); using exceptions for control flow hides both.

**3. Runtime and resources.** Anything that waits gets a **timeout** — no exceptions.
Anything that grows gets a **bound**: reading a whole file into memory, an unbounded queue,
cache or retry loop, a result set with no limit. Ask what happens at ten times the expected
input. Shared mutable state gets an owner; check-then-act across a boundary is a race.

**4. Failure of connected systems.** Every network call, database, queue, file system and
third-party API fails in **three** ways, not one:

- **not reachable** — the easy case, and the only one most code handles
- **too slow** — worse than down, because it consumes your resources while you wait
- **wrong answer** — the forgotten one: a 200 with an empty body, a truncated list, stale
  data, a schema that changed. Validate what comes back; it is untrusted input too.

Per dependency, decide and record: timeout, whether a retry is safe (**only if the operation
is idempotent** — a retried payment is a second payment), how many attempts with what
backoff, and what the caller sees when the budget is exhausted.

## Whose decision is it

- **What the user sees on failure is a requirement**, not an implementation detail — abort,
  degrade, retry silently, ask. It belongs in `knowledge/05-requirements/`, elicited via
  `/req-elicit`, which asks about every connected system.
- **How it is achieved is the agent's decision** — timeouts, backoff, guard clauses.

When you find yourself inventing the visible behaviour, stop: that is the user's call, and
guessing it produces software that does the wrong thing correctly.

## What this costs, and how to pay it

Error handling adds branches, and branches push against the nesting and assignment limits in
`.claude/rules/code-quality.md`. That tension is real and was decided, not waved away — see
`ADR-0009` in `knowledge/10-pm/decisions/`. The short version: **the limit stays, the shape
changes.**

- Guard clauses and early returns instead of an `else` that wraps the happy path.
- Error handling extracted into a named unit — `retry_with_budget`, `parse_or_reject`.
- The `try` around the whole function body, not around each statement.

If a unit still cannot fit, that is a signal it is doing two things: the work, and the
recovery. Split it.

## Testing it

A handled failure without a test is an assumption. Per error path you handle, one test that
actually triggers it — the Definition of Done in `.claude/rules/workflow.md` requires it.

Mock the dependency, not your own code (`.claude/rules/tdd.md`), and mock all three failure
modes, not just the unreachable one. The timeout and the wrong-answer tests are the ones
that find real bugs.

## Never

- Catch an exception and do nothing with it.
- Call anything over a network without a timeout.
- Retry a non-idempotent operation.
- Retry forever, or without backoff.
- Log an error and continue as if it had not happened.
- Turn an infrastructure failure into a silent empty result.
- Report success for work that partly failed.
