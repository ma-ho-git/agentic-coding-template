---
title: Obsidian-Kanban Dateiformat
type: knowledge
tags: [topic/meta, stack/obsidian]
status: active
created: 2026-08-19
updated: 2026-08-19
review_after: 2026-11-19
related: ["[[ADR-0003 Kanban-Board mit Wikilink-Karten]]", "[[Konventionen der Wissensdatenbank]]", "[[00-index]]"]
---

# Obsidian-Kanban Dateiformat

## Kurz

Ein Kanban-Board des obsidian-kanban-Plugins ist eine einzelne Markdown-Datei mit fester
Struktur. Format aus dem Parser-Quellcode verifiziert, nicht aus Blogbeiträgen abgeschrieben.

## Kernpunkte

- Frontmatter-Schlüssel: `kanban-plugin: board` (ältere Versionen: `basic`)
- Lane = Überschrift zweiter Ebene: `## Lane-Name`
- Karte = Listeneintrag mit Checkbox: `- [ ] Inhalt`, erledigt `- [x] Inhalt`
- Erledigt-Lane wird durch einen Absatz `**Complete**` als erste Zeile der Lane markiert
- Archiv: waagerechte Linie `***`, dann `## Archive`
- Einstellungen am Dateiende in einem `%% kanban:settings`-Kommentarblock mit JSON-Codeblock
- Karten dürfen beliebiges Markdown enthalten, also auch `[[Wikilinks]]`

## Beispiel

```markdown
---

kanban-plugin: board

---

## Ready

- [ ] [[T-0042 Token-Refresh]]

## Done

**Complete**

- [x] [[T-0001 Repo-Setup]]

%% kanban:settings
```{"kanban-plugin":"board"}```
%%
```

## Wartungslage

- Ursprüngliches Repo `mgmeyers/obsidian-kanban` ist **archiviert**
- Fortführung: `obsidian-community/obsidian-kanban`
- Der ursprüngliche Autor sucht seit Januar 2026 Maintainer
- Risiko gering: das Board bleibt auch ohne Plugin normales, lesbares Markdown

## Quellen

- `src/parsers/formats/list.ts` in https://github.com/obsidian-community/obsidian-kanban — abgerufen 2026-08-19
- https://github.com/obsidian-community/obsidian-kanban/blob/main/MAINTAINERS.md — abgerufen 2026-08-19
