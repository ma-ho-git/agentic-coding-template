---
title: Fehler- und Ausfallverhalten wird bewusst entschieden
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20
nachweis: review
status: entwurf
tasks: ["[[T-0025 Robustheit als Pflicht des Agenten]]", "[[T-0026 Verschluckte Ausnahmen sichtbar machen]]"]
tags: [topic/requirements, topic/code]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[REQ-0009 Kein Code mit bekannten Sicherheitslücken]]", "[[REQ-0006 Testgetriebene Entwicklung ist verpflichtend]]"]
---

# REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden

## Anforderung

Der Agent muss bei Entwurf, Code und Review wie ein erfahrener Entwickler auf Fehlerfälle,
Ausnahmen, Laufzeitverhalten und den Ausfall angebundener Systeme prüfen, diese Fälle
behandeln und die getroffene Behandlung sichtbar machen.

## Begründung

Genau hier trennt sich Produktionscode vom Prototyp — und genau hier fehlt einem
unerfahrenen Nutzer das Vorwissen, um danach zu fragen. Ein Agent, der nur den Gutfall baut,
liefert etwas, das in der Vorführung funktioniert und im Betrieb ausfällt; der Nutzer merkt
es erst dann. Die Verantwortung dafür kann nicht bei dem liegen, der die Frage nicht kennt —
sie liegt beim Agenten.

Abgrenzung: [[REQ-0009 Kein Code mit bekannten Sicherheitslücken]] deckt Angriffe ab. Hier
geht es um Fehler ohne Angreifer — kaputte Eingaben, abgestürzte Nachbarn,
Zeitüberschreitungen.

## Abnahme

- Eine Regeldatei benennt die zu prüfenden Klassen: Eingabe- und Grenzfälle, Ausnahmepfade,
  Laufzeit und Ressourcen (Zeitgrenzen, unbegrenztes Wachstum, Nebenläufigkeit) sowie
  Ausfall angebundener Systeme (nicht erreichbar, zu langsam, falsche Antwort).
- Die Erhebung fragt für **jedes** angebundene System, was bei dessen Ausfall geschehen
  soll, und hält die Antwort als Anforderung fest.
- Die Definition of Done verlangt je behandeltem Fehlerpfad des geänderten Codes mindestens
  einen Test, der ihn auslöst.
- Der `@contract`-Block nennt das Fehlerverhalten der Einheit unter `invariants:`.
- Der Review-Agent prüft die genannten Klassen als eigene Linse.
- Eine verschluckte Ausnahme (Fang ohne Behandlung) erzeugt einen Hinweis.

## Präzisierungen

- Der Umfang skaliert mit dem Projektzuschnitt: Ein `skript` ohne angebundene Systeme hat
  hier wenig zu entscheiden. Die **Frage** wird trotzdem gestellt — es skaliert die Antwort,
  nicht die Prüfung (`.claude/rules/workflow.md`).

## Offene Fragen

- keine
