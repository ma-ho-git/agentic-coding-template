---
title: Rahmen und Startgate
aliases: ["Rahmen und Startgate", "baseline"]
type: knowledge
tags: [topic/requirements]
status: active
baseline_status: entwurf
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Projektvision]]", "[[00-index]]"]
---

# Rahmen und Startgate

> **Diese Datei entscheidet, ob entwickelt werden darf.**
> Solange `baseline_status: entwurf` steht, wird kein Produktivcode geschrieben.
> Nur der Mensch setzt sie auf `vereinbart` — ein Agent schlägt vor, er bescheinigt sich nichts selbst.

## Kurz

Der Rahmen beantwortet: *Was wird gebaut, und was muss dabei gelten?* Er muss vollständig
sein, bevor die Entwicklung beginnt — nicht weil Vorab-Spezifikation Selbstzweck wäre,
sondern weil eine spät entdeckte Rahmenanforderung fertige Arbeit entwertet.

Vollständig heißt: **jede** der sechs Kategorien unten ist entweder mit mindestens einer
vereinbarten Rahmenanforderung belegt **oder** ausdrücklich als nicht zutreffend begründet.

Regeln: `.claude/rules/requirements.md`. Entscheidung:
[[ADR-0005 Anforderungen als Pflicht vor dem Code]].

## Zielartefakt

<Ein bis drei Sätze: was genau entsteht hier? Siehe [[Projektvision]] für das Warum.>

*Beim Projektstart ausfüllen — `/req-elicit` führt durch die Fragen.*

## Kategorien

Je Kategorie: Wikilinks auf die Rahmenanforderungen **oder** eine Begründung,
warum sie hier nicht greift. Ein leerer Abschnitt ist ein offener Punkt, keine Antwort.

### Funktional

*Kernleistung des Systems, grob. Was muss es können, damit es überhaupt seinen Zweck erfüllt?*

- <offen>

### Technisch

*Plattform, Schnittstellen, Datenhaltung, Performanz, Zielumgebung.*

- <offen>

### Organisatorisch

*Betrieb, Rollen, Auslieferung, Prozessvorgaben, Zusammenarbeit.*

- <offen>

### Sicherheit

*Schutzbedarf, Authentisierung, Autorisierung, Datenschutz, Geheimnisverwaltung.*

- <offen>

### Recht

*Regulierung, Lizenzen, Aufbewahrungsfristen, Nutzungsrechte an Ergebnissen.*

- <offen>

### Qualität

*Bedienbarkeit, Zuverlässigkeit, Wartbarkeit — soweit über die generellen Coderegeln hinaus.*

- <offen>

## Freigabe

| Feld | Wert |
| --- | --- |
| Rahmen vollständig geprüft am | — |
| Freigegeben durch | — |
| Bemerkungen | — |

Nach der Freigabe `baseline_status` auf `vereinbart` setzen. Ab dann gilt für neue
Erkenntnisse: Rahmenanforderungen ändern sich nur über `/req-change`, nicht durch stilles
Überschreiben.
