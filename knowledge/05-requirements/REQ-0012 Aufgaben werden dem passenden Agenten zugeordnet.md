---
title: Aufgaben werden dem passenden Agenten zugeordnet
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: review
status: vereinbart
tasks: ["[[T-0005 Cowork-Onboarding-Paket]]"]
tags: [topic/requirements, topic/agents]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0012 Aufgaben werden dem passenden Agenten zugeordnet

## Anforderung

Vor Beginn einer Aufgabe muss geprüft werden, ob Claude Code oder Claude Cowork dafür
besser geeignet ist; die Aufgabe soll von diesem Agenten bearbeitet werden.

## Begründung

Cowork liest die Repo-Konfiguration nicht und führt die Hooks nicht aus. Code dort zu
schreiben umgeht genau die Absicherungen, die das Template ausmachen.

## Abnahme

`CLAUDE.md` §6 enthält eine Routing-Tabelle. Jede Aufgabendatei nennt im Feld `agent` den
vorgesehenen Agenten mit Begründung. `/task-next` meldet ausdrücklich, wenn der laufende
Agent der falsche ist. `cowork/` enthält das Einrichtungspaket für Cowork.

## Herkunft

[[Szenario]], Abschnitt „Bestehende Systeme":

> Claude Cowork — liest sie **nicht**, braucht ein eigenes Einrichtungspaket

## Präzisierungen

- keine

## Offene Fragen

- keine
