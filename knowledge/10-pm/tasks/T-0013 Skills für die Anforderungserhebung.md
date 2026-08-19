---
id: T-0013
title: Skills für die Anforderungserhebung
type: task
implements: []
infrastruktur: Aufbau der Anforderungsebene selbst - kann sich nicht auf eine Anforderung stützen, die es noch nicht gibt
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/requirements, topic/agents]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]"]
---

# T-0013 Skills für die Anforderungserhebung

## Ziel

Ein Agent kann Anforderungen erheben, prüfen und ändern, ohne dass der Nutzer das Verfahren
erklären muss.

## Akzeptanzkriterien

- [x] `/req-elicit` — führt das Interview mit dem Nutzer, schreibt Vision, Stakeholder,
      Glossar und die ersten `REQ-XXXX`-Dateien. Fragt nach, statt zu raten.
- [x] `/req-validate` — führt Sommervilles fünf Prüfungen (Gültigkeit, Konsistenz,
      Vollständigkeit, Realismus, Prüfbarkeit) über den Anforderungsbestand aus und meldet
      je Fund die betroffene Anforderung
- [x] `/req-change` — bei geänderter Anforderung: betroffene Tasks, Tests und Codestellen
      über die Traceability-Kette finden, sofort Machbares anpassen, den Rest als
      Folgeaufgabe in `Ready` anlegen
- [x] Jeder Skill nennt in seiner `description`, wann er greift, und hält sich an die
      Struktur der bestehenden Skills
- [x] `/req-elicit` erzeugt in einem Trockenlauf eine formal gültige Anforderungsdatei
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
- **2026-08-19 umgesetzt.** Drei Skills unter `.claude/skills/req-*/`.
- `/req-elicit` hat zwei Modi, gesteuert über `baseline_status`: Rahmenmodus vor dem Gate
  (alle sechs Kategorien, jede wird gefragt), Stufenmodus danach (nur die nächste Stufe,
  ausdrückliches Verbot, auf Vorrat zu erheben).
- Zwei Regeln, die der Skill hart durchhält: er öffnet das Gate nie selbst, und er nimmt
  unprüfbare Formulierungen nicht entgegen, sondern bietet eine messbare Umformulierung an
  und lässt den Nutzer korrigieren.
- `/req-change` folgt bewusst der Struktur von `/contract-sync`, damit beide gleich zu lesen
  sind. Zusätzlich die Unterscheidung Präzisierung (protokollieren) vs. echte Änderung
  (voller Durchlauf) — im Zweifel als Änderung behandeln.
- Trockenlauf: Anforderungsdatei nach Vorlage in einer Vault-Kopie erzeugt, aus
  `baseline.md` verlinkt → `check_vault.py` meldet 0 Fehler, 0 Warnungen. Gegenprobe mit
  einer fehlerhaften Anforderung (ohne `review_after`, ohne Verlinkung) → 2 Fehler,
  1 Warnung, Exit 1. Die Prüfung greift also wirklich.
