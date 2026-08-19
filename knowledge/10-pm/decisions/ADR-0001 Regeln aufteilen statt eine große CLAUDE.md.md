---
title: ADR-0001 Regeln aufteilen statt eine große CLAUDE.md
type: decision
tags: [topic/meta, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-02-19
related: ["[[Konfigurationsebenen von Claude Code]]", "[[T-0001 Agentenregeln und Repo-Grundgerüst]]"]
---

# ADR-0001 Regeln aufteilen statt eine große CLAUDE.md

## Status

angenommen

## Kontext

- Die Projektvorgaben ergeben ausformuliert deutlich über 600 Zeilen
- Anthropic empfiehlt unter 200 Zeilen je `CLAUDE.md`; längere Dateien senken messbar die Befolgung
- `CLAUDE.md` wird in **jeder** Session vollständig geladen und kostet dauerhaft Kontext

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Alles in `CLAUDE.md` | ein Ort, nichts zu suchen | über Budget, schlechtere Befolgung, teuer |
| `CLAUDE.md` + `.claude/rules/` | thematisch trennbar, pfad-gebunden ladbar | mehrere Dateien |
| Alles in Skills | lädt nur bei Bedarf | Kernregeln wären nicht präsent, wenn niemand sie aufruft |

## Entscheidung

Dreiteilung nach Ladeverhalten:

- **`CLAUDE.md`** (94 Zeilen) — Einstieg, Nicht-Verhandelbares, Verweise
- **immer geladene Regeln** — `workflow.md`, `knowledge-base.md`, `agent-conduct.md`
- **pfad-gebundene Regeln** — `tdd.md`, `code-quality.md`, `contracts.md`, `security.md`
  über `paths:`-Frontmatter, laden nur bei Quelldateien
- **Skills** — Abläufe, laden nur bei Aufruf

## Konsequenzen

- Dauerlast rund 288 statt über 600 Zeilen
- Wer nur an der Wissensdatenbank arbeitet, bekommt keine Code-Regeln in den Kontext
- Die Glob-Liste in `paths:` muss gepflegt werden, wenn neue Dateiendungen dazukommen
- Regeln stehen an mehreren Orten — Widersprüche müssen aktiv vermieden werden

## Revidieren wenn

- Claude Code das Kontextbudget für Instruktionsdateien deutlich anhebt
- Sich zeigt, dass pfad-gebundene Regeln zu spät oder gar nicht laden
