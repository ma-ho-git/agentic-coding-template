---
title: Einsatzbereites Gerüst für strukturiertes Vibe-Coding
type: requirement
ebene: rahmen
kategorie: funktional
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19
nachweis: demo
status: entwurf
tasks: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0001 Einsatzbereites Gerüst für strukturiertes Vibe-Coding

## Anforderung

Das Template muss nach dem Klonen ein vollständiges Gerüst bereitstellen, mit dem ein
Agent strukturiert zu entwickeln beginnen kann, ohne dass der Nutzer Regeln, Ablage oder
Abläufe selbst erfinden muss.

## Begründung

Ohne fertiges Gerüst beginnt jedes Projekt mit derselben Einrichtungsarbeit, und jedes
löst sie anders. Das Template existiert genau, um diese Wiederholung zu ersparen.

## Abnahme

Nach `git clone` und `/bootstrap` existieren: Regeldateien in `.claude/rules/`, ein Vault
unter `knowledge/` mit Board und Anforderungsbereich, ein aktives Stack-Profil und
arbeitende Hooks. Es fehlt keine Datei, die der Zyklus voraussetzt.

Abgegrenzt gegen [[REQ-0017 Anforderungserhebung vor der Entwicklung]]: „einsatzbereit"
heißt, dass das **Gerüst** vollständig ist — nicht, dass sofort codiert wird. Der Weg zum
ersten Code führt über die Anforderungserhebung und das Startgate.

## Präzisierungen

- keine

## Offene Fragen

- keine
