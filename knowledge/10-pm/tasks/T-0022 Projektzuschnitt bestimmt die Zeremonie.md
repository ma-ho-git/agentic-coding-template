---
id: T-0022
title: Projektzuschnitt bestimmt die Zeremonie
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/meta, topic/agents]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0022 Projektzuschnitt bestimmt die Zeremonie

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — der Teil, der die Zeremonie an die Projektgröße anpasst.

## Ziel

Ein Wegwerfskript kostet nicht dieselbe Zeremonie wie ein Produkt.

## Akzeptanzkriterien

- [ ] `/bootstrap` klärt den Zuschnitt: Skript, Werkzeug oder Produkt
- [ ] Der Zuschnitt ist im Repository hinterlegt und für Skills und Hooks lesbar
- [ ] Ein kleiner Zuschnitt reduziert Pflichten nachvollziehbar — mit **protokollierter
      Begründung**, nicht durch stilles Abschalten
- [ ] Starre Leitplanken bleiben in **jedem** Zuschnitt aktiv; nur flexible und
      Dokumentationspflichten skalieren
- [ ] README erklärt die Zuschnitte in einer Tabelle

## Kontext

- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[Spec-Driven-Development - was andere Projekte machen]]

## Agent

`claude-code` — Skill, Konfiguration, Dokumentation.

## Abhängigkeiten

- [[T-0019 Leitplanken benennen und klassifizieren]]

## Notizen

- Wichtige Grenze: Proportionalität darf nie eine starre Leitplanke abschalten.
  Sonst wird der Zuschnitt zum Schlupfloch — genau das Risiko, das im Register unter
  „Regeln werden formal erfüllt, aber sinnentleert" steht.
- Keines der Fremdprojekte kennt Proportionalität; hier gibt es keine Vorlage zum Abschauen.
