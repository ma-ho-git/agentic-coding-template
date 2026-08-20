---
title: Fremdlösungen
aliases: ["Fremdlösungen"]
type: knowledge
tags: [topic/requirements, topic/meta]
status: active
scan_status: gesucht
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[Rahmen und Startgate]]", "[[Spec-Driven-Development - was andere Projekte machen]]", "[[ADR-0010 Eigene Umsetzung statt Fremdbasis]]", "[[ADR-0011 Das Startgate hat zwei Bedingungen]]", "[[00-index]]"]
---

# Fremdlösungen

> **Diese Datei hält fest, ob vor dem Codieren nach einer bestehenden Lösung gesucht wurde.**
> Gesucht **oder** bewusst übersprungen sind beide gültige Antworten — nicht beantwortet ist
> keine. `check_gate.py` liest `scan_status` und verweigert Produktivcode, solange `offen`
> steht oder die Datei fehlt ([[ADR-0011 Das Startgate hat zwei Bedingungen]]).
>
<!-- template-placeholder -->
> **Für ein eigenes Projekt:** Inhalt ersetzen, `scan_status` auf `offen` zurücksetzen.

## Kurz

Die billigste Zeile Code ist die, die jemand anderes schon geschrieben und gewartet hat.
Deshalb wird nach der Erhebung und **vor** der ersten Codeaufgabe einmal geschaut, ob es das
Gesuchte schon gibt — gemessen an den vereinbarten Anforderungen, nicht am Bauchgefühl.

Ablauf: `/solution-scan`. Regeln: `.claude/rules/workflow.md`.

## Status

| Feld | Wert |
| --- | --- |
| `scan_status` | `gesucht` |
| Durchgeführt am | 2026-08-20 (Marktumschau bereits am 2026-08-20 im Rahmen von T-0019) |
| Befunde | [[Spec-Driven-Development - was andere Projekte machen]] |
| Entscheidung | [[ADR-0010 Eigene Umsetzung statt Fremdbasis]] |

## Geprüfte Kandidaten

| Kandidat | Lizenz | Wartung | Anforderungsabgleich |
| --- | --- | --- | --- |
| GitHub Spec Kit | MIT | aktiv | erfüllt Ablaufsteuerung; **nicht** [[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]] — die „Constitution" ist reine Prosa |
| BMAD-Method | quelloffen | aktiv | Rollenmodell nützlich; Durchsetzung ebenfalls nur Prosa |
| AWS Kiro | kommerziell, IDE | aktiv | scheidet aus: kein klonbares Repository-Template, Bindung an eine IDE |
| OpenSpec | quelloffen | kleiner | leichtgewichtig, deckt weniger ab als Spec Kit |

**Sonderfall dieses Repositories:** Die Umschau entstand vor diesem Verfahren und trägt
deshalb nicht das vollständige Kandidatenraster aus `/solution-scan` — Abrufdaten und
Wartungsstände stehen in der verlinkten Notiz, nicht hier. Für ein neu geklontes Projekt
gilt der normale Weg.

## Übernommene Fremdkomponenten

Keine. Es wurde keine Fremdbasis übernommen — siehe
[[ADR-0010 Eigene Umsetzung statt Fremdbasis]]. Wird später eine übernommen, kommt sie in
das Register der Fremdkomponenten samt ihrer Lizenzpflichten (T-0029).
