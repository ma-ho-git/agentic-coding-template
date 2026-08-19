---
id: T-0012
title: Anforderungsregeln und Vault-Struktur
type: task
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Sommerville Software Engineering - was das Template übernimmt]]"]
---

# T-0012 Anforderungsregeln und Vault-Struktur

## Ziel

Das Template hat einen Ort für Anforderungen und eine verbindliche Regel, was eine
Anforderung ist — bevor irgendein Skill sie benutzt.

## Akzeptanzkriterien

- [ ] `.claude/rules/requirements.md` existiert: Anforderungsarten, Pflichtfelder,
      die Prüfbarkeitsregel, Sommervilles fünf Validierungsprüfungen
- [ ] `knowledge/05-requirements/` angelegt mit `vision.md`, `stakeholders.md`,
      `glossary.md`, `constraints.md`, `risks.md` — jeweils als ausgefüllte Vorlage
- [ ] `knowledge/90-meta/templates/requirement.md` existiert und passt zur Regel
- [ ] `knowledge/90-meta/conventions.md` kennt den neuen Ordner, den Dateinamen `REQ-XXXX`,
      `type: requirement` und den Tag-Namespace-Zusatz
- [ ] `CLAUDE.md` §1 hat die neue Nicht-Verhandelbare, §2 den neuen Pfad, §3 den
      erweiterten Zyklus — und bleibt unter 200 Zeilen
- [ ] `tools/check_vault.py` akzeptiert `type: requirement` ohne Fehler

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[Sommerville Software Engineering - was das Template übernimmt]]

## Agent

`claude-code` — Regeldateien, Templates, Prüfskript.

## Abhängigkeiten

- keine

## Notizen

- Grundlage für alles Weitere. Zuerst erledigen, sonst referenzieren die Skills ins Leere.
- Sprache: `.claude/` englisch, `knowledge/` deutsch (CLAUDE.md §7).
