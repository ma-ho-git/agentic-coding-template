---
id: T-0001
title: Agentenregeln und Repo-Grundgerüst
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
tags: [topic/meta, stack/claude-code]
related: ["[[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]]", "[[Konfigurationsebenen von Claude Code]]"]
---

# T-0001 Agentenregeln und Repo-Grundgerüst

## Ziel

Das Template enthält eine schlanke `CLAUDE.md` als Einstiegspunkt und thematisch getrennte
Regeldateien, die die Vorgaben des Projekts für Agenten verbindlich beschreiben.

## Akzeptanzkriterien

- [x] `CLAUDE.md` unter 200 Zeilen, verweist auf alle Regeldateien
- [x] Regeln in `.claude/rules/` nach Thema getrennt
- [x] Code-nahe Regeln über `paths:`-Frontmatter nur bei Quelldateien geladen
- [x] Vorgaben zu TDD, Codequalität, Contract-Kommentar, Sicherheit, Wissensdatenbank
      und Agentenverhalten vollständig abgebildet
- [x] `LICENSE` und `.gitignore` vorhanden

## Kontext

- [[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]]
- [[Konfigurationsebenen von Claude Code]]

## Agent

`claude-code` — Dateien im Repo anlegen, Struktur festlegen.

## Abhängigkeiten

- keine

## Notizen

- Immer geladen: `CLAUDE.md`, `workflow.md`, `knowledge-base.md`, `agent-conduct.md` (~288 Zeilen)
- Pfad-gebunden: `tdd.md`, `code-quality.md`, `contracts.md`, `security.md`
