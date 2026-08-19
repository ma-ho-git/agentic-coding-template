---
title: ADR-0005 Anforderungen als Pflicht vor dem Code
type: decision
tags: [topic/requirements, topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2027-02-19
related: ["[[Sommerville Software Engineering - was das Template übernimmt]]", "[[ADR-0003 Kanban-Board mit Wikilink-Karten]]", "[[T-0012 Anforderungsregeln und Vault-Struktur]]"]
---

# ADR-0005 Anforderungen als Pflicht vor dem Code

## Status

angenommen

## Kontext

- Vorgabe: das Template soll nicht einfach Code schreiben, sondern eine vereinfachte,
  Vibe-Coding-taugliche Fassung von Sommervilles *Software Engineering* durchführen
- Das Template beginnt heute beim Task. Die Kette lautet
  `Task → Test → Code → @contract` — alles vor dem Task fehlt
- Akzeptanzkriterien im Task sind ein **Ersatz** für Anforderungen: sie sagen, wann *diese
  Aufgabe* fertig ist, nie *warum es das System geben soll*
- Niemand fragt den Nutzer je systematisch, was er braucht
- Zielkonflikt: vollständige Anforderungserhebung vor dem ersten Code ist Wasserfall und
  würde Vibe-Coding töten

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Alles vorab spezifizieren | Klassisch korrekt, vollständige Sicht vor dem Bauen | Wasserfall; tötet den iterativen Charakter, der den Nutzen des Templates ausmacht |
| Anforderungen nur empfehlen | Kein Reibungsverlust | Wird übersprungen; genau der Zustand, den diese Entscheidung beheben soll |
| **Inkrementell erheben, Bezug erzwingen** | Anforderungen sind Pflicht, ohne Vorab-Lastenheft | Zwei Artefaktebenen müssen synchron gehalten werden |

## Entscheidung

Anforderungen werden **inkrementell** erhoben. Verbindlich ist nicht „alles vorher",
sondern:

> **Kein Task ohne Rückverweis auf eine vereinbarte Anforderung.**

Konkret:

1. Eigener Vault-Bereich `knowledge/05-requirements/`, eine Datei je Anforderung
   (`REQ-0001 …md`) — analog zu Tasks, aus demselben Grund wie in
   [[ADR-0003 Kanban-Board mit Wikilink-Karten]]: IDs für Rückverfolgbarkeit, eigener
   Status, und keine Datei, die alle Agenten gleichzeitig beschreiben.
2. Jede Anforderung trägt Quelle, Begründung, Priorität und eine **prüfbare** Abnahme.
   Nicht prüfbar formuliert heißt: noch keine Anforderung.
3. Task-Frontmatter bekommt `implements:` mit mindestens einem Anforderungs-Wikilink.
   Ausnahme nur für Infrastruktur-/Wartungsaufgaben, dann mit ausdrücklicher Begründung.
4. Rückverfolgbarkeit in beide Richtungen, maschinell geprüft durch
   `tools/check_traceability.py` in der CI.
5. Durchsetzung auf Task-Ebene per Hook. Code-Schreibzugriffe werden **nicht** blockiert —
   das wäre laut und träfe das template-eigene Tooling.

Die Kette lautet damit:

```
Stakeholder → REQ-XXXX → T-XXXX → Test → Code (@contract)
```

## Konsequenzen

- `/bootstrap` erhebt bei einem neuen Projekt zuerst Anforderungen, nicht Tasks
- `/task-new` verlangt den Anforderungsbezug, `/task-next` prüft ihn, `/task-done` prüft
  die Abnahme der Anforderung
- Neue Skills `/req-elicit`, `/req-validate`, `/req-change`; letzterer ist das Gegenstück
  zu `/contract-sync`, eine Ebene höher
- Zwei Ebenen können auseinanderlaufen — dafür existiert die Traceability-Prüfung, so wie
  `/board-sync` das für Board und Task-Frontmatter tut
- Mehr Schreibarbeit je Projekt. Bewusst in Kauf genommen: ohne Anforderung ist die
  Akzeptanzprüfung eines Tasks eine Selbstauskunft des Agenten
- Qualitätsanforderungen treiben ab jetzt Architekturentscheidungen (`/architecture`),
  statt dass ADRs ad hoc entstehen

## Revidieren wenn

- Sich zeigt, dass der Anforderungsbezug in der Praxis nur pro forma gesetzt wird —
  dann ist die Regel wirkungslos und braucht eine andere Durchsetzung
- Projekte dieser Größe die Ein-Ebenen-Vereinfachung (Nutzer- und Systemanforderung
  zusammengelegt) nicht mehr tragen
