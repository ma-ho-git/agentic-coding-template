---
id: T-0020
title: Startgate als starre Leitplanke durchsetzen
type: task
implements: ["[[REQ-0019 Leitplanken in zwei Klassen]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, stack/python]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0020 Startgate als starre Leitplanke durchsetzen

## Anforderung

[[REQ-0019 Leitplanken in zwei Klassen]] — der Teil, der den Startgate-Übertritt starr durchsetzt.

## Ziel

Solange der Rahmen nicht vereinbart ist, entsteht kein Produktivcode — durchgesetzt, nicht angemahnt.

## Akzeptanzkriterien

- [x] `.claude/hooks/check_gate.py` verweigert Schreibzugriffe auf Produktivcode,
      solange `baseline_status` nicht `vereinbart` ist
- [x] Ausgenommen und in `config.json` konfigurierbar: `.claude/**`, `tools/**`, `tests/**`,
      `examples/**` sowie alles außerhalb der Code-Endungen — Werkzeug, Konfiguration und
      Dokumentation bleiben frei, sonst käme man nicht zum Erheben
- [x] Die Meldung erklärt den Grund, nennt die Klasse `[STARR]` und weist den Weg
      (`/req-elicit`, dann Freigabe durch den Menschen)
- [x] Tests: gesperrter Fall, offenes Gate, jede Ausnahme, fehlende `baseline.md`
      (dann fail closed — gesperrt)
- [x] Hook in `.claude/settings.json` als `PreToolUse` verdrahtet
- [x] Volle Suite grün, dieses Repo arbeitsfähig (sein Code ist Werkzeug und damit ausgenommen)
- [x] `CLAUDE.md` §7 unterscheidet sichtbar zwischen vom Anbieter festgelegten Bezeichnern
      (unverhandelbar englisch) und der eigenen Sprachkonvention für Fließtext

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

### 2026-08-20 umgesetzt

- `check_gate.py` als `PreToolUse(Write|Edit)` verdrahtet. Sieben Tests, vorher rot;
  Suite 75/75.
- Gemeinsamen `deny()`-Helfer nach `_common.py` gezogen und `git_guard.py` darauf
  umgestellt. Damit erben **beide** Vorab-Verweigerer ihr `[RIGID]`-Label aus derselben
  Quelle — das war die Zusage aus T-0019, nicht nur für künftige Hooks.
- Realitätstest gegen den echten Repo-Zustand (Gate geschlossen): `src/*.py` und
  `app/*.ts` verweigert; `.claude/`, `tools/`, `tests/`, `examples/`, `README.md` und der
  Anforderungsbereich erlaubt. Genau die Trennlinie zwischen Werkzeug und Produkt.
- Fehlende `baseline.md` gilt als geschlossen — fail closed nach
  `.claude/rules/security.md`, nicht durchgelassen.
- Pfade außerhalb des Projekts werden ebenfalls verweigert: `relative()` liefert dort
  `../…`, was auf keine Ausnahme passt. Fällt damit ohne Sonderfall auf die sichere Seite.
- **Sprachpräzisierung (mit erledigt):** `CLAUDE.md` §7 unterscheidet jetzt zwischen vom
  Anbieter festgelegten **Bezeichnern** (Event-Namen, JSON-Schlüssel, Frontmatter-Schlüssel,
  Pfade — unverhandelbar, eine Übersetzung bricht sie) und der **eigenen Konvention** für
  Fließtext. Geprüft: alle Anbieter-Bezeichner im Repo sind bereits korrekt. Englischen
  Fließtext verlangt der Anbieter nirgends — das ist unsere Wahl, und ein geklontes Projekt
  darf sie ändern.
