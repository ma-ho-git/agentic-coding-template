---
title: Testnamen sind Verhaltenssätze, keine Bezeichner
type: decision
status: accepted
tags: [topic/guardrails, topic/testing, stack/python]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[REQ-0007 Grenzen für Funktionsgröße und Benennung]]", "[[REQ-0019 Leitplanken in zwei Klassen]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[T-0041 Testnamen von der Wortgrenze ausnehmen]]"]
---

# ADR-0013 Testnamen sind Verhaltenssätze, keine Bezeichner

## Status

Angenommen, 2026-08-20. Entschieden vom Auftraggeber, nachdem drei Möglichkeiten
gegenübergestellt waren.

## Kontext

Die Drei-Wort-Grenze aus [[REQ-0007 Grenzen für Funktionsgröße und Benennung]] meldete
**139 von 154** Testfunktionen dieses Repositories — 90 %. Rechnet man das von pytest
erzwungene `test_`-Präfix heraus, bleiben immer noch 118.

Dahinter liegt kein Schlamperei-Problem, sondern ein Widerspruch zwischen zwei eigenen
Regeln. `.claude/rules/tdd.md` verlangt ausdrücklich:

> A test name states the behaviour, not the method name: `rejects_expired_token`,
> not `test_validate`.

Ein Verhalten in drei Wörtern auszusprechen gelingt selten; mit dem Pflichtpräfix ist die
Grenze konstruktionsbedingt überschritten. Die eine Regel verlangt also genau das, was die
andere anmahnt.

Das ist mehr als Lärm. [[ADR-0006 Zwei Klassen von Leitplanken]] hält fest, dass die Klasse
einer Meldung erkennbar bleiben muss — „whatever cannot be told apart is eventually treated
the same — as noise". Ein Hinweis, der fast immer feuert, erzieht dazu, die ganze flexible
Klasse zu überlesen. Dann trifft es auch die Hinweise, die etwas bedeuten.

## Entscheidung

Die Wortgrenze gilt nicht für Funktionen, deren Name das **Pflichtpräfix eines
Testrunners** trägt: `test_` (pytest) und `TestXxx` (Go).

Die Ausnahme hängt am **Namen**, nicht am Verzeichnis. Ein Testname in einem
Produktivverzeichnis ist immer noch ein Verhaltenssatz; eine Hilfsfunktion in `tests/` ist
immer noch eine Funktion und bleibt geprüft. Zuweisungen, Parameter und Verschachtelung
greifen bei Testfunktionen unverändert.

## Erwogene Alternativen

**Nichts ändern, Begründung im Docstring.** Formal ausreichend — die flexible Leitplanke
verlangt eine Begründung im Code, und die stand dort. Verworfen: Eine Begründung, die man
in jede Testdatei kopieren muss, ist keine Ausnahme mehr, sondern eine Regel, die zufällig
andersherum steht. Und der Hinweis wäre weiter bei jedem Commit erschienen.

**Das Limit global auf vier Wörter anheben.** Verworfen: Es hätte auch Produktivcode
gelockert, wo die Drei-Wort-Grenze eine bewusste Vorgabe aus dem Projektauftrag ist. Ein
Problem im Testcode darf nicht die Grenze im Produktivcode verschieben.

**Präfix herausrechnen statt ausnehmen** (also `test_rejects_expired_token` als drei Wörter
zählen). Gemessen und verworfen: Es hätte noch 118 der 154 Namen gemeldet. Die Grenze passt
nicht knapp daneben — sie passt für diese Sorte Name gar nicht.

## Folgen

- `check_quality.py` meldet nach der Änderung **keinen** der 154 Testnamen mehr.
- Der Preis: Ein wirklich ausufernder Testname wird nicht mehr angemahnt. Hinnehmbar — ein
  langer Testname beschreibt entweder ein Verhalten genau, oder er verrät einen Test, der zu
  viel auf einmal prüft, und das fällt im Review auf, nicht an der Wortzahl.
- Was die Ausnahme **nicht** deckt: `document()` in `tools/handover_texts.py` überschreitet
  die Parametergrenze und behält seine Begründung im Code. Das ist der Einzelfall, für den
  die flexible Klasse gedacht ist — im Unterschied zu einer Grenze, die für eine ganze
  Sorte Bezeichner nie gepasst hat.
- Aus dieser Sitzung als Faustregel: **Eine flexible Leitplanke, die bei fast allen Fällen
  feuert, ist keine Leitplanke, sondern ein Messfehler.** Wer sie das nächste Mal begründen
  will, zählt vorher, wie oft sie feuert.
