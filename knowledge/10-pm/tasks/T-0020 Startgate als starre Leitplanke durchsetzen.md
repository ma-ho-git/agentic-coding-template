---
id: T-0020
title: Startgate als starre Leitplanke durchsetzen
type: task
implements: ["[[REQ-0019 Leitplanken in zwei Klassen]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, stack/python]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0020 Startgate als starre Leitplanke durchsetzen

## Anforderung

[[REQ-0019 Leitplanken in zwei Klassen]] — der Teil, der den Startgate-Übertritt starr durchsetzt.

## Ziel

Solange der Rahmen nicht vereinbart ist, entsteht kein Produktivcode — durchgesetzt, nicht angemahnt.

## Akzeptanzkriterien

- [ ] `.claude/hooks/check_gate.py` verweigert Schreibzugriffe auf Produktivcode,
      solange `baseline_status` nicht `vereinbart` ist
- [ ] Ausgenommen und in `config.json` konfigurierbar: `.claude/**`, `tools/**`, `tests/**`,
      `examples/**` sowie alles außerhalb der Code-Endungen — Werkzeug, Konfiguration und
      Dokumentation bleiben frei, sonst käme man nicht zum Erheben
- [ ] Die Meldung erklärt den Grund, nennt die Klasse `[STARR]` und weist den Weg
      (`/req-elicit`, dann Freigabe durch den Menschen)
- [ ] Tests: gesperrter Fall, offenes Gate, jede Ausnahme, fehlende `baseline.md`
      (dann fail closed — gesperrt)
- [ ] Hook in `.claude/settings.json` als `PreToolUse` verdrahtet
- [ ] Volle Suite grün, dieses Repo arbeitsfähig (sein Code ist Werkzeug und damit ausgenommen)

## Kontext

- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[Spec-Driven-Development - was andere Projekte machen]]

## Agent

`claude-code` — Hook-Code mit Tests.

## Abhängigkeiten

- [[T-0019 Leitplanken benennen und klassifizieren]] — die Meldungsform kommt von dort

## Notizen

- `PreToolUse` statt `PostToolUse`: die Datei soll gar nicht erst geschrieben werden.
- Fehlt `baseline.md`, wird gesperrt, nicht durchgelassen — fail closed nach
  `.claude/rules/security.md`.
- Achtung beim Bauen: dieses Repository hat selbst ein geschlossenes Gate. Die Ausnahme für
  `tools/**` und `.claude/**` ist die Voraussetzung dafür, hier überhaupt weiterarbeiten zu
  können — das ist kein Schlupfloch, sondern die Grenze zwischen Werkzeug und Produkt.
