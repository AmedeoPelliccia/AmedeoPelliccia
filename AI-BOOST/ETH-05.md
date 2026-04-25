---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-05
principle: Diversity, Non-Discrimination, and Fairness
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "EU AI Act Recital 70"
---

# ETH-05 — Diversity, Non-Discrimination, and Fairness

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[4]`

---

## 1. Principle

Multilingual training ensures balanced performance across all 24 EU official languages; bias audits are conducted per work package.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| EU AI Act Recital 70 | Non-discrimination requirements and bias mitigation in AI systems |

## 3. Implementation

- Training corpora are balanced across all 24 EU official languages.
- Bias audits are conducted for each work package to detect demographic, linguistic, and geographic bias.
- Training data is audited for representation balance before model training.
- Evaluation benchmarks include fairness metrics across language groups.

## 4. Verification

- Bias evaluation report produced per work package.
- Multilingual performance parity metrics tracked.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [ethics-and-security.yaml](ethics-and-security.yaml)
