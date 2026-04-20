---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-01
principle: Human Agency and Oversight
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "EU AI Act Art. 14"
  - "ALTAI §1"
---

# ETH-01 — Human Agency and Oversight

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[0]`

---

## 1. Principle

AI systems remain under meaningful human control; no fully autonomous safety-critical decisions without human-in-the-loop.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| EU AI Act Art. 14 | Human oversight requirements for high-risk AI systems |
| ALTAI §1 | Assessment List for Trustworthy AI — Human Agency and Oversight |

## 3. Implementation

- All safety-critical inference outputs require human review before operational use.
- Human-in-the-loop checkpoints are embedded in the PATH → MTL governance pipeline.
- Override mechanisms are available at every stage of the AI decision chain.

## 4. Verification

- Audit trail confirms human approval at each gate in `simplex-contract.yaml`.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [ethics-and-security.yaml](ethics-and-security.yaml)
