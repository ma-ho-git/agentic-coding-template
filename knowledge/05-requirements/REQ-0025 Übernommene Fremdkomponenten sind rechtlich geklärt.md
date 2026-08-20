---
title: Übernommene Fremdkomponenten sind rechtlich geklärt
type: requirement
ebene: rahmen
kategorie: recht
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20
nachweis: test
status: vereinbart
tasks: ["[[T-0029 Fremdkomponenten rechtlich absichern]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]", "[[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]", "[[Rahmen und Startgate]]"]
---

# REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt

## Anforderung

Wird eine Ausgangsbasis ausgewählt, muss die Entwicklung darauf aufsetzen, sofern es
rechtlich zulässig ist. Die daraus folgenden Pflichten sind zu dokumentieren und im Projekt
zu erfüllen.

## Begründung

Eine Lizenz, die erst beim Ausliefern auffällt, entwertet die gesamte darauf gebaute Arbeit:
Copyleft kann die eigene Weitergabe erzwingen oder unmöglich machen, Namensnennungspflichten
lassen sich nachträglich nur mit einem neuen Release erfüllen. Das ist der klassische
unheilbare Fall — der Code ist dann schon geschrieben.

Der Nutzer, für den dieses Template gedacht ist, kennt den Unterschied zwischen MIT, Apache
und GPL in der Regel nicht. Er muss ihn auch nicht kennen; der Agent muss ihn prüfen.

## Abnahme

- Vor der Übernahme wird die Lizenz gegen die Weitergabeabsicht des Projekts geprüft (die
  `recht`-Kategorie des Rahmens). Das Ergebnis steht in einem ADR — bei Unvereinbarkeit
  einschließlich des Ablehnungsgrunds.
- Ein Register der Fremdkomponenten führt je Eintrag: Komponente, Version, Lizenz, Pflichten
  (Namensnennung, Lizenztext beilegen, Quelloffenlegung, Änderungshinweis), Quelle mit
  Abrufdatum.
- Die Pflichten sind im Repository **erfüllt**, nicht nur notiert: Lizenztexte liegen bei,
  Namensnennung steht dort, wo sie verlangt wird.
- Eine Prüfung meldet jede registrierte Komponente, deren Lizenztext im Repository fehlt.

## Präzisierungen

- keine

## Offene Fragen

- keine
