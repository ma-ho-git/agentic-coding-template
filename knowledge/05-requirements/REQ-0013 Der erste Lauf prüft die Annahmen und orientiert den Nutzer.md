---
title: Der erste Lauf prüft die Annahmen und orientiert den Nutzer
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: demo
status: entwurf
tasks: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]"]
tags: [topic/requirements, topic/agents]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer

## Anforderung

Bei der ersten Anfrage nach dem Klonen muss selbstständig geprüft werden, ob Vorgaben des
Projekts anzupassen sind, weil sich Voraussetzungen bei Claude, GitHub oder anderen
Ressourcen geändert haben. Danach ist dem Verwender sehr kurz zu erklären, was das Projekt
macht, was die ersten Schritte sind und was seine eigenen Aufgaben sind.

## Begründung

Ein Template altert gegen Dienste, die sich ändern. Wer es Monate später klont, baut sonst
auf Annahmen, die nicht mehr gelten — und merkt es erst, wenn etwas bricht.

## Abnahme

`/bootstrap` arbeitet `knowledge/90-meta/environment-manifest.md` ab, setzt je Eintrag
`verified` und `state`, passt betroffene Dateien an und schließt mit einer Orientierung von
höchstens 20 Zeilen in drei Abschnitten. Der SessionStart-Hook fordert `/bootstrap` an,
wenn der jüngste Eintrag älter als 30 Tage ist.

## Herkunft

[[Szenario]], Abschnitt „Ablauf":

> Vorlage klonen, erster Lauf prüft die eigenen Annahmen und richtet das Projekt ein.

## Präzisierungen

- keine

## Offene Fragen

- keine
