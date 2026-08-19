---
id: T-0008
title: Schreibzugriff auf das GitHub-Repo
type: task
status: doing
priority: hoch
agent: cowork
owner: marcus
created: 2026-08-19
started: 2026-08-19
finished:
tags: [topic/meta, stack/github]
related: ["[[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]"]
---

# T-0008 Schreibzugriff auf das GitHub-Repo

## Ziel

Der Agent kann Änderungen direkt nach `ma-ho-git/agentic-coding-template` pushen.

## Akzeptanzkriterien

- [ ] `git push` auf einen Branch des Repos gelingt aus der Session heraus
- [ ] Der Weg ist in der Wissensdatenbank dokumentiert, damit er reproduzierbar ist

## Kontext

- [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]

## Agent

`cowork` — nur der Mensch kann die Freigabe in der Oberfläche erteilen.

## Abhängigkeiten

- keine

## Notizen

- Lesen funktioniert bereits (öffentliches Repo, kein Credential nötig)
- Rückfallweg: Auslieferung als ZIP, Push durch den Nutzer lokal
