---
title: Dokumentation ist für Mensch und Agent nutzbar
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: test
status: vereinbart
tasks: ["[[T-0003 Wissensdatenbank aufsetzen]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0004 Dokumentation ist für Mensch und Agent nutzbar

## Anforderung

Die Wissensdatenbank muss so geschrieben und verknüpft sein, dass Menschen wie Agenten
Zusammenhänge schnell erfassen: nach Themen sortierte Auflistungen mit stichpunktartigen,
aussagekräftigen Abschnitten statt Fließtext, verlinkt und getaggt.

## Begründung

Zwei Lesergruppen mit einem Format zu bedienen geht nur über Kürze und Struktur. Fließtext
zwingt beide zum Lesen von Anfang bis Ende; ein Agent kann darin nicht gezielt nachschlagen.

## Abnahme

Jede Notiz hat Frontmatter mit Pflichtfeldern, mindestens einen ausgehenden Wikilink und
ist von `00-index.md` aus erreichbar. Tags tragen einen Namespace. Geprüft durch
`tools/check_vault.py` — 0 Fehler, 0 Waisen.

## Präzisierungen

- keine

## Offene Fragen

- keine
