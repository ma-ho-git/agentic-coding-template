---
title: Projektwissen wird eigenständig dokumentiert
type: requirement
ebene: rahmen
kategorie: funktional
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: test
status: entwurf
tasks: ["[[T-0003 Wissensdatenbank aufsetzen]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0003 Projektwissen wird eigenständig dokumentiert

## Anforderung

Recherchiertes oder als wichtig eingestuftes Wissen muss von den Agenten eigenständig
dokumentiert werden. Mehrfach aufgetretene oder schwer zu lösende Probleme müssen mit
ihrer Lösung festgehalten werden.

## Begründung

Wissen, das nur im Sitzungsverlauf steht, ist beim nächsten Start verloren. Ein Problem,
das zweimal auftritt und zweimal neu gelöst wird, kostet zweimal.

## Abnahme

Für jede Auslöserbedingung aus `.claude/rules/knowledge-base.md` existiert eine Notiz.
Troubleshooting-Notizen führen Symptom, Kontext, Ursache, Lösung, Sackgassen, Vorbeugung
und ein Feld `occurrences`. `tools/check_vault.py` meldet 0 Fehler.

## Herkunft

[[Szenario]], Abschnitt „Ablauf":

> Was dabei gelernt wurde, landet in der Wissensdatenbank statt im Gesprächsverlauf.

## Präzisierungen

- keine

## Offene Fragen

- keine
