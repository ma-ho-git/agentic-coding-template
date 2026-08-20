---
title: Spec-Driven-Development - was andere Projekte machen
type: knowledge
tags: [topic/requirements, topic/agents]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2026-11-20
related: ["[[ADR-0006 Zwei Klassen von Leitplanken]]", "[[Sommerville Software Engineering - was das Template übernimmt]]", "[[00-index]]"]
---

# Spec-Driven-Development - was andere Projekte machen

## Kurz

Marktumschau vor dem Ausbau des Leitplanken-Konzepts. Beantwortet: gibt es das schon, was
können wir übernehmen, und wo ist unser Ansatz tatsächlich stärker.

## Kernpunkte — Begriffe

- **Vibe Coding** (Karpathy): prompten, Ergebnis übernehmen, laufen lassen — ohne den Code
  zu lesen.
- **Vibe Engineering** (Simon Willison, Oktober 2025): diszipliniertes Arbeiten mit
  Coding-Agenten. Jeder Diff wird gelesen, alles läuft über Versionskontrolle, Tests sind
  Pflicht, Verantwortung bleibt beim Menschen.
- Willison selbst schreibt im Mai 2026, dass die Grenze in seiner eigenen Arbeit
  verschwimmt — der Begriff beschreibt eine Haltung, keine erzwungene Praxis. **Genau diese
  Lücke füllt eine Werkzeugkette mit Durchsetzung.**

## Kernpunkte — die Projekte

| Projekt | Größe | Kern |
| --- | --- | --- |
| GitHub Spec Kit | ~93k Sterne, MIT, Claude-Code-tauglich | CLI, Ablauf `constitution → specify → clarify → plan → tasks → implement` |
| BMAD-Method | ~48k Sterne | Benannte Agentenrollen (Architect, PM, QA, Dev), harte Rollengrenzen, „Constitution" |
| AWS Kiro | kommerziell, IDE | Spec-first als IDE, Modell-Routing je Aufgabe |
| OpenSpec | kleiner | leichtgewichtige Alternative |

Berichtete Wirkung von SDD laut Anbietern: drei- bis zehnfach höhere Erstlauf-Trefferquote
bei nicht-trivialen Aufgaben. **Anbieterangabe, nicht unabhängig geprüft.**

## Was wir übernehmen sollten

- **`/clarify` als eigener Schritt** vor der Planung: unterspezifizierte Stellen gezielt
  auflösen. Wir erledigen das bisher nebenbei in `/req-elicit`.
- **Generierte Checklisten je Projekt** statt einer festen Prüfliste (Spec Kit
  `/checklist`).
- **Konsistenzprüfung über Artefakte hinweg** (Spec Kit `/analyze`) — bei uns bereits als
  Code vorhanden (`tools/check_traceability.py`), also stärker.

## Wo unser Ansatz stärker ist

Spec Kits **Constitution ist reine Prosa ohne Durchsetzung**. BMAD ebenso. Das ist genau die
Schwäche, die [[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]] adressiert.

Die Guardrails-Literatur bestätigt das Modell ausdrücklich in drei Schichten:

1. **Soft Guardrails** — Anweisungen in natürlicher Sprache. Schwächste Schicht, durch
   Umformulierung oder Prompt-Injection umgehbar.
2. **Traffic Screening** — Laufzeitprüfung bewegter Daten. Für Coding-Agenten kaum relevant.
3. **Hard Boundaries** — deterministisch, im Code oder in der Infrastruktur. Vom Modell
   nicht überschreibbar.

Claude-Code-Hooks mit **Exit-Code 2** sind Schicht 3: der Agent kann sie nicht überstimmen.
Empfehlung der Literatur wörtlich sinngemäß: blockieren bei den Grenzen, die nie nachgeben
dürfen — warnen bei den weicheren Konventionen.

## Was uns fehlt (Stand der Umschau)

- Keines der Projekte adressiert **unerfahrene Anwender**. Alle setzen voraus, dass jemand
  eine Anforderung beurteilen kann. Das ist unsere Zielgruppen-Lücke, nicht nur unsere.
- Keines kennt **Proportionalität**: Wegwerfskript und Produkt bekommen dieselbe Zeremonie.

## Quellen

- https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/ — abgerufen 2026-08-20
- https://github.com/github/spec-kit — Ablauf und Kommandos, abgerufen 2026-08-20
- https://www.marktechpost.com/2026/05/08/9-best-ai-tools-for-spec-driven-development-in-2026-kiro-bmad-gsd-and-more-compare/ — abgerufen 2026-08-20
- https://idanhabler.medium.com/building-safer-agents-soft-guardrails-hard-boundaries-and-the-layers-between-14205d709b93 — Drei-Schichten-Modell, abgerufen 2026-08-20
- https://dev.to/aws/ai-agent-guardrails-rules-that-llms-cannot-bypass-596d — Durchsetzung per Hook, abgerufen 2026-08-20
- Sternzahlen und Versionsangaben stammen aus den Übersichtsartikeln, nicht aus der
  GitHub-API — als Größenordnung zu lesen.
