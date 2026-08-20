---
title: Szenario
aliases: ["Szenario"]
type: knowledge
tags: [topic/requirements]
status: active
created: 2026-08-20
updated: 2026-08-20
review_after: 2027-02-20
related: ["[[Rahmen und Startgate]]", "[[Projektvision]]", "[[00-index]]"]
---

# Szenario

<!-- template-placeholder -->
> **Für ein eigenes Projekt:** diese Datei vollständig ersetzen — oder löschen, wenn kein
> Szenario aufgenommen wurde. Was hier steht, ist das Szenario **dieses Templates** und
> zugleich ein ausgefülltes Beispiel.
>
> **Sonderfall dieses Repositories:** Das Szenario wurde nachträglich aus der ursprünglichen
> Vorgabe vom 2026-08-19 und den Ergänzungen vom 2026-08-20 rekonstruiert — die Datei gab es zu dem Zeitpunkt noch nicht.
> Wörtliche Zitate sind als solche gekennzeichnet; alles Übrige ist geordnete Wiedergabe und
> vom Auftraggeber noch nicht bestätigt. Im Normalfall entsteht diese Datei **vor** der
> Erhebung, aus dem, was der Nutzer selbst erzählt.

## Wer und wann

Ein Mensch, der mit Claude Code und Claude Cowork ein Softwareprojekt anfängt — der
Auftraggeber selbst, und jeder, der die Vorlage später klont. Ausdrücklich auch Anwender
ohne Erfahrung in Softwareentwicklung.

Ausgelöst wird es beim Projektstart: klonen, `/bootstrap` aufrufen, loslegen.

## Ablauf

1. Vorlage klonen, erster Lauf prüft die eigenen Annahmen und richtet das Projekt ein.
2. Vorhaben schildern, daraus Anforderungen erheben, Rahmen vereinbaren.
3. Aufgaben auf einem Kanban-Board führen, eine nach der anderen abarbeiten.
4. Je Aufgabe: Test zuerst, dann Code, dann die betroffenen Stellen nachziehen.
5. Was dabei gelernt wurde, landet in der Wissensdatenbank statt im Gesprächsverlauf.

## Ergebnis

- Der Projektstand ist nach Sitzungsende aus dem Repository lesbar, nicht aus dem Chat.
- Zu jeder Aufgabe ist erkennbar, welche Anforderung sie erfüllt.
- Eine Regelverletzung wird abgelehnt, nicht bloß angemahnt.
- Am Ende steht ein kurzes README, das den Einstieg ermöglicht, samt geklärter Nutzungsrechte.

## Was schiefgehen kann

- Es wird sofort codiert, ohne dass festgehalten ist, was entstehen soll.
- Wissen bleibt im Sitzungsverlauf und ist beim nächsten Start verloren.
- Dasselbe Problem wird zweimal gelöst, weil die erste Lösung nirgends steht.
- Regeln stehen in Prosa und gelten nur, solange sie jemandem präsent sind.
- Mehrere Agenten arbeiten aneinander vorbei, weil ein gemeinsamer Stand fehlt.
- Ein unerfahrener Nutzer versteht das Verfahren nicht und füllt Pflichtfelder mit
  Platzhaltern — die Form bleibt, der Nutzen ist weg.

## Mengen und Häufigkeit

Zuschnitt ist ein Mensch mit ein bis zwei Agenten, nicht ein großes Team. Die Vorlage wird
je Projekt einmal geklont und dann über die Projektlaufzeit benutzt.

## Bestehende Systeme

- **Claude Code** — lädt die Repo-Konfiguration selbst
- **Claude Cowork** — liest sie **nicht**, braucht ein eigenes Einrichtungspaket
- **GitHub** — öffentliche Bereitstellung, CI
- **Obsidian** — Wissensdatenbank, Kanban-Ansicht über ein Community-Plugin; alles bleibt
  ohne Obsidian lesbares Markdown

## Was nicht passieren darf

Wörtlich aus der Vorgabe:

> „Agenten und Subagenten dürfen das durchzuführende Projekt nicht gefährden, zusätzliche
> Kosten verursachen oder andere Projekte gefährden"

> „Erstellter Code darf keine (bekannten oder offensichtlichen) Sicherheitslücken beinhalten"

Dazu: keine Geheimnisse im Repository, keine zerstörerischen Git-Operationen, kein Zugriff
außerhalb dieses Repositories.

## Offene Punkte

- Der Wortlaut dieser Rekonstruktion ist vom Auftraggeber noch nicht bestätigt.
