---
id: T-0024
title: Szenario trägt die Anforderungserhebung
type: task
implements: ["[[REQ-0022 Das Szenario trägt die weitere Entwicklung]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[T-0023 Szenario als optionaler Einstieg]]", "[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
---

# T-0024 Szenario trägt die Anforderungserhebung

## Anforderung

[[REQ-0022 Das Szenario trägt die weitere Entwicklung]]

## Ziel

Das Szenario darf nicht Dekoration sein. Was daraus abgeleitet wird, bleibt bis zur
Textstelle zurückverfolgbar.

## Akzeptanzkriterien

- [ ] `/req-elicit` liest ein vorhandenes Szenario und schlägt Anforderungen daraus ab,
      statt kalt zu fragen
- [ ] Jede abgeleitete Anforderung nennt das Szenario in `quelle` **und zitiert die Stelle**,
      aus der sie stammt
- [ ] Der Konflikt „Ableiten grenzt an Erfinden" ist im Skill ausdrücklich aufgelöst:
      Zitat sichtbar, Bestätigung des Nutzers vor `vereinbart`
- [ ] `/req-validate` meldet jeden Szenario-Bestandteil ohne Anforderung und jede
      Anforderung, die dem Szenario widerspricht
- [ ] Rückverfolgungskette in `.claude/rules/requirements.md` beginnt beim Szenario
- [ ] `tools/check_traceability.py` meldet ein vorhandenes Szenario, das keine einzige
      Anforderung als Quelle nennt — mit Test
- [ ] Die Grenze der maschinellen Prüfung ist benannt: sie prüft die Verbindung,
      nicht die inhaltliche Abdeckung

## Kontext

- [[T-0023 Szenario als optionaler Einstieg]] liefert die Datei, die hier gelesen wird

## Agent

`claude-code` — Skills, Regeln, Prüfwerkzeug mit Test.

## Abhängigkeiten

- [[T-0023 Szenario als optionaler Einstieg]]

## Notizen

- Kein Szenario vorhanden heißt: alles läuft wie bisher. Der Weg ohne Szenario darf durch
  diese Aufgabe nicht schlechter werden.
