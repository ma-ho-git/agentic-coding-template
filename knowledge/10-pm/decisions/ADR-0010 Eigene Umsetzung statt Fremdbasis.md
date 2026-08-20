---
title: ADR-0010 Eigene Umsetzung statt Fremdbasis
type: decision
tags: [topic/meta, topic/requirements]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[Spec-Driven-Development - was andere Projekte machen]]", "[[ADR-0002 Prüfbare Vorgaben in Hooks statt in Prosa]]", "[[Fremdlösungen]]", "[[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]"]
---

# ADR-0010 Eigene Umsetzung statt Fremdbasis

## Status

angenommen

> **Nachträglich festgehalten.** Die Entscheidung fiel faktisch beim Aufbau des Templates;
> die Pflicht, sie als ADR zu führen, entstand erst mit
> [[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]. Sie wird hier
> nachgezogen, weil genau dieser Fall — „wir bauen selbst" — derjenige ist, der am ehesten
> unbegründet bleibt.

## Kontext

- Marktumschau: [[Spec-Driven-Development - was andere Projekte machen]]. Vier ernsthafte
  Kandidaten: GitHub Spec Kit (~93k Sterne, MIT), BMAD-Method (~48k Sterne), AWS Kiro
  (kommerziell), OpenSpec.
- Die Kandidaten decken den **Ablauf** gut ab: Spezifikation, Planung, Aufgabenzerlegung,
  benannte Agentenrollen.
- Sie decken die Kernanforderung dieses Projekts **nicht** ab:
  [[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]. Spec Kits
  „Constitution" ist Prosa, BMADs Rollengrenzen ebenso. Die Guardrails-Literatur nennt
  Prosa-Anweisungen ausdrücklich die schwächste Schicht — umgehbar durch Umformulierung.

## Optionen

| Option | Vorteil | Nachteil |
| --- | --- | --- |
| Spec Kit übernehmen und erweitern | großer Funktionsumfang, aktive Wartung, MIT | die fehlende Durchsetzung ist kein Randstück, sondern das Herz des Vorhabens; wir müssten den Kern ersetzen und den Rest mitschleppen |
| BMAD übernehmen | ausgereiftes Rollenmodell | dasselbe Durchsetzungsproblem, dazu ein Rollenmodell, das für einen Menschen mit ein bis zwei Agenten überdimensioniert ist |
| Kiro | ausgereift | kommerziell und IDE-gebunden — kein klonbares Repository-Template, damit unvereinbar mit dem Zielartefakt |
| **Eigene Umsetzung, Konzepte übernehmen** | Durchsetzung von Anfang an im Zentrum; klein genug für einen Menschen | wir schreiben Ablaufsteuerung, die es anderswo schon gibt |

## Entscheidung

Eigene Umsetzung. **Konzepte** werden übernommen, **Code** nicht.

Der Grund ist die 80/20-Frage aus `/solution-scan`: Die Kandidaten erfüllen viel, aber die
fehlenden zwanzig Prozent sind genau der Grund, aus dem dieses Projekt existiert. Ein
Kandidat, dem der Kern fehlt, ist auch bei neunzig Prozent Abdeckung wertlos — man müsste
sein Herz austauschen und trüge die restliche Fremdmasse als Ballast.

Übernommen wurden Ideen, ausdrücklich benannt in der Umschau: ein eigener Klärungsschritt vor
der Planung, projektbezogene statt fester Prüflisten, artefaktübergreifende
Konsistenzprüfung — Letztere existiert hier bereits als Code
(`tools/check_traceability.py`) und ist damit stärker als das Vorbild.

## Konsequenzen

- Kein Fremdcode, also keine geerbten Lizenzpflichten. Das Register der Fremdkomponenten
  bleibt vorerst leer.
- Der Ablauf muss selbst gepflegt werden — Spec Kit bekommt Verbesserungen geschenkt, wir
  nicht.
- Die Umschau bleibt gültig und wird bei `review_after` erneut geprüft. Wenn ein Projekt
  Durchsetzung nachrüstet, ändert das die Grundlage dieser Entscheidung.

## Revidieren wenn

- Eines der Projekte maschinelle Durchsetzung bekommt, die über Prosa hinausgeht. Dann ist
  der Grund für den Eigenbau weg, und die Entscheidung gehört neu getroffen.
- Der Pflegeaufwand für die Ablaufsteuerung den Nutzen der eigenen Durchsetzung übersteigt.
