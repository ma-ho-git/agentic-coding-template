---
id: T-0019
title: Leitplanken benennen und klassifizieren
type: task
implements: ["[[REQ-0019 Leitplanken in zwei Klassen]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/agents, topic/meta]
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]"]
---

# T-0019 Leitplanken benennen und klassifizieren

## Anforderung

[[REQ-0019 Leitplanken in zwei Klassen]] — der Teil, der die beiden Klassen benennt, den Zuordnungstest liefert und die Klasse in jeder Meldung sichtbar macht.

## Ziel

Wer eine Regel liest oder eine Meldung sieht, erkennt sofort, ob sie verhandelbar ist.

## Akzeptanzkriterien

- [x] `.claude/rules/guardrails.md` definiert beide Klassen und den vierteiligen
      Zuordnungstest aus dem ADR
- [x] Jede bestehende Prüfung ist einer Klasse zugeordnet, dokumentiert in der Regeldatei
- [x] Jede Hook-Meldung nennt ihre Klasse — blockierende als `[STARR]`, hinweisende als
      `[FLEXIBEL]`, mit Hinweis, dass eine Abweichung bei flexiblen im Code zu begründen ist
- [x] `CLAUDE.md` nennt das Prinzip in den Nicht-Verhandelbaren
- [x] `code-quality.md` weist seine Grenzen als flexibel aus
- [x] Tests decken die neue Meldungsform ab, bestehende Tests bleiben grün

## Kontext

- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[Spec-Driven-Development - was andere Projekte machen]]

## Agent

`claude-code` — Regeldateien und Hook-Code.

## Abhängigkeiten

- keine

## Notizen

- Die Unterscheidung existiert seit [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]
  faktisch, war aber nie benannt. Hier wird sie zum Konzept.
- Sichtbarkeit ist kein Beiwerk: wer Wand und Hinweis nicht unterscheiden kann, behandelt
  am Ende beides als Rauschen.

### 2026-08-20 umgesetzt

- Label sitzt in `block()` und `advise()` in `_common.py`, plus `deny()` im `git_guard.py`.
  Damit erbt **jeder künftige Hook** die Klasse automatisch, sofern er die Helfer benutzt —
  statt sie in fünf Meldungstexte zu kopieren.
- Fünf neue Tests in `tests/hooks/test_guardrail_labels.py`, vorher rot. Suite 68/68;
  die 63 bestehenden blieben unberührt, weil sie auf Teilzeichenketten prüfen.
- **Abweichung vom eigenen Akzeptanzkriterium:** dort stand `[STARR]`/`[FLEXIBEL]`.
  Umgesetzt als `[RIGID]`/`[FLEXIBLE]` — `CLAUDE.md` §7 verlangt Englisch unter `.claude/`,
  und die umgebenden Meldungen sind es auch. Ein deutsches Label in einer englischen Zeile
  liest sich für beide Leser schlechter. Die Zuordnung der Begriffe steht in
  `guardrails.md`.
- `guardrails.md` sagt in eigener Sache die Wahrheit: das Startgate ist als starr
  klassifiziert, aber noch nicht durchgesetzt — nach der Definition der Datei also noch
  nicht starr. Zeile in der Tabelle als „not yet enforced — T-0020" markiert, statt
  vorwegzunehmen, was erst T-0020 baut.
- Nebenbefund beim Verifizieren: der `git_guard` blockierte mein eigenes Prüfskript, weil
  darin ein gefährliches Kommando als **Testdatum** vorkam. Kein Fehler — die Prüfung sieht
  die ganze Kommandozeile und kann Nutzung nicht von Erwähnung unterscheiden. Wer solche
  Fälle prüfen will, baut das Literal zur Laufzeit zusammen.
