---
id: T-0033
title: Anpassbarkeit nachweisen
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
related: ["[[T-0004 Stack-Profile und Doku-Schema]]", "[[T-0022 Projektzuschnitt bestimmt die Zeremonie]]", "[[REQ-0018 Das Template hält seine eigenen Vorgaben ein]]", "[[T-0034 Erstlauf im frischen Klon durchspielen]]"]
---

# T-0033 Anpassbarkeit nachweisen

## Anforderung

[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]] — der Teil, der noch fehlt.
Die Anpassungsstellen existieren; **nachgewiesen** ist noch keine davon.

## Ziel

`nachweis: demo`. Eine Eigenschaft, die niemand vorgeführt hat, ist eine Behauptung — und
ungeprüfte Eigenschaften verschwinden mit der Zeit.

## Akzeptanzkriterien

- [x] Stackwechsel durchgespielt: von `stacks/python.md` auf `stacks/typescript.md`, indem
      nur `stacks/active.md` ersetzt wird
- [x] Dabei nachgewiesen, dass **keine** Datei unter `.claude/rules/` und `.claude/hooks/`
      angefasst werden musste — belegt über `git diff --name-only`, nicht behauptet
- [x] Schwellwertänderung durchgespielt: eine Grenze in `config.json` geändert, Wirkung im
      Hook sichtbar, kein Hook-Code berührt
- [x] Platzhalterprüfung: ein Werkzeug oder eine dokumentierte Prüfung findet
      Template-Platzhalter in `00-index.md`, `README.md`, `vision.md`, `baseline.md`
- [x] Was sich dabei als **nicht** anpassbar herausstellt, wird als Befund festgehalten —
      nicht stillschweigend nachgebessert
- [x] Ergebnis im Fortschrittslog, Anforderung auf `umgesetzt`, sofern die Abnahme trägt

## Ergebnis

Drei Durchläufe, je mit `git diff --name-only` als Beleg statt einer Behauptung.

| Durchgespielt | Geänderte Dateien | Ergebnis |
| --- | --- | --- |
| Stackwechsel Python → TypeScript | nur `stacks/active.md` | alle Prüfungen und 106 Tests grün |
| `max_assignments` 20 → 2 | nur `.claude/hooks/config.json` | Hook meldete sofort vier Überschreitungen in `check_vault.py` |
| `project_scope` produkt → skript | nur `.claude/hooks/config.json` | Sitzungsbericht wechselte den Text |

Keine Datei unter `.claude/rules/` und keine unter `.claude/hooks/` musste angefasst werden.
Alle drei Änderungen wurden anschließend zurückgenommen — **der Diff war der Beleg, nicht der
Endzustand.**

### Zwei Befunde, die niemand bestellt hatte

1. **Der Stackwechsel ist folgenlos, weil kein Code das Stack-Profil liest.** `stacks/active.md`
   wird nur von zwei Skills in Prosa erwähnt; kein Hook, kein Werkzeug, keine CI-Zeile liest
   es. Die Abnahme trägt — aber aus einem schwächeren Grund als die Formulierung nahelegt.
   Nebenwirkung: Nichts prüft, ob das aktive Profil zur Wirklichkeit passt. Man kann auf
   TypeScript umstellen, während das Repository Python bleibt, und nichts beschwert sich.
2. **`.github/workflows/rules.yml` verdrahtet `python3` und `pytest` fest.** Ein Projekt, das
   den Stack wechselt, muss die CI-Datei anfassen. Der Wortlaut der Anforderung nennt nur
   `.claude/rules/` und `.claude/hooks/` — verletzt ist er also nicht. Dem Sinn nach ist der
   Stackwechsel damit trotzdem nicht vollständig. Zur Entscheidung vorgelegt, nicht
   stillschweigend zur Aufgabe gemacht.

### Platzhalterprüfung — erst musste ein Marker her

Die vier Pflichtdokumente trugen **drei verschiedene Formulierungen** („Für ein eigenes
Projekt", „Beim Start eines eigenen Projekts") und die README gar keine. Eine mechanische
Prüfung darauf wäre geraten gewesen. Also zuerst ein eindeutiger Marker
`<!-- template-placeholder -->` in alle betroffenen Dokumente, dann das Werkzeug.

`tools/check_placeholders.py` meldet für dieses Repository 12 Dokumente, 4 davon Kern — und
**das ist die richtige Antwort**: Hier gehören die Platzhalter hin. Deshalb läuft die Prüfung
in `/bootstrap` (Schritt 4a) und **nicht in CI**; eine Prüfung, deren korrektes Ergebnis „rot"
ist, gehört nicht in die Pipeline. Begründung in `.claude/rules/guardrails.md` festgehalten,
damit sie niemand später „repariert".

### Abnahmestand von REQ-0026

Vier der fünf Punkte tragen, einer ist **erst im Klon beobachtbar** und liegt als
[[T-0034 Erstlauf im frischen Klon durchspielen]] bereit. Die Anforderung bleibt deshalb
`vereinbart` und geht **nicht** auf `umgesetzt` — die Tabelle mit dem Einzelstand steht in
der Anforderung selbst.

Fünf neue Tests, Suite 111 grün. `check_vault.py`, `check_traceability.py` und
`check_licenses.py` ohne Befund.

## Kontext

- Gebaut wurde das Verhalten in [[T-0004 Stack-Profile und Doku-Schema]] und
  [[T-0022 Projektzuschnitt bestimmt die Zeremonie]]; diese Aufgabe liefert den Beleg
- Gleiche Haltung wie [[REQ-0018 Das Template hält seine eigenen Vorgaben ein]]: nachweisen
  statt behaupten

## Agent

`claude-code` — Durchspielen, Git-Diff als Beleg, gegebenenfalls kleines Prüfwerkzeug.

## Abhängigkeiten

- keine

## Notizen

- Der Stackwechsel wird **durchgespielt und zurückgenommen**, nicht dauerhaft vollzogen:
  Dieses Repository bleibt auf Python. Der Beleg ist der Diff, nicht der Endzustand.
- Ehrliche Erwartung: Die Platzhalterprüfung findet vermutlich etwas. `README.md` und
  `00-index.md` tragen bewusst Template-Hinweise — dann ist zu klären, ob die Abnahme
  „keine Rückstände nach `/bootstrap`" den Ist-Zustand vor `/bootstrap` überhaupt meint.
