---
title: Subagenten nur nach Kosten-Nutzen-Prüfung
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: soll
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: review
status: entwurf
tasks: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]"]
tags: [topic/requirements, topic/agents]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0014 Subagenten nur nach Kosten-Nutzen-Prüfung

## Anforderung

Subagenten dürfen für Teilaufgaben eingesetzt werden, aber erst nach positiver
Kosten-/Nutzenprüfung oder auf Basis einer bereits dokumentierten positiven Prüfung für
diese Art von Aufgabe.

## Begründung

Ein Subagent startet ohne Kontext und muss ihn sich neu erarbeiten. Das lohnt sich bei
abgegrenzten Recherchen und schadet bei allem, was den Gesprächsverlauf braucht.

## Abnahme

`.claude/rules/agent-conduct.md` nennt vier Prüffragen; ab zwei Ja ist der Einsatz
gerechtfertigt. Jede Prüfung wird als Zeile in
`knowledge/90-meta/subagent-decisions.md` festgehalten, mit Aufgabenart, Entscheidung,
Begründung und Ergebnis.

## Präzisierungen

- keine

## Offene Fragen

- keine
