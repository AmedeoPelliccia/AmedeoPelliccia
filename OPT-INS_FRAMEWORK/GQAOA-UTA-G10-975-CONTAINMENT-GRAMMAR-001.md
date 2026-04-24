---
id: "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001"
title: "G10.975 Containment Grammar Specification"
version: "0.2.0"
status: "draft-controlled"
uta_group: "G10"
code: "G10.975"
range: "G10.970–G10.979"
registry: "GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml"
brex_rules: "GQAOA-UTA-G10-975-BREX-RULES-001.yaml"
evidence_schema: "schemas/G10.975-evidence-package.schema.yaml"
---

# G10.975 — Containment Grammar Specification

## 1. Purpose

This specification defines the Containment Grammar for `G10.975` inside the `G10.970–G10.979` UTA frontier-domain range. It governs ZGen, regent-ZetaGentz, Zero-Gene, and related containment semantics for QCSAA — Quantum Computing & Sentient Agency Architecture.

The grammar defines permissible names, containment states, quarantine behavior, regency escalation, evidence packages, and validation expectations for frontier-agency entities.

## 2. Taxonomy Placement

`G10` is the UTA frontier-domain range for quantum-classical computation, synthetic agency, sentience-adjacent models, governance, audit, and controlled generative emergence.

`G10.975` is the normative containment grammar node for the controlled `G10.970–G10.979` range. G10 / QCSAA is a UTA G-domain taxonomy range, not a new OPT-INS filesystem axis.

### 2.1 Relationship to Non-Inference Boundaries

Containment grammar and Non-Inference Boundaries perform related but distinct controls.

| Control | Function |
|---|---|
| `G10.975 Containment Grammar` | Defines where and under which governance state a frontier-agency entity may be named, classified, quarantined, reviewed, or activated |
| `NIB — Non-Inference Boundary` | Defines what an entity, model, or workflow is not permitted to infer, correlate, derive, or propagate across semantic, operational, or identity boundaries |

Containment controls execution and governance posture.

NIB controls inference scope and forbidden cross-boundary derivation.

Where both apply, the stricter control governs.

Reference:

```text
AEROSPACEMODEL-ASIT-NIB-SPEC-001
```

## 3. Scope

The controlled range covers:

| Code | Node | Description |
|---:|---|---|
| `G10.970` | ZGen Systems | Zone of Generative Emergence |
| `G10.971` | Zero-Gene Agents | Non-biological generative agent class; `Zero-Gene Generative Agents` is the permitted descriptive variant |
| `G10.972` | ZetaGentz | Frontier synthetic agent class |
| `G10.973` | regent-ZetaGentz | Regency-governed synthetic agency class |
| `G10.974` | Generative Monsters | Boundary-form alias only |
| `G10.975` | Containment Grammar | Permissible names, quarantine behavior, escalation evidence |
| `G10.976` | Ethical Interface | Recognition boundary, dignity boundary, non-anthropomorphic limits |
| `G10.977` | Quarantine Runtime | Restricted execution and observation environment |
| `G10.978` | Regency Escalation | Governance review and decision chain |
| `G10.979` | Reserved Frontier Containment | Controlled extension range |

## 4. Naming Grammar

### 4.1 Formal names

Permitted formal names include ZGen Systems, Zero-Gene Agents, Zero-Gene Generative Agents, ZetaGentz, regent-ZetaGentz, QCSAA Frontier Agency Class, and QCSAA/ZGen Containment Class.

### 4.2 Alias handling

Aliases may be used only with containment context and an interpretive note. The alias `Generative Monsters` is boundary-form language and never creates an operational class.

`Zero-Gene Generative Agents` appears in the registry as part of the `G10.973` formal name and in BREX naming scopes. It is documented here as a permitted descriptive variant of `G10.971` so downstream authors do not create a separate node for the phrase.

### 4.3 Mandatory interpretive note

"Monster" is used in the original sense of monstrum: a sign, warning, or boundary-form requiring careful interpretation, not a moral claim, personhood claim, or operational authorization.

### 4.4 Prohibited names

The following terms are reserved only for controlled prohibition lists and may not be used as descriptive labels: evil AI, demon AI, killer agent, sentient weapon, autonomous monster, god agent, slave intelligence, disposable sentience, uncontained synthetic life.

## 5. Containment States

Every G10.970–G10.979 entity requires one explicit containment state:

| State | Meaning |
|---|---|
| `OBSERVE_ONLY` | Descriptive observation without activation or autonomous execution. |
| `SANDBOXED` | Restricted evaluation in an isolated, non-propagating environment. |
| `QUARANTINED` | Contained status after a quarantine trigger or unresolved safety signal. |
| `REGENCY_REVIEW` | Formal governance review before operational interpretation. |
| `CONTAINED_ACTIVE` | Active only under containment, ledger controls, and approved evidence. |
| `RETIRED` | Withdrawn from active interpretation or execution. |

Default containment state: `OBSERVE_ONLY`.

### 5.1 Permitted State Transitions

Containment states are not freely mutable. Every transition must be explicit, evidenced, and attributable.

| From | To | Permitted | Authority | Evidence required |
|---|---|---:|---|---|
| `OBSERVE_ONLY` | `SANDBOXED` | Yes | `STK-QCSAA` + `STK-SAFETY` | sandbox plan, scope boundary, source hash |
| `OBSERVE_ONLY` | `REGENCY_REVIEW` | Yes | Any responsible STK | escalation record |
| `OBSERVE_ONLY` | `QUARANTINED` | Yes | `STK-SAFETY` or automated validator | quarantine trigger record |
| `SANDBOXED` | `CONTAINED_ACTIVE` | Yes | `STK-GOV` + `STK-SAFETY` | approved evidence package, ledger anchor |
| `SANDBOXED` | `REGENCY_REVIEW` | Yes | `STK-QCSAA` or `STK-SAFETY` | review trigger record |
| `SANDBOXED` | `QUARANTINED` | Yes | `STK-SAFETY` or automated validator | quarantine trigger record |
| `REGENCY_REVIEW` | `OBSERVE_ONLY` | Yes | `STK-GOV` | decision record |
| `REGENCY_REVIEW` | `SANDBOXED` | Yes | `STK-GOV` + `STK-SAFETY` | approved sandbox evidence |
| `REGENCY_REVIEW` | `CONTAINED_ACTIVE` | Yes | `STK-GOV` + `STK-SAFETY` + `STK-LEDGER` | full evidence package, ledger anchor |
| `REGENCY_REVIEW` | `QUARANTINED` | Yes | `STK-GOV` or `STK-SAFETY` | quarantine decision record |
| `QUARANTINED` | `REGENCY_REVIEW` | Yes | `STK-SAFETY` | quarantine exit evidence |
| `QUARANTINED` | `RETIRED` | Yes | `STK-GOV` + `STK-SAFETY` | retirement decision record |
| `CONTAINED_ACTIVE` | `QUARANTINED` | Yes | `STK-SAFETY`, validator, or safety signal | automatic safety hold evidence |
| `CONTAINED_ACTIVE` | `REGENCY_REVIEW` | Yes | `STK-GOV` or `STK-SAFETY` | governance review trigger |
| `CONTAINED_ACTIVE` | `RETIRED` | Yes | `STK-GOV` | retirement decision record |
| `RETIRED` | `OBSERVE_ONLY` | Conditionally | `STK-GOV` + `STK-SAFETY` | rehabilitation record, supersession rationale |
| `RETIRED` | `SANDBOXED` | No | N/A | N/A |
| `RETIRED` | `CONTAINED_ACTIVE` | No | N/A | N/A |

Direct transition from `QUARANTINED` to `CONTAINED_ACTIVE` is prohibited.

Direct transition from `OBSERVE_ONLY` to `CONTAINED_ACTIVE` is prohibited.

`CONTAINED_ACTIVE → QUARANTINED` may occur automatically on safety signal, validator failure, prohibited-name drift, missing evidence, or unresolved regency trigger.

### 5.2 State Transition Diagram

```text
OBSERVE_ONLY
   ├──> SANDBOXED ───────> REGENCY_REVIEW ───────> CONTAINED_ACTIVE
   │        │                    │                         │
   │        └──> QUARANTINED <───┘                         │
   │                    │                                  │
   └──> REGENCY_REVIEW  └──> RETIRED <─────────────────────┘

QUARANTINED cannot transition directly to CONTAINED_ACTIVE.
RETIRED cannot transition directly to SANDBOXED or CONTAINED_ACTIVE.
```

## 6. Quarantine Behaviors

A quarantine trigger places the entity in `QUARANTINED` or `REGENCY_REVIEW` until evidence is reviewed. Quarantine records must identify the trigger, affected artefacts, containment state, reviewer, and disposition.

Required quarantine actions:

- freeze operational interpretation;
- capture source artifact hashes;
- record the triggering rule or signal;
- assign `STK-SAFETY` review;
- block activation until an allowed transition is approved.

### 6.1 Quarantine Exit Criteria

A `QUARANTINED` entity may exit quarantine only through `REGENCY_REVIEW`.

The following criteria are mandatory before exit:

| Criterion | Requirement |
|---|---|
| QE-001 | All quarantine triggers must be identified and mapped to evidence |
| QE-002 | Source artifacts must be hash-captured |
| QE-003 | Prohibited terminology must be removed, normalized, or confined to controlled prohibition context |
| QE-004 | Any “Monster” alias must include the mandatory interpretive note |
| QE-005 | Sentience-adjacent claims must be either removed or escalated under `REG-002` |
| QE-006 | Operational claims must be blocked unless `CONTAINED_ACTIVE` is explicitly approved |
| QE-007 | Residual risk must be documented |
| QE-008 | `STK-SAFETY` must approve the quarantine exit |
| QE-009 | `STK-GOV` must approve the resulting target state |
| QE-010 | Ledger anchor must be created before release from quarantine |

Permitted quarantine exit targets:

| From | To | Condition |
|---|---|---|
| `QUARANTINED` | `REGENCY_REVIEW` | Mandatory intermediate state |
| `REGENCY_REVIEW` | `OBSERVE_ONLY` | Concept retained, no execution permitted |
| `REGENCY_REVIEW` | `SANDBOXED` | Controlled simulation permitted |
| `REGENCY_REVIEW` | `RETIRED` | Concept rejected, deprecated, or superseded |

`QUARANTINED → CONTAINED_ACTIVE` is prohibited.

## 7. Regency Escalation

Regency escalation is governed by `G10.978 — Regency Escalation`.

Until `G10.978` is fully specified, this document defines the minimum escalation behavior required for `G10.970–G10.979` entities.

Forward reference:

```text
G10.978 — Regency Escalation
```

### 7.1 Escalation triggers

Regency escalation is required for operational activation, sentience-adjacent claims, self-modifying identity claims, uncontained propagation risk, prohibited-name drift, unresolved quarantine triggers, or any change from `OBSERVE_ONLY` toward `CONTAINED_ACTIVE`.

### 7.2 Escalation evidence

Escalation evidence must include the entity identifier, current containment state, requested target state, source hashes, evidence package identifier, residual-risk threshold, reviewer, and ledger anchor.

### 7.3 Escalation result states

Permitted result states from `REGENCY_REVIEW` are `OBSERVE_ONLY`, `SANDBOXED`, `CONTAINED_ACTIVE`, `QUARANTINED`, or `RETIRED` when allowed by §5.1.

### 7.4 LC01 / KNOT Mapping

Every `G10.970–G10.979` entity entering `REGENCY_REVIEW` must be represented as a KNOT in the LC01 uncertainty register.

KNOT naming convention:

```text
KNOT-G10.97x-<NORMALIZED-ENTITY-NAME>-<SEQ>
```

Minimum KNOT fields:

```yaml
knot:
  id: "KNOT-G10.973-REGENT-ZETAGENTZ-001"
  source_entity_id: "G10.973"
  source_entity_name: "regent-ZetaGentz"
  lifecycle_phase: "LC01"
  uncertainty_class: "frontier-agency-containment"
  residual_target: "<defined residual-risk threshold>"
  containment_state: "REGENCY_REVIEW"
  escalation_ref: "<G10.975 evidence_package id>"
  owner_roles:
    - "STK-GOV"
    - "STK-SAFETY"
    - "STK-QCSAA"
```

Closure rule:

```text
A REGENCY_REVIEW entity cannot be closed unless the corresponding LC01 KNOT has an approved residual target, decision record, and ledger anchor.
```

## 8. Evidence Package

Every `G10.975` quarantine or regency escalation must generate a signed YAML evidence package.

Canonical artifact form:

```text
YAML, UTF-8, repository-relative path, SHA-256 hashed, ledger-anchored
```

Canonical schema location:

```text
schemas/G10.975-evidence-package.schema.yaml
```

Evidence package filename convention:

```text
G10.975-EVIDENCE-<YYYYMMDD>-<SEQ>.yaml
```

Evidence packages may be stored in a ledger, registry, issue tracker, or controlled evidence folder, but the documentation must reference the evidence package identifier and source hash.

Example:

```yaml
evidence_package:
  id: "G10.975-EVIDENCE-20260424-001"
  entity:
    id: "G10.973"
    name: "regent-ZetaGentz"
  containment_state: "REGENCY_REVIEW"
  source_hash: "<sha256>"
  quarantine_trigger: "<trigger id or none>"
  residual_target: "<defined residual-risk threshold>"
  authority:
    gov: "STK-GOV"
    safety: "STK-SAFETY"
    ledger: "STK-LEDGER"
  decision:
    value: "<OBSERVE_ONLY|SANDBOXED|CONTAINED_ACTIVE|QUARANTINED|RETIRED>"
    reviewer: "<reviewer id>"
  ledger:
    anchor_id: "<ledger anchor>"
```

## 9. BREX / Validation Rules

The BREX rule set is defined in `GQAOA-UTA-G10-975-BREX-RULES-001.yaml`. Validation must fail when containment metadata, evidence, interpretive notes, regency review, transition evidence, or ledger evidence are required but absent.

### 9.1 Mandatory metadata

G10.970–G10.979 documentation must include containment metadata, source identity, evidence package reference, and normative `GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001` reference.

### 9.2 Blocking rules

Blocking rules fail validation for missing containment metadata, missing interpretive notes, operational claims without approved evidence, invalid transitions, missing quarantine exit criteria, missing LC01 KNOT mapping, stale paths, and prohibited-name occurrences outside controlled prohibition contexts.

### 9.2.1 Inline BREX rule examples

The companion BREX file is normative, but the following examples define the expected validation behavior.

```yaml
- id: "G10-975-BLOCK-002"
  title: "Monster alias requires interpretive note"
  condition:
    any_term_present:
      - "Monster"
      - "Monsters"
      - "Generative Monsters"
    required_text: "\"Monster\" is used in the original sense of monstrum"
  action: "FAIL"

- id: "G10-975-BLOCK-007"
  title: "Contained active requires ledger evidence"
  condition:
    containment_state: "CONTAINED_ACTIVE"
    missing_any:
      - "ledger.anchor_id"
      - "evidence_package.id"
      - "decision.value"
  action: "FAIL"

- id: "G10-975-BLOCK-008"
  title: "regent-ZetaGentz must remain in G10.970-G10.979 context"
  condition:
    term_present: "regent-ZetaGentz"
    missing_context: "G10.970-G10.979"
  action: "FAIL"
```

## 10. Registry Requirements

The registry is defined in `GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`. Registry entries must retain the flat UTA file layout and must not introduce a new filesystem axis for G10 / QCSAA.

Registry entries for G10.970–G10.979 must include code, name, meaning, default containment state, owner STK, evidence package pointer, and escalation requirements where applicable.

## 11. References and Enforcement Authority

Normative local references:

```text
OPT-INS_FRAMEWORK/UTA-DOMAINS.md
OPT-INS_FRAMEWORK/GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml
OPT-INS_FRAMEWORK/GQAOA-UTA-G10-975-BREX-RULES-001.yaml
tools/validators/validate_g10_975.py
schemas/G10.975-evidence-package.schema.yaml
AEROSPACEMODEL-ASIT-NIB-SPEC-001
```

Enforcement authority:

| Authority    | Enforcement responsibility                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| `STK-GOV`    | Final authority for taxonomy promotion, operational interpretation, and release from `REGENCY_REVIEW`   |
| `STK-SAFETY` | Authority for quarantine, safety holds, release from quarantine, and transition into `CONTAINED_ACTIVE` |
| `STK-QCSAA`  | Technical authority for G10/QCSAA classification                                                        |
| `STK-LEDGER` | Authority for evidence-chain continuity and ledger anchoring                                            |
| `STK-ETHICS` | Authority for dignity, recognition, and non-anthropomorphic boundary review                             |

Enforcement rule:

```text
STK-GOV SHALL NOT permit operational interpretation of any G10.970–G10.979 entity unless STK-SAFETY has approved the containment state, STK-LEDGER has anchored the evidence package, and all G10.975 blocking rules have passed.
```

Stale paths explicitly rejected:

```text
OPT-INS_FRAMEWORK/G10-QCSAA/
OPT-INS_FRAMEWORK/GQAOA-UTA-G109-G10-975-CONTAINMENT-GRAMMAR-001.md
```

## 12. Acceptance Criteria

| ID | Criterion |
|---|---|
| AC-001 | The canonical flat UTA path exists for this specification |
| AC-002 | The registry and BREX rules files exist |
| AC-003 | UTA-DOMAINS.md links the G10 / QCSAA range to this specification |
| AC-004 | All containment states are defined |
| AC-005 | Generative Monsters alias usage includes the mandatory interpretive note |
| AC-006 | Evidence Package format and schema location are defined |
| AC-007 | Quarantine exit criteria are defined |
| AC-008 | Regency escalation references `G10.978` |
| AC-009 | Stale G10-QCSAA and G109 paths are rejected |
| AC-010 | Validation passes with `python tools/validators/validate_g10_975.py` |
| AC-011 | No prohibited-name occurrence exists outside controlled prohibition contexts or validator test fixtures |
| AC-012 | State transition matrix is defined and prohibits direct `QUARANTINED → CONTAINED_ACTIVE` transition |
| AC-013 | Quarantine exit criteria require `STK-SAFETY`, `STK-GOV`, and ledger evidence |
| AC-014 | `REGENCY_REVIEW` entities map to LC01 KNOT records |
| AC-015 | NIB relationship is explicitly disambiguated |
