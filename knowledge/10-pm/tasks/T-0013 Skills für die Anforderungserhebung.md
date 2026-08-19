---
id: T-0013
title: Skills für die Anforderungserhebung
type: task
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/requirements, topic/agents]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]"]
---

# T-0013 Skills für die Anforderungserhebung

## Ziel

Ein Agent kann Anforderungen erheben, prüfen und ändern, ohne dass der Nutzer das Verfahren
erklären muss.

## Akzeptanzkriterien

- [ ] `/req-elicit` — führt das Interview mit dem Nutzer, schreibt Vision, Stakeholder,
      Glossar und die ersten `REQ-XXXX`-Dateien. Fragt nach, statt zu raten.
- [ ] `/req-validate` — führt Sommervilles fünf Prüfungen (Gültigkeit, Konsistenz,
      Vollständigkeit, Realismus, Prüfbarkeit) über den Anforderungsbestand aus und meldet
      je Fund die betroffene Anforderung
- [ ] `/req-change` — bei geänderter Anforderung: betroffene Tasks, Tests und Codestellen
      über die Traceability-Kette finden, sofort Machbares anpassen, den Rest als
      Folgeaufgabe in `Ready` anlegen
- [ ] Jeder Skill nennt in seiner `description`, wann er greift, und hält sich an die
      Struktur der bestehenden Skills
- [ ] `/req-elicit` erzeugt in einem Trockenlauf eine formal gültige Anforderungsdatei
      (gegen `tools/check_vault.py` geprüft)

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[T-0012 Anforderungsregeln und Vault-Struktur]]

## Agent

`claude-code` — Skill-Dateien im Repo.

## Abhängigkeiten

- [[T-0012 Anforderungsregeln und Vault-Struktur]]

## Notizen

- `/req-change` ist das Gegenstück zu `/contract-sync`, eine Ebene höher. Struktur von dort
  übernehmen, damit beide gleich zu lesen sind.
- `/req-elicit` ist der einzige Skill, der ausdrücklich Rückfragen an den Menschen stellen
  **soll** — Elicitation ohne Stakeholder ist Raten.
