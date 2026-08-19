---
id: T-0014
title: Rückverfolgbarkeit maschinell prüfen
type: task
implements: []
infrastruktur: Aufbau der Anforderungsebene selbst - kann sich nicht auf eine Anforderung stützen, die es noch nicht gibt
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/requirements, stack/python]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]", "[[T-0010 CI-Workflow für die Regelprüfung]]"]
---

# T-0014 Rückverfolgbarkeit maschinell prüfen

## Ziel

Die Kette Anforderung → Task → Test → Code wird geprüft, nicht behauptet.

## Akzeptanzkriterien

- [x] `tools/check_traceability.py` prüft und meldet:
      Task ohne `implements:` → Fehler; `implements:` zeigt auf nicht existierende
      Anforderung → Fehler; vereinbarte Anforderung ohne Task → Warnung (noch nicht
      umgesetzt); Anforderung `umgesetzt`, aber Tasks nicht alle `done` → Fehler
- [x] Rückrichtung geprüft: `tasks:` in der Anforderung und `implements:` im Task stimmen
      überein, einseitige Verweise werden gemeldet
- [x] Ausnahme für Infrastrukturaufgaben wird erkannt und nicht als Fehler gemeldet
- [x] Tests zuerst geschrieben, decken jeden Fehlerfall und jeden Positivfall ab
- [x] `.claude/hooks/check_task.py` blockiert das Schreiben einer Task-Datei ohne gültiges
      `implements:`, mit Positiv- und Negativtests
- [x] Hook in `.claude/settings.json` verdrahtet, Skript in `.github/workflows/rules.yml`
      eingebunden
- [x] Volle Suite grün, `ruff` sauber

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
- **2026-08-19 umgesetzt.** 21 neue Tests (15 Traceability, 6 Hook), TDD-Zyklus je Teil
  mit rotem Vorlauf. Volle Suite 59/59.
- Alle 17 bestehenden Tasks verletzten die neue Regel — eine CI einzubauen, die sofort rot
  ist, wäre keine fertige Aufgabe. Deshalb rückwirkend als `infrastruktur:` markiert, mit
  zwei ehrlich unterschiedenen Begründungen: T-0001–T-0011 als Template-Grundgerüst vor
  Einführung der Pflicht, T-0012–T-0017 als Aufbau der Anforderungsebene selbst.
  **Vorläufig** — [[T-0017 Anforderungskette am Beispiel nachweisen]] ersetzt sie durch
  echte Anforderungsbezüge, wo es welche gibt.
- Eigener Fehler beim Markieren: erster Durchlauf prüfte `implements:` im ganzen Dateitext
  statt nur im Frontmatter und übersprang deshalb drei Tasks, die das Wort in ihren
  Akzeptanzkriterien führen. Auf Frontmatter eingegrenzt.
- Der Quality-Hook monierte `check_backlinks()` mit Tiefe 4 → Paarvergleich in
  `link_mismatch()` ausgelagert.
- **Bekannte Lücke:** `check_task.py` hängt an `PostToolUse(Write|Edit)`. Wer eine
  Task-Datei über Bash schreibt, umgeht ihn. Deshalb prüft `check_traceability.py`
  dasselbe noch einmal in der CI — die Bash-Lücke ist damit gedeckt, aber erst beim PR.
