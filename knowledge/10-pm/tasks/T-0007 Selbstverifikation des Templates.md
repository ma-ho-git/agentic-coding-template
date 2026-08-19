---
id: T-0007
title: Selbstverifikation des Templates
type: task
status: doing
priority: hoch
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started: 2026-08-19
finished:
tags: [topic/meta]
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0003 Wissensdatenbank aufsetzen]]"]
---

# T-0007 Selbstverifikation des Templates

## Ziel

Das Template hält seine eigenen Vorgaben ein, nachweislich und nicht nur behauptet.

## Akzeptanzkriterien

- [ ] Board-Datei in Obsidian mit installiertem Kanban-Plugin geöffnet und korrekt gerendert
- [ ] Alle Hooks gegen Positiv- und Negativfälle geprüft, Ergebnisse protokolliert
- [x] Kein Wikilink im Vault zeigt ins Leere
- [x] Keine Waisen-Notiz: alles von `00-index.md` aus erreichbar
- [x] `CLAUDE.md` unter 200 Zeilen, immer geladene Regeln zusammen unter 300 Zeilen
- [ ] Trockenlauf von `/bootstrap` in einem frischen Klon
- [x] Alle Frontmatter-Pflichtfelder in jeder Notiz vorhanden

## Kontext

- [[T-0002 Hooks zur Durchsetzung der Vorgaben]]
- [[T-0003 Wissensdatenbank aufsetzen]]

## Agent

`claude-code` — Skripte ausführen, Dateien prüfen. Das Rendern in Obsidian kann nur
der Mensch bestätigen.

## Abhängigkeiten

- [[T-0005 Cowork-Onboarding-Paket]]
- [[T-0006 README und Lizenz]]

## Notizen

- Für den Link- und Frontmatter-Check ist ein kleines Prüfskript sinnvoll — dann ist es
  wiederholbar statt einmalig
