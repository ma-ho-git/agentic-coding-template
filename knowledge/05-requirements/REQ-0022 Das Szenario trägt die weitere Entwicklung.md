---
title: Das Szenario trägt die weitere Entwicklung
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20
nachweis: test
status: vereinbart
tasks: ["[[T-0024 Szenario trägt die Anforderungserhebung]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[REQ-0021 Szenario als optionaler Einstieg]]", "[[REQ-0017 Anforderungserhebung vor der Entwicklung]]", "[[Rahmen und Startgate]]"]
---

# REQ-0022 Das Szenario trägt die weitere Entwicklung

## Anforderung

Liegt ein Szenario vor, muss der weitere Entwicklungsprozess darauf aufsetzen — insbesondere
leitet die Anforderungserhebung ihre Vorschläge daraus ab und weist die Herkunft nach.

## Begründung

Ein Szenario, das einmal gelesen und dann vergessen wird, ist Dekoration. Es ist die einzige
Stelle, an der der Nutzer in **seinen eigenen Worten** festgehalten hat, was er will. Jede
spätere Ableitung muss darauf zurückführbar bleiben — sonst ersetzt der Agent unbemerkt die
Absicht des Nutzers durch seine eigene, und niemand kann das hinterher auseinanderhalten.

## Abnahme

- Bei vorhandenem Szenario schlägt die Erhebung Anforderungen daraus ab, statt kalt zu
  fragen; jede so entstandene Anforderung nennt das Szenario in `quelle`.
- Die Validierung meldet jeden Bestandteil des Szenarios, den keine Anforderung abdeckt, und
  jede Anforderung, die dem Szenario widerspricht.
- Die Rückverfolgungskette in `.claude/rules/requirements.md` beginnt beim Szenario.
- `tools/check_traceability.py` meldet, wenn ein Szenario existiert, aber keine einzige
  Anforderung es als Quelle nennt.

## Präzisierungen

- Die maschinelle Prüfung kann nur die *Verbindung* prüfen, nicht die inhaltliche
  Abdeckung — Prosa ist nicht maschinell abgleichbar. Die inhaltliche Prüfung bleibt bei
  der Validierung und damit beim Menschen.

## Offene Fragen

- keine
