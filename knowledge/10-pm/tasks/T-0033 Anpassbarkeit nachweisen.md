---
id: T-0033
title: Anpassbarkeit nachweisen
type: task
implements: ["[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]]"]
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-20
started:
finished:
tags: [topic/meta, topic/requirements]
related: ["[[T-0004 Stack-Profile und Doku-Schema]]", "[[T-0022 Projektzuschnitt bestimmt die Zeremonie]]", "[[REQ-0018 Das Template hält seine eigenen Vorgaben ein]]"]
---

# T-0033 Anpassbarkeit nachweisen

## Anforderung

[[REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln]] — der Teil, der noch fehlt.
Die Anpassungsstellen existieren; **nachgewiesen** ist noch keine davon.

## Ziel

`nachweis: demo`. Eine Eigenschaft, die niemand vorgeführt hat, ist eine Behauptung — und
ungeprüfte Eigenschaften verschwinden mit der Zeit.

## Akzeptanzkriterien

- [ ] Stackwechsel durchgespielt: von `stacks/python.md` auf `stacks/typescript.md`, indem
      nur `stacks/active.md` ersetzt wird
- [ ] Dabei nachgewiesen, dass **keine** Datei unter `.claude/rules/` und `.claude/hooks/`
      angefasst werden musste — belegt über `git diff --name-only`, nicht behauptet
- [ ] Schwellwertänderung durchgespielt: eine Grenze in `config.json` geändert, Wirkung im
      Hook sichtbar, kein Hook-Code berührt
- [ ] Platzhalterprüfung: ein Werkzeug oder eine dokumentierte Prüfung findet
      Template-Platzhalter in `00-index.md`, `README.md`, `vision.md`, `baseline.md`
- [ ] Was sich dabei als **nicht** anpassbar herausstellt, wird als Befund festgehalten —
      nicht stillschweigend nachgebessert
- [ ] Ergebnis im Fortschrittslog, Anforderung auf `umgesetzt`, sofern die Abnahme trägt

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
