---
description: Before the first line of code, check whether the thing already exists - open source projects, frameworks, libraries - and measure each candidate against the agreed requirements. Offers the search, never forces it, and records the decision either way. Use once the start gate is open and before the first coding task.
allowed-tools: Read, Glob, Grep, WebSearch, WebFetch, Write, Edit
---

# Scan for existing solutions

The cheapest line of code is the one somebody else already wrote and maintains.

An agent writes everything from scratch quite happily, because writing costs it nothing. The
project pays anyway — at the latest when the thing has to be maintained. So this step is
offered, always, at one specific moment.

**The offer is mandatory. Searching is not.** The user decides; you record the decision.

## 1. The moment

After the start gate is open (`baseline_status: vereinbart`), before the first coding task.

Not earlier: without agreed requirements there is nothing to measure a candidate against, and
a scan without a yardstick produces a list of popular projects, not an answer.

Not later: once the home-made version exists it wins, because it exists — not because it is
better. That is a decision made by inertia, and inertia is not an argument.

The decision is recorded either way before the first code task — see Section 6.

## 2. Make the offer

> Bevor wir anfangen zu bauen: Soll ich einmal schauen, ob es so etwas schon fertig gibt?
> Oft gibt es eine Bibliothek, die den Kern schon kann — dann bauen wir nur noch das drumherum,
> was dich von anderen unterscheidet.
>
> Das kostet ein paar Minuten und kann einiges an Arbeit sparen. Es kann aber auch heißen,
> dass nichts passt — das ist ein genauso gutes Ergebnis, dann wissen wir es.

A no is a complete answer. Record it with the reason (Section 6) and move on.

## 3. Search against the requirements, not against the vibe

Derive the search terms from `knowledge/05-requirements/` — the target artefact from
`baseline.md`, the `funktional` requirements, the `technisch` constraints. Search in the
stack's own ecosystem first (its package index), then generally.

What you are looking for is not "a popular project in this area" but **something that already
does what the `muss` requirements say**.

## 4. The hard rule: no candidate without a retrieved source

**Never name a project from memory.** For every candidate, retrieve the actual repository or
package page in this session. A library you remember may be renamed, abandoned, merged, or
may never have existed in the shape you remember it — and a recommendation nobody checked is
worse than no recommendation, because it will be trusted.

If you cannot retrieve it, it is not a candidate. Say that plainly rather than listing it
with a caveat.

## 5. Per candidate, record all five

| Field | Why it decides something |
| --- | --- |
| Source with retrieval date | anything else is hearsay; facts about projects go stale |
| Licence | decides whether it may be used at all — `T-0029`, the register of third-party components |
| Maintenance | last release, last commit, open issue trend, how many maintainers |
| Requirement match | **per REQ-ID**: fulfilled / partly / not |
| Cost of adoption | learning curve, coupling, how hard it is to leave again |

**"Fulfils 80 % of the requirements" says nothing.** Which 20 % is missing is the whole
question. If the gap is the reason the project exists at all, a 90 % match is worth nothing;
if the gap is a report format, a 60 % match may be excellent.

### Judging maintenance honestly

A dead project with a good README is **worse** than no candidate: it looks like a shortcut
and turns into a maintenance burden that is now yours. Look at dates, not stars. One
maintainer, last release two years ago, issues piling up unanswered — say so, and say it
before the licence question, because it decides the same way.

## 6. Write it down — both outcomes

**The findings** → a note in `knowledge/20-knowledge/`, in the format of
`knowledge/90-meta/templates/knowledge.md`: the comparison table, one section per serious
candidate, sources with retrieval dates.

**The decision** → an ADR in `knowledge/10-pm/decisions/`, **also when the decision is
"none of them"**. That is the case most worth recording: the next person to ask "why did we
build this ourselves?" deserves an answer that is not a shrug.

**The status** → `knowledge/05-requirements/fremdloesungen.md`, with `scan_status`:

- `gesucht` — searched, findings and decision linked
- `uebersprungen` — deliberately not searched, **with the user's reason**
- `offen` — not yet decided; the gate stays shut

A skipped scan is a legitimate choice. A skipped scan with no reason is not a choice, it is
an omission wearing the same clothes.

## 7. If a candidate is chosen

- The legal side runs through `T-0029`: licence checked against the project's distribution
  intent, obligations recorded and **fulfilled** in the repository.
- Requirements the candidate already satisfies do not disappear. They stay, and their
  `nachweis` becomes a test against the candidate — you still have to show it does what was
  asked.
- What the candidate does *not* cover is what you build. That is now the project.

## 8. Routing

Retrieval-heavy and self-contained: hand the search to the `researcher` subagent or to
Cowork (`CLAUDE.md` §6). The judgement — which candidate fits which requirement — comes
back here and is not delegated. Record the cost/benefit check in
`knowledge/90-meta/subagent-decisions.md`.

## 9. Report

Short. Per candidate one line: name, licence, maintenance, requirement match. Then your
recommendation with its reason — and the reason has to name requirements, not qualities.

**You recommend, the user decides.** As everywhere else in this method.

## Never

- Name a project you did not retrieve in this session.
- Report a match percentage without saying which requirements are missing.
- Recommend an unmaintained project because it fits technically.
- Hide a candidate you had to reject — the rejection with its reason is a finding.
- Skip the ADR because the answer was "we build it ourselves".
- Decide the adoption yourself.
