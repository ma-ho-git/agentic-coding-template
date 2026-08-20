---
id: T-0036
title: CI als echter Rückhalt
type: task
implements: ["[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/agents, topic/meta]
related: ["[[T-0035 Durchsetzung am Commit]]", "[[T-0037 Scharfschaltung nachweisen]]"]
---

# T-0036 CI als echter Rückhalt

## Anforderung

[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]] — Befund F2: CI triggert
nur auf Pull Requests nach `main`. Direkte Pushes, Feature-Branches und lokale Solo-Arbeit —
der Normalfall der Zielgruppe — sehen keinen einzigen maschinellen Rückhalt.

## Ziel

CI läuft auf jedem Push, prüft dasselbe wie der Commit-Engpass, und niemand kann ihr einen
Überspring-Schalter mitgeben.

## Akzeptanzkriterien

- [x] Workflow triggert auf `push` (alle Branches) und weiter auf Pull Requests nach `main`
- [x] Der geprüfte Bereich ist der gepushte Commit-Bereich; Rückfall auf den letzten Commit,
      wenn die Vorgänger-Referenz fehlt (Force-Push, erster Commit)
- [x] CI ruft `tools/check_all.py` auf — dieselbe Logik wie der Commit-Engpass, keine
      Duplikation; das Startgate wird damit erstmals auch in CI geprüft
- [x] Änderungen an Leitplanken-Dateien (`.claude/hooks/`, `.claude/settings.json`,
      `.claude/rules/guardrails.md`, `tools/check_*`) erzeugen eine **laute, sichtbare
      Warnung** im CI-Lauf — eine Leitplanken-Änderung darf nie beiläufig durchrutschen.
      Sie blockt nicht: Leitplanken weiterentwickeln ist legitim, unbemerkt ändern nicht.
- [x] Die Bereichslogik ist lokal durchgespielt (CI selbst ist hier nicht ausführbar) und
      der Lauf auf diesem Repository bleibt grün

## Ergebnis

- Workflow triggert auf `push` (alle Branches) und weiter auf Pull Requests nach `main`.
  Bereichslogik mit drei Rückfallstufen: PR-Basis → Vorgänger-Referenz des Pushs → letzter
  Commit → Vollprüfung, wenn gar keine Referenz trägt.
- CI ruft **dasselbe** `tools/check_all.py` wie der Commit-Engpass — kein zweites Regelwerk,
  das auseinanderlaufen kann. Damit prüft CI erstmals auch das Startgate und die Task-Regel
  am Diff.
- Leitplanken-Sichtbarkeit: Änderungen unter `.claude/hooks/`, an den Settings, an
  `guardrails.md`, an den Prüfwerkzeugen oder am Workflow selbst erzeugen eine
  `::warning::`-Annotation je Datei plus einen Eintrag in der Lauf-Zusammenfassung.
  Bewusst keine Sperre — Leitplanken weiterentwickeln ist legitim, unbemerkt ändern nicht.
- Lokal simuliert: `--range HEAD~1..HEAD` und `--range origin/main...HEAD` beide Exit 0;
  die Diff-Erkennung listet korrekt die vier Enforcement-Dateien, die T-0035 angefasst hat —
  die Warnung hätte beim heutigen Push zu Recht gefeuert.
- YAML gegen den Parser geprüft. Der echte CI-Lauf startet mit dem Push dieses Commits —
  erstmals überhaupt für einen Push auf diesen Branch.

## Kontext

- [[T-0035 Durchsetzung am Commit]] liefert `check_all`; diese Aufgabe verdrahtet es als
  zweiten, nicht überspringbaren Anker
- Für dieses Template-Repository bleibt das Gate in CI folgenlos (der eigene Code liegt in
  Gate-Ausnahmepfaden); in geklonten Projekten schützt es

## Agent

`claude-code` — Workflow, lokale Simulation.

## Abhängigkeiten

- [[T-0035 Durchsetzung am Commit]]

## Notizen

- Die Warnung bei Leitplanken-Änderungen ist bewusst keine Sperre. Wer sie zur Sperre macht,
  friert die Leitplanken ein und erzwingt Umgehungen — Sichtbarkeit ist hier die richtige
  Härte.
