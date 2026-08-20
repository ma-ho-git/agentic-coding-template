---
id: T-0019
title: Leitplanken benennen und klassifizieren
type: task
implements: ["[[REQ-0019 Leitplanken in zwei Klassen]]"]
status: doing
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished:
tags: [topic/agents, topic/meta]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0019 Leitplanken benennen und klassifizieren

## Anforderung

[[REQ-0019 Leitplanken in zwei Klassen]] — der Teil, der die beiden Klassen benennt, den Zuordnungstest liefert und die Klasse in jeder Meldung sichtbar macht.

## Ziel

Wer eine Regel liest oder eine Meldung sieht, erkennt sofort, ob sie verhandelbar ist.

## Akzeptanzkriterien

- [ ] `.claude/rules/guardrails.md` definiert beide Klassen und den vierteiligen
      Zuordnungstest aus dem ADR
- [ ] Jede bestehende Prüfung ist einer Klasse zugeordnet, dokumentiert in der Regeldatei
- [ ] Jede Hook-Meldung nennt ihre Klasse — blockierende als `[STARR]`, hinweisende als
      `[FLEXIBEL]`, mit Hinweis, dass eine Abweichung bei flexiblen im Code zu begründen ist
- [ ] `CLAUDE.md` nennt das Prinzip in den Nicht-Verhandelbaren
- [ ] `code-quality.md` weist seine Grenzen als flexibel aus
- [ ] Tests decken die neue Meldungsform ab, bestehende Tests bleiben grün

## Kontext

- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[Spec-Driven-Development - was andere Projekte machen]]

## Agent

`claude-code` — Regeldateien und Hook-Code.

## Abhängigkeiten

- keine

## Notizen

- Die Unterscheidung existiert seit [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]
  faktisch, war aber nie benannt. Hier wird sie zum Konzept.
- Sichtbarkeit ist kein Beiwerk: wer Wand und Hinweis nicht unterscheiden kann, behandelt
  am Ende beides als Rauschen.
