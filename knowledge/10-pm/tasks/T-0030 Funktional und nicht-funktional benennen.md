---
id: T-0030
title: Funktional und nicht-funktional benennen
type: task
implements: ["[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[T-0031 Qualitätsmerkmale vollständig abfragen]]"]
---

# T-0030 Funktional und nicht-funktional benennen

## Anforderung

[[REQ-0017 Anforderungserhebung vor der Entwicklung]] — Präzisierung vom 2026-08-20.

## Ziel

Die Unterscheidung funktional / nicht-funktional ist der Grundbegriff der
Anforderungserhebung. Im Projekt kommt sie nirgends vor.

## Akzeptanzkriterien

- [ ] `.claude/rules/requirements.md` benennt beide Arten und sagt, **warum sie
      unterschiedlich erhoben werden**: funktionale erzählt der Nutzer von selbst,
      nicht-funktionale muss man gegen eine Liste abfragen
- [ ] Unsere sechs Kategorien sind auf Sommervilles drei Gruppen abgebildet
      (Produkt / organisatorisch / extern), in einer Tabelle
- [ ] `organisatorisch` schließt ausdrücklich **Entwicklungs- und Prozessvorgaben** ein
      (Prozessstandards, Coding-Standards, Werkzeugpflichten)
- [ ] Die Überschneidung `technisch` ↔ `qualitaet` ist benannt statt verschwiegen, mit
      einer Faustregel, was wohin gehört
- [ ] Methodenglossar erklärt beide Begriffe in je zwei Zeilen
- [ ] Der Befund am eigenen Bestand ist als Wissensnotiz festgehalten: fünf von 25
      Anforderungen liegen dort, wo die Literatur sie nicht einordnen würde — die
      Kategorien tragen als Fragenliste, nicht als Klassifikation

## Kontext

- Entscheidung des Auftraggebers vom 2026-08-20: Kategorien schärfen, den vereinbarten
  Bestand **nicht** umsortieren
- Die Fehleinordnung deckt sich mit der dokumentierten LLM-Schwäche bei der Kategorisierung

## Agent

`claude-code` — Regeln, Glossar, Wissensnotiz.

## Abhängigkeiten

- keine

## Notizen

- Kein `/req-change`: Der Wortlaut keiner Anforderung ändert sich, nur die Erklärung der
  Kategorien. Das ist eine Präzisierung.
