---
id: T-0004
title: Stack-Profile und Doku-Schema
type: task
status: done
priority: hoch
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta, stack/python, stack/typescript]
related: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]", "[[Dokumentationsstandards je Sprache]]"]
---

# T-0004 Stack-Profile und Doku-Schema

## Ziel

Das Template bleibt sprachagnostisch, liefert aber austauschbare Profile mit konkreten
Kommandos und dem jeweils verbreitetsten Dokumentationsstandard.

## Akzeptanzkriterien

- [x] Profil-Vorlage mit allen Pflichtfeldern
- [x] Profil für Python (pytest, ruff, mypy, Google-Style-Docstrings)
- [x] Profil für TypeScript (vitest, eslint, tsc, TSDoc)
- [x] Jedes Profil zeigt den `@contract`-Block in der Kommentarsyntax der Sprache
- [x] `stacks/active.md` wird beim Bootstrap erzeugt und von `/task-done` gelesen

## Kontext

- [[Dokumentationsstandards je Sprache]]

## Agent

`claude-code` — Dateien anlegen, Kommandos verifizieren.

## Abhängigkeiten

- [[T-0001 Agentenregeln und Repo-Grundgerüst]]

## Notizen

- Versionen und Kommandos sind beim Bootstrap gegen die aktuelle Realität zu prüfen
