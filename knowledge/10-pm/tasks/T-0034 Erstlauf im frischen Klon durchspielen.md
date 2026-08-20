---
id: T-0034
title: Erstlauf im frischen Klon durchspielen
type: task
implements: ["[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-20
started: 2026-08-20
finished: 2026-08-20
tags: [topic/meta, topic/requirements]
related: ["[[T-0033 Anpassbarkeit nachweisen]]", "[[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]]", "[[T-0038 Übergabe von der Vorlage zum Projekt]]"]
---

# T-0034 Erstlauf im frischen Klon durchspielen

## Anforderung

[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]] — der vierte Abnahmepunkt: „Nach
`/bootstrap` enthält kein Pflichtdokument des Projekts noch einen Template-Platzhalter."

## Ziel

Der einzige Abnahmepunkt, der sich **im Template selbst nicht zeigen lässt**. Hier gehören
die Platzhalter hin; ihr Verschwinden ist erst in einem Klon beobachtbar.

## Akzeptanzkriterien

- [x] Frischer Klon, `/bootstrap` vollständig durchlaufen — mit einem echten kleinen Vorhaben,
      nicht mit Platzhaltertext
- [x] `python3 tools/check_placeholders.py` meldet danach **0 Kerndokumente**
- [x] Notiert, welche Schritte des Bootstrap unklar waren oder Rückfragen brauchten — der
      Erstlauf ist zugleich der Praxistest für
      [[REQ-0013 Der erste Lauf prüft die Annahmen und orientiert den Nutzer]] und
      [[REQ-0020 Für unerfahrene Anwender nutzbar]]
- [x] Ergebnis im Fortschrittslog; REQ-0026 auf `umgesetzt`, wenn alle fünf Abnahmepunkte
      tragen

## Ergebnis

Frischer Klon, `/bootstrap` von Schritt 1 bis 3a durchgespielt — mit einem echten Vorhaben
des Auftraggebers: *„Ich möchte ein Werkzeug, das meine Obsidian-Notizen nach offenen
Aufgaben durchsucht."* Kein Platzhaltertext, echte Antworten.

**Entstanden ist ein vollständiger Rahmen:** Szenario, Vision, Stakeholder, Randbedingungen,
Glossar, Risiken, acht Anforderungen über fünf der sechs Kategorien, Qualitätsmerkmale
einzeln durchgegangen. Jede aus dem Szenario abgeleitete Anforderung zitiert ihre Stelle
unter `## Herkunft`.

| Prüfung im übergebenen Klon | Ergebnis |
| --- | --- |
| `check_vault`, `check_traceability`, `check_licenses` | je 0 Fehler, 0 Warnungen |
| `handover --check` | „Handover complete - this is a project of its own." |
| `check_armed` | sieben von sieben ARMED |
| Probe-Commit mit Produktivcode | **vom geschlossenen Gate verweigert** |

### Vier Befunde — zwei behoben, zwei notiert

1. **`handover --check` meldete die eigenen Anforderungen des Projekts** als „template
   history". Es konnte Rückstände der Vorlage nicht von dem unterscheiden, was das Projekt
   selbst erarbeitet hatte — Schritt 3a wäre **nie** sauber zurückgekommen. Behoben:
   `--apply` vermerkt `handover_done` in der Hook-Konfiguration; danach werden nur noch
   Platzhalter geprüft. **Mit Test.**
2. **Das archivierte Fortschrittslog wurde zur Waise.** Es war nur aus dem Index verlinkt,
   und ein neues Projekt schreibt seinen Index neu. Behoben: Die Archiv-README verlinkt jetzt
   jedes archivierte Dokument, nach Art gruppiert — nebenbei wird das Beispiel damit
   durchblätterbar. **Mit Test.**
3. **Schritt 1 ist mehrdeutig.** „For each entry whose `verified` date is older than 30
   days" und die darunter stehende Liste „Check at minimum: …" lesen sich widersprüchlich:
   Ist die Liste an die 30-Tage-Bedingung gebunden oder gilt sie immer? Ein Agent löst das
   nach Laune auf, ein Anfänger merkt es nicht. **Notiert, nicht behoben.**
4. **`baseline.md` behauptet nach der Übergabe weiter den Rahmen der Vorlage** — Zielartefakt
   und 36 REQ-Verweise, die ins Archiv zeigen — bis `/req-elicit` sie überschreibt.
   Entschärft, nicht folgenlos: Das geschlossene Gate verhindert, dass darauf gebaut wird,
   und der Platzhalter-Marker zwingt zum Ersetzen. **Notiert.**

### Zur Anfängertauglichkeit (REQ-0020)

Vom ersten Satz bis zum vollständigen Rahmen: **vier Fragerunden, elf Fragen**, jede mit
Vorschlägen zum Widersprechen. Der Nutzer musste nie aus dem Nichts formulieren und nie einen
Fachbegriff kennen. Der Qualitäts-Sweep hat gehalten, was er sollte — er hat sichtbar gemacht,
dass Wartbarkeit und Anpassbarkeit hier bewusst entfallen, statt sie zu übergehen.

Offen im Beispielprojekt geblieben: die Kategorie **Organisatorisch** und damit das Gate.
Beides gehört dem Menschen, nicht dem Erstlauf.

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
