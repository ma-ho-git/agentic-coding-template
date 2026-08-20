---
id: T-0041
title: Testnamen von der Wortgrenze ausnehmen
type: task
implements: ["[[REQ-0007 Grenzen für Funktionsgröße und Benennung]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/guardrails, stack/python]
related: ["[[REQ-0019 Leitplanken in zwei Klassen]]", "[[ADR-0013 Testnamen sind Verhaltenssätze, keine Bezeichner]]"]
---

# T-0041 Testnamen von der Wortgrenze ausnehmen

## Anforderung

[[REQ-0007 Grenzen für Funktionsgröße und Benennung]] — Präzisierung des Geltungsbereichs,
vom Auftraggeber am 2026-08-20 entschieden.

## Ziel

Die Drei-Wort-Grenze feuert bei **139 von 154** Testfunktionen im Repository, also bei 90 %.
Auch ohne das von pytest erzwungene `test_`-Präfix bleiben 118. Ein Hinweis, der fast immer
feuert, erzieht dazu, die ganze Klasse zu überlesen — samt der Hinweise, die etwas bedeuten.

Dahinter liegt ein Widerspruch zwischen zwei eigenen Regeln: `.claude/rules/tdd.md` verlangt
ausdrücklich Namen, die das Verhalten aussprechen („`rejects_expired_token`, nicht
`test_validate`"). Das sind konstruktionsbedingt drei Wörter **plus** Pflichtpräfix.

`check_quality.py` prüft die Wortgrenze deshalb nicht mehr für Testfunktionen. Alles andere
in Testdateien — Variablen, Hilfsfunktionen, Klassen — bleibt geprüft.

## Akzeptanzkriterien

- [x] Die Wortgrenze meldet keine Funktion, deren Name das Pflichtpräfix einer Testfunktion
      trägt (`test_` für pytest, `Test` für Go)
- [x] Hilfsfunktionen, Variablen und Klassen in Testdateien bleiben geprüft — die Ausnahme
      hängt am Namen, nicht am Verzeichnis
- [x] Die übrigen Prüfungen greifen bei Testfunktionen unverändert: Zuweisungen, Parameter,
      Verschachtelung
- [x] Hook-Tests für Positiv- und Negativfall, wie die Abnahme von REQ-0007 es verlangt
- [x] Gemessen: der Hinweis feuert danach bei keiner der 154 Testfunktionen mehr
- [x] Die Begründungen im Code, die es nur wegen dieser Grenze gab, sind entfernt
- [x] `.claude/rules/code-quality.md` und die Präzisierung in REQ-0007 benennen die Ausnahme

## Kontext

- Warum am Namen und nicht am Pfad: Die Ausnahme gilt der **Sorte Bezeichner**, nicht dem
  Ordner. Ein Testname in einem Produktivverzeichnis ist immer noch ein Verhaltenssatz, und
  eine Hilfsfunktion in `tests/` ist immer noch eine Funktion.
- Was die Ausnahme **nicht** deckt: `document()` in `tools/handover_texts.py` überschreitet
  die Parametergrenze und behält seine Begründung im Code. Das ist der Einzelfall, für den
  die flexible Klasse gedacht ist.

## Agent

`claude-code` — Hook, Tests, Regeltext.

## Abhängigkeiten

- keine

## Ergebnis

- `check_quality.py` kennt `is_test_name()`: `test_` (pytest) und `TestXxx` (Go). Angewandt
  im Python- und im generischen Prüfer, damit die Regel in beiden Sprachen dieselbe ist.
- **Gemessen: 139 → 0.** Keine der 154 Testfunktionen löst den Hinweis noch aus.
- Die Begründung, die dafür in 20 Testdateien stand, ist entfernt — sie war nur nötig,
  solange die Prüfung falsch lag.
- Negativfälle bleiben grün und sichern die Ausnahme gegen Ausweitung: eine Hilfsfunktion in
  einer Testdatei wird weiter gemeldet, und `test_it(one, two, three, four)` verstößt
  weiterhin gegen die Parametergrenze.
- Suite 158 grün.

## Notizen

- `document()` in `tools/handover_texts.py` bleibt mit Begründung im Code stehen. Der
  Unterschied zur Testnamen-Grenze ist der Grund, aus dem es zwei Klassen gibt: ein
  Einzelfall trägt eine Begründung, eine Grenze, die für eine ganze Sorte Bezeichner nie
  gepasst hat, gehört korrigiert.
