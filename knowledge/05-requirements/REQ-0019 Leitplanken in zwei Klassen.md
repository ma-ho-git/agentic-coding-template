---
title: Leitplanken in zwei Klassen
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20
nachweis: test
status: entwurf
tasks: ["[[T-0019 Leitplanken benennen und klassifizieren]]", "[[T-0020 Startgate als starre Leitplanke durchsetzen]]"]
tags: [topic/requirements, topic/agents]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# REQ-0019 Leitplanken in zwei Klassen

## Anforderung

Die Vorteile von KI-Agenten sollen genutzt, ihre Nachteile durch Leitplanken begrenzt werden.
Es muss mindestens zwei Arten geben: **starre** Leitplanken für kritische Entscheidungen und
**flexible** Leitplanken für Optimierungsentscheidungen.

## Begründung

Ein Agent hat kein Gefühl dafür, welche Regel gerade wie schwer wiegt. Ohne Unterscheidung
gilt entweder alles absolut — dann erzeugt jede Stilfrage einen Abbruch — oder nichts,
dann hält auch die Sicherheitsgrenze nicht. Die Zweiteilung ist das, was Verbindlichkeit
und Beweglichkeit gleichzeitig möglich macht.

## Abnahme

- Eine benannte Regel definiert beide Klassen und liefert einen Zuordnungstest
- Jede durchgesetzte Prüfung ist einer Klasse zugeordnet, und die Klasse steht in ihrer Meldung
- Starre Leitplanken sind maschinell durchgesetzt (Exit-Code 2 oder `deny`) — eine starre
  Leitplanke, die nur in Prosa steht, gilt als nicht erfüllt
- Flexible Leitplanken blockieren nicht, verlangen aber eine Begründung im Code bei Abweichung
- Der Startgate-Übertritt ist starr durchgesetzt

## Präzisierungen

- keine

## Offene Fragen

- keine
