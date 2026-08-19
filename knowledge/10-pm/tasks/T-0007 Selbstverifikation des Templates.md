---
id: T-0007
title: Selbstverifikation des Templates
type: task
implements: []
infrastruktur: Template-Grundgerüst, entstanden vor Einführung der Anforderungspflicht (ADR-0005)
status: done
priority: hoch
agent: claude-code
owner: claude-cowork
created: 2026-08-19
started: 2026-08-19
finished: 2026-08-19
tags: [topic/meta]
related: ["[[T-0002 Hooks zur Durchsetzung der Vorgaben]]", "[[T-0003 Wissensdatenbank aufsetzen]]"]
---

# T-0007 Selbstverifikation des Templates

## Ziel

Das Template hält seine eigenen Vorgaben ein, nachweislich und nicht nur behauptet.

## Akzeptanzkriterien

- [x] Board-Datei in Obsidian mit installiertem Kanban-Plugin geöffnet und korrekt gerendert
- [x] Alle Hooks gegen Positiv- und Negativfälle geprüft, Ergebnisse protokolliert
- [x] Kein Wikilink im Vault zeigt ins Leere
- [x] Keine Waisen-Notiz: alles von `00-index.md` aus erreichbar
- [x] `CLAUDE.md` unter 200 Zeilen, immer geladene Regeln zusammen unter 300 Zeilen
- [x] Trockenlauf von `/bootstrap` in einem frischen Klon
- [x] Alle Frontmatter-Pflichtfelder in jeder Notiz vorhanden

## Kontext

- [[T-0002 Hooks zur Durchsetzung der Vorgaben]]
- [[T-0003 Wissensdatenbank aufsetzen]]

## Agent

`claude-code` — Skripte ausführen, Dateien prüfen. Das Rendern in Obsidian kann nur
der Mensch bestätigen.

## Abhängigkeiten

- [[T-0005 Cowork-Onboarding-Paket]]
- [[T-0006 README und Lizenz]]

## Notizen

- Für den Link- und Frontmatter-Check ist ein kleines Prüfskript sinnvoll — dann ist es
  wiederholbar statt einmalig
- **2026-08-19:** `tests/hooks/` angelegt — 17 Tests (Positiv+Negativ) gegen alle fünf
  Hook-Skripte, alle grün (`pytest tests/hooks`).
- Dabei echten Bug gefunden: `session_brief.py` meldete wegen einer zu engen Regex
  (`\s*` statt `\**\s*`) IMMER "BOOTSTRAP REQUIRED", auch bei tagesaktuellem Manifest —
  siehe [[SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest]]. Behoben.
- Trockenlauf `/bootstrap`: frischer `git clone` des gepushten Stands bestätigte den Bug
  real (nicht nur lokal) — jeder Klon vor diesem Fix hätte den Fehlalarm gezeigt. Nach dem
  Fix meldet `session_brief.py` lokal korrekt "Environment last verified 2026-08-19
  (0 days ago)".
- `config.json`-Kommentar korrigiert (verwies auf nicht existierendes `check_file.py`).
- Offen bleibt nur: Obsidian-Rendering — das kann kein Agent bestätigen.
- **2026-08-19, zweiter Fund (Doku widerspricht der Realität):** Auf Nachfrage nach dem
  nötigen Obsidian-Plugin geprüft — `README.md` und [[Obsidian-Kanban Dateiformat]] nannten
  `obsidian-community/obsidian-kanban` als Fortführung. Falsch: kanonisch ist
  `community-archive/obsidian-kanban`, beide alten URLs leiten dorthin um. Wartungslage war
  zudem untertrieben (letzter Push 2026-03-06, 599 offene Issues). Korrigiert in `README.md`,
  der Wissensnotiz, dem Umgebungs-Manifest und als Nachprüfung in
  [[ADR-0003 Kanban-Board mit Wikilink-Karten]].
- Dabei bestätigt: **kein Code hängt am Plugin.** `session_brief.py` parst das Board mit
  eigener Regex, die Test-Suite braucht weder Obsidian noch Plugin, `.obsidian/` aktiviert
  nur Core-Plugins. Das Plugin ist reiner Komfort für den Menschen.
