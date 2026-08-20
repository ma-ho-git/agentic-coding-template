---
id: T-0040
title: Übergabe hinterlässt leere Formulare
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/requirements]
related: ["[[T-0038 Übergabe von der Vorlage zum Projekt]]", "[[T-0034 Erstlauf im frischen Klon durchspielen]]"]
---

# T-0040 Übergabe hinterlässt leere Formulare

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — Befund 4 aus
[[T-0034 Erstlauf im frischen Klon durchspielen]].

## Ziel

Nach der Übergabe tragen **sieben** Rahmendokumente weiter den Inhalt der Vorlage: Rahmen,
Vision, Randbedingungen, Glossar, Risiken, Stakeholder, Fremdlösungen und Fremdkomponenten.
`baseline.md` behauptet das Zielartefakt der Vorlage und verlinkt 36 Anforderungen, die ins
Archiv zeigen.

Der Schaden ist begrenzt — geschlossenes Gate, Platzhalter-Marker —, aber das Risiko ist
real: Ein Agent **schreibt in die vorhandenen Kategorielisten hinein**, statt sie zu
ersetzen. Dann steht im Rahmen des neuen Projekts eine Mischung aus zwei Vorhaben.

Ein leeres Formular mit Ausfüllhinweisen ist für einen Anfänger auch schlicht verständlicher
als das ausgefüllte Formular eines fremden Projekts.

## Akzeptanzkriterien

- [x] `handover --apply` ersetzt die Rahmendokumente durch Skelette: Struktur und
      Ausfüllhinweise, kein fremder Inhalt
- [x] Die Skelette behalten Titel, Aliasse und Frontmatter, damit Wikilinks und
      `check_vault.py` weiter tragen — insbesondere `[[Rahmen und Startgate]]`
- [x] Gate-Marker in den Skeletten: `baseline_status: entwurf`, `scan_status: offen`
- [x] Der Platzhalter-Marker bleibt in jedem Skelett, damit `handover --check` das Ausfüllen
      weiterhin einfordert
- [x] Nach `--apply` in einem frischen Klon: `check_vault.py` und `check_traceability.py`
      ohne Befund, keine Waisen, keine kaputten Links
- [x] Tests je Dokument; zusätzlich ein Test, dass zweimaliges `--apply` nichts kaputt macht
- [x] Am echten Klon nachgewiesen, nicht nur an Testdoppeln

## Kontext

- Preis der Entscheidung: Der Klon verliert die ausgefüllte `baseline.md` als
  Anschauungsmaterial. Vertretbar — das Archiv behält 78 ausgefüllte Dokumente samt aller
  Anforderungen und ADRs, und die Vorlage auf GitHub behält ihre eigenen.

## Agent

`claude-code` — Werkzeug, Skelettinhalte, Tests.

## Abhängigkeiten

- [[T-0038 Übergabe von der Vorlage zum Projekt]]

## Ergebnis

- `tools/handover_texts.py` — alle acht Skelette plus die beiden schon vorhandenen
  Dokumentvorlagen (Archiv-README, leeres Board). Eigene Datei, weil es Literale sind und
  `handover.py` sonst über die Dateilängen-Grenze läuft.
- `handover.py` schreibt sie in `apply()`; ein zweiter `--apply` ist ein No-op und kann die
  Antworten des Projekts nicht mehr durch ein leeres Formular ersetzen.
- `pending()` und `unfilled()` trennen zwei Fragen, die vorher eine waren: *noch die
  Vorlage* (blockiert, nur `--apply` behebt es) gegen *noch nicht ausgefüllt* (Arbeit des
  Projekts; nur die vier Kerndokumente blockieren).
- `reset_field()` entfällt — die Skelette bringen `entwurf`/`offen` selbst mit. Das Verhalten
  prüft weiterhin `test_apply_resets_both_gate_markers`.

## Nachweis am echten Klon

`git clone` des Branches, `--apply`, dann:

| Prüfung | Ergebnis |
| --- | --- |
| `check_vault.py` | 0 Fehler, 0 Warnungen — keine Waisen, keine kaputten Links |
| `check_traceability.py` | 0 Fehler, 0 Warnungen |
| `handover.py` (check) | keine `PENDING`-Zeile mehr; 11 Formulare als To-do, davon 4 Kern |
| `check_gate.py` gegen `src/app.py` | `deny`, `[RIGID] Start gate closed` |
| Testsuite | 154 grün |

## Notizen

- Nicht ins Archiv verschieben: `baseline.md` und `vision.md` heißen dort genauso, und
  Obsidian löst Wikilinks über den Namen auf — `[[Rahmen und Startgate]]` würde mehrdeutig.
  Deshalb ersetzen statt umziehen.
- Die Skelette sind zugleich die beste Stelle, um einem Anfänger zu sagen, **was** in das
  Dokument gehört. Ausfüllhinweise sind hier kein Beiwerk, sondern der halbe Zweck.
