---
id: T-0032
title: Artefakttyp bestimmt die Beispiele
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[T-0031 Qualitätsmerkmale vollständig abfragen]]", "[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
---

# T-0032 Artefakttyp bestimmt die Beispiele

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — Präzisierung vom 2026-08-20.

## Ziel

`/req-elicit` fragt als Erstes nach dem Artefakttyp — und benutzt danach für alle
dieselbe Beispielspalte „Kommandozeilenwerkzeug". Ein Anfänger kann ein CLI-Beispiel
nicht auf seinen Dienst übertragen; genau das ist ja seine Lücke.

## Akzeptanzkriterien

- [ ] Wissensnotiz mit einem Profil je Artefakttyp: Bibliothek, Kommandozeilenwerkzeug,
      Dienst/API, Datenstrecke, Anwendung mit Oberfläche, Wegwerfskript
- [ ] Je Profil: die drei bis fünf Qualitätsmerkmale, die dort tatsächlich entscheiden,
      je mit einer messbaren Beispielanforderung
- [ ] `/req-elicit` wählt seine Beispiele nach dem genannten Artefakttyp
- [ ] **Die Fragenliste bleibt in jedem Fall gleich** — artefaktabhängig sind Beispiele,
      Messgrößen und die Tiefe, nie der Umfang der Prüfung
- [ ] Unbekannter oder gemischter Typ: alle Profile anbieten statt raten

## Kontext

- ISO 25010 ist ausdrücklich zum Zuschneiden gedacht; welche Merkmale zählen, hängt vom
  System ab
- Gleiche Bauform wie der Projektzuschnitt: die Prüfung skaliert nie, nur die Antwort

## Agent

`claude-code` für den Einbau. Die Recherche je Artefakttyp gehört zu `researcher` oder
Cowork — in dieser Sitzung blockierte der Egress-Proxy jeden Seitenabruf.

## Abhängigkeiten

- [[T-0031 Qualitätsmerkmale vollständig abfragen]]

## Notizen

- Die Profile sind eine Vorauswahl, kein Gesetz. Sie sollen dem Nutzer das Übertragen
  abnehmen, nicht ihm vorschreiben, was ihm wichtig zu sein hat.
