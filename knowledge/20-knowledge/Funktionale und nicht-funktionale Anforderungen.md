---
title: Funktionale und nicht-funktionale Anforderungen
type: knowledge
tags: [topic/requirements]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Sommerville Software Engineering - was das Template übernimmt]]", "[[Rahmen und Startgate]]", "[[00-index]]"]
---

# Funktionale und nicht-funktionale Anforderungen

## Kurz

Warum die beiden Arten unterschiedlich erhoben werden müssen, wie unsere sechs Kategorien
dazu stehen, und was die Prüfung des eigenen Bestands ergeben hat. Nachschlagen, bevor die
Kategorienliste angefasst wird.

> **Belastbarkeit:** Bei der Recherche am 2026-08-20 hat der Egress-Proxy dieser Umgebung
> **jeden** Seitenabruf blockiert. Die Angaben stammen aus Suchmaschinen-Zusammenfassungen
> mehrerer unabhängiger Seiten, die übereinstimmen — nicht aus abgerufenen Primärquellen.
> Vor einer Verwendung, an der etwas hängt, an der Norm gegenprüfen.

## Kernpunkte

- **Funktional** = was das System können muss. **Nicht-funktional** = wie gut, unter welchen
  Bedingungen, unter welchen Regeln.
- Die Erhebung ist **asymmetrisch**: Funktionale erzählt der Nutzer von selbst, ein Szenario
  besteht fast nur daraus. Nicht-funktionale erzählt er nie — sie erscheinen nur, wenn man
  sie **gegen eine Liste** abfragt.
- Zweiter Unterschied: Eine funktionale Anforderung ist meist prüfbar, wie sie dasteht. Eine
  nicht-funktionale ist es fast nie, bis sie eine Zahl oder ein beobachtbares Szenario trägt.
- Sommerville teilt die nicht-funktionalen in drei Gruppen: **Produkt** (Verhalten des
  Ergebnisses), **organisatorisch** (Hausregeln, inkl. Entwicklungsprozess und
  Coding-Standards), **extern** (Regulierung, Gesetz, Interoperabilität).
- ISO/IEC 25010:2023 nennt neun Produktqualitätsmerkmale: funktionale Eignung,
  Leistungseffizienz, Kompatibilität, Interaktionsfähigkeit, Zuverlässigkeit, Sicherheit,
  Wartbarkeit, Flexibilität, **Safety**. Gegenüber 2011: Safety neu, *Usability* →
  *Interaction Capability*, *Portability* → *Flexibility*.
- Die Norm ist **zum Zuschneiden gedacht**. Welche Merkmale zählen, hängt vom System ab.
- Standardwerkzeug für Messbarkeit ist das Qualitätsszenario aus ATAM:
  **Auslöser → erwartete Reaktion → Messgröße.**
- KI-Befund aus der Literatur: LLMs können nicht-funktionale Anforderungen **aus funktionalen
  ableiten** — genau das, was Menschen vergessen. Dokumentierte Schwäche: Mehrdeutigkeit und
  die **korrekte Einordnung in Kategorien**.

## Details — unsere sechs Kategorien

| Kategorie | Art | Sommerville-Gruppe |
| --- | --- | --- |
| `funktional` | funktional | — |
| `technisch` | nicht-funktional | Produkt |
| `qualitaet` | nicht-funktional | Produkt |
| `sicherheit` | nicht-funktional | Produkt + extern |
| `organisatorisch` | nicht-funktional | organisatorisch |
| `recht` | nicht-funktional | extern |

Fünf der sechs Kategorien sind also nicht-funktional. Das ist kein Zufall, sondern die
Bauform: Die Liste existiert, weil nicht-funktionale Anforderungen sonst durchfallen.

## Details — Befund am eigenen Bestand (2026-08-20)

Prüfung der 25 Rahmenanforderungen dieses Repositories gegen die Literatur:

- **8 von 25** liegen unter `qualitaet` — der größte Topf. Typisches Symptom eines
  Sammelbeckens.
- **REQ-0006** (TDD), **REQ-0007** (Größengrenzen), **REQ-0008** (Contract-Kommentar) stehen
  unter `qualitaet`, sind nach Sommerville aber **Entwicklungsanforderungen** — organisatorisch.
- **REQ-0011** (Durchsetzung), **REQ-0016** (Doku-Standard je Sprache) stehen unter
  `technisch`, sind ebenfalls Prozessvorgaben.

**Schlussfolgerung, nicht Korrektur:** Die sechs Kategorien tragen als **Fragenliste**, nicht
als **Klassifikation**. Der Auftraggeber hat am 2026-08-20 entschieden, die Beschreibungen zu
schärfen und den vereinbarten Bestand nicht umzusortieren — eine Umsortierung von fünf gerade
bestätigten Anforderungen kostet mehr Vertrauen, als die sauberere Ablage bringt.

**Nebenwirkung, die man kennen muss:** `/req-validate` prüft „hat jede Kategorie eine
Anforderung?". `technisch` sieht durch REQ-0011 und REQ-0016 belegt aus, obwohl dieses Projekt
kaum echte technische Anforderungen erhoben hat. Die Prüfung geht durch — aus dem falschen
Grund. Wer die Kategorienabdeckung ernst nimmt, liest sie inhaltlich nach.

**Und:** Die Fehleinordnung stammt vom Agenten und deckt sich exakt mit der in der Literatur
beschriebenen LLM-Schwäche. Ein Grund mehr, die Kategorie nicht als Wahrheit zu lesen.

## Quellen

Alle am 2026-08-20 über die Suche ermittelt, **keine davon abrufbar** (Egress-Proxy):

- ISO/IEC 25010:2023, offizielle Beschreibung — https://www.iso.org/standard/78176.html
- ISO 25010 erklärt, neun Merkmale — https://www.sonarsource.com/resources/library/iso-iec-25010-explained/
- ISO 25010 Merkmale und Untermerkmale — https://iso25000.com/en/iso-25000-standards/iso-25010
- arc42 Qualitätsmodell zu ISO 25010 — https://quality.arc42.org/standards/iso-25010
- Zuschnitt der Norm auf das eigene System — https://blog.codacy.com/iso-25010-software-quality-model
- Sommerville, Kapitel Software Requirements (Vorlesungsfolien) — https://www.khoury.northeastern.edu/home/lieber/com3205/f02/lectures/sommerville/ch05.ppt
- ATAM und Utility Tree — https://www.geeksforgeeks.org/software-engineering/architecture-tradeoff-analysis-method-atam/
- Qualitätsszenario, Form Auslöser/Reaktion/Messgröße — https://dzone.com/articles/what-heck-utility-tree
- Übersicht zu automatischer NFR-Erzeugung mit LLMs — https://www.themoonlight.io/en/review/automated-non-functional-requirements-generation-in-software-engineering-with-large-language-models-a-comparative-study
- Leitfaden zur NFR-Erhebung — https://microsoft.github.io/code-with-engineering-playbook/design/design-patterns/non-functional-requirements-capture-guide/
