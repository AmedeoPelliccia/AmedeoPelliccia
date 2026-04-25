---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-02
principle: Technical Robustness and Safety
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "simplex-contract.yaml INV-001–INV-003"
---

# ETH-02 — Technical Robustness and Safety

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[1]`

---

## 1. Principle

Models are validated through evidence-gated pipelines before deployment in safety-critical domains.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| simplex-contract.yaml INV-001–INV-003 | Evidence-gated invariants for model qualification |

## 3. Implementation

- Every AI model passes through the simplex-contract evidence-gating pipeline before operational deployment.
- Invariants INV-001, INV-002, and INV-003 define minimum robustness thresholds.
- Adversarial robustness testing is conducted as part of the WP4 evaluation phase.
- Fallback mechanisms ensure graceful degradation when model confidence is below threshold.

## 4. Verification

- Evidence packages produced per `simplex-contract.yaml` conformity assessment.
- Red-team evaluation reports document robustness testing outcomes.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [simplex-contract.yaml](../simplex-contract.yaml) · [ethics-and-security.yaml](ethics-and-security.yaml)
