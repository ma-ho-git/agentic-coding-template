---
title: Das Template hält seine eigenen Vorgaben ein
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 ("die Wissensdatenbank ... sollte aber auch schon für dieses Projekt angelegt und genutzt werden")
nachweis: test
status: entwurf
tasks: ["[[T-0007 Selbstverifikation des Templates]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0018 Das Template hält seine eigenen Vorgaben ein

## Anforderung

Das Template muss die Regeln, die es Projekten vorschreibt, selbst einhalten und das
nachweisen — nicht behaupten.

## Begründung

Ein Regelwerk, dessen eigenes Repository die Regeln verletzt, wird nicht ernst genommen und
ist auch inhaltlich verdächtig: was sich am eigenen Gegenstand nicht anwenden lässt, taugt
selten für fremde. Die Selbstanwendung ist zugleich der einzige realistische Test.

## Abnahme

- `tools/check_vault.py` und `tools/check_traceability.py` melden für dieses Repository
  0 Fehler
- Die Testsuite unter `tests/` deckt jeden Hook mit Positiv- **und** Negativfall ab und ist grün
- Jede Aufgabe nennt eine Anforderung oder eine Infrastrukturbegründung
- Der Vault wird für dieses Projekt selbst geführt, nicht nur für fremde vorbereitet

## Präzisierungen

- 2026-08-20: Ergänzt, nachdem `/req-validate` auffiel, dass ein Erfolgskriterium der
  [[Projektvision]] ohne Anforderung dastand.

## Offene Fragen

- keine
