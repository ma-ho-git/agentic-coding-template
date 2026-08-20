---
id: T-0034
title: Erstlauf im frischen Klon durchspielen
type: task
implements: ["[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]]"]
status: doing
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished:
tags: [topic/meta, topic/requirements]
related: ["[[T-0033 Anpassbarkeit nachweisen]]", "[[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]]"]
---

# T-0034 Erstlauf im frischen Klon durchspielen

## Anforderung

[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]] — der vierte Abnahmepunkt: „Nach
`/bootstrap` enthält kein Pflichtdokument des Projekts noch einen Template-Platzhalter."

## Ziel

Der einzige Abnahmepunkt, der sich **im Template selbst nicht zeigen lässt**. Hier gehören
die Platzhalter hin; ihr Verschwinden ist erst in einem Klon beobachtbar.

## Akzeptanzkriterien

- [ ] Frischer Klon, `/bootstrap` vollständig durchlaufen — mit einem echten kleinen Vorhaben,
      nicht mit Platzhaltertext
- [ ] `python3 tools/check_placeholders.py` meldet danach **0 Kerndokumente**
- [ ] Notiert, welche Schritte des Bootstrap unklar waren oder Rückfragen brauchten — der
      Erstlauf ist zugleich der Praxistest für
      [[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]] und
      [[REQ-0020 Für unerfahrene Anwender nutzbar]]
- [ ] Ergebnis im Fortschrittslog; REQ-0026 auf `umgesetzt`, wenn alle fünf Abnahmepunkte
      tragen

## Kontext

- [[T-0033 Anpassbarkeit nachweisen]] hat drei der fünf Abnahmepunkte belegt, einen als
  konstruktionsbedingt eingeordnet und diesen hier offen gelassen
- Braucht einen Menschen: `/bootstrap` stellt Fragen, die niemand für den Nutzer beantwortet

## Agent

`claude-code` gemeinsam mit dem Nutzer. Ohne echte Antworten ist der Durchlauf wertlos.

## Abhängigkeiten

- keine

## Notizen

- Am aufschlussreichsten wird vermutlich nicht die Platzhalterprüfung, sondern die Liste der
  Stellen, an denen der Erstlauf gestockt hat. Die gehört vollständig aufgeschrieben, auch
  wenn sie unangenehm ist.
