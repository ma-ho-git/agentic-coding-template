---
id: T-0016
title: Architekturschritt aus Qualitätsanforderungen
type: task
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Sommerville Software Engineering - was das Template übernimmt]]"]
---

# T-0016 Architekturschritt aus Qualitätsanforderungen

## Ziel

Architekturentscheidungen entstehen aus den Qualitätsanforderungen, nicht nebenbei.

## Akzeptanzkriterien

- [ ] `/architecture` existiert: liest die Qualitätsanforderungen, benennt die
      Zielkonflikte zwischen ihnen, schlägt ein Architekturmuster vor und schreibt das
      Ergebnis als ADR
- [ ] Der Skill kennt Sommervilles Grundkonflikte (Performanz gegen Wartbarkeit,
      Sicherheit gegen Performanz, Verfügbarkeit gegen Einfachheit) und zwingt zu einer
      benannten Abwägung statt zu einer Wunschliste
- [ ] Das erzeugte ADR verlinkt die Qualitätsanforderungen, aus denen es folgt —
      beidseitig
- [ ] `.claude/rules/code-quality.md` verweist für die Musterwahl auf diesen Schritt,
      statt die Patternliste doppelt zu führen

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[Sommerville Software Engineering - was das Template übernimmt]] — Kapitel 6

## Agent

`claude-code` — Skill-Datei und Regelanpassung.

## Abhängigkeiten

- [[T-0012 Anforderungsregeln und Vault-Struktur]]

## Notizen

- Bewusst leichtgewichtig: kein eigenes Architekturdokument, ein ADR je Entscheidung.
  Die ADR-Struktur existiert bereits und hat sich bewährt.
- Systemmodellierung (Sommerville Kap. 5) bleibt außen vor, siehe Abgrenzung in der
  Wissensnotiz.
