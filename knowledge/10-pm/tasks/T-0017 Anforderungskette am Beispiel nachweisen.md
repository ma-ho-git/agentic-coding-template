---
id: T-0017
title: Anforderungskette am Beispiel nachweisen
type: task
implements: ["[[REQ-0017 Anforderungserhebung vor der Entwicklung]]"]
status: done
priority: mittel
agent: claude-code
owner: claude-code
created: 2026-08-19
started: 2026-08-20
finished: 2026-08-20
tags: [topic/requirements, topic/meta]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0009 Beispielprojekt als Smoke-Test]]"]
---

# T-0017 Anforderungskette am Beispiel nachweisen

## Ziel

Die Kette Anforderung → Task → Test → Code ist an einem echten Fall durchlaufen, nicht nur
beschrieben — und das Template wendet sie auf sich selbst an.

## Akzeptanzkriterien

- [x] `examples/slugify/` bekommt vorgelagerte Anforderungen: mindestens eine funktionale
      und eine Qualitätsanforderung, beide prüfbar formuliert
- [x] `examples/slugify/README.md` zeigt den vollständigen Weg von der Anforderung bis zum
      Code, nicht erst ab dem Test
- [x] Eine Anforderungsänderung wird durchgespielt und mit `/req-change` nachgezogen —
      analog zum bestehenden `/contract-sync`-Nachweis
- [x] Das Template selbst hat `knowledge/05-requirements/` gefüllt: Vision, Stakeholder und
      die Anforderungen, aus denen dieses Template entstanden ist
- [x] Bestehende Tasks bekommen rückwirkend ihren `implements:`-Bezug, soweit sinnvoll;
      reine Infrastrukturaufgaben werden als solche gekennzeichnet
- [x] `tools/check_traceability.py` meldet für den gesamten Vault 0 Fehler

## Kontext

- [[ADR-0005 Anforderungen als Pflicht vor dem Code]]
- [[T-0009 Beispielprojekt als Smoke-Test]] — dieselbe Rolle, eine Ebene höher

## Agent

`claude-code` — Beispielcode, Vault-Pflege, Prüflauf.

## Abhängigkeiten

- [[T-0013 Skills für die Anforderungserhebung]]
- [[T-0014 Rückverfolgbarkeit maschinell prüfen]]
- [[T-0015 Bestehenden Arbeitszyklus anpassen]]

## Notizen

- Selbstanwendung ist der eigentliche Test: wenn das Template seine eigenen Anforderungen
  nicht sauber aufschreiben kann, taugt das Format nicht.
- Die Vision für das Template steht bereits sinngemäß in der Aufgabenstellung des Nutzers —
  daraus ableiten, nicht neu erfinden.

- **2026-08-20 umgesetzt.**
- Das Template hat jetzt **18 eigene Anforderungen**, abgeleitet aus der Projektvorgabe vom
  2026-08-19 — nicht erfunden. Jede nennt `quelle`, Begründung und prüfbare Abnahme.
  Alle sechs Rahmenkategorien belegt, keine leer, keine mit Alibi-Begründung.
- 15 der 18 Aufgaben rückwirkend verlinkt, 26 Verweise in beide Richtungen.
  Nur noch drei bleiben Infrastruktur: T-0008 (GitHub-Zugriff), T-0011 (Fehlerbehebung im
  Werkzeug) und — nach dem Fund unten — keine weitere. Die vorläufigen
  Infrastruktur-Marken aus T-0014 sind damit ersetzt.
- Gegenprobe gemacht: einen Rückverweis entfernt → `check_traceability.py` meldet den
  einseitigen Verweis. Die 0-Fehler-Meldung ist also echt, nicht strukturell.
- **`/req-validate` fand zwei echte Fehler in meiner eigenen Ableitung:**
  1. *Konsistenz:* Die Abnahme von REQ-0001 behauptete, `/task-next` könne nach dem
     Bootstrap sofort eine Aufgabe aufnehmen. Mit dem Startgate aus REQ-0017 verweigert
     `/task-next` das aber. Die Abnahme war durch die eigene Regel falsifiziert →
     umformuliert und ausdrücklich gegen REQ-0017 abgegrenzt.
  2. *Vollständigkeit:* Das Vision-Erfolgskriterium „das Template hält seine eigenen
     Vorgaben ein" hatte keine Anforderung. → REQ-0018 ergänzt, T-0007 von Infrastruktur
     auf diesen Bezug umgestellt.
- `constraints.md` und `risks.md` standen noch als Platzhalter da, während die Freigabe
  „Rahmen vollständig geprüft" behauptet hätte. Beide gefüllt.
- Beispiel: `examples/slugify/requirements/` mit zwei Anforderungen; die README zeigt jetzt
  die Kette **ab der Anforderung**, nicht erst ab dem Test, und erklärt den
  Höhenunterschied zwischen `/req-change` und `/contract-sync`.
- **Offen und bewusst so:** `baseline_status` steht auf `entwurf`, alle Anforderungen auf
  `status: entwurf`. Nur der Mensch öffnet das Gate — der Agent legt vor.
