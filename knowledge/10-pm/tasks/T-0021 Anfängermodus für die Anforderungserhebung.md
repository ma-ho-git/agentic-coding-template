---
id: T-0021
title: Anfängermodus für die Anforderungserhebung
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/agents]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0021 Anfängermodus für die Anforderungserhebung

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — der Teil, der die Erhebung für Menschen ohne Vorerfahrung bedienbar macht.

## Ziel

Ein Anfänger kann die Anforderungserhebung durchlaufen, ohne die Fachbegriffe vorher zu kennen.

## Akzeptanzkriterien

- [x] `/req-elicit` erklärt jede der sechs Kategorien in einem Satz mit Beispiel
- [x] Der Skill macht Vorschläge nach Projekttyp, statt nur zu fragen
- [x] „Weiß ich nicht" erzeugt eine offene Frage in der Anforderung, niemals eine erfundene
- [x] Methoden-Glossar unter `knowledge/05-requirements/` erklärt Anforderung, Rahmen,
      Startgate, ADR, Contract, Rückverfolgbarkeit in je zwei Zeilen
- [x] `/req-validate` sagt beim Gate-Urteil, was fehlt und was der Nutzer konkret tun soll

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

### 2026-08-20 umgesetzt

- **Kein Moduswechsel.** Erst als Frage geplant („Wie vertraut bist du mit Anforderungen?"),
  dann verworfen: Erklären kostet einen Erfahrenen eine überflogene Zeile, Nicht-Erklären
  kostet einen Anfänger das ganze Verfahren. Der Skill erklärt jetzt immer — ein bewegliches
  Teil weniger.
- Vier Haltungsregeln im Skill, in dieser Reihenfolge wirksam:
  1. **Erklären, dann fragen** — je Kategorie ein Satz plus Beispiel aus einem Projekt der
     gleichen Art. Dafür fragt der Skill zuerst, *was* gebaut wird.
  2. **Vorschlagen statt verhören** — zwei bis drei plausible Anforderungen zur Korrektur
     anbieten. Einen falschen Vorschlag abzulehnen ist ungleich leichter, als aus dem
     Nichts zu erfinden, und legt offen, was wirklich gemeint war.
  3. **„Weiß ich nicht" ist zulässig** und erzeugt eine offene Frage, nie eine erfundene
     Anforderung. Ausdrücklich als schlimmstmögliches Ergebnis benannt: eine erfundene
     Anforderung, die aussieht wie vereinbart.
  4. **Eine Frage auf einmal**, wenn der Nutzer unsicher ist. Sechs Fragen am Stück lesen
     sich wie eine Prüfung.
- Kategorientabelle mit Ein-Satz-Erklärung und Beispiel je Kategorie; ausdrücklich bleibt es
  dabei, dass **jede** Kategorie gefragt wird — „für ein Wegwerfskript brauche ich nichts"
  ist eine gute Begründung, muss aber hingeschrieben werden.
- `methodenglossar.md` erklärt die Begriffe des Verfahrens in je zwei Zeilen, abgegrenzt vom
  bestehenden Fachglossar. Beide verlinken aufeinander, damit niemand im falschen sucht.
- `/req-validate` nennt beim Gate-Urteil nicht mehr nur die Lücke, sondern die eine Handlung,
  die sie schließt — mit Beispielausgabe im Skill.
- Nicht enthalten, absichtlich: die Zeremonie nach Projektgröße abzustufen. Das ist
  [[T-0022 Projektzuschnitt bestimmt die Zeremonie]]; hier wäre es Vermischung zweier Fragen.
