---
id: T-0012
title: Anforderungsregeln und Vault-Struktur
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
tags: [topic/requirements, topic/meta]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Sommerville Software Engineering - was das Template übernimmt]]"]
---

# T-0012 Anforderungsregeln und Vault-Struktur

## Ziel

Das Template hat einen Ort für Anforderungen und eine verbindliche Regel, was eine
Anforderung ist — bevor irgendein Skill sie benutzt.

## Akzeptanzkriterien

- [x] `.claude/rules/requirements.md` existiert: die zwei Ebenen (Rahmen/Detail), die
      sechs Rahmenkategorien, Pflichtfelder, die Prüfbarkeitsregel, das Startgate und
      Sommervilles fünf Validierungsprüfungen
- [x] `knowledge/05-requirements/` angelegt mit `baseline.md` (Startgate), `vision.md`,
      `stakeholders.md`, `glossary.md`, `constraints.md`, `risks.md` — jeweils als
      ausgefüllte Vorlage
- [x] `baseline.md` trägt `baseline_status` und je Rahmenkategorie einen Abschnitt, der
      entweder Anforderungen verlinkt oder die Nichtanwendbarkeit begründet
- [x] `knowledge/90-meta/templates/requirement.md` existiert und passt zur Regel
- [x] `knowledge/90-meta/conventions.md` kennt den neuen Ordner, den Dateinamen `REQ-XXXX`,
      `type: requirement` und den Tag-Namespace-Zusatz
- [x] `CLAUDE.md` §1 hat die neue Nicht-Verhandelbare, §2 den neuen Pfad, §3 den
      erweiterten Zyklus — und bleibt unter 200 Zeilen
- [x] `tools/check_vault.py` akzeptiert `type: requirement` ohne Fehler

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
- **2026-08-19 umgesetzt.** Während der Arbeit hat der Nutzer die Entscheidung präzisiert:
  nicht rein inkrementell, sondern **Rahmen vorab, Details je Entwicklungsstufe**, mit
  Startgate. [[ADR-0005 Anforderungen als Pflicht vor dem Code]] entsprechend überarbeitet,
  bevor gebaut wurde.
- Zwei Formatentscheidungen unterwegs:
  - `status` führt bei Anforderungen den Lebenszyklus (`entwurf`/`vereinbart`/`umgesetzt`/
    `verworfen`), nicht `active`/`deprecated`. Erst `zustand` als eigenes Feld probiert,
    dann verworfen — Task-Dateien nutzen `status` bereits genauso. Die bis dahin
    undokumentierte Abweichung ist jetzt in [[Konventionen der Wissensdatenbank]] festgehalten.
  - Rahmendokumente (`vision`, `stakeholders`, `glossary`, `constraints`, `risks`,
    `baseline`) sind `type: knowledge`; `type: requirement` bleibt den REQ-Dateien
    vorbehalten. `baseline.md` trägt zusätzlich `baseline_status` als Gate.
- `check_vault.py`: `requirement` in `DATED_TYPES` aufgenommen, damit Anforderungen ein
  Prüfdatum tragen müssen. TDD-Zyklus sauber, mit `git stash` gegengeprüft, dass der Test
  ohne den Fix wirklich rot ist.
- Eigener Fehler dabei: erstes Testfixture ließ `updated` **und** `review_after` weg und
  erwartete einen Fehler — es sind zwei. Fixture auf den benannten Fall geschärft, statt
  die Erwartung anzupassen.
