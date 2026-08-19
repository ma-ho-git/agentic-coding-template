---
id: T-0008
title: Schreibzugriff auf das GitHub-Repo
type: task
status: done
priority: hoch
agent: cowork
owner: marcus
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta, stack/github]
related: ["[[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]"]
---

# T-0008 Schreibzugriff auf das GitHub-Repo

## Ziel

Der Agent kann Änderungen direkt nach `ma-ho-git/agentic-coding-template` pushen.

## Akzeptanzkriterien

- [x] `git push` auf einen Branch des Repos gelingt aus der Session heraus
- [x] Der Weg ist in der Wissensdatenbank dokumentiert, damit er reproduzierbar ist

## Kontext

- [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]

## Agent

`cowork` — nur der Mensch kann die Freigabe in der Oberfläche erteilen.

## Abhängigkeiten

- keine

## Notizen

- Lesen funktioniert bereits (öffentliches Repo, kein Credential nötig)
- Rückfallweg: Auslieferung als ZIP, Push durch den Nutzer lokal
- **2026-08-19, verifiziert:** `git push -u origin claude/vibe-coding-template-kb-03odfw`
  gelang direkt aus dieser Claude-Code-Cloud-Session (nicht Cowork — Git-Operationen sind
  laut Routing-Tabelle in `CLAUDE.md` §6 ohnehin Claude-Code-Aufgabe, nicht Cowork-Aufgabe).
  Ursache: das Repo war der Session bereits als Source zugeordnet, mit fest zugewiesenem
  Push-Branch — genau der in [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]
  beschriebene Lösungsweg war bereits vollzogen. Nicht separat verifiziert: ob eine
  Cowork-Session (die laut `agent`-Feld ursprünglich vorgesehen war) ebenfalls Zugriff hat —
  Cowork macht laut Routing-Tabelle keine Git-Operationen, daher für den eigentlichen Zweck
  dieser Task (Agent kann pushen) nicht relevant.
