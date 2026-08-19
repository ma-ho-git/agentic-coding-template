# Cowork setup

Cowork does not read this repository's `.claude/` directory. Its rules, hooks, subagents and
skills apply to Claude Code only. This folder closes that gap — manually, in about five minutes.

See `knowledge/20-knowledge/Cowork liest die Repo-Konfiguration nicht.md` for the evidence,
and `knowledge/10-pm/decisions/ADR-0004 …` for why this is a folder of instructions rather
than a plugin.

## Setup

**1. Create a Cowork project for this repository**

Give it the repository folder as its context folder, so Cowork can read the rules and the
knowledge base directly from disk.

**2. Paste the project instructions**

Copy the whole of `cowork/PROJECT-INSTRUCTIONS.md` into the project's *Instructions* field.

**3. Add the skills to your account**

Run `bash cowork/build-skills.sh`. It produces one `.skill` file per skill in `cowork/dist/`.
Upload them in the Desktop app under **Customize → Skills**, or in the skill settings on
claude.ai. Cowork syncs account skills at session start.

**4. Check it works**

Start a Cowork task in the project and ask: *"Welche Aufgabe steht als nächstes an?"*
Cowork should read `knowledge/10-pm/board.md` and answer from it.

## What Cowork can and cannot do here

| | Claude Code | Cowork |
| --- | --- | --- |
| Knows the rules | yes, automatically | yes, via the pasted instructions |
| Hooks enforce them | yes | **no** |
| Runs tests, linters, builds | yes | not reliably |
| Git operations | yes | avoid |
| Research, documents, spreadsheets | possible | this is what it is good at |

**The consequence:** code work belongs in Claude Code, where the checks actually run.
Cowork does research, documents, triage, and knowledge base maintenance.

## Keeping it in sync

`PROJECT-INSTRUCTIONS.md` is a hand-maintained summary of `.claude/rules/`. When the rules
change, update it in the same commit — otherwise the two agents drift apart, which is worse
than Cowork knowing nothing at all.
