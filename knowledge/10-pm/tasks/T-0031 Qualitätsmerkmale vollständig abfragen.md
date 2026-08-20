---
id: T-0031
title: Qualitätsmerkmale vollständig abfragen
type: task
implements: ["[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
status: ready
priority: hoch
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[T-0030 Funktional und nicht-funktional benennen]]", "[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]"]
---

# T-0031 Qualitätsmerkmale vollständig abfragen

## Anforderung

[[REQ-0017 Anforderungserhebung vor der Entwicklung]] — Präzisierung vom 2026-08-20.

## Ziel

`qualitaet` ist heute ein Eimer für sieben Merkmale. Wer „wie gut, wie schnell, wie
bedienbar" gefragt wird, antwortet Performance und hört auf.

## Akzeptanzkriterien

- [ ] `/req-elicit` geht die Qualitätsmerkmale einzeln durch, nicht als eine Frage —
      Leistung, Kompatibilität, Bedienbarkeit, Zuverlässigkeit, Sicherheit, Wartbarkeit,
      Flexibilität/Portabilität, Safety
- [ ] Je Merkmal ein Satz Erklärung und ein Beispiel; „trifft hier nicht zu" bleibt eine
      vollständige Antwort, aber sie wird **gefragt**
- [ ] Die Szenarioform steht als Anleitung zur Messbarkeit drin:
      **Auslöser → erwartete Reaktion → Messgröße**, mit zwei durchgerechneten Beispielen
- [ ] `/req-validate` meldet Qualitätsmerkmale ohne Anforderung und ohne Abwahlbegründung
- [ ] Die Herkunft der Liste ist als Wissensnotiz belegt, samt Hinweis, dass die
      Primärquellen in dieser Umgebung nicht abrufbar waren und nachzuprüfen sind

## Kontext

- ISO/IEC 25010:2023 nennt neun Merkmale; `funktionale Eignung` fällt bei uns mit der
  Kategorie `funktional` zusammen
- Abgrenzung: [[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]] deckt
  Zuverlässigkeit im Code ab — hier geht es um die **Erhebung** des Anspruchs

## Agent

`claude-code` — Skills, Wissensnotiz.

## Abhängigkeiten

- [[T-0030 Funktional und nicht-funktional benennen]]

## Notizen

- Gefahr: Neun Merkmale einzeln abzufragen kann zum Verhör werden. Die Bündelung muss so
  gewählt sein, dass ein kleines Projekt in zwei Minuten durch ist — sonst wird der Schritt
  übersprungen und die Erhebung ist schlechter als vorher.
