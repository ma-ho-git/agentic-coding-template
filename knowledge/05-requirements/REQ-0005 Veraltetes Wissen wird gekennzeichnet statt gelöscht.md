---
title: Veraltetes Wissen wird gekennzeichnet statt gelöscht
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: review
status: entwurf
tasks: ["[[T-0003 Wissensdatenbank aufsetzen]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0005 Veraltetes Wissen wird gekennzeichnet statt gelöscht

## Anforderung

Die Wissensdatenbank muss aktualisiert werden. Veraltetes Wissen muss als `deprecated`
gekennzeichnet werden, mit der Angabe, warum es veraltet ist.

## Begründung

Gelöschtes Wissen hinterlässt keine Spur — wer die alte Lösung noch im Kopf hat, findet
keine Erklärung, warum sie nicht mehr gilt. Die Begründung ist der eigentliche Wert.

## Abnahme

Notizen tragen `review_after`. Veraltete tragen `status: deprecated`, `deprecated_on`,
`deprecated_reason` und wo möglich `superseded_by`. `/kb-review` findet überfällige Notizen;
der SessionStart-Hook meldet ihre Anzahl.

## Präzisierungen

- keine

## Offene Fragen

- keine
