# Knowledge Base

The vault lives in `knowledge/`. It is Obsidian-compatible and written in **German**.
It is written for two readers at once: a human skimming, and an agent searching.
That means: topic-sorted lists of short, telegraphic sections — not flowing prose.

## What must be written down

Write a note when any of these happen. This is an obligation, not a suggestion.

| Trigger | Goes to |
| --- | --- |
| You researched something outside the repo and used the answer | `20-knowledge/` |
| You decided between real alternatives | `10-pm/decisions/` (ADR) |
| A problem cost more than one attempt to solve | `30-troubleshooting/` |
| The same problem appeared a second time | `30-troubleshooting/` — and raise its priority |
| You learned a non-obvious fact about the stack, API, or domain | `20-knowledge/` |
| You checked whether a subagent was worth it | `90-meta/subagent-decisions.md` |

Do not write a note for: things the code already says, one-line facts available in official
docs you did not have to dig for, or session narration.

## Note format

Every note starts with frontmatter:

```yaml
---
title: Kurzer, suchbarer Titel
type: knowledge | troubleshooting | decision | task | progress
tags: [topic/auth, stack/python]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[Andere Notiz]]"]
---
```

Body structure, in this order:

1. **Kurz** — two or three lines: what this is, when you need it.
2. **Kernpunkte** — bullets. Telegraphic. One fact per bullet.
3. **Details / Ablauf** — only if a bullet is not enough.
4. **Quellen** — links, with retrieval date.

Templates: `knowledge/90-meta/templates/`.

## Troubleshooting notes

The most valuable notes in the vault. Structure is fixed:

- **Symptom** — the exact error message or observed behaviour. Copy it verbatim; this is
  what a future search will match on.
- **Kontext** — versions, OS, stack, what was being attempted.
- **Ursache** — the actual cause, not the first guess.
- **Lösung** — the steps that worked, copy-pasteable.
- **Sackgassen** — what did not work, so nobody repeats it.
- **Vorbeugung** — how to avoid hitting this again.

## Linking and tagging

- Link with `[[Wikilinks]]`. Every note links to at least one other note. Orphans are a bug.
- `knowledge/00-index.md` is the hub — every topic area is reachable from it.
- Tags are namespaced and lowercase:
  `topic/<domain>`, `stack/<tech>`, `type/<kind>`, `status/<state>`.
- Prefer three precise tags over eight vague ones.
- New tag namespaces get added to `knowledge/90-meta/conventions.md`, not invented ad hoc.

## Keeping it current — deprecation

The vault must be maintained, not just filled.

- Never delete outdated knowledge. Mark it:

  ```yaml
  status: deprecated
  deprecated_on: 2026-11-02
  deprecated_reason: API v1 abgeschaltet; v2 hat anderes Auth-Modell
  superseded_by: "[[Auth mit API v2]]"
  ```

  Add `#status/deprecated` to the tags and a one-line note at the top of the body.
- Every note carries `review_after`. Default: 3 months for stack/API knowledge,
  12 months for domain knowledge.
- Run `/kb-review` when notes are past `review_after`, or after any dependency upgrade,
  API migration, or architecture change.
- When you find a note that contradicts reality, fixing it is part of the current task,
  not a separate favour.

## Skills

`/kb-capture` writes a note correctly. `/kb-review` runs the deprecation pass.
Use them — they exist so the format stays consistent across agents.
