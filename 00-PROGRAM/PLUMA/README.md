# 00-PROGRAM/PLUMA/README.md
# Governance Kernel — PLUMA / OPT-IN Backend Logic
#
# This directory contains the executable governance layer:
# machine-enforceable contracts, invariants, and evidence-gated
# state machines that PLUMA validators run against.
#
# Structure:
#   simplex-contract.yaml       — Simplex classification, state machine, invariants
#   contributions-registry.yaml — Backend-auditable contributions classification
#   03-CAX_PHASES/              — CAx phase artifacts linked by run_manifest_ref

## Contents

| File | Purpose |
|------|---------|
| `simplex-contract.yaml` | Classification states, transitions (monotone + rollback), deterministic invariants (INV-001–003), execution model with validator rules, gating conditions with evidence provenance |
| `contributions-registry.yaml` | 5 contribution domains (CONTRIB-001–005) with Nature, Assets, Maturity, Externality, Risk dimensions and value assessment matrix |
| `03-CAX_PHASES/` | CAx phase artifacts referenced by `run_manifest_ref` in gating conditions |

## Invariants Enforced

1. **INV-001** — No certification claim may reference anything outside `K_full(t)`
2. **INV-002** — State transitions must be monotone unless a regulatory rollback event is recorded (requires `regulatory_event_id` + `signed_approval`)
3. **INV-003** — Every gate requires `evidence_refs[]`, `approvals[]`, and `run_manifest_ref` before closing

## Execution Model

```
MIXED ──(moc_pkg)──▶ CONDITIONAL ──(evidence_approved)──▶ FULL
  │                         │
  ├──(refine)───────────────┘
  └──(refine)──▶ INADMISSIBLE

        CONDITIONAL ──(evidence_fail)──▶ REJECTED

Rollbacks (require regulatory_event_id + signed_approval):
  FULL ──(regulatory_rollback)──▶ CONDITIONAL
  CONDITIONAL ──(regulatory_rollback)──▶ MIXED
```

## Reference

- Root README.md §10–§15
- Schema version: simplex-contract.yaml `schema_version: "2.0.0"`
