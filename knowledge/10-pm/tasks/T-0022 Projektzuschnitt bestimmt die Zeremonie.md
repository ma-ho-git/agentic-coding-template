---
id: T-0022
title: Projektzuschnitt bestimmt die Zeremonie
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/agents]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]]"]
---

# T-0022 Projektzuschnitt bestimmt die Zeremonie

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — der Teil, der die Zeremonie an die Projektgröße anpasst.

## Ziel

Ein Wegwerfskript kostet nicht dieselbe Zeremonie wie ein Produkt.

## Akzeptanzkriterien

- [x] `/bootstrap` klärt den Zuschnitt: Skript, Werkzeug oder Produkt
- [x] Der Zuschnitt ist im Repository hinterlegt und für Skills und Hooks lesbar
- [x] Ein kleiner Zuschnitt reduziert Pflichten nachvollziehbar — mit **protokollierter
      Begründung**, nicht durch stilles Abschalten
- [x] Starre Leitplanken bleiben in **jedem** Zuschnitt aktiv; nur flexible und
      Dokumentationspflichten skalieren
- [x] README erklärt die Zuschnitte in einer Tabelle

## Kontext

- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[Spec-Driven-Development - was andere Projekte machen]]
- [[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]] — Entscheidung dieser Aufgabe

## Ergebnis

- `project_scope` in `.claude/hooks/config.json`, drei Werte, Vorgabe `produkt`.
  Unbekannter oder fehlender Wert fällt auf `produkt` zurück — der Rückfall kostet
  Schreibarbeit, nie Sicherheit.
- `session_brief.py` nennt den Zuschnitt in jeder Sitzung, zusammen mit dem Satz, dass
  starre Leitplanken davon unberührt bleiben. Ein stiller Wert wäre das Schlupfloch selbst.
- `/bootstrap` Schritt 2a fragt ihn und schreibt **beides**: den Wert in die Konfiguration,
  die Begründung nach `knowledge/05-requirements/baseline.md`.
- `/req-elicit` liest ihn und passt die Erhebungstiefe an — nie die Fragenliste.
- `.claude/rules/workflow.md` beschreibt die drei Zuschnitte, `.claude/rules/guardrails.md`
  hält fest, dass kein Zuschnitt eine starre Leitplanke bewegt.
- Nebenbefund, gleich behoben: `baseline.md` verlinkte REQ-0019 und REQ-0020 nicht und
  sprach noch von 18 Anforderungen.

Tests: `tests/hooks/test_project_scope.py`, drei Fälle (gesetzter Zuschnitt, Vorgabe,
unbekannter Wert). Gesamtsuite 78 grün, `check_vault.py` und `check_traceability.py`
ohne Befund.

## Agent

`claude-code` — Skill, Konfiguration, Dokumentation.

## Abhängigkeiten

- [[T-0019 Leitplanken benennen und klassifizieren]]

## Notizen

- Wichtige Grenze: Proportionalität darf nie eine starre Leitplanke abschalten.
  Sonst wird der Zuschnitt zum Schlupfloch — genau das Risiko, das im Register unter
  „Regeln werden formal erfüllt, aber sinnentleert" steht.
- Keines der Fremdprojekte kennt Proportionalität; hier gibt es keine Vorlage zum Abschauen.
