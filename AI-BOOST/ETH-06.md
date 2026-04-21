---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-06
principle: Societal and Environmental Well-Being
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "Green Deal Digital alignment"
---

# ETH-06 — Societal and Environmental Well-Being

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[5]`

---

## 1. Principle

Environmental footprint (CO₂-per-inference) is tracked and reported; sustainability targets are set per HPC job.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| Green Deal Digital alignment | EU Green Deal digital sustainability objectives |

## 3. Implementation

- CO₂ emissions are tracked per training run and per inference request (kg CO₂e per 1M tokens).
- HPC allocations prioritise nodes powered by renewable energy.
- Model architecture and training pipeline are optimised for compute efficiency (FLOPs per quality point).
- Environmental impact is included in all public reporting and model cards.

## 4. Verification

- Sustainability section included in every model card.
- Renewable energy percentage tracked in compute mix.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [ethics-and-security.yaml](ethics-and-security.yaml)
