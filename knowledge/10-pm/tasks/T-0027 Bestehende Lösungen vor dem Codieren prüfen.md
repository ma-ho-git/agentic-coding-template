---
id: T-0027
title: Bestehende Lösungen vor dem Codieren prüfen
type: task
implements: ["[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/meta, topic/requirements]
related: ["[[T-0028 Startgate verlangt die Fremdlösungs-Entscheidung]]", "[[T-0029 Fremdkomponenten rechtlich absichern]]"]
---

# T-0027 Bestehende Lösungen vor dem Codieren prüfen

## Anforderung

[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]

## Ziel

Bevor der Eigenbau beginnt, wird einmal geschaut, ob es das schon gibt — gemessen an den
vereinbarten Anforderungen, nicht am Bauchgefühl.

## Akzeptanzkriterien

- [ ] Skill `/solution-scan`, im Zyklus zwischen geöffnetem Startgate und erster Codeaufgabe
- [ ] **Kein Kandidat ohne aufgerufene Quelle.** Eine aus dem Gedächtnis genannte Bibliothek
      ist kein Kandidat — das steht als harte Regel im Skill
- [ ] Je Kandidat: Quelle mit Abrufdatum, Lizenz, Wartungsstand (letzte Aktivität), und je
      Rahmenanforderung erfüllt / teilweise / nicht erfüllt, mit REQ-ID
- [ ] Ergebnis als Notiz in `knowledge/20-knowledge/`, Auswahl als ADR — auch wenn die
      Entscheidung „nichts davon" lautet
- [ ] `knowledge/05-requirements/fremdloesungen.md` hält die Entscheidung des Nutzers fest:
      gesucht oder bewusst übersprungen, mit Grund
- [ ] Arbeitszyklus in `CLAUDE.md` §3 und `.claude/rules/workflow.md` ergänzt
- [ ] Routing-Empfehlung auf `researcher` beziehungsweise Cowork, mit Eintrag im Register
      der Subagenten-Entscheidungen

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
