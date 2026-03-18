---
# pels-014.yaml
# Machine-readable specification for SPEC-PELS-014
# Product and Engineering Lifecycle Standard (14-State Model).
# Reference: ESSA/SPEC-PELS-014.md
# Author: Engineering Governance Board

schema_version: "1.0.0"
document_type: lifecycle_state_model
last_updated: "2026-02-26T00:00:00Z"

# ─────────────────────────────────────────────
# 1. Specification Metadata
# ─────────────────────────────────────────────
specification:
  id: SPEC-PELS-014
  title: Product and Engineering Lifecycle Standard
  version: "1.0.0"
  date: "2026-02-26"
  author: Engineering Governance Board
  status: released
  scope: >
    Applicable to all technical artifacts, hardware, software, and
    documentation within the programme.

# ─────────────────────────────────────────────
# 2. Lifecycle Streams
# ─────────────────────────────────────────────
streams:
  - id: ENGINEERING
    label: Engineering Stream
    description: >
      Definition, virtual validation, and regulatory approval.
      Output: Type Design.
    states: [CON, REQ, ARC, DES, ANA, VER, VAL, CRT]

  - id: PRODUCT
    label: Product Stream
    description: >
      Physical instantiation, operation, and in-service management.
      Output: Physical Asset.
    states: [PRD, DLV, OPS, MNT, MOD, RET]

# ─────────────────────────────────────────────
# 3. State Definitions
# ─────────────────────────────────────────────
states:

  # ── Engineering Stream (1–8) ──────────────
  - number: 1
    code: CON
    label: Conceived
    stream: ENGINEERING
    gate:
      trigger: Project Kick-off
    definition: >
      The need or opportunity is identified.
    artifacts:
      - Project Charter
      - Stakeholder Register
    exit_criteria: Project Plan Approved

  - number: 2
    code: REQ
    label: Specified
    stream: ENGINEERING
    gate:
      trigger: Requirements Review (RR)
    definition: >
      Functional and non-functional requirements are baselined.
    artifacts:
      - System Requirement Specification (SRS)
      - Interface Control Document (ICD)
    exit_criteria: Requirements Traceability Matrix (RTM) frozen

  - number: 3
    code: ARC
    label: Architected
    stream: ENGINEERING
    gate:
      trigger: System Architecture Review (SAR)
    definition: >
      Logical and physical architecture defined. System interfaces
      established.
    artifacts:
      - Architecture Description Document
      - System Block Diagrams
    exit_criteria: Architecture Baseline established

  - number: 4
    code: DES
    label: Designed
    stream: ENGINEERING
    gate:
      trigger: Critical Design Review (CDR)
    definition: >
      Detailed design completed. Ready for manufacturing/coding.
    artifacts:
      - 2D/3D Models
      - Schematics
      - Software Design Documents
    exit_criteria: Design Release (Drawing/Model signed off)

  - number: 5
    code: ANA
    label: Analyzed
    stream: ENGINEERING
    gate:
      trigger: Analysis Baseline (AB)
    definition: >
      Engineering analysis validates the design against requirements
      (Stress, Thermal, CFD, Safety).
    artifacts:
      - Analysis Reports
      - Safety Assessment (FHA/FTA)
    exit_criteria: Analysis results confirm Design margins

  - number: 6
    code: VER
    label: Verified
    stream: ENGINEERING
    gate:
      trigger: Test Completion (TRR)
    definition: >
      The system meets specified requirements (Builds Right).
    artifacts:
      - Verification Plans
      - Test Reports
      - Compliance Matrix
    exit_criteria: Verification Cross-Reference Index (VCRI) closed

  - number: 7
    code: VAL
    label: Validated
    stream: ENGINEERING
    gate:
      trigger: User Acceptance (UAT)
    definition: >
      The system meets user needs in the operational environment
      (Right Build).
    artifacts:
      - Validation Reports
      - Flight Test Reports
    exit_criteria: User/Operator sign-off

  - number: 8
    code: CRT
    label: Certified
    stream: ENGINEERING
    gate:
      trigger: Type Certificate (TC)
    definition: >
      Regulatory Authority (EASA/FAA) approves the design for
      production/operation.
    artifacts:
      - Type Certificate Data Sheet (TCDS)
      - AFM approvals
    exit_criteria: Certificate Issued

  # ── Product Stream (9–14) ─────────────────
  - number: 9
    code: PRD
    label: Produced
    stream: PRODUCT
    gate:
      trigger: First Article Inspection (FAI)
    definition: >
      The first physical unit is manufactured and inspected against
      the Design Definition.
    artifacts:
      - First Article Inspection Report (FAIR)
      - Production Records
    exit_criteria: Conformity confirmed

  - number: 10
    code: DLV
    label: Delivered
    stream: PRODUCT
    gate:
      trigger: Handover Protocol
    definition: >
      Transfer of custody and ownership to the customer/operator.
    artifacts:
      - Certificate of Conformity (CoC)
      - Delivery Note
      - Acceptance Test Report
    exit_criteria: Customer Acceptance Document signed

  - number: 11
    code: OPS
    label: Operational
    stream: PRODUCT
    gate:
      trigger: Entry Into Service (EIS)
    definition: >
      The product is active in the operational environment.
    artifacts:
      - Operational Manuals
      - Flight Log Data
      - Performance Monitoring
    exit_criteria: Product is generating value/data

  - number: 12
    code: MNT
    label: Maintained
    stream: PRODUCT
    gate:
      trigger: Scheduled Service (Check)
    definition: >
      Preventive or corrective maintenance performed to retain
      airworthiness. Configuration remains consistent.
    artifacts:
      - Job Cards
      - Maintenance Logs
      - Service Reports
    exit_criteria: Return to Service (RTS) Certificate

  - number: 13
    code: MOD
    label: Modified
    stream: PRODUCT
    gate:
      trigger: Major Change / Retrofit
    definition: >
      A significant alteration to the baseline configuration
      (Service Bulletin or Engineering Order).
    artifacts:
      - Service Bulletin (SB)
      - Engineering Order (EO)
      - Revised Drawings
    exit_criteria: "Reroute to OPS or CRT if re-certification required"

  - number: 14
    code: RET
    label: Retired
    stream: PRODUCT
    gate:
      trigger: End of Life (EOL)
    definition: >
      Permanent removal from service. Disposal or archiving.
    artifacts:
      - Decommissioning Report
      - Recycling Certificates
      - Archive Index
    exit_criteria: Lifecycle Closed

# ─────────────────────────────────────────────
# 4. Transition Logic (State Machine)
# ─────────────────────────────────────────────
transitions:
  standard_flow:
    sequence: [CON, REQ, ARC, DES, ANA, VER, VAL, CRT, PRD, DLV, OPS]
    rule: "Skipping states is forbidden"

  operational_loops:
    - id: maintenance_loop
      label: Maintenance Loop
      path: "OPS ⇄ MNT"
      description: >
        The product remains in the same configuration baseline.

    - id: modification_loop
      label: Modification Loop
      path: "OPS → MOD → OPS"
      description: >
        The product changes configuration.

    - id: re_certification
      label: Re-Certification
      path: "MOD → CRT"
      description: >
        If modification requires authority approval.

  termination:
    path: "OPS → RET"

# ─────────────────────────────────────────────
# 5. Naming Convention
# ─────────────────────────────────────────────
naming_convention:
  pattern: "[Program]-[ATA]-[Article]-[STATE]-[Sequence]-[Variant]"
  state_position: lifecycle_suffix
  examples:
    - filename: "GP-AM-AMPEL-0100-28-1-DES-001-A"
      description: "Tank Design Files (State 4)"
    - filename: "GP-AM-AMPEL-0100-28-1-ANA-001-A"
      description: "Tank Stress Analysis (State 5)"
    - filename: "GP-AM-AMPEL-0100-28-1-CRT-001-A"
      description: "Tank Certification Memo (State 8)"
    - filename: "GP-AM-AMPEL-0100-28-1-MNT-001-A"
      description: "Tank Inspection Checklist (State 12)"

# ─────────────────────────────────────────────
# 6. Governance Matrix
# ─────────────────────────────────────────────
governance:
  - phase: "1-3 (Concept/Spec/Arch)"
    approving_authority: Chief Engineer
    review_board: Requirements Review Board (RRB)

  - phase: "4-5 (Design/Analysis)"
    approving_authority: Design Authority
    review_board: Design Review Board (DRB)

  - phase: "6-7 (Ver/Val)"
    approving_authority: Chief Test Engineer
    review_board: Test Review Board (TRB)

  - phase: "8 (Certification)"
    approving_authority: Certification Manager
    review_board: Certification Board / Authority

  - phase: "9-10 (Prod/Deliver)"
    approving_authority: Production Manager
    review_board: Quality Board

  - phase: "11-13 (Ops/Maint/Mod)"
    approving_authority: Operator / CAMO
    review_board: Configuration Control Board (CCB)

  - phase: "14 (Retire)"
    approving_authority: Asset Manager
    review_board: Final Review Board

# ─────────────────────────────────────────────
# 7. Revision History
# ─────────────────────────────────────────────
revision_history:
  - version: "1.0.0"
    date: "2026-02-26"
    description: Initial release — 14-state lifecycle model

---

# SPEC-PELS-014: Product and Engineering Lifecycle Standard

**Spec ID:** SPEC-PELS-014
**Title:** Product and Engineering Lifecycle Standard
**Version:** 1.0.0
**Date:** 2026-02-26
**Author:** Engineering Governance Board
**Status:** Released
**Scope:** Applicable to all technical artifacts, hardware, software, and documentation within the programme.
**Machine-readable spec:** [`pels-014.yaml`](pels-014.yaml)

---

## 1. Purpose & Scope

This specification establishes a unified **14-State Lifecycle Model** applicable to all system artifacts. It bridges the gap between **Engineering Activities** (virtual/design domain) and **Product Stages** (physical/operational domain).

The model ensures that every artifact carries a deterministic state identifier in its filename, providing instant visibility of its maturity, legality, and configuration status.

---

## 2. Lifecycle Architecture

The 14 states are divided into two primary domains:

1. **Engineering Stream (States 1–8):** Focuses on definition, virtual validation, and regulatory approval. The output is a *Type Design*.
2. **Product Stream (States 9–14):** Focuses on physical instantiation, operation, and in-service management. The output is a *Physical Asset*.

---

## 3. Detailed State Definitions

### 3.1. Engineering Stream (Definition & Approval)

| # | Code | State | Gate (Trigger) | Definition & Exit Criteria |
|:---|:---|:---|:---|:---|
| **1** | **CON** | **Conceived** | Project Kick-off | **Definition:** The need or opportunity is identified. **Artifacts:** Project Charter, Stakeholder Register. **Exit:** Project Plan Approved. |
| **2** | **REQ** | **Specified** | Requirements Review (RR) | **Definition:** Functional and non-functional requirements are baselined. **Artifacts:** System Requirement Specification (SRS), Interface Control Document (ICD). **Exit:** Requirements Traceability Matrix (RTM) frozen. |
| **3** | **ARC** | **Architected** | System Architecture Review (SAR) | **Definition:** Logical and physical architecture defined. System interfaces established. **Artifacts:** Architecture Description Document, System Block Diagrams. **Exit:** Architecture Baseline established. |
| **4** | **DES** | **Designed** | Critical Design Review (CDR) | **Definition:** Detailed design completed. Ready for manufacturing/coding. **Artifacts:** 2D/3D Models, Schematics, Software Design Documents. **Exit:** Design Release (Drawing/Model signed off). |
| **5** | **ANA** | **Analyzed** | Analysis Baseline (AB) | **Definition:** Engineering analysis validates the design against requirements (Stress, Thermal, CFD, Safety). **Artifacts:** Analysis Reports, Safety Assessment (FHA/FTA). **Exit:** Analysis results confirm Design margins. |
| **6** | **VER** | **Verified** | Test Completion (TRR) | **Definition:** The system meets specified requirements (Builds Right). **Artifacts:** Verification Plans, Test Reports, Compliance Matrix. **Exit:** Verification Cross-Reference Index (VCRI) closed. |
| **7** | **VAL** | **Validated** | User Acceptance (UAT) | **Definition:** The system meets user needs in the operational environment (Right Build). **Artifacts:** Validation Reports, Flight Test Reports. **Exit:** User/Operator sign-off. |
| **8** | **CRT** | **Certified** | Type Certificate (TC) | **Definition:** Regulatory Authority (EASA/FAA) approves the design for production/operation. **Artifacts:** Type Certificate Data Sheet (TCDS), AFM approvals. **Exit:** Certificate Issued. |

### 3.2. Product Stream (Instantiation & Operations)

| # | Code | State | Gate (Trigger) | Definition & Exit Criteria |
|:---|:---|:---|:---|:---|
| **9** | **PRD** | **Produced** | First Article Inspection (FAI) | **Definition:** The first physical unit is manufactured and inspected against the Design Definition. **Artifacts:** First Article Inspection Report (FAIR), Production Records. **Exit:** Conformity confirmed. |
| **10** | **DLV** | **Delivered** | Handover Protocol | **Definition:** Transfer of custody and ownership to the customer/operator. **Artifacts:** Certificate of Conformity (CoC), Delivery Note, Acceptance Test Report. **Exit:** Customer Acceptance Document signed. |
| **11** | **OPS** | **Operational** | Entry Into Service (EIS) | **Definition:** The product is active in the operational environment. **Artifacts:** Operational Manuals, Flight Log Data, Performance Monitoring. **Exit:** Product is generating value/data. |
| **12** | **MNT** | **Maintained** | Scheduled Service (Check) | **Definition:** Preventive or corrective maintenance performed to retain airworthiness. Configuration remains consistent. **Artifacts:** Job Cards, Maintenance Logs, Service Reports. **Exit:** Return to Service (RTS) Certificate. |
| **13** | **MOD** | **Modified** | Major Change / Retrofit | **Definition:** A significant alteration to the baseline configuration (Service Bulletin or Engineering Order). **Artifacts:** Service Bulletin (SB), Engineering Order (EO), Revised Drawings. **Exit:** Reroute to **OPS** or **CRT** if re-certification required. |
| **14** | **RET** | **Retired** | End of Life (EOL) | **Definition:** Permanent removal from service. Disposal or archiving. **Artifacts:** Decommissioning Report, Recycling Certificates, Archive Index. **Exit:** Lifecycle Closed. |

---

## 4. Transition Logic (State Machine)

The lifecycle follows a rigorous state machine logic. Skipping states is forbidden.

**Standard Flow:**

```
CON → REQ → ARC → DES → ANA → VER → VAL → CRT → PRD → DLV → OPS
```

**Operational Loops:**

- **Maintenance Loop:** `OPS ⇄ MNT` (The product remains in the same configuration baseline).
- **Modification Loop:** `OPS → MOD → OPS` (The product changes configuration).
- **Re-Certification:** `MOD → CRT` (If modification requires authority approval).

**Termination:**

```
OPS → RET
```

---

## 5. Naming Convention Integration

The state code forms the **Lifecycle Suffix** in the filename structure.

**Pattern:**

```text
[Program]-[ATA]-[Article]-[STATE]-[Sequence]-[Variant]
```

**Example: GP-AM Fuel System (ATA 28, Article 1)**

- `GP-AM-AMPEL-0100-28-1-DES-001-A`: Tank Design Files (State 4).
- `GP-AM-AMPEL-0100-28-1-ANA-001-A`: Tank Stress Analysis (State 5).
- `GP-AM-AMPEL-0100-28-1-CRT-001-A`: Tank Certification Memo (State 8).
- `GP-AM-AMPEL-0100-28-1-MNT-001-A`: Tank Inspection Checklist (State 12).

---

## 6. Governance Matrix

| Phase | Approving Authority | Review Board |
|:---|:---|:---|
| **1-3 (Concept/Spec/Arch)** | Chief Engineer | Requirements Review Board (RRB) |
| **4-5 (Design/Analysis)** | Design Authority | Design Review Board (DRB) |
| **6-7 (Ver/Val)** | Chief Test Engineer | Test Review Board (TRB) |
| **8 (Certification)** | Certification Manager | Certification Board / Authority |
| **9-10 (Prod/Deliver)** | Production Manager | Quality Board |
| **11-13 (Ops/Maint/Mod)** | Operator / CAMO | Configuration Control Board (CCB) |
| **14 (Retire)** | Asset Manager | Final Review Board |

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`pels-014.yaml`](pels-014.yaml) | Machine-readable lifecycle state model: 14 states, transitions, governance matrix |
| [`../simplex-contract.yaml`](../simplex-contract.yaml) | Evidence-gated admissibility framework referenced by certification gate (CRT) |
| [`../AI-BOOST/DEL-04-innovation-and-impact.md`](../AI-BOOST/DEL-04-innovation-and-impact.md) | Innovation and Impact deliverable — TRL progression aligned with PELS-14 states |
