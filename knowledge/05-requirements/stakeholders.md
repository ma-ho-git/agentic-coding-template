---
title: Stakeholder
aliases: ["Stakeholder", "stakeholders"]
type: knowledge
tags: [topic/requirements]
status: active
created: 2026-08-19
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Projektvision]]", "[[Rahmen und Startgate]]", "[[00-index]]"]
---

# Stakeholder

> **Für ein eigenes Projekt:** diese Datei vollständig ersetzen. Der Inhalt beschreibt die
> Beteiligten **dieses Templates** und dient als ausgefülltes Beispiel.

## Kurz

Wer ein Interesse am System hat, was er davon braucht, und **wer entscheidet**. Jede
Anforderung nennt im Feld `quelle` einen Eintrag aus dieser Liste — ohne Quelle keine
Rückverfolgbarkeit.

## Übersicht

| Rolle | Wer | Interesse | Entscheidet über |
| --- | --- | --- | --- |
| Auftraggeber, Autor | Marcus | Template, das strukturiertes Vibe-Coding erzwingt statt es zu empfehlen | Umfang, Prioritäten, Regelwerk, Startgate |
| Verwender | wer das Repo klont | schneller, verlässlicher Projektstart ohne eigene Einrichtungsarbeit | eigenen Projektzuschnitt, eigene Schwellwerte |
| Claude Code | Agent | ausführbare, widerspruchsfreie Regeln; Zugriff auf Board und Wissensdatenbank | nichts — schlägt vor, setzt um |
| Claude Cowork | Agent | dieselben Regeln, aber ohne Repo-Konfiguration erreichbar | nichts |

## Wer nicht gefragt wurde

- **Teams ab drei Personen.** Das Template ist auf einen Menschen mit ein bis zwei Agenten
  zugeschnitten. Rollen-, Freigabe- und Konfliktprozesse für Teams fehlen bewusst.
- **Betreiber ausgelieferter Software.** Das Template begleitet die Entwicklung, nicht den
  Betrieb des damit gebauten Systems.
- **Nutzer anderer Coding-Agenten.** Regeln liegen in Claude-Code-Format
  (`.claude/rules/`, Hooks); Übertragbarkeit wurde nicht geprüft.

## Entscheidungswege

Bei Zielkonflikten zwischen Anforderungen entscheidet **Marcus**. Agenten benennen den
Konflikt, schlagen eine Auflösung vor und halten sie als ADR fest — sie entscheiden ihn nicht
selbst. Das Startgate in [[Rahmen und Startgate]] öffnet ausschließlich der Mensch.

## Offene Fragen

- keine
