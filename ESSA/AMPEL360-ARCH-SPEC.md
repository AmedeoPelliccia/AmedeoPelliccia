# AMPEL360 — Aerospace Model for Product and Engineering Lifecycles (360°)

| Metadata | Value |
|----------|-------|
| **Document ID** | AMPEL360-ARCH-SPEC-v2.0 |
| **Classification** | CIVIL_PUBLIC |
| **Status** | Active Development |
| **Effective Date** | 2026-03-07 |
| **Author** | Amedeo Pelliccia — IDEALEeu Enterprise |
| **Parent** | ESSA-DOC-AMPEL360-001 ([AMPEL360.md](AMPEL360.md)) |
| **Companion YAML** | [`ampel360.yaml`](ampel360.yaml) |

---

## 1  Definition and Scope

AMPEL360 is an end-to-end aerospace lifecycle architecture that governs the design, engineering, certification, operation, and continuous digital traceability of aircraft systems and programmes. The designation "360" denotes the complete angular span of the lifecycle: a closed loop where no phase is terminal and every state produces traceable outputs that feed forward or feed back into adjacent phases.

AMPEL360 is a lifecycle state machine, a safety-first execution engine, a compliance-aware orchestration kernel, and a value-preserving circular framework. It is none of the following: a PLM tool, a documentation repository, or a certification body. These may consume AMPEL360 outputs or operate within its governance envelope, but they do not define it.

### 1.1  Mission Statement

AMPEL360 defines a safety-first, profile-adaptive aerospace lifecycle architecture governing systems from concept and requirements through certification, operation, modification, reuse, and traceable closure, preserving traceability, compliance, and value across the full asset continuum.

### 1.2  Mission-to-Material Traceability

The strongest invariant AMPEL360 enforces is unbroken traceability across the entire lifecycle:

```
Mission Intent → Requirements → Design → Build → Operate → Transfer → Recover Materials
```

Subject to two global constraints:

```
Safety ⊆ All States
Traceability preserved across ownership changes
```

No phase transition may occur without verifiable evidence that both constraints are satisfied.

---

## 2  The 360° Phase Map

The twelve phases constitute the full aerospace lifecycle loop. Each phase is a controlled state with explicit entry criteria, exit criteria, and evidence requirements.

| Phase | Scope |
|-------|-------|
| **P000** | Mission Intent / Programme Charter |
| **P010** | Requirements (Regulatory + Operational) |
| **P020** | Preliminary Design |
| **P030** | Detailed Design |
| **P040** | Analysis and Verification Models |
| **P050** | Industrialization / Tooling |
| **P060** | Production / Integration |
| **P070** | Testing and Certification |
| **P080** | Entry Into Service |
| **P090** | Operations and Fleet Management |
| **P100** | Leasing / Transfer / Portfolio Governance |
| **P110** | Mid-Life Upgrade / Retrofit |
| **P120** | Decommissioning / Recycling / Circular Recovery |

Phase P120 feeds material passports and residual digital twin archives back into P000-class programme decisions, closing the loop.

---

## 3  Structural Axes

AMPEL360 is not linear. Four orthogonal axes intersect every phase and constrain state transitions. No phase transition is valid unless all four axes are satisfied.

### 3.1  Safety Axis (H-factor)

The Safety Axis activates progression. Every state transition requires demonstration that the safety envelope is preserved or explicitly renegotiated under controlled authority. The H-factor (Human Exposure Factor) is the root variable from which risk thresholds, DAL assignments, and survivability requirements are derived.

### 3.2  Security Axis

The Security Axis protects integrity and authority. It governs access control, information classification, provenance verification, and tamper evidence across all lifecycle artifacts.

### 3.3  Economic Axis

The Economic Axis governs leasing, portfolio management, residual value preservation, and ownership transfer. It treats leasing as a first-class lifecycle state rather than external business metadata.

### 3.4  Circular Axis

The Circular Axis enforces material traceability, Digital Product Passport (DPP) compliance, recycling mandates, and end-of-life material recovery.

---

## 4  Leasing as First-Class Lifecycle State

Leasing is an embedded lifecycle state transition. The data model enforces this as a temporal graph:

```
Asset_ID
  ├── Operator_A [valid_from → valid_to]
  │     ├── config_baseline: SB_LIST_A
  │     └── regulatory_regime: EASA
  └── Operator_B [valid_from → ...]
        ├── config_baseline: SB_LIST_B
        └── regulatory_regime: FAA
```

---

## 5  Decommissioning as Structured Output

Phase P120 produces five mandatory deliverables: material recovery map, hazardous component tracking, recyclable mass index, residual digital twin archive, and compliance closure package.

---

## 6  Recycling Integration and Circular Compliance

AMPEL360 connects to DPP logic at part level. Circular compliance artifacts are produced throughout the lifecycle in SSOT folders LC03 through LC14 and assembled into the DPP closure package at P120.

---

## 7  AMPEL360-SPLIT — Human Presence Safety Ontology

### 7.1  HOB — Human On Board

Catastrophic failure probability < 10⁻⁹ per flight hour. Deterministic override authority. Fail-operational architectures. DAL A dominant.

### 7.2  NHOB — No Human On Board

Safety objective shifts from survivability to external harm minimization. Ground control authority. Autonomy tolerance calibrated to operational environment.

### 7.3  Fork Granularity

Recommended path: binary classification → multi-tiered → continuous indexing.

---

## 8  AMPEL360-DEF — Defense Profile Extension

Defence profile is implemented as a dual-layer architecture: civil safety root with defence extension on top. Mandatory extensions: ROE/Engagement Constraints, Civilian Protection Invariants, Post-Event Auditability, Classification Overlay.

---

## 9  Three-Axis Profile Constructor

### 9.1  Axis A — Operational Environment

| Value | Description |
|-------|-------------|
| `AIR` | Atmospheric flight operations |
| `SPACE` | Orbital, sub-orbital, and deep-space operations |

### 9.2  Axis B — Functional Mission

| Value | Description |
|-------|-------------|
| `PAX_TRANSPORT` | Passenger-carrying operations |
| `CARGO_ONLY` | Cargo and unmanned payload operations |

### 9.3  Axis C — Payload Classification

| Value | Description |
|-------|-------------|
| `CIVIL_PUBLIC` | No classification restrictions |
| `COMMERCIAL_SENSITIVE` | Business-confidential, limited disclosure |
| `EXPORT_CONTROLLED` | Subject to ITAR, EAR, or equivalent |
| `DEFENSE_CLASSIFIED` | Military classification regime |

### 9.4  Composite Profile Model

```json
{
  "profile_id": "AIR.PAX_TRANSPORT.CIVIL_PUBLIC.EASA-Q100",
  "axes": {
    "environment": "AIR",
    "function": "PAX_TRANSPORT",
    "payload_class": "CIVIL_PUBLIC"
  },
  "regulatory": {
    "primary": "EASA",
    "software": {
      "do178c": { "enabled": true, "dal": "A" }
    }
  }
}
```

### 9.5  Profile Resolution Logic

1. **Select base kernel** — H-pipeline gates, security integrity checks, interpret/confirm/activate/publish state machine.
2. **Apply axis packs** — ENV → FUNC → PAYLOAD (structural order).
3. **Apply named regulatory overlay** — most restrictive wins.

### 9.7  Reference Profiles

- **Q100**: `AIR.PAX_TRANSPORT.CIVIL_PUBLIC.EASA-Q100(+DO-178C-DAL-A)`
- **Q10**: `SPACE.CARGO_ONLY.COMMERCIAL_SENSITIVE.SPACE-Q10`
- **Defense**: `SPACE.CARGO_ONLY.DEFENSE_CLASSIFIED.SPACE-Q10-DEF`

---

## 10  Graph Root Architecture Decision

Recommended: **Programme-centric (Option B) with Safety Envelope as constraint root (Option C)**.

---

## 11  Implementation Data Model

See [`ampel360/resolver.py`](../../ampel360/resolver.py) for the Python implementation.

---

## 12  Phase-Axis Interaction Matrix

| Phase | Safety (H) | Security | Economic | Circular |
|-------|-----------|----------|----------|----------|
| P000 | Risk envelope definition | Classification assignment | Business case | Circularity targets |
| P010 | H-derived requirements | Security requirements | Cost constraints | DPP requirements |
| P020 | Safety architecture | Secure design patterns | Make/buy decisions | Material selection |
| P030 | FMEA, FTA, SSA | Vulnerability analysis | Production cost model | Material passports |
| P040 | Safety evidence | Penetration testing | Model cost tracking | LCA models |
| P050 | Production safety | Supply chain security | Tooling investment | Waste minimization |
| P060 | Quality gates | Manufacturing security | Unit cost actuals | Material traceability |
| P070 | Compliance demonstration | Security certification | Certification cost | Environmental cert |
| P080 | Operational safety case | Operational security | Delivery economics | DPP activation |
| P090 | ICA, ADs, fleet safety | Operational security | Operating cost | In-service DPP updates |
| P100 | Safety state transfer | Classification transfer | Asset valuation | DPP chain of custody |
| P110 | Modification safety | Security update | Residual value | Material impact |
| P120 | Safe disposal | Data destruction | Residual recovery | Material recovery |

---

## 13  Implementation Artifacts

| Artifact | Purpose | Format |
|----------|---------|--------|
| [`ampel360.profile_axes.schema.json`](../../schemas/ampel360.profile_axes.schema.json) | JSON Schema for composite profile validation | JSON Schema |
| [`profiles/axis_packs/env_air.yaml`](../../profiles/axis_packs/env_air.yaml) | AIR environment axis pack | YAML |
| [`profiles/axis_packs/env_space.yaml`](../../profiles/axis_packs/env_space.yaml) | SPACE environment axis pack | YAML |
| [`profiles/axis_packs/func_pax.yaml`](../../profiles/axis_packs/func_pax.yaml) | PAX_TRANSPORT function pack | YAML |
| [`profiles/axis_packs/func_cargo.yaml`](../../profiles/axis_packs/func_cargo.yaml) | CARGO_ONLY function pack | YAML |
| [`profiles/axis_packs/payload_*.yaml`](../../profiles/axis_packs/) | Payload classification packs | YAML |
| [`profiles/overlays/easa_q100.yaml`](../../profiles/overlays/easa_q100.yaml) | EASA-Q100 regulatory overlay | YAML |
| [`profiles/overlays/space_q10.yaml`](../../profiles/overlays/space_q10.yaml) | SPACE-Q10 regulatory overlay | YAML |
| [`ampel360/resolver.py`](../../ampel360/resolver.py) | Deterministic `resolve_profile()` implementation | Python |
| [`tests/test_profile_resolution.py`](../../tests/test_profile_resolution.py) | Profile resolution validation tests | Python/pytest |

---

## Appendix A — Glossary

| Term | Definition |
|------|------------|
| **AMPEL360** | Aerospace Model for Product and Engineering Lifecycles (360°) |
| **DAL** | Design Assurance Level (per DO-178C / DO-254) |
| **DPP** | Digital Product Passport |
| **H-factor** | Human Exposure Factor — root safety variable |
| **HOB** | Human On Board — safety ontology classification |
| **ICA** | Instructions for Continued Airworthiness |
| **NHOB** | No Human On Board — safety ontology classification |
| **ROE** | Rules of Engagement |
| **SSOT** | Single Source of Truth |
| **TT** | Teknia Token — incentive alignment unit (1 TT = 360 deg) |

## Appendix B — Document History

| Version | Date | Change Summary |
|---------|------|----------------|
| 1.0 | 2026-01-11 | Initial architectural definition (multi-document) |
| 2.0 | 2026-03-01 | Consolidated single-document specification; added profile resolver, phase-axis matrix, graph root recommendation, implementation data model, and constraint merge rules |
| 2.0 (editorial) | 2026-03-07 | Updated AMPEL360 formal expansion and canonical lifecycle definition; aligned metadata with the 2026-03-07 branding revision without changing the v2.0 implementation baseline |

---

*AMPEL360 — Amedeo Pelliccia / IDEALE-ESG*
*AI-Assisted Development*
