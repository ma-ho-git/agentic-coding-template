---
id: T-0011
title: matches_any() Pfadabgleich reparieren
type: task
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/agents, stack/python]
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0010 CI-Workflow für die Regelprüfung]]", "[[matches_any() exemption trifft falsche Pfade]]"]
---

# T-0011 matches_any() Pfadabgleich reparieren

## Ziel

`matches_any()` in `.claude/hooks/_common.py` exemptiert nur Dateien, deren **Pfad
tatsächlich** einem der `contract_exempt_globs`-Muster entspricht — nicht jede Datei,
deren Pfad irgendwo zufällig eine passende Zeichenkette enthält.

## Akzeptanzkriterien

- [ ] `matches_any()` behandelt `/` als Pfadgrenze (z. B. via `pathlib.PurePath.match`
      oder eine korrekt segmentierte `fnmatch.translate`-Variante), kein Cross-Segment-Match
- [ ] Regressionstest reproduziert den Fund aus
      [[matches_any() exemption trifft falsche Pfade]] (Pfad mit `test_`-Präfix in einem
      Zwischenordner wird NICHT mehr exemptiert)
- [ ] Bestehende, gewollte Exemptions bleiben korrekt: `tests/`-Ordner, `test_*.py`-Dateien,
      `.claude/**`, `node_modules/**` usw. — alle bestehenden Hook-Tests bleiben grün
- [ ] `check_contract.py` UND `check_quality.py` (beide Aufrufer von `matches_any()`)
      erneut gegen Positiv-/Negativfälle geprüft

## Kontext

- [[matches_any() exemption trifft falsche Pfade]] — vollständige Fehleranalyse
- Gefunden beim Bau von `tools/ci_check.py` (T-0010)

## Agent

`claude-code`

## Abhängigkeiten

- keine

## Notizen

- Nicht im Rahmen von T-0010 miterledigt: der Fix berührt gemeinsame Logik, die von zwei
  Hooks genutzt wird, und verdient einen eigenen TDD-Zyklus statt einer Nebenbei-Änderung.
