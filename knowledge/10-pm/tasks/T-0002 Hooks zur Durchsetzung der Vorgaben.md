---
id: T-0002
title: Hooks zur Durchsetzung der Vorgaben
type: task
status: done
priority: hoch
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta, stack/claude-code]
related: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]", "[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]"]
---

# T-0002 Hooks zur Durchsetzung der Vorgaben

## Ziel

Maschinell prüfbare Vorgaben werden deterministisch geprüft, nicht dem Ermessen des Agenten
überlassen.

## Akzeptanzkriterien

- [x] Geheimnisse in Schreibvorgängen werden blockiert (`check_secrets.py`)
- [x] Fehlender `@contract`-Header in Quelldateien wird blockiert (`check_contract.py`)
- [x] Veraltetes `updated:`-Datum erzeugt einen Hinweis, keine Blockade
- [x] Funktionslänge, Parameterzahl, Verschachtelung und Namenslänge erzeugen Hinweise
      (`check_quality.py`)
- [x] Zerstörerische Git- und Shell-Kommandos werden vor Ausführung abgelehnt (`git_guard.py`)
- [x] Sitzungsstart zeigt Board-Stand, Bootstrap-Status und überfällige Notizen
      (`session_brief.py`)
- [x] Alle Hooks gegen Positiv- und Negativbeispiele getestet
- [x] Schwellenwerte in `.claude/hooks/config.json` konfigurierbar

## Kontext

- [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]
- [[Konfigurationsebenen von Claude Code]]

## Agent

`claude-code` — Skripte schreiben und ausführen.

## Abhängigkeiten

- [[T-0001 Agentenregeln und Repo-Grundgerüst]]

## Notizen

- Blockierend: Geheimnisse, fehlender Contract-Header, gefährliche Kommandos
- Nur Hinweis: Größen- und Namensgrenzen, veraltetes Contract-Datum
- Aufteilung nach Absprache mit dem Nutzer ("gemischt")
- Python-Prüfung nutzt `ast` und ist exakt; andere Sprachen heuristisch per Regex
