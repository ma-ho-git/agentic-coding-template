---
id: T-0011
title: matches_any() Pfadabgleich reparieren
type: task
implements: []
infrastruktur: Template-Grundgerüst, entstanden vor Einführung der Anforderungspflicht (ADR-0005)
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/agents, stack/python]
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0010 CI-Workflow für die Regelprüfung]]", "[[matches_any() exemption trifft falsche Pfade]]"]
---

# T-0011 matches_any() Pfadabgleich reparieren

## Ziel

`matches_any()` in `.claude/hooks/_common.py` exemptiert nur Dateien, deren **Pfad
tatsächlich** einem der `contract_exempt_globs`-Muster entspricht — nicht jede Datei,
deren Pfad irgendwo zufällig eine passende Zeichenkette enthält.

## Akzeptanzkriterien

- [x] `matches_any()` behandelt `/` als Pfadgrenze (z. B. via `pathlib.PurePath.match`
      oder eine korrekt segmentierte `fnmatch.translate`-Variante), kein Cross-Segment-Match
- [x] Regressionstest reproduziert den Fund aus
      [[matches_any() exemption trifft falsche Pfade]] (Pfad mit `test_`-Präfix in einem
      Zwischenordner wird NICHT mehr exemptiert)
- [x] Bestehende, gewollte Exemptions bleiben korrekt: `tests/`-Ordner, `test_*.py`-Dateien,
      `.claude/**`, `node_modules/**` usw. — alle bestehenden Hook-Tests bleiben grün
- [x] `check_contract.py` UND `check_quality.py` (beide Aufrufer von `matches_any()`)
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
- **2026-08-19 umgesetzt.** `fnmatch` in `_common.py` durch eigene, pfadbewusste
  Glob-Übersetzung ersetzt (`glob_regex()` + `next_token()`, Token-Tabelle
  längster-Treffer-zuerst). Details und Regex-Tabelle in
  [[matches_any() exemption trifft falsche Pfade]].
- TDD: `tests/hooks/test_common.py` mit 12 Fällen zuerst geschrieben — 2 rot (der
  dokumentierte Bug), 10 grün (die Exemptions, die weiter greifen müssen). Nach dem Fix
  alle 12 grün, volle Suite 36/36, `ruff` sauber.
- Erster Fix-Entwurf verletzte die eigene Regel (`elif`-Kette = Verschachtelungstiefe 5,
  Grenze 3) und wurde von `check_quality.py` gemeldet → auf die Token-Tabelle umgebaut.
  Das ist genau der in `code-quality.md` genannte „deep chain of if"-Fall.
- Beide Aufrufer end-to-end nachgewiesen: `check_contract.py` blockt jetzt
  `test_run_0/greet.py` korrekt und lässt `tests/unit/helper.py` sowie
  `test_run_0/test_thing.py` weiterhin durch; `check_quality.py` überspringt
  `node_modules/` und `build/`, meldet aber `generated_reports/` — vorher fälschlich
  von `**/generated/**` verschluckt.
