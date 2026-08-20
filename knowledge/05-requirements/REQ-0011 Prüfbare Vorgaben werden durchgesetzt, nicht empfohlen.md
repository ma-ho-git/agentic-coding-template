---
title: Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen
type: requirement
ebene: rahmen
kategorie: technisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: test
status: vereinbart
tasks: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0010 CI-Workflow für die Regelprüfung]]"]
tags: [topic/requirements, stack/claude-code]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen

## Anforderung

Vorgaben, die sich maschinell prüfen lassen, müssen durchgesetzt werden — nicht nur in
Prosa beschrieben. Die Prüfung muss auch für Beiträge greifen, die nicht durch einen Agenten
mit Hooks entstanden sind.

## Begründung

Anweisungen in Instruktionsdateien beeinflussen das Verhalten, garantieren es aber nicht.
Was verbindlich sein soll, braucht eine Instanz, die es ablehnt.

## Abnahme

Hooks in `.claude/hooks/` laufen bei SessionStart, vor Bash-Kommandos und nach
Schreibvorgängen. `.github/workflows/rules.yml` führt dieselben Skripte am Pull Request aus.
Jeder Hook hat Tests für Positiv- und Negativfall; die Suite ist grün.

## Herkunft

[[Szenario]], Abschnitt „Ergebnis":

> Eine Regelverletzung wird abgelehnt, nicht bloß angemahnt.

## Präzisierungen

- keine

## Offene Fragen

- keine
