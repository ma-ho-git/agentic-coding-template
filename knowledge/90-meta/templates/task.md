---
id: T-XXXX
title: <Kurzer Titel>
type: task
implements: ["[[REQ-XXXX Titel]]"]   # mindestens eine vereinbarte Anforderung
infrastruktur:           # nur wenn implements leer: Begründung, warum kein Fachbezug
status: backlog          # backlog | ready | doing | review | done
priority: mittel         # hoch | mittel | niedrig
agent: claude-code       # claude-code | cowork
owner:                   # leer bis beansprucht
created: JJJJ-MM-TT
started:
finished:
tags: [topic/<bereich>]
related: []
---

# T-XXXX <Kurzer Titel>

## Anforderung

<Welche Anforderung wird damit erfüllt, und welcher Teil davon?
 Bei Infrastrukturaufgaben: warum es keine gibt.>

## Ziel

<Ein Satz: was ist danach wahr, was vorher nicht wahr war.>

## Akzeptanzkriterien

- [ ] <prüfbar formuliert — wie würde man es verifizieren?>
- [ ] <...>

## Kontext

- <Wikilinks auf ADRs, Wissensnotizen, verwandte Tasks — mindestens einer>

## Agent

`claude-code` — <halber Satz Begründung, Routing-Tabelle: CLAUDE.md §6>

## Abhängigkeiten

- <blockierende Tasks als Wikilinks, oder "keine">

## Notizen

<Verlauf, Entscheidungen, Sackgassen — während der Arbeit ergänzen>
