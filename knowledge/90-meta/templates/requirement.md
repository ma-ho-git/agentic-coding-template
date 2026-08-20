---
title: <Kurzer, suchbarer Titel>
type: requirement
ebene: rahmen              # rahmen | detail
kategorie: funktional      # funktional | technisch | organisatorisch | sicherheit | recht | qualitaet
prioritaet: muss           # muss | soll | kann
stufe:                     # nur bei ebene=detail: Entwicklungsstufe, sonst leer
quelle: <Stakeholder oder Dokument; bei Ableitung aus dem Szenario zusätzlich "[[Szenario]]">
nachweis: test             # test | messung | review | demo
status: entwurf            # entwurf | vereinbart | umgesetzt | verworfen
tasks: []
tags: [topic/<bereich>]
created: JJJJ-MM-TT
updated: JJJJ-MM-TT
review_after: JJJJ-MM-TT
related: ["[[baseline]]"]
---

# REQ-XXXX <Titel>

## Anforderung

<Ein Satz. "Das System muss …" — prüfbar formuliert, nicht wolkig.>

## Begründung

<Warum wird das gebraucht? Ohne Begründung keine Anforderung.>

## Abnahme

<Konkret messbar: Schwellwert, Szenario, beobachtbares Verhalten.
 Wenn hier nichts Prüfbares steht, ist es noch keine Anforderung.>

## Herkunft

<Nur bei Ableitung aus dem Szenario. Die Stelle wörtlich zitieren, mit Abschnittsnamen:

 [[Szenario]], Abschnitt „Ablauf":

 > Datei einlesen, Dubletten raus, nach Region sortieren.

 Damit bleibt unterscheidbar, wo der Nutzer gesprochen hat und wo der Agent interpretiert.>

## Präzisierungen

<Nachschärfungen beim Codieren, mit Datum. Aussageänderungen laufen über /req-change
 und gehören nicht hierher.>

## Offene Fragen

- <was noch mit dem Stakeholder zu klären ist, oder "keine">
