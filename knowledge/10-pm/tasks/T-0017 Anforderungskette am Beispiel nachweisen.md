---
id: T-0017
title: Anforderungskette am Beispiel nachweisen
type: task
status: ready
priority: mittel
agent: claude-code
owner:
created: 2026-08-19
started:
finished:
tags: [topic/requirements, topic/meta]
related: ["[[ADR-0005 Anforderungen als Pflicht vor dem Code]]", "[[T-0009 Beispielprojekt als Smoke-Test]]"]
---

# T-0017 Anforderungskette am Beispiel nachweisen

## Ziel

Die Kette Anforderung → Task → Test → Code ist an einem echten Fall durchlaufen, nicht nur
beschrieben — und das Template wendet sie auf sich selbst an.

## Akzeptanzkriterien

- [ ] `examples/slugify/` bekommt vorgelagerte Anforderungen: mindestens eine funktionale
      und eine Qualitätsanforderung, beide prüfbar formuliert
- [ ] `examples/slugify/README.md` zeigt den vollständigen Weg von der Anforderung bis zum
      Code, nicht erst ab dem Test
- [ ] Eine Anforderungsänderung wird durchgespielt und mit `/req-change` nachgezogen —
      analog zum bestehenden `/contract-sync`-Nachweis
- [ ] Das Template selbst hat `knowledge/05-requirements/` gefüllt: Vision, Stakeholder und
      die Anforderungen, aus denen dieses Template entstanden ist
- [ ] Bestehende Tasks bekommen rückwirkend ihren `implements:`-Bezug, soweit sinnvoll;
      reine Infrastrukturaufgaben werden als solche gekennzeichnet
- [ ] `tools/check_traceability.py` meldet für den gesamten Vault 0 Fehler

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
