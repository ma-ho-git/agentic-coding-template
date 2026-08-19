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
| Rein inkrementell erheben | Kein Vorab-Lastenheft | **Zielartefakt bleibt zu unsicher beschrieben.** Rahmensetzende Anforderungen (Technik, Recht, Sicherheit) tauchen zu spät auf und entwerten fertige Arbeit |
| **Rahmen vorab, Details je Stufe** | „Das Große" steht, bevor gebaut wird; Details bleiben beweglich | Zwei Ebenen und ein Gate müssen gepflegt werden |

## Entscheidung

Anforderungen haben **zwei Ebenen**. Verbindlich ist:

> **Der Rahmen steht vor dem ersten Code. Details kommen je Entwicklungsstufe.
> Kein Task ohne Rückverweis auf eine vereinbarte Anforderung.**

### Ebene 1 — Rahmenanforderungen (`ebene: rahmen`)

Vollständig zu klären, **bevor** die erste Zeile Produktivcode entsteht. Sie beantworten:
*Was wird gebaut, und was muss dabei gelten?* Kategorien:

| Kategorie | Beispiel |
| --- | --- |
| `funktional` | Kernleistung des Systems, grob |
| `technisch` | Plattform, Schnittstellen, Datenhaltung, Performanz |
| `organisatorisch` | Betrieb, Rollen, Auslieferung, Prozess |
| `sicherheit` | Schutzbedarf, Authentisierung, Datenschutz |
| `recht` | Regulierung, Lizenzen, Aufbewahrung |
| `qualitaet` | Bedienbarkeit, Zuverlässigkeit, Wartbarkeit |

Diese Anforderungen sind architekturprägend: wer sie spät entdeckt, wirft fertige Arbeit weg.

### Ebene 2 — Detailanforderungen (`ebene: detail`)

Je Entwicklungsstufe bedarfsgerecht erhoben, **nicht auf Vorrat**. Beim Codieren dürfen sie
iterativ nachgeschärft werden: Präzisierung ohne Aussageänderung wird in der Anforderung
protokolliert, eine echte Aussageänderung läuft über `/req-change`.

### Das Startgate

`knowledge/05-requirements/baseline.md` trägt `baseline_status: entwurf | vereinbart`.
Erst auf `vereinbart` beginnt die Entwicklung. Der Rahmen gilt als vollständig, wenn **jede**
Kategorie oben entweder mindestens eine vereinbarte Rahmenanforderung hat **oder**
ausdrücklich als nicht zutreffend begründet ist.

Beides ist ein Fehler: Sicherheit stillschweigend übergehen — und für ein Wegwerfskript
Sicherheitsanforderungen erfinden. Die erzwungene Begründung trifft genau diese Mitte.

### Umsetzung

1. Eigener Vault-Bereich `knowledge/05-requirements/`, eine Datei je Anforderung
   (`REQ-0001 …md`) — analog zu Tasks, aus demselben Grund wie in
   [[ADR-0003 Kanban-Board mit Wikilink-Karten]]: IDs für Rückverfolgbarkeit, eigener
   Status, und keine Datei, die alle Agenten gleichzeitig beschreiben.
2. Jede Anforderung trägt Ebene, Kategorie, Quelle, Begründung, Priorität und eine
   **prüfbare** Abnahme. Nicht prüfbar formuliert heißt: noch keine Anforderung.
3. Task-Frontmatter bekommt `implements:` mit mindestens einem Anforderungs-Wikilink.
   Ausnahme nur für Infrastruktur-/Wartungsaufgaben, dann mit ausdrücklicher Begründung.
4. Rückverfolgbarkeit in beide Richtungen, maschinell geprüft durch
   `tools/check_traceability.py` in der CI. Dasselbe Skript prüft das Startgate.
5. Durchsetzung auf Task-Ebene per Hook. Code-Schreibzugriffe werden **nicht** blockiert —
   das wäre laut und träfe das template-eigene Tooling.

Die Kette lautet damit:

```
Stakeholder → Rahmen (baseline.md) → REQ-XXXX → T-XXXX → Test → Code (@contract)
```

## Konsequenzen

- `/bootstrap` erhebt bei einem neuen Projekt zuerst den **Rahmen**, nicht Tasks — und
  öffnet das Gate erst, wenn der Nutzer ihn bestätigt hat
- Bestehende Regeln gelten unverändert weiter: TDD, `@contract`, Größen- und Namensgrenzen,
  Sicherheitsvorgaben, KB-Pflicht. Anforderungen kommen davor, ersetzen nichts davon
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
- Das Startgate sich als Bremse erweist, weil Nutzer den Rahmen vor dem ersten Prototyp
  nicht benennen können — dann braucht es einen ausdrücklichen Spike-Modus mit Verfallsdatum
