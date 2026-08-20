---
id: T-0025
title: Robustheit als Pflicht des Agenten
type: task
implements: ["[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/code, topic/agents]
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[T-0026 Verschluckte Ausnahmen sichtbar machen]]"]
---

# T-0025 Robustheit als Pflicht des Agenten

## Anforderung

[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]

## Ziel

Der Agent baut nicht nur den Gutfall. Fehler, Ausnahmen, Laufzeit und der Ausfall
angebundener Systeme werden geprüft, behandelt und sichtbar gemacht.

## Akzeptanzkriterien

- [ ] `.claude/rules/robustness.md`, pfadgebunden auf Quelldateien wie `security.md`
- [ ] Vier Klassen benannt, je mit Behandlungsregel: Eingabe- und Grenzfälle, Ausnahmepfade,
      Laufzeit und Ressourcen, Ausfall angebundener Systeme
- [ ] `/req-elicit` fragt für jedes angebundene System, was bei dessen Ausfall geschehen
      soll — anfängertauglich formuliert, mit Vorschlag
- [ ] Definition of Done in `.claude/rules/workflow.md` verlangt je behandeltem Fehlerpfad
      des geänderten Codes einen Test, der ihn auslöst
- [ ] `.claude/rules/contracts.md` sagt ausdrücklich, dass `invariants:` das Fehlerverhalten
      nennt
- [ ] `code-reviewer` prüft die Klassen als eigene Linse
- [ ] ADR löst den Zielkonflikt zu [[REQ-0007 Grenzen für Funktionsgröße und Benennung]] auf:
      Fehlerbehandlung erzeugt Zweige, die flexiblen Grenzen drücken dagegen

## Kontext

- Abgrenzung zu `.claude/rules/security.md`: dort Angriffe, hier Fehler ohne Angreifer
- `tdd.md` verlangt bereits Grenzfalltests — hier kommt der Ausfall der Nachbarsysteme dazu

## Agent

`claude-code` — Regeln, Skill, Agentendefinition, ADR.

## Abhängigkeiten

- keine

## Notizen

- Der Zielkonflikt ist echt und darf nicht stillschweigend zugunsten einer Seite entschieden
  werden. Vermutete Auflösung: Fehlerbehandlung als benannte Wächterklausel herausziehen,
  nicht verschachteln — die Grenze bleibt, die Form ändert sich.
