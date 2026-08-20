---
description: Derive an architecture decision from the quality requirements - name the conflicts between them, choose a structure, and record it as an ADR. Use once the framework is agreed and before building a component whose shape the quality requirements constrain.
argument-hint: [what is being decided]
allowed-tools: Read, Glob, Grep, Write, Edit
---

# Architecture from quality requirements

Architecture is not chosen for elegance. It is the answer to *which quality do we favour
when two of them pull apart.* This skill forces that question to be asked out loud.

Rules: `.claude/rules/requirements.md`. Sommerville chapter 6, as adopted here:
`knowledge/20-knowledge/Sommerville Software Engineering - was das Template übernimmt.md`.

## 1. Gather what constrains the shape

Read `knowledge/05-requirements/` and collect every requirement with
`kategorie: qualitaet`, `technisch` or `sicherheit`. Those three shape structure;
`funktional` requirements rarely do.

Only `status: vereinbart` counts. Building a structure on a draft is how rework starts.

Add `constraints.md` — a fixed platform or an existing system to integrate with removes
options before you start weighing anything.

## 2. Name the conflicts

This is the step people skip. Go through the collected requirements in pairs and say where
they pull apart. The recurring ones:

| Requirement wants | Pulls towards | Conflicts with |
| --- | --- | --- |
| Performance | few large components, short paths, local calls | maintainability, security layering |
| Maintainability | many small replaceable components | performance |
| Security | layered access, critical assets in inner layers | performance, convenience |
| Availability | redundancy, replaceable at runtime | simplicity |
| Safety | critical parts isolated in few subsystems | reuse |

**Write the conflict down even when the answer feels obvious.** "We favour maintainability
over performance here, because no requirement states a latency threshold" is a decision.
Silently favouring one is not.

If two agreed requirements genuinely cannot both hold, that is not an architecture problem
— it is a requirements defect. Stop and take it back to `/req-change`.

## 3. Choose a structure

Check whether a known architectural pattern fits before inventing one:

| Pattern | Fits when | Costs |
| --- | --- | --- |
| Layered | security or maintainability dominates; clear dependency direction | indirection, slower paths |
| Repository | many components share a large body of data | the store becomes a bottleneck |
| Client-Server | work distributes; several clients | network dependency, latency |
| Pipe and Filter | data flows through ordered transformations | poor fit for interactive use |
| MVC | several views on the same data | overhead for a single view |

These are **system-level** structures. Unit-level patterns — Factory, Strategy, Adapter and
friends — are a different decision and stay in `.claude/rules/code-quality.md`.

If none fits, write the plain structure and say so. A forced pattern is worse than none.

## 4. Record it as an ADR

`knowledge/10-pm/decisions/ADR-XXXX <title>.md`, from
`knowledge/90-meta/templates/decision.md`. Beyond the usual sections:

- **Kontext** names the requirements by ID that made this decision necessary
- **Optionen** carries the conflict from step 2, not a feature comparison
- **Entscheidung** states which quality was favoured and which was accepted as weaker
- **Konsequenzen** says what becomes harder, not only what becomes possible

Then link both directions: the ADR references the requirements, and each requirement gets
the ADR in its `related`. A one-sided link decays.

## 5. Report

Name: which requirements drove it, which conflict you found, what was decided, and what was
consciously accepted as the weaker side. If you found no conflict worth deciding, say that
plainly and skip the ADR — an ADR that records no tradeoff is paperwork.
