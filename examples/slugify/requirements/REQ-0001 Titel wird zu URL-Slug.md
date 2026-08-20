---
title: Titel wird zu URL-Slug
type: requirement
ebene: rahmen
kategorie: funktional
prioritaet: muss
stufe:
quelle: Redaktion (fiktiv, Beispiel)
nachweis: test
status: vereinbart
tasks: []
tags: [topic/beispiel]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: []
---

# REQ-0001 Titel wird zu URL-Slug

## Anforderung

Das System muss aus einem beliebigen Artikeltitel eine URL-sichere Kennung erzeugen.

## Begründung

Artikeltitel enthalten Großbuchstaben, Satzzeichen und Leerzeichen. In einer URL sind die
teils verboten, teils schwer lesbar und über Systeme hinweg unterschiedlich kodiert.

## Abnahme

- `slugify("Hello World", 60)` liefert `"hello-world"`
- Satzzeichen entfallen: `slugify("Wait, what?!", 60)` liefert `"wait-what"`
- Das Ergebnis enthält ausschließlich `a-z`, `0-9` und `-`

## Präzisierungen

- keine

## Offene Fragen

- keine
