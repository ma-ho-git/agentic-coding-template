# Requirements

No production code without a requirement it serves. This is the layer the rest of the
template stands on: a test proves the code does what the task said, a requirement is the
only thing that says the task was worth doing.

Decision and rationale: `knowledge/10-pm/decisions/ADR-0005 …`.
What is adopted from Sommerville, and what is deliberately not:
`knowledge/20-knowledge/Sommerville Software Engineering - was das Template übernimmt.md`.

## Two levels

Requirements are **not** gathered purely incrementally — that leaves the target artefact
too vaguely described and lets architecture-shaping constraints surface far too late.

### Level 1 — Framework (`ebene: rahmen`)

Answers *what is being built, and what must hold while building it.* Must be **complete and
agreed before the first line of production code**. Six categories:

| Category | Covers |
| --- | --- |
| `funktional` | the system's core service, coarse |
| `technisch` | platform, interfaces, data, performance |
| `organisatorisch` | operation, roles, delivery, process |
| `sicherheit` | protection needs, authentication, privacy |
| `recht` | regulation, licences, retention |
| `qualitaet` | usability, reliability, maintainability |

These are architecture-shaping. Discovering one late throws away finished work.

### Level 2 — Detail (`ebene: detail`)

Elicited **per development stage, on demand — never stockpiled**. During coding they may be
sharpened iteratively:

- **Sharpening** (same statement, more precise) → record it in the requirement, note the date.
- **Change** (different statement) → run `/req-change`. Never edit the statement silently.

## The start gate

`knowledge/05-requirements/baseline.md` carries `baseline_status: entwurf | vereinbart`.
Development starts only at `vereinbart`.

The framework is complete when **every** category above either

- has at least one agreed framework requirement, **or**
- is explicitly justified as not applicable.

Both failure modes are real: silently skipping security, and inventing security requirements
for a throwaway script. The forced justification hits the middle.

Only the user can move the gate to `vereinbart`. An agent proposes; it never self-certifies.

## What a requirement must carry

One file per requirement, `knowledge/05-requirements/REQ-XXXX <title>.md`.

| Field | Meaning |
| --- | --- |
| `ebene` | `rahmen` or `detail` |
| `kategorie` | one of the six above |
| `prioritaet` | `muss`, `soll`, `kann` |
| `status` | `entwurf`, `vereinbart`, `umgesetzt`, `verworfen` |
| `quelle` | which stakeholder or document it comes from |
| `nachweis` | how satisfaction is proven: `test`, `messung`, `review`, `demo` |
| `tasks` | wikilinks to the tasks implementing it |

Body: the statement itself, the **rationale**, and a concrete **acceptance** description.

- **No source, no traceability.** Every requirement names where it came from.
- **No rationale, no requirement.** Without a reason it is cargo cult and nobody can judge
  it later.
- Only `vereinbart` requirements may be built on. `entwurf` means still under discussion.

## Verifiability — the rule that matters most

If you cannot say how it would be checked, it is not a requirement yet.

| Rejected | Accepted |
| --- | --- |
| "must be user-friendly" | "a trained user completes task X in under 30 s" |
| "must be fast" | "p95 response under 200 ms at 50 concurrent users" |
| "must be secure" | "no plaintext credential at rest; dependency audit clean before release" |
| "must be maintainable" | the size and naming limits in `code-quality.md` apply |

This is what lets TDD dock onto requirements at all: an unmeasurable requirement produces
an unwritable test.

## Validation — the five checks

Run by `/req-validate` over the whole set. From Sommerville:

| Check | Question |
| --- | --- |
| Validity | Does the system provide the functions that best support the need? |
| Consistency | Are there conflicts between requirements? |
| Completeness | Are all functions the user needs included? |
| Realism | Implementable with the available budget and technology? |
| Verifiability | Can it be checked at all? |

Conflicts are normal, especially between quality requirements — performance versus
maintainability, security versus convenience. Name the conflict and decide it in an ADR;
do not quietly satisfy one and drop the other.

## Traceability

```
Stakeholder → baseline.md → REQ-XXXX → T-XXXX → test → code (@contract)
```

Maintained in both directions and checked by `tools/check_traceability.py`:

- Task without `implements:` → error. Exception: infrastructure and maintenance work,
  marked as such with a stated reason.
- `implements:` pointing at a non-existent requirement → error.
- Agreed requirement with no task → warning, not yet implemented.
- Requirement marked `umgesetzt` while its tasks are unfinished → error.

## What this does not replace

Requirements come **before** the existing rules, they replace none of them. TDD,
`@contract`, the size and naming limits, the security rules and the knowledge base
obligations all continue to apply unchanged.
