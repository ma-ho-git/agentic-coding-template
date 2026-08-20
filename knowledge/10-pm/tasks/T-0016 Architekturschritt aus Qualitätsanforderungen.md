---
id: T-0016
title: Architekturschritt aus Qualitätsanforderungen
type: task
implements: []
infrastruktur: Aufbau der Anforderungsebene selbst - kann sich nicht auf eine Anforderung stützen, die es noch nicht gibt
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/meta]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Sommerville Software Engineering - was das Template übernimmt]]"]
---

# T-0016 Architekturschritt aus Qualitätsanforderungen

## Ziel

Architekturentscheidungen entstehen aus den Qualitätsanforderungen, nicht nebenbei.

## Akzeptanzkriterien

- [x] `/architecture` existiert: liest die Qualitätsanforderungen, benennt die
      Zielkonflikte zwischen ihnen, schlägt ein Architekturmuster vor und schreibt das
      Ergebnis als ADR
- [x] Der Skill kennt Sommervilles Grundkonflikte (Performanz gegen Wartbarkeit,
      Sicherheit gegen Performanz, Verfügbarkeit gegen Einfachheit) und zwingt zu einer
      benannten Abwägung statt zu einer Wunschliste
- [x] Das erzeugte ADR verlinkt die Qualitätsanforderungen, aus denen es folgt —
      beidseitig
- [x] `.claude/rules/code-quality.md` verweist für die **System**-Struktur auf diesen
      Schritt; die Unit-Muster bleiben dort (siehe Notiz)

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[Sommerville Software Engineering - was das Template übernimmt]] — Kapitel 6

## Agent

`claude-code` — Skill-Datei und Regelanpassung.

## Abhängigkeiten

- [[T-0012 Anforderungsregeln und Vault-Struktur]]

## Notizen

- Bewusst leichtgewichtig: kein eigenes Architekturdokument, ein ADR je Entscheidung.
  Die ADR-Struktur existiert bereits und hat sich bewährt.
- Systemmodellierung (Sommerville Kap. 5) bleibt außen vor, siehe Abgrenzung in der
  Wissensnotiz.
- **2026-08-20 umgesetzt.** `/architecture` liest Anforderungen der Kategorien `qualitaet`,
  `technisch` und `sicherheit` — `funktional` prägt die Struktur selten.
- **Vom eigenen Akzeptanzkriterium abgewichen, bewusst:** Das Kriterium verlangte, die
  Patternliste aus `code-quality.md` zu entfernen und dorthin zu verweisen. Beim Umsetzen
  zeigte sich, dass zwei verschiedene Entscheidungen vermischt waren: Systemstruktur
  (Sommerville Kap. 6 — Schichten, Repository, Client-Server) folgt aus
  Qualitätsanforderungen und gehört in `/architecture`; Unit-Muster (Factory, Strategy,
  Adapter) sind eine Entscheidung beim Schreiben einer einzelnen Einheit und gehören in
  die pfad-gebundene Regel, die genau dann lädt. Beide Listen bleiben, aber getrennt und
  mit benannter Zuständigkeit — keine Dopplung. `Repository` steht in beiden, weil es
  wirklich beide Ebenen berührt; das ist im Text vermerkt.
- Kernidee des Skills: Schritt 2 zwingt dazu, den Zielkonflikt **aufzuschreiben**, auch
  wenn die Antwort offensichtlich scheint. Ein ADR ohne benannte Abwägung ist Papier.
- Abgrenzung eingebaut: widersprechen sich zwei vereinbarte Anforderungen wirklich, ist das
  kein Architekturproblem, sondern ein Anforderungsfehler → zurück zu `/req-change`.
