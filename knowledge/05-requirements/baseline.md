---
title: Rahmen und Startgate
aliases: ["Rahmen und Startgate", "baseline"]
type: knowledge
tags: [topic/requirements]
status: active
baseline_status: vereinbart
created: 2026-08-19
updated: 2026-08-20
review_after: 2026-11-20
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]]", "[[Projektvision]]", "[[00-index]]"]
---

# Rahmen und Startgate

> **Diese Datei entscheidet, ob entwickelt werden darf.**
> Solange `baseline_status: entwurf` steht, wird kein Produktivcode geschrieben.
> Nur der Mensch setzt sie auf `vereinbart` — ein Agent schlägt vor, er bescheinigt sich nichts selbst.
>
<!-- template-placeholder -->
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

## Projektzuschnitt

`project_scope: produkt` (`.claude/hooks/config.json`).

**Begründung:** Das Template wird öffentlich bereitgestellt, von fremden Projekten geklont
und über längere Zeit gepflegt. Es ist außerdem sein eigener Prüfstein — was hier an
Dokumentationspflicht wegfällt, fällt in jedem geklonten Projekt als Vorbild ebenfalls weg.
Ein kleinerer Zuschnitt wäre hier also nicht nur ungenau, sondern lehrreich falsch.

Der Zuschnitt skaliert ausschließlich Dokumentationspflicht und Erhebungstiefe. Anforderungen,
TDD und alle starren Leitplanken gelten in jedem Zuschnitt unverändert —
siehe `.claude/rules/workflow.md` und `.claude/rules/guardrails.md`.

Bei einer späteren Änderung: neue Begründung hier ergänzen, die alte stehen lassen.

## Kategorien

### Funktional

- [[REQ-0001 Einsatzbereites Gerüst für strukturiertes Vibe-Coding]]
- [[REQ-0002 Projektmanagement in der Wissensdatenbank]]
- [[REQ-0003 Projektwissen wird eigenständig dokumentiert]]
- [[REQ-0021 Szenario als optionaler Einstieg]]

### Technisch

- [[REQ-0011 Prüfbare Vorgaben werden durchgesetzt, nicht empfohlen]]
- [[REQ-0016 Dokumentationsschema je Programmiersprache]]

### Organisatorisch

- [[REQ-0012 Aufgaben werden dem passenden Agenten zugeordnet]]
- [[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]]
- [[REQ-0014 Subagenten nur nach Kosten-Nutzen-Prüfung]]
- [[REQ-0017 Anforderungserhebung vor der Entwicklung]]
- [[REQ-0019 Leitplanken in zwei Klassen]]
- [[REQ-0022 Das Szenario trägt die weitere Entwicklung]]
- [[REQ-0024 Vorhandene Lösungen werden vor dem Codieren geprüft]]

### Sicherheit

- [[REQ-0009 Kein Code mit bekannten Sicherheitslücken]]
- [[REQ-0010 Agenten gefährden weder das Projekt noch sein Umfeld]]

### Recht

- [[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]
- [[REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt]]

### Qualität

- [[REQ-0004 Dokumentation ist für Mensch und Agent nutzbar]]
- [[REQ-0005 Veraltetes Wissen wird gekennzeichnet statt gelöscht]]
- [[REQ-0006 Testgetriebene Entwicklung ist verpflichtend]]
- [[REQ-0007 Grenzen für Funktionsgröße und Benennung]]
- [[REQ-0008 Contract-Kommentar macht den Wirkungsradius lesbar]]
- [[REQ-0018 Das Template hält seine eigenen Vorgaben ein]]
- [[REQ-0020 Für unerfahrene Anwender nutzbar]]

#### Qualitätsmerkmale im Einzelnen

Die Kategorie `qualitaet` deckt acht Merkmale ab. Jedes braucht eine Anforderung **oder** eine
Abwahl mit Grund — sonst fällt es durch, ohne dass es jemand merkt. Geprüft von `/req-validate`.

| Merkmal | Stand |
| --- | --- |
| **Tempo** | Keine Anforderung. Abgewählt: Die Prüfungen arbeiten auf einzelnen Dateien, der Vault hat Projektgröße, niemand wartet auf sie. Bei sehr großen Vaults wäre das nachzuholen — `session_brief.py` liest bei jedem Start den ganzen Vault. |
| **Zusammenspiel** | Teilweise über [[REQ-0002 Projektmanagement in der Wissensdatenbank]]. Die Kompatibilität zu Obsidian und zum Kanban-Plugin steht bewusst in [[Randbedingungen]] und nicht als Anforderung: Das Board bleibt auch ohne Plugin lesbar, es hängt kein Code daran. |
| **Bedienbarkeit** | [[REQ-0020 Für unerfahrene Anwender nutzbar]], [[REQ-0004 Dokumentation ist für Mensch und Agent nutzbar]], [[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]] |
| **Zuverlässigkeit** | [[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]] |
| **Sicherheit** | Eigene Kategorie: [[REQ-0009 Kein Code mit bekannten Sicherheitslücken]], [[REQ-0010 Agenten gefährden weder das Projekt noch sein Umfeld]] |
| **Wartbarkeit** | [[REQ-0005 Veraltetes Wissen wird gekennzeichnet statt gelöscht]], [[REQ-0007 Grenzen für Funktionsgröße und Benennung]], [[REQ-0008 Contract-Kommentar macht den Wirkungsradius lesbar]], [[REQ-0018 Das Template hält seine eigenen Vorgaben ein]] |
| **Anpassbarkeit** | [[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]] |
| **Gefahr für Mensch oder Sachwert** | Trifft nicht zu. Das Template erzeugt Text und Prüfskripte; ein Fehler kostet Arbeitszeit, nicht Gesundheit oder Sachwerte. Der einzige Schadensfall wäre ein zerstörerisch handelnder Agent, und den deckt [[REQ-0010 Agenten gefährden weder das Projekt noch sein Umfeld]] ab. |

**Anpassbarkeit — Lücke am 2026-08-20 gefunden und geschlossen.** Das Template *war* längst
anpassbar: Stack-Profile, Schwellwerte in `config.json`, Projektzuschnitt, austauschbare
Regeldateien. Verlangt hatte es nur keine Anforderung. Sichtbar wurde das erst beim
Einzeldurchgang der Qualitätsmerkmale; unter der einen Frage „wie gut, wie schnell, wie
bedienbar" fiel es nicht auf. Ergänzt und am selben Tag bestätigt als
[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]].

Der **Nachweis** steht noch aus: Die Anpassungsstellen existieren, vorgeführt wurde keine.
Das holt [[T-0033 Anpassbarkeit nachweisen]] nach. Die Anforderung bleibt bis dahin
`vereinbart`, nicht `umgesetzt` — für das Startgate genügt das, denn das Gate fragt nach dem
vereinbarten Rahmen, nicht nach erbrachten Nachweisen.
- [[REQ-0023 Fehler- und Ausfallverhalten wird bewusst entschieden]]

## Freigabe

| Feld | Wert |
| --- | --- |
| Rahmen vollständig geprüft am | 2026-08-20 |
| Anforderungen einzeln bestätigt | 2026-08-20 durch Marcus (Auftraggeber), alle 26 einzeln vorgelegt und bestätigt |
| Nachtrag nach der Bestätigung | REQ-0026 (Anpassbarkeit) kam am 2026-08-20 dazu, nachdem der Einzeldurchgang der Qualitätsmerkmale die Lücke sichtbar gemacht hatte. Ebenfalls einzeln vorgelegt und bestätigt. |
| Änderung bei der Bestätigung | REQ-0020: Abnahme sagte „ein kleiner Zuschnitt schaltet Zeremonie ab" — widersprach [[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]]. Vor der Bestätigung korrigiert: der Zuschnitt verringert Dokumentationspflicht und Erhebungstiefe und schaltet nie eine starre Leitplanke ab. |
| Startgate freigegeben durch | Marcus (Auftraggeber), 2026-08-20 — nach Bestätigung aller 26 Anforderungen und dem bestandenen Erstlauf im frischen Klon ([[T-0034 Erstlauf im frischen Klon durchspielen]]) |

**Kategorienabdeckung:** alle sechs belegt — funktional (4), technisch (2), organisatorisch (7),
sicherheit (2), recht (2), qualitaet (9). Keine Kategorie ist als „nicht zutreffend" begründet;
für dieses Projekt greift jede.

**Qualitätsmerkmale:** alle acht haben Anforderung oder begründete Abwahl (Abschnitt oben).
Die letzte Lücke — Anpassbarkeit — wurde am 2026-08-20 gefunden und mit REQ-0026 geschlossen.

**Hinweis zum Sonderfall dieses Repositories:** Das Template wurde gebaut, bevor es seine
eigene Anforderungsebene besaß. Die Anforderungen sind daher nachträglich aus der
ursprünglichen Vorgabe abgeleitet und die bereits erledigten Aufgaben rückwirkend verlinkt.
Für ein neu geklontes Projekt gilt der normale Weg: erst `/req-elicit`, dann das Gate, dann
Code.

**Das Gate ist offen.** Ab jetzt gilt: Rahmenanforderungen ändern sich nur über
`/req-change`, nicht durch stilles Überschreiben.

Für ein geklontes Projekt gilt das **nicht**: `tools/handover.py --apply` setzt
`baseline_status` auf `entwurf` zurück, bevor die Erhebung beginnt — nachgewiesen in
[[T-0038 Übergabe von der Vorlage zum Projekt]]. Ein Klon startet also mit geschlossenem Gate.
