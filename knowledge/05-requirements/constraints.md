---
title: Randbedingungen
aliases: ["Randbedingungen", "constraints"]
type: knowledge
tags: [topic/requirements]
status: active
created: 2026-08-19
updated: 2026-08-20
review_after: 2026-11-20
related: ["[[Rahmen und Startgate]]", "[[Projektvision]]", "[[00-index]]"]
---

# Randbedingungen

<!-- template-placeholder -->
> **Für ein eigenes Projekt:** Inhalt ersetzen. Was hier steht, sind die Randbedingungen
> **dieses Templates** und zugleich ein ausgefülltes Beispiel.

## Kurz

Vorgaben, die **nicht verhandelbar** sind und den Lösungsraum von außen beschneiden.
Unterschied zur Anforderung: eine Anforderung sagt, was das System leisten soll; eine
Randbedingung sagt, was ohnehin feststeht.

## Technisch

- Zielumgebung ist **Claude Code**. Regeln, Skills und Hooks liegen im Format, das Claude
  Code lädt (`.claude/`), und sind nicht auf andere Coding-Agenten übertragbar geprüft.
- **Claude Cowork liest die Repo-Konfiguration nicht.** Alles, was dort gelten soll, muss
  über `cowork/` separat zugestellt werden — siehe
  [[Cowork liest die Repo-Konfiguration nicht]].
- Werkzeuge laufen mit **Python 3 aus der Standardbibliothek**, ohne Laufzeitabhängigkeiten.
  Ein Template, dessen Prüfungen erst nach einer Installation laufen, prüft beim Erstlauf gar nichts.
- Die Wissensdatenbank ist **reines Markdown** und bleibt ohne Obsidian und ohne Plugin
  lesbar.

## Organisatorisch

- Ein Mensch mit ein bis zwei Agenten. Keine Team-, Rollen- oder Freigabeprozesse.
- Entwicklung erfolgt **iterativ gemeinsam mit dem Auftraggeber**, nicht als Auftragsarbeit
  am Stück.
- Agenten mergen nicht selbst; Review und Merge bleiben beim Menschen.

## Rechtlich

- Öffentliches GitHub-Repository, daher muss die Lizenz vor Veröffentlichung stehen.
- Eingesetzte Bausteine müssen mit einer permissiven Lizenz vereinbar sein.
- Das Kanban-Plugin ist GPL-3.0 — es wird **nicht** mitgeliefert, sondern nur sein
  Dateiformat genutzt. Damit entsteht keine Lizenzbindung.

## Was daraus folgt

- Keine Laufzeitabhängigkeiten in den Prüfskripten, auch wenn eine Bibliothek bequemer wäre.
- Kein Plugin-Code im Repository.
- Keine Konstruktion, die zwingend Obsidian voraussetzt.
- Keine Automatisierung, die ohne menschliche Freigabe merged oder veröffentlicht.
