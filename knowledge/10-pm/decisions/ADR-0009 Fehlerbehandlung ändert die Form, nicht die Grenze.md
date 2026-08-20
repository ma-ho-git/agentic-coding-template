---
title: ADR-0009 Fehlerbehandlung ändert die Form, nicht die Grenze
type: decision
tags: [topic/code, topic/meta]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]", "[[REQ-0007 Grenzen für Funktionsgröße und Benennung]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[T-0025 Robustheit als Pflicht des Agenten]]"]
---

# ADR-0009 Fehlerbehandlung ändert die Form, nicht die Grenze

## Status

angenommen

## Kontext

- [[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]] verlangt, Fehlerfälle,
  Ausnahmen und den Ausfall angebundener Systeme zu behandeln. Jede Behandlung ist ein
  zusätzlicher Zweig.
- [[REQ-0007 Grenzen für Funktionsgröße und Benennung]] begrenzt Zuweisungen (20) und
  Verschachtelungstiefe (3). Der Konflikt ist nicht theoretisch: `check_quality.py` zählt
  `try` als Verschachtelungsebene (`ast.Try` steht in der Liste). Ein `try` um eine Schleife
  mit einer Bedingung darin liegt bereits **auf** der Grenze; eine zweite Bedingung
  überschreitet sie.
- Zielkonflikte zwischen Qualitätsanforderungen sind laut `.claude/rules/requirements.md`
  normal — aber sie werden benannt und entschieden, nicht stillschweigend zugunsten der
  Seite aufgelöst, die gerade im Weg steht.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Grenze anheben, wenn Fehler behandelt werden | keine Reibung | „behandelt Fehler" ist nicht prüfbar; die Ausnahme wird zur Regel, und die Grenze bedeutet nichts mehr |
| `try` nicht als Ebene zählen | technisch ein Einzeiler | ein wirklich tief verschachteltes `try/except/else` würde unsichtbar |
| **Grenze bleibt, Form ändert sich** | beide Anforderungen bleiben in Kraft | mehr kleine Funktionen; gelegentlich eine begründete Überschreitung |

## Entscheidung

Die Grenze bleibt, die Form der Fehlerbehandlung passt sich an.

Drei Formen, in dieser Reihenfolge:

1. **Wächterklausel und früher Ausstieg** statt eines `else`, das den Gutfall einschließt.
   Der Fehlerfall wird oben abgeräumt, der Rest der Funktion liest sich linear.
2. **Fehlerbehandlung als benannte Einheit** — `retry_with_budget`, `parse_or_reject`.
   Aus einer Ebene Verschachtelung wird ein Funktionsname, den man lesen kann.
3. **Ein `try` um den Funktionsrumpf**, nicht eines je Anweisung.

Passt eine Einheit danach immer noch nicht, macht sie zweierlei — die Arbeit und die
Erholung davon. Dann wird sie geteilt, und das ist keine Zumutung, sondern der Befund.

### Warum `try` weiter als Ebene zählt

Innerhalb eines `try` hat jede Zeile einen zweiten, unsichtbaren Ausgang. Das ist genau die
Last, die die Verschachtelungsgrenze abbilden soll — der Leser muss den Ausnahmepfad
mitdenken, obwohl er nirgends steht. Ein `try` billiger zu machen als ein `if` wäre eine
Aussage über die Lesbarkeit, die nicht stimmt.

### Warum der Konflikt begrenzt ist

Die Größengrenzen sind **flexible** Leitplanken ([[ADR-0006 Zwei Klassen von Leitplanken]]):
Sie melden, sie blockieren nicht. Wer eine Fehlerbehandlung schreibt, die sich nicht sinnvoll
teilen lässt, überschreitet die Grenze und schreibt den Grund in den Code. Der Konflikt kann
also nie dazu führen, dass Robustheit unterbleibt — nur dazu, dass eine Abweichung sichtbar
wird. Genau dafür ist die Klasse gedacht.

## Konsequenzen

- `.claude/rules/robustness.md` führt die drei Formen samt Kostenhinweis.
- `code-quality.md` bleibt unverändert — kein Schwellwert wird angefasst, keine Ausnahme
  eingebaut.
- Mehr kleine, benannte Einheiten für Fehlerbehandlung. Nebenwirkung: Sie sind einzeln
  testbar, was die Testpflicht je Fehlerpfad billiger macht.

## Revidieren wenn

- Die Hinweise in der Praxis überwiegend an Fehlerbehandlung hängen, die sich nachweislich
  nicht sinnvoll teilen lässt. Dann ist der Schwellwert falsch — nicht die Entscheidung,
  dass Fehlerbehandlung sich der Grenze fügt.
