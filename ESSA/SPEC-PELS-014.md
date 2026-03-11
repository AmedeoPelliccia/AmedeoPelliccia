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
