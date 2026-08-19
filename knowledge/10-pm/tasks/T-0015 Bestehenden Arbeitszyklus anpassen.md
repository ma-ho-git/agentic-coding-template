---
id: T-0015
title: Bestehenden Arbeitszyklus anpassen
type: task
implements: []
infrastruktur: Aufbau der Anforderungsebene selbst - kann sich nicht auf eine Anforderung stützen, die es noch nicht gibt
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/requirements, topic/agents]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]"]
---

# T-0015 Bestehenden Arbeitszyklus anpassen

## Ziel

Der bestehende Zyklus kennt Anforderungen — an jeder Stelle, an der er sie braucht.

## Akzeptanzkriterien

- [ ] `/task-new` verlangt `implements:` mit mindestens einem Anforderungs-Wikilink und
      bietet den Ausnahmeweg für Infrastrukturaufgaben mit Begründung an
- [ ] `/task-next` prüft in der Bereitschaftsprüfung, dass die verlinkte Anforderung
      `vereinbart` ist — Tasks auf Anforderungen im Entwurf werden nicht gestartet
- [ ] `/task-done` prüft die Abnahme der Anforderung, setzt deren Status auf `umgesetzt`,
      wenn alle zugehörigen Tasks fertig sind, und pflegt die Rückverfolgbarkeit
- [ ] `/bootstrap` erhebt bei einem leeren Projekt zuerst Anforderungen (`/req-elicit`),
      bevor Tasks entstehen
- [ ] `.claude/rules/workflow.md`: Lebenszyklus und Definition of Done um die
      Anforderungspunkte erweitert
- [ ] `knowledge/90-meta/templates/task.md` hat das Feld `implements:` und den Abschnitt
      für den Anforderungsbezug
- [ ] `.claude/hooks/session_brief.py` meldet den Anforderungsstand und weist auf
      `/req-elicit` hin, wenn keine vereinbarte Anforderung existiert — mit Tests

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[T-0012 Anforderungsregeln und Vault-Struktur]]

## Agent

`claude-code` — Skills, Regeln, Hook.

## Abhängigkeiten

- [[T-0012 Anforderungsregeln und Vault-Struktur]]
- [[T-0014 Rückverfolgbarkeit maschinell prüfen]]

## Notizen

- Heikelster Teil: die bestehenden Skills sind erprobt. Änderungen minimal halten,
  nichts umschreiben, was nicht mit Anforderungen zu tun hat.
- `session_brief.py` hat bereits Tests — die bleiben grün, neue kommen dazu.
