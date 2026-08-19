---
title: Index
type: knowledge
tags: [topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-02-19
related: ["[[Konventionen der Wissensdatenbank]]"]
---

# Wissensdatenbank — Index

> **Projekt:** Agentic Coding Template
> **Zweck:** Vorlage für strukturiertes Vibe-Coding mit Claude Code und Claude Cowork.
>
> *Beim Start eines eigenen Projekts: diese beiden Zeilen ersetzen.*

Einstiegspunkt des Vaults. Jede Notiz ist von hier aus erreichbar — direkt oder über eine
Themennotiz. Waisen sind ein Fehler und gehören repariert.

## Projektmanagement

- [[board|Kanban-Board]] — aktueller Stand aller Aufgaben
- Aufgaben: `10-pm/tasks/` — eine Datei je Task, Wahrheit ist das `status`-Feld
- Fortschritt: [[2026-08|Fortschritt 2026-08]]

### Entscheidungen (ADR)

- [[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]]
- [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]
- [[ADR-0003 Kanban-Board mit Wikilink-Karten]]
- [[ADR-0004 Cowork über ein leichtes Paket anbinden]]

## Projektwissen

### Agenten und Werkzeuge

- [[Konfigurationsebenen von Claude Code]] — welche Ebene lädt wann, und was das kostet
- [[Cowork liest die Repo-Konfiguration nicht]] — die zentrale Einschränkung für das Routing

### Wissensdatenbank und Format

- [[Konventionen der Wissensdatenbank]] — Ablage, Frontmatter, Tags, Verlinkung
- [[Obsidian-Kanban Dateiformat]] — verifiziertes Board-Format und Wartungslage

### Code und Dokumentation

- [[Dokumentationsstandards je Sprache]] — Vorauswahl je Sprache, samt ihrer Belastbarkeit

## Troubleshooting

- [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]
- [[SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest]]

## Meta

- [[Konventionen der Wissensdatenbank]] — verbindlich für alle Notizen
- [[Umgebungs-Manifest]] — externe Annahmen des Templates mit Prüfdatum
- [[Register der Subagenten-Entscheidungen]] — Kosten-/Nutzenprüfungen mit Ergebnis
- Templates: `90-meta/templates/`

## Tag-Übersicht

`topic/meta` · `topic/agents` · `stack/claude-code` · `stack/cowork` · `stack/obsidian`
· `stack/github` · `stack/python` · `stack/typescript`

Neue Namespaces zuerst in [[Konventionen der Wissensdatenbank]] eintragen.
