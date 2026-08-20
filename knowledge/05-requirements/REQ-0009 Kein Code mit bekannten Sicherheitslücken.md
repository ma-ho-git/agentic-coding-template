---
title: Kein Code mit bekannten Sicherheitslücken
type: requirement
ebene: rahmen
kategorie: sicherheit
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: test
status: entwurf
tasks: ["[[T-0001 Agentenregeln und Repo-Grundgerüst]]", "[[T-0002 Hooks zur Durchsetzung der Vorgaben]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0009 Kein Code mit bekannten Sicherheitslücken

## Anforderung

Erstellter Code darf keine bekannten oder offensichtlichen Sicherheitslücken enthalten.
Geheimnisse dürfen nicht ins Repository gelangen.

## Begründung

Eine Sicherheitslücke, die beim Schreiben entsteht, ist billig zu vermeiden und teuer zu
finden. Ein einmal committetes Geheimnis bleibt in der Historie, auch nach dem Löschen.

## Abnahme

`.claude/hooks/check_secrets.py` blockiert Schreibvorgänge mit Anmeldedaten-Mustern
(getestet gegen Positiv- und Negativfälle). `.claude/rules/security.md` führt eine
Prüfliste, die vor dem Verlassen der Review-Lane gegen den Diff durchgegangen wird.

## Herkunft

[[Szenario]], Abschnitt „Was nicht passieren darf":

> Erstellter Code darf keine (bekannten oder offensichtlichen) Sicherheitslücken beinhalten

## Präzisierungen

- keine

## Offene Fragen

- keine
