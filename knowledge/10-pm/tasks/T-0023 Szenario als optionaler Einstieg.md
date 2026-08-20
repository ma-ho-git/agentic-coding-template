---
id: T-0023
title: Szenario als optionaler Einstieg
type: task
implements: ["[[REQ-0021 Szenario als optionaler Einstieg]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
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

- [x] Skill `/szenario` bietet das Szenario an; eine Ablehnung führt ohne Umweg in die
      reguläre Erhebung, das Szenario bleibt nachtragbar
- [x] Die Anleitung nennt die Pflichtbestandteile (wer, Auslöser, normaler Ablauf, Ergebnis)
      und die nützlichen Zusätze (was schiefgehen kann, Mengen, bestehende Systeme, was nicht
      passieren darf), je mit einem Beispielsatz — zusammen unter einer Bildschirmseite
- [x] Der Skill fragt nach, wo das Szenario lückenhaft ist, statt die Lücke selbst zu füllen
- [x] Vorlage `knowledge/90-meta/templates/szenario.md`
- [x] Ergebnis liegt als `knowledge/05-requirements/szenario.md` im Repository
- [x] `/bootstrap` bietet das Szenario vor der Erhebung an
- [x] `check_vault.py` ohne Befund

## Kontext

- Der Nutzen liegt beim Anfänger: [[REQ-0020 Für unerfahrene Anwender nutzbar]]
- Haltung wie in `/req-elicit`: erklären statt fragen, vorschlagen statt verhören,
  „weiß ich nicht" erzeugt eine offene Frage, nie eine Erfindung

## Ergebnis

- Skill `/szenario`: bietet einmal an, nimmt ein Nein an, verweist auf die Nachtragbarkeit.
- Die Hilfe ist ein **Block von vierzehn Zeilen**, kein Fragebogen — drei Pflichtteile, vier
  nützliche Zusätze, je mit einem Beispielsatz aus dem Alltag.
- Tragende Entwurfsentscheidung: **der Nutzer erzählt, der Agent ordnet und liest zurück.**
  Ein Formular hätte genau die Nutzer abgeschreckt, für die der Schritt gedacht ist.
- Zweite Entscheidung: **die Worte des Nutzers bleiben stehen.** „Die Liste ist manchmal
  kaputt" wird hier nicht zu „inkonsistente Eingabedaten" — der Fachbegriff gehört in die
  abgeleitete Anforderung, nicht ins Szenario. Sonst verschwindet genau das, was das
  Szenario wertvoll macht.
- Lücken werden erfragt, nie gefüllt. „Weiß ich nicht" landet unter Offene Punkte.
- Angebot in `/bootstrap` (Schritt 3.0) und in `/req-elicit` (Rahmenmodus), Zyklus in
  `CLAUDE.md` §3, Hinweis im README.
- Vorlage `knowledge/90-meta/templates/szenario.md`; `knowledge/05-requirements/szenario.md`
  ist als ausgefülltes Beispiel angelegt — rekonstruiert aus der Vorgabe vom 2026-08-19 und
  ausdrücklich als unbestätigt gekennzeichnet.

Suite 78 grün (unverändert — reine Skill- und Dokumentationsarbeit), `check_vault.py` und
`check_traceability.py` ohne Befund.

## Agent

`claude-code` — Skill, Vorlage, Dokumentation.

## Abhängigkeiten

- keine

## Notizen

- Eigener Skill statt dritter Modus in `/req-elicit`: der ist mit Rahmen- und Stufenmodus
  bereits zweigeteilt, und ein Szenario wird auch nachträglich geschrieben.
