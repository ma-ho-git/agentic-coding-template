---
description: Check the requirement set against Sommerville's five validation checks - validity, consistency, completeness, realism, verifiability - and report whether the start gate may open. Use before agreeing requirements, before opening the gate, and after a batch of new requirements.
allowed-tools: Read, Glob, Grep
---

# Validate requirements

Reports. Does not repair. A requirement is the user's statement, not yours — you may find
the flaw, but the user decides the wording.

Rules: `.claude/rules/requirements.md`.

## 1. Read the set

Everything in `knowledge/05-requirements/`: `baseline.md`, the framework documents, and
every `REQ-XXXX` file with its frontmatter.

## 2. The five checks

Walk all five over the whole set. Name the affected requirement by ID for every finding.

### Validity

Does each requirement actually serve the vision, and does the set together support the
stated need? Look for requirements that describe a **solution** rather than a need —
"muss PostgreSQL verwenden" is usually a constraint or a premature design decision, not a
requirement. Flag it and ask what need it serves.

### Consistency

Contradictions between requirements. The frequent pairs:

- one demands offline capability, another a live external service
- one demands full audit logging, another data minimisation
- a detail requirement contradicts a framework requirement it should refine

Conflicts between quality requirements are **normal**, not defects — performance versus
maintainability, security versus convenience. Name the conflict; the resolution belongs in
an ADR via `/architecture`, not in a silent edit.

### Completeness

- **Scenario coverage.** If `knowledge/05-requirements/szenario.md` exists, walk it section by
  section: is every statement in it either covered by a requirement or knowingly out of
  scope? Name the uncovered passage verbatim — this is the check the machine cannot do, and
  the one most likely to find a real gap, because a scenario is where users mention things
  they never think to repeat.
- Reverse direction too: a requirement citing `[[Szenario]]` whose `## Herkunft` quote is not
  actually in the scenario is a **fabricated derivation**. Report it as the most severe kind
  of finding — it looks agreed and is not.
- Does every category in `baseline.md` have either requirements or a written justification?
- Does every framework requirement have a `quelle`?
- Are error and boundary cases covered, or only the happy path?
- Anything in `vision.md` under success criteria with no requirement behind it?

### Realism

Implementable with the stated constraints (`constraints.md`) and the active stack profile?
Flag requirements that assume capacity, budget, data or access nobody confirmed exists.

### Verifiability

The hard one. For each requirement: **could you write the test?** If the acceptance section
holds no threshold, no scenario and no observable behaviour, it fails this check — no matter
how reasonable it sounds. Quote the offending wording so the user sees exactly what you mean.

## 3. Check gate readiness

Separately from the five checks, report whether `baseline.md` could move to `vereinbart`:

- every category covered or justified
- every framework requirement `vereinbart`, none left `entwurf`
- target artefact described

State the verdict as a recommendation. **Only the user opens the gate.**

### Say what to do, not only what is missing

Assume the reader has never opened a gate before. „Rahmen unvollständig" tells them nothing.
Name the gap, and name the one action that closes it:

```
Noch offen, bevor das Gate aufgehen kann:

  Kategorie Recht    — keine Anforderung, keine Begründung.
                       Zu tun: entweder eine Anforderung ergänzen, oder in baseline.md
                       hinschreiben, warum sie hier nicht greift („reines lokales
                       Werkzeug, keine Weitergabe, keine Regulierung betroffen").

  REQ-0004           — steht auf `entwurf`.
                       Zu tun: Wortlaut lesen und bestätigen, dann auf `vereinbart` setzen.

Alles andere ist beisammen. Am schnellsten geht das mit /req-elicit.
```

When everything is in place, say so just as concretely — which line to change, in which
file, and that the change is the user's to make.

## 4. Report

Group by check, most severe first. Per finding: requirement ID, what is wrong, and a
concrete proposal.

```
Szenario-Abdeckung
  „Der Server antwortet manchmal nicht"  → keine Anforderung. Vorschlag: Kategorie
                                           qualitaet, Verhalten bei Ausfall festlegen.

Prüfbarkeit
  REQ-0004 „schnell genug"  → kein Schwellwert. Vorschlag: p95 unter 200 ms bei 50 Nutzern.

Konsistenz
  REQ-0002 vs REQ-0007      → offline-fähig vs. Live-Abfrage. Zielkonflikt, gehört ins ADR.
```

End with the gate verdict in one sentence. "Keine Funde" is a valid result — say it plainly
rather than manufacturing findings.
