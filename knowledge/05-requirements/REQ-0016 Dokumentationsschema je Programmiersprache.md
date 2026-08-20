---
title: Dokumentationsschema je Programmiersprache
type: requirement
ebene: rahmen
kategorie: technisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: review
status: entwurf
tasks: ["[[T-0004 Stack-Profile und Doku-Schema]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0016 Dokumentationsschema je Programmiersprache

## Anforderung

Für die Code-Dokumentation ist je Sprache der weitverbreitetste Standard zu ermitteln, als
Projektschema festzuhalten und anzuwenden. Die Dokumentation ist aussagekräftig und
stichpunktartig, ohne Füllwörter; komplizierte Zuweisungen werden dokumentiert.

## Begründung

Ein sprachfremdes Kommentarschema kostet jeden Leser Übersetzungsarbeit und macht die
vorhandenen Werkzeuge der Sprache unbrauchbar.

## Abnahme

Das aktive Stack-Profil unter `stacks/active.md` nennt den Docstring-Standard und das
prüfende Werkzeug. Neuer Code folgt ihm. [[Dokumentationsstandards je Sprache]] hält die
Vorauswahl je Sprache samt ihrer Belastbarkeit fest.

## Präzisierungen

- keine

## Offene Fragen

- keine
