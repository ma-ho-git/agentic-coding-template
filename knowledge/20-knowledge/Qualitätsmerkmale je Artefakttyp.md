---
title: Qualitätsmerkmale je Artefakttyp
type: knowledge
tags: [topic/requirements]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Funktionale und nicht-funktionale Anforderungen]]", "[[Rahmen und Startgate]]", "[[00-index]]"]
---

# Qualitätsmerkmale je Artefakttyp

## Kurz

Welche Qualitätsmerkmale bei welcher Art von Software tatsächlich entscheiden — mit je einer
messbaren Beispielanforderung. Vorlage für `/req-elicit`, damit ein Anfänger nicht ein
CLI-Beispiel auf seinen Dienst übertragen muss.

> **Die Frageliste ändert sich nie.** Alle acht Merkmale werden in jedem Projekt gefragt
> ([[Funktionale und nicht-funktionale Anforderungen]]). Artefaktabhängig sind **Beispiele,
> Messgrößen und die erwartete Tiefe** — nie der Umfang der Prüfung. Dieselbe Grenze wie beim
> Projektzuschnitt.

> **Belastbarkeit:** Handwerkswissen, keine Norm. Nur die Versionierungsregel für Bibliotheken
> hat eine zitierbare Quelle (SemVer 2.0.0). Die Profile sind eine Vorauswahl zum
> Widersprechen, kein Katalog zum Abhaken.

## Kernpunkte

- Ein **Profil ersetzt die Erhebung nicht**, es liefert den Einstiegsvorschlag. Der Nutzer
  widerspricht — das ist billiger, als aus dem Nichts zu antworten.
- **Gemischter oder unklarer Typ:** beide Profile anbieten, nicht raten. Ein Werkzeug mit
  Weboberfläche ist beides.
- Am aufschlussreichsten ist meist, **was ein Profil weglässt**. „Tempo ist hier egal" ist
  eine vollwertige Antwort und spart dem Projekt eine erfundene Zahl.

## Details — die Profile

### Bibliothek

Der Aufrufer ist fremder Code, nicht ein Mensch. Alles dreht sich um den Vertrag.

| Merkmal | Messbares Beispiel |
| --- | --- |
| **Zusammenspiel** *(entscheidend)* | „Wer auf 2.x festgelegt ist, läuft nach jedem Minor-Update unverändert weiter — geprüft an der Testsuite eines Beispielaufrufers." |
| **Wartbarkeit** | „Eine öffentliche Funktion verschwindet nie stillschweigend: Abkündigung steht mindestens eine Minor-Version vor der Entfernung in der Freigabemitteilung." |
| **Bedienbarkeit** | „Ein fremder Entwickler bindet die Bibliothek in unter 15 Minuten ein, allein anhand der README." |
| **Zuverlässigkeit** | „Es treten nur dokumentierte Ausnahmetypen nach außen; interne Fehler werden übersetzt, nicht durchgereicht." |

Meist nicht relevant: Tempo (außer in Kernschleifen), Gefahr für Mensch oder Sachwert.

### Kommandozeilenwerkzeug

Läuft in Skripten und in Pipes. Bedient wird es von Menschen **und** von anderen Programmen.

| Merkmal | Messbares Beispiel |
| --- | --- |
| **Bedienbarkeit** | „`--help` erklärt jede Option in einer Zeile; die Standardaufgabe gelingt ohne Handbuch beim ersten Versuch." |
| **Zusammenspiel** *(oft übersehen)* | „Nutzdaten nach stdout, Meldungen nach stderr, Exit-Code 0 nur bei Erfolg — damit es in einer Pipe funktioniert." |
| **Tempo** | „10.000 Zeilen in unter 2 Sekunden, inklusive Start." |
| **Anpassbarkeit** | „Läuft unter Linux und macOS ohne zusätzliche Systempakete." |
| **Zuverlässigkeit** | „Bricht bei kaputter Eingabe ab, ohne eine halb geschriebene Zieldatei zu hinterlassen." |

### Dienst oder API

Läuft dauerhaft, wird von außen benutzt, fällt irgendwann aus.

| Merkmal | Messbares Beispiel |
| --- | --- |
| **Zuverlässigkeit** | „Verfügbarkeit 99,5 % im Monat, gemessen an einer Statusprüfung im Minutentakt." |
| **Tempo** | „p95 der Antwortzeit unter 200 ms bei 50 gleichzeitigen Nutzern." |
| **Sicherheit** | „Kein Endpunkt ohne Authentifizierung; Zugriffe werden protokolliert, ohne Nutzdaten mitzuschreiben." |
| **Wartbarkeit** | „Jede Anfrage trägt eine Korrelations-ID, die im Protokoll wiederauffindbar ist." — ohne das ist ein Fehlerbericht aus dem Betrieb wertlos |
| **Zusammenspiel** | „Eine bestehende Schnittstellenversion bleibt nach einer Änderung mindestens sechs Monate erreichbar." |

### Datenstrecke (Batch, Import, ETL)

Läuft unbeaufsichtigt und bricht mitten drin ab. Genau darum geht es.

| Merkmal | Messbares Beispiel |
| --- | --- |
| **Zuverlässigkeit** *(entscheidend)* | „Ein zweimal gestarteter Lauf erzeugt dasselbe Ergebnis und keine Dubletten." — Idempotenz |
| **Zuverlässigkeit, zweiter Teil** | „Ein Abbruch nach der Hälfte lässt sich ohne manuelles Aufräumen erneut starten." |
| **Tempo** | „Der Tageslauf verarbeitet 5 Millionen Zeilen in unter 30 Minuten." |
| **Funktionale Eignung** | „Zeilen, die die Prüfregeln verletzen, landen vollständig in einer Fehlerdatei — nie stillschweigend verworfen." |

### Anwendung mit Oberfläche

Ein Mensch sitzt davor und urteilt in Sekunden.

| Merkmal | Messbares Beispiel |
| --- | --- |
| **Bedienbarkeit** | „Ein geübter Nutzer schließt die Hauptaufgabe in unter 30 Sekunden ab." |
| **Tempo** *(gefühlt, nicht gemessen am Server)* | „Jede Aktion gibt in unter 100 ms sichtbare Rückmeldung; längere Vorgänge zeigen Fortschritt." |
| **Bedienbarkeit, Barrierefreiheit** | „Alle Funktionen per Tastatur erreichbar, Kontrastverhältnis mindestens 4,5:1." |
| **Zusammenspiel** | „Läuft in den jeweils letzten zwei Hauptversionen von Firefox, Chrome und Safari." |

### Wegwerfskript

Das ehrlichste Profil: Fast nichts trifft zu, und das aufzuschreiben ist die Arbeit.

| Merkmal | Messbares Beispiel |
| --- | --- |
| **Zuverlässigkeit** *(das einzige, das fast immer bleibt)* | „Bricht mit Fehlermeldung ab, statt eine halb bearbeitete Datei zu hinterlassen." |
| **Sicherheit** *(nur wenn echte Daten im Spiel sind)* | „Verarbeitet Kundendaten nur im Arbeitsspeicher, schreibt nichts auf Platte." |

Alles andere wird mit einem Satz abgewählt: „Läuft einmal auf meinem Rechner, danach gelöscht."
Wichtig ist, dass die Abwahl **dasteht** — sonst weiß beim zweiten Lauf niemand mehr, dass es
eine Entscheidung war.

## Quellen

- Semantic Versioning 2.0.0 — https://semver.org/ (2026-08-20, über die Suche ermittelt;
  Abruf durch den Egress-Proxy blockiert)
- Übrige Profile: Handwerkswissen, keine Einzelquelle. Bei Zweifel am konkreten Schwellwert
  entscheidet der Nutzer, nicht dieses Dokument.
