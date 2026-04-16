---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-07
principle: Accountability
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "simplex-contract.yaml execution model"
---

# ETH-07 — Accountability

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[6]`

---

## 1. Principle

All AI artefacts are traceable through the PATH → MTL governance pipeline with immutable audit trails.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| simplex-contract.yaml execution model | Deterministic governance pipeline with evidence gating |

## 3. Implementation

- Every AI model, dataset, and inference result is registered in the PATH → MTL governance pipeline.
- Immutable audit trails record all training, evaluation, and deployment events.
- All access to model artefacts and training infrastructure is logged (ISO 27001 Annex A.12).
- Contributor attribution is tracked through the Capillary Merit Index (CMI).

## 4. Verification

- Audit trail integrity verified at each milestone gate.
- Full traceability from training data through to deployment output.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [simplex-contract.yaml](../simplex-contract.yaml) · [ethics-and-security.yaml](ethics-and-security.yaml)
