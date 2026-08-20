# Requirements

No production code without a requirement it serves. A test proves the code does what the
task said; a requirement is the only thing that says the task was worth doing.

Decision: `knowledge/10-pm/decisions/ADR-0005 …`. What is adopted from Sommerville and what
is not: `knowledge/20-knowledge/Sommerville Software Engineering - was das Template übernimmt.md`.

## The scenario — optional to have, binding once it exists

Before elicitation the user may describe the project in their own words — `/szenario`,
written to `knowledge/05-requirements/szenario.md`. Optional: offered once, a no is a
complete answer.

**Once it exists, it is the basis.** Elicitation derives proposals from it instead of asking
cold, and every requirement derived from it does two things:

- names it in `quelle` — `quelle: <Stakeholder> — "[[Szenario]]"`
- **quotes the passage** it came from, under `## Herkunft`, with the section name

The quote is what separates deriving from inventing. Without it, nobody can tell afterwards
which sentence the user actually said and which the agent supplied — and a requirement the
user never stated, wearing the look of one they agreed, is the worst artefact this method
can produce. `tools/check_traceability.py` reports a scenario that no requirement derives
from; the *content* of the coverage is checked by `/req-validate` and by the user, because
prose cannot be diffed mechanically.

A scenario is not a requirement: it is unstructured, may contradict itself, and carries no
`Abnahme`. Never build from it directly.

## Two levels

Not purely incremental — that leaves the target artefact too vaguely described and lets
architecture-shaping constraints surface far too late.

**Framework** (`ebene: rahmen`) — *what is being built, and what must hold while building it.*
Complete and agreed **before the first line of production code**:

| Category | Covers | Sommerville |
| --- | --- | --- |
| `funktional` | the system's core service, coarse | functional |
| `technisch` | platform, interfaces, data volumes, operating environment | product |
| `qualitaet` | how good: performance, compatibility, usability, reliability, maintainability, flexibility, safety | product |
| `sicherheit` | protection needs, authentication, privacy | product + external |
| `organisatorisch` | operation, roles, delivery — **and how development itself is done**: process standards, coding standards, mandatory tooling | organisational |
| `recht` | regulation, licences, retention, rights to the result | external |

## Functional and non-functional — why they are elicited differently

`funktional` is the functional category. **The other five are non-functional**, in
Sommerville's three groups: product (how the delivered thing behaves), organisational (rules
of the house, including development process), external (imposed from outside).

That is not vocabulary for its own sake. The two kinds behave differently in elicitation:

- **Functional requirements the user volunteers.** A scenario consists almost entirely of
  them. Ask "what should it do" and you get answers.
- **Non-functional requirements the user never volunteers.** Not because they do not care —
  because nobody thinks to say "and it should still work when the network is down". They
  only surface when asked **against a list**. That list is the point of the six categories.

Second difference: a functional requirement is usually testable as written; a non-functional
one is usually not, until it carries a number or an observable scenario. Hence the
verifiability rule below, which exists almost entirely for the non-functional five.

### Where does it go when two categories fit?

`technisch` and `qualitaet` overlap, and so do `organisatorisch` and `qualitaet`. Faustregel:

- **What the system must run on** → `technisch` ("Python 3.11 under Linux, files up to 100 MB")
- **How well it must do it** → `qualitaet` ("10,000 rows in under 5 seconds")
- **How the team must work** → `organisatorisch` ("test-driven", "docstrings per the profile")

The categories are a **checklist for completeness, not a taxonomy**. A requirement filed one
category off is not a defect; a category nobody asked about is. If a requirement plausibly
fits two, pick one and move on — but never let a thing fall between them.

**Detail** (`ebene: detail`) — per development stage, on demand, never stockpiled. While
coding they may be *sharpened*: same statement, more precise, recorded with a date. A
*different* statement is a change and goes through `/req-change`.

## The start gate

`knowledge/05-requirements/baseline.md` carries `baseline_status: entwurf | vereinbart`.
Development starts only at `vereinbart`.

Complete means every category above either has an agreed framework requirement **or** is
explicitly justified as not applicable. Both failure modes are real: silently skipping
security, and inventing security requirements for a throwaway script.

Only the user opens the gate. An agent proposes; it never self-certifies.

## What a requirement carries

One file per requirement, `knowledge/05-requirements/REQ-XXXX <title>.md`.

| Field | Meaning |
| --- | --- |
| `ebene` | `rahmen` or `detail` |
| `kategorie` | one of the six above |
| `prioritaet` | `muss`, `soll`, `kann` |
| `status` | `entwurf`, `vereinbart`, `umgesetzt`, `verworfen` |
| `quelle` | which stakeholder or document it comes from |
| `nachweis` | `test`, `messung`, `review` or `demo` |
| `tasks` | wikilinks to the tasks implementing it |

Body: statement, **rationale**, concrete **acceptance**. No source means no traceability;
no rationale means cargo cult. Only `vereinbart` requirements may be built on.

## Verifiability — the rule that matters most

If you cannot say how it would be checked, it is not a requirement yet.

| Rejected | Accepted |
| --- | --- |
| "must be user-friendly" | "a trained user completes task X in under 30 s" |
| "must be fast" | "p95 response under 200 ms at 50 concurrent users" |
| "must be secure" | "no plaintext credential at rest; dependency audit clean before release" |

This is what lets TDD dock onto requirements at all: an unmeasurable requirement produces an
unwritable test.

## Validation

`/req-validate` runs Sommerville's five checks over the set: **validity, consistency,
completeness, realism, verifiability**. Conflicts between quality requirements are normal.
Name the conflict and decide it in an ADR; never quietly satisfy one and drop the other.

## Traceability

`Stakeholder → Szenario → baseline.md → REQ-XXXX → T-XXXX → test → code (@contract)`

The scenario link is present only when a scenario was captured; the chain is complete
without it.

Both directions, checked by `tools/check_traceability.py` and by a hook on task files.
A task without `implements:` is an error; infrastructure and maintenance work is the only
exception and states its reason in `infrastruktur:`.

## What this does not replace

Requirements come **before** the existing rules and replace none of them. TDD, `@contract`,
the size and naming limits, the security rules and the knowledge base obligations all
continue to apply unchanged.
