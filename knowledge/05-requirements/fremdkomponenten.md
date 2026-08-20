---
title: Fremdkomponenten
aliases: ["Fremdkomponenten"]
type: knowledge
tags: [topic/requirements, topic/meta]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[Fremdlösungen]]", "[[REQ-0025 Übernommene Fremdkomponenten sind rechtlich geklärt]]", "[[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]", "[[00-index]]"]
---

# Fremdkomponenten

> **Wer auf fremdem Code aufsetzt, erbt dessen Pflichten.** Dieses Register führt sie —
> und `tools/check_licenses.py` prüft in CI, dass zu jedem Eintrag der Lizenztext im
> Repository liegt.
>
<!-- template-placeholder -->
> **Für ein eigenes Projekt:** Tabelle leeren und beim Übernehmen einer Komponente füllen.

## Kurz

Eine Lizenz, die erst beim Ausliefern auffällt, entwertet die darauf gebaute Arbeit. Deshalb
wird **vor** der Übernahme geprüft, ob die Lizenz zur Weitergabeabsicht des Projekts passt,
und die Entscheidung als ADR festgehalten — bei Unvereinbarkeit samt Ablehnungsgrund.

Vorgelagert: [[Fremdlösungen]] (`/solution-scan`) findet die Kandidaten.

## Ablauf vor jeder Übernahme

1. **Eigene Weitergabeabsicht feststellen.** Sie steht in der `recht`-Kategorie des Rahmens —
   hier [[REQ-0015 Öffentliche Bereitstellung mit geklärten Nutzungsrechten]]: öffentlich,
   MIT.
2. **Lizenz der Komponente lesen** — die Datei im Repository der Komponente, nicht die
   Angabe auf einer Paketseite. Die beiden weichen häufiger ab, als man denkt.
3. **Verträglichkeit prüfen** (Orientierung, kein Rechtsrat — im Zweifel entscheidet der
   Mensch, nicht der Agent):

   | Lizenzfamilie | Typische Pflichten | Wirkung auf eine MIT-Weitergabe |
   | --- | --- | --- |
   | MIT, BSD, ISC | Namensnennung, Lizenztext beilegen | unproblematisch |
   | Apache-2.0 | zusätzlich Änderungshinweis, Patentklausel | unproblematisch, Pflichten sind umfangreicher |
   | LGPL | Austauschbarkeit der Bibliothek, Quelloffenlegung der Bibliothek | möglich, aber mit Auflagen an die Einbindung |
   | GPL, AGPL | Quelloffenlegung des **gesamten** abgeleiteten Werks unter derselben Lizenz | unvereinbar mit einer MIT-Weitergabe |
   | keine Lizenz genannt | keine Rechte eingeräumt | **nicht verwendbar**, auch wenn der Code öffentlich liegt |

4. **Entscheidung als ADR**, auch bei Ablehnung. Ein Kandidat, der an der Lizenz scheitert,
   ist ein Befund — er wird begründet abgelehnt, nicht verschwiegen.
5. **Eintrag hier anlegen**, Lizenztext nach `licenses/` legen, Namensnennung ins `README.md`
   setzen, wo sie verlangt wird.

## Register

Format eines Eintrags:

```
| Komponente | Version | Lizenz | Lizenztext | Pflichten | Quelle (abgerufen) |
| beispiel-lib | 2.3.1 | MIT | `licenses/beispiel-lib-LICENSE.txt` | Namensnennung, Lizenztext beilegen | https://github.com/… (2026-08-20) |
```

| Komponente | Version | Lizenz | Lizenztext | Pflichten | Quelle (abgerufen) |
| --- | --- | --- | --- | --- | --- |

**Leer.** Das Template übernimmt keinen Fremdcode —
[[ADR-0010 Eigene Umsetzung statt Fremdbasis]]. Ein leeres Register ist ein gültiger Zustand
und kein fehlender Eintrag.

## Was die Prüfung leistet — und was nicht

`tools/check_licenses.py` prüft **Vollständigkeit**: dass jeder Eintrag vollständig ist, sein
Lizenztext im Repository liegt und die Quelle ein Abrufdatum trägt. Zusätzlich meldet sie
einen Lizenztext, den kein Eintrag referenziert.

Sie prüft **nicht die Rechtmäßigkeit**. Ob eine Lizenz zum Vorhaben passt, entscheidet der
Mensch. Das Werkzeug stellt nur sicher, dass niemand die Frage überspringt — wer daraus ein
Gefühl von Rechtssicherheit ableitet, hat es missverstanden.
