---
title: ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa
type: decision
tags: [topic/meta, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-02-19
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[Konfigurationsebenen von Claude Code]]"]
---

# ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa

## Status

angenommen

## Kontext

- Anthropic dokumentiert ausdrücklich: Anweisungen in `CLAUDE.md` beeinflussen das Verhalten,
  erzwingen es nicht
- Zentrale Projektvorgaben sind maschinell prüfbar: Funktionslänge, Parameterzahl,
  Namenslänge, Vorhandensein des Contract-Kommentars, Geheimnisse, gefährliche Kommandos
- Ohne Durchsetzung bleiben genau die Vorgaben optional, die den Kern des Templates ausmachen

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Nur Regeltext | kein Aufwand, keine Reibung | wird statistisch befolgt, nicht sicher |
| Alles blockierend | maximale Verbindlichkeit | Fehlalarme blockieren echte Arbeit |
| Gemischt | Sicherheitskritisches hart, Stil weich | zwei Kategorien zu erklären |

## Entscheidung

Gemischt, nach Absprache mit dem Nutzer.

**Blockierend** (Exit 2 bzw. `permissionDecision: deny`):
- mögliche Geheimnisse in einem Schreibvorgang
- fehlender oder unvollständiger `@contract`-Header in einer Quelldatei
- zerstörerische Git- und Shell-Kommandos

**Nur Hinweis** (`additionalContext`):
- Funktionslänge, Parameterzahl, Verschachtelungstiefe, Namenslänge, Dateilänge
- veraltetes `updated:`-Datum im Contract-Block

## Konsequenzen

- Die Kernvorgaben gelten real, nicht nur auf dem Papier
- Fehlalarme sind möglich; Schwellenwerte liegen deshalb in `.claude/hooks/config.json`
- Hooks laufen nur in Claude Code — Cowork bleibt ungeschützt, siehe [[ADR-0004 Cowork über ein leichtes Paket anbinden]]
- Es braucht zusätzlich CI, damit auch Beiträge ohne Agenten geprüft werden ([[T-0010 CI-Workflow für die Regelprüfung]])

## Revidieren wenn

- Fehlalarme die Arbeit spürbar behindern — dann Schwellen lockern, nicht Hooks abschalten
- Cowork Repo-Hooks unterstützt
