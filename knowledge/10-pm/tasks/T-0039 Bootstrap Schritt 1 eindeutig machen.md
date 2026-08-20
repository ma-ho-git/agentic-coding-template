---
id: T-0039
title: Bootstrap Schritt 1 eindeutig machen
type: task
implements: ["[[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/agents]
related: ["[[T-0034 Erstlauf im frischen Klon durchspielen]]", "[[T-0040 Übergabe hinterlässt leere Formulare]]"]
---

# T-0039 Bootstrap Schritt 1 eindeutig machen

## Anforderung

[[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]] — Befund 3 aus
[[T-0034 Erstlauf im frischen Klon durchspielen]].

## Ziel

Der Skill sagt „For each entry whose `verified` date is older than 30 days" und listet
darunter, auf gleicher Ebene und ohne Verbindung, „Check at minimum: …". Beim Erstlauf war
nicht entscheidbar, ob die Liste an die Bedingung gebunden ist oder immer gilt.

## Akzeptanzkriterien

- [x] Die Prüfliste ist eindeutig der Bedingung zugeordnet — sie sagt, **was** zu prüfen ist,
      wenn geprüft wird, nicht **dass** immer zu prüfen ist
- [x] Der Fall „alle Einträge frisch" ist ausdrücklich behandelt: nichts abrufen, weitergehen,
      und das dem Nutzer sagen statt stillschweigend zu überspringen
- [x] Der Skill weist darauf hin, dass ein Klon das **Prüfdatum der Vorlage** erbt — ein
      heute geklontes Projekt überspringt Schritt 1 also zu Recht, ein in sechs Monaten
      geklontes nicht
- [x] Kein anderer Schritt verändert

## Ergebnis

- Schritt 1 beginnt jetzt mit der Entscheidung, **ob überhaupt etwas zu tun ist**, statt sie
  zwischen zwei Listen zu verstecken.
- Der Fall „alles frisch" ist ausdrücklich behandelt — und zwar so, dass der Agent es **sagt**
  statt still zu überspringen. Ein Schritt, der wortlos nichts tut, sieht für einen Anfänger
  aus wie ein Schritt, der vergessen wurde.
- Die vererbten Prüfdaten sind benannt: Heute geklont ist alles frisch und Schritt 1 folgenlos,
  in sechs Monaten geklont ist alles fällig. Das ist gewolltes Verhalten und steht jetzt auch
  so da — vorher hätte man es für ein Versehen halten können.
- Die Prüfliste heißt nicht mehr „Check at minimum", sondern sagt ausdrücklich, dass sie das
  **Was** beschreibt und nicht das **Ob**.

Kein anderer Schritt verändert. Reine Skill-Prosa, Suite unverändert 151 grün.

## Kontext

- Beim Erstlauf am 2026-08-20 waren alle Einträge einen Tag alt; ich habe die Mehrdeutigkeit
  nach eigenem Ermessen aufgelöst. Ein anderer Agent löst sie anders auf — genau das soll
  ein Skill verhindern.

## Agent

`claude-code` — reine Skill-Prosa.

## Abhängigkeiten

- keine

## Notizen

- Kleiner Textfehler mit großer Reichweite: Schritt 1 läuft in **jedem** frisch geklonten
  Projekt, und er ist der erste Eindruck des Verfahrens.
