---
id: T-0024
title: Szenario trägt die Anforderungserhebung
type: task
implements: ["[[REQ-0022 Das Szenario trägt die weitere Entwicklung]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/meta]
related: ["[[T-0023 Szenario als optionaler Einstieg]]", "[[REQ-0017 Anforderungserhebung vor der Entwicklung]]", "[[ADR-0008 Aus dem Szenario ableiten, ohne zu erfinden]]"]
---

# T-0024 Szenario trägt die Anforderungserhebung

## Anforderung

[[REQ-0022 Das Szenario trägt die weitere Entwicklung]]

## Ziel

Das Szenario darf nicht Dekoration sein. Was daraus abgeleitet wird, bleibt bis zur
Textstelle zurückverfolgbar.

## Akzeptanzkriterien

- [x] `/req-elicit` liest ein vorhandenes Szenario und schlägt Anforderungen daraus ab,
      statt kalt zu fragen
- [x] Jede abgeleitete Anforderung nennt das Szenario in `quelle` **und zitiert die Stelle**,
      aus der sie stammt
- [x] Der Konflikt „Ableiten grenzt an Erfinden" ist im Skill ausdrücklich aufgelöst:
      Zitat sichtbar, Bestätigung des Nutzers vor `vereinbart`
- [x] `/req-validate` meldet jeden Szenario-Bestandteil ohne Anforderung und jede
      Anforderung, die dem Szenario widerspricht
- [x] Rückverfolgungskette in `.claude/rules/requirements.md` beginnt beim Szenario
- [x] `tools/check_traceability.py` meldet ein vorhandenes Szenario, das keine einzige
      Anforderung als Quelle nennt — mit Test
- [x] Die Grenze der maschinellen Prüfung ist benannt: sie prüft die Verbindung,
      nicht die inhaltliche Abdeckung

## Kontext

- [[T-0023 Szenario als optionaler Einstieg]] liefert die Datei, die hier gelesen wird

## Ergebnis

- **Der Zielkonflikt ist aufgelöst, nicht ausgesessen** —
  [[ADR-0008 Aus dem Szenario ableiten, ohne zu erfinden]]. Kern: Gefährlich ist nicht das Hinzufügen, sondern das
  *unsichtbare* Hinzufügen. Jede Ableitung ergänzt etwas — ein Szenario sagt „Dubletten
  raus", eine Anforderung muss sagen, woran eine Dublette erkannt wird. Das ist der Zweck
  der Erhebung, nicht ihr Fehler. Also: vorschlagen, zitieren, bestätigen — und den eigenen
  Zusatz ausdrücklich benennen, als Frage statt als Feststellung.
- `/req-elicit` Abschnitt 3a führt das aus; `## Herkunft` in Vorlage und Regeln nimmt das
  Zitat auf; `quelle` nennt zusätzlich `"[[Szenario]]"`.
- `check_traceability.py`: neuer Fehler, wenn ein Szenario existiert, aus dem keine einzige
  Anforderung abgeleitet wurde. Vier Tests, davon einer für `parse_note`.
- `/req-validate` prüft **beide** Richtungen: unabgedeckte Szenario-Stellen, und — schwerer —
  ein `## Herkunft`-Zitat, das im Szenario gar nicht steht. Das ist eine erfundene Ableitung
  und sieht vereinbart aus.
- Die Grenze der Maschine ist ausgeschrieben: sie prüft die Verbindung, nicht die Abdeckung.
  Prosa lässt sich nicht diffen; alles andere wäre ein falsches Sicherheitsgefühl.
- **Am eigenen Bestand nachgewiesen:** Die Prüfung schlug beim ersten echten Lauf an. 14
  Anforderungen, deren Inhalt sichtbar im Szenario steht, tragen jetzt Quelle und wörtliches
  Zitat; die übrigen 11 nicht — sie stammen aus anderen Quellen, und genau das soll
  unterscheidbar bleiben.

Suite 82 grün (vier neu), `check_vault.py`, `check_traceability.py` und `ci_check.py` ohne
Befund.

## Agent

`claude-code` — Skills, Regeln, Prüfwerkzeug mit Test.

## Abhängigkeiten

- [[T-0023 Szenario als optionaler Einstieg]]

## Notizen

- Kein Szenario vorhanden heißt: alles läuft wie bisher. Der Weg ohne Szenario darf durch
  diese Aufgabe nicht schlechter werden.
