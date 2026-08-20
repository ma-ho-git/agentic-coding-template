---
id: T-0031
title: Qualitätsmerkmale vollständig abfragen
type: task
implements: ["[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
status: done
priority: hoch
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/meta]
related: ["[[T-0030 Funktional und nicht-funktional benennen]]", "[[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]", "[[Funktionale und nicht-funktionale Anforderungen]]"]
---

# T-0031 Qualitätsmerkmale vollständig abfragen

## Anforderung

[[REQ-0017 Anforderungserhebung vor der Entwicklung]] — Präzisierung vom 2026-08-20.

## Ziel

`qualitaet` ist heute ein Eimer für sieben Merkmale. Wer „wie gut, wie schnell, wie
bedienbar" gefragt wird, antwortet Performance und hört auf.

## Akzeptanzkriterien

- [x] `/req-elicit` geht die Qualitätsmerkmale einzeln durch, nicht als eine Frage —
      Leistung, Kompatibilität, Bedienbarkeit, Zuverlässigkeit, Sicherheit, Wartbarkeit,
      Flexibilität/Portabilität, Safety
- [x] Je Merkmal ein Satz Erklärung und ein Beispiel; „trifft hier nicht zu" bleibt eine
      vollständige Antwort, aber sie wird **gefragt**
- [x] Die Szenarioform steht als Anleitung zur Messbarkeit drin:
      **Auslöser → erwartete Reaktion → Messgröße**, mit zwei durchgerechneten Beispielen
- [x] `/req-validate` meldet Qualitätsmerkmale ohne Anforderung und ohne Abwahlbegründung
- [x] Die Herkunft der Liste ist als Wissensnotiz belegt, samt Hinweis, dass die
      Primärquellen in dieser Umgebung nicht abrufbar waren und nachzuprüfen sind

## Ergebnis

- `/req-elicit` fragt die acht Qualitätsmerkmale als **Sweep in drei Durchgängen** ab, nicht
  als eine Frage. Die Reihenfolge im Skill ist jetzt: Merkmale (3a) → Ausfallverhalten je
  Abhängigkeit (3b) → Messbarkeit (3c).
- **Der Entwurf löst die Verhör-Gefahr aus der Aufgabennotiz so:** Durchgang 1 zeigt alle acht
  auf **einem Bildschirm** und fragt einmal, was zutrifft — der Agent markiert vorab die zwei
  bis drei, die er für dieses Artefakt erwartet, und sagt warum. Erst Durchgang 2 stellt je
  genanntem Merkmal eine Frage, Durchgang 3 wählt den Rest mit je einer Zeile ab. Ein kleines
  Projekt ist in zwei Minuten durch, ohne dass eine Frage entfällt.
- Die Merkmale stehen in **Nutzerworten**, nicht in Normbegriffen: Tempo, Zusammenspiel,
  Bedienbarkeit, Zuverlässigkeit, Sicherheit, Wartbarkeit, Anpassbarkeit, Gefahr für Mensch
  oder Sachwert. Der Nutzer soll antworten können, nicht klassifizieren.
- **Zwei Merkmale werden namentlich nachgefragt, auch wenn der Nutzer fertig ist:**
  Wartbarkeit — weil die Person, die es in einem Jahr ändert, nicht im Raum sitzt — und
  Anpassbarkeit, weil niemand plant umzuziehen.
- Szenarioform als Anleitung zur Messbarkeit: **Auslöser → erwartete Reaktion → Messgröße**,
  mit zwei durchgerechneten Beispielen. Dazu der Gesprächsdreh, der wirklich hilft: „Wann
  genau wäre es dir zu langsam?" erzeugt einen Schwellwert, „wie schnell soll es sein?"
  erzeugt „schnell". Kann der Nutzer keine Messgröße nennen, ist das eine offene Frage —
  nie eine Zahl vom Agenten.
- `/req-validate` meldet jedes Merkmal ohne Anforderung **und** ohne Abwahl, in Nutzerworten.
- Methodenglossar erklärt das Qualitätsszenario.

### Der Sweep hat beim ersten Lauf eine echte Lücke gefunden

Am eigenen Rahmen durchgespielt und als Abschnitt in `baseline.md` festgehalten. Ergebnis:
**Anpassbarkeit hat weder Anforderung noch Abwahl.** Das Template *ist* anpassbar —
Stack-Profile, Schwellwerte, Projektzuschnitt, austauschbare Regeln — aber keine der 25
Anforderungen verlangt das. Unter der einen Frage „wie gut, wie schnell, wie bedienbar" war
das nicht sichtbar; beim Einzeldurchgang fiel es sofort auf. Genau dafür ist der Sweep da.

Zusätzlich ehrlich vermerkt: **Zusammenspiel** ist nur teilweise belegt — die Obsidian- und
Plugin-Kompatibilität steht bewusst in den Randbedingungen, nicht als Anforderung. **Tempo**
ist begründet abgewählt, mit dem Hinweis, dass `session_brief.py` bei jedem Start den ganzen
Vault liest und das bei sehr großen Vaults nachzuholen wäre.

Der Freigabe-Abschnitt in `baseline.md` weist die Lücke aus: Der Rahmen ist an dieser Stelle
unvollständig und das ist vor dem Gate zu entscheiden.

Suite 106 grün (unverändert — Skills, Glossar, Rahmen), `check_vault.py` und
`check_traceability.py` ohne Befund.

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
