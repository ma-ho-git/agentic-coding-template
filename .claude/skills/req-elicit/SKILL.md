---
description: Elicit requirements with the user - the project framework before any code, or the detail requirements for the next development stage. Explains each category before asking, proposes rather than interrogates, and writes vision, stakeholders, glossary and REQ files. Use at project start, when the start gate is still open, or before beginning a new development stage.
argument-hint: [rahmen|stufe] [topic]
allowed-tools: Read, Glob, Grep, Write, Edit
---

# Elicit requirements

This is the one skill that **must ask the human**. Elicitation without a stakeholder is
guessing, and a guessed requirement is worse than none — it looks agreed.

Assume the user has never written a requirement before. Explaining costs an expert one line
they skim; not explaining costs a beginner the whole method.

Rules: `.claude/rules/requirements.md`. Terms the user may not know:
`knowledge/05-requirements/methodenglossar.md` — point at it, do not recite it.

## 1. Determine the mode

Read `knowledge/05-requirements/baseline.md`.

| `baseline_status` | Mode | What you elicit |
| --- | --- | --- |
| `entwurf` | **Framework** | What is being built, plus all six categories. Section 3. |
| `vereinbart` | **Stage** | Detail requirements for the next stage only. Section 4. |

If the argument says otherwise than the gate, follow the gate and say why.

## 2. How to ask — applies throughout

**Explain, then ask.** Never pose a question the user may not understand. For every
category: one sentence on what it covers, one example from a project like theirs, then the
question.

**Propose, do not interrogate.** Offer two or three plausible requirements and let the user
correct them. Rejecting a wrong proposal is far easier than inventing from nothing — and it
surfaces what they actually meant.

> Für ein Kommandozeilenwerkzeug wäre üblich: „läuft ohne Installation als einzelne Datei".
> Trifft das zu, oder ist das bei dir anders?

**„Weiß ich nicht" is a valid answer.** It never produces an invented requirement. Write the
gap into `Offene Fragen` of the affected requirement, or leave the category open in
`baseline.md`, and say plainly that this is now the user's open point. A fabricated
requirement that looks agreed is the worst outcome this skill can produce.

**One question at a time** when the user is unsure. A list of six questions reads like an
exam and gets abandoned.

**Never make the user feel tested.** They are the domain expert; the method is your job.

## 3. Framework mode — before any production code

**Is there a scenario?** Read `knowledge/05-requirements/szenario.md`. If it does not exist,
offer `/szenario` once — describing the project is far easier than answering six categories.
A no is a complete answer and is not asked twice. If it does exist, work from Section 3a
before anything else here.

Ask first what kind of thing is being built — script, tool, service, library, application.
Every example below is then chosen to match.

Read `project_scope` from `.claude/hooks/config.json` (`/bootstrap` sets it; missing means
`produkt`). It sets how deep the answers need to be — never which questions get asked:

| Scope | How deep |
| --- | --- |
| `skript` | ask all six categories; „trifft hier nicht zu, weil …" is a complete answer |
| `werkzeug` | insist on real answers for `funktional`, `technisch`, `sicherheit`, `recht` |
| `produkt` | every category gets an agreed requirement |

Every scope passes through the start gate, and no scope skips a category.
Details: `.claude/rules/workflow.md`.

Then work in this order, writing each answer down before moving on.

1. **Vision** → `vision.md`. Problem, target artefact, success criteria, **non-goals**.
   Push for non-goals; they are the most valuable part and users rarely volunteer them.
2. **Stakeholders** → `stakeholders.md`. Who is affected, who decides when requirements
   conflict. Ask explicitly who was *not* asked.
3. **The six categories** → one `REQ-XXXX` file per requirement, `ebene: rahmen`.

   | Category | One sentence | Example — command line tool |
   | --- | --- | --- |
   | `funktional` | What it must be able to do to be worth building | „Liest eine CSV und schreibt eine bereinigte CSV" |
   | `technisch` | What it must run on and cope with | „Läuft mit Python 3.11 unter Linux, Dateien bis 100 MB" |
   | `organisatorisch` | Who operates it, how it ships, who may do what | „Wird als einzelne Datei weitergegeben, keine Installation" |
   | `sicherheit` | What needs protecting, and from whom | „Verarbeitet Kundendaten, legt nichts auf Platte ab" |
   | `recht` | Regulation, licences, retention, rights to the result | „Eingesetzte Bibliotheken müssen MIT oder Apache sein" |
   | `qualitaet` | How good, how fast, how usable | „10.000 Zeilen in unter 5 Sekunden" |

   **Ask about every category**, even the ones that look irrelevant — that is the point of
   having a list. A category may end up empty, but only with a written reason in
   `baseline.md`, never by being skipped. „Für ein Wegwerfskript brauche ich nichts" is a
   perfectly good reason; write it down as one.

4. **Glossary** → `glossary.md`. Capture domain terms as they come up. Fix one spelling per
   term; the code will use exactly that.
5. **Constraints and risks** → `constraints.md`, `risks.md` for anything fixed from outside
   or likely to derail the project.
6. **Fill `baseline.md`**: target artefact, and per category either the requirement
   wikilinks or the justification for it not applying.
7. **Propose the gate**, never open it. Summarise what is covered, what you justified as not
   applicable, and what is still open — then ask the user to set
   `baseline_status: vereinbart`.

## 3a. Deriving from a scenario — without inventing

This section resolves a real tension. The scenario invites you to derive; the hardest rule in
this skill forbids inventing. Both stay in force, and this is how:

**Propose, quote, confirm — in that order.**

1. **Propose** the requirement you read out of the scenario.
2. **Quote** the passage it came from, verbatim, so the user sees your source:

   > Aus deinem Szenario: „Datei einlesen, Dubletten raus, nach Region sortieren."
   > Daraus würde ich machen: „Das Werkzeug entfernt Dubletten anhand der Kundennummer
   > und sortiert nach Region." Die Kundennummer steht nicht im Szenario — rate ich da
   > richtig, oder ist das Merkmal ein anderes?

3. **Confirm.** The user corrects or agrees. Only then does it go into a `REQ` file, still
   `status: entwurf`.

**Name what you added.** Every derivation adds something the scenario did not say —
a threshold, a mechanism, a boundary. Say which part is the user's and which is yours, in
the same breath. A derivation whose additions stay invisible is an invention with a citation
stapled to it.

**Write both down.** The derived requirement carries `quelle: <Stakeholder> — "[[Szenario]]"`
and a `## Herkunft` section quoting the passage with its section name. Not optional:
`tools/check_traceability.py` reports a scenario that no requirement derives from.

**What the scenario does not answer stays open.** A category the scenario is silent on gets
asked normally — the scenario is a head start, never a substitute for the six categories.
Never fill a gap with something that merely sounds consistent with the scenario.

**Contradictions are findings, not noise.** When the scenario contradicts itself, or a later
statement contradicts it, say so and let the user decide. Do not quietly pick the version
that fits your draft.

## 4. Stage mode — one development stage at a time

Only after the gate is open.

1. Ask what the **next stage** should deliver. One stage, not a roadmap.
2. Elicit only the requirements that stage needs. **Do not stockpile.** A requirement for a
   stage nobody has committed to is speculation, and speculation ages badly.
3. Write them with `ebene: detail` and `stufe: <stage name>`.
4. Check each against the framework: a detail requirement that contradicts a framework
   requirement is a conflict — surface it, do not resolve it silently.

## 5. Writing a requirement

From `knowledge/90-meta/templates/requirement.md`, into
`knowledge/05-requirements/REQ-XXXX <title>.md`. Next free four-digit ID.

Required, none of it optional:

- **Statement** — one sentence, testable. „Das System muss …"
- **Rationale** — why. No rationale, no requirement.
- **Acceptance** — a threshold, a scenario, an observable behaviour.
- `quelle` — which stakeholder said so.
- `nachweis` — `test`, `messung`, `review` or `demo`.
- `status: entwurf` until the user agrees it. You do not agree requirements on your own.

### Push back on unverifiable wording

When the user says something unmeasurable, do not write it down as given. Offer a measurable
reformulation and let them correct you:

> „Benutzerfreundlich" kann ich nicht prüfen — ich wüsste nicht, woran wir später sehen,
> ob es stimmt. Wäre „ein geübter Nutzer schließt X in unter 30 Sekunden ab" richtig, oder
> meinst du etwas anderes?

Explain *why* it matters when the user seems new: an unmeasurable requirement produces an
unwritable test, and then nobody can say whether the software does what was asked. This is
the single most valuable thing this skill does.

## 6. Link it up

- Requirement → `related` to `[[Rahmen und Startgate]]`, plus the framework requirement it
  refines, if any
- `baseline.md` → wikilink to every framework requirement, in its category section
- Both directions, in the same edit

## 7. Report

State plainly: how many requirements written, which categories are covered, which are
justified as not applicable, and **what is still open**. If the framework is incomplete, say
so — never imply the gate could open.

End with the one next step, not a list. A beginner needs to know what to do now.

## Never

- Invent a requirement the user did not state, to fill a category or to unblock yourself.
- Set `baseline_status: vereinbart` yourself.
- Mark a requirement `vereinbart` without the user agreeing to that exact wording.
- Elicit requirements for stages beyond the next one.
- Derive a requirement from the scenario without quoting the passage it came from.
- Present your own addition as if the scenario had said it.
- Accept an unverifiable statement without offering a measurable alternative.
- Use a method term without explaining it or pointing at the glossary.
