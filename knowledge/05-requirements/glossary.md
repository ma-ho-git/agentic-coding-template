---
title: Glossar
aliases: ["Glossar", "glossary"]
type: knowledge
tags: [topic/requirements]
status: active
created: 2026-08-19
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Projektvision]]", "[[Konventionen der Wissensdatenbank]]", "[[00-index]]"]
---

# Glossar

> **Für ein eigenes Projekt:** Begriffe durch die eigene Fachdomäne ersetzen. Die Einträge
> hier sind das Vokabular **dieses Templates** und zugleich ein ausgefülltes Beispiel.

## Kurz

Das verbindliche Vokabular. Kein Beiwerk: die Coderegel „Namen aus maximal drei Wörtern, für
Menschen aussagekräftig" ist nur einlösbar, wenn feststeht, wie die Dinge heißen.

**Regel:** Ein Begriff, eine Schreibweise, im Gespräch wie im Code.

Die Begriffe des *Verfahrens* — Anforderung, Rahmen, Startgate, ADR — stehen nicht hier,
sondern im [[Methodenglossar]].

## Begriffe

| Begriff | Bedeutung | Im Code | Nicht verwenden |
| --- | --- | --- | --- |
| Anforderung | Was das System leisten oder einhalten muss, mit Quelle, Begründung und prüfbarer Abnahme | `requirement`, `REQ-XXXX` | Feature, Story, Wunsch |
| Rahmen | Die vor dem ersten Code zu klärende Anforderungsebene | `ebene: rahmen`, `baseline` | Lastenheft, Spezifikation |
| Startgate | Die Freigabe in `baseline.md`, ab der entwickelt werden darf | `baseline_status` | Meilenstein, Freigabe |
| Aufgabe | Eine Arbeitseinheit mit Akzeptanzkriterien, die eine Anforderung erfüllt | `task`, `T-XXXX` | Ticket, Issue, Item |
| Lane | Eine Spalte des Boards; der Aufgabenstand | `Backlog`, `Ready`, `Doing`, `Review`, `Done` | Spalte, Status-Bucket |
| Contract-Kommentar | Der `@contract`-Block am Dateianfang, der den Wirkungsradius lesbar macht | `@contract` | Header, Docblock |
| Wirkungsradius | Die Menge der von einer Änderung betroffenen Codestellen | `consumers`, `depends-on` | Impact, Blast Radius |
| Regel | Verbindliche Vorgabe unter `.claude/rules/` | `rule` | Guideline, Konvention |
| Hook | Skript, das eine Regel maschinell durchsetzt | `hook` | Check, Validator |
| Skill | Aufrufbarer Ablauf unter `.claude/skills/` | `skill`, `/name` | Command, Makro |
| Stack-Profil | Die Datei, die Testlauf, Linter und Doku-Standard des Projekts benennt | `stacks/active.md` | Toolchain, Setup |

## Abgrenzungen

- **Anforderung vs. Aufgabe:** die Anforderung sagt, *was* gelten muss und warum; die Aufgabe
  sagt, *was getan wird*, um sie zu erfüllen. Eine Anforderung überlebt viele Aufgaben.
- **Anforderung vs. Randbedingung:** eine Anforderung ist zu erfüllen; eine Randbedingung
  steht ohnehin fest und schneidet nur den Lösungsraum.
- **Rahmen vs. Detail:** Rahmen prägt die Architektur und steht vor dem Code; Detail wird je
  Entwicklungsstufe erhoben und darf beim Codieren nachgeschärft werden.
- **Regel vs. Skill:** eine Regel gilt immer und wird geprüft; ein Skill wird aufgerufen.
- **Präzisierung vs. Änderung:** dieselbe Aussage genauer ist eine Präzisierung; eine andere
  Aussage ist eine Änderung und läuft über `/req-change`.

## Offene Fragen

- keine
