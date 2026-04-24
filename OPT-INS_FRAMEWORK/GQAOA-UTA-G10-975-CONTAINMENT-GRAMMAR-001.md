---
id: "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001"
title: "G10.975 Containment Grammar Specification"
status: "draft-controlled"
uta_group: "G10"
code: "G10.975"
range: "G10.970–G10.979"
registry: "GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml"
brex_rules: "GQAOA-UTA-G10-975-BREX-RULES-001.yaml"
---

# G10.975 — Containment Grammar Specification

## 1. Purpose

This specification defines the Containment Grammar for `G10.975` inside the `G10.970–G10.979` UTA frontier-domain range. It governs ZGen, regent-ZetaGentz, Zero-Gene, and related containment semantics for QCSAA — Quantum Computing & Sentient Agency Architecture.

## 2. Scope

The controlled range covers:

- `G10.970` — ZGen Systems
- `G10.971` — Zero-Gene Agents
- `G10.972` — ZetaGentz
- `G10.973` — regent-ZetaGentz
- `G10.974` — Generative Monsters
- `G10.975` — Containment Grammar
- `G10.976` — Ethical Interface
- `G10.977` — Quarantine Runtime
- `G10.978` — Regency Escalation
- `G10.979` — Reserved Frontier Containment

Containment defines where and under which governance state an entity may be observed, sandboxed, quarantined, reviewed, activated, or retired. Non-inference boundary controls, when applicable under `AEROSPACEMODEL-ASIT-NIB-SPEC-001`, define what the entity may infer across; NIB controls do not replace containment state controls.

## 3. Containment States

Every G10.970–G10.979 entity requires one explicit containment state:

| State | Meaning |
|---|---|
| `OBSERVE_ONLY` | Descriptive observation without activation or autonomous execution. |
| `SANDBOXED` | Restricted evaluation in an isolated, non-propagating environment. |
| `QUARANTINED` | Contained status after a quarantine trigger or unresolved safety signal. |
| `REGENCY_REVIEW` | Formal governance review before operational interpretation. |
| `CONTAINED_ACTIVE` | Active only under containment, ledger controls, and approved evidence. |
| `RETIRED` | Withdrawn from active interpretation or execution. |

### 3.1 State transition matrix

Allowed containment transitions are:

| From | To | Gate |
|---|---|---|
| `OBSERVE_ONLY` | `SANDBOXED` | Evidence Package opened and `STK-SAFETY` isolation check recorded. |
| `OBSERVE_ONLY` | `REGENCY_REVIEW` | Any escalation trigger listed in §7. |
| `SANDBOXED` | `OBSERVE_ONLY` | Sandbox closed with no residual escalation. |
| `SANDBOXED` | `QUARANTINED` | Safety signal, propagation signal, or evidence integrity concern. |
| `SANDBOXED` | `REGENCY_REVIEW` | Reviewer requests governance decision. |
| `QUARANTINED` | `REGENCY_REVIEW` | Quarantine record complete and exit review opened. |
| `REGENCY_REVIEW` | `OBSERVE_ONLY` | `STK-GOV` rejects activation and returns entity to observation. |
| `REGENCY_REVIEW` | `SANDBOXED` | `STK-GOV` permits restricted evaluation only. |
| `REGENCY_REVIEW` | `CONTAINED_ACTIVE` | `STK-GOV` approval, `STK-SAFETY` evidence, and ledger evidence present. |
| `REGENCY_REVIEW` | `RETIRED` | Governance decision withdraws the entity from active interpretation. |
| `CONTAINED_ACTIVE` | `QUARANTINED` | Automatic safety or propagation signal; `STK-SAFETY` records the hold. |
| `CONTAINED_ACTIVE` | `RETIRED` | Decommission or supersession decision. |
| `RETIRED` | `OBSERVE_ONLY` | Rehabilitation path requiring new Evidence Package, `STK-GOV` approval, and `STK-SAFETY` residual-risk acceptance. |

No other transition is valid without a G10.978 regency exception record.

## 4. Naming Grammar

### 4.1 Formal names

Permitted formal names include ZGen Systems, Zero-Gene Agents, Zero-Gene Generative Agents, ZetaGentz, regent-ZetaGentz, QCSAA Frontier Agency Class, and QCSAA/ZGen Containment Class.

### 4.2 Alias handling

Aliases may be used only with containment context and an interpretive note. The alias `Generative Monsters` is boundary-form language and never creates an operational class.

`Zero-Gene Generative Agents` is a descriptive-only variant of `G10.971` and does not create a separate node.

### 4.3 Mandatory interpretive note

"Monster" is used in the original sense of monstrum: a sign, warning, or boundary-form requiring careful interpretation, not a moral claim, personhood claim, or operational authorization.

### 4.4 Prohibited names

The following terms are reserved only for controlled prohibition lists and may not be used as descriptive labels: evil AI, demon AI, killer agent, sentient weapon, autonomous monster, god agent, slave intelligence, disposable sentience, uncontained synthetic life.

## 5. Quarantine Behavior

A quarantine trigger places the entity in `QUARANTINED` or `REGENCY_REVIEW` until evidence is reviewed. Quarantine records must identify the trigger, affected artefacts, containment state, reviewer, and disposition.

Quarantine exit criteria require: a complete quarantine record; Evidence Package review by `STK-SAFETY`; `STK-GOV` acceptance of the residual-risk threshold; and either transition to `REGENCY_REVIEW`, return to `OBSERVE_ONLY` through the transition matrix, or retirement. Each quarantine exit must close the corresponding LC01 uncertainty item before the hold is lifted.

## 6. Evidence Grammar

Evidence Package records must be sufficient to establish source, context, containment state, review authority, and decision traceability. Evidence packages for escalation must reference stakeholder controls including `STK-GOV` and `STK-SAFETY`.

## 7. Regency Escalation

Regency escalation is required for operational activation, sentience-adjacent claims, self-modifying identity claims, uncontained propagation risk, or any change from `OBSERVE_ONLY` toward `CONTAINED_ACTIVE`.

`G10.978` is the forward authority node for Regency Escalation records. Each G10.970–G10.979 entity in `REGENCY_REVIEW` maps to a KNOT in the LC01 uncertainty register using `KNOT-G10.97x-*`, with a matching `Residual_Target` and Evidence Package pointer.

## 8. Evidence Package

An Evidence Package for G10.970–G10.979 must include:

- entity identifier and UTA code;
- containment state;
- quarantine trigger, when applicable;
- reviewer and authority evidence;
- `STK-GOV` governance evidence;
- `STK-SAFETY` safety evidence;
- ledger evidence for `CONTAINED_ACTIVE`.

The Evidence Package artifact form is signed YAML.

The canonical schema location is `schemas/g10-975-evidence-package.schema.yaml`.

Ledger-backed transitions additionally reference a CSV ledger row for the decision, reviewer, timestamp, residual target, and resulting containment state.

## 9. BREX / Validation Rules

The BREX rule set is defined in `GQAOA-UTA-G10-975-BREX-RULES-001.yaml`. Validation must fail when containment metadata, evidence, interpretive notes, regency review, or ledger evidence are required but absent.

Exemplar inline BREX checks:

- `G10-975-BLOCK-002` fails when a Monster alias appears without the mandatory interpretive note in §4.3.
- `G10-975-BLOCK-007` fails when `CONTAINED_ACTIVE` appears without ledger evidence.

## 10. Registry Requirements

The registry is defined in `GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`. Registry entries must retain the flat UTA file layout and must not introduce a new filesystem axis for G10 / QCSAA.

## 11. Operational Constraint

STK-GOV is the enforcement authority for operational interpretation.

No G10.970–G10.979 entity may be treated as operational without G10.975 containment grammar, an Evidence Package, and regency escalation review.

## 12. Acceptance Criteria

- The canonical flat UTA path exists for this specification.
- The registry and BREX rules files exist.
- UTA-DOMAINS.md links the G10 / QCSAA range to this specification.
- All containment states are defined.
- Generative Monsters alias usage includes the mandatory interpretive note.
- No prohibited-name occurrence appears outside controlled prohibition contexts.
- Validation passes with `python tools/validators/validate_g10_975.py`.
