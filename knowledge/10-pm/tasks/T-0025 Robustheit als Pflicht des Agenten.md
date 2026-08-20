---
id: T-0025
title: Robustheit als Pflicht des Agenten
type: task
implements: ["[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/code, topic/agents]
related: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]", "[[T-0026 Verschluckte Ausnahmen sichtbar machen]]", "[[ADR-0009 Fehlerbehandlung ändert die Form, nicht die Grenze]]"]
---

# T-0025 Robustheit als Pflicht des Agenten

## Anforderung

[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]

## Ziel

Der Agent baut nicht nur den Gutfall. Fehler, Ausnahmen, Laufzeit und der Ausfall
angebundener Systeme werden geprüft, behandelt und sichtbar gemacht.

## Akzeptanzkriterien

- [x] `.claude/rules/robustness.md`, pfadgebunden auf Quelldateien wie `security.md`
- [x] Vier Klassen benannt, je mit Behandlungsregel: Eingabe- und Grenzfälle, Ausnahmepfade,
      Laufzeit und Ressourcen, Ausfall angebundener Systeme
- [x] `/req-elicit` fragt für jedes angebundene System, was bei dessen Ausfall geschehen
      soll — anfängertauglich formuliert, mit Vorschlag
- [x] Definition of Done in `.claude/rules/workflow.md` verlangt je behandeltem Fehlerpfad
      des geänderten Codes einen Test, der ihn auslöst
- [x] `.claude/rules/contracts.md` sagt ausdrücklich, dass `invariants:` das Fehlerverhalten
      nennt
- [x] `code-reviewer` prüft die Klassen als eigene Linse
- [x] ADR löst den Zielkonflikt zu [[REQ-0007 Grenzen für Funktionsgröße und Benennung]] auf:
      Fehlerbehandlung erzeugt Zweige, die flexiblen Grenzen drücken dagegen

## Ergebnis

- `.claude/rules/robustness.md` (100 Zeilen, pfadgebunden auf Quelldateien).
- **Tragendes Gerüst: jeder Fehler bekommt eine von vier Antworten** — verhindern,
  behandeln, weiterreichen, bewusst abstürzen. „Bewusst abstürzen" ausdrücklich als
  legitime Antwort benannt; Schweigen nie.
- **Der Fund, der die Regel wertvoll macht:** Ein angebundenes System fällt auf *drei* Arten
  aus, nicht auf eine — nicht erreichbar, zu langsam, **falsche Antwort**. Die dritte ist
  die vergessene: 200 mit leerem Rumpf, abgeschnittene Liste, veraltete Daten, geändertes
  Schema. Rückgaben sind ebenfalls fremde Eingabe.
- Wiederholung nur bei **idempotenten** Operationen — eine wiederholte Zahlung ist eine
  zweite Zahlung.
- **Zuständigkeit getrennt:** Was der Nutzer im Fehlerfall *sieht*, ist eine Anforderung und
  seine Entscheidung. *Wie* das erreicht wird, entscheidet der Agent. Wer die sichtbare
  Reaktion errät, baut Software, die das Falsche korrekt tut.
- `/req-elicit` fragt das je angebundenem System — einmal pro Abhängigkeit, nicht einmal
  insgesamt, mit Vorschlag zum Widersprechen.
- Definition of Done: je behandeltem Fehlerpfad ein Test, der ihn auslöst. Eine behandelte
  Ausnahme ohne Test ist eine Annahme.
- `contracts.md`: `invariants:` nennt das Fehlerverhalten — der Teil, den ein Aufrufer nicht
  aus der Signatur lesen kann und regelmäßig falsch annimmt.
- `code-reviewer` bekommt Robustheit als eigene Linse (jetzt 7 statt 6).

### Zielkonflikt entschieden

[[ADR-0009 Fehlerbehandlung ändert die Form, nicht die Grenze]]. Der Konflikt ist konkret:
`check_quality.py` zählt `try` als Verschachtelungsebene, ein `try` um eine Schleife mit
einer Bedingung liegt schon auf der Grenze. Entschieden: **Grenze bleibt, Form ändert sich**
— Wächterklausel, benannte Fehlerbehandlungseinheit, ein `try` um den Rumpf. `try` zählt
weiter mit, weil dort jede Zeile einen unsichtbaren zweiten Ausgang hat; das ist genau die
Last, die die Grenze abbilden soll.

Der Konflikt ist begrenzt, weil die Größengrenzen **flexibel** sind: Sie melden, sie
blockieren nicht. Robustheit kann also nie an ihnen scheitern — eine Abweichung wird nur
sichtbar. Genau dafür gibt es die Klasse.

Suite 82 grün (unverändert — Regeln und Skills, kein Code berührt; der maschinelle Teil ist
[[T-0026 Verschluckte Ausnahmen sichtbar machen]]). Vault- und Rückverfolgbarkeitsprüfung
ohne Befund.

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
