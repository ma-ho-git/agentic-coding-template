---
id: T-0010
title: CI-Workflow für die Regelprüfung
type: task
status: backlog
priority: mittel
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/meta, stack/github]
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]"]
---

# T-0010 CI-Workflow für die Regelprüfung

## Ziel

Die Regeln gelten auch für Beiträge, die nicht durch einen Agenten mit Hooks entstanden sind.

## Akzeptanzkriterien

- [ ] GitHub-Actions-Workflow prüft Contract-Header, Geheimnisse und Größengrenzen
- [ ] Wiederverwendung der Skripte aus `.claude/hooks/`, keine zweite Implementierung
- [ ] Prüfergebnis erscheint als Status am Pull Request

## Kontext

- [[T-0002 Hooks zur Durchsetzung der Vorgaben]]
- [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]

## Agent

`claude-code`

## Abhängigkeiten

- [[T-0007 Selbstverifikation des Templates]]

## Notizen

- Die Hook-Skripte müssen dafür einen Datei-Modus bekommen, der ohne stdin-Payload arbeitet
