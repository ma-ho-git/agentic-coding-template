---
id: T-0023
title: Szenario als optionaler Einstieg
type: task
implements: ["[[REQ-0021 Szenario als optionaler Einstieg]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[T-0024 Szenario trägt die Anforderungserhebung]]"]
---

# T-0023 Szenario als optionaler Einstieg

## Anforderung

[[REQ-0021 Szenario als optionaler Einstieg]]

## Ziel

Wer nicht weiß, was eine Anforderung ist, kann trotzdem erzählen, was er vorhat.
Das Szenario ist dieser Einstieg — angeboten, nie verlangt.

## Akzeptanzkriterien

- [ ] Skill `/szenario` bietet das Szenario an; eine Ablehnung führt ohne Umweg in die
      reguläre Erhebung, das Szenario bleibt nachtragbar
- [ ] Die Anleitung nennt die Pflichtbestandteile (wer, Auslöser, normaler Ablauf, Ergebnis)
      und die nützlichen Zusätze (was schiefgehen kann, Mengen, bestehende Systeme, was nicht
      passieren darf), je mit einem Beispielsatz — zusammen unter einer Bildschirmseite
- [ ] Der Skill fragt nach, wo das Szenario lückenhaft ist, statt die Lücke selbst zu füllen
- [ ] Vorlage `knowledge/90-meta/templates/szenario.md`
- [ ] Ergebnis liegt als `knowledge/05-requirements/szenario.md` im Repository
- [ ] `/bootstrap` bietet das Szenario vor der Erhebung an
- [ ] `check_vault.py` ohne Befund

## Kontext

- Der Nutzen liegt beim Anfänger: [[REQ-0020 Für unerfahrene Anwender nutzbar]]
- Haltung wie in `/req-elicit`: erklären statt fragen, vorschlagen statt verhören,
  „weiß ich nicht" erzeugt eine offene Frage, nie eine Erfindung

## Agent

`claude-code` — Skill, Vorlage, Dokumentation.

## Abhängigkeiten

- keine

## Notizen

- Eigener Skill statt dritter Modus in `/req-elicit`: der ist mit Rahmen- und Stufenmodus
  bereits zweigeteilt, und ein Szenario wird auch nachträglich geschrieben.
