---
id: T-0028
title: Startgate verlangt die Fremdlösungs-Entscheidung
type: task
implements: ["[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/agents]
related: ["[[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]", "[[T-0020 Startgate als starre Leitplanke durchsetzen]]", "[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[ADR-0011 Das Startgate hat zwei Bedingungen]]"]
---

# T-0028 Startgate verlangt die Fremdlösungs-Entscheidung

## Anforderung

[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]] — „muss angeboten werden",
maschinell durchgesetzt.

## Ziel

Ein Schritt, der nur in Prosa steht, ist die weichste Leitplanke — das hat dieses Projekt
bei [[T-0020 Startgate als starre Leitplanke durchsetzen]] schon einmal gelernt.

## Akzeptanzkriterien

- [x] `check_gate.py` verweigert Schreibzugriff auf Produktivcode, solange keine
      Entscheidung über die Fremdlösungs-Suche festgehalten ist
- [x] Die Meldung nennt, **welche** der beiden Bedingungen fehlt — Rahmen oder Entscheidung —
      und den einen Schritt, der sie erfüllt
- [x] Erfüllbar durch eine bewusste Ablehnung mit Grund; Suchen ist nicht erzwungen
- [x] Ausnahmen bleiben wie gehabt: Werkzeug, Tests, Beispiele, alles außerhalb von Quellcode
- [x] Tests: beide Bedingungen einzeln und gemeinsam, Ausnahmepfade unverändert grün
- [x] `.claude/rules/guardrails.md` führt die Prüfung in der Zuordnungstabelle
- [x] ADR hält die Zuordnung fest: unheilbar, weil der fertige Eigenbau die Entscheidung
      faktisch vorwegnimmt

## Ergebnis

- `check_gate.py` prüft zwei Bedingungen: Rahmen vereinbart, und Fremdlösungs-Frage
  beantwortet (`scan_status` ist `gesucht` oder `uebersprungen`).
- **Die Reihenfolge ist keine Geschmacksfrage.** Rahmen zuerst — ohne vereinbarte
  Anforderungen fehlt der Maßstab, an dem ein Kandidat gemessen würde. Zuerst nach
  Fremdlösungen zu fragen hieße, nach etwas zu suchen, das noch niemand beschrieben hat.
- Die Meldung nennt immer nur die **eine** fehlende Bedingung und den einen Schritt, der sie
  erfüllt. Zwei Wände auf einmal zu zeigen hilft niemandem.
- **Kein Zwang zur Suche:** `uebersprungen` öffnet das Gate. Verlangt wird eine Antwort,
  keine Suche.
- **Ehrlich bei der Einordnung** ([[ADR-0011 Das Startgate hat zwei Bedingungen]]): Starr
  wird die Prüfung über Kriterium 4 des Zuordnungstests — die Entscheidung ist dem Menschen
  vorbehalten. Kriterium 1 „unheilbar" trifft **nicht im strengen Sinn**; man kann später
  noch eine Bibliothek übernehmen. Praktisch gewinnt der Eigenbau durch Trägheit, und das
  verstärkt die Begründung, trägt sie aber nicht allein. Das steht so im ADR, damit niemand
  später einen strengeren Grund unterstellt, als vorliegt.
- Ausnahmen unverändert: Werkzeug, Tests, Beispiele, Dokumentation und der
  Anforderungsbereich bleiben schreibbar.
- `guardrails.md` führt jetzt zehn Prüfungen, die Gate-Zeile ist in zwei aufgeteilt.

Sechs neue Tests (beide Bedingungen einzeln und gemeinsam, Ausnahmepfade, Meldungstext).
Suite 95 grün. Beide Meldungen an einem echten Aufruf geprüft — im Repo selbst greift die
Rahmen-Bedingung, in einem Probeverzeichnis mit offenem Rahmen die zweite.

## Kontext

- Entscheidung des Auftraggebers vom 2026-08-20: Startgate erweitern statt Prozessschritt
- [[T-0027 Bestehende Lösungen vor dem Codieren prüfen]] liefert die Datei, die hier
  gelesen wird

## Agent

`claude-code` — Hook, Tests, Regeln.

## Abhängigkeiten

- [[T-0027 Bestehende Lösungen vor dem Codieren prüfen]]

## Notizen

- Die Prüfung darf nicht zur Formalie verkommen. Sie kann nur die Verbindung prüfen, nicht
  die Ernsthaftigkeit der Begründung — das ist dieselbe Grenze wie beim Projektzuschnitt und
  gehört ausdrücklich in die Regel geschrieben.
