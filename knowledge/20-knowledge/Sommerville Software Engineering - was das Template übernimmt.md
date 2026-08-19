---
title: Sommerville Software Engineering - was das Template übernimmt
type: knowledge
tags: [topic/requirements, topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-08-19
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[00-index]]"]
---

# Sommerville Software Engineering - was das Template übernimmt

## Kurz

Grundlage für den Anforderungsteil des Templates: Ian Sommerville, *Software Engineering*,
10. Auflage. Diese Notiz hält fest, **welche** Konzepte übernommen werden, in welcher
Vereinfachung — und was bewusst wegbleibt.

## Kernpunkte — Kapitel 4, Requirements Engineering

- Zwei Ebenen: **Nutzeranforderungen** (natürliche Sprache, für Auftraggeber) und
  **Systemanforderungen** (detailliert, strukturiert). Template führt sie zu **einer**
  Ebene zusammen — für Projekte dieser Größe ist die Trennung Ballast.
- **Funktional** = was das System leistet. **Nicht-funktional** = Randbedingungen und
  Qualitäten. Sommerville betont: NFRs sind oft kritischer als FRs, weil ihre Verletzung
  das System unbrauchbar macht, nicht nur unvollständig.
- NFR-Klassifikation: **Produkt** (Bedienbarkeit, Effizienz, Zuverlässigkeit, Sicherheit),
  **Organisation** (Umgebung, Betrieb, Entwicklungsprozess), **extern** (Recht, Ethik,
  Regulierung).
- Prozessschritte: **Elicitation → Spezifikation → Validierung → Änderungsverwaltung**.
- Die fünf Validierungsprüfungen (wörtlich übernommen, sie sind der Kern von `/req-validate`):

  | Prüfung | Frage |
  | --- | --- |
  | Gültigkeit (validity) | Leistet das System die Funktionen, die den Bedarf am besten decken? |
  | Konsistenz (consistency) | Gibt es Widersprüche zwischen Anforderungen? |
  | Vollständigkeit (completeness) | Sind alle vom Kunden benötigten Funktionen enthalten? |
  | Realismus (realism) | Umsetzbar mit verfügbarem Budget und verfügbarer Technik? |
  | Prüfbarkeit (verifiability) | Lässt sich die Anforderung überhaupt prüfen? |

- **Prüfbarkeit ist die Schlüsselregel für Agenten.** Eine nicht messbare Anforderung
  („benutzerfreundlich") lässt sich weder testen noch abnehmen. Messbar formuliert
  („geübter Nutzer schließt Aufgabe X in unter 30 s ab") dockt direkt an TDD an.
- Jede Anforderung braucht eine **Quelle** (welcher Stakeholder) und eine **Begründung**.
  Ohne Quelle ist Rückverfolgbarkeit unmöglich, ohne Begründung entsteht Cargo-Cult.
- **Traceability**: Anforderungen müssen vorwärts (zu Design und Code) und rückwärts
  (zum Stakeholder) verfolgbar sein.

## Kernpunkte — Kapitel 6, Architectural Design

- Qualitätsanforderungen treiben die Architektur, und sie **widersprechen einander**:
  Performanz will wenige große Komponenten, Wartbarkeit viele kleine; Sicherheit will
  Schichten, Performanz will kurze Wege.
- Architekturmuster als Vokabular: Schichten, Repository, Client-Server, MVC,
  Pipe-and-Filter.
- Template-Umsetzung: kein eigenes Architekturdokument, sondern ein ADR je Entscheidung —
  ausgelöst durch die Qualitätsanforderungen, siehe `/architecture`.

## Was das Template bewusst NICHT übernimmt

Damit niemand das hier für eine vollständige Sommerville-Umsetzung hält:

- Kap. 5 Systemmodellierung (UML, Kontext-/Interaktions-/Strukturmodelle) — optional,
  nicht verpflichtend
- Kap. 15–21: Wiederverwendung, komponentenbasierte SE, verteilte SE, SOA,
  Systems of Systems, Echtzeit-SE
- Kap. 11–14: Zuverlässigkeits-, Sicherheits- und Resilienz-*Engineering* als eigene
  Disziplinen (Sicherheit bleibt auf dem Niveau von `.claude/rules/security.md`)
- Formale Spezifikation
- Aufwandsschätzung (COCOMO) und klassische Projektplanung aus Kap. 23
- Konfigurationsmanagement aus Kap. 25 — git deckt das ab

## Vereinfachungen für Vibe-Coding

- **Inkrementell statt Wasserfall.** Anforderungen werden nach und nach erhoben. Verbindlich
  ist nicht „alles vorher", sondern „kein Task ohne Anforderungsbezug".
- Markdown statt IEEE-830-Struktur.
- Eine Anforderung ist ein paar Zeilen, keine Seite.
- Strukturprüfung maschinell (`tools/check_traceability.py`) statt durch Review-Sitzungen.

## Quellen

- Ian Sommerville, *Software Engineering*, 10. Auflage, Pearson —
  https://www.pearson.com/en-us/subject-catalog/p/software-engineering/P200000003258/9780137503148
  — abgerufen 2026-08-19
- Sommerville, Foliensatz „Requirements Engineering Processes", Kapitel 6 (ältere Auflage),
  https://ccs.neu.edu/home/lieber/com3205/f02/lectures/sommerville/ch06.ppt — abgerufen 2026-08-19
  (Quelle für den Wortlaut der fünf Validierungsprüfungen)
- Die NFR-Klassifikation (Produkt/Organisation/extern) und die Trennung Nutzer-/
  Systemanforderungen stammen aus dem Lehrbuchtext selbst und wurden **nicht** gegen eine
  Onlinequelle gegengeprüft — als Standardinhalt der 10. Auflage geführt.
