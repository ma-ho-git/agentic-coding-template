---
id: T-0009
title: Beispielprojekt als Smoke-Test
type: task
implements: []
infrastruktur: Template-Grundgerüst, entstanden vor Einführung der Anforderungspflicht (ADR-0005)
status: done
priority: niedrig
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta]
related: ["[[T-0007 Selbstverifikation des Templates]]"]
---

# T-0009 Beispielprojekt als Smoke-Test

## Ziel

Ein minimales Beispielprojekt zeigt den vollständigen Zyklus und beweist, dass die Regeln
in der Praxis funktionieren.

## Akzeptanzkriterien

- [x] Kleines, echtes Feature nach TDD umgesetzt
- [x] Contract-Kommentare vorhanden und über mindestens zwei Dateien verknüpft
- [x] Eine Änderung löst nachweislich eine Folgeaufgabe über `/contract-sync` aus
- [x] Board und Wissensdatenbank am Ende konsistent

## Kontext

- [[T-0007 Selbstverifikation des Templates]]

## Agent

`claude-code`

## Abhängigkeiten

- [[T-0007 Selbstverifikation des Templates]]

## Notizen

- Offene Frage geklärt (mit dem Nutzer, 2026-08-19): `examples/`-Ordner statt eigener
  Branch — bleibt in diesem PR sichtbar, kein Branch-Wechsel nötig. Hinweis zum Löschen
  beim Projektstart steht in `examples/README.md`.
- **Umgesetzt:** `examples/slugify/` — `slugify(text, max_length)` +
  `article_url(title)`, beide per TDD entwickelt, per `@contract` verlinkt.
  Ablauf inkl. der echten Vertragsänderung (neuer Pflichtparameter `max_length`) und dem
  `/contract-sync`-Lauf, der den Bruch in `article.py` fand und behob, ist in
  `examples/slugify/README.md` dokumentiert.
- `/contract-sync` real ausgeführt: `consumers:`-Liste in `slugify.py` gegen `grep
  slugify\(` über den ganzen Repo verifiziert — keine undokumentierte Aufrufstelle,
  Contract-Block war korrekt. Kleiner Fix in `article.py` sofort erledigt
  (`SLUG_MAX_LENGTH = 60`), beide `updated:`-Daten bestätigt aktuell.
- Volle Suite grün (`pytest tests` → 24/24), `ruff` sauber, CI-Check aus T-0010 gegen die
  neuen Dateien gegenprobiert (exit 0).
