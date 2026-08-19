---
id: T-0014
title: Rückverfolgbarkeit maschinell prüfen
type: task
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/requirements, stack/python]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]", "[[T-0010 CI-Workflow für die Regelprüfung]]"]
---

# T-0014 Rückverfolgbarkeit maschinell prüfen

## Ziel

Die Kette Anforderung → Task → Test → Code wird geprüft, nicht behauptet.

## Akzeptanzkriterien

- [ ] `tools/check_traceability.py` prüft und meldet:
      Task ohne `implements:` → Fehler; `implements:` zeigt auf nicht existierende
      Anforderung → Fehler; vereinbarte Anforderung ohne Task → Warnung (noch nicht
      umgesetzt); Anforderung `umgesetzt`, aber Tasks nicht alle `done` → Fehler
- [ ] Rückrichtung geprüft: `tasks:` in der Anforderung und `implements:` im Task stimmen
      überein, einseitige Verweise werden gemeldet
- [ ] Ausnahme für Infrastrukturaufgaben wird erkannt und nicht als Fehler gemeldet
- [ ] Tests zuerst geschrieben, decken jeden Fehlerfall und jeden Positivfall ab
- [ ] `.claude/hooks/check_task.py` blockiert das Schreiben einer Task-Datei ohne gültiges
      `implements:`, mit Positiv- und Negativtests
- [ ] Hook in `.claude/settings.json` verdrahtet, Skript in `.github/workflows/rules.yml`
      eingebunden
- [ ] Volle Suite grün, `ruff` sauber

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[T-0010 CI-Workflow für die Regelprüfung]] — CI existiert bereits, hier nur erweitern

## Agent

`claude-code` — Python, Tests, CI.

## Abhängigkeiten

- [[T-0012 Anforderungsregeln und Vault-Struktur]]

## Notizen

- Aufbau an `tools/check_vault.py` anlehnen: Exit 1 bei Fehlern, Warnungen brechen nicht ab.
- `check_task.py` greift nur auf `knowledge/10-pm/tasks/*.md` — nicht auf Code, siehe
  Entscheidung in [[ADR-0005 Anforderungen als Pflicht vor dem Code]].
