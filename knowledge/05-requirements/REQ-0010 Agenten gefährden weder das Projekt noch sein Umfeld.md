---
title: Agenten gefährden weder das Projekt noch sein Umfeld
type: requirement
ebene: rahmen
kategorie: sicherheit
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Projektvorgabe vom 2026-08-19 — "[[Szenario]]"
nachweis: test
status: vereinbart
tasks: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]"]
tags: [topic/requirements, topic/agents]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]"]
---

# REQ-0010 Agenten gefährden weder das Projekt noch sein Umfeld

## Anforderung

Agenten und Subagenten dürfen das Projekt nicht gefährden, keine zusätzlichen Kosten
verursachen und keine anderen Projekte gefährden.

## Begründung

Ein Agent hat dieselben Rechte wie die Sitzung, in der er läuft. Ohne harte Grenze ist ein
zerstörerisches Kommando nur ein Tippfehler entfernt — und Kosten entstehen lautlos.

## Abnahme

`.claude/hooks/git_guard.py` verweigert Force-Push, Push auf den Standardbranch,
`reset --hard`, History-Rewriting und rekursives Löschen außerhalb des Projekts; getestet.
`.claude/rules/agent-conduct.md` verbietet kostenpflichtige Dienste und Zugriffe außerhalb
des Repositories ohne ausdrücklichen Auftrag.

## Herkunft

[[Szenario]], Abschnitt „Was nicht passieren darf":

> Agenten und Subagenten dürfen das durchzuführende Projekt nicht gefährden, zusätzliche Kosten verursachen oder andere Projekte gefährden

## Präzisierungen

- keine

## Offene Fragen

- keine
