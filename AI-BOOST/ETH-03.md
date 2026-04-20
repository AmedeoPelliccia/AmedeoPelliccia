---
schema_version: "1.0.0"
document_type: ethical_principle
last_updated: "2026-02-25T00:00:00Z"

id: ETH-03
principle: Privacy and Data Governance
parent_deliverable: DEL-07
programme: AI-BOOST
grant_agreement: "101135737"
managing_body: EuroHPC JU
status: draft

references:
  - "GDPR Art. 5, 25"
---

# ETH-03 — Privacy and Data Governance

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **Parent deliverable:** [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md)
> **Machine-readable source:** [`ethics-and-security.yaml`](ethics-and-security.yaml) § `ethical_framework.guiding_principles[2]`

---

## 1. Principle

All training data complies with GDPR; personal data is minimised, pseudonymised, or excluded.

## 2. Regulatory References

| Reference | Scope |
|-----------|-------|
| GDPR Art. 5 | Principles relating to processing of personal data |
| GDPR Art. 25 | Data protection by design and by default |

## 3. Implementation

- Training corpora use publicly available, non-personal data.
- Personal data is excluded or pseudonymised before ingestion.
- Data Protection Impact Assessment (DPIA) conducted before training on any dataset containing personal data.
- Data subject rights procedures are documented in the Data Management Plan (DEL-03).
- All training and inference runs on EU-based EuroHPC infrastructure; no extra-EU data transfers for safety-critical workloads.

## 4. Verification

- Data provenance registry (DEL-03) tracks all training data sources.
- Consent audit trail maintained for user-generated content.
- Opt-out request process documented and operational.
- Periodic review at milestones M6, M18, and M36.

---

*See also:* [DEL-07 Ethics and Security](DEL-07-ethics-and-security.md) · [DEL-03 Data Management Plan](DEL-03-data-management-plan.md) · [ethics-and-security.yaml](ethics-and-security.yaml)
