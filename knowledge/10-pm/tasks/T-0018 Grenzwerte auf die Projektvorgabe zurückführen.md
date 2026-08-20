---
id: T-0018
title: Grenzwerte auf die Projektvorgabe zurückführen
type: task
implements: ["[[REQ-0007 Grenzen für Funktionsgröße und Benennung]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta, stack/python]
related: ["[[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]]", "[[T-0002 Hooks zur Durchsetzung der Vorgaben]]"]
---

# T-0018 Grenzwerte auf die Projektvorgabe zurückführen

## Anforderung

Keine — Korrektur des Regelwerks selbst. Der Nutzer hat beim Audit festgestellt, dass
mehrere durchgesetzte Grenzwerte nicht aus seiner Vorgabe stammen, sondern von früheren
Sitzungen ergänzt wurden, ohne das kenntlich zu machen.

## Ziel

Jede durchgesetzte Grenze ist entweder gefordert oder als Zugabe des Templates erkennbar —
und die Funktionsgrenze misst das, was der Nutzer gemeint hat.

## Akzeptanzkriterien

- [x] `check_quality.py` zählt **Zuweisungen** statt Rumpfzeilen; `config.json` führt
      `max_assignments: 20` statt `max_function_lines`
- [x] Tests zuerst: eine Funktion mit vielen Zeilen aber wenigen Zuweisungen fällt nicht
      mehr auf, eine mit über 20 Zuweisungen schon
- [x] `code-quality.md` weist je Grenze aus, ob sie aus der Projektvorgabe stammt oder vom
      Template ergänzt wurde, mit Begründung bei den Zugaben
- [x] Die nirgends hergeleitete 300-Zeilen-Grenze für immer geladene Regeldateien ist
      als Grenzwert abgeschafft; es bleibt der qualitative Hinweis, dass diese Dateien
      knapp bleiben sollen
- [x] `CLAUDE.md`-Grenze von 200 Zeilen bleibt, aber mit genannter Quelle statt als
      gesetzte Zahl
- [x] Volle Suite grün, `ruff` sauber, bestehende Tests bleiben grün

## Kontext

- [[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]] — nennt „rund 288 Zeilen" als
  Beobachtung, nie als Grenzwert. Die 300 wurden daraus fälschlich abgeleitet.
- [[T-0002 Hooks zur Durchsetzung der Vorgaben]] — hier entstanden die Schwellwerte

## Agent

`claude-code` — Hook-Code, Konfiguration, Regeldatei.

## Abhängigkeiten

- keine

## Notizen

- Entscheidung des Nutzers: Verschachtelungsgrenze bleibt aktiv (gut begründet, hat in
  diesem Projekt zweimal zu besserem Code geführt), Dateilänge bleibt als markierte Zugabe,
  die Regel-Zeilengrenze entfällt.
- Die 300-Zeilen-Grenze für Regeldateien war nie im Code — sie stand nur als
  Akzeptanzkriterium in T-0007 und hat in T-0015 trotzdem eine Inhaltskürzung getrieben.
