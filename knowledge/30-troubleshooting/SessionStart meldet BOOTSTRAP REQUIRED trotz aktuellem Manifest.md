---
title: SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest
type: troubleshooting
tags: [topic/agents, stack/claude-code]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
occurrences: 1
related: ["[[Umgebungs-Manifest]]", "[[T-0007 Selbstverifikation des Templates]]"]
---

# SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest

## Symptom

```
BOOTSTRAP REQUIRED: no verified entry in the environment manifest. Run /bootstrap first.
```

Meldung erscheint bei jedem Sitzungsstart, obwohl `knowledge/90-meta/environment-manifest.md`
mehrere Einträge mit `verified:` auf das heutige Datum enthält.

## Kontext

- `.claude/hooks/session_brief.py`, Funktion `bootstrap_line()`
- Manifest-Format laut `environment-manifest.md`: `- **verified:** 2026-08-19` (Markdown-fett)

## Ursache

Die Regex in `bootstrap_line()` lautete `verified:\s*(\d{4}-\d{2}-\d{2})`. `\s*` überspringt
nur Leerraum. Zwischen `verified:` und dem Datum stehen im echten Manifest aber zwei
`*`-Zeichen (Markdown-Fettschrift schließt), keine Leerzeichen. Die Regex matchte dadurch
**keinen einzigen** Eintrag — unabhängig vom tatsächlichen Prüfdatum. Der Hook fiel also
immer auf den "kein Eintrag gefunden"-Zweig zurück und meldete Bootstrap-Pflicht, selbst bei
einem taggenau gepflegten Manifest.

Gefunden bei der Selbstverifikation (T-0007), beim gezielten Testen aller Hooks gegen
Positiv-/Negativfälle — nicht durch Lesen des Codes allein sichtbar, sondern erst als der
erste Test mit realistischem Manifest-Text (statt vereinfachtem Test-Fixture) geschrieben
wurde.

## Lösung

1. Regex auf `verified:\**\s*(\d{4}-\d{2}-\d{2})` ändern — Sternchen vor dem Leerraum
   optional zulassen.
2. Test mit dem echten Bullet-Format (`- **verified:** DATUM`) schreiben, nicht mit
   vereinfachtem `verified: DATUM` — sonst fängt der Test genau diesen Bug nicht.
3. Hook manuell gegen das reale Manifest laufen lassen und die Ausgabe lesen, nicht nur den
   Exit-Code prüfen.

## Sackgassen

- Erster Testfall für `session_brief.py` nutzte `"verified: {datum}"` ohne Fettschrift —
  lief grün, obwohl der Bug im echten Code längst vorhanden war. Ein Test ist nur so gut wie
  sein Fixture; synthetische Daten müssen das reale Format abbilden.

## Vorbeugung

- Hook-Tests immer mit einer Kopie des realen Dateiformats füttern, nie mit einer
  vereinfachten Annäherung.
- Nach jeder Änderung an einem Hook: einmal manuell gegen die echten Projektdateien laufen
  lassen, nicht nur die Unit-Tests.
