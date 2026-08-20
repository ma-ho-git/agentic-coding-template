---
title: Testgetriebene Entwicklung ist verpflichtend
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: test
status: entwurf
tasks: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0006 Testgetriebene Entwicklung ist verpflichtend

## Anforderung

Code muss testgetrieben entstehen: zuerst ein fehlschlagender Test, dann der Code, der ihn
bestehen lässt, dann Refactoring.

## Begründung

Ein Test, der nach dem Code entsteht, prüft die Implementierung statt der Absicht — und
besteht auch dann, wenn die Absicht verfehlt wurde.

## Abnahme

`.claude/rules/tdd.md` ist verbindlich und nennt genau drei Ausnahmen, jede im
Commit zu begründen. Für jede Verhaltensänderung existiert ein Test, der ohne die Änderung
fehlschlägt. Volle Suite grün vor jedem Abschluss einer Aufgabe.

## Präzisierungen

- keine

## Offene Fragen

- keine
