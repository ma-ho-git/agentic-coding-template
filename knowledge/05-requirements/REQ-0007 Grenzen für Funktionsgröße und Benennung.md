---
title: Grenzen für Funktionsgröße und Benennung
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: test
status: vereinbart
tasks: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0018 Grenzwerte auf die Projektvorgabe zurückführen]]", "[[T-0041 Testnamen von der Wortgrenze ausnehmen]]"]
tags: [topic/requirements, stack/python]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0007 Grenzen für Funktionsgröße und Benennung

## Anforderung

Funktionen mit mehr als 20 Zuweisungen oder mehr als drei Parametern müssen auf Aufteilung
geprüft und, wo sinnvoll möglich, aufgeteilt werden. Eine Funktionalität je Funktion.
Namen von Funktionen, Variablen und Konstanten bestehen aus höchstens drei für Menschen
aussagekräftigen Wörtern.

## Begründung

Spaghetti-Code entsteht schleichend. Maschinell prüfbare Grenzen erzwingen die Frage nach
der Aufteilung an der Stelle, an der sie noch billig ist.

## Abnahme

`.claude/hooks/check_quality.py` meldet Überschreitungen von `max_assignments`,
`max_parameters` und `max_name_words` aus `config.json`. Bewusste Überschreitungen tragen
eine Begründung im Code. Hook-Tests decken Positiv- und Negativfall ab.

## Präzisierungen

- **2026-08-20 — Geltungsbereich der Wortgrenze.** Sie gilt Bezeichnern, nicht Testnamen.
  Ein Testname ist ein Satz über Verhalten, und [[REQ-0006 Testgetriebene Entwicklung ist verpflichtend]]
  verlangt genau das. Gemessen feuerte die Grenze bei 139 von 154 Testfunktionen; die
  Begründung und die verworfenen Alternativen stehen in
  [[ADR-0013 Testnamen sind Verhaltenssätze, keine Bezeichner]]. Die Aussage der Anforderung
  bleibt unverändert — Zuweisungen, Parameter und alle übrigen Bezeichner sind nicht berührt.

## Offene Fragen

- keine
