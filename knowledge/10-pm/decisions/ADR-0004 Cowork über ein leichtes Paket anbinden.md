---
title: ADR-0004 Cowork über ein leichtes Paket anbinden
type: decision
tags: [topic/agents, stack/cowork]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[Cowork liest die Repo-Konfiguration nicht]]", "[[T-0005 Cowork-Onboarding-Paket]]"]
---

# ADR-0004 Cowork über ein leichtes Paket anbinden

## Status

angenommen

## Kontext

- Vorgabe: Es ist zu prüfen, welcher Agent für die nächste Aufgabe geeignet ist,
  und dieser ist zu nutzen
- Cowork-Sessions laden nur die im claude.ai-Konto aktivierten Skills, nicht `.claude/skills/`
  aus einem geklonten Repo. Hooks, Regeln und Subagenten aus dem Repo greifen dort ebenfalls nicht.
- Ein reines Repo-Template steuert also Claude Code vollständig und Cowork gar nicht

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Cowork ignorieren | kein Aufwand | Routing-Vorgabe bleibt unerfüllt |
| Leichtes Paket | schnell, verständlich, sofort nutzbar | manueller Einrichtungsschritt je Nutzer |
| Vollwertiges Plugin | ein Bundle für beide Umgebungen | deutlich mehr Bauaufwand und Pflege |

## Entscheidung

Leichtes Paket, nach Absprache mit dem Nutzer:

- `cowork/PROJECT-INSTRUCTIONS.md` zum Einfügen in die Cowork-Projekt-Instructions
- einzelne `.skill`-Pakete zum Hochladen in den claude.ai-Account
- Einrichtungsschritte im `cowork/README.md`

## Konsequenzen

- Cowork kennt die Regeln, aber ohne Durchsetzung — Hooks existieren dort nicht
- Deshalb gehört Codearbeit nach Claude Code, Cowork übernimmt Recherche und Dokumente
- Jeder Nutzer muss die Einrichtung einmal manuell durchführen
- Bei Regeländerungen müssen die Cowork-Artefakte nachgezogen werden — Gefahr des Auseinanderlaufens

## Revidieren wenn

- Cowork Repo-Konfiguration liest — dann wird `cowork/` überflüssig
- Das Template ohnehin als Plugin verteilt werden soll
