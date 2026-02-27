# AA-093 — Autonomy Assurance Case

> **Artefact ID:** AA-093
> **Domain:** 093 — Autonomy & Assurance
> **Parent Taxonomy:** UTS-TAX-001 v1.1
> **Status:** DRAFT
> **Author:** Amedeo Pelliccia
> **Frameworks:** EACST · GAIA EU
> **Classification:** Extension Domain (UTS Extension Roadmap)

---

## 1. Purpose

The **Autonomy Assurance Case (AA-093)** is the primary evidence artefact for Domain 093. It provides a structured, auditable argument that an autonomous system achieves and maintains the required levels of:

- **Reliability** — the system performs its intended function within defined bounds
- **Robustness** — the system maintains safe behaviour under out-of-distribution or adversarial conditions
- **Explainability (XAI)** — decisions made by AI/autonomous components can be traced and justified
- **Fail-safe design** — faults degrade gracefully without catastrophic consequence
- **SOTIF residual risk** — Safety of the Intended Functionality residual risk is within accepted thresholds

This artefact is **mandatory** prior to any GAIA EU admissibility review for autonomous systems and is referenced by EACST certification packages.

---

## 2. Scope

AA-093 applies to all UTS programmes where autonomous or semi-autonomous functions operate in any of the following modes:

| Autonomy Level | Description | Example |
|---|---|---|
| **L1 — Assisted** | Human-in-the-loop, AI advisory | Route suggestions, anomaly alerts |
| **L2 — Supervised** | Human-on-the-loop, AI executes | Auto-land with crew override |
| **L3 — Conditional** | AI executes; human intervened on request | Urban air mobility nominal ops |
| **L4 — High** | AI executes; human intervention optional | Long-range autonomous cargo |
| **L5 — Full** | No human intervention in operational design domain | Fully autonomous resupply missions |

AA-093 is **required for L2 and above**. L1 systems require a simplified assurance statement (AA-093-LITE).

---

## 3. Artefact Structure

```
AA-093/
├── README.md                    ← this file
├── aa-093-assurance-case.yaml   ← machine-readable assurance case (GSN/CAE)
├── evidence/
│   ├── EV-093-001-reliability/  ← MTBF, availability, fault tree data
│   ├── EV-093-002-robustness/   ← adversarial test results, ODD bounds
│   ├── EV-093-003-xai/          ← explainability scores, SHAP/LIME reports
│   ├── EV-093-004-sotif/        ← SOTIF residual risk register
│   └── EV-093-005-failsafe/     ← fail-safe verification records
├── reviews/
│   ├── internal-review-v1.md
│   └── eacst-signoff-checklist.md
└── CHANGELOG.md
```

---

## 4. Minimum Evidence Requirements

The following evidence items are **mandatory** for AA-093 package completeness:

| Evidence ID | Title | Acceptance Criterion | Owner |
|---|---|---|---|
| `EV-093-001` | Reliability & Availability Analysis | MTBF ≥ 10⁹ h for safety functions; availability ≥ 99.9999% | Reliability & Availability Engineer |
| `EV-093-002` | Robustness & ODD Validation Report | ≥ 95% test pass rate within operational design domain | Autonomy Systems Architect |
| `EV-093-003` | Explainability Assessment | Explainability score ≥ 0.7 for all L3+ decisions | XAI Specialist |
| `EV-093-004` | SOTIF Residual Risk Register | All Class A risks mitigated; Class B risks accepted with rationale | SOTIF Lead |
| `EV-093-005` | Fail-Safe Verification Record | All single-point failure modes verified safe; no undetected dual failures | Safety Case Author |

---

## 5. Limits of Use (LoU)

| Code | Limit | Enforcement |
|---|---|---|
| `LoU-093-001` | Autonomous safety function MTBF ≥ 10⁹ hours | Verified by independent reliability analysis; re-demonstrated after major SW change |
| `LoU-093-002` | Explainability score ≥ 0.7 for all Level 3+ autonomous decisions | Assessed per decision class; re-evaluated on model update |
| `LoU-093-003` | Assurance case mandatory prior to GAIA EU admissibility review | Gating condition; no AI admissibility token issued without AA-093 |
| `LoU-093-004` | ODD (Operational Design Domain) must be formally specified and bounded | Non-compliance invalidates all associated EV-093-002 evidence |
| `LoU-093-005` | Any change to autonomy software ≥ ASIL-B impact requires AA-093 resubmission | Enforced via CM gate in CI/CD pipeline |

---

## 6. Roles & Responsibilities

| Role | Responsibilities |
|---|---|
| **Autonomy Systems Architect** | Authors top-level assurance argument; owns ODD specification; approves EV-093-002 |
| **Reliability & Availability Engineer** | Produces fault trees, FMEA, MTBF analysis; owns EV-093-001 |
| **XAI Specialist** | Designs explainability methodology; produces EV-093-003; selects appropriate XAI framework |
| **Safety Case Author** | Structures GSN/CAE argument; links evidence to claims; owns overall AA-093 package |
| **SOTIF Lead** | Manages residual risk register; conducts SOTIF analysis per ISO 21448 / EACST-SOT; owns EV-093-004 |
| **Independent Reviewer** | Conducts adversarial review of the assurance case; signs off readiness for GAIA EU submission |

---

## 7. Key Terms & Metrics

| Term | Definition | Unit |
|---|---|---|
| **MTBF** | Mean Time Between Failures — average operational time between failures of a safety function | Hours |
| **Availability** | Proportion of time the autonomous function is operational and within spec | % |
| **Explainability Score** | Fidelity-weighted measure of how accurately post-hoc explanations reflect model behaviour (0–1) | Dimensionless |
| **Assurance Case Coverage** | % of operational scenarios covered by a linked claim + evidence pair in the GSN | % |
| **SOTIF Residual Risk** | Risk remaining after mitigation measures, attributed to autonomous system limitations | Risk class (A/B/C) |
| **ODD** | Operational Design Domain — the defined set of operating conditions within which the autonomous system is designed to function | Specification |
| **Fail-safe state** | A known, bounded, recoverable system state reached upon fault detection | State definition |

---

## 8. Interfaces with Other Domains

```
AA-093 ──depends on──► 000  (safety philosophy & human factors baseline)
AA-093 ──depends on──► 030  (AI/ML models, sensor fusion — the autonomous function itself)
AA-093 ──depends on──► 040  (simulation evidence for edge-case and ODD coverage)
AA-093 ──depends on──► 091  (human factors validation for L2/L3 handover interfaces)
AA-093 ──feeds into──► GAIA EU Admissibility Review
AA-093 ──feeds into──► EACST Certification Package
```

### Domain Cell Reference

```yaml
domain_cell:
  cell_id: "CELL_093_030"
  axes:
    - code: "093"
      bounds: { metric: "explainability_score", min: 0.7, max: 1.0 }
    - code: "030"
      bounds: { metric: "inference_accuracy", min: 0.85, max: 1.0 }
  admissibility:
    ai_use: "AI_AUTONOMOUS"
    required_evidence:
      - "AA-093"
      - "EV-093-001"
      - "EV-093-002"
      - "EV-093-003"
      - "EV-093-004"
      - "EV-093-005"
  limits_of_use:
    - "LoU-093-001"
    - "LoU-093-002"
    - "LoU-093-003"
  signoff: "EACST + GAIA-EU"
```

---

## 9. Assurance Case Format

AA-093 uses the **Goal Structuring Notation (GSN)** as the primary argument format, with optional CAE (Claims–Arguments–Evidence) for sub-claims. The top-level argument structure is:

```
G1: The autonomous system [X] is acceptably safe to operate within ODD [Y]
  ├── G2: The system is sufficiently reliable (EV-093-001)
  ├── G3: The system behaves robustly within and at the boundary of the ODD (EV-093-002)
  ├── G4: Autonomous decisions are explainable to required level (EV-093-003)
  ├── G5: SOTIF residual risk is within accepted threshold (EV-093-004)
  └── G6: All identified failure modes result in a safe state (EV-093-005)
```

The machine-readable form is encoded in `aa-093-assurance-case.yaml` using the `gsn-yaml` schema (see Related Artefacts).

---

## 10. Review & Approval Gates

| Gate | Condition | Approver |
|---|---|---|
| **AA-093-G1** Internal Draft | All evidence items drafted; internal peer review complete | Safety Case Author |
| **AA-093-G2** Independent Review | Adversarial review passed; all major findings resolved | Independent Reviewer |
| **AA-093-G3** EACST Submission Ready | LoU compliance confirmed; all evidence linked and version-controlled | Autonomy Systems Architect |
| **AA-093-G4** GAIA EU Admissibility Token | GAIA EU review board accepted; AI admissibility class assigned | GAIA EU Review Board |

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1 | TBD | Amedeo Pelliccia | Initial skeleton from UTS-TAX-001 v1.1 extension definition |

---

## Related Artefacts

| File | Purpose |
|---|---|
| `aa-093-assurance-case.yaml` | Machine-readable GSN assurance case |
| `../UTS-TAX-001/README.md` | Parent taxonomy document |
| `../EACST/eacst-regulatory-framework.yaml` | EACST machine-readable regulatory framework |
| `../GAIA-EU/domain-atlas.yaml` | GAIA EU Domain Atlas — admissibility model |
| `../093-ext/SKILL.md` | Engineering guidance for autonomy assurance practitioners |
| `EV-093-001` through `EV-093-005` | Evidence packs — see `evidence/` subdirectory |
