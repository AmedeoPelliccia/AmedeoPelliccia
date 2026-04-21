---
# workplan-milestones-gantt.yaml
# Machine-readable specification for DEL-05 Workplan, Milestones & Gantt.
# Programme: AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
# Section: Implementation → Work Plan and Resources (Quality & Efficiency)
# Reference: AI-BOOST/DEL-05-workplan-milestones-gantt.md
# Author: Amedeo Pelliccia

schema_version: "1.0.0"
document_type: workplan_milestones_gantt
last_updated: "2026-02-25T00:00:00Z"

# ─────────────────────────────────────────────
# 1. Deliverable Metadata
# ─────────────────────────────────────────────
deliverable:
  id: DEL-05
  title: "Workplan, Milestones & Gantt"
  section: "Implementation → Work Plan and Resources (Quality & Efficiency)"
  programme:
    name: AI-BOOST
    grant_agreement: "GA 101135737"
    funding_body: EuroHPC JU
  status: draft
  due_milestones:
    - milestone: M6
      scope: initial
    - milestone: M18
      scope: mid_term_update
    - milestone: M36
      scope: final

# ─────────────────────────────────────────────
# 2. Project Duration
# ─────────────────────────────────────────────
project:
  duration_months: 36
  start_month: M1
  end_month: M36

# ─────────────────────────────────────────────
# 3. Work Packages
# ─────────────────────────────────────────────
work_packages:
  - id: WP1
    title: Project Management & Quality Assurance
    lead: coordinator
    effort_pm: 24
    start: M1
    end: M36
    objectives: [OBJ-01, OBJ-02, OBJ-03, OBJ-04, OBJ-05]
    tasks:
      - id: T1.1
        title: Consortium coordination & governance
        start: M1
        end: M36
        deliverables:
          - id: D1.1
            title: Consortium Agreement
            due: M1
      - id: T1.2
        title: Quality assurance & risk management
        start: M1
        end: M36
        deliverables:
          - id: D1.2
            title: Quality Plan
            due: M3
          - id: D1.3
            title: Risk Register
            due: M3
            updates: [M12, M24]
      - id: T1.3
        title: Financial & administrative management
        start: M1
        end: M36
        deliverables:
          - id: D1.4
            title: Periodic Reports
            due: M18
            updates: [M36]
      - id: T1.4
        title: Ethics oversight & compliance monitoring
        start: M1
        end: M36
        deliverables:
          - id: D1.5
            title: Ethics Review Reports
            due: M12
            updates: [M24, M36]

  - id: WP2
    title: Sovereign Frontier AI Model Development
    lead: ai_lead
    effort_pm: 120
    start: M1
    end: M30
    objectives: [OBJ-01, OBJ-02, OBJ-04]
    tasks:
      - id: T2.1
        title: "Architecture design & scaling strategy (GAIA-EU MoE)"
        start: M1
        end: M6
        deliverables:
          - id: D2.1
            title: Architecture Specification
            due: M6
      - id: T2.2
        title: "Multilingual training data pipeline (24 EU languages)"
        start: M3
        end: M12
        deliverables:
          - id: D2.2
            title: Training Data Report
            due: M12
      - id: T2.3
        title: "Staged model training (S1 → S2 → S3 scaling)"
        start: M6
        end: M24
        deliverables:
          - id: D2.3
            title: Model Checkpoints
            due: M12
            updates: [M18, M24]
      - id: T2.4
        title: Quantum-augmented expert routing module
        start: M6
        end: M24
        deliverables:
          - id: D2.4
            title: Quantum Module Report
            due: M24
      - id: T2.5
        title: Benchmark evaluation & model validation
        start: M18
        end: M30
        deliverables:
          - id: D2.5
            title: Benchmark Report
            due: M30

  - id: WP3
    title: HPC Infrastructure & Simulation Acceleration
    lead: hpc_lead
    effort_pm: 96
    start: M1
    end: M30
    objectives: [OBJ-02, OBJ-04]
    tasks:
      - id: T3.1
        title: EuroHPC node allocation & environment setup
        start: M1
        end: M6
        deliverables:
          - id: D3.1
            title: HPC Environment Report
            due: M6
      - id: T3.2
        title: Distributed training framework deployment
        start: M3
        end: M12
        deliverables:
          - id: D3.2
            title: Training Framework Documentation
            due: M12
      - id: T3.3
        title: "Simulation acceleration pipeline (≥ 10× target)"
        start: M6
        end: M24
        deliverables:
          - id: D3.3
            title: Acceleration Benchmark Report
            due: M24
      - id: T3.4
        title: Hybrid quantum-classical integration layer
        start: M12
        end: M30
        deliverables:
          - id: D3.4
            title: Hybrid Integration Report
            due: M30

  - id: WP4
    title: Certification-Grade Governance & Gating
    lead: governance_lead
    effort_pm: 84
    start: M3
    end: M36
    objectives: [OBJ-01, OBJ-03]
    tasks:
      - id: T4.1
        title: "PATH → MTL governance pipeline implementation"
        start: M3
        end: M18
        deliverables:
          - id: D4.1
            title: Governance Pipeline v1.0
            due: M18
      - id: T4.2
        title: Simplex-based admissibility classification
        start: M6
        end: M24
        deliverables:
          - id: D4.2
            title: Admissibility Framework Report
            due: M24
      - id: T4.3
        title: "AI model qualification (≥ 3 models gated)"
        start: M12
        end: M36
        deliverables:
          - id: D4.3
            title: Qualification Dossiers
            due: M24
            updates: [M36]
      - id: T4.4
        title: AI Act compliance-by-design toolkit
        start: M6
        end: M30
        deliverables:
          - id: D4.4
            title: Compliance Toolkit Release
            due: M30

  - id: WP5
    title: "Sustainability, Ethics & Compliance"
    lead: sustainability_lead
    effort_pm: 48
    start: M1
    end: M36
    objectives: [OBJ-05]
    tasks:
      - id: T5.1
        title: "CO₂-per-inference metric design & integration"
        start: M1
        end: M12
        deliverables:
          - id: D5.1
            title: Sustainability Metric Specification
            due: M12
      - id: T5.2
        title: HPC energy monitoring & reporting dashboard
        start: M6
        end: M24
        deliverables:
          - id: D5.2
            title: Sustainability Dashboard
            due: M24
      - id: T5.3
        title: "Ethics & dual-use assessment"
        start: M1
        end: M36
        deliverables:
          - id: D5.3
            title: Ethics Reports
            due: M12
            updates: [M24, M36]
      - id: T5.4
        title: "GDPR & data governance compliance"
        start: M1
        end: M36
        deliverables:
          - id: D5.4
            title: Compliance Audit Reports
            due: M18
            updates: [M36]

  - id: WP6
    title: "Dissemination, Exploitation & Communication"
    lead: dissemination_lead
    effort_pm: 48
    start: M1
    end: M36
    objectives: [OBJ-01, OBJ-02, OBJ-03, OBJ-04, OBJ-05]
    tasks:
      - id: T6.1
        title: Project website & visual identity
        start: M1
        end: M6
        deliverables:
          - id: D6.1
            title: Project Website
            due: M3
      - id: T6.2
        title: Scientific publications & conference participation
        start: M6
        end: M36
        deliverables:
          - id: D6.2
            title: Publication Log
            due: M18
            updates: [M36]
      - id: T6.3
        title: Exploitation & IP management
        start: M6
        end: M36
        deliverables:
          - id: D6.3
            title: Exploitation Plan Update
            due: M18
            updates: [M36]
      - id: T6.4
        title: "Standardisation engagement (CEN/CENELEC, EUROCAE)"
        start: M12
        end: M36
        deliverables:
          - id: D6.4
            title: Standardisation Report
            due: M36
      - id: T6.5
        title: Public communication & policy engagement
        start: M1
        end: M36
        deliverables:
          - id: D6.5
            title: Communication Activity Report
            due: M18
            updates: [M36]

# ─────────────────────────────────────────────
# 4. Milestones
# ─────────────────────────────────────────────
milestones:
  - id: MS-01
    title: HPC environment operational
    wp: WP3
    due: M6
    verification: "EuroHPC allocation confirmed; test workloads executed"
  - id: MS-02
    title: Architecture design approved
    wp: WP2
    due: M6
    verification: "Architecture specification peer-reviewed and accepted"
  - id: MS-03
    title: Quality plan & risk register baseline
    wp: WP1
    due: M3
    verification: "Documents approved by consortium board"
  - id: MS-04
    title: S1 model checkpoint trained
    wp: WP2
    due: M12
    verification: "Training converged; benchmark scores recorded"
  - id: MS-05
    title: Governance pipeline v1.0 deployed
    wp: WP4
    due: M18
    verification: "Pipeline operational; ≥ 1 model processed through gates"
  - id: MS-06
    title: "Simulation ≥ 10× acceleration demonstrated"
    wp: WP3
    due: M24
    verification: "Benchmark vs. baseline documented"
  - id: MS-07
    title: "≥ 3 AI models gate-qualified"
    wp: WP4
    due: M36
    verification: "Qualification dossiers complete; evidence gates passed"
  - id: MS-08
    title: "CO₂-per-inference tracking operational"
    wp: WP5
    due: M12
    verification: "Metric integrated into HPC job scheduler; dashboard live"
  - id: MS-09
    title: Mid-term review
    wp: WP1
    due: M18
    verification: "EC review passed"
  - id: MS-10
    title: Final review & project closure
    wp: WP1
    due: M36
    verification: "All deliverables submitted; final report accepted"

# ─────────────────────────────────────────────
# 5. Resource Allocation (Person-Months)
# ─────────────────────────────────────────────
resource_allocation:
  partners:
    - id: coordinator
      label: Coordinator
      effort: { WP1: 12, WP2: 24, WP3: 12, WP4: 18, WP5: 12, WP6: 12, total: 90 }
    - id: ai_research
      label: AI Research Partner
      effort: { WP1: 4, WP2: 48, WP3: 12, WP4: 12, WP5: 6, WP6: 6, total: 88 }
    - id: hpc_partner
      label: HPC Partner
      effort: { WP1: 4, WP2: 24, WP3: 48, WP4: 6, WP5: 12, WP6: 6, total: 100 }
    - id: aerospace_cert
      label: Aerospace/Certification Partner
      effort: { WP1: 2, WP2: 12, WP3: 12, WP4: 36, WP5: 6, WP6: 12, total: 80 }
    - id: sustainability_ethics
      label: Sustainability/Ethics Partner
      effort: { WP1: 2, WP2: 12, WP3: 12, WP4: 12, WP5: 12, WP6: 12, total: 62 }
  totals: { WP1: 24, WP2: 120, WP3: 96, WP4: 84, WP5: 48, WP6: 48, grand_total: 420 }

  equipment:
    - item: EuroHPC pre-exascale allocation
      provider: EuroHPC JU
      justification: "Frontier model training (S1–S3), simulation acceleration, hybrid quantum-classical runs"
    - item: "Secure data storage (L1–L2)"
      provider: Coordinator / HPC Partner
      justification: "Encrypted storage for consortium data per DMP security classification"
    - item: Quantum computing access
      provider: National QC facility
      justification: "Hybrid quantum-classical expert routing experiments (T2.4, T3.4)"

# ─────────────────────────────────────────────
# 6. Quality Management
# ─────────────────────────────────────────────
quality_management:
  gates:
    - id: G1
      name: Feasibility
      criteria: "Scope and approach validated"
      evidence: "Architecture review, risk assessment"
    - id: G2
      name: Design
      criteria: "Technical design peer-reviewed"
      evidence: "Design documents, review minutes"
    - id: G3
      name: Implementation
      criteria: "Code / artefact meets specification"
      evidence: "Test reports, CI/CD logs, benchmark results"
    - id: G4
      name: Validation
      criteria: "Results meet KPI targets"
      evidence: "Benchmark scores, qualification dossiers"
    - id: G5
      name: Release
      criteria: "Deliverable approved for submission"
      evidence: "Internal review sign-off, quality checklist"

  metrics:
    - metric: Deliverable on-time rate
      target: "≥ 90 %"
    - metric: "Gate pass rate (first attempt)"
      target: "≥ 80 %"
    - metric: "Test coverage (code deliverables)"
      target: "≥ 85 %"
    - metric: Publication acceptance rate
      target: "≥ 60 %"
    - metric: Audit finding closure time
      target: "≤ 30 days"

  review_cycle:
    - activity: WP progress teleconference
      frequency: monthly
      participants: "WP leads, coordinator"
    - activity: Consortium plenary meeting
      frequency: "every 6 months"
      participants: all partners
    - activity: Quality audit
      frequency: annual
      participants: "coordinator + external auditor"
    - activity: EC periodic report
      schedule: [M18, M36]
      participants: "coordinator → EC"
    - activity: Risk register review
      frequency: quarterly
      participants: "WP leads, coordinator"

# ─────────────────────────────────────────────
# 7. Risk Management
# ─────────────────────────────────────────────
risk_management:
  risks:
    - id: R-01
      risk: EuroHPC allocation delayed or insufficient
      likelihood: medium
      impact: high
      mitigation: "Early submission; fallback to national HPC; phased scaling strategy"
      owner: hpc_lead
    - id: R-02
      risk: Model training does not converge at scale
      likelihood: medium
      impact: high
      mitigation: "Chinchilla-optimal compute schedule; staged S1→S2→S3 with go/no-go gates"
      owner: ai_lead
    - id: R-03
      risk: Key personnel departure
      likelihood: medium
      impact: medium
      mitigation: "Knowledge sharing protocol; 2-deep staffing on critical tasks"
      owner: coordinator
    - id: R-04
      risk: "Regulatory uncertainty (AI Act delegated acts)"
      likelihood: medium
      impact: medium
      mitigation: "Active standards body participation; adaptive compliance framework"
      owner: governance_lead
    - id: R-05
      risk: Partner withdrawal
      likelihood: low
      impact: high
      mitigation: "Consortium agreement fallback clauses; task reallocation plan"
      owner: coordinator
    - id: R-06
      risk: "Data security breach (L2+ data)"
      likelihood: low
      impact: high
      mitigation: "Encryption, RBAC, 24-hour incident response, regular penetration tests"
      owner: sustainability_lead
    - id: R-07
      risk: IP conflict between partners
      likelihood: low
      impact: medium
      mitigation: "Clear background IP register; 60-day opt-in publication protocol"
      owner: coordinator
    - id: R-08
      risk: Recruitment of specialised AI/HPC talent
      likelihood: high
      impact: medium
      mitigation: "Competitive salaries; remote-first; EU doctoral network partnerships"
      owner: all_leads
  contingency: >
    If any milestone is at risk of delay by more than 3 months: (1) WP lead
    reports root-cause analysis, (2) coordinator convenes ad-hoc steering
    committee within 2 weeks, (3) steering committee decides on task
    reallocation, scope adjustment, resource rebalancing, or formal amendment
    request to EC, (4) decision and corrective action plan recorded in risk
    register.

# ─────────────────────────────────────────────
# 8. Critical Path
# ─────────────────────────────────────────────
critical_path:
  - step: 1
    period: "M1–M6"
    activities: "EuroHPC setup (T3.1) + Architecture design (T2.1)"
    note: "Prerequisite for model training"
  - step: 2
    period: "M6–M24"
    activities: "Staged model training (T2.3)"
    note: "Longest lead-time activity"
  - step: 3
    period: "M18–M36"
    activities: "Governance pipeline (T4.1) + AI model qualification (T4.3)"
    note: "Gate-dependent on trained models"
  - step: 4
    period: "M24–M36"
    activities: "Benchmark evaluation (T2.5) + Final qualification dossiers (T4.3)"
    note: "Final deliverables"

# ─────────────────────────────────────────────
# 9. Revision History
# ─────────────────────────────────────────────
revision_history:
  - version: "0.1"
    date: "2026-02-25"
    milestone: M6
    description: "Initial Workplan, Milestones & Gantt"
---

# DEL-05 — Workplan, Milestones & Gantt

**Deliverable ID:** DEL-05
**Section:** Implementation → Work Plan and Resources (Quality & Efficiency)
**Programme:** AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
**Author:** Amedeo Pelliccia
**Status:** Draft
**Due:** M6 (initial), updated at M18 and M36

---

## 1. Project Structure Overview

AI-BOOST is organised into **6 Work Packages (WPs)** spanning a **36-month** programme. The structure aligns with the five project objectives (OBJ-01–OBJ-05) and the IDEALE-ESG framework, ensuring traceability from technical tasks to evaluation criteria.

| WP | Title | Lead | Months | Objectives |
|----|-------|------|--------|------------|
| WP1 | Project Management & Quality Assurance | Coordinator | M1–M36 | All |
| WP2 | Sovereign Frontier AI Model Development | AI Lead | M1–M30 | OBJ-01, OBJ-02, OBJ-04 |
| WP3 | HPC Infrastructure & Simulation Acceleration | HPC Lead | M1–M30 | OBJ-02, OBJ-04 |
| WP4 | Certification-Grade Governance & Gating | Governance Lead | M3–M36 | OBJ-01, OBJ-03 |
| WP5 | Sustainability, Ethics & Compliance | Sustainability Lead | M1–M36 | OBJ-05 |
| WP6 | Dissemination, Exploitation & Communication | Dissemination Lead | M1–M36 | All |

---

## 2. Work Package Descriptions

### WP1 — Project Management & Quality Assurance

**Lead:** Coordinator
**Effort:** 24 PM
**Period:** M1–M36

| Task | Description | Period | Deliverables |
|------|-------------|--------|--------------|
| T1.1 | Consortium coordination & governance | M1–M36 | D1.1 Consortium Agreement (M1) |
| T1.2 | Quality assurance & risk management | M1–M36 | D1.2 Quality Plan (M3), D1.3 Risk Register (M3, updated M12, M24) |
| T1.3 | Financial & administrative management | M1–M36 | D1.4 Periodic Reports (M18, M36) |
| T1.4 | Ethics oversight & compliance monitoring | M1–M36 | D1.5 Ethics Review Reports (M12, M24, M36) |

### WP2 — Sovereign Frontier AI Model Development

**Lead:** AI Lead
**Effort:** 120 PM
**Period:** M1–M30

| Task | Description | Period | Deliverables |
|------|-------------|--------|--------------|
| T2.1 | Architecture design & scaling strategy (GAIA-EU MoE) | M1–M6 | D2.1 Architecture Specification (M6) |
| T2.2 | Multilingual training data pipeline (24 EU languages) | M3–M12 | D2.2 Training Data Report (M12) |
| T2.3 | Staged model training (S1 → S2 → S3 scaling) | M6–M24 | D2.3 Model Checkpoints (M12, M18, M24) |
| T2.4 | Quantum-augmented expert routing module | M6–M24 | D2.4 Quantum Module Report (M24) |
| T2.5 | Benchmark evaluation & model validation | M18–M30 | D2.5 Benchmark Report (M30) |

### WP3 — HPC Infrastructure & Simulation Acceleration

**Lead:** HPC Lead
**Effort:** 96 PM
**Period:** M1–M30

| Task | Description | Period | Deliverables |
|------|-------------|--------|--------------|
| T3.1 | EuroHPC node allocation & environment setup | M1–M6 | D3.1 HPC Environment Report (M6) |
| T3.2 | Distributed training framework deployment | M3–M12 | D3.2 Training Framework Documentation (M12) |
| T3.3 | Simulation acceleration pipeline (≥ 10× target) | M6–M24 | D3.3 Acceleration Benchmark Report (M24) |
| T3.4 | Hybrid quantum-classical integration layer | M12–M30 | D3.4 Hybrid Integration Report (M30) |

### WP4 — Certification-Grade Governance & Gating

**Lead:** Governance Lead
**Effort:** 84 PM
**Period:** M3–M36

| Task | Description | Period | Deliverables |
|------|-------------|--------|--------------|
| T4.1 | PATH → MTL governance pipeline implementation | M3–M18 | D4.1 Governance Pipeline v1.0 (M18) |
| T4.2 | Simplex-based admissibility classification | M6–M24 | D4.2 Admissibility Framework Report (M24) |
| T4.3 | AI model qualification (≥ 3 models gated) | M12–M36 | D4.3 Qualification Dossiers (M24, M36) |
| T4.4 | AI Act compliance-by-design toolkit | M6–M30 | D4.4 Compliance Toolkit Release (M30) |

### WP5 — Sustainability, Ethics & Compliance

**Lead:** Sustainability Lead
**Effort:** 48 PM
**Period:** M1–M36

| Task | Description | Period | Deliverables |
|------|-------------|--------|--------------|
| T5.1 | CO₂-per-inference metric design & integration | M1–M12 | D5.1 Sustainability Metric Specification (M12) |
| T5.2 | HPC energy monitoring & reporting dashboard | M6–M24 | D5.2 Sustainability Dashboard (M24) |
| T5.3 | Ethics & dual-use assessment | M1–M36 | D5.3 Ethics Reports (M12, M24, M36) |
| T5.4 | GDPR & data governance compliance | M1–M36 | D5.4 Compliance Audit Reports (M18, M36) |

### WP6 — Dissemination, Exploitation & Communication

**Lead:** Dissemination Lead
**Effort:** 48 PM
**Period:** M1–M36

| Task | Description | Period | Deliverables |
|------|-------------|--------|--------------|
| T6.1 | Project website & visual identity | M1–M6 | D6.1 Project Website (M3) |
| T6.2 | Scientific publications & conference participation | M6–M36 | D6.2 Publication Log (M18, M36) |
| T6.3 | Exploitation & IP management | M6–M36 | D6.3 Exploitation Plan Update (M18, M36) |
| T6.4 | Standardisation engagement (CEN/CENELEC, EUROCAE) | M12–M36 | D6.4 Standardisation Report (M36) |
| T6.5 | Public communication & policy engagement | M1–M36 | D6.5 Communication Activity Report (M18, M36) |

---

## 3. Milestones

| ID | Milestone | WP | Due | Verification |
|----|-----------|----|-----|--------------|
| MS-01 | HPC environment operational | WP3 | M6 | EuroHPC allocation confirmed; test workloads executed |
| MS-02 | Architecture design approved | WP2 | M6 | Architecture specification peer-reviewed and accepted |
| MS-03 | Quality plan & risk register baseline | WP1 | M3 | Documents approved by consortium board |
| MS-04 | S1 model checkpoint trained | WP2 | M12 | Training converged; benchmark scores recorded |
| MS-05 | Governance pipeline v1.0 deployed | WP4 | M18 | Pipeline operational; ≥ 1 model processed through gates |
| MS-06 | Simulation ≥ 10× acceleration demonstrated | WP3 | M24 | Benchmark vs. baseline documented |
| MS-07 | ≥ 3 AI models gate-qualified | WP4 | M36 | Qualification dossiers complete; evidence gates passed |
| MS-08 | CO₂-per-inference tracking operational | WP5 | M12 | Metric integrated into HPC job scheduler; dashboard live |
| MS-09 | Mid-term review | WP1 | M18 | EC review passed |
| MS-10 | Final review & project closure | WP1 | M36 | All deliverables submitted; final report accepted |

---

## 4. Gantt Chart

```
Work Package / Task                          M1  M3  M6  M9  M12  M15  M18  M21  M24  M27  M30  M33  M36
──────────────────────────────────────────── ─── ─── ─── ─── ──── ──── ──── ──── ──── ──── ──── ──── ────
WP1 Project Management & Quality
  T1.1 Consortium coordination               ████████████████████████████████████████████████████████████
  T1.2 Quality assurance & risk mgmt         ████████████████████████████████████████████████████████████
  T1.3 Financial & admin management          ████████████████████████████████████████████████████████████
  T1.4 Ethics oversight                      ████████████████████████████████████████████████████████████

WP2 Sovereign Frontier AI Model
  T2.1 Architecture design                   ██████████████
  T2.2 Multilingual data pipeline                ███████████████████
  T2.3 Staged model training                          ██████████████████████████████████████████
  T2.4 Quantum-augmented expert routing               ██████████████████████████████████████████
  T2.5 Benchmark evaluation                                               ██████████████████████████

WP3 HPC Infrastructure & Simulation
  T3.1 EuroHPC setup                         ██████████████
  T3.2 Distributed training framework             ███████████████████
  T3.3 Simulation acceleration                        ██████████████████████████████████████████
  T3.4 Hybrid quantum-classical                                    ██████████████████████████████████████

WP4 Certification-Grade Governance
  T4.1 PATH → MTL pipeline                        ████████████████████████████████
  T4.2 Simplex admissibility                           ██████████████████████████████████████████
  T4.3 AI model qualification                                      ██████████████████████████████████████████
  T4.4 AI Act compliance toolkit                       ██████████████████████████████████████████████████

WP5 Sustainability, Ethics & Compliance
  T5.1 CO₂-per-inference metric              ████████████████████████
  T5.2 Energy monitoring dashboard                     ██████████████████████████████████████████
  T5.3 Ethics & dual-use assessment          ████████████████████████████████████████████████████████████
  T5.4 GDPR & data governance               ████████████████████████████████████████████████████████████

WP6 Dissemination & Exploitation
  T6.1 Website & visual identity             █████████
  T6.2 Scientific publications                        ████████████████████████████████████████████████████
  T6.3 Exploitation & IP management                    ████████████████████████████████████████████████████
  T6.4 Standardisation engagement                                   ████████████████████████████████████████
  T6.5 Public communication                  ████████████████████████████████████████████████████████████

Milestones                                    ▲       ▲       ▲            ▲            ▲                 ▲
                                            MS-03  MS-01  MS-04        MS-05        MS-06              MS-07
                                                   MS-02  MS-08        MS-09                           MS-10
```

---

## 5. Resource Allocation

### 5.1 Person-Months by Work Package

| Partner | WP1 | WP2 | WP3 | WP4 | WP5 | WP6 | Total |
|---------|-----|-----|-----|-----|-----|-----|-------|
| Coordinator | 12 | 24 | 12 | 18 | 12 | 12 | 90 |
| AI Research Partner | 4 | 48 | 12 | 12 | 6 | 6 | 88 |
| HPC Partner | 4 | 24 | 48 | 6 | 12 | 6 | 100 |
| Aerospace/Certification Partner | 2 | 12 | 12 | 36 | 6 | 12 | 80 |
| Sustainability/Ethics Partner | 2 | 12 | 12 | 12 | 12 | 12 | 62 |
| **Total** | **24** | **120** | **96** | **84** | **48** | **48** | **420** |

### 5.2 Major Equipment and Infrastructure

| Item | Provider | Justification |
|------|----------|---------------|
| EuroHPC pre-exascale allocation | EuroHPC JU | Frontier model training (S1–S3), simulation acceleration, hybrid quantum-classical runs |
| Secure data storage (L1–L2) | Coordinator / HPC Partner | Encrypted storage for consortium data per DMP security classification |
| Quantum computing access | National QC facility | Hybrid quantum-classical expert routing experiments (T2.4, T3.4) |

### 5.3 Other Major Costs

| Category | Estimated Cost | Justification |
|----------|---------------|---------------|
| Travel & subsistence | As per GA rates | Consortium meetings (bi-annual), conference participation (4/year), standardisation body meetings |
| Open-access publication fees | As per OA policy | Gold OA where required; Green OA via preprint for remainder |
| Subcontracting | < 10% total budget | External audit (T1.2), specialised security assessment (T5.4) |
| Equipment (non-HPC) | As per GA rates | Development workstations, GPU test nodes for pre-HPC validation |

---

## 6. Quality Management

### 6.1 Quality Assurance Framework

Quality is managed through the evidence-gated governance pipeline (PATH → MTL) and the simplex-contract admissibility framework. All deliverables pass through the following gate sequence:

| Gate | Name | Criteria | Evidence |
|------|------|----------|----------|
| G1 | **Feasibility** | Scope and approach validated | Architecture review, risk assessment |
| G2 | **Design** | Technical design peer-reviewed | Design documents, review minutes |
| G3 | **Implementation** | Code / artefact meets specification | Test reports, CI/CD logs, benchmark results |
| G4 | **Validation** | Results meet KPI targets | Benchmark scores, qualification dossiers |
| G5 | **Release** | Deliverable approved for submission | Internal review sign-off, quality checklist |

### 6.2 Quality Metrics

| Metric | Target | Measured |
|--------|--------|----------|
| Deliverable on-time rate | ≥ 90 % | Per milestone review |
| Gate pass rate (first attempt) | ≥ 80 % | Gate log audit |
| Test coverage (code deliverables) | ≥ 85 % | CI/CD reports |
| Publication acceptance rate | ≥ 60 % | Publication tracker |
| Audit finding closure time | ≤ 30 days | Risk register |

### 6.3 Review and Reporting Cycle

| Activity | Frequency | Participants |
|----------|-----------|--------------|
| WP progress teleconference | Monthly | WP leads, coordinator |
| Consortium plenary meeting | Every 6 months | All partners |
| Quality audit | Annual | Coordinator + external auditor |
| EC periodic report | M18, M36 | Coordinator → EC |
| Risk register review | Quarterly | WP leads, coordinator |

---

## 7. Risk Management

### 7.1 Risk Register

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|-----------|--------|------------|-------|
| R-01 | EuroHPC allocation delayed or insufficient | Medium | High | Early submission; fallback to national HPC; phased scaling strategy | HPC Lead |
| R-02 | Model training does not converge at scale | Medium | High | Chinchilla-optimal compute schedule; staged S1→S2→S3 with go/no-go gates | AI Lead |
| R-03 | Key personnel departure | Medium | Medium | Knowledge sharing protocol; 2-deep staffing on critical tasks | Coordinator |
| R-04 | Regulatory uncertainty (AI Act delegated acts) | Medium | Medium | Active standards body participation; adaptive compliance framework | Governance Lead |
| R-05 | Partner withdrawal | Low | High | Consortium agreement fallback clauses; task reallocation plan | Coordinator |
| R-06 | Data security breach (L2+ data) | Low | High | Encryption, RBAC, 24-hour incident response, regular penetration tests | Sustainability Lead |
| R-07 | IP conflict between partners | Low | Medium | Clear background IP register; 60-day opt-in publication protocol | Coordinator |
| R-08 | Recruitment of specialised AI/HPC talent | High | Medium | Competitive salaries; remote-first; EU doctoral network partnerships | All leads |

### 7.2 Contingency Plan

If any milestone is at risk of delay by more than 3 months:

1. WP lead reports to coordinator with root-cause analysis
2. Coordinator convenes ad-hoc steering committee within 2 weeks
3. Steering committee decides on: (a) task reallocation, (b) scope adjustment, (c) resource rebalancing, or (d) formal amendment request to EC
4. Decision and corrective action plan recorded in risk register

---

## 8. Critical Path

The project critical path runs through:

1. **M1–M6:** EuroHPC environment setup (T3.1) + Architecture design (T2.1) → prerequisite for model training
2. **M6–M24:** Staged model training (T2.3) → longest lead-time activity
3. **M18–M36:** Governance pipeline (T4.1) + AI model qualification (T4.3) → gate-dependent on trained models
4. **M24–M36:** Benchmark evaluation (T2.5) + Final qualification dossiers (T4.3) → final deliverables

Any delay in EuroHPC allocation (T3.1) or model training (T2.3) propagates directly to project completion.

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`workplan-milestones-gantt.yaml`](workplan-milestones-gantt.yaml) | Machine-readable specification: work packages, milestones, Gantt data, resource allocation, quality metrics |
| DEL-04 — Innovation and Impact (planned artefact) | Innovation and Impact — exploitation routes and TRL progression aligned with WP outputs |
| DEL-03 — Data Management Plan (planned artefact) | Data Management Plan — dataset lifecycle aligned with WP schedule |
| Root [`README.md`](../README.md) | Profile-level reference under Current Focus |
| [`simplex-contract.yaml`](../simplex-contract.yaml) | Evidence-gated admissibility framework used in quality management (§6) |
| [`contributions-registry.yaml`](../contributions-registry.yaml) | Contribution governance for resource allocation and attribution |
