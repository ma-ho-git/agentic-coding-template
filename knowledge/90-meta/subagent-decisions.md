---
title: Register der Subagenten-Entscheidungen
aliases: ["Register der Subagenten-Entscheidungen"]
type: knowledge
tags: [topic/agents, topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-20
review_after: 2027-02-19
related: ["[[Konventionen der Wissensdatenbank]]", "[[00-index]]"]
---

# Register der Subagenten-Entscheidungen

## Kurz

Jede Kosten-/Nutzenprüfung vor einem Subagenten-Einsatz landet hier — mit Ergebnis.
Vor einer neuen Prüfung **zuerst hier nachsehen**: eine dokumentierte positive Entscheidung
für dieselbe Aufgabenart reicht als Grundlage, es muss nicht neu hergeleitet werden.

Prüfkriterien: `.claude/rules/agent-conduct.md`.

## Register

| Datum | Aufgabenart | Agent | Entscheidung | Begründung | Ergebnis |
| --- | --- | --- | --- | --- | --- |
| 2026-08-19 | Recherche zu externer Doku (mehrere Quellen, große Seiten) | `researcher` | ja | Rohtext der Doku-Seiten würde den Hauptkontext füllen; Antwort ist kompakt und prüfbar | offen |
| 2026-08-19 | Regeldateien und Hooks im Template schreiben | — | nein | Erfordert den vollen Gesprächskontext und iterative Abstimmung mit dem Nutzer | inline erledigt, richtig so |
| 2026-08-19 | Review einer Änderung gegen die Projektregeln | `code-reviewer` | ja | Eigener Kontext erzwingt frischen Blick; Ergebnis ist ohne Nacharbeit prüfbar | offen |
| 2026-08-20 | Suche nach bestehenden Lösungen (`/solution-scan`) | `researcher` | ja | Viele abgerufene Projektseiten füllen sonst den Hauptkontext; das Ergebnis ist je Kandidat gegen die REQ-IDs prüfbar. **Die Bewertung bleibt beim Hauptagenten** — delegiert wird das Abrufen, nicht das Urteil | offen |

## Daumenregeln (aus den bisherigen Fällen)

- **Ja** bei: breiten Suchen, Doku-Recherche, Review, unabhängigen Prüfungen
- **Nein** bei: Änderungen an denselben Dateien, allem was den Gesprächsverlauf braucht,
  Aufgaben unter etwa fünf Minuten Eigenaufwand
- **Nie** als Ausweichmanöver vor einem schwierigen Problem
