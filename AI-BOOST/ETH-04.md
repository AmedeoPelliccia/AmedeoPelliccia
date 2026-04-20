---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-04
principle: Transparency
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "EU AI Act Art. 53 (GPAI transparency)"
---

# ETH-04 — Transparency

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[3]`

---

## 1. Principle

Model architectures, training data sources, and evaluation results are publicly documented.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| EU AI Act Art. 53 | Transparency obligations for providers of general-purpose AI models |

## 3. Implementation

- Model architectures are published with full technical documentation.
- Training data sources are catalogued in the data provenance registry (DEL-03).
- Evaluation results (benchmarks, safety assessments, bias audits) are included in model cards.
- Open-weights releases include comprehensive model cards and datasheets.

## 4. Verification

- Public model card published for each released model.
- Data provenance registry accessible to consortium reviewers.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [ethics-and-security.yaml](ethics-and-security.yaml)
