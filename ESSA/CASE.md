# ESSA Case Study

**European Space Safety Agency — Governed under the European Sovereign Systems Architecture**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-CASE-001 |
| **Version** | v0.1-draft |
| **Status** | Illustrative Reference Case |
| **Parent** | ESSA Constitutional Root Document (ESSA/README.md) |
| **Subject System** | European Space Safety Agency (ESSA) — civil-platforms fork |
| **Scenario** | Reusable Space Platform operator lifecycle certification |
| **Last Updated** | 2026-02-28 |

---

## 1. Case Purpose

This document demonstrates how the **European Sovereign Systems Architecture (ESSA)** governs the **European Space Safety Agency** (the canonical space-based civil-platforms fork of the same acronym) as a concrete lifecycle governance implementation.

It traces a reference operator — **EuroSpace GmbH** — seeking certification of a **Reusable Space Platform (RSP)** through ESSA's CIVIL-PLATFORMS lifecycle standard (CCTLS), with the EU-SECURITY overlay applied and ALPC evaluation performed at the end.

This case serves as:

- A worked reference for operators entering the ESSA governance framework
- A validation baseline confirming the constitutional invariants of ESSA/README.md hold across all phases
- A template for future case artefacts under ESSA

---

## 2. Subject System and Context

### 2.1 Operator

| Field | Value |
|-------|-------|
| Operator name | EuroSpace GmbH |
| Registry ID | OP-EU-2026-001 |
| Established | Germany (EU-established operator) |
| Scope | Uncrewed and crewed suborbital + low-Earth-orbit operations |
| Applicable Parts | Part-STO, Part-LRE, Part-RSP, Part-CAW-S, Part-SUST, Part-CYB-S |

### 2.2 Platform

| Field | Value |
|-------|-------|
| Platform name | AURORA-1 |
| Platform type | Two-stage partially-reusable launch vehicle |
| Domain | RSP |
| Reuse applicability | Stage-1 booster (target: 10 reflight cycles per unit) |
| First flight | Phase B milestone |

### 2.3 Governance Context

EuroSpace GmbH operates under the European Space Safety Agency regulatory framework.

The following **Parts** apply to this certification case:

| Roadmap Phase | Active Parts |
|---------------|-------------|
| Phase A (0–18 months) | Part-STO Light, Part-LRE, Part-SPP, Part-SUST |
| Phase B (18–36 months) | Part-RSP, Part-CAW-S, Part-MRO-S, Part-CYB-S |
| Phase C (36–60 months) | Part-SCL, Part-STO-ORA |

---

## 3. Governance Application — Phase Walk-Through

This section traces AURORA-1 through CCTLS phases P000–P120, showing the governed token graph and EU-SECURITY control linkages at each phase.

---

### Phase P000 — Registry & Governance

**What is governed:** Operator identity, AoR assignments, roles, ledger initialisation, baseline zero.

**Tokens created:**

```yaml
- token_id: REG-OP-EU-2026-001
  token_type: REG_ENTRY
  phase: P000
  package_id: PKG-P000-REGISTRY
  aor_id: AOR-ESSA-OP-001
  title: "EuroSpace GmbH — Operator Registry Entry"
  version: "1.0.0"
  status: CONFIRMED
  bindings:
    domain: RSP
    operation_context: LRE
  links:
    - rel: verified_by
      target_token_id: MCSC-ETH-01     # traceable authority
    - rel: verified_by
      target_token_id: MCSC-ETH-04     # ledger write-back
```

**EU-SECURITY controls applied:** MCSC-ETH-01, MCSC-ETH-04

**Gate result:** REG-OP-EU-2026-001 CONFIRMED → ACTIVATED → operator identity established in EU Civil Space Transport Registry.

---

### Phase P010 — Scope & Operational Context

**What is governed:** Mission definition, operational limits, applicability boundaries.

**Tokens created:**

```yaml
- token_id: SCOPE-AURORA1-LRE-2026
  token_type: SCOPE_NODE
  phase: P010
  aor_id: AOR-ESSA-SCOPE-001
  title: "AURORA-1 Operational Scope — LRE + RSP Domain"
  version: "1.0.0"
  status: CONFIRMED
  bindings:
    domain: RSP
    operation_context: LRE
    asset_state: AS_BUILT
    effectivity: [ALL]
  links:
    - rel: derives_from
      target_token_id: REG-OP-EU-2026-001
```

**Scope declared:**

- Launch operations from Spaceport Azores (EU territory)
- Re-entry and booster recovery operations (Atlantic corridor)
- Payload mass class: 4 000–8 000 kg LEO
- No crewed operations in Phase A/B

---

### Phase P020 — Safety & Risk Envelope

**What is governed:** Hazard identification, safety objectives, acceptance criteria.

**Tokens created:**

```yaml
- token_id: HAZARD-AURORA1-LRE-001
  token_type: HAZARD
  phase: P020
  package_id: PKG-P020-SAFETY
  aor_id: AOR-ESSA-SAF-001
  title: "Uncontrolled re-entry — Stage 1 booster"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: verified_by
      target_token_id: MCSC-ETH-03     # non-maleficence
    - rel: verified_by
      target_token_id: MCSC-RES-01     # BCP token required

- token_id: SAF-OBJ-AURORA1-001
  token_type: SAF_OBJ
  phase: P020
  aor_id: AOR-ESSA-SAF-001
  title: "Individual casualty risk ≤ 1×10⁻⁶ per flight event"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: supports
      target_token_id: HAZARD-AURORA1-LRE-001
    - rel: verified_by
      target_token_id: MCSC-ETH-03
```

**EU-SECURITY controls applied:** MCSC-ETH-03 (non-maleficence), MCSC-RES-01 (BCP)

**Gate result:** Hazard register CONFIRMED. Safety objectives ACTIVATED. ALPC evidence obligation raised: traceability from SAF-OBJ to test evidence (P070) required.

---

### Phase P030 — Logistics & Industrial Chains

**What is governed:** Supply chain topology, fabrication processes, ESG overlay.

**Key chain nodes:**

```yaml
- token_id: CHAIN-AURORA1-PROPULSION
  token_type: CHAIN
  phase: P030
  package_id: PKG-P030-CHAIN-TOPOLOGY
  aor_id: AOR-ESSA-CHAIN-001
  title: "AURORA-1 Propulsion Supply Chain"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: verified_by
      target_token_id: MCSC-ETH-04     # ledger write-back

- token_id: CHAIN-NODE-ENGTEC-DE
  token_type: CHAIN_NODE
  phase: P030
  package_id: PKG-P030-SUPPLY
  aor_id: AOR-ESSA-CHAIN-001
  title: "EngTec GmbH — Propulsion subsystem supplier"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: recorded_in
      target_token_id: CHAIN-AURORA1-PROPULSION
    - rel: verified_by
      target_token_id: MCSC-SCI-01     # provenance trace hook
    - rel: verified_by
      target_token_id: MCSC-SCI-02     # supplier MCSC-ETH assessment

- token_id: KPI_MEASURE-CO2e-AURORA1-2026Q1
  token_type: KPI_MEASURE
  phase: P030
  package_id: PKG-P030-ESG-OVERLAY
  aor_id: AOR-ESSA-CHAIN-001
  title: "CO₂e KPI — Propulsion chain Q1 2026"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: measured_on
      target_token_id: CHAIN-NODE-ENGTEC-DE
  metadata:
    kpi_id: KPI-CO2e
    period: {from: "2026-01-01", to: "2026-03-31"}
    value: 48.2
    unit: tCO2e
```

**EU-SECURITY controls applied:** MCSC-SCI-01, MCSC-SCI-02, MCSC-ETH-04

**Hard rule verified:** every KPI_MEASURE carries `links: [{ rel: measured_on, target_token_id: CHAIN_NODE }]` ✓

---

### Phase P040 — Numerical & Simulation Methods (DMU + PMU)

**What is governed:** Structural and aerothermal models for Stage-1 re-entry, DMU geometry, PMU simulation runs.

**Key tokens:**

```yaml
- token_id: DMU-AURORA1-STAGE1-v1
  token_type: DMU_ITEM
  phase: P040
  package_id: PKG-P040-DMU
  aor_id: AOR-ESSA-SIM-001
  title: "AURORA-1 Stage-1 DMU — reuse-critical structure"
  version: "1.0.0"
  status: CONFIRMED

- token_id: SIM-AURORA1-REENTRY-001
  token_type: SIM_RUN
  phase: P040
  package_id: PKG-P040-SIM-RUNS
  aor_id: AOR-ESSA-SIM-001
  title: "Stage-1 re-entry trajectory simulation — 10-cycle envelope"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: supports
      target_token_id: SAF-OBJ-AURORA1-001
    - rel: derives_from
      target_token_id: DMU-AURORA1-STAGE1-v1
```

---

### Phase P050 — Design Office Authority (DOA Sign)

**What is governed:** DOA sign-off on Stage-1 structural qualification; findings closure.

**Key tokens:**

```yaml
- token_id: DOA-SIGN-AURORA1-STR-001
  token_type: DOA_SIGN
  phase: P050
  package_id: PKG-P050-DOA-SIGNOFF
  aor_id: AOR-ESSA-DOA-001
  title: "DOA sign-off — Stage-1 structural qualification"
  version: "1.0.0"
  status: ACTIVATED
  links:
    - rel: supports
      target_token_id: SIM-AURORA1-REENTRY-001
    - rel: verified_by
      target_token_id: MCSC-ACC-02     # authority approval before ACTIVATE
    - rel: verified_by
      target_token_id: MCSC-ETH-01     # traceable authority
```

**EU-SECURITY controls applied:** MCSC-ACC-02, MCSC-ETH-01

**Gate result:** DOA_SIGN cannot ACTIVATE unless `links: [{ rel: supports, target_phase: P040 }]` present ✓

---

### Phase P060 — Product/Tool Quality & Conformity (CE)

**What is governed:** CE declarations for Ground Support Equipment (GSE); tool calibration records; third-party component conformity.

**Key tokens:**

```yaml
- token_id: CE-DECL-GSE-FUELLING-001
  token_type: CE_DECL
  phase: P060
  package_id: PKG-P060-CE-TECH-FILE
  aor_id: AOR-ESSA-CONF-001
  title: "CE Declaration — Cryogenic fuelling GSE"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: verified_by
      target_token_id: MCSC-SCI-03     # third-party conformity before ACTIVATE
```

**EU-SECURITY controls applied:** MCSC-SCI-03

---

### Phase P070 — Flight Tests (CERT)

**What is governed:** AURORA-1 certification flight campaign; test cases and reports.

**Key tokens:**

```yaml
- token_id: TEST-CAMPAIGN-AURORA1-CERT-001
  token_type: TEST_CAMPAIGN
  phase: P070
  package_id: PKG-P070-TEST-CAMPAIGNS
  aor_id: AOR-ESSA-TEST-001
  title: "AURORA-1 Certification Flight Campaign"
  version: "1.0.0"
  status: ACTIVATED

- token_id: TEST-REPORT-AURORA1-FLT-001
  token_type: TEST_REPORT
  phase: P070
  package_id: PKG-P070-REPORTS
  aor_id: AOR-ESSA-TEST-001
  title: "AURORA-1 Flight 1 — Certification Test Report"
  version: "1.0.0"
  status: PUBLISHED
  links:
    - rel: verifies
      target_token_id: SAF-OBJ-AURORA1-001
    - rel: supports
      target_token_id: DOA-SIGN-AURORA1-STR-001
```

**Traceability chain verified:** SAF-OBJ → TEST_REPORT → DOA_SIGN ✓

---

### Phase P080 — In-Service + ICAs + MRO (Reuse Cycles)

**What is governed:** Stage-1 refurbishment after recovery; Instructions for Continued Airworthiness; reuse-cycle life tracking. Governed under Part-CAW-S and Part-MRO-S.

**Key tokens:**

```yaml
- token_id: ICA-TASK-AURORA1-STG1-INSPECT-001
  token_type: ICA_TASK
  phase: P080
  package_id: PKG-P080-ICA
  aor_id: AOR-ESSA-MRO-001
  title: "Stage-1 booster post-recovery inspection procedure"
  version: "1.0.0"
  status: CONFIRMED
  bindings:
    domain: RSP
    operation_context: SHOP
    asset_state: AS_FLOWN
    reuse_cycle_id: RC-2026-01
    effectivity: [ALL]

- token_id: MRO-JOB-AURORA1-STG1-REFURB-001
  token_type: MRO_JOB
  phase: P080
  package_id: PKG-P080-MRO
  aor_id: AOR-ESSA-MRO-001
  title: "Stage-1 refurbishment cycle 1 — Propulsion cleaning & NDT"
  version: "1.0.0"
  status: ACTIVATED
  bindings:
    domain: RSP
    operation_context: SHOP
    asset_state: REMOVED
    reuse_cycle_id: RC-2026-01
  links:
    - rel: derives_from
      target_token_id: ICA-TASK-AURORA1-STG1-INSPECT-001
    - rel: verified_by
      target_token_id: MCSC-ACC-03     # occurrence → root cause
```

**Hard rule verified:** `domain=RSP` + reuse applies → `reuse_cycle_id` REQUIRED ✓

**EU-SECURITY controls applied:** MCSC-ACC-03

---

### Phase P090 — Mission Ops & Traffic / Range Control

**What is governed:** AURORA-1 Flight 2 mission plan; launch window authorisation from Spaceport Azores; STM deconfliction. Governed under Part-LRE and Part-SPP.

**Key tokens:**

```yaml
- token_id: MISSION-PLAN-AURORA1-FLT2
  token_type: MISSION_PLAN
  phase: P090
  package_id: PKG-P090-MISSION-CONTROL
  aor_id: AOR-ESSA-OPS-001
  title: "AURORA-1 Flight 2 Mission Plan"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: verified_by
      target_token_id: MCSC-HOB-03     # human confirmation required
    - rel: verified_by
      target_token_id: MCSC-ETH-02     # human override path defined

- token_id: TRAFFIC-CLR-AURORA1-FLT2
  token_type: TRAFFIC_CLEARANCE
  phase: P090
  package_id: PKG-P090-TRAFFIC-STM
  aor_id: AOR-ESSA-OPS-001
  title: "Launch window clearance — STM deconfliction T-72h"
  version: "1.0.0"
  status: ACTIVATED
  links:
    - rel: supports
      target_token_id: MISSION-PLAN-AURORA1-FLT2
```

**EU-SECURITY controls applied:** MCSC-HOB-03, MCSC-ETH-02

**Interface consumed:** EU SST conjunction warning data (EUSPA IF-SST → ESSA DIR-04) ✓

---

### Phase P100 — ESG Reporting & Transparency

**What is governed:** Consolidated ESG report for AURORA-1 operations 2026 Q1; chain + operation KPI aggregation.

**Key tokens:**

```yaml
- token_id: ESG-RPT-AURORA1-2026Q1
  token_type: ESG_REPORT
  phase: P100
  package_id: PKG-P100-ESG-CONSOLIDATION
  aor_id: AOR-ESSA-ESG-001
  title: "AURORA-1 ESG Report — 2026 Q1"
  version: "1.0.0"
  status: PUBLISHED
  links:
    - rel: supports
      target_token_id: KPI_MEASURE-CO2e-AURORA1-2026Q1  # P030 chain
    - rel: supports
      target_token_id: MRO-JOB-AURORA1-STG1-REFURB-001  # P080 ops

- token_id: AGG-RULE-CO2e-AURORA1
  token_type: AGG_RULE
  phase: P100
  package_id: PKG-P100-ESG-CONSOLIDATION
  aor_id: AOR-ESSA-ESG-001
  title: "CO₂e aggregation rule — chain + operations"
  version: "1.0.0"
  status: CONFIRMED
  metadata:
    method: sum
    inputs: [KPI_MEASURE-CO2e-AURORA1-2026Q1, MRO-CO2e-OPS-2026Q1]
    boundary: AURORA-1 programme
    period: "2026-Q1"
```

**Hard rule verified:** ESG_REPORT compiles only KPI_MEASURE anchored to P030/P080 and declares AGG_RULE ✓

---

### Phase P120 — Cyber & Resilience (Cross-Cutting)

**What is governed:** Cybersecurity controls for Mission Control System; Business Continuity Plan for launch operations. Governed under Part-CYB-S.

**Key tokens:**

```yaml
- token_id: CYB-CTRL-MCS-001
  token_type: CYB_CONTROL
  phase: P120
  package_id: PKG-P120-CYBER
  aor_id: AOR-ESSA-CYB-001
  title: "Mission Control System — access control baseline"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: verified_by
      target_token_id: MCSC-SOV-03     # EU cyber baseline

- token_id: BCP-LRE-AURORA1-001
  token_type: BCP_ITEM
  phase: P120
  package_id: PKG-P120-RESILIENCE
  aor_id: AOR-ESSA-RES-001
  title: "Launch operations BCP — range abort and operator notification"
  version: "1.0.0"
  status: CONFIRMED
  links:
    - rel: verified_by
      target_token_id: MCSC-RES-01
    - rel: verified_by
      target_token_id: MCSC-RES-03     # no SPOF in activation chain

- token_id: RECOVERY-TEST-BCP-001
  token_type: RECOVERY_TEST
  phase: P120
  package_id: PKG-P120-RESILIENCE
  aor_id: AOR-ESSA-RES-001
  title: "BCP recovery test — launch abort drill 2026-02"
  version: "1.0.0"
  status: PUBLISHED
  links:
    - rel: supports
      target_token_id: BCP-LRE-AURORA1-001
    - rel: verified_by
      target_token_id: MCSC-RES-02     # test executed per baseline cycle
```

**EU-SECURITY controls applied:** MCSC-RES-01, MCSC-RES-02, MCSC-RES-03, MCSC-SOV-03

---

## 4. EU-SECURITY Overlay Summary

The table below confirms EU-SECURITY mandatory control coverage for the AURORA-1 case.

| Phase | Mandatory Controls | Token(s) Linking | Coverage |
|-------|-------------------|-----------------|---------|
| P020 | MCSC-ETH-03, MCSC-RES-01 | HAZARD-AURORA1-LRE-001 | ✓ |
| P050 | MCSC-ACC-02, MCSC-ETH-01 | DOA-SIGN-AURORA1-STR-001 | ✓ |
| P080 | MCSC-ACC-03, MCSC-SCI-01 | MRO-JOB-AURORA1-STG1-REFURB-001 | ✓ |
| P090 | MCSC-HOB-03, MCSC-ETH-02 | MISSION-PLAN-AURORA1-FLT2 | ✓ |
| P120 | All MCSC-RES-* | BCP-LRE-AURORA1-001, RECOVERY-TEST-BCP-001 | ✓ |

**Cross-cutting (all phases):** MCSC-ETH-04 (ledger write-back) — verified via MTLdg audit trail ✓

**Supply chain controls:** MCSC-SCI-01, MCSC-SCI-02, MCSC-SCI-03 — applied in P030/P060 ✓

**Human oversight:** MCSC-HOB-01 (AI artefact classification), MCSC-HOB-02 (execution boundary), MCSC-HOB-03 (human confirmation) — applied in P090 ✓

**Sovereign interoperability:** MCSC-SOV-01 (EU-compliant infrastructure), MCSC-SOV-03 (cyber baseline) — applied in P000/P120 ✓

---

## 5. ALPC Certification Evaluation

ALPC evaluated the AURORA-1 lifecycle graph against the six ALPC criteria.

### 5.1 Evaluation Summary

| ALPC Criterion | Result | Notes |
|---------------|--------|-------|
| Structural completeness | PASS | All 13 CCTLS phases have at least one token; P110 correctly empty (RESERVED) |
| Traceability coverage | PASS | SAF-OBJ → TEST_REPORT → DOA_SIGN → SIM_RUN chain verified |
| Evidence sufficiency | PASS | TEST-REPORT-AURORA1-FLT-001 PUBLISHED, linked to SAF-OBJ and DOA_SIGN |
| EU-SECURITY control coverage | PASS | All mandatory linkages per MCSC §4.2 present (see §4 above) |
| Phase coherence | PASS | No P050 ACTIVATE without P040 `supports` link; no P100 ESG_REPORT without AGG_RULE |
| Baseline integrity | PASS | All tokens carry sha3-512 checksum; MTLdg ledger entries confirmed |

### 5.2 Certification Decision

**ALPC CERTIFICATION GRANTED**

```
Case:          ESSA-CASE-001
Operator:      EuroSpace GmbH (OP-EU-2026-001)
Platform:      AURORA-1
Scope:         Part-STO / Part-LRE / Part-SPP / Part-SUST (Phase A)
               Part-RSP / Part-CAW-S / Part-MRO-S / Part-CYB-S (Phase B)
Decision:      CERTIFIED
Baseline:      BL-AURORA1-2026-001
Ledger anchor: MTLdg-ANCHOR-AURORA1-2026-001
```

**Constitutional invariants confirmed:**

- No activation occurred without confirmation ✓
- No publication occurred without invariant validation ✓
- Ethics enforced at gate level (all MCSC-ETH controls satisfied) ✓
- Commercial layers did not weaken core ESSA invariants ✓

---

## 6. EUSPA Interface Consumption

During this case the following ESSA ↔ EUSPA interfaces were consumed:

| Interface | ESSA Function | EUSPA Service | Direction | Consumed in Phase |
|-----------|--------------|---------------|-----------|------------------|
| IF-SST | Operations Oversight (DIR-04) | EU SST conjunction warnings | EUSPA → ESSA | P090 |
| IF-SUST | Sustainability (DIR-06, Part-SUST) | SST debris cataloguing | Bidirectional | P080, P100 |
| IF-STM | Mission Ops (Part-LRE, Part-SPP) | STM coordination | Bidirectional | P090 |

No EUSPA service was duplicated. ESSA consumed EUSPA outputs as specified in `essa-regulatory-framework.yaml §12`. ✓

---

## 7. Lessons and Constitutional Validation

This case validates the following ESSA constitutional claims:

| Claim (from ESSA/README.md) | Validation Evidence |
|-----------------------------|---------------------|
| "Certification is invariant validation over a governed graph" | ALPC evaluated 6 graph-level criteria; no narrative judgement required |
| "No activation without confirmation" | DOA-SIGN-AURORA1-STR-001 could not ACTIVATE until P040 link and MCSC-ACC-02 satisfied |
| "Ethics is enforced at gate level" | MCSC-ETH-01/02/03/04 verified at CONFIRM/ACTIVATE gates, not post-hoc |
| "Commercial layers may build upon ESSA; they may not weaken its core invariants" | Part-STO/RSP/CAW-S operated within constitutional token graph; no invariant weakened |
| "ESG is measured, not declared" | KPI_MEASURE-CO2e anchored to CHAIN_NODE and aggregated via AGG_RULE |

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`case.yaml`](case.yaml) | Machine-readable companion — ESSA-CASE-001 token manifest |
| [`README.md`](README.md) | ESSA Constitutional Root Document |
| [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml) | Parts catalogue, registry schema, roadmap |
| [`cctls.yaml`](cctls.yaml) | CCTLS lifecycle standard — phase and token definitions |
| [`EU-SECURITY/README.md`](EU-SECURITY/README.md) | MCSC control definitions |
| [`EU-SECURITY/INTEGRATIONS/README.md`](EU-SECURITY/INTEGRATIONS/README.md) | MCSC ↔ CCTLS package integration index |
| [`ANNEX-A-glossary.md`](ANNEX-A-glossary.md) | MTL/MTLdg/DOF normative glossary |
