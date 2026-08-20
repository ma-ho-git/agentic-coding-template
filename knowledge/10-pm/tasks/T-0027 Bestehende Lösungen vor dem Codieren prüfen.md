---
id: T-0027
title: Bestehende Lösungen vor dem Codieren prüfen
type: task
implements: ["[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/requirements]
related: ["[[T-0028 Startgate verlangt die Fremdlösungs-Entscheidung]]", "[[T-0029 Fremdkomponenten rechtlich absichern]]", "[[ADR-0010 Eigene Umsetzung statt Fremdbasis]]"]
---

# T-0027 Bestehende Lösungen vor dem Codieren prüfen

## Anforderung

[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]

## Ziel

Bevor der Eigenbau beginnt, wird einmal geschaut, ob es das schon gibt — gemessen an den
vereinbarten Anforderungen, nicht am Bauchgefühl.

## Akzeptanzkriterien

- [x] Skill `/solution-scan`, im Zyklus zwischen geöffnetem Startgate und erster Codeaufgabe
- [x] **Kein Kandidat ohne aufgerufene Quelle.** Eine aus dem Gedächtnis genannte Bibliothek
      ist kein Kandidat — das steht als harte Regel im Skill
- [x] Je Kandidat: Quelle mit Abrufdatum, Lizenz, Wartungsstand (letzte Aktivität), und je
      Rahmenanforderung erfüllt / teilweise / nicht erfüllt, mit REQ-ID
- [x] Ergebnis als Notiz in `knowledge/20-knowledge/`, Auswahl als ADR — auch wenn die
      Entscheidung „nichts davon" lautet
- [x] `knowledge/05-requirements/fremdloesungen.md` hält die Entscheidung des Nutzers fest:
      gesucht oder bewusst übersprungen, mit Grund
- [x] Arbeitszyklus in `CLAUDE.md` §3 und `.claude/rules/workflow.md` ergänzt
- [x] Routing-Empfehlung auf `researcher` beziehungsweise Cowork, mit Eintrag im Register
      der Subagenten-Entscheidungen

## Ergebnis

- Skill `/solution-scan`, im Zyklus zwischen geöffnetem Gate und erster Codeaufgabe;
  `CLAUDE.md` §3, `.claude/rules/workflow.md` und README ergänzt.
- **Harte Regel: kein Kandidat ohne in dieser Sitzung abgerufene Quelle.** Eine aus dem
  Gedächtnis genannte Bibliothek kann umbenannt, aufgegeben oder verschmolzen sein — oder nie
  in dieser Form existiert haben. Eine ungeprüfte Empfehlung ist schlimmer als keine, weil
  ihr geglaubt wird. Lässt sie sich nicht abrufen, ist sie kein Kandidat.
- **Die Einsicht, die die Bewertung trägt: „erfüllt 80 % der Anforderungen" sagt nichts.**
  Entscheidend ist, *welche* 20 % fehlen. Fehlt der Grund, aus dem das Projekt überhaupt
  existiert, ist auch ein Kandidat mit 90 % wertlos; fehlt ein Berichtsformat, können 60 %
  ausgezeichnet sein.
- **Zweite Einsicht: ein totes Projekt mit gutem README ist schlimmer als kein Kandidat.**
  Es sieht nach Abkürzung aus und wird zur Wartungslast, die dann die eigene ist. Datum
  schlägt Sternchen.
- Fünf Pflichtfelder je Kandidat: Quelle mit Abrufdatum, Lizenz, Wartungsstand,
  Anforderungsabgleich je REQ-ID, Übernahmekosten.
- Entscheidung als ADR **auch bei „nichts davon"** — das ist der Fall, der sonst unbegründet
  bleibt, und die Frage „warum haben wir das selbst gebaut?" verdient eine Antwort.
- `knowledge/05-requirements/fremdloesungen.md` hält den Status maschinenlesbar
  (`scan_status: gesucht | uebersprungen | offen`); die Durchsetzung folgt in
  [[T-0028 Startgate verlangt die Fremdlösungs-Entscheidung]].
- Am eigenen Projekt vorgeführt: Die Umschau aus T-0019 ist der Befund,
  [[ADR-0010 Eigene Umsetzung statt Fremdbasis]] die nachgezogene Entscheidung. Begründung
  ist genau die 80/20-Frage — Spec Kit und BMAD erfüllen den Ablauf, aber nicht
  [[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]], und das ist der Kern.
- Subagenten-Register ergänzt: Abrufen delegieren, **Urteilen nicht**.

Suite 89 grün (unverändert — Skill und Dokumentation), Vault- und
Rückverfolgbarkeitsprüfung ohne Befund.

## Kontext

- Der Zeitpunkt ist der Punkt: vorher fehlen die Anforderungen, hinterher gewinnt der
  Eigenbau, weil er schon dasteht
- Haltungsvorbild ist `/req-elicit`: nichts erfinden, Unsicheres als unsicher ausweisen

## Agent

`claude-code` für den Skill. Die Recherche selbst gehört zu `researcher` oder Cowork.

## Abhängigkeiten

- keine (setzt inhaltlich einen vereinbarten Rahmen voraus, nicht eine andere Aufgabe)

## Notizen

- Der Skill darf keine Empfehlung aussprechen, die er nicht belegen kann. Ein Kandidat mit
  unklarer Lizenz oder totem Wartungsstand wird genannt und begründet abgelehnt, nicht
  verschwiegen.
