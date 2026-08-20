---
title: Für unerfahrene Anwender nutzbar
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20 — "[[Szenario]]"
nachweis: demo
status: vereinbart
tasks: ["[[T-0021 Anfängermodus für die Anforderungserhebung]]", "[[T-0022 Projektzuschnitt bestimmt die Zeremonie]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]", "[[Projektvision]]"]
---

# REQ-0020 Für unerfahrene Anwender nutzbar

## Anforderung

Das Template muss einen Software-Engineering-Ansatz mit KI-Agenten auch für **unerfahrene
Anwender** ermöglichen. Es darf nicht voraussetzen, dass der Nutzer Anforderungen, Architektur
oder Qualitätsmaße bereits beurteilen kann.

## Begründung

Der Ansatz verlangt vom Menschen genau die Entscheidungen, die er am wenigsten delegieren
kann — Umfang, Freigabe, Zielkonflikte. Wer diese Begriffe nicht kennt, kann sie nicht
treffen und bricht ab. Ein Verfahren, das nur Erfahrene bedienen können, verfehlt den Zweck:
gerade Unerfahrene brauchen die Leitplanken am dringendsten.

## Abnahme

- `/req-elicit` erklärt jede Anforderungskategorie in einem Satz mit Beispiel und macht
  Vorschläge nach Projekttyp, statt nur zu fragen
- „Weiß ich nicht" ist eine zulässige Antwort und erzeugt eine offene Frage, **niemals** eine
  erfundene Anforderung
- Ein Methoden-Glossar erklärt die Begriffe des Verfahrens (Anforderung, Rahmen, Startgate,
  ADR, Contract, Rückverfolgbarkeit) in je zwei Zeilen
- Der Projektzuschnitt wird beim Bootstrap geklärt; ein kleiner Zuschnitt verringert
  Dokumentationspflicht und Erhebungstiefe — mit protokollierter Begründung — und schaltet
  niemals eine starre Leitplanke ab
- Jede Meldung einer Leitplanke nennt ihre Klasse, damit erkennbar ist, was verhandelbar ist

## Herkunft

[[Szenario]], Abschnitt „Wer und wann":

> Ausdrücklich auch Anwender ohne Erfahrung in Softwareentwicklung.

## Präzisierungen

- keine

## Offene Fragen

- Wie wird „unerfahren" nachgewiesen? Ein Test mit echten Anfängern steht aus; die Abnahme
  prüft bis dahin nur die Vorkehrungen, nicht ihre Wirkung.
