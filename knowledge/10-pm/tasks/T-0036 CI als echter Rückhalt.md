---
id: T-0036
title: CI als echter Rückhalt
type: task
implements: ["[[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
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

- [ ] Workflow triggert auf `push` (alle Branches) und weiter auf Pull Requests nach `main`
- [ ] Der geprüfte Bereich ist der gepushte Commit-Bereich; Rückfall auf den letzten Commit,
      wenn die Vorgänger-Referenz fehlt (Force-Push, erster Commit)
- [ ] CI ruft `tools/check_all.py` auf — dieselbe Logik wie der Commit-Engpass, keine
      Duplikation; das Startgate wird damit erstmals auch in CI geprüft
- [ ] Änderungen an Leitplanken-Dateien (`.claude/hooks/`, `.claude/settings.json`,
      `.claude/rules/guardrails.md`, `tools/check_*`) erzeugen eine **laute, sichtbare
      Warnung** im CI-Lauf — eine Leitplanken-Änderung darf nie beiläufig durchrutschen.
      Sie blockt nicht: Leitplanken weiterentwickeln ist legitim, unbemerkt ändern nicht.
- [ ] Die Bereichslogik ist lokal durchgespielt (CI selbst ist hier nicht ausführbar) und
      der Lauf auf diesem Repository bleibt grün

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
