---
title: Projektmanagement in der Wissensdatenbank
type: requirement
ebene: rahmen
kategorie: funktional
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: test
status: vereinbart
tasks: ["[[T-0003 Wissensdatenbank aufsetzen]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0002 Projektmanagement in der Wissensdatenbank

## Anforderung

Die Agenten müssen ihre Arbeit über eine Kanban-artige Aufgabenverwaltung in der
Wissensdatenbank strukturieren und den Projektfortschritt dort dokumentieren. Mehrere
Agenten müssen parallel daran arbeiten können.

## Begründung

Ohne einen gemeinsamen, eindeutigen Ort für den Aufgabenstand greifen zwei Agenten
dieselbe Aufgabe auf oder übersehen eine fertige. Der Fortschritt muss nachlesbar sein,
nicht im Sitzungsverlauf verschwinden.

## Abnahme

Board mit den Lanes Backlog/Ready/Doing/Review/Done, eine Datei je Aufgabe mit
Status im Frontmatter, Fortschrittslog je Monat. `/board-sync` meldet keine Abweichungen
zwischen Board und Aufgabendateien.

## Herkunft

[[Szenario]], Abschnitt „Ablauf":

> Aufgaben auf einem Kanban-Board führen, eine nach der anderen abarbeiten.

## Präzisierungen

- keine

## Offene Fragen

- keine
