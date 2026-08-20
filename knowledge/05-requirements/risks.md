---
title: Risiken
aliases: ["Risiken", "risks"]
type: knowledge
tags: [topic/requirements, topic/meta]
status: active
created: 2026-08-19
updated: 2026-08-20
review_after: 2026-11-20
related: ["[[Rahmen und Startgate]]", "[[Projektvision]]", "[[00-index]]"]
---

# Risiken

<!-- template-placeholder -->
> **Für ein eigenes Projekt:** Register leeren und mit den eigenen Risiken füllen.

## Kurz

Was das Projekt zum Scheitern bringen kann, und was dagegen läuft. Bewusst schlank —
Sommervilles Kapitel 22 in der Fassung, die für ein Vibe-Coding-Projekt trägt.
Ein eingetretenes Risiko wandert nach `knowledge/30-troubleshooting/`.

## Register

| Risiko | Wahrsch. | Auswirkung | Gegenmaßnahme | Status |
| --- | --- | --- | --- | --- |
| Regeln werden formal erfüllt, aber sinnentleert (Anforderung pro forma verlinkt, Infrastruktur-Ausnahme als Schlupfloch) | mittel | hoch | `/task-new` verbietet ausdrücklich, die Ausnahme zum Entsperren zu nutzen; Begründungspflicht macht Missbrauch sichtbar | offen |
| Zu viele Hinweise erzeugen Rauschen; Warnungen werden ignoriert | mittel | hoch | Grenzwerte auf das Geforderte zurückgeführt, Zugaben markiert (siehe [[T-0018 Grenzwerte auf die Projektvorgabe zurückführen]]) | gemindert |
| Obsidian-Kanban-Plugin bleibt unmaintained, Format bricht | niedrig | niedrig | Board ist reines Markdown; kein Code hängt am Plugin | akzeptiert |
| Claude Code ändert Hook-Events oder Konfigurationsformat | mittel | hoch | Umgebungs-Manifest mit Prüfdatum; `/bootstrap` erzwingt die Nachprüfung ab 30 Tagen | gemindert |
| Anforderungen und Code laufen auseinander | mittel | mittel | `check_traceability.py` in der CI, `/req-change` als vorgesehener Weg | gemindert |
| Wissen bleibt im Sitzungsverlauf statt im Vault | mittel | mittel | Auslöserliste in `knowledge-base.md`, Fortschrittslog als Pflicht der Definition of Done | gemindert |
| Der Rahmen wird zu früh freigegeben, Sicherheits- oder Rechtsvorgabe taucht spät auf | niedrig | hoch | Startgate verlangt je Kategorie Beleg oder begründete Nichtanwendbarkeit; nur der Mensch gibt frei | gemindert |

## Eingetretene Risiken

- [[Git-Proxy verweigert Push - Repo nicht in der Session freigegeben]] — Zugriff war beim
  ersten Auslieferungsversuch nicht freigegeben
- [[SessionStart meldet BOOTSTRAP REQUIRED trotz aktuellem Manifest]] — eine Prüfung, die
  wegen eines Formatfehlers nie griff
- [[matches_any() exemption trifft falsche Pfade]] — eine Ausnahmeregel, die zu viel durchließ
