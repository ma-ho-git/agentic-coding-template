---
id: T-0028
title: Startgate verlangt die Fremdlösungs-Entscheidung
type: task
implements: ["[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/meta, topic/agents]
related: ["[[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]", "[[T-0020 Startgate als starre Leitplanke durchsetzen]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0028 Startgate verlangt die Fremdlösungs-Entscheidung

## Anforderung

[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]] — „muss angeboten werden",
maschinell durchgesetzt.

## Ziel

Ein Schritt, der nur in Prosa steht, ist die weichste Leitplanke — das hat dieses Projekt
bei [[T-0020 Startgate als starre Leitplanke durchsetzen]] schon einmal gelernt.

## Akzeptanzkriterien

- [ ] `check_gate.py` verweigert Schreibzugriff auf Produktivcode, solange keine
      Entscheidung über die Fremdlösungs-Suche festgehalten ist
- [ ] Die Meldung nennt, **welche** der beiden Bedingungen fehlt — Rahmen oder Entscheidung —
      und den einen Schritt, der sie erfüllt
- [ ] Erfüllbar durch eine bewusste Ablehnung mit Grund; Suchen ist nicht erzwungen
- [ ] Ausnahmen bleiben wie gehabt: Werkzeug, Tests, Beispiele, alles außerhalb von Quellcode
- [ ] Tests: beide Bedingungen einzeln und gemeinsam, Ausnahmepfade unverändert grün
- [ ] `.claude/rules/guardrails.md` führt die Prüfung in der Zuordnungstabelle
- [ ] ADR hält die Zuordnung fest: unheilbar, weil der fertige Eigenbau die Entscheidung
      faktisch vorwegnimmt

## Kontext

- Entscheidung des Auftraggebers vom 2026-08-20: Startgate erweitern statt Prozessschritt
- [[T-0027 Bestehende Lösungen vor dem Codieren prüfen]] liefert die Datei, die hier
  gelesen wird

## Agent

`claude-code` — Hook, Tests, Regeln.

## Abhängigkeiten

- [[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]

## Notizen

- Die Prüfung darf nicht zur Formalie verkommen. Sie kann nur die Verbindung prüfen, nicht
  die Ernsthaftigkeit der Begründung — das ist dieselbe Grenze wie beim Projektzuschnitt und
  gehört ausdrücklich in die Regel geschrieben.
