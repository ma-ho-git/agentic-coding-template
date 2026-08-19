---
id: T-0006
title: README und Lizenz
type: task
status: done
priority: mittel
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started:
finished: 2026-08-19
tags: [topic/meta]
related: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]"]
---

# T-0006 README und Lizenz

## Ziel

Wer das Repo klont, versteht in unter drei Minuten, was es tut und wie er startet.

## Akzeptanzkriterien

- [x] MIT-Lizenz recherchiert, begründet und als `LICENSE` hinterlegt
- [x] `README.md` auf Deutsch, kurz: Zweck, Voraussetzungen, erste Schritte,
      Aufgaben des Verwenders, Struktur in einer Tabelle
- [x] Hinweis, dass generierter Projektcode nicht unter der Template-Lizenz steht
- [x] Keine Behauptung im README, die im Repo nicht eingelöst ist

## Kontext

- [[T-0001 Agentenregeln und Repo-Grundgerüst]]

## Agent

`claude-code` — Dateien anlegen.

## Abhängigkeiten

- [[T-0005 Cowork-Onboarding-Paket]]

## Notizen

- MIT gewählt: kurz, permissiv, Standard für Templates
