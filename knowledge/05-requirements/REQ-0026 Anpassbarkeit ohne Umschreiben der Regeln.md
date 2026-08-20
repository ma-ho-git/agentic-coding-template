---
title: Anpassbarkeit ohne Umschreiben der Regeln
type: requirement
ebene: rahmen
kategorie: qualitaet
prioritaet: muss
stufe:
quelle: Marcus (Auftraggeber), Ergänzung vom 2026-08-20 — Lücke aus dem Qualitätsmerkmale-Durchgang (T-0031)
nachweis: demo
status: vereinbart
tasks: ["[[T-0004 Stack-Profile und Doku-Schema]]", "[[T-0022 Projektzuschnitt bestimmt die Zeremonie]]", "[[T-0033 Anpassbarkeit nachweisen]]", "[[T-0034 Erstlauf im frischen Klon durchspielen]]"]
tags: [topic/requirements, topic/meta]
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[Rahmen und Startgate]]", "[[Projektvision]]", "[[REQ-0001 Einsatzbereites Gerüst für strukturiertes Vibe-Coding]]", "[[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]]"]
---

# REQ-0026 Anpassbarkeit ohne Umschreiben der Regeln

## Anforderung

Das Template muss sich an ein neues Projekt anpassen lassen, ohne dass seine Regeln oder
Prüfskripte umgeschrieben werden müssen. Angepasst wird über vorgesehene Stellen —
Stack-Profil, Schwellwerte, Projektzuschnitt, Anforderungsbereich —, nicht durch Eingriffe
in `.claude/rules/` oder `.claude/hooks/`.

## Begründung

Bei einer Vorlage, die geklont und umgebaut wird, ist Anpassbarkeit kein Nebeneffekt, sondern
der Kern des Nutzens. Wer zum Anpassen eine Regeldatei aufmachen muss, ändert sie — und ab da
driftet jedes Projekt in eine eigene Richtung. Dann ist es keine Vorlage mehr, sondern ein
Ausgangspunkt, den niemand mehr aktualisieren kann.

Der zweite Grund ist der Nutzer, für den das hier gedacht ist: Wer die Regeln nicht beurteilen
kann, soll sie nicht bearbeiten müssen, um loszulegen. Die vorgesehenen Stellen sind genau
die, an denen eine falsche Entscheidung nichts kaputt macht.

Die Lücke fiel am 2026-08-20 auf, als die Qualitätsmerkmale zum ersten Mal einzeln
durchgegangen wurden. Das Template *war* längst anpassbar — nur verlangt hatte es niemand,
und ungeprüfte Eigenschaften verschwinden mit der Zeit.

## Abnahme

- **Stackwechsel ohne Regeländerung.** Ein Projekt wechselt die Programmiersprache, indem
  `stacks/active.md` ersetzt wird. Keine Datei unter `.claude/rules/` und keine unter
  `.claude/hooks/` wird dabei angefasst — nachgewiesen an einem Durchlauf.
- **Schwellwerte ohne Codeänderung.** Jede flexible Grenze ist in
  `.claude/hooks/config.json` änderbar; kein Hook muss dafür bearbeitet werden.
- **Zeremonie ohne Regeländerung.** `project_scope` verändert Dokumentationspflicht und
  Erhebungstiefe, ohne dass eine Regeldatei neu geschrieben wird.
- **Keine Rückstände nach der Übernahme.** Nach `/bootstrap` enthält kein Pflichtdokument des
  Projekts (`00-index.md`, `README.md`, `vision.md`, `baseline.md`) noch einen
  Template-Platzhalter.
- **Grenze, ausdrücklich:** Nicht anpassbar sind die **starren Leitplanken**
  (`.claude/rules/guardrails.md`). Sie zu ändern ist eine Entscheidung des Menschen an der
  Regel selbst, kein Anpassungsvorgang — sonst wird „anpassbar" zum Freibrief, genau wie es
  der Projektzuschnitt nicht sein darf ([[ADR-0007 Projektzuschnitt skaliert nur die Dokumentation]]).

## Präzisierungen

### 2026-08-20 — nachträglich erhoben, Nachweis steht aus

Das Verhalten war vor der Anforderung da: [[T-0004 Stack-Profile und Doku-Schema]] und
[[T-0022 Projektzuschnitt bestimmt die Zeremonie]] haben die Anpassungsstellen gebaut, ohne
dass eine Anforderung sie verlangte. Beide sind rückwirkend verknüpft.

**Vorgeführt ist bisher keine davon.** Das holt [[T-0033 Anpassbarkeit nachweisen]] nach —
bis dahin bleibt die Anforderung `vereinbart`, nicht `umgesetzt`.

### 2026-08-20 — Stand der Abnahme nach T-0033

| Abnahmepunkt | Stand |
| --- | --- |
| Stackwechsel ohne Regeländerung | **belegt** — `git diff --name-only` zeigt nur `stacks/active.md`; alle Prüfungen und 106 Tests blieben grün |
| Schwellwerte ohne Codeänderung | **belegt** — `max_assignments` auf 2 gesetzt, der Hook meldete sofort vier Überschreitungen; nur `config.json` im Diff |
| Zeremonie ohne Regeländerung | **belegt** — `project_scope: skript` änderte den Sitzungsbericht; nur `config.json` im Diff |
| Keine Rückstände nach `/bootstrap` | **offen** — im Template selbst nicht zeigbar, hier gehören die Platzhalter hin. Prüfwerkzeug existiert (`tools/check_placeholders.py`), der Durchlauf fehlt: [[T-0034 Erstlauf im frischen Klon durchspielen]] |
| Starre Leitplanken nicht anpassbar | **gilt konstruktionsbedingt** — es gibt keinen Konfigurationswert, der eine starre Prüfung abschaltet; `project_scope` und `config.json` erreichen sie nicht |

**Deshalb bleibt die Anforderung `vereinbart`, nicht `umgesetzt`.** Vier von fünf Punkten
tragen; einer ist erst im Klon beobachtbar.

**Zwei Befunde aus dem Nachweis, die niemand bestellt hatte:**

1. Der Stackwechsel ist folgenlos, **weil kein Code das Stack-Profil liest**. `stacks/active.md`
   ist Dokumentation für den Agenten, kein Konfigurationswert. Die Abnahme trägt — aber aus
   einem schwächeren Grund als die Formulierung nahelegt, und nichts prüft, ob das aktive
   Profil zur Wirklichkeit passt.
2. `.github/workflows/rules.yml` verdrahtet `python3` und `pytest` fest. Ein Projekt, das auf
   TypeScript wechselt, **muss die CI-Datei anfassen**. Der Wortlaut der Anforderung nennt nur
   `.claude/rules/` und `.claude/hooks/`, ist also nicht verletzt — dem Sinn nach ist der
   Stackwechsel damit trotzdem nicht vollständig.

## Offene Fragen

- keine
