---
id: T-0030
title: Funktional und nicht-funktional benennen
type: task
implements: ["[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/meta]
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[T-0031 Qualitätsmerkmale vollständig abfragen]]", "[[Funktionale und nicht-funktionale Anforderungen]]"]
---

# T-0030 Funktional und nicht-funktional benennen

## Anforderung

[[REQ-0017 Anforderungserhebung vor der Entwicklung]] — Präzisierung vom 2026-08-20.

## Ziel

Die Unterscheidung funktional / nicht-funktional ist der Grundbegriff der
Anforderungserhebung. Im Projekt kommt sie nirgends vor.

## Akzeptanzkriterien

- [x] `.claude/rules/requirements.md` benennt beide Arten und sagt, **warum sie
      unterschiedlich erhoben werden**: funktionale erzählt der Nutzer von selbst,
      nicht-funktionale muss man gegen eine Liste abfragen
- [x] Unsere sechs Kategorien sind auf Sommervilles drei Gruppen abgebildet
      (Produkt / organisatorisch / extern), in einer Tabelle
- [x] `organisatorisch` schließt ausdrücklich **Entwicklungs- und Prozessvorgaben** ein
      (Prozessstandards, Coding-Standards, Werkzeugpflichten)
- [x] Die Überschneidung `technisch` ↔ `qualitaet` ist benannt statt verschwiegen, mit
      einer Faustregel, was wohin gehört
- [x] Methodenglossar erklärt beide Begriffe in je zwei Zeilen
- [x] Der Befund am eigenen Bestand ist als Wissensnotiz festgehalten: fünf von 25
      Anforderungen liegen dort, wo die Literatur sie nicht einordnen würde — die
      Kategorien tragen als Fragenliste, nicht als Klassifikation

## Ergebnis

- `.claude/rules/requirements.md` hat einen eigenen Abschnitt: beide Arten benannt, und
  **warum sie unterschiedlich erhoben werden** — funktionale erzählt der Nutzer von selbst,
  ein Szenario besteht fast nur daraus; nicht-funktionale erzählt er nie, sie erscheinen nur,
  wenn man sie gegen eine Liste abfragt. Genau dafür gibt es die sechs Kategorien.
- Zweiter Unterschied ergänzt: eine funktionale Anforderung ist meist prüfbar, wie sie
  dasteht — eine nicht-funktionale fast nie, bis sie eine Zahl trägt. Die Prüfbarkeitsregel
  existiert also im Wesentlichen für die fünf nicht-funktionalen Kategorien.
- Kategorientabelle um die Sommerville-Spalte erweitert: Produkt, organisatorisch, extern.
- `organisatorisch` schließt jetzt ausdrücklich **Entwicklungs- und Prozessvorgaben** ein.
- Die Überschneidung `technisch` ↔ `qualitaet` ↔ `organisatorisch` ist benannt statt
  verschwiegen, mit Faustregel: worauf es läuft / wie gut es das tut / wie das Team arbeitet.
  Dazu der Satz, der die Kategorien richtig einordnet: **Prüfliste für Vollständigkeit, keine
  Taxonomie.** Eine Anforderung eine Kategorie daneben ist kein Fehler; eine Kategorie, die
  niemand gefragt hat, schon.
- Methodenglossar erklärt beide Begriffe anfängertauglich; `/req-elicit` nennt die
  Unterscheidung an der Stelle, an der die Kategorien abgefragt werden.
- Wissensnotiz [[Funktionale und nicht-funktionale Anforderungen]] hält Recherche und Befund
  fest — samt der Einschränkung, dass der Egress-Proxy jeden Abruf einer Primärquelle
  blockiert hat und die Angaben aus übereinstimmenden Suchzusammenfassungen stammen.
- **Der Befund steht drin, nicht nur die Regel:** fünf von 25 Anforderungen liegen dort, wo
  die Literatur sie nicht einordnen würde; die Fehleinordnung stammt vom Agenten und deckt
  sich exakt mit der dokumentierten LLM-Schwäche bei der Kategorisierung. Dokumentiert ist
  auch die Nebenwirkung: `/req-validate` sieht `technisch` als belegt an, obwohl dieses
  Projekt kaum echte technische Anforderungen erhoben hat.

Suite 106 grün (unverändert — Regeln, Glossar, Skill, Notiz), `check_vault.py` und
`check_traceability.py` ohne Befund.

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
