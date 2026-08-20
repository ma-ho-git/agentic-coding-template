---
title: Methodenglossar
aliases: ["Methodenglossar", "methodenglossar"]
type: knowledge
tags: [topic/requirements, topic/meta]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-08-20
related: ["[[Rahmen und Startgate]]", "[[Glossar]]", "[[00-index]]"]
---

# Methodenglossar

## Kurz

Die Begriffe des **Verfahrens**, je in zwei Zeilen. Nicht zu verwechseln mit dem [[Glossar]]
— das erklärt die Fachdomäne des Projekts, dieses hier die Arbeitsweise.

Für alle gedacht, die mit dem Template starten, ohne Software-Engineering gelernt zu haben.
Wer einen Begriff in einer Rückfrage nicht kennt: hier steht er.

## Anforderungen

**Anforderung**
Ein Satz darüber, was das System können oder einhalten muss — plus die Begründung und eine
prüfbare Abnahme. Sagt *was*, nie *wie*.

**Rahmen**
Die Anforderungen, die vor dem ersten Code feststehen müssen: was gebaut wird, und was
dabei gilt. Wer sie spät entdeckt, wirft fertige Arbeit weg.

**Detailanforderung**
Anforderung für die nächste Entwicklungsstufe. Wird bei Bedarf erhoben, nicht auf Vorrat,
und darf beim Programmieren nachgeschärft werden.

**Startgate**
Die Freigabe in `baseline.md`. Solange sie zu ist, entsteht kein Produktivcode — durchgesetzt
durch einen Hook, nicht nur angemahnt. Nur ein Mensch öffnet sie.

**Abnahme**
Der Teil der Anforderung, der sagt, woran man erkennt, dass sie erfüllt ist. Muss messbar,
beobachtbar oder testbar sein.

**Prüfbarkeit**
Die Regel, dass eine Anforderung ohne prüfbare Abnahme noch keine ist. „Benutzerfreundlich"
fällt durch, „geübter Nutzer schafft X in unter 30 Sekunden" besteht.

**Rückverfolgbarkeit**
Die Kette Stakeholder → Anforderung → Aufgabe → Test → Code. Beantwortet in beide Richtungen:
warum gibt es diesen Code, und wo steckt diese Anforderung im Code.

**Stakeholder**
Wer ein Interesse am System hat. Jede Anforderung nennt, von wem sie kommt — sonst lässt sie
sich später nicht klären.

## Arbeitsweise

**Aufgabe (Task)**
Eine Arbeitseinheit mit Akzeptanzkriterien, die eine Anforderung erfüllt. Liegt als Datei
vor und als Karte auf dem Board.

**Board**
Die Übersicht aller Aufgaben in Spalten: Backlog, Ready, Doing, Review, Done. Zeigt den
Stand; die Wahrheit steht in der Aufgabendatei.

**ADR** (Architecture Decision Record)
Notiz über eine Entscheidung zwischen echten Alternativen: Kontext, Optionen, Entscheidung,
Folgen. Damit später nachvollziehbar ist, warum es so kam.

**TDD** (testgetriebene Entwicklung)
Erst der Test, der fehlschlägt, dann der Code, der ihn bestehen lässt. Verhindert Tests, die
nur bestätigen, was ohnehin schon dasteht.

**Contract-Kommentar**
Ein Block am Anfang jeder Quelldatei, der festhält, wovon sie abhängt und wer sie benutzt.
Macht bei einer Änderung sichtbar, was sonst noch betroffen ist.

**Wirkungsradius**
Die Menge der Stellen, die eine Änderung mitzieht. Steht im Contract-Kommentar, damit man
sie nicht suchen muss.

## Leitplanken

**Starre Leitplanke** — `[RIGID]`
Eine Grenze, die nicht nachgibt, weil ihre Verletzung nicht heilbar ist. Wird maschinell
durchgesetzt; der Agent kann sie nicht überstimmen.

**Flexible Leitplanke** — `[FLEXIBLE]`
Ein Hinweis auf die üblicherweise bessere Lösung. Darf überschritten werden — dann gehört
die Begründung in den Code.

**Hook**
Ein kleines Skript, das automatisch bei bestimmten Aktionen läuft und Regeln durchsetzt.
Läuft, ob der Agent will oder nicht.

**Skill**
Ein aufrufbarer Ablauf, z. B. `/req-elicit`. Wird nur geladen, wenn er gebraucht wird.

## Wenn etwas trotzdem unklar ist

Frag nach. Eine beantwortete Frage ist billiger als eine geratene Annahme — das gilt in
beide Richtungen, für dich wie für den Agenten.
