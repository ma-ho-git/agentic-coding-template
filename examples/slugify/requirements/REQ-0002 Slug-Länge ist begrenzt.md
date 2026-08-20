---
title: Slug-Länge ist begrenzt
type: requirement
ebene: detail
kategorie: qualitaet
prioritaet: muss
stufe: Stufe 2
quelle: Betrieb (fiktiv, Beispiel)
nachweis: test
status: vereinbart
tasks: []
tags: [topic/beispiel]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: []
---

# REQ-0002 Slug-Länge ist begrenzt

## Anforderung

Ein erzeugter Slug darf eine festgelegte Höchstlänge nicht überschreiten.

## Begründung

Nachgelagerte Systeme kürzen zu lange Pfadsegmente stillschweigend. Zwei Artikel, deren Titel
sich erst spät unterscheiden, kollidieren dann auf derselben URL. Besser vorne begrenzen als
hinten raten.

## Abnahme

- `slugify(text, max_length)` liefert nie ein Ergebnis länger als `max_length`
- `slugify("one two three four", 7)` liefert `"one-two"`
- Artikel-URLs sind auf 60 Zeichen Slug begrenzt

## Präzisierungen

- 2026-08-20: Höchstlänge für Artikel-URLs auf 60 Zeichen festgelegt (`SLUG_MAX_LENGTH`)

## Offene Fragen

- keine
