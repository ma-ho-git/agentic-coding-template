---
id: T-0003
title: Wissensdatenbank aufsetzen
type: task
implements: []
infrastruktur: Template-Grundgerüst, entstanden vor Einführung der Anforderungspflicht (ADR-0005)
status: done
priority: hoch
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta, stack/obsidian]
related: ["[[Konventionen der Wissensdatenbank]]", "[[ADR-0003 Kanban-Board mit Wikilink-Karten]]"]
---

# T-0003 Wissensdatenbank aufsetzen

## Ziel

Ein Obsidian-kompatibler Vault, der von Agenten geführt und aktuell gehalten wird und
gleichzeitig für Menschen lesbar bleibt.

## Akzeptanzkriterien

- [x] Ordnerstruktur nach Themen (`10-pm`, `20-knowledge`, `30-troubleshooting`, `90-meta`)
- [x] Konventionen für Frontmatter, Tags und Verlinkung dokumentiert
- [x] Templates für Task, Wissen, Troubleshooting und ADR
- [x] Kanban-Board im Format des obsidian-kanban-Plugins
- [x] Vault bereits mit dem Wissen aus diesem Projekt gefüllt
- [x] Alle Notizen von `00-index.md` aus erreichbar, keine Waisen
- [x] Deprecation-Workflow beschrieben und mit `review_after` verankert

## Kontext

- [[Konventionen der Wissensdatenbank]]
- [[ADR-0003 Kanban-Board mit Wikilink-Karten]]

## Agent

`claude-code` — viele Dateien im Repo anlegen und verlinken.

## Abhängigkeiten

- [[T-0001 Agentenregeln und Repo-Grundgerüst]]

## Notizen

- Board-Karten sind reine Wikilinks, Details liegen in den Task-Dateien — reduziert
  Merge-Konflikte bei paralleler Arbeit auf eine Zeile
