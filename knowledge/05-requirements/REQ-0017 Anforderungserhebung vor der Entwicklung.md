---
title: Anforderungserhebung vor der Entwicklung
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: review
status: vereinbart
tasks: ["[[T-0012 Anforderungsregeln und Vault-Struktur]]", "[[T-0013 Skills für die Anforderungserhebung]]", "[[T-0014 Rückverfolgbarkeit maschinell prüfen]]", "[[T-0015 Bestehenden Arbeitszyklus anpassen]]", "[[T-0016 Architekturschritt aus Qualitätsanforderungen]]", "[[T-0017 Anforderungskette am Beispiel nachweisen]]", "[[T-0030 Funktional und nicht-funktional benennen]]", "[[T-0031 Qualitätsmerkmale vollständig abfragen]]"]
tags: [topic/requirements, topic/requirements]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0017 Anforderungserhebung vor der Entwicklung

## Anforderung

Vor dem Codieren muss eine Anforderungserhebung und -dokumentation stattfinden. Der Rahmen
— was gebaut wird, samt geltender technischer, funktionaler, organisatorischer,
sicherheitskritischer und weiterer nicht coding-spezifischer Anforderungen — ist vor dem
ersten Produktivcode zu klären. Detailanforderungen folgen je Entwicklungsstufe und dürfen
beim Codieren nachgeschärft werden. Die Anforderungen dienen als Grundlage der Entwicklung.

## Begründung

Ohne Anforderungen sagt eine Aufgabe nur, wann sie fertig ist, nie warum es sie geben soll.
Rein inkrementelle Erhebung beschreibt das Zielartefakt zu unsicher und lässt
architekturprägende Vorgaben zu spät auftauchen.

## Abnahme

`knowledge/05-requirements/baseline.md` trägt `baseline_status`; Entwicklung beginnt erst
bei `vereinbart`, und jede der sechs Rahmenkategorien ist belegt oder ausdrücklich als nicht
zutreffend begründet. Jede Aufgabe nennt `implements:` oder eine Infrastrukturbegründung.
`tools/check_traceability.py` meldet 0 Fehler.

## Herkunft

[[Szenario]], Abschnitt „Was schiefgehen kann":

> Es wird sofort codiert, ohne dass festgehalten ist, was entstehen soll.

## Präzisierungen

### 2026-08-20 — Erhebung nennt die Arten und fragt die Merkmale einzeln

Recherche zu funktionalen und nicht-funktionalen Anforderungen ergab zwei Lücken, die den
Wortlaut dieser Anforderung nicht ändern, aber ihre Umsetzung schärfen:

- Die Begriffe **funktional / nicht-funktional** kommen im Projekt nicht vor, obwohl die
  sechs Kategorien genau darauf beruhen. Sie werden benannt und auf Sommervilles drei
  Gruppen abgebildet ([[T-0030 Funktional und nicht-funktional benennen]]).
- `qualitaet` wird als **eine** Frage gestellt und deckt sieben Merkmale ab. Künftig werden
  sie einzeln abgefragt, mit der Szenarioform als Anleitung zur Messbarkeit
  ([[T-0031 Qualitätsmerkmale vollständig abfragen]]).

## Offene Fragen

- keine
