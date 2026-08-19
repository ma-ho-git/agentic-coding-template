---
description: Run the knowledge base maintenance pass - find notes past their review date, verify them against reality, mark outdated knowledge as deprecated with a reason, and repair broken links and orphans. Use when notes are past review_after, after a dependency upgrade or API migration, or on a regular cadence.
allowed-tools: Read, Glob, Grep, Edit, Write, WebSearch, WebFetch
---

# Knowledge base review

Filling the vault is easy. Keeping it true is the work. A wrong note is worse than a missing one.

## 1. Build the worklist

- Notes with `review_after` in the past and `status: active`.
- Notes tagged with anything that changed recently (upgraded dependency, migrated API,
  refactored area).
- Notes not reachable from `knowledge/00-index.md`.
- Notes with no outgoing `[[Wikilink]]`.
- Broken wikilinks anywhere in the vault.

## 2. Verify each note

Check the claim against reality — the code, the current docs, the installed versions.
Then choose one:

**Still true** → set `updated` and a new `review_after`. One line, done.

**Partly wrong** → fix the wrong part, set `updated`, and add a line under the change:
`> Korrigiert am <Datum>: <was war falsch>`

**Outdated** → deprecate. Never delete:

```yaml
status: deprecated
deprecated_on: 2026-11-02
deprecated_reason: API v1 abgeschaltet; v2 nutzt anderes Auth-Modell
superseded_by: "[[Auth mit API v2]]"
```

Add `#status/deprecated` to `tags` and one line at the top of the body saying what replaced it.
If a successor note is needed and does not exist, write it — deprecating without a successor
leaves a hole.

**Unverifiable** → say so in the note (`> Nicht verifizierbar am <Datum>: <warum>`),
set a short `review_after`, and leave it active. Do not guess.

## 3. Repair the graph

- Orphans get linked from the nearest topic note and from `00-index.md`.
- Broken links get repaired or removed, and the removal noted.
- Duplicate notes on one topic get merged; the loser becomes `deprecated` with
  `superseded_by` pointing at the survivor.
- Tags outside the namespaces in `conventions.md` get corrected.

## 4. Report

Counts: reviewed, confirmed, corrected, deprecated, unverifiable, links repaired.
Then the one thing that matters: which area of the vault is drifting fastest, and why.
