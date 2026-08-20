# @contract
# provides:   every document tools/handover.py writes out: SKELETONS (filename -> empty
#             framework form), ARCHIVE_README, EMPTY_BOARD; the first two carry
#             {today}/{review} placeholders for the dates
# depends-on: none - pure data, formatted by its consumer
# consumers:  tools/handover.py#write_skeletons, #write_archive_readme, #apply
# invariants: every skeleton keeps its title and aliases so wikilinks survive, carries the
#             template-placeholder marker so the handover check still demands filling in,
#             and holds at least one outgoing wikilink so check_vault sees no orphan
# updated:    2026-08-20

#!/usr/bin/env python3
"""The documents a clone receives when it stops being the template.

A beginner reading another project's filled-in framework learns the wrong thing;
worse, an agent may append to its category lists instead of replacing them. So the
handover leaves forms with prompts rather than somebody else's answers.

Separate module because these are literals, not logic: keeping them here is what
holds handover.py itself inside the file-length limit.
"""
from __future__ import annotations

HEAD = """---
title: {title}
aliases: [{aliases}]
type: knowledge
tags: [topic/requirements]
status: active
{extra}created: {{today}}
updated: {{today}}
review_after: {{review}}
related: [{related}]
---

<!-- template-placeholder -->
> **Noch auszufüllen.** {hint}

# {title}

"""


# Six parameters over the limit of three: each is one field of the document being
# described, and grouping them into an object would only move the six names one level
# away from the eight call sites that have to read as documents, not as constructors.
def document(title, aliases, related, hint, body, extra=""):
    """One skeleton: frontmatter, fill-in banner, then the empty structure."""
    return HEAD.format(title=title, aliases=aliases, related=related,
                       hint=hint, extra=extra) + body


SKELETONS = {
    "baseline.md": document(
        "Rahmen und Startgate", '"Rahmen und Startgate", "baseline"',
        '"[[Projektvision]]", "[[00-index]]"',
        "`/req-elicit` füllt diese Datei. Solange `baseline_status: entwurf` steht, "
        "entsteht kein Produktivcode.",
        """> **Diese Datei entscheidet, ob entwickelt werden darf.** Nur ein Mensch setzt
> `baseline_status` auf `vereinbart`.

## Zielartefakt

*Was wird gebaut? Zwei bis drei Sätze — was es ist, für wen, und woran man erkennt, dass es
fertig ist.*

## Projektzuschnitt

*`project_scope` aus `.claude/hooks/config.json`, und der **Grund** für die Wahl.*

## Kategorien

Jede der sechs braucht entweder eine Anforderung **oder** eine geschriebene Begründung,
warum sie hier nicht greift. Beides ist gültig; nichts zu schreiben ist es nicht.

### Funktional

*Was muss es können, um überhaupt einen Nutzen zu haben?*

### Technisch

*Worauf läuft es, womit arbeitet es zusammen, mit welchen Datenmengen?*

### Organisatorisch

*Wer betreibt es, wie wird es weitergegeben — und wie wird entwickelt?*

### Sicherheit

*Was ist zu schützen, und vor wem?*

### Recht

*Lizenzen, Vorschriften, Rechte am Ergebnis.*

### Qualität

*Wie gut, wie schnell, wie zuverlässig? Die acht Merkmale einzeln durchgehen —
`/req-elicit` führt durch.*

## Freigabe

| Feld | Wert |
| --- | --- |
| Rahmen vorgelegt am | *Datum* |
| Freigegeben durch | *— offen* |
""", extra="baseline_status: entwurf\n"),

    "vision.md": document(
        "Projektvision", '"Projektvision", "vision"',
        '"[[Rahmen und Startgate]]", "[[00-index]]"',
        "Das Warum des Projekts auf einer Seite — verständlich, ohne eine einzige "
        "Anforderung zu kennen.",
        """## Kurz

*Zwei bis drei Zeilen: was hier entsteht und wofür.*

## Problem

*Was ist heute mühsam, fehleranfällig oder unmöglich? Ohne diesen Absatz weiß später
niemand mehr, warum es das Projekt gibt.*

## Zielartefakt

*Was genau entsteht — Skript, Werkzeug, Dienst, Bibliothek, Anwendung?*

## Erfolgskriterien

*Woran misst man, dass es geklappt hat? Beobachtbar formulieren.*

## Nicht-Ziele

*Was ausdrücklich **nicht** gebaut wird. Der wertvollste Abschnitt — und der, den niemand
von selbst schreibt.*

## Offene Fragen

- *offen gebliebene Punkte, oder „keine"*
"""),

    "stakeholders.md": document(
        "Stakeholder", '"Stakeholder"',
        '"[[Rahmen und Startgate]]", "[[Projektvision]]"',
        "Wer betroffen ist — und wer entscheidet, wenn Anforderungen sich widersprechen.",
        """## Beteiligte

| Wer | Rolle | Interesse |
| --- | --- | --- |
| *Name* | *Auftraggeber, Nutzer, Betrieb …* | *woran dieser Person gelegen ist* |

## Wer nicht gefragt wurde

*Ausdrücklich benennen. Wessen Interessen fehlen, merkt man sonst erst spät.*
"""),

    "constraints.md": document(
        "Randbedingungen", '"Randbedingungen"',
        '"[[Rahmen und Startgate]]"',
        "Was von außen feststeht und nicht verhandelt wird.",
        """## Kernpunkte

- *Vorgegebene Technik, Formate, Schnittstellen*
- *Zeitliche oder finanzielle Grenzen*
- *Vorhandene Systeme, an die man sich anpassen muss*

Unterschied zur Anforderung: Eine Randbedingung **steht fest**, eine Anforderung wird
vereinbart.
"""),

    "glossary.md": document(
        "Glossar", '"Glossar"',
        '"[[Rahmen und Startgate]]", "[[Methodenglossar]]"',
        "Das Vokabular der Fachdomäne — eine Schreibweise je Begriff, auch für den Code.",
        """## Begriffe

**Begriff**
*Was er bedeutet. Und wie er im Code heißt — eine Schreibweise, keine zwei.*

Die Begriffe des **Verfahrens** (Anforderung, Startgate, ADR …) stehen im
[[Methodenglossar]], nicht hier.
"""),

    "risks.md": document(
        "Risiken", '"Risiken"',
        '"[[Rahmen und Startgate]]"',
        "Was das Projekt gefährdet — und was dagegen läuft.",
        """## Register

| Risiko | Wirkung | Was dagegen läuft |
| --- | --- | --- |
| *Was schiefgehen kann* | *Was es kostet* | *Anforderung, Prüfung oder Entscheidung* |

Ein Risiko ohne Gegenmaßnahme ist kein Eintrag, sondern eine Sorge. Entweder etwas dagegen
tun, oder es bewusst hinnehmen — und das hinschreiben.
"""),

    "fremdloesungen.md": document(
        "Fremdlösungen", '"Fremdlösungen"',
        '"[[Rahmen und Startgate]]"',
        "`/solution-scan` füllt diese Datei. Solange `scan_status: offen` steht, "
        "entsteht kein Produktivcode.",
        """## Kurz

Die billigste Zeile Code ist die, die jemand anderes schon geschrieben und gewartet hat.
Nach der Erhebung und **vor** der ersten Codeaufgabe wird einmal geschaut, ob es das
Gesuchte schon gibt — gemessen an den vereinbarten Anforderungen.

## Status

| Feld | Wert |
| --- | --- |
| `scan_status` | `offen` |

`gesucht` **oder** `uebersprungen` — mit Grund — öffnen beide das Gate. Unbeantwortet nicht.

## Geprüfte Kandidaten

*Je Kandidat: Quelle mit Abrufdatum, Lizenz, Wartungsstand, und je Anforderung erfüllt /
teilweise / nicht. Kein Kandidat ohne abgerufene Quelle.*
""", extra="scan_status: offen\n"),

    "fremdkomponenten.md": document(
        "Fremdkomponenten", '"Fremdkomponenten"',
        '"[[Fremdlösungen]]", "[[Rahmen und Startgate]]"',
        "Nur nötig, wenn Fremdcode übernommen wird — dann aber vor der Übernahme.",
        """## Kurz

Wer auf fremdem Code aufsetzt, erbt dessen Pflichten. `tools/check_licenses.py` prüft in CI,
dass zu jedem Eintrag der Lizenztext im Repository liegt.

## Register

| Komponente | Version | Lizenz | Lizenztext | Pflichten | Quelle (abgerufen) |
| --- | --- | --- | --- | --- | --- |

*Leer ist ein gültiger Zustand — er heißt: kein Fremdcode, keine geerbten Pflichten.*
"""),
}

ARCHIVE_README = """---
title: Beispielarchiv
aliases: ["Beispielarchiv"]
type: knowledge
tags: [topic/meta]
status: active
created: {today}
updated: {today}
review_after: {review}
related: ["[[00-index]]"]
---

# Beispielarchiv

## Kurz

Hier liegt der Projektstand der **Vorlage**, aus der dieses Projekt geklont wurde:
ihre Anforderungen, Aufgaben, Entscheidungen, ihr Fortschrittslog und ihr Szenario.
Verschoben von `tools/handover.py`, damit sie das eigene Projekt nicht belasten.

## Wozu das gut ist

Ein ausgefülltes Beispiel zeigt mehr als eine leere Vorlage. Wer wissen will, wie eine
brauchbare Anforderung aussieht, was in einen ADR gehört oder wie eine Aufgabe geschnitten
wird, findet hier vier Dutzend echte Fälle — samt der Fehler, die dabei gemacht wurden.

## Was hier liegt

{inhalt}

## Was es nicht ist

**Keine Anforderung dieses Projekts.** Die Prüfwerkzeuge sehen dieses Verzeichnis nicht an:
`check_traceability.py` liest nur `05-requirements` und `10-pm/tasks`, und die
Platzhalterprüfung überspringt diesen Pfad. Nichts hier gilt für dich.

Wenn du es nicht brauchst: löschen. Es hängt nichts daran.
"""

EMPTY_BOARD = """---

kanban-plugin: board

---

## Backlog

## Ready

## Doing

## Review

## Done

%% kanban:settings
```
{"kanban-plugin":"board","show-checkboxes":true,"lane-width":320}
```
%%
"""
