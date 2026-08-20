---
id: T-0010
title: CI-Workflow für die Regelprüfung
type: task
implements: ["[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta, stack/github]
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]"]
---

# T-0010 CI-Workflow für die Regelprüfung

## Ziel

Die Regeln gelten auch für Beiträge, die nicht durch einen Agenten mit Hooks entstanden sind.

## Akzeptanzkriterien

- [x] GitHub-Actions-Workflow prüft Contract-Header, Geheimnisse und Größengrenzen
- [x] Wiederverwendung der Skripte aus `.claude/hooks/`, keine zweite Implementierung
- [x] Prüfergebnis erscheint als Status am Pull Request

## Kontext

- [[T-0002 Hooks zur Durchsetzung der Vorgaben]]
- [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]

## Agent

`claude-code`

## Abhängigkeiten

- [[T-0007 Selbstverifikation des Templates]]

## Notizen

- Die Hook-Skripte müssen dafür einen Datei-Modus bekommen, der ohne stdin-Payload arbeitet
- **2026-08-19, umgesetzt:** `tools/ci_check.py` baut pro Datei das gleiche
  PostToolUse-Event, das die Hooks interaktiv erwarten, und ruft `check_secrets.py` +
  `check_contract.py` (blockierend) sowie `check_quality.py` (Hinweis) als Subprozess auf —
  keine zweite Implementierung der Regeln. `.github/workflows/rules.yml` ermittelt die
  geänderten Dateien per `git diff` gegen den Base-Branch und übergibt sie an das Skript;
  zusätzlich laufen `tools/check_vault.py` und die volle `pytest`-Suite.
- Dabei einen echten, unabhängigen Bug in `.claude/hooks/_common.py#matches_any()`
  gefunden (Cross-Segment-Glob-Match wegen `fnmatch` ohne Pfadgrenzen) — nicht hier
  mitbehoben, siehe [[T-0011 matches_any() Pfadabgleich reparieren]].
- Lokal gegen den realen Diff dieser Branch gegenprobiert (`git diff --name-only
  origin/main...HEAD` → `tools/ci_check.py <dateien>`) — Exit 0, nur die erwarteten
  Namens-Hinweise, keine Blocker.
