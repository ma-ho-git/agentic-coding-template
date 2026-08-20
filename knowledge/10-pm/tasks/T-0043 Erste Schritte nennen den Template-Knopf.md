---
id: T-0043
title: Erste Schritte nennen den Template-Knopf
type: task
implements: ["[[REQ-0020 Für unerfahrene Anwender nutzbar]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/docs]
related: ["[[T-0042 README auf den gebauten Stand bringen]]"]
---

# T-0043 Erste Schritte nennen den Template-Knopf

## Anforderung

[[REQ-0020 Für unerfahrene Anwender nutzbar]] — der erste Weg ins Projekt darf keinen
Handgriff verlangen, dessen Zweck man erst verstehen muss.

## Ziel

Das Repository ist seit dem 2026-08-20 bei GitHub als Template-Repository markiert. Damit
gibt es einen Weg, den die README nicht kennt: **„Use this template"** erzeugt ein eigenes
Repository mit einem einzigen frischen Commit und ohne die Historie der Vorlage.

Die README nennt nur den Klon-Weg und lässt den Nutzer das von Hand nachbauen:

```bash
rm -rf .git && git init
```

Zwei Probleme damit. Erstens ist es umständlicher als ein Knopfdruck. Zweitens — und das
wiegt schwerer — ist `rm -rf .git` für jemanden ohne Git-Erfahrung ein Kommando, dessen
Wirkung er nicht beurteilen kann, und es steht als **erster Schritt** in der Anleitung.
Wer es falsch abtippt oder im falschen Verzeichnis ausführt, verliert ein anderes Repository.

Der Klon-Weg bleibt trotzdem stehen: nicht jeder hat ein GitHub-Konto oder will eines
benutzen.

## Akzeptanzkriterien

- [x] „Erste Schritte" nennt „Use this template" als ersten Weg, mit einem Satz dazu, was der
      Knopf tut (eigenes Repository, ein Commit, keine fremde Historie)
- [x] Der Klon-Weg bleibt als Alternative erhalten, erkennbar als solche
- [x] Bei `rm -rf .git` steht, was es bewirkt und warum es nötig ist — kein unerklärtes
      destruktives Kommando in einer Anleitung für Anfänger
- [x] `/bootstrap` bleibt in beiden Wegen der nächste Schritt
- [x] Keine Behauptung ohne Deckung: `is_template` ist geprüft, nicht angenommen
- [x] `check_vault.py` und `check_placeholders.py` verhalten sich unverändert

## Kontext

- Gefunden beim Nachprüfen des Merges nach `main`: Der Repository-Zustand hat sich geändert
  (`is_template: false` → `true`), die Anleitung nicht.
- Kein Ersatz für T-0042, sondern die Folge davon: Dieselbe Stelle, ein neuer Weg.

## Agent

`claude-code`.

## Abhängigkeiten

- keine

## Ergebnis

- „Erste Schritte" führt jetzt zwei Wege: **Use this template** zuerst (mit direktem Link
  auf `/generate`), der Klon-Weg darunter als „Ohne GitHub-Konto".
- `rm -rf .git` steht weiterhin dort, wo es gebraucht wird, aber mit Kommentar in der Zeile
  **und** einem Absatz darunter: was gelöscht wird, was bleibt, und wann man besser den
  Knopf nimmt. Ein destruktives Kommando ohne Erklärung ist in einer Anfängeranleitung
  genau die falsche erste Zeile.
- `is_template: true` über die GitHub-API geprüft, nicht angenommen.
- `check_vault.py` 0/0, `check_placeholders.py` unverändert 14 Dokumente (4 Kern),
  Suite 158 grün.
