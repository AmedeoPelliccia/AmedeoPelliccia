# Federated Query Relaxation Policy — Contract Spec v1.0

**AMPEL360 Federated Architecture — Federated Contract Stabilization (B)**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL360-FED-QRP-001 |
| **Version** | v1.0 |
| **Status** | Normative Contract — Federated Architecture |
| **Parent** | ESSA-DOC-AMPEL360-FED-001 |
| **Authority Matrix** | [`../federation/authority_matrix.v1.1.md`](../federation/authority_matrix.v1.1.md) |
| **Machine-readable** | [`relaxation_policy.v1.0.yaml`](relaxation_policy.v1.0.yaml) |
| **Last Updated** | 2026-03-01 |

---

## Core Principle

> **Hard filters never relax. Soft filters relax in defined order. Every relaxation is explicit and annotated.**
>
> The relaxation policy answers: *what does the engine do when a valid, authority-resolved query returns zero results?*
> The answer is never "silently expand scope."
> Every scope change is a declared relaxation step, carried in the result payload.

---

## B.1 Filter Classes

### Hard Filters — Never Relaxed Automatically

A hard-filtered tag **must** be present and **must** match. If no records match, the engine returns `H_EXCEPTION(empty_result)` with the failing tag named. The scope is **never** widened automatically.

| Tag | Rationale |
|-----|-----------|
| `oem_id` | Cross-OEM results are always wrong. An Airbus AMM cannot be applied to a Boeing aircraft. |
| `model_id` | Cross-model results risk procedural errors (e.g. A320ceo vs A320neo task numbering). |
| `type_design_ref` | Technical baseline without a TC anchor is unverifiable. |
| `tenant_scope` | ACL boundary — never crossed regardless of result set. Multi-tenant isolation is absolute. |

### Soft Filters — Relaxable with Ordered Policy

A soft-filtered tag is applied when present. If it matches nothing, the relaxation ladder (§B.2) is applied **in order**. The result is always annotated with the relaxation step applied.

| Tag | Relaxation Permitted |
|-----|---------------------|
| `operator_id` | Yes — relax from operator-specific to OEM generic (A0/A3 sourced only) |
| `operator_regime` | Yes — relax from exact match to **compatible** only; never to conflicting regime |
| `effectivity` | Yes — widen from tail-specific to model-wide **with applicability warning** |
| `as_maintained_config` | Yes (Technical Publications only) — degrade to as-delivered baseline if post-SB content unavailable |

---

## B.2 Relaxation Ladder — Deterministic

When a query returns **zero results**, apply the following ladder in strict order. At each step, stop and return if results are found. **Never skip a step; never apply two relaxations simultaneously unless explicitly stated.**

```
PRECONDITION:  oem_id (HARD) and model_id (HARD) already matched.
               tenant_scope (HARD) already applied.
               Query has returned 0 results.

STEP 1 — Operator-Specific Query (baseline)
  Filter: operator_id (exact) + operator_regime (exact) + effectivity (tail-specific)
  Authority: any (A0/A1/A2/A3)
  On match:  RETURN  match_level=EXACT
  On zero:   proceed to Step 2

STEP 2 — Relax operator_id to OEM/MRO generic
  Filter: NO operator_id filter
  Authority constraint: A0 (OEM) or A3 (MRO) sourced documents ONLY
                        (A2 operator-specific docs excluded at this step)
  ACL:    current tenant_scope still applies
  On match:  RETURN  match_level=RELAXED_OPERATOR
             Annotate: why_returned=["operator_id relaxed to OEM/MRO generic"]
  On zero:   proceed to Step 3

STEP 3 — Relax operator_regime to compatible (not conflicting)
  Define compatible regimes:
    EASA-compatible: [EASA, UKCAA]          # UK CAA accepted for EASA operators post-Brexit
    FAA-compatible:  [FAA, TCCA]            # TCCA bilateral with FAA
    Conflicting:     EASA-sourced docs NEVER returned for FAA-only query (and vice versa)
  Filter: operator_regime IN compatible_set
  On match:  RETURN  match_level=RELAXED_REGIME
             Annotate: why_returned=["regime relaxed to compatible set: <set>"]
             applicability_risk=MED
  On zero:   proceed to Step 4

STEP 4 — Relax effectivity from tail-specific to model-wide (with warning)
  Filter: effectivity.scope IN [MODEL_WIDE, MODEL_FAMILY_WIDE]
  On match:  RETURN  match_level=RELAXED_EFFECTIVITY
             Annotate: why_returned=["effectivity widened from tail-specific to model-wide"]
             applicability_risk=HIGH
             FORCE applicability_banner=true in result payload
             (Banner text: "Document applicability not confirmed for MSN <msn>. Engineer review required.")
  On zero:   proceed to Step 5

STEP 5 — No compliant evidence
  Do NOT widen oem_id or model_id (hard stop).
  Do NOT cross tenant_scope (hard stop).
  RETURN  H_EXCEPTION(no_compliant_evidence)
  Include in exception payload:
    - failing_tag: the tag that returned zero at each step
    - steps_applied: list of relaxation steps attempted
    - suggested_remediation: (e.g. "Check if SB is embodied", "Verify operator regime", "Request OEM generic docs")
```

---

## B.3 Output Obligations — Explainability

Every item returned by a federated query **MUST** include the following fields in its result payload. These prevent silent cross-fleet contamination.

| Field | Type | Description |
|-------|------|-------------|
| `match_level` | enum | `EXACT` / `RELAXED_OPERATOR` / `RELAXED_REGIME` / `RELAXED_EFFECTIVITY` |
| `authority_class` | enum | `A0` / `A1` / `A2` / `A3` — authority class of the returned document |
| `why_returned` | list of string | Ordered list of relaxations applied to retrieve this result |
| `applicability_risk` | enum | `LOW` (EXACT match) / `MED` (regime relaxed) / `HIGH` (effectivity widened) |
| `applicability_banner` | boolean | `true` if `match_level == RELAXED_EFFECTIVITY` — forces UI banner |
| `tenant_scope_applied` | string | The ACL boundary that was active for this query |
| `authority_assertions` | object | `{ oem_id, model_id, operator_id, operator_regime }` as resolved and used |

### Output Payload Example

```json
{
  "document_ref": "AMM-A321-28-10-00-001",
  "match_level": "RELAXED_OPERATOR",
  "authority_class": "A0",
  "why_returned": ["operator_id relaxed to OEM/MRO generic at Step 2"],
  "applicability_risk": "LOW",
  "applicability_banner": false,
  "tenant_scope_applied": "operator:icao:BAW",
  "authority_assertions": {
    "oem_id": "oem:airbus",
    "model_id": "ac_model:airbus:a321neo",
    "operator_id": "relaxed:OEM_GENERIC",
    "operator_regime": "EASA"
  },
  "provenance": {
    "asserted_by": { "authority_class": "A0", "system_id": "airbus-world-portal" },
    "asserted_at": "2026-01-15T08:00:00Z",
    "confidence": 1.0,
    "evidence_ref": "TC:EASA.A.064"
  }
}
```

---

## B.4 Per-IA-Mode Relaxation Rules

| IA Mode | `oem_id` | `model_id` | `operator_id` | `operator_regime` | `effectivity` | Max Step |
|---------|----------|------------|---------------|-------------------|---------------|----------|
| **Technical Publications** | HARD | HARD | SOFT (Step 2) | SOFT (Step 3) | SOFT (Step 4) | Step 4 |
| **Compliance / Lease** | HARD | HARD | HARD (no relax) | HARD (no relax) | SOFT (Step 4 with HIGH risk banner) | Step 4 only via explicit opt-in |
| **Fleet Management** | HARD | HARD | SOFT multi-operator (portfolio scope only) | SOFT (Step 3) | SOFT (Step 4) | Step 4 |

**Compliance / Lease mode note:** `operator_id` and `operator_regime` are **HARD** in this mode because regulatory compliance findings are specific to the operator's AOC jurisdiction. Cross-operator or cross-regime compliance documents are structurally invalid. An engineer must explicitly opt in before `effectivity` relaxation is applied, and the result carries `applicability_risk=HIGH` unconditionally.

---

## B.5 Multi-Tenant Isolation — Absolute Boundary

The `tenant_scope` tag is a hard filter that **never** participates in the relaxation ladder. It is applied before step 1 and remains active through all relaxation steps.

```
GIVEN  tenant = operator:icao:BAW

ALL steps apply WITHIN tenant scope.
Step 2 (OEM generic) still filters to:
  records accessible to tenant:BAW (A0/A3 docs in BAW's licensed access scope)
  NOT: records from tenant:RYR even if they are A0/A3 sourced
```

**Lessor exception:** A lessor tenant (e.g. `operator:internal:LESSOR-001`) may have a declared portfolio `[BAW, AFR, TAP]`. In Fleet Management mode, the relaxation ladder applies across all portfolio members simultaneously. The tenant boundary is the portfolio declaration, not a single operator.

---

## B.6 Inhibitors (Relaxation Enforcement)

| ID | Condition | Action |
|----|-----------|--------|
| **QRP-INH-001** | Relaxation step attempts to cross `tenant_scope` boundary | **FAIL** — absolute stop; H_EXCEPTION(acl_boundary_violation) |
| **QRP-INH-002** | Relaxation step attempts to widen `oem_id` or `model_id` | **FAIL** — hard tag relaxation never permitted |
| **QRP-INH-003** | Step 3 returns `operator_regime` that is in conflicting set | **FAIL** — conflicting regime docs blocked; only compatible set permitted |
| **QRP-INH-004** | Step 4 result returned without `applicability_banner = true` | **FAIL** — banner is mandatory for effectivity-relaxed results |
| **QRP-INH-005** | Result payload missing `match_level`, `authority_class`, or `why_returned` | **FAIL** — incomplete result; do not surface to user |
| **QRP-INH-006** | Compliance/Lease mode attempts operator_id relaxation without explicit engineer opt-in | **FAIL** — hard stop; return H_EXCEPTION(no_compliant_evidence) |

---

## B.7 Relationship to Authority Matrix

This policy defines **what to do when hard-filtered queries fail**. The filter mode for each tag per IA Mode is derived from the authority classes defined in the Authority Matrix (`federation/authority_matrix.v1.1.md`). The two documents together form the complete federated query contract.

| Component | Answers |
|-----------|---------|
| Authority Matrix (A) | Who asserts each tag; what is authoritative; what conflicts mean |
| Relaxation Policy (B) | What happens when a valid query returns zero; how scope degrades; what the result must declare |
