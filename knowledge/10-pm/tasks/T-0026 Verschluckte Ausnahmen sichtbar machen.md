---
id: T-0026
title: Verschluckte Ausnahmen sichtbar machen
type: task
implements: ["[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/code, topic/meta]
related: ["[[T-0025 Robustheit als Pflicht des Agenten]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0026 Verschluckte Ausnahmen sichtbar machen

## Anforderung

[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]] — der maschinell
prüfbare Teil.

## Ziel

`code-quality.md` verbietet schon heute, eine Ausnahme zu fangen und nichts damit zu tun.
Durchgesetzt wird es von nichts. Ein Hinweis macht die Stelle sichtbar.

## Akzeptanzkriterien

- [x] `check_quality.py` meldet einen Fang ohne Behandlung — Python und JavaScript/TypeScript
- [x] Die Meldung trägt `[FLEXIBLE]` und nennt Datei und Zeile
- [x] Kein Fehlalarm, wenn im Fang erneut geworfen, protokolliert oder ein Ersatzwert mit
      Begründung im Code gesetzt wird
- [x] Tests je Sprache: positiver Fall, negativer Fall, begründeter Fall
- [x] Schwellwert beziehungsweise Abschaltung in `.claude/hooks/config.json`

## Ergebnis

- `check_quality.py` meldet zwei Fälle: ein `except`-Block, dessen Rumpf nur `pass` oder ein
  nacktes Literal enthält (Python, über den AST), und ein leerer `catch`-Block (JS/TS, über
  ein eng gefasstes Muster).
- **Die Entwurfsentscheidung, die die Prüfung brauchbar macht: ein Kommentar im Block räumt
  den Befund ab.** Nicht als Schlupfloch, sondern weil das genau der Vertrag der flexiblen
  Klasse ist — die Prüfung verbietet das Ignorieren nicht, sie macht die Entscheidung
  sichtbar. Das deckt sich mit `robustness.md`: „wenn ein Fehler wirklich ignorierbar ist,
  schreib das *Warum* in den Code".
- Bewusst eng gefasst, um Fehlalarme zu vermeiden: Ein `catch`, das einen Ersatzwert
  zurückgibt, ist eine **sichtbare** Entscheidung und wird nicht gemeldet. Gemeldet wird nur
  der stumme, unbegründete Fall.
- Grenze offen benannt: Für JS/TS ist die Erkennung textbasiert und findet daher nur den
  klar leeren Block. Ein Parser je Sprache wäre genauer und deutlich teurer — für einen
  Hinweis lohnt das nicht.
- Abschaltbar über `flag_swallowed_exceptions` in `.claude/hooks/config.json`.
- Zuordnungstabelle in `guardrails.md` ergänzt (jetzt neun Prüfungen).

Sieben neue Tests (stumm, begründet, weitergeworfen, behandelt — je Sprache — plus der
Schalter). Suite 89 grün. Gegenprobe an echtem Code: `ci_check.py` über alle Hooks und
Werkzeuge meldet nichts, und eine echte `.js`-Datei mit leerem `catch` wird erkannt.

## Kontext

- Klassenzuordnung nach [[ADR-0006 Zwei Klassen von Leitplanken]]: heilbar, also flexibel.
  Wer die Ausnahme bewusst verschluckt, schreibt den Grund in den Code.

## Agent

`claude-code` — Hook, Tests.

## Abhängigkeiten

- [[T-0025 Robustheit als Pflicht des Agenten]] (liefert die Regel, auf die die Meldung zeigt)

## Notizen

- Die Erkennung bleibt textbasiert wie die übrigen Prüfungen. Ein Parser je Sprache wäre
  genauer und deutlich teurer — bei einem Hinweis lohnt das nicht.
