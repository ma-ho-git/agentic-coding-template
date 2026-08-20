---
title: Rahmen und Startgate
aliases: ["Rahmen und Startgate", "baseline"]
type: knowledge
tags: [topic/requirements]
status: active
baseline_status: entwurf
created: 2026-08-19
updated: 2026-08-20
review_after: 2026-11-20
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[Projektvision]]", "[[00-index]]"]
---

# Rahmen und Startgate

> **Diese Datei entscheidet, ob entwickelt werden darf.**
> Solange `baseline_status: entwurf` steht, wird kein Produktivcode geschrieben.
> Nur der Mensch setzt sie auf `vereinbart` — ein Agent schlägt vor, er bescheinigt sich nichts selbst.
>
> **Für ein eigenes Projekt:** Inhalt ersetzen, `baseline_status` auf `entwurf` zurücksetzen.
> Was hier steht, ist der Rahmen **dieses Templates** und zugleich ein ausgefülltes Beispiel.

## Kurz

Der Rahmen beantwortet: *Was wird gebaut, und was muss dabei gelten?* Er muss vollständig
sein, bevor die Entwicklung beginnt — nicht weil Vorab-Spezifikation Selbstzweck wäre,
sondern weil eine spät entdeckte Rahmenanforderung fertige Arbeit entwertet.

Vollständig heißt: **jede** der sechs Kategorien unten ist entweder mit mindestens einer
Rahmenanforderung belegt **oder** ausdrücklich als nicht zutreffend begründet.

Regeln: `.claude/rules/requirements.md`. Entscheidung:
[[ADR-0005 Anforderungen als Pflicht vor dem Code]].

## Zielartefakt

Eine klonbare Projektvorlage, die Claude Code und Claude Cowork ein Gerüst für strukturiertes
Vibe-Coding gibt: verbindliche Regeln, eine Obsidian-kompatible Wissensdatenbank mit
Aufgabenverwaltung, verpflichtende Anforderungserhebung vor dem Codieren, und Prüfungen, die
das durchsetzen statt es zu empfehlen. Ausführlich in [[Projektvision]].

## Kategorien

### Funktional

- [[REQ-0001 Einsatzbereites Gerüst für strukturiertes Vibe-Coding]]
- [[REQ-0002 Projektmanagement in der Wissensdatenbank]]
- [[REQ-0003 Projektwissen wird eigenständig dokumentiert]]

### Technisch

- [[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]
- [[REQ-0016 Dokumentationsschema je Programmiersprache]]

### Organisatorisch

- [[REQ-0012 Aufgaben werden dem passenden Agenten zugeordnet]]
- [[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]]
- [[REQ-0014 Subagenten nur nach Kosten-Nutzen-Prüfung]]
- [[REQ-0017 Anforderungserhebung vor der Entwicklung]]

### Sicherheit

- [[REQ-0009 Kein Code mit bekannten Sicherheitslücken]]
- [[REQ-0010 Agenten gefährden weder das Projekt noch sein Umfeld]]

### Recht

- [[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]

### Qualität

- [[REQ-0004 Dokumentation ist für Mensch und Agent nutzbar]]
- [[REQ-0005 Veraltetes Wissen wird gekennzeichnet statt gelöscht]]
- [[REQ-0006 Testgetriebene Entwicklung ist verpflichtend]]
- [[REQ-0007 Grenzen für Funktionsgröße und Benennung]]
- [[REQ-0008 Contract-Kommentar macht den Wirkungsradius lesbar]]
- [[REQ-0018 Das Template hält seine eigenen Vorgaben ein]]

## Freigabe

| Feld | Wert |
| --- | --- |
| Rahmen vollständig geprüft am | 2026-08-20 (durch den Agenten vorgelegt) |
| Freigegeben durch | — offen, siehe Hinweis |
| Bemerkungen | Alle 18 Anforderungen stehen auf `status: entwurf`. Sie sind aus der Projektvorgabe vom 2026-08-19 abgeleitet, nicht erfunden — aber der Auftraggeber hat den Wortlaut noch nicht bestätigt. |

**Hinweis zum Sonderfall dieses Repositories:** Das Template wurde gebaut, bevor es seine
eigene Anforderungsebene besaß. Die Anforderungen sind daher nachträglich aus der
ursprünglichen Vorgabe abgeleitet und die bereits erledigten Aufgaben rückwirkend verlinkt.
Für ein neu geklontes Projekt gilt der normale Weg: erst `/req-elicit`, dann das Gate, dann
Code.

Nach der Freigabe `baseline_status` auf `vereinbart` setzen und die Anforderungen auf
`status: vereinbart`. Ab dann gilt: Rahmenanforderungen ändern sich nur über `/req-change`,
nicht durch stilles Überschreiben.
