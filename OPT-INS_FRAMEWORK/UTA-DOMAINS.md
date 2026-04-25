---
id: "GQAOA-UTA-G10-QCSAA-REGISTRY-001"
title: "G10 / QCSAA Registry"
version: "0.2.0"
status: "draft-controlled"
uta_group: "G10"
code_range: "900-999"
name: "QCSAA"
expansion: "Quantum Computing & Sentient Agency Architecture"
normative_spec: "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001"
evidence_schema: "schemas/G10.975-evidence-package.schema.yaml"

description: >
  UTA G-domain frontier taxonomy for quantum-classical computation,
  synthetic agency, sentience-adjacent models, governance, audit,
  and controlled generative emergence.

default_controls:
  containment_state: "OBSERVE_ONLY"
  owner_stk:
    - "STK-QCSAA"
    - "STK-SAFETY"
  evidence_package_pointer: "required-on-quarantine-or-regency-escalation"
  evidence_package_filename: "G10.975-EVIDENCE-<YYYYMMDD>-<SEQ>.yaml"
  lc01_knot_required_for_regency_review: true
  direct_quarantined_to_contained_active_prohibited: true

controlled_ranges:
  "970-979":
    name: "ZGen / regent-ZetaGentz Containment Semantics"
    status: "reserved-controlled"
    normative_spec: "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001"
    normative_path: "OPT-INS_FRAMEWORK/GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md"
    default_containment_state: "OBSERVE_ONLY"
    evidence_schema: "schemas/G10.975-evidence-package.schema.yaml"

    nodes:
      "970":
        id: "G10.970"
        name: "ZGen Systems"
        meaning: "Zone of Generative Emergence"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-QCSAA"]
        evidence_package_pointer: null

      "971":
        id: "G10.971"
        name: "Zero-Gene Agents"
        permitted_descriptive_variant: "Zero-Gene Generative Agents"
        meaning: "Non-biological generative agent class"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-QCSAA"]
        evidence_package_pointer: null

      "972":
        id: "G10.972"
        name: "ZetaGentz"
        meaning: "Frontier synthetic agent class"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-QCSAA"]
        evidence_package_pointer: null

      "973":
        id: "G10.973"
        name: "regent-ZetaGentz"
        formal_name: "regent-ZetaGentz — Zero-Gene Generative Agents"
        aliases:
          - "Zero-Gene Generative Monsters"
          - "Boundary-form Generative Systems"
        meaning: "Regency-governed frontier agency class"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-QCSAA", "STK-GOV", "STK-SAFETY"]
        evidence_package_pointer: "required-for-regency-review"
        lc01_knot_required: true
        escalation_required: true

      "974":
        id: "G10.974"
        name: "Generative Monsters"
        meaning: "Boundary-form alias only"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-QCSAA", "STK-ETHICS"]
        evidence_package_pointer: null
        alias_policy: "Requires mandatory interpretive note under G10.975"

      "975":
        id: "G10.975"
        name: "Containment Grammar"
        meaning: "Permissible names, quarantine behavior, regency escalation, and evidence grammar"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-GOV", "STK-QCSAA", "STK-SAFETY"]
        evidence_package_pointer: "schemas/G10.975-evidence-package.schema.yaml"

      "976":
        id: "G10.976"
        name: "Ethical Interface"
        meaning: "Recognition boundary, dignity boundary, and non-anthropomorphic limits"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-ETHICS", "STK-GOV"]
        evidence_package_pointer: null

      "977":
        id: "G10.977"
        name: "Quarantine Runtime"
        meaning: "Restricted execution and observation environment"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-SAFETY", "STK-QCSAA"]
        evidence_package_pointer: "required-for-quarantine"

      "978":
        id: "G10.978"
        name: "Regency Escalation"
        meaning: "Governance escalation and decision evidence chain"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-GOV", "STK-SAFETY", "STK-LEDGER"]
        evidence_package_pointer: "required-for-regency-review"
        lc01_knot_required: true

      "979":
        id: "G10.979"
        name: "Reserved Frontier Containment"
        meaning: "Controlled extension range"
        containment_state: "OBSERVE_ONLY"
        owner_stk: ["STK-GOV", "STK-QCSAA"]
        evidence_package_pointer: null

mandatory_controls:
  containment_state_required: true
  state_transition_matrix_required: true
  quarantine_exit_criteria_required: true
  evidence_package_required_for_escalation: true
  evidence_schema_required: "schemas/G10.975-evidence-package.schema.yaml"
  ledger_required_for_contained_active: true
  regency_review_required_for_operational_activation: true
  lc01_knot_required_for_regency_review: true
  monster_alias_requires_interpretive_note: true
  nib_relationship_disambiguated: true

prohibited_without_review:
  - "operational activation"
  - "autonomous execution"
  - "sentience-adjacent claim"
  - "self-modifying identity"
  - "uncontained propagation"

prohibited_transitions:
  - "QUARANTINED -> CONTAINED_ACTIVE"
  - "OBSERVE_ONLY -> CONTAINED_ACTIVE"
  - "RETIRED -> SANDBOXED"
  - "RETIRED -> CONTAINED_ACTIVE"

stale_paths_rejected:
  - "OPT-INS_FRAMEWORK/G10-QCSAA/"
  - "OPT-INS_FRAMEWORK/GQAOA-UTA-G109-G10-975-CONTAINMENT-GRAMMAR-001.md"

---

# UTA Domains

## G10 / 900–999 — QCSAA

**QCSAA** — Quantum Computing & Sentient Agency Architecture

`G10` defines the UTA frontier-domain range for quantum-classical computation, synthetic agency, sentience-adjacent models, governance, audit, and controlled generative emergence.

### G10.970–G10.979 — ZGen / regent-ZetaGentz Containment Semantics

The `G10.970–G10.979` range is reserved for ZGen / regent-ZetaGentz containment semantics.

| Code | Node | Description |
|---:|---|---|
| `G10.970` | ZGen Systems | Zone of Generative Emergence |
| `G10.971` | Zero-Gene Agents | Non-biological generative agents |
| `G10.972` | ZetaGentz | Frontier synthetic agent class |
| `G10.973` | regent-ZetaGentz | Regency-governed synthetic agency class |
| `G10.974` | Generative Monsters | Boundary-form alias only |
| `G10.975` | Containment Grammar | Permissible names, quarantine behavior, escalation evidence |
| `G10.976` | Ethical Interface | Recognition boundary, dignity boundary, non-anthropomorphic limits |
| `G10.977` | Quarantine Runtime | Restricted execution and observation environment |
| `G10.978` | Regency Escalation | Governance review and decision chain |
| `G10.979` | Reserved Frontier Containment | Controlled extension range |

Normative specification:

- [G10.975 — Containment Grammar Specification](GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md)

Registry:

- [G10 / QCSAA Registry](GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml)

BREX / validation rules:

- [G10.975 BREX Rules](GQAOA-UTA-G10-975-BREX-RULES-001.yaml)

Constraint:

```text
No G10.970–G10.979 entity may be treated as operational without G10.975 containment grammar, evidence package, and regency escalation review.
```
