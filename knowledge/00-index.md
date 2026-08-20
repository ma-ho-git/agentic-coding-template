---
title: Index
type: knowledge
tags: [topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-20
review_after: 2027-02-19
related: ["[[Konventionen der Wissensdatenbank]]"]
---

# Wissensdatenbank — Index

> **Projekt:** Agentic Coding Template
> **Zweck:** Vorlage für strukturiertes Vibe-Coding mit Claude Code und Claude Cowork.
>
> *Beim Start eines eigenen Projekts: diese beiden Zeilen ersetzen.*

Einstiegspunkt des Vaults. Jede Notiz ist von hier aus erreichbar — direkt oder über eine
Themennotiz. Waisen sind ein Fehler und gehören repariert.

## Anforderungen

Der Rahmen steht vor dem ersten Code — Regeln in `.claude/rules/requirements.md`.

- [[Szenario]] — das Vorhaben in den Worten des Nutzers, Grundlage der Erhebung
- [[Rahmen und Startgate]] — **entscheidet, ob entwickelt werden darf**
- [[Projektvision]] — Problem, Zielartefakt, Erfolgskriterien, Nicht-Ziele
- [[Stakeholder]] — wer beteiligt ist und wer entscheidet
- [[Glossar]] — verbindliches Vokabular, auch für die Benennung im Code
- [[Methodenglossar]] — die Begriffe des Verfahrens, für den Einstieg ohne Vorkenntnisse
- [[Fremdlösungen]] — ob vor dem Codieren nach einer bestehenden Lösung gesucht wurde
- [[Fremdkomponenten]] — übernommener Fremdcode und die geerbten Lizenzpflichten
- [[Randbedingungen]] — was von außen feststeht
- [[Risiken]] — was das Projekt gefährdet, und was dagegen läuft
- Einzelanforderungen: `05-requirements/REQ-XXXX ….md`

## Projektmanagement

- [[board|Kanban-Board]] — aktueller Stand aller Aufgaben
- Aufgaben: `10-pm/tasks/` — eine Datei je Task, Wahrheit ist das `status`-Feld
- Fortschritt: [[2026-08|Fortschritt 2026-08]]

### Entscheidungen (ADR)

- [[ADR-0001 Regeln aufteilen statt eine große CLAUDE.md]]
- [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]
- [[ADR-0003 Kanban-Board mit Wikilink-Karten]]
- [[ADR-0004 Cowork über ein leichtes Paket anbinden]]
- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[ADR-0006 Zwei Klassen von Leitplanken]]
- [[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]]
- [[ADR-0008 Aus dem Szenario ableiten, ohne zu erfinden]]
- [[ADR-0009 Fehlerbehandlung ändert die Form, nicht die Grenze]]
- [[ADR-0010 Eigene Umsetzung statt Fremdbasis]]
- [[ADR-0011 Das Startgate hat zwei Bedingungen]]

## Projektwissen

### Agenten und Werkzeuge

- [[Konfigurationsebenen von Claude Code]] — welche Ebene lädt wann, und was das kostet
- [[Cowork liest die Repo-Konfiguration nicht]] — die zentrale Einschränkung für das Routing
- [[Spec-Driven-Development - was andere Projekte machen]] — Marktumschau und Abgrenzung

### Wissensdatenbank und Format

- [[Konventionen der Wissensdatenbank]] — Ablage, Frontmatter, Tags, Verlinkung
- [[Obsidian-Kanban Dateiformat]] — verifiziertes Board-Format und Wartungslage

### Code und Dokumentation

- [[Dokumentationsstandards je Sprache]] — Vorauswahl je Sprache, samt ihrer Belastbarkeit

### Anforderungen und Vorgehen

- [[Funktionale und nicht-funktionale Anforderungen]] — warum beide anders erhoben werden,
  und was die Prüfung des eigenen Bestands ergab
- [[Sommerville Software Engineering - was das Template übernimmt]] — welche Konzepte
  übernommen werden, in welcher Vereinfachung, und was bewusst wegbleibt

## Troubleshooting

- [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]]
- [[SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest]]
- [[matches_any() exemption trifft falsche Pfade]]
- [[Wikilink über Zeilenumbruch wird nicht erkannt]]

## Meta

- [[Konventionen der Wissensdatenbank]] — verbindlich für alle Notizen
- [[Umgebungs-Manifest]] — externe Annahmen des Templates mit Prüfdatum
- [[Register der Subagenten-Entscheidungen]] — Kosten-/Nutzenprüfungen mit Ergebnis
- Templates: `90-meta/templates/`

## Tag-Übersicht

`topic/meta` · `topic/agents` · `stack/claude-code` · `stack/cowork` · `stack/obsidian`
· `stack/github` · `stack/python` · `stack/typescript`

Neue Namespaces zuerst in [[Konventionen der Wissensdatenbank]] eintragen.
