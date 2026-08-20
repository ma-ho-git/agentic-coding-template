---
id: T-0021
title: Anfängermodus für die Anforderungserhebung
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, topic/agents]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0021 Anfängermodus für die Anforderungserhebung

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — der Teil, der die Erhebung für Menschen ohne Vorerfahrung bedienbar macht.

## Ziel

Ein Anfänger kann die Anforderungserhebung durchlaufen, ohne die Fachbegriffe vorher zu kennen.

## Akzeptanzkriterien

- [ ] `/req-elicit` erklärt jede der sechs Kategorien in einem Satz mit Beispiel
- [ ] Der Skill macht Vorschläge nach Projekttyp, statt nur zu fragen
- [ ] „Weiß ich nicht" erzeugt eine offene Frage in der Anforderung, niemals eine erfundene
- [ ] Methoden-Glossar unter `knowledge/05-requirements/` erklärt Anforderung, Rahmen,
      Startgate, ADR, Contract, Rückverfolgbarkeit in je zwei Zeilen
- [ ] `/req-validate` sagt beim Gate-Urteil, was fehlt und was der Nutzer konkret tun soll

## Kontext

- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[Spec-Driven-Development - was andere Projekte machen]]

## Agent

`claude-code` — Skill-Dateien und eine Vault-Notiz.

## Abhängigkeiten

- [[T-0019 Leitplanken benennen und klassifizieren]]

## Notizen

- Größte Zielgruppen-Lücke: keines der untersuchten Fremdprojekte adressiert
  unerfahrene Anwender, siehe [[Spec-Driven-Development - was andere Projekte machen]].
- Das bestehende Glossar erklärt die Fachdomäne, nicht die Methode. Beides wird gebraucht.
