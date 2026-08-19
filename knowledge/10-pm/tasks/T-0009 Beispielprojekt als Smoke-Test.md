---
id: T-0009
title: Beispielprojekt als Smoke-Test
type: task
status: backlog
priority: niedrig
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/meta]
related: ["[[T-0007 Selbstverifikation des Templates]]"]
---

# T-0009 Beispielprojekt als Smoke-Test

## Ziel

Ein minimales Beispielprojekt zeigt den vollständigen Zyklus und beweist, dass die Regeln
in der Praxis funktionieren.

## Akzeptanzkriterien

- [ ] Kleines, echtes Feature nach TDD umgesetzt
- [ ] Contract-Kommentare vorhanden und über mindestens zwei Dateien verknüpft
- [ ] Eine Änderung löst nachweislich eine Folgeaufgabe über `/contract-sync` aus
- [ ] Board und Wissensdatenbank am Ende konsistent

## Kontext

- [[T-0007 Selbstverifikation des Templates]]

## Agent

`claude-code`

## Abhängigkeiten

- [[T-0007 Selbstverifikation des Templates]]

## Notizen

- Offene Frage: als eigener Branch oder als `examples/`-Ordner im Template?
  Ein Ordner im Template müsste beim Projektstart gelöscht werden.
