---
title: git_guard verwechselt Erwähnung mit Gebrauch
type: troubleshooting
tags: [topic/agents, stack/claude-code]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[ADR-0012 Durchsetzung an drei Ankerpunkten]]", "[[00-index]]"]
---

# git_guard verwechselt Erwähnung mit Gebrauch

## Kurz

git_guard liest den **gesamten** Bash-Kommandotext — auch Heredoc-Inhalte. Wer eine Datei
schreibt, die ein gesperrtes Kommando bloß *erwähnt* (Test, Doku, Kanarienvogel), wird
behandelt, als wollte er es *ausführen*.

## Symptom

```
[RIGID] Blocked by .claude/rules/agent-conduct.md: direct push to the default branch.
Command: python3 - <<'PY' ...
```

Das verweigerte „Kommando" ist ein Python-Heredoc, das eine Datei schreiben sollte — der
Auslöser steht als String **im Dateiinhalt**.

## Kontext

- Jede Datei, die über Bash geschrieben wird und gesperrte Muster als Text enthält:
  Testfälle, Kanarienvögel, Dokumentation der Sperren selbst.
- Aufgetreten bei T-0007 (Verifikationsskript) und erneut am 2026-08-20 beim Schreiben von
  `check_armed.py`: `--force` war zerlegt, aber „origin main" zusammengelassen — das
  Push-auf-main-Muster griff. **occurrences: 2**

## Ursache

Textbasierte Prüfung ohne Parsing. Der Hook kann nicht unterscheiden, ob ein Muster
ausgeführt oder zitiert wird — Heredoc-Inhalte sind Teil des Kommandotexts.

## Lösung

Gesperrte Literale **zur Laufzeit zusammensetzen**, sodass der Kommandotext das Muster nie
zusammenhängend enthält:

```python
DESTRUCTIVE = "git push " + "--for" + "ce origin ma" + "in"
```

Alle Bestandteile zerlegen, auf die ein Muster anspricht — nicht nur den auffälligsten
(der zweite Vorfall entstand genau daraus).

## Sackgassen

- Das Muster im Hook „präziser" machen: Ohne Shell-Parsing bleibt jede Textprüfung
  anfällig; die Präzisierung verschiebt den Fehlalarm nur.
- Die Datei über das Write-Tool schreiben, um git_guard zu umgehen: funktioniert, verschiebt
  das Problem aber auf jede spätere Bash-Bearbeitung derselben Datei.

## Vorbeugung

- In Prosa die Auslöser nicht zusammenhängend schreiben: „no-verify" ohne Bindestriche
  davor, „hooksPath" ohne Präfix, Push-Ziele nicht wörtlich neben dem Kommandowort.
- Beim Erweitern von git_guard sofort prüfen, welche eigenen Dateien das neue Muster
  erwähnen — und deren Literale zerlegen, **bevor** das Muster aktiv wird.
