---
name: kb-capture
description: Write a note into the project's Obsidian knowledge base in the required format - researched knowledge, a troubleshooting entry, or an architecture decision record. Use after research, after solving a problem that took more than one attempt, or after choosing between real alternatives.
license: MIT
---

# Capture knowledge

For projects built from the agentic-coding-template. The vault is the `knowledge/` folder of
the project repository. Written in German, telegraphic, bullets over prose.

## 1. Read the conventions first

`knowledge/90-meta/conventions.md` is authoritative — folders, frontmatter fields, tag
namespaces, linking rules. If this skill and that file disagree, that file wins.

## 2. Check for an existing note

Search `knowledge/` for the topic before creating anything. Extend an existing note, or
deprecate it and write the successor. Never leave two notes that contradict each other.

## 3. Choose type and location

| Type | Location | Use when |
| --- | --- | --- |
| `knowledge` | `knowledge/20-knowledge/` | researched or non-obvious facts you will need again |
| `troubleshooting` | `knowledge/30-troubleshooting/` | a problem that cost more than one attempt |
| `decision` | `knowledge/10-pm/decisions/` | a real choice between alternatives |

Use the matching template from `knowledge/90-meta/templates/`.

## 4. Write it

Frontmatter is mandatory: `title`, `type`, `tags`, `status: active`, `created`, `updated`,
`review_after`, `related`. Set `review_after` three months out for stack and API facts,
twelve months for domain knowledge.

Body order: **Kurz** → **Kernpunkte** → **Details** (only if needed) → **Quellen** with
retrieval dates.

In a troubleshooting note, copy the error message **verbatim** into `Symptom`. That exact
string is what a future search will match on.

## 5. Wire it in

- At least one `[[Wikilink]]` out, and a link back from the note you linked to.
- Tags only from the namespaces declared in `conventions.md`.
- Reachable from `knowledge/00-index.md` — add it there if the topic area is new.
- Linked from the task that produced it.

## 6. Check yourself

Would this have saved you the last hour if you had found it? If not, it is too thin.
Anything already visible in the code? Cut it. Full sentences with filler? Cut them to fragments.
