---
# ═══════════════════════════════════════════════
# Consolidated Front Matter — Dual-Use Risk Analysis, Export Control & Data Protection
# ═══════════════════════════════════════════════
# Machine-readable companion: dual-use-risk-analysis.yaml (Documents 1 and 2)
# Programme: AI-BOOST — GA 101135737 (EuroHPC JU)
# IDEALE Pillar: D — Defense (dual-use awareness & export control)
# Author: Amedeo Pelliccia
# Related: DEL-03 §5.5; DEL-03 §6.1; README.md IDEALE-D pillar

schema_version: "1.0.0"
last_updated: "2026-04-14T00:00:00Z"
concern_areas:
  - document_type: dual_use_risk_analysis
    machine_readable_companion: dual-use-risk-analysis.yaml
    yaml_document: 1
  - document_type: data_protection
    machine_readable_companion: dual-use-risk-analysis.yaml
    yaml_document: 2
---

# Dual-Use Risk Analysis, Export Control & Data Protection

> **Programme:** AI-BOOST — GA 101135737 (EuroHPC JU)
> **IDEALE Pillar:** D — Defense (dual-use awareness & export control)
> **Machine-readable companion:** [`dual-use-risk-analysis.yaml`](dual-use-risk-analysis.yaml) (two YAML documents)
> **Related deliverables:** [DEL-03 Data Management Plan](DEL-03-data-management-plan.md) §5.5 Export Control, §6.1 Personal Data (GDPR)

---

## 1. Purpose

This document provides the AI-BOOST project's assessment of dual-use risks, export control obligations, and data protection compliance. It complements the Data Management Plan (DEL-03) and aligns with the **IDEALE-D** pillar's requirement for dual-use awareness, export control screening, and secure-by-design documentation.

This Markdown file uses a single consolidated front matter block, while the corresponding machine-readable companion remains split into two YAML documents:
- **YAML Document 1:** `dual_use_risk_analysis` — risk register (§2) and export control (§3)
- **YAML Document 2:** `data_protection` — GDPR compliance (§4)

**Regulatory basis:**
- EU Dual-Use Regulation (EU) 2021/821
- US Export Administration Regulations (EAR) / International Traffic in Arms Regulations (ITAR)
- General Data Protection Regulation (EU) 2016/679 (GDPR)

---

## 2. Dual-Use Risk Register

| ID | Category | Description | Likelihood | Impact | Mitigation |
|----|----------|-------------|:----------:|:------:|------------|
| **DU-01** | Military application of simulation acceleration | AI surrogate models could accelerate weapons system design. | Low | **High** | Export-control screening of consortium partners; restricted model variants for defense-adjacent use cases. |
| **DU-02** | Adversarial misuse of open-weights model | Open-weights release could enable generation of harmful content. | **Medium** | Medium | Red-teaming prior to release (WP4); safety fine-tuning; responsible release protocol. |
| **DU-03** | Surveillance capability | Multilingual NLP could be repurposed for mass surveillance. | Low | **High** | No biometric processing capability; data processing agreements prohibit surveillance use. |

### 2.1 Risk Matrix

```
         │  Low Impact  │  Medium Impact  │  High Impact
─────────┼──────────────┼─────────────────┼──────────────
High     │              │                 │
Medium   │              │     DU-02       │
Low      │              │                 │  DU-01, DU-03
```

### 2.2 Residual Risk Assessment

- **DU-01:** Residual risk **low** after partner screening and model-variant restrictions. Re-assessed at each consortium review.
- **DU-02:** Residual risk **low–medium** pending completion of WP4 red-teaming. Will be downgraded after responsible release protocol is validated.
- **DU-03:** Residual risk **low**. Architecture explicitly excludes biometric processing pipelines; contractual safeguards in place.

---

## 3. Export Control Requirements

| Requirement | Status | Evidence |
|-------------|:------:|----------|
| EU Dual-Use Regulation (EU) 2021/821 screening | 🟢 Completed | All consortium partners screened; no listed entities. |
| US EAR/ITAR assessment | 🟢 Completed | Core pipeline assessed; no US-origin controlled technology identified. |
| End-use monitoring | 🟡 Planned | Responsible use license terms will be used to support monitoring of model distribution and downstream use. |

### 3.1 Screening Process

1. **Partner screening** — All consortium members verified against EU consolidated sanctions lists and dual-use entity lists prior to grant agreement signature.
2. **Technology classification** — Core AI pipeline components reviewed against Annex I of Regulation (EU) 2021/821; no listed items identified.
3. **Non-EU access controls** — Partners outside the EU require additional approval for L1+ data access (see [DEL-03 §5.5](DEL-03-data-management-plan.md)).
4. **Model distribution** — Open-weights releases carry a responsible use license that prohibits military end-use without prior authorisation.

### 3.2 Compliance Gates

This assessment feeds into the following IDEALE compliance gates:

| Gate | Description | Reference |
|------|-------------|-----------|
| `GATE-EXPORT-CONTROL` | Dual-Use Regulation (EU) 2021/821 screening | `§3.1b` §5.2 |
| `GATE-IP-CLEAR` | Intellectual property and export classification clearance | `§3.1b` §5.2 |

---

## 4. Data Protection — GDPR Compliance

| Aspect | Status |
|--------|--------|
| Personal data processed | **No** |
| Regulation reference | Regulation (EU) 2016/679 (GDPR) |
| Data Protection Officer | Legal Lead Partner (`dpo@partner.eu`) |
| Privacy Impact Assessment required | No — no personal data is processed |
| Cross-border transfers | Not applicable — all data processed within EU-sovereign EuroHPC infrastructure |

### 4.1 Contingency

If personally identifiable information (PII) is inadvertently discovered in any dataset:

1. Data is **quarantined** immediately.
2. The Data Protection Officer is notified within 24 hours.
3. Data is **anonymised** or **deleted** per GDPR Article 17 (Right to Erasure).
4. The incident is logged and reported at the next consortium review.

### 4.2 Data Sovereignty

All training data consists of anonymised or synthetic simulation outputs processed exclusively on EU-sovereign EuroHPC sites. No third-country transfers are performed, eliminating the need for Standard Contractual Clauses (SCCs) or adequacy decisions.

### 4.3 Endpoints

| ID | Type | Name | URL | Notes |
|----|------|------|-----|-------|
| **EP-01** | Data Processing | EuroHPC Primary Processing Node | `https://eurohpc.ai-boost.eu/processing` | EU-sovereign; role-based access; consortium partners only |
| **EP-02** | Data Subject Rights | DSAR Portal | `https://ai-boost.eu/dsar` | GDPR Articles 15–22; response within 30 days |
| **EP-03** | DPO Contact | Data Protection Officer | `mailto:dpo@partner.eu` | Inquiries, breach notifications, DPIA consultations |

---

## 5. Review Schedule

| Milestone | Date | Scope |
|-----------|------|-------|
| **M6** | 2026-02-25 | Initial risk register and export control screening |
| **M18** | 2027-02-25 | Mid-term review; update post-WP4 red-teaming |
| **M24** | 2027-08-25 | Integrity audit, export control review, contingency assessment |
| **M36** | 2028-08-25 | Final assessment and close-out report |

---

## 6. References

- [DEL-03 — Data Management Plan](DEL-03-data-management-plan.md)
- [EU Dual-Use Regulation (EU) 2021/821](https://eur-lex.europa.eu/eli/reg/2021/821)
- [General Data Protection Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679)
- [IDEALE-D Pillar — Defense](../README.md)
- [ESSA EU-Security — MCSC](../ESSA/EU-SECURITY/README.md)
