# AMPEL360 Federated Contract — Global Tag Authority Matrix

**AMPEL360 — Federated Contract Stabilization: Identity Authority, Temporal Binding, Query Determinism**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL360-FED-AUTH-001 |
| **Version** | v1.1 |
| **Status** | Normative Contract — Federated Architecture |
| **Parent** | ESSA-DOC-AMPEL360-FED-001 ([AMPEL360-FED.md](AMPEL360-FED.md)) |
| **Companion** | [`ampel360-fed-auth.yaml`](ampel360-fed-auth.yaml) |
| **Contract spec** | [`../federation/authority_matrix.v1.1.md`](../federation/authority_matrix.v1.1.md) · [`../federation/authority_matrix.v1.1.yaml`](../federation/authority_matrix.v1.1.yaml) |
| **Schema** | [`../schemas/global_tags.v1.schema.json`](../schemas/global_tags.v1.schema.json) |
| **Related** | [`AMPEL360-FED.md`](AMPEL360-FED.md) · [`H-PIPELINE.md`](H-PIPELINE.md) · [`AMPEL360-Q100.md`](AMPEL360-Q100.md) |
| **Domain** | Civil Aviation — Federated Fleet Data Governance |
| **Regulatory Authority** | EASA / FAA (dual-authority) |
| **Last Updated** | 2026-03-01 |

---

## Design Correction from v0.1

> **v0.1 error:** `oem_id` and `model_id` were described as "hard-coded to tail."
>
> **v1.1 correction:** OEM and Model are **type design anchors**, not tail anchors.
> The tail (MSN / registration) binds to the structural tags via **effectivity mapping**.
> `msn` and `registration` live in the structural block but are owned by A0 / A1 respectively.
>
> This distinction is critical: an OEM document applies to a *type*, not to a *tail* —
> until effectivity resolution maps the type applicability to the specific MSN.

---

## Core Principle

> **Resolve authority before resolving data.**
>
> Without a defined authority hierarchy, federated tag assertions from OEM portals,
> MRO systems, and operator databases will collide silently.
> This document establishes who is authoritative for each tag, when, and at what scope —
> before any data is ingested or any RAG query is executed.

The federated contract stabilizes at four pillars:
1. **Global Tag Authority Matrix** — who asserts what, and with what precedence
2. **Qualified Namespace Scheme** — how assertions are scoped to prevent cross-system collision
3. **Temporal Binding Model** — how asset identity and configuration state are time-bound
4. **Query Determinism Policy** — hard vs. soft filter rules per IA Mode

---

## 1. Identity Authority Model

Three systems assert Global Tags in a federation. Each has a different claim scope.

Four authority classes govern all assertions (A0–A3):

| Class | Name | Scope | Examples |
|-------|------|-------|---------|
| **A0** | Type Design Authority | TC holder / OEM authoritative packet | Airbus World portal, Boeing Toolbox, OEM type certificate |
| **A1** | Regulatory Registry | Civil registry / AOC validation | EASA EDOM, FAA DRS, national aircraft register |
| **A2** | Operator Authority | Operator manuals, procedures, AMP deltas | Airline ops engineering, operator AMP, lessee docs |
| **A3** | Maintainer Authority | MRO embodied config / work packages / RTS | AMOS, TRAX, OASES, maintenance work orders |

| Source System | Claims Authority Over | Claim Type | Authority Class |
|--------------|----------------------|------------|----------------|
| **OEM Portal / Type Certificate** | `oem_id`, `model_id`, `type_design_ref`, `msn`, `as_delivered_config`, `effectivity` (applicability rules) | Structural — type design anchor, bound to asset family | **A0** |
| **Registry (FAA / EASA)** | `oem_id`, `model_id`, `type_design_ref`, `registration`, `regulatory_authority` | Validation — confirms A0 against certificated type | **A1** |
| **AOC Holder (Operator)** | `operator_id`, `operator_regime`, `model_alias` | Temporal — valid only within ownership/operation window | **A1** (operator_id), **A2** (regime/alias) |
| **Lessor Portfolio System** | `operator_id` (portfolio group scope) | Portfolio — aggregates operator windows; never overrides OEM or AOC holder | **A2** |
| **MRO Maintenance System** | `as_maintained_config`, `config_embodied`, `effectivity` (current state) | Embodiment state — current SB/EO incorporation against MSN | **A3** |
| **Engineering Orders (EO)** | `as_maintained_config` (proposed) | Proposed state — pre-embodiment; subordinate to A3 embodied state | **A3** (proposed) |

**Key constraint:** No downstream system (Operator, Lessor, MRO) may reassert `oem_id`, `model_id`, or `type_design_ref`. These are structurally anchored to the type certificate and asset family, not to the tail.

---

## 2. Global Tag Authority Matrix

The Authority Matrix defines, for each Global Tag, the primary authority, secondary validation source, and conflict resolution rule. This is the **contract-grade v1.1** table.

**Structural (quasi-immutable) — type design anchors:**

| Tag | Field Name | Primary Authority | Secondary Authority | Conflict Resolution |
|-----|-----------|------------------|--------------------|--------------------|
| **OEM** | `oem_id` | **A0** OEM Portal / Type Certificate | A1 Registry | **Immutable.** Once set for asset family. Mismatch → **FAIL** (data integrity breach). |
| **Model** | `model_id` | **A0** Type Certificate | A1 Registry, A2 (alias only) | A0 wins always. A2 may add `model_alias` but **cannot redefine** `model_id`. |
| **Type Design Ref** | `type_design_ref` | **A0** Type Certificate | A1 Registry | Mandatory for technical baseline publication. Absence blocks CONFIRM gate. |
| **MSN** | `msn` | **A0** OEM | — | Permanent key. Never changed. |
| **Registration** | `registration` | **A1** Registry | — | Mutable; changes with operator/jurisdiction transfer. |

**Temporal overlay — time-bound to AOC / ownership windows:**

| Tag | Field Name | Primary Authority | Secondary Authority | Conflict Resolution |
|-----|-----------|------------------|--------------------|--------------------|
| **Operator** | `operator_id` | **A1** AOC Holder (Registry) | A2, Lessor | **Temporal.** Valid within `[valid_from, valid_to)`. Overlaps → **FAIL** unless explicitly multi-operator with `H_SIGNOFF`. |
| **Regime** | `operator_regime` | **A2** Operator | A1 Registry | Must be consistent with AOC/jurisdiction. Mismatch → **FAIL** (DAL A/B) / **WARN** (DAL C/D). |

**Config-realisation (stateful):**

| Tag | Field Name | Primary Authority | Secondary Authority | Conflict Resolution |
|-----|-----------|------------------|--------------------|--------------------|
| **As-Delivered Config** | `as_delivered_config` | **A0** OEM | — | Delivery baseline. Immutable. |
| **As-Maintained Config** | `as_maintained_config` | **A3** MRO / Continuing Airworthiness | A2, A0 | A3 embodied state **overrides** A0 standard. Requires `evidence_ref` (EO/SB/WP). |
| **Effectivity** | `effectivity` | **A0 + A3** (computed) | A2 (narrows only) | A0 defines applicability rules; A3 defines current MSN state; A2 can **narrow** but **never widen** beyond A0 bounds. |

### 2.1 Authority Precedence Rule

```
Structural precedence:  oem_id  >  model_id  >  type_design_ref  >  operator_id  >  operator_regime  >  config realisation

Temporal override:      operator_id and operator_regime are the only tags subject to temporal override.
                        They cannot override oem_id, model_id, or type_design_ref at any point or scope.

Conflict rule:          If two systems assert conflicting values for the same tag,
                        the system ranked higher in structural precedence wins.
                        For operator_id conflicts, the currently-active AOC window wins.
```

**Rationale:** `oem_id` and `model_id` are fixed at the type certificate and MSN record. They are structurally upstream of any operational configuration. Allowing operators or lessors to assert or redefine them would break traceability to the certificated type — a safety-critical failure mode.

### 2.2 Conflict Detection Rules

| Rule ID | Conflict Scenario | Detection Point | Resolution |
|---------|------------------|-----------------|------------|
| **AUTH-CON-001** | Two systems assert different `oem_id` for same MSN | INTERPRET gate | OEM Portal assertion wins; Registry used for validation; `H_EXCEPTION` raised if mismatch |
| **AUTH-CON-002** | `model_id` in AMP differs from OEM TC designation | CONFIRM gate | OEM TC designation wins; AMP alias recorded as `H_CONSTRAINT` annotation only |
| **AUTH-CON-003** | Multiple `operator_id` assertions with overlapping time windows | CONFIRM gate | Chronologically latest AOC registration wins; overlap is flagged as `H_EXCEPTION` requiring `H_SIGNOFF` resolution |
| **AUTH-CON-004** | `config_id` from EO conflicts with MRO embodied state | ACTIVATE gate | MRO embodied state wins; EO recorded as pending — only promoted after embodiment confirmation |
| **AUTH-CON-005** | Lessor asserts `operator_id` outside valid portfolio window | CONFIRM gate | `H_EXCEPTION` raised; lessor claim rejected; current AOC holder assertion applied |

---

## 3. Qualified Namespace Scheme

To prevent tag collisions between systems using internal codes for the same entity, all Global Tag values **SHALL** be expressed as qualified namespaces:

```
Format:  [AUTHORITY_ID]:[VALUE]

Examples:
  oem_id:       AIRBUS:A321         (OEM-issued, globally unambiguous)
  model_id:     AIRBUS:A321neo      (OEM-issued type designator)
  operator_id:  BAW:UK-AOC-0001     (AOC holder designator, registry-confirmed)
  operator_id:  LESSOR-001:PORT-01  (Lessor portfolio grouping — sub-authority)
  config_id:    AMOS:SB-28-1234-R02 (MRO system identifier for embodied SB)
```

### 3.1 Namespace Resolution for RAG Queries

When the AMPEL-A7 RAG engine receives a query containing a Global Tag value, it **SHALL** resolve it through the following namespace hierarchy:

```
GIVEN  query_tag = "737-MAX8"

RESOLVE:
  1. Check if value is qualified:  "BOEING:737-MAX8"  →  use directly
  2. If unqualified:
       a. Look up in OEM registry → resolve to "BOEING:737-MAX8"
       b. If ambiguous (multiple OEMs have matching alias) → H_EXCEPTION (ambiguous tag)
       c. If not found → H_EXCEPTION (unresolvable tag)
  3. Apply resolved namespace to query filter

NEVER: pass unqualified tag to downstream search
```

### 3.2 Operator-Specific Namespace Isolation

Operator-internal codes (procedure numbers, fleet IDs, internal part numbers) are **always** scoped under their operator namespace and are **never** promoted to global scope:

```
Global scope  (cross-system visible):   AIRBUS:A321neo
Operator scope (isolated):              BAW:PROC-7701   (British Airways internal procedure)
Lessor scope  (portfolio-internal):     LESSOR-001:PORT-01

RAG rule:  A query in BAW context may resolve BAW:PROC-7701,
           but it CANNOT cross-resolve to RYR:PROC-7701 (different operator, same internal code).
```

---

## 4. Temporal Binding Model

Aircraft data is never static. Every Global Tag assertion that can change over time **MUST** carry temporal binding fields. Without these, the RAG engine will mix current and historical states, producing invalid results.

### 4.1 MSN / Tail Effectivity

The `oem_id` and `model_id` tags are structurally bound to the MSN (Manufacturer Serial Number) at manufacture. They do not carry `valid_from` / `valid_to` — they are permanent.

```yaml
structural_binding:
  msn:         "10001"           # Manufacturer Serial Number — permanent key
  oem_id:      "AIRBUS:A321"     # Immutable — set at manufacture
  model_id:    "AIRBUS:A321neo"  # Immutable — set at TC certification
  registration: "G-TTNE"        # Mutable — changes with operator/jurisdiction
```

### 4.2 Operator Temporal Window

The `operator_id` tag is temporally bounded. An operator's authority over a specific tail ends when the aircraft is transferred or leased to another operator.

```yaml
operator_window:
  msn:          "10001"
  operator_id:  "BAW:UK-AOC-0001"
  valid_from:   "2022-04-01T00:00:00Z"   # Delivery date / lease commencement
  valid_to:     null                      # null = currently active
  transfer_event: null                    # populated on transfer (H_UPDATE trigger)
```

**Query rule:** The RAG engine **SHALL** evaluate `valid_to` before applying any `operator_id` filter:
- `valid_to == null` → operator window is currently active; apply filter normally
- `valid_to < query_timestamp` → window is historical; query **SHALL NOT** use this operator assertion for current-state queries; it may be used for historical queries only

### 4.3 Configuration State (SB/EO Effectivity)

The `config_id` tag encodes the embodiment state of a Service Bulletin or Engineering Order against a specific MSN. A document tagged with `config_id = SB-28-1234-R02` is only applicable to tails where that SB is **embodied**.

```yaml
configuration_binding:
  msn:                   "10001"
  config_id:             "AMOS:SB-28-1234-R02"
  embodied:              true               # MRO confirmed embodiment
  embodiment_date:       "2024-09-15"
  pre_embodiment_state:  "AMOS:SB-28-1234-R01"  # Previous baseline
  h_evidence_ref:        "H-EV-BAW-0001"   # Linked MRO work order evidence
```

**Query rule:** Technical Publications and Compliance queries that depend on SB embodiment state **SHALL** filter on `embodied == true` for the relevant MSN before surfacing AMM task references that assume post-SB configuration.

### 4.4 Temporal Conflict Matrix

| Scenario | Detection | Action |
|----------|-----------|--------|
| Query asks for current operator but MSN has `valid_to` set | CONFIRM gate | Return `H_EXCEPTION` (stale operator assertion); escalate to `H_SIGNOFF` |
| Two operator windows overlap (no `valid_to` on predecessor) | CONFIRM gate | `H_EXCEPTION`; block until overlap resolved via transfer event |
| SB `embodied == false` but query assumes post-SB config | ACTIVATE gate | `H_EXCEPTION`; filter result to pre-SB documentation set only |
| MSN `valid_from` is in the future (pre-delivery) | INTERPRET gate | `H_CONSTRAINT` warning; flag as pre-delivery asset — operator queries blocked |

---

## 5. Query Determinism Policy

Before IA Mode selection, the federation contract defines whether each tag filter is **hard** (must match, no expansion) or **soft** (expand if empty, degrade gracefully).

### 5.1 Filter Mode Definitions

| Filter Mode | Behaviour | Failure Behaviour |
|-------------|-----------|-------------------|
| **HARD** | Tag must be present and must match — zero results otherwise | Return `H_EXCEPTION(empty_result)` — never expand scope |
| **SOFT** | Tag is used if present; if absent or unmatched, query expands to next scope level | Return results with `H_CONSTRAINT(scope_degraded)` annotation |
| **TEMPORAL_HARD** | Hard filter + temporal validity check — rejects historical assertions | Return `H_EXCEPTION(stale_tag)` |

### 5.2 Per-IA-Mode Filter Matrix

| Tag | Technical Publications Mode | Compliance / Lease Mode | Fleet Management Mode |
|-----|-----------------------------|-------------------------|-----------------------|
| `oem_id` | **HARD** | **HARD** | **HARD** |
| `model_id` | **HARD** | **HARD** | **HARD** |
| `operator_id` | **SOFT** (optional override) | **TEMPORAL_HARD** | **SOFT** (multi-operator aggregate) |
| `config_id` | **SOFT** (degrade to generic AMM if absent) | **HARD** (SB embodiment required for AD compliance) | **SOFT** |
| Temporal validity | Applied to `operator_id` only | Applied to `operator_id` + `config_id` | Applied to `operator_id`; historical states permitted for trend analysis |

### 5.3 Query Relaxation Cascade

When a SOFT filter finds no matching records at the primary operator scope, the engine applies a defined relaxation cascade **in order** — it does **not** silently expand:

```
Relaxation cascade for SOFT operator_id filter:

Step 1:  Query operator-specific records  (e.g. BAW:A321neo procedures)
         → if results found: RETURN (annotate with operator scope)

Step 2:  Query OEM generic records         (e.g. AIRBUS:A321neo base AMM)
         → if results found: RETURN with H_CONSTRAINT(scope=OEM_GENERIC) annotation

Step 3:  No results at either scope
         → RETURN H_EXCEPTION(no_matching_record) — never return cross-operator results
```

**Hard filter failure:** If a HARD filter returns no results, the engine **SHALL** return `H_EXCEPTION(empty_result)` with:
- The tag that failed to match
- The scope searched
- Suggested remediation (e.g., "Check if operator_id BAW:UK-AOC-0001 has valid_to set")

### 5.4 Cross-Operator Visibility Rules

| Context | Cross-Operator Visibility | Rationale |
|---------|--------------------------|-----------|
| Technical Publications query | **Not permitted** (SOFT degrades to OEM generic, never to other operator) | Operator AMM customisations are proprietary |
| Compliance / Lease query | **Strictly prohibited** (TEMPORAL_HARD on operator_id) | Regulatory environment differs per operator; cross-contamination is a compliance risk |
| Fleet Management query — lessor | **Permitted only within declared portfolio** (operator_id must be in lessor's registered portfolio) | Lessor has contractual right to aggregate across its own fleet |
| Fleet Management query — MRO | **Permitted only for declared work scope** (operator_id list declared in MRO contract scope) | MRO may access multiple operators but only within contracted scope |

---

## 6. RAG Engine Authority Resolution

The AMPEL-A7 RAG engine **SHALL** execute the following authority resolution sequence on every federated query before semantic search begins:

```
GIVEN  query = { oem_id, model_id, operator_id, config_id, ia_mode, query_timestamp }

STEP 1 — Tag Qualification
  For each tag in query:
    IF unqualified → resolve via namespace registry
    IF unresolvable → H_EXCEPTION(unresolvable_tag); ABORT

STEP 2 — Authority Validation
  Validate oem_id against OEM Portal / Registry
  Validate model_id consistency with oem_id (AUTH-CON-002)
  Validate operator_id temporal window (valid_from ≤ query_timestamp ≤ valid_to OR valid_to == null)
    IF expired → H_EXCEPTION(stale_operator); ABORT for current-state queries
  Validate config_id embodiment state against MRO (if present)

STEP 3 — Authority Precedence Application
  Apply structural precedence: oem_id > model_id > operator_id > config_id
  In any conflict: higher-precedence authority wins; H_EXCEPTION logged

STEP 4 — Filter Mode Application (per IA Mode, §5.2)
  Apply HARD / SOFT / TEMPORAL_HARD per tag per mode
  For SOFT with no match: apply relaxation cascade (§5.3)
  For HARD with no match: H_EXCEPTION(empty_result); ABORT

STEP 5 — Qualified Namespace Filter
  Filter index to records where:
    record.oem_id   == oem_id    (HARD)
    record.model_id == model_id  (HARD)
    record.operator_id matches filter mode (HARD/SOFT/TEMPORAL_HARD)
    record.config_id matches filter mode (if present)

STEP 6 — Semantic Similarity Ranking
  Apply semantic ranking within filtered set
  Return top-k results with:
    - H_EVIDENCE metadata (source, authority_id, revision, index_ts)
    - H_CONSTRAINT annotation (scope applied: operator / OEM_generic / portfolio)
    - Any H_EXCEPTION records from steps 1–5
```

---

## 7. Additional H-Pipeline Inhibitors (Authority-Specific)

| ID | Inhibitor | Condition | Blocked Operation |
|----|-----------|-----------|-------------------|
| **AUTH-INH-001** | `¬oem_id_validated` → BLOCKED | `oem_id` not confirmed by OEM Portal or Registry | All queries — structural tag missing |
| **AUTH-INH-002** | `model_id_oem_mismatch` → BLOCKED | `model_id` not consistent with declared `oem_id` authority chain | CONFIRM gate |
| **AUTH-INH-003** | `operator_id_temporal_expired` → BLOCKED | `operator_id` `valid_to` < `query_timestamp` for current-state queries | All current-state queries |
| **AUTH-INH-004** | `operator_window_overlap` → BLOCKED | Two active operator assertions for same MSN without resolved transfer event | CONFIRM gate (requires `H_SIGNOFF` to resolve) |
| **AUTH-INH-005** | `config_id_not_embodied` → BLOCKED | `config_id` required for compliance query but MRO status = not embodied | ACTIVATE gate for compliance records |
| **AUTH-INH-006** | `unqualified_namespace` → BLOCKED | Tag value not in `[AUTHORITY_ID]:[VALUE]` format after qualification step | INTERPRET gate |
| **AUTH-INH-007** | `cross_operator_visibility_prohibited` → BLOCKED | Query attempts to access another operator's records outside declared portfolio or MRO scope | All queries — hard isolation boundary |

---

## 8. Relationship to Constitutional Instruments

| Instrument | AUTH Role |
|------------|----------|
| **ESSA-CONST-001** | Satisfies CI-003 (Deterministic Gates) via hard filter rules and authority conflict resolution; CI-004 (Machine-Verifiable Conformance) via qualified namespace enforcement |
| **ESSA-DOC-AMPEL360-FED-001** | AUTH is the contract stabilization sub-component of FED; FED §2 Global Tags are governed by the authority matrix defined here |
| **ESSA-DOC-AMPEL360-Q100-001** | Q100 is the primary aviation domain profile; AUTH temporal binding rules apply directly to Q100 CS-25 compliance traceability |
| **ESSA-DOC-H-001** | Authority conflicts generate `H_EXCEPTION`; resolved conflicts generate `H_CONSTRAINT`; temporal transfers generate `H_UPDATE` |
| **ESSA-DOC-SF-001** | Safety-first: AUTH-INH-001 and AUTH-INH-007 enforce that no unvalidated or cross-contaminated data can enter the active `H_ENVELOPE` |
| **ESSA-STD-CCTLS-001** | Authority resolution maps to CCTLS INTERPRET (qualification) → CONFIRM (validation) → ACTIVATE (embodiment) → PUBLISH (sign-off) |

---

## 9. Next Structural Move — (B) Federated Query Relaxation Policy

This document defines the per-tag filter modes (§5) and the relaxation cascade stub (§5.3). The full **Federated Query Relaxation Policy** — covering the deterministic relaxation ladder, compatible-regime sets, per-IA-mode rules, output obligations, and hard-stop inhibitors — is defined in:

> **[`../rag/relaxation_policy.v1.0.md`](../rag/relaxation_policy.v1.0.md)** · [`../rag/relaxation_policy.v1.0.yaml`](../rag/relaxation_policy.v1.0.yaml)
> Document ID: **ESSA-DOC-AMPEL360-FED-QRP-001 v1.0**

The contract-grade authority matrix (v1.1) and the relaxation policy (v1.0) together form the complete federated query contract. Neither document is sufficient alone:
- The authority matrix answers: *who asserts what, and what is authoritative*
- The relaxation policy answers: *what happens when a valid query returns zero results*
