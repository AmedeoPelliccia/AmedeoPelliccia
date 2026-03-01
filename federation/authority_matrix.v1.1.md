# Global Tag Authority Matrix — Contract Spec v1.1

**AMPEL360 Federated Architecture — Federated Contract Stabilization (A)**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL360-FED-AUTH-001 |
| **Version** | v1.1 |
| **Status** | Normative Contract — Federated Architecture |
| **Parent** | ESSA-DOC-AMPEL360-FED-001 |
| **Schema** | [`../schemas/global_tags.v1.schema.json`](../schemas/global_tags.v1.schema.json) |
| **Machine-readable** | [`authority_matrix.v1.1.yaml`](authority_matrix.v1.1.yaml) |
| **Supersedes** | ESSA-DOC-AMPEL360-FED-AUTH-001 v0.1-draft |
| **Last Updated** | 2026-03-01 |

---

## Design Correction from v0.1

> **v0.1 error:** `oem_id` and `model_id` were described as "hard-coded to tail."
>
> **v1.1 correction:** OEM and Model are **type design anchors**, not tail anchors.
> The tail (MSN / registration) binds to the structural tags via the **effectivity mapping**.
> `msn` and `registration` live in the structural block but are owned by A0 / A1 respectively.
> This distinction is critical: an OEM document applies to a *type*, not to a *tail* —
> until effectivity resolution maps the type applicability to the specific MSN.

---

## A.1 Canonical Global Tag Attributes

### Structural (Quasi-Immutable) — Type Design Anchors

| Field | Description | Authority | Immutable |
|-------|-------------|-----------|-----------|
| `oem_id` | OEM namespace identifier. `oem:airbus`, `oem:boeing` | **A0** | Yes |
| `model_id` | OEM type certificate designator. `ac_model:airbus:a321neo` | **A0** | Yes |
| `type_design_ref` | TC / TC-holder reference. Mandatory for technical baseline publication | **A0** (validated: A1) | Yes |
| `msn` | Manufacturer Serial Number — primary permanence key | **A0** | Yes |
| `registration` | Current tail registration — changes on transfer | **A1** | No |
| `model_alias` | Operator alias for model. Cannot redefine `model_id` | **A2** | No |

### Temporal Overlay — Time-Bound to AOC / Ownership Windows

| Field | Description | Authority | Immutable |
|-------|-------------|-----------|-----------|
| `operator_id` | AOC holder. `operator:icao:BAW` · `operator:iata:BA` · `operator:internal:<id>` | **A1** | No |
| `operator_temporal_window` | `{ valid_from, valid_to (null=active), transfer_event_ref }` | **A1** | No |
| `operator_regime` | `EASA` / `FAA` / `UKCAA` / `TCCA` / `CASA` / `ANAC` / `OTHER` | **A2** (validated: A1) | No |
| `operator_regime_window` | Temporal window for regime (required if operator can change) | **A1** | No |

### Config-Realisation — Stateful (SB / EO Embodiment)

| Field | Description | Authority | Immutable |
|-------|-------------|-----------|-----------|
| `as_delivered_config` | Delivery baseline. `config:oem:airbus:baseline-A321-R01` | **A0** | Yes |
| `as_maintained_config` | Current SB/EO state. `config:mro:<site>:<config_id>` | **A3** | No |
| `config_embodied` | Boolean — MRO confirmed embodiment | **A3** | No |
| `config_embodiment_date` | ISO 8601 date of A3 confirmation | **A3** | No |
| `effectivity` | MSN / tail / line-number applicability scope. Computed jointly | **A0 + A3** | No |

---

## A.2 Authority Class Definitions

| Class | Name | Scope | Examples |
|-------|------|-------|---------|
| **A0** | Type Design Authority | TC holder / OEM authoritative packet | Airbus World portal, Boeing Toolbox, OEM type cert |
| **A1** | Regulatory Registry | Civil registry / AOC validation | EASA EDOM, FAA DRS, national aircraft register |
| **A2** | Operator Authority | Operator manuals, procedures, AMP deltas | Airline ops engineering, operator AMP, lessee docs |
| **A3** | Maintainer Authority | MRO embodied config / work packages / RTS | AMOS, TRAX, OASES; maintenance work orders |

---

## A.3 Authority Matrix

| Attribute | Master Authority | Validators | Conflict Rule (deterministic) |
|-----------|-----------------|------------|-------------------------------|
| `oem_id` | **A0** Type Design | A1 | **Immutable.** Once set for asset family: if mismatch → **FAIL** (data integrity breach). |
| `model_id` | **A0** Type Design | A1, A2 | A0 wins. A2 may add `model_alias` but **cannot redefine** `model_id`. |
| `type_design_ref` | **A0** Type Design | A1 | Mandatory for publication of technical baseline. Absence blocks CONFIRM gate. |
| `operator_id` | **A1** Registry/AOC | A2, Lessor | **Temporal overlay** — valid only within `[valid_from, valid_to)`. Overlaps → **FAIL** unless explicitly multi-operator (rare, requires `H_SIGNOFF`). |
| `operator_regime` | **A2** Operator | A1 | Must be consistent with AOC/jurisdiction. Mismatch → **WARN** (DAL C/D) / **FAIL** (DAL A/B) by policy. |
| `as_maintained_config` | **A3** MRO / Continuing Airworthiness | A2, A0 | For embodied state, **A3 overrides** A0 "standard" baseline. Requires evidence link (EO/SB/WP). |
| `effectivity` | **A0 + A3** (computed) | A2 | A0 defines applicability rules; A3 defines current MSN state; A2 can **narrow** (operator procedures) but **never widen** beyond A0 bounds. |

---

## A.4 Qualified Namespace Scheme

All tag values **MUST** be expressed as qualified namespaces to prevent cross-system collisions.

### Namespace Prefixes

| Tag | Namespace Pattern | Examples |
|-----|------------------|---------|
| `oem_id` | `oem:<name>` | `oem:airbus`, `oem:boeing`, `oem:embraer` |
| `model_id` | `ac_model:<oem>:<type>` | `ac_model:airbus:a321neo`, `ac_model:boeing:737max8` |
| `type_design_ref` | `TC:<authority>.<ref>` | `TC:EASA.A.064`, `TC:FAA.A16WE` |
| `operator_id` | `operator:icao:<code>` or `operator:iata:<code>` or `operator:internal:<id>` | `operator:icao:BAW`, `operator:internal:LESSOR-001` |
| `operator procedures` | `proc:operator:<opid>:<proc_id>` | `proc:operator:BAW:PROC-7701` |
| `as_maintained_config` | `config:mro:<site>:<config_id>` | `config:mro:heathrow:SB-A321-28-1234-R02` |
| `as_delivered_config` | `config:oem:<oem>:<baseline_id>` | `config:oem:airbus:A321-STD-R01` |

### Namespace Resolution Rule

```
GIVEN  query_tag = "A321neo"          # unqualified

RESOLVE:
  1. Is value qualified (contains ':')?  No → proceed to resolution
  2. Look up in OEM type registry
     → resolves to "ac_model:airbus:a321neo"
  3. If ambiguous (multiple OEMs match) → H_EXCEPTION(ambiguous_tag); ABORT
  4. If not found in registry → H_EXCEPTION(unresolvable_tag); ABORT

RULE: Never pass unqualified tag to downstream search or index filter.
```

### Cross-System Namespace Isolation

- `proc:operator:BAW:PROC-7701` is **never** cross-resolved to `proc:operator:RYR:PROC-7701`
- Operator-scope identifiers are always contained within their authority boundary
- Lessor-scope aggregation is bounded to declared portfolio members only

---

## A.5 Mandatory Provenance Fields

Every tag assertion **MUST** carry these fields. Without them the assertion is rejected at the INTERPRET gate.

| Field | Type | Description |
|-------|------|-------------|
| `asserted_by.authority_class` | `A0` / `A1` / `A2` / `A3` | Authority class of the asserting system |
| `asserted_by.system_id` | string | Identifier of the asserting system |
| `asserted_at` | ISO 8601 datetime | Timestamp of assertion |
| `confidence` | float 0–1 | 1.0 = authoritative primary source; <0.7 triggers `H_EXCEPTION` warning |
| `evidence_ref` | string | Registry entry, TC reference, work order, or `H_EVIDENCE` ID |

**Provenance example:**

```json
{
  "asserted_by": { "authority_class": "A3", "system_id": "amos-heathrow-01" },
  "asserted_at": "2026-02-28T10:30:00Z",
  "confidence": 1.0,
  "evidence_ref": "H-EV-BAW-WO-20260228-0041"
}
```

---

## A.6 Inhibitors (Authority Matrix Enforcement)

| ID | Condition | Gate | Action |
|----|-----------|------|--------|
| **AUTH-INH-001** | `oem_id` assertion from class other than A0 | INTERPRET | **FAIL** — reject and raise `H_EXCEPTION(unauthorised_oem_assertion)` |
| **AUTH-INH-002** | `model_id` redefinition attempt by A2 | INTERPRET | **FAIL** — reject; A2 may only submit `model_alias` |
| **AUTH-INH-003** | `type_design_ref` absent on technical baseline publication | CONFIRM | **FAIL** — block CONFIRM gate |
| **AUTH-INH-004** | `operator_id` temporal windows overlap without `H_SIGNOFF` resolution | CONFIRM | **FAIL** — block until transfer event resolved |
| **AUTH-INH-005** | `operator_regime` inconsistent with AOC jurisdiction (DAL A/B) | CONFIRM | **FAIL**; DAL C/D = **WARN** |
| **AUTH-INH-006** | `as_maintained_config` asserted without `evidence_ref` | ACTIVATE | **FAIL** — config not trusted without maintenance evidence |
| **AUTH-INH-007** | `effectivity` widened by A2 beyond A0 applicability bounds | ACTIVATE | **FAIL** — A2 may only narrow, not widen |
| **AUTH-INH-008** | Any tag assertion with `confidence` < 0.7 | INTERPRET | `H_EXCEPTION(low_confidence)`; human review required before CONFIRM |
| **AUTH-INH-009** | Any tag assertion missing provenance fields | INTERPRET | **FAIL** — assertion rejected entirely |

---

## A.7 Relationship to Relaxation Policy

This matrix defines **what is authoritative**. The Federated Query Relaxation Policy (`rag/relaxation_policy.v1.0.md`) defines **what happens when a hard-filtered query returns no results** — including which tags may be relaxed, in what order, and what output obligations apply.

Cross-reference: [`../rag/relaxation_policy.v1.0.md`](../rag/relaxation_policy.v1.0.md)
