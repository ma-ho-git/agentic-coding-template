---
description: Pick the next task to work on, check it is actually ready, recommend whether Claude Code or Cowork should do it, and claim it. Use at the start of a work session or after finishing a task.
allowed-tools: Read, Glob, Grep, Edit
---

# Next task

## 1. Read the board

`knowledge/10-pm/board.md`. Work down this order:

1. **Review** — anything sitting in Review blocks the flow. Clear it first.
2. **Doing** with no owner — an abandoned task. Reclaim or move it back to Ready.
3. **Ready** — highest `priority`, then oldest `created`, then unblocked dependencies.

Never start something from Backlog while Ready has cards.

## 2. Check readiness

Open the task file. It is only ready when:

- acceptance criteria are present and testable
- all `Abhängigkeiten` tasks are Done
- the goal is understandable without asking the user

If not, fix the task file first (or move it back to Backlog and say why), then pick again.

## 3. Recommend the agent

Compare the task's `agent` field against the routing table in `CLAUDE.md` §6 and against
what the task actually needs. If the current agent is the wrong one, say so plainly:

> Diese Aufgabe passt besser zu <agent>, weil <Grund>. Ich kann sie hier trotzdem angehen,
> empfehle aber den Wechsel.

Do not silently do work with the wrong tool.

## 4. Claim it

1. Task file: `status: doing`, `owner: <agent id>`, `started: <today>`.
2. Board: move that one card line to the `Doing` lane. One line, nothing else.

## 5. Say what happens next

Restate the goal in one sentence, name the first test you will write, and list anything
you need from the user. Then start with the failing test.
