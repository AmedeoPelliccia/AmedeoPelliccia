# EACST — Common Civil Transport Lifecycle Standard (CCTLS) v0.3.0

**Document ID:** EACST-STD-CCTLS-001
**Version:** 0.3.0
**Status:** Draft
**Parent:** EACST-STD-MTL-001

---

## 0) Purpose and Scope

**Purpose:** Define a common lifecycle for "civil aviation + civil RSP" that EACST can standardise first, with **tokenisable**, **traceable** and **auditable** artefacts in a portal of the **AMPEL360-SPACE-T-PORTAL** type.

**Civil scope:** operations, reusable platforms, maintenance/ICA/MRO, industrial chains, product/tool conformity, mission/traffic control, ESG reporting.

**Cyber/resilience:** cross-cutting to all phases.

---

## 1) State Machine (Operational Determinism)

Every governed object follows this state machine:

* **INTERPRET** → capture structured intent
* **CONFIRM** → validate schema, bindings, mandatory links, policies
* **ACTIVATE** → execute (generate/register/publish)
* **PUBLISH** → only if applicable (released/usable artefact)

**Rule:** no "operational" output exists without Confirm → Activate.

---

## 2) EACST Phases (Corrected Numbering)

| Phase    | Name                                              | What it governs                                                                 | Typical Atom                           |
| -------- | ------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------- |
| **P000** | Registry & Governance                             | identities, AoR, roles, ledger, baselines, state                                | `REG_ENTRY`                            |
| **P010** | Scope & Operational Context                       | mission, limits, applicability, context (LINE/SHOP/FLIGHT/LRE)                   | `SCOPE_NODE`                           |
| **P020** | Safety & Risk Envelope                            | hazards, safety objectives, acceptance criteria                                  | `HAZARD`, `SAF_OBJ`                    |
| **P030** | Logistics & Industrial Chains                     | SUPPLY/FAB/CONTRACT (chain domain) + **S&C measured on chain**                   | `CHAIN_NODE`, `PROCESS`, `KPI_MEASURE` |
| **P040** | Numerical & Simulation Methods (DMU+PMU)          | numerical methods, DMU/PMU, qualification, runs/results                          | `METHOD`, `SIM_RUN`                    |
| **P050** | Design Office Authority (DOA sign)                | sign-off design authority, findings/closure                                      | `DOA_SIGN`, `FINDING`                  |
| **P060** | Product/Tool Quality & Conformity (CE)            | CE/EU conformity where applicable + tool/product "fit-for-use" release           | `CE_DECL`, `CAL_CERT`                  |
| **P070** | Flight Tests (CERT)                               | test/demonstration campaigns for certification                                   | `TEST_CAMPAIGN`, `TEST_REPORT`         |
| **P080** | In-Service + ICAs + MRO (incl. shop/refurb/reuse) | in-service operation, ICA, MRO line+shop, refurb/reuse, occurrences/directives   | `ICA_TASK`, `MRO_JOB`, `OCC_REPORT`    |
| **P090** | Mission Ops & Traffic / Range Control             | mission control, slots/windows, STM/ATM/UTM, range safety, constraints           | `MISSION_PLAN`, `TRAFFIC_CLEARANCE`    |
| **P100** | ESG Reporting & Transparency                      | consolidation + ESG publication (chains + operation) + audit                     | `ESG_REPORT`, `AGG_RULE`               |
| **P110** | RESERVED                                          | Reserved for future extensions (e.g., spaceport infrastructure/training orgs)    | —                                      |
| **P120** | Cyber & Resilience (Cross-cutting)                | controls, risks, incidents; linkable to any phase                                | `CYB_CONTROL`, `RES_CONTROL`           |

> **P110** is **reserved** (unused in v0.3.0) for future extensions without breaking numbering.

> **Sustainability & Circularity** is **not** a phase; it is **measured on chains** (P030) and also on operation/MRO (P080), and consolidated in P100.

---

## 3) Portal Model (AoR Cards)

**UI Rule:** the portal is **card-based** and each card represents **exactly one AoR entry**.

### AoR (Minimum)

```yaml
aor:
  aor_id: "AOR-000123"
  title: "Cryo Valve Supplier Chain + KPI overlay"
  phase: "P030"
  domain: "DUAL"                 # AVIATION | RSP | DUAL
  owner_role: "Chain-Authority"
  audience_role: "Engineering"
  lifecycle_deliverable_product: "EACST-CHAIN-BASELINE"
  bindings:
    operation_context: "LINE"    # LINE | SHOP | FLIGHT | LRE
    asset_state: "INSTALLED"     # INSTALLED | REMOVED | AS_BUILT | AS_FLOWN
    reuse_cycle_id: null
    effectivity: ["ALL"]
    variants: []
  template_id: "TPL-P030-CHAIN-001"
  metadata_schema_id: "SCH-P030-CHAIN-META-001"
```

---

## 4) Token Model (Unified for All Phases)

### Token Base (Normative)

```yaml
token:
  token_id: "TOK-..."
  token_type: "..."
  phase: "P030"
  package_id: "PKG-..."
  subpackage_id: "SUBPKG-..."
  aor_id: "AOR-..."

  title: "..."
  version: "1.0.0"
  checksum: "sha3-512:..."

  template_id: "TPL-..."
  metadata_schema_id: "SCH-..."

  bindings:
    domain: "DUAL"
    operation_context: "LINE"
    asset_state: "INSTALLED"
    reuse_cycle_id: null
    effectivity: ["ALL"]
    variants: []

  links:
    - rel: "supports"
      target_token_id: "TOK-..."

  children: ["TOK-..."]
  status: "CONFIRMED"            # DRAFT|CONFIRMED|ACTIVATED|PUBLISHED|OBSOLETE
```

### Recommended Relations (`rel`)

* `derives_from` — derivation
* `supports` — supports
* `verifies` — verifies/demonstrates
* `approved_by` — approved by
* `recorded_in` — recorded in
* `supersedes` — supersedes
* `measured_on` — **mandatory for ESG overlay**

---

## 5) Prompt Units (AI Generator Tab)

Each card has an **AI Generator** with **tokenised prompt units**.

### Prompt Unit (Minimum)

* `prompt_id`, `version`, `checksum`
* Mandatory bindings:
  * `audience_role`
  * `lifecycle_deliverable_product`
  * `template_id`
  * `metadata_schema_id`
* `token_graph[]` (tokens assembled)
* `assembly_order` (deterministic order)
* `activation_policy` (Confirm → Activate)

### Contractual Output on Activation

* `content_body` (fills template)
* `metadata` (complies with schema)
* `validation_status: PASS|WARN|FAIL`
* `artifact_hash` (sha3-512)
* Write-back to AoR (`artifacts[]` + audit trail)

---

## 6) Packages and Schemas by Phase (Essentials)

### P030 — Logistics & Industrial Chains (chain domain + S&C measured on chain)

#### Packages

* `PKG-P030-CHAIN-TOPOLOGY` (graph)
* `PKG-P030-SUPPLY` (suppliers/capabilities)
* `PKG-P030-FABRICATION` (process specs/capability envelope)
* `PKG-P030-CONTRACTING` (contract/SOW/SLA/clauses)
* `PKG-P030-TRACE-HOOKS` (lot/cert hooks to P080/P100)
* `PKG-P030-ESG-OVERLAY` (**S&C overlay**)

#### Atoms (token_type)

**Base chain:**

* `CHAIN`, `CHAIN_NODE`, `CHAIN_EDGE`, `PROCESS`
* `SUPPLIER`, `CAPABILITY`
* `CONTRACT`, `SOW`, `SLA`, `QUALITY_CLAUSE`
* `TRACE_HOOK`, `CERTIFICATE`

**ESG overlay (measurement on chain):**

* `KPI_DEF`, `KPI_MEASURE`, `OBJ`, `AGG_RULE`, `EVIDENCE`, `SC_SCORECARD`

#### Hard Rule

* Every `KPI_MEASURE` and `OBJ` **MUST** have `links: [{rel: measured_on, target_token_id: (CHAIN_NODE|CHAIN_EDGE|PROCESS|CHAIN)}]`.
* If the target is `CHAIN` (aggregate), there **MUST** exist an explicit `AGG_RULE` with inputs.

---

### P040 — Numerical & Simulation Methods (DMU+PMU)

#### Packages

* `PKG-P040-METHODS` (methods + qualification)
* `PKG-P040-DMU` (DMU artefacts)
* `PKG-P040-PMU` (PMU artefacts)
* `PKG-P040-SIM-RUNS` (runs/results)

#### Atoms

* `METHOD`, `MODEL_SPEC`, `VALIDATION_CASE`
* `DMU_ITEM`, `PMU_ITEM`
* `SIM_RUN`, `RESULT`, `INTERP`

#### Recommended Gate

* A `DOA_SIGN` (P050) **cannot CONFIRM** if it does not link to:
  * `METHOD/MODEL_SPEC` and at least one `VALIDATION_CASE` when applicable.

---

### P050 — Design Office Authority (DOA sign)

#### Packages

* `PKG-P050-DOA-SIGNOFF`
* `PKG-P050-FINDINGS`
* `PKG-P050-CLOSURE`

#### Atoms

* `DOA_SIGN`, `FINDING`, `CLOSURE`, `COMPLIANCE_ITEM`

#### Recommended Gate

* `DOA_SIGN` **MUST** link to inputs:
  * P040 (`METHOD`, `SIM_RUN/INTERP`) and/or P030 (feasibility chain) as applicable.

---

### P060 — Product/Tool Quality & Conformity (CE)

#### Packages

* `PKG-P060-PRODUCT-CONFORMITY`
* `PKG-P060-TOOL-QUALITY`
* `PKG-P060-CE-TECH-FILE`
* `PKG-P060-RELEASE-TO-USE`
* `PKG-P060-NCR-DISPOSITION` (optional)

#### Atoms

* `PRODUCT_ITEM`, `TOOL_ITEM`
* `CE_DECL`, `TECH_FILE`, `CONFORMITY_ASSESS`, `TEST_EVIDENCE`, `CERTIFICATE`
* `CAL_CERT`, `QUAL_RECORD`, `TOOL_CONTROL_EVENT`
* `NCR`, `DISPOSITION`, `CLOSURE`

#### Normative Note (Coherence)

* **CE** typically applies to **tools/equipment/machinery/instrumentation**, not the complete "vehicle".
* For non-CE items, use `conformity_regime: SECTORIAL|INTERNAL` but maintain the same pattern of evidence + release.

---

### P070 — Flight Tests (CERT)

#### Packages

* `PKG-P070-TEST-CAMPAIGNS`
* `PKG-P070-TEST-CASES`
* `PKG-P070-REPORTS`
* `PKG-P070-NCR`

#### Atoms

* `TEST_CAMPAIGN`, `TEST_CASE`, `PROC_STEP`, `MEASUREMENT`
* `TEST_REPORT`, `DATA_LOG`, `NCR`

---

### P080 — In-Service + ICAs + MRO (line+shop+refurb+reuse) + occurrences/directives

#### Packages

* `PKG-P080-OPS-LOGS`
* `PKG-P080-ICA` (Instructions for Continued Airworthiness)
* `PKG-P080-MRO` (line+shop)
* `PKG-P080-REUSE` (reuse cycles/life limits)
* `PKG-P080-OCCURRENCE`
* `PKG-P080-DIRECTIVES`

#### Atoms (includes maintenance breakdown)

* Manual packages (tokenisable):
  * `PKG-AMM` (R/I, cleaning, inspection, calibration… down to steps)
  * `PKG-IPC` (installed parts figures/items)
  * `PKG-CMM` (component maintenance)
  * `PKG-IPL` (*IPC-like structure but for shop*)
* Procedural atoms: `ICA_TASK`, `MRO_JOB`, `STEP`, `CHECK`, `TOOL`, `LIMIT`, `WARN`, `CAUT`, `NOTE`, `VAR`
* Parts/catalogue atoms: `FIG`, `CALLOUT`, `ITEM`, `VAR`
* Occurrence/directives: `OCC_REPORT`, `ROOT_CAUSE`, `CORRECTIVE_ACTION`, `DIRECTIVE`, `COMPLIANCE_REC`

#### IPC vs IPL Rule (Fixed)

* **IPC**: `operation_context=LINE`, `asset_state=INSTALLED`
* **IPL (shop)**: `operation_context=SHOP`, `asset_state=REMOVED`
* If `domain=RSP` and reuse applies: `reuse_cycle_id=REQUIRED`

---

### P090 — Mission Ops & Traffic / Range Control

#### Packages

* `PKG-P090-MISSION-CONTROL`
* `PKG-P090-TRAFFIC-STM`
* `PKG-P090-ATM-UTM-INTERFACE`
* `PKG-P090-RANGE-COORD`
* `PKG-P090-CONSTRAINTS`

#### Atoms

* `MISSION_PLAN`, `MISSION_RULESET`
* `TRAFFIC_CLEARANCE` (slot/window/authorisation)
* `TRAJECTORY_PROFILE`, `CONSTRAINT`
* `RANGE_COORD_EVENT`, `CONTROL_ACTION`
* `ALERT`, `POST_MISSION_SUMMARY`

#### Minimum Links (Recommended)

* `TRAFFIC_CLEARANCE` → `MISSION_PLAN`
* `POST_MISSION_SUMMARY` → P080 logs and, if applicable, `OCC_REPORT`

---

### P100 — ESG Reporting & Transparency

#### Packages

* `PKG-P100-ESG-CONSOLIDATION`
* `PKG-P100-ESG-DISCLOSURE`
* `PKG-P100-AUDIT-TRAIL`

#### Atoms

* `ESG_REPORT`, `DISCLOSURE_ITEM`
* `AGG_RULE` (mandatory for aggregates)
* `AUDIT_EVIDENCE`

#### Hard Rule

* An `ESG_REPORT` **MUST** compile only:
  * `KPI_MEASURE` anchored to P030 (chain elements) and/or P080 (ops/mro events)
  * and declare `AGG_RULE` (method + inputs + boundary + period).

---

### P120 — Cyber & Resilience (Cross-cutting Layer)

#### Packages

* `PKG-P120-CYBER`
* `PKG-P120-RESILIENCE`

#### Atoms

* `CYB_CONTROL`, `THREAT`, `RISK_ASSESS`, `INCIDENT`, `MITIGATION`
* `RES_CONTROL`, `BCP_ITEM`, `RECOVERY_TEST`

**Rule:** any token in any phase may link to P120 controls.

---

## 7) Minimum Registries (for Studio Validation)

### 7.1 Phase Registry

```yaml
EACST_PHASE_REGISTRY:
  - phase: P000
    name: Registry & Governance
  - phase: P010
    name: Scope & Operational Context
  - phase: P020
    name: Safety & Risk Envelope
  - phase: P030
    name: Logistics & Industrial Chains
  - phase: P040
    name: Numerical & Simulation Methods (DMU+PMU)
  - phase: P050
    name: Design Office Authority (DOA sign)
  - phase: P060
    name: Product/Tool Quality & Conformity (CE)
  - phase: P070
    name: Flight Tests (CERT)
  - phase: P080
    name: In-Service + ICAs + MRO (incl shop/refurb/reuse)
  - phase: P090
    name: Mission Ops & Traffic / Range Control
  - phase: P100
    name: ESG Reporting & Transparency
  - phase: P110
    name: RESERVED
  - phase: P120
    name: Cyber & Resilience (Cross-cutting)
```

### 7.2 Package Registry (Extract with Key Rules)

```yaml
EACST_PACKAGE_REGISTRY:
  - package_id: PKG-P030-ESG-OVERLAY
    phase: P030
    unit_token_types: [KPI_DEF, KPI_MEASURE, OBJ, AGG_RULE, EVIDENCE]
    required_links:
      KPI_MEASURE:
        - { rel: measured_on, target_types: [CHAIN_NODE, CHAIN_EDGE, PROCESS, CHAIN] }

  - package_id: PKG-P040-METHODS
    phase: P040
    unit_token_types: [METHOD, MODEL_SPEC, VALIDATION_CASE, SIM_RUN, RESULT, INTERP]

  - package_id: PKG-P050-DOA-SIGNOFF
    phase: P050
    unit_token_types: [DOA_SIGN, FINDING, CLOSURE, COMPLIANCE_ITEM]
    required_links:
      DOA_SIGN:
        - { rel: supports, target_phase: P040 }

  - package_id: PKG-P060-TOOL-QUALITY
    phase: P060
    unit_token_types: [TOOL_ITEM, CAL_CERT, QUAL_RECORD, TOOL_CONTROL_EVENT]
    required_links:
      TOOL_ITEM:
        - { rel: supports, target_types: [CAL_CERT] }

  - package_id: PKG-P080-ICA
    phase: P080
    unit_token_types: [ICA_TASK, STEP, WARN, CAUT, NOTE, CHECK, TOOL, LIMIT, VAR]

  - package_id: PKG-P090-MISSION-CONTROL
    phase: P090
    unit_token_types: [MISSION_PLAN, MISSION_RULESET, CONTROL_ACTION, POST_MISSION_SUMMARY]

  - package_id: PKG-P100-ESG-CONSOLIDATION
    phase: P100
    unit_token_types: [ESG_REPORT, AGG_RULE, AUDIT_EVIDENCE]
    required_links:
      ESG_REPORT:
        - { rel: supports, target_phases: [P030, P080] }

  - package_id: PKG-P120-CYBER
    phase: P120
    unit_token_types: [CYB_CONTROL, THREAT, RISK_ASSESS, INCIDENT, MITIGATION]
```

---

## 8) Minimum Examples

### 8.1 KPI Measured on Chain (P030)

```yaml
token:
  token_id: "KPI_MEASURE-CO2e-SUP-A-2026Q1"
  token_type: "KPI_MEASURE"
  phase: "P030"
  package_id: "PKG-P030-ESG-OVERLAY"
  subpackage_id: "SUBPKG-CHAIN-SC-MEASURE"
  aor_id: "AOR-000123"
  version: "1.0.0"
  checksum: "sha3-512:..."
  bindings:
    domain: "DUAL"
    operation_context: "LINE"
    asset_state: "AS_BUILT"
    effectivity: ["ALL"]
    variants: []
  links:
    - rel: "measured_on"
      target_token_id: "CHAIN_NODE-SUPPLIER-A"
  metadata:
    kpi_id: "KPI-CO2e"
    period: {from: "2026-01-01", to: "2026-03-31"}
    value: 12.4
    unit: "tCO2e"
```

### 8.2 IPL Shop (IPC-like but Shop) within P080

```yaml
token:
  token_id: "FIG-IPL-SHOP-VALVE-EXPLODED-001"
  token_type: "FIG"
  phase: "P080"
  package_id: "PKG-IPL"
  subpackage_id: "SUBPKG-IPL-ShopBreakdownFigures"
  aor_id: "AOR-000777"
  version: "1.0.0"
  checksum: "sha3-512:..."
  bindings:
    domain: "RSP"
    operation_context: "SHOP"
    asset_state: "REMOVED"
    reuse_cycle_id: "RC-2026-03"
    effectivity: ["ALL"]
    variants: []
  children: ["ITEM-001", "ITEM-002", "VAR-EFF-A"]
```
