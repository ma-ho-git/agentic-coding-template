---
id: T-0026
title: Verschluckte Ausnahmen sichtbar machen
type: task
implements: ["[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]"]
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/code, topic/meta]
related: ["[[T-0025 Robustheit als Pflicht des Agenten]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0026 Verschluckte Ausnahmen sichtbar machen

## Anforderung

[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]] — der maschinell
prüfbare Teil.

## Ziel

`code-quality.md` verbietet schon heute, eine Ausnahme zu fangen und nichts damit zu tun.
Durchgesetzt wird es von nichts. Ein Hinweis macht die Stelle sichtbar.

## Akzeptanzkriterien

- [ ] `check_quality.py` meldet einen Fang ohne Behandlung — Python und JavaScript/TypeScript
- [ ] Die Meldung trägt `[FLEXIBLE]` und nennt Datei und Zeile
- [ ] Kein Fehlalarm, wenn im Fang erneut geworfen, protokolliert oder ein Ersatzwert mit
      Begründung im Code gesetzt wird
- [ ] Tests je Sprache: positiver Fall, negativer Fall, begründeter Fall
- [ ] Schwellwert beziehungsweise Abschaltung in `.claude/hooks/config.json`

## Kontext

- Klassenzuordnung nach [[ADR-0006 Zwei Klassen von Leitplanken]]: heilbar, also flexibel.
  Wer die Ausnahme bewusst verschluckt, schreibt den Grund in den Code.

## Agent

`claude-code` — Hook, Tests.

## Abhängigkeiten

- [[T-0025 Robustheit als Pflicht des Agenten]] (liefert die Regel, auf die die Meldung zeigt)

## Notizen

- Die Erkennung bleibt textbasiert wie die übrigen Prüfungen. Ein Parser je Sprache wäre
  genauer und deutlich teurer — bei einem Hinweis lohnt das nicht.
