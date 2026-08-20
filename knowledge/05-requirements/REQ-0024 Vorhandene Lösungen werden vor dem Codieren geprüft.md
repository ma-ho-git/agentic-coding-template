---
title: Vorhandene Lösungen werden vor dem Codieren geprüft
type: requirement
ebene: rahmen
kategorie: organisatorisch
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20
nachweis: review
status: entwurf
tasks: ["[[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]", "[[T-0028 Startgate verlangt die Fremdlösungs-Entscheidung]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[REQ-0017 Anforderungserhebung vor der Entwicklung]]", "[[REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt]]", "[[Rahmen und Startgate]]"]
---

# REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft

## Anforderung

Nach der Erhebungsphase und vor der Coding-Phase muss der Agent anbieten, nach bestehenden
Lösungen — Open Source, Frameworks, Bibliotheken — zu suchen, die als Ausgangsbasis dienen
können, und je Kandidat ausweisen, welche Anforderungen er bereits erfüllt.

## Begründung

Die billigste Zeile Code ist die, die jemand anderes schon geschrieben und gewartet hat. Ein
Agent schreibt bereitwillig alles selbst, weil ihn das Schreiben nichts kostet — das Projekt
zahlt trotzdem, spätestens bei der Wartung.

Der Zeitpunkt ist nicht beliebig: Vorher sind die Anforderungen nicht bekannt, an denen ein
Kandidat gemessen werden müsste. Später steht der Eigenbau schon da, und dann gewinnt er,
weil er schon da ist — nicht weil er besser wäre.

Angeboten, nicht erzwungen: Ob eine Fremdbasis in Frage kommt, entscheidet der Nutzer.

## Abnahme

- Das Angebot erfolgt, sobald der Rahmen vereinbart ist, und vor der ersten Codeaufgabe.
  Die Entscheidung des Nutzers — suchen oder nicht — wird im Repository festgehalten, samt
  Begründung.
- Je Kandidat ausgewiesen: Quelle mit Abrufdatum, Lizenz, Wartungsstand (letzte Aktivität),
  und je Anforderung des Rahmens, ob der Kandidat sie erfüllt, teilweise erfüllt oder nicht
  erfüllt — mit REQ-ID.
- **Kein Kandidat ohne aufgerufene Quelle.** Eine aus dem Gedächtnis genannte Bibliothek ist
  kein Kandidat, sondern eine Behauptung.
- Ergebnis als Notiz in der Wissensdatenbank, die Auswahlentscheidung als ADR — auch dann,
  wenn die Entscheidung „nichts davon" lautet.

## Präzisierungen

- keine

## Offene Fragen

- keine
