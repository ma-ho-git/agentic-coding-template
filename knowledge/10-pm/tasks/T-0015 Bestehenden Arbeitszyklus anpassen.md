---
id: T-0015
title: Bestehenden Arbeitszyklus anpassen
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
tags: [topic/requirements, topic/agents]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]"]
---

# T-0015 Bestehenden Arbeitszyklus anpassen

## Ziel

Der bestehende Zyklus kennt Anforderungen — an jeder Stelle, an der er sie braucht.

## Akzeptanzkriterien

- [x] `/task-new` verlangt `implements:` mit mindestens einem Anforderungs-Wikilink und
      bietet den Ausnahmeweg für Infrastrukturaufgaben mit Begründung an
- [x] `/task-next` prüft in der Bereitschaftsprüfung, dass die verlinkte Anforderung
      `vereinbart` ist — Tasks auf Anforderungen im Entwurf werden nicht gestartet
- [x] `/task-done` prüft die Abnahme der Anforderung, setzt deren Status auf `umgesetzt`,
      wenn alle zugehörigen Tasks fertig sind, und pflegt die Rückverfolgbarkeit
- [x] `/bootstrap` erhebt bei einem leeren Projekt zuerst Anforderungen (`/req-elicit`),
      bevor Tasks entstehen
- [x] `.claude/rules/workflow.md`: Lebenszyklus und Definition of Done um die
      Anforderungspunkte erweitert
- [x] `knowledge/90-meta/templates/task.md` hat das Feld `implements:` und den Abschnitt
      für den Anforderungsbezug (bereits in T-0014 miterledigt)
- [x] `.claude/hooks/session_brief.py` meldet den Anforderungsstand und weist auf
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
- **2026-08-19 umgesetzt.** Alle vier Skills, `workflow.md` und `session_brief.py`
  angepasst. Drei neue Tests, Suite 62/62.
- `/bootstrap` hat jetzt einen eigenen Schritt 3 „Elicit the framework, before any task" —
  vorher wurde direkt das Board geseedet. Das war die eigentliche Lücke: ein Board vor den
  Anforderungen lädt genau zu dem ein, was die Regel verhindern soll.
- `/task-next` bekommt einen Schritt 0: bei geschlossenem Gate wird keine Aufgabe gezogen,
  Infrastrukturaufgaben ausgenommen.
- **Grenze gerissen und repariert:** `requirements.md` brachte die immer geladenen Regeln
  auf 335 Zeilen, Grenze laut [[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]] ist
  300. Meine Fassung war ausschweifender als der Hausstil. Auf 88 Zeilen gekürzt (Details
  der fünf Prüfungen stehen ohnehin in `/req-validate`), Summe jetzt exakt 300.
- Der Hook meldet für dieses Projekt korrekt „Requirements: none yet" — dieses Repo hat
  seine eigenen Anforderungen noch nicht, das ist [[T-0017 Anforderungskette am Beispiel nachweisen]].
