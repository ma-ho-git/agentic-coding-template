---
title: ADR-0003 Kanban-Board mit Wikilink-Karten
type: decision
tags: [topic/meta, stack/obsidian]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-02-19
related: ["[[Obsidian-Kanban Dateiformat]]", "[[T-0003 Wissensdatenbank aufsetzen]]"]
---

# ADR-0003 Kanban-Board mit Wikilink-Karten

## Status

angenommen

## Kontext

- Vorgabe: Kanban-artige Aufgabenverwaltung im Obsidian-Vault
- Vorgabe: mehrere Agenten sollen parallel am Projekt arbeiten können
- Das obsidian-kanban-Plugin speichert ein Board als **eine** Markdown-Datei
- Eine gemeinsam beschriebene Datei ist bei Parallelarbeit die Konfliktquelle schlechthin

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Board mit vollständigen Karten | eine Datei, alles sichtbar | jeder Schreibvorgang trifft dieselbe Datei, Konflikte betreffen Inhalt |
| Nur Task-Dateien, kein Board | konfliktfrei | kein Board, Vorgabe nicht erfüllt |
| Board mit Wikilink-Karten | Board vorhanden, Konflikte auf eine Zeile reduziert | zwei Orte, können auseinanderlaufen |

## Entscheidung

Board im Plugin-Format, Karten ausschließlich als Wikilink:

```markdown
- [ ] [[T-0042 Token-Refresh]]
```

Alle Inhalte liegen in `knowledge/10-pm/tasks/T-XXXX ….md`.
Die Wahrheit ist das `status`-Feld im Frontmatter der Task-Datei; das Board ist eine Ansicht darauf.

## Konsequenzen

- Ein Statuswechsel ändert genau eine Zeile — Konflikte sind trivial auflösbar
- Board und Frontmatter können auseinanderlaufen; dafür existiert `/board-sync`
- Menschen sehen im Board nur Titel; Details brauchen einen Klick
- Das Board bleibt auch ohne installiertes Plugin lesbares Markdown

## Revidieren wenn

- Das Kanban-Plugin endgültig unmaintained ist und das Format bricht
- Sich zeigt, dass Board und Frontmatter regelmäßig divergieren — dann Board generieren

## Nachprüfung 2026-08-19

Entscheidung bleibt bestehen. Auslöser der Prüfung: Frage nach dem nötigen Obsidian-Plugin.

- Wartungslage des Plugins hat sich verschlechtert (Org `community-archive`, letzter Push
  2026-03-06) — siehe [[Obsidian-Kanban Dateiformat]]. Das Format ist aber **nicht** gebrochen,
  die erste Revidierungsbedingung ist damit nicht erfüllt.
- Der eigentliche Wert der Entscheidung ist unabhängig vom Plugin: kein Code hängt daran,
  `board.md` bleibt ohne Plugin lesbar. Das Plugin ist reiner Komfort.
- `xiwcx/obsidian-bases-kanban` würde Lanes aus dem `status:`-Feld generieren und damit die
  zweite Revidierungsbedingung vorwegnehmen. Bewusst nicht umgestellt: kleineres Projekt,
  und Divergenz ist bisher nicht real aufgetreten (`/board-sync` meldete zuletzt 0 Abweichungen).
