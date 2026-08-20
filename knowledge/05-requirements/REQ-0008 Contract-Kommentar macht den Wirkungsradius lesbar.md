---
title: Contract-Kommentar macht den Wirkungsradius lesbar
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: test
status: entwurf
tasks: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]", "[[T-0009 Beispielprojekt als Smoke-Test]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0008 Contract-Kommentar macht den Wirkungsradius lesbar

## Anforderung

Jede Quelldatei muss am Anfang einen Kommentar tragen, aus dem die Abhängigkeiten zu
anderen Funktionen und Dateien hervorgehen, damit von einer Änderung betroffene Codestellen
gefunden werden, ohne die komplette Codebasis zu durchsuchen. Der Kommentar ist aktuell zu
halten; nicht sofort durchführbare Folgeänderungen gehen in die Projektplanung.

## Begründung

Der Wirkungsradius einer Änderung ist die teuerste Unbekannte beim Ändern fremden Codes.
Am Code notiert ist er in Sekunden lesbar; ein veralteter Eintrag ist allerdings schlimmer
als keiner, weil man ihm glaubt.

## Abnahme

`.claude/hooks/check_contract.py` blockiert Quelldateien ohne gültigen `@contract`-Block
mit allen Pflichtschlüsseln und meldet veraltete `updated`-Daten. `/contract-sync` findet
Konsumenten über die Liste statt über eine Repo-Suche; nicht sofort machbare Folgearbeit
liegt als Aufgabe in `Ready`, nie in `Backlog`.

## Präzisierungen

- keine

## Offene Fragen

- keine
