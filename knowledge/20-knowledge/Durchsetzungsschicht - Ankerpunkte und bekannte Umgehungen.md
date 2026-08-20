---
title: Durchsetzungsschicht - Ankerpunkte und bekannte Umgehungen
type: knowledge
tags: [topic/agents, stack/claude-code]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2026-11-20
related: ["[[ADR-0012 Durchsetzung an drei Ankerpunkten]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[00-index]]"]
---

# Durchsetzungsschicht - Ankerpunkte und bekannte Umgehungen

## Kurz

Warum die Hook-Schicht allein nicht trägt, wie die drei Ankerpunkte zusammenwirken, und
welche Umgehungen bekannt und akzeptiert sind. Nachschlagen, bevor jemand die
Durchsetzung „vereinfacht".

## Kernpunkte

- **Hook-Matcher decken nur das jeweilige Tool.** `Write|Edit`-Hooks sehen keinen einzigen
  über Bash geschriebenen Byte. In der Cloud-Umgebung ist Bash der Normalweg — die Lücke war
  hier also der Regelfall, bewiesen an der eigenen Sitzung vom 2026-08-20.
- **Der Commit ist der einzige Engpass, den jeder Schreibweg passiert.** Deshalb läuft dort
  `check_all --staged`; CI wiederholt dasselbe je Push als Rückhalt, dem niemand einen
  Überspring-Schalter mitgeben kann.
- **Die dokumentierte Standard-Umgehung ist der Überspring-Schalter beim Commit** (lang und
  kurz). git_guard verweigert beide für den Agenten, ebenso das Umbiegen des Hook-Pfads.
- **Deny-Regeln schützen die Hook-Dateien selbst nicht zuverlässig** (Issue #11226).
  Konsequenz hier: nicht verhindern, sondern laut machen — CI warnt je geänderter
  Enforcement-Datei.
- **Die Hooks versagen offen.** Fehlender Interpreter oder crashendes Skript heißt: die
  Schicht ist stumm abwesend. Gegenmittel ist der Nachweis: `check_armed.py` feuert jede
  Leitplanke mit einem Kanarienvogel und erwartet ARMED — `/bootstrap` protokolliert das im
  Manifest.
- **Kanarienvogel-Falle:** AWSs dokumentierter Beispielschlüssel enthält „EXAMPLE" und fällt
  damit absichtlich unter die Platzhalter-Ausnahme der Geheimnisprüfung. Ein Kanarienvogel
  muss wie ein echtes Geheimnis aussehen, sonst prüft er die Ausnahme statt der Regel —
  gefunden beim allerersten Lauf des Selbsttests.

## Details — die Abdeckung

| Anker | Sieht | Sieht nicht |
| --- | --- | --- |
| Tool-Aufruf (Hooks) | Write/Edit des Agenten | Bash-Schreibvorgänge, fremde Editoren |
| Commit (pre-commit) | jede gestagte Änderung, egal woher | nie Committetes; entfernten Hook |
| CI (jeder Push) | alles, was die Maschine verlässt | was nie gepusht wird |

Garantie der drei zusammen: Ein Verstoß kommt nicht leise weit. Nicht mehr — und das steht
so auch in `.claude/rules/guardrails.md`.

## Quellen

Recherche vom 2026-08-20; Suchzusammenfassungen, Seitenabrufe vom Egress-Proxy blockiert:

- Hooks-Referenz (Matcher je Tool) — https://code.claude.com/docs/en/hooks-guide
- Deny-Regeln schützen Hook-Dateien nicht — https://github.com/anthropics/claude-code/issues/11226
- Agenten und der Überspring-Schalter, Schichtenmodell mit CI-Rückhalt —
  https://pydevtools.com/handbook/how-to/how-to-stop-ai-agents-from-bypassing-pre-commit-hooks/
- Pre-commit vs. CI, was wohin gehört — https://tildalice.io/pre-commit-hooks-vs-ci-when-to-skip-local-checks/
- Git-Hooks-Grundlagen — https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
