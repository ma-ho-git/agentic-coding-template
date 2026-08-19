---
description: Write a knowledge base note in the project's format - researched knowledge, a troubleshooting entry, or an architecture decision record. Use after research, after solving a problem that took more than one attempt, or after choosing between real alternatives.
argument-hint: [knowledge|troubleshooting|decision] [topic]
allowed-tools: Read, Glob, Grep, Write, Edit
---

# Capture knowledge

German. Telegraphic. Bullets over prose. A future reader skims — write for skimming.

## 1. Check for an existing note

Search `knowledge/` for the topic before creating anything. If a note exists:
extend it, or mark it deprecated and write the successor. Never leave two notes
that contradict each other.

## 2. Choose type and location

| Type | Location | Use when |
| --- | --- | --- |
| `knowledge` | `knowledge/20-knowledge/` | researched or non-obvious facts you will need again |
| `troubleshooting` | `knowledge/30-troubleshooting/` | a problem that cost more than one attempt |
| `decision` | `knowledge/10-pm/decisions/` | a real choice between alternatives |

Template: `knowledge/90-meta/templates/<type>.md`.

## 3. Write it

Frontmatter is mandatory: `title`, `type`, `tags`, `status: active`, `created`, `updated`,
`review_after`, `related`.

`review_after`: 3 months for stack/API facts, 12 months for domain knowledge.

Body order: **Kurz** → **Kernpunkte** → **Details** (only if needed) → **Quellen** (with date).

For troubleshooting notes keep the fixed sections and copy the error message **verbatim**
into `Symptom` — that string is what a future search will match on.

## 4. Wire it in

- At least one `[[Wikilink]]` to an existing note, and a link back from that note.
- Tags from the namespaces in `knowledge/90-meta/conventions.md`.
  A new namespace goes into conventions first.
- Reachable from `knowledge/00-index.md`. Add it there if the topic area is new.
- Link it from the task that produced it.

## 5. Check yourself

- Would this have saved me the last hour if I had found it? If no, it is too thin.
- Is anything here already in the code? Delete it.
- Any full sentences with filler? Cut them to fragments.
