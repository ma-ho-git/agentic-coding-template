---
title: Konventionen der Wissensdatenbank
aliases: ["Konventionen der Wissensdatenbank"]
type: knowledge
tags: [topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-08-19
related: ["[[00-index]]"]
---

# Konventionen der Wissensdatenbank

## Kurz

Verbindliche Regeln für Ablage, Frontmatter, Tags und Verlinkung im Vault.
Gelten für Menschen und Agenten gleichermaßen. Änderungen hier zuerst, dann in den Notizen.

## Ordnerstruktur

| Ordner | Inhalt |
| --- | --- |
| `00-index.md` | Einstiegspunkt, Themenübersicht, Hub aller Bereiche |
| `10-pm/` | Projektmanagement: Board, Tasks, ADRs, Fortschritt |
| `20-knowledge/` | recherchiertes und projektrelevantes Wissen |
| `30-troubleshooting/` | Problem → Ursache → Lösung |
| `90-meta/` | Konventionen, Templates, Register, Umgebungs-Manifest |

## Dateinamen

- Tasks: `T-0042 Kurzer Titel.md` — vierstellige ID, Leerzeichen, sprechender Titel
- ADRs: `ADR-0007 Kurzer Titel.md`
- Wissen und Troubleshooting: sprechender Titel, keine ID
- Keine Umlaute-Ersetzung nötig, keine Unterstriche, keine Datumspräfixe

### Ausnahme: Dateien mit stabilem Pfad

Notizen, die aus Code, Regeln oder Skripten heraus referenziert werden, behalten einen
kurzen ASCII-Dateinamen (`conventions.md`, `environment-manifest.md`,
`subagent-decisions.md`). Damit `[[Wikilinks]]` trotzdem sprechend bleiben, tragen sie
im Frontmatter ein `aliases`-Feld:

```yaml
title: Konventionen der Wissensdatenbank
aliases: ["Konventionen der Wissensdatenbank"]
```

Obsidian löst Wikilinks über Aliase auf; `tools/check_vault.py` ebenfalls.

## Frontmatter

Pflichtfelder in **jeder** Notiz:

| Feld | Werte |
| --- | --- |
| `title` | wie die Überschrift |
| `type` | `knowledge`, `troubleshooting`, `decision`, `task`, `progress` |
| `tags` | Liste, Namespaces siehe unten |
| `status` | `active` oder `deprecated` |
| `created` | JJJJ-MM-TT |
| `updated` | JJJJ-MM-TT — wann zuletzt gegen die Realität geprüft |
| `review_after` | JJJJ-MM-TT — 3 Monate Stack/API, 12 Monate Domäne |
| `related` | Liste von Wikilinks, mindestens einer |

Zusätzlich bei `deprecated`: `deprecated_on`, `deprecated_reason`, optional `superseded_by`.
Zusätzlich bei Troubleshooting: `occurrences` (hochzählen bei Wiederauftreten).

## Tag-Namespaces

Kleingeschrieben, mit Schrägstrich verschachtelt. Neue Namespaces **hier zuerst eintragen**.

| Namespace | Bedeutung | Beispiele |
| --- | --- | --- |
| `topic/` | Fachbereich | `topic/auth`, `topic/meta`, `topic/agents` |
| `stack/` | Technologie | `stack/python`, `stack/claude-code`, `stack/obsidian` |
| `type/` | Notizart, wenn Filterung nötig | `type/troubleshooting` |
| `status/` | Sonderzustand | `status/deprecated`, `status/unverified` |

Drei präzise Tags schlagen acht vage. Kein Tag ohne Namespace.

## Verlinkung

- `[[Wikilinks]]`, keine Markdown-Pfadlinks innerhalb des Vaults
- Jede Notiz hat mindestens einen ausgehenden Link. Waisen sind ein Fehler.
- Jede Notiz ist von `00-index.md` aus erreichbar — direkt oder über eine Themennotiz
- Beziehungen werden beidseitig gepflegt: wer verlinkt, verlinkt zurück
- Aufgabenbezug: Notiz verlinkt den Task, der sie erzeugt hat

## Schreibstil

- Stichpunkte statt Fließtext. Fragmente statt Sätze. Keine Füllwörter.
- Ein Fakt pro Stichpunkt.
- Fehlermeldungen und Kommandos **wörtlich** kopieren — genau danach wird gesucht.
- Quellen immer mit Abrufdatum.
- Was nicht verifiziert ist, wird als nicht verifiziert gekennzeichnet.

## Was nicht in den Vault gehört

- Was im Code steht — der Code ist die Quelle, nicht die Notiz
- Sitzungsprotokolle und Gesprächsverläufe
- Geheimnisse jeder Art (siehe `.claude/rules/security.md`)
- Einzeilige Fakten, die in einer Suche sofort auffindbar wären
