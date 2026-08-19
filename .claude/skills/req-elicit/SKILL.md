---
description: Elicit requirements with the user - the project framework before any code, or the detail requirements for the next development stage. Writes vision, stakeholders, glossary and REQ files. Use at project start, when the start gate is still open, or before beginning a new development stage.
argument-hint: [rahmen|stufe] [topic]
allowed-tools: Read, Glob, Grep, Write, Edit
---

# Elicit requirements

This is the one skill that **must ask the human**. Elicitation without a stakeholder is
guessing, and a guessed requirement is worse than none — it looks agreed.

Rules: `.claude/rules/requirements.md`. Decision:
`knowledge/10-pm/decisions/ADR-0005 …`.

## 1. Determine the mode

Read `knowledge/05-requirements/baseline.md`.

| `baseline_status` | Mode | What you elicit |
| --- | --- | --- |
| `entwurf` | **Framework** | What is being built, plus all six categories. Section 2. |
| `vereinbart` | **Stage** | Detail requirements for the next stage only. Section 3. |

If the argument says otherwise than the gate, follow the gate and say why.

## 2. Framework mode — before any production code

Goal: *what is being built, and what must hold while building it.* Work in this order and
write each answer down before moving on — do not collect everything and write at the end.

1. **Vision** → `vision.md`. Problem, target artefact, success criteria, **non-goals**.
   Push for non-goals; they are the most valuable part and users rarely volunteer them.
2. **Stakeholders** → `stakeholders.md`. Who is affected, who decides when requirements
   conflict. Ask explicitly who was *not* asked.
3. **The six categories** → one `REQ-XXXX` file per requirement, `ebene: rahmen`.

   | Category | Ask about |
   | --- | --- |
   | `funktional` | the core service — what must it do to be worth building? |
   | `technisch` | platform, interfaces, data, expected load, target environment |
   | `organisatorisch` | who operates it, how it ships, process constraints |
   | `sicherheit` | what needs protecting, who may see what, credential handling |
   | `recht` | licences, regulation, retention, rights to the result |
   | `qualitaet` | usability, reliability, maintainability beyond the code rules |

   For **every** category ask, even when it looks irrelevant. A category may end up empty —
   but only with a written reason in `baseline.md`, never by being skipped.
4. **Glossary** → `glossary.md`. Capture the domain terms as they come up in the interview.
   Fix one spelling per term; the code will use exactly that.
5. **Constraints and risks** → `constraints.md`, `risks.md` for anything that is fixed from
   outside or could derail the project.
6. **Fill `baseline.md`**: target artefact, and per category either the requirement
   wikilinks or the justification for it not applying.
7. **Propose the gate**, never open it. Summarise what is covered and what you justified as
   not applicable, then ask the user to set `baseline_status: vereinbart`.

## 3. Stage mode — one development stage at a time

Only after the gate is open.

1. Ask what the **next stage** should deliver. One stage, not a roadmap.
2. Elicit only the requirements that stage needs. **Do not stockpile.** A requirement for a
   stage nobody has committed to is speculation, and speculation ages badly.
3. Write them with `ebene: detail` and `stufe: <stage name>`.
4. Check each against the framework: a detail requirement that contradicts a framework
   requirement is a conflict — surface it, do not resolve it silently.

## 4. Writing a requirement

From `knowledge/90-meta/templates/requirement.md`, into
`knowledge/05-requirements/REQ-XXXX <title>.md`. Next free four-digit ID.

Required, and none of it is optional:

- **Statement** — one sentence, testable. "Das System muss …"
- **Rationale** — why. No rationale, no requirement.
- **Acceptance** — a threshold, a scenario, an observable behaviour.
- `quelle` — which stakeholder said so.
- `nachweis` — `test`, `messung`, `review` or `demo`.
- `status: entwurf` until the user agrees it. You do not agree requirements on your own.

### Push back on unverifiable wording

When the user says something unmeasurable, do not write it down as given. Offer a
measurable reformulation and let them correct you:

> „Benutzerfreundlich" kann ich nicht prüfen. Wäre „ein geübter Nutzer schließt X in unter
> 30 Sekunden ab" richtig, oder meinst du etwas anderes?

This is the single most valuable thing this skill does. An unmeasurable requirement
produces an unwritable test.

## 5. Link it up

- Requirement → `related` to `[[Rahmen und Startgate]]`, plus the framework requirement it
  refines, if any
- `baseline.md` → wikilink to every framework requirement, in its category section
- Both directions, in the same edit

## 6. Report

State plainly: how many requirements written, which categories are covered, which are
justified as not applicable, and **what is still open**. If the framework is incomplete,
say so — never imply the gate could open.

## Never

- Invent a requirement the user did not state, to fill a category.
- Set `baseline_status: vereinbart` yourself.
- Mark a requirement `vereinbart` without the user agreeing to that exact wording.
- Elicit requirements for stages beyond the next one.
- Accept an unverifiable statement without offering a measurable alternative.
