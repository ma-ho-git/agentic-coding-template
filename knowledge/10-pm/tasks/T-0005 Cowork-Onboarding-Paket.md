---
id: T-0005
title: Cowork-Onboarding-Paket
type: task
status: done
priority: hoch
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started:
finished: 2026-08-19
tags: [topic/agents, stack/cowork]
related: ["[[Cowork liest die Repo-Konfiguration nicht]]", "[[ADR-0004 Cowork über ein leichtes Paket anbinden]]"]
---

# T-0005 Cowork-Onboarding-Paket

## Ziel

Cowork arbeitet nach denselben Regeln wie Claude Code, obwohl es `.claude/` im Repo nicht liest.

## Akzeptanzkriterien

- [x] `cowork/PROJECT-INSTRUCTIONS.md` — Text zum Einfügen in die Cowork-Projekt-Instructions,
      verweist auf die Regeldateien im freigegebenen Ordner
- [x] `cowork/README.md` — Einrichtungsschritte, in unter fünf Minuten durchführbar
- [x] Mindestens zwei Skills als `.skill`-Paket für den claude.ai-Account
      (Wissenserfassung, Task-Übergabe)
- [x] Die Grenzen sind benannt: Hooks greifen in Cowork nicht

## Kontext

- [[Cowork liest die Repo-Konfiguration nicht]]
- [[ADR-0004 Cowork über ein leichtes Paket anbinden]]

## Agent

`claude-code` — Dateien und Pakete erzeugen.

## Abhängigkeiten

- [[T-0001 Agentenregeln und Repo-Grundgerüst]]

## Notizen

- Alternative wäre ein vollwertiges Plugin; verworfen wegen Aufwand, siehe ADR-0004
