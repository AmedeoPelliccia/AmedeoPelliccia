---
# application-strategy.yaml
# Machine-readable application strategy for the AI-BOOST project
# under the Frontier AI Grand Challenge (EuroHPC JU).
# Grant Agreement: GA 101135737
# Deadline: 2026-04-13
# Reference: AI-BOOST/README.md
# Author: Amedeo Pelliccia

schema_version: "1.0.0"
document_type: application_strategy
last_updated: "2026-02-25T00:00:00Z"

# ─────────────────────────────────────────────
# 1. Programme Identity
# ─────────────────────────────────────────────
programme:
  name: AI-BOOST
  full_title: >
    AI-Based Optimisation of Operational Simulation and Testing
  call: Frontier AI Grand Challenge
  funding_body: EuroHPC JU
  grant_agreement: "GA 101135737"
  deadline: "2026-04-13"
  framework_alignment:
    - IDEALE-ESG (Information, Aerospace, Economy pillars)
    - AMPEL360 certification framework
    - OPT-IN / PLUMA governance kernel

# ─────────────────────────────────────────────
# 2. Evaluation Criteria Map
# ─────────────────────────────────────────────
evaluation_criteria:
  - id: EXCELLENCE
    label: Excellence
    subsections:
      - id: EXCELLENCE-OA
        label: Objectives & Ambition
        deliverable_ref: DEL-01
      - id: EXCELLENCE-METH
        label: Methodology
        deliverable_ref: DEL-02

  - id: IMPACT
    label: Impact
    subsections:
      - id: IMPACT-PATH
        label: Pathways towards Impact
        deliverable_ref: DEL-03
      - id: IMPACT-MEAS
        label: Measures to Maximise Impact
        deliverable_ref: DEL-04

  - id: IMPLEMENTATION
    label: Quality and Efficiency of the Implementation
    subsections:
      - id: IMPL-WORK
        label: Work Plan and Resources
        deliverable_ref: DEL-05
      - id: IMPL-CAP
        label: Capacity of Participants and Consortium
        deliverable_ref: DEL-06

# ─────────────────────────────────────────────
# 3. Deliverable Registry
# ─────────────────────────────────────────────
deliverables:

  - id: DEL-01
    title: "Project Concept & Objectives"
    evaluation_criterion: EXCELLENCE
    evaluation_subsection: Objectives & Ambition
    status: draft
    description: >
      Defines the project vision, scientific and technological objectives,
      measurable ambition targets, and alignment with EuroHPC JU strategic
      priorities and the IDEALE-ESG framework.
    content:
      vision: >
        AI-BOOST aims to establish a European-sovereign, certification-grade
        AI framework that couples frontier large-scale models with
        high-performance computing infrastructure to accelerate simulation,
        testing, and validation workflows across aerospace, energy, and
        defence domains — under full governance, traceability, and
        environmental accountability.
      objectives:
        - id: OBJ-01
          label: Deterministic AI Governance at HPC Scale
          description: >
            Deliver a deterministic AI governance pipeline (PATH → MTL)
            that operates natively on EuroHPC infrastructure, ensuring
            every AI model, dataset, and inference result is traceable,
            gated, and auditable — from training through deployment.
          kpi: "100 % of AI artefacts gate-validated before operational use"
          alignment:
            - IDEALE pillar: Information (data sovereignty)
            - IDEALE pillar: Governance (deterministic pipelines)

        - id: OBJ-02
          label: Frontier Simulation Acceleration
          description: >
            Achieve order-of-magnitude acceleration of multi-physics
            simulation workflows (CFD, FEM, coupled aero-thermal-structural)
            by integrating AI surrogate models trained and validated on
            EuroHPC pre-exascale and exascale systems.
          kpi: "≥ 10× speed-up vs. baseline full-fidelity simulation"
          alignment:
            - IDEALE pillar: Aerospace (certification-grade engineering)
            - IDEALE pillar: Energy (hydrogen system simulation)

        - id: OBJ-03
          label: Certification-Grade AI for Safety-Critical Domains
          description: >
            Develop and demonstrate AI model qualification pathways
            compatible with EASA CS-25 / Part 21 and emerging EU AI Act
            requirements, producing evidence packages that satisfy
            mixed-boundary simplex admissibility (simplex-contract.yaml).
          kpi: "≥ 3 AI models qualified through evidence-gated pipeline"
          alignment:
            - IDEALE pillar: Aerospace (certification)
            - IDEALE pillar: Defence (dual-use awareness)
            - AMPEL360 framework: simplex classification

        - id: OBJ-04
          label: Sovereign European AI–HPC Integration
          description: >
            Ensure all training, inference, and data pipelines run on
            European HPC infrastructure with no dependency on
            extra-European cloud providers for safety-critical workloads,
            aligned with EU data sovereignty and export-control
            requirements.
          kpi: "100 % of safety-critical workloads on EuroHPC nodes"
          alignment:
            - IDEALE pillar: Information (data sovereignty)
            - IDEALE pillar: Defence (export control)
            - EuroHPC JU objective: strategic autonomy

        - id: OBJ-05
          label: Sustainability-Aware HPC Utilisation
          description: >
            Integrate environmental footprint tracking (energy consumption,
            carbon intensity) into every HPC job, enabling lifecycle
            assessment of AI model training and inference aligned with
            Digital Product Passport and ESG reporting requirements.
          kpi: "CO₂-per-inference metric tracked for all production models"
          alignment:
            - ESG constraint: Environment (LC14 circularity, DPP)
            - IDEALE pillar: Energy (renewable integration)

      ambition: >
        AI-BOOST goes beyond incremental improvement. It targets structural
        integration of AI governance, HPC infrastructure, and certification
        workflows into a single, auditable, European-sovereign pipeline.
        The ambition is not merely to use HPC for AI — but to make
        AI-on-HPC certification-grade, traceable, and environmentally
        accountable. No existing European project combines deterministic
        governance (PATH → MTL), mixed-boundary admissibility
        (simplex-contract), and frontier HPC at this integration depth.

      novelty:
        - Deterministic AI governance pipeline native to EuroHPC
        - Mixed-boundary simplex classification applied to AI model qualification
        - Capillary Merit Index (CMI) for contributor attribution in HPC-scale projects
        - Sustainability tracking integrated at the HPC job level

      eurohpc_alignment:
        - EuroHPC JU strategic priority: European AI sovereignty
        - EuroHPC JU strategic priority: Industrial uptake of HPC
        - EuroHPC JU strategic priority: Skills and talent development
        - Frontier AI Grand Challenge scope: Large-scale AI models on pre-exascale/exascale

  - id: DEL-02
    title: "Methodology"
    evaluation_criterion: EXCELLENCE
    evaluation_subsection: Methodology
    status: stub
    description: >
      Technical approach, work methodology, and risk management strategy.

  - id: DEL-03
    title: "Pathways towards Impact"
    evaluation_criterion: IMPACT
    evaluation_subsection: Pathways towards Impact
    status: stub
    description: >
      Expected scientific, economic, and societal impact pathways.

  - id: DEL-04
    title: "Measures to Maximise Impact"
    evaluation_criterion: IMPACT
    evaluation_subsection: Measures to Maximise Impact
    status: stub
    description: >
      Dissemination, exploitation, and communication plan.

  - id: DEL-05
    title: "Work Plan and Resources"
    evaluation_criterion: IMPLEMENTATION
    evaluation_subsection: Work Plan and Resources
    status: stub
    description: >
      Work packages, deliverables schedule, milestones, and resource allocation.

  - id: DEL-06
    title: "Capacity of Participants"
    evaluation_criterion: IMPLEMENTATION
    evaluation_subsection: Capacity of Participants and Consortium
    status: stub
    description: >
      Consortium composition, complementarity, and operational capacity.

  - id: DEL-07
    title: "Ethics and Security"
    evaluation_criterion: EXCELLENCE
    evaluation_subsection: Ethics and Security
    status: stub
    description: >
      Ethical considerations, dual-use assessment, data protection, and security.

  - id: DEL-08
    title: "Open Science and Data Management"
    evaluation_criterion: EXCELLENCE
    evaluation_subsection: Methodology
    status: stub
    description: >
      Open science practices, FAIR data management, and reproducibility.

  - id: DEL-09
    title: "Financial Plan"
    evaluation_criterion: IMPLEMENTATION
    evaluation_subsection: Financial Plan
    status: stub
    evaluation_mapping:
      status: unmapped_stub
      reason: >
        This deliverable is intentionally not yet mapped to an evaluation_criteria
        subsection; it serves as a planning stub for the separate financial annex.
    description: >
      Budget breakdown, cost justification, and financial sustainability.

---

# AI-BOOST — Application Strategy

**Call:** Frontier AI Grand Challenge · EuroHPC JU · GA 101135737
**Deadline:** 2026-04-13
**Machine-readable spec:** [`application-strategy.yaml`](application-strategy.yaml)

---

## 1. Project Concept

AI-BOOST targets the structural integration of **frontier AI models**, **European HPC infrastructure**, and **certification-grade governance** into a single auditable pipeline — enabling simulation acceleration, AI model qualification, and sustainability tracking across aerospace, energy, and defence domains.

IDEALE-ESG is the applicant action submitted to the AI-BOOST call. Its objective is to establish and deliver AMPEL360, a full-lifecycle programme in which an integrated product is designed, validated, certified, manufactured, and operated as the principal asset—under a single product identity spanning air transportation and space operations, including space tourism—through an auditable framework integrating frontier AI, deterministic-by-design execution, statistical and empirical validation, European HPC, and European governance.

---

## 2. Deliverable Map

| Deliverable | Title | Evaluation Criterion | Status |
|-------------|-------|---------------------|--------|
| **DEL-01** | Project Concept & Objectives | Excellence → Objectives & Ambition | draft |
| DEL-02 | Methodology | Excellence → Methodology | stub |
| **DEL-03** | Data Management Plan | Excellence → Data | draft |
| DEL-04 | Measures to Maximise Impact | Impact → Measures to Maximise Impact | stub |
| DEL-05 | Work Plan and Resources | Implementation → Work Plan and Resources | stub |
| DEL-06 | Capacity of Participants | Implementation → Capacity of Participants | stub |
| DEL-07 | Ethics and Security | Ethics → Ethics and Security | stub |
| DEL-08 | Pathways towards Impact | Impact → Pathways towards Impact | stub |
| DEL-09 | Financial Plan | Implementation → Financial Plan | stub |

---

## 3. DEL-01 — Project Concept & Objectives (Excellence → Objectives & Ambition)

### 3.1 Vision

AI-BOOST aims to establish a European-sovereign, certification-grade AI framework that couples frontier large-scale models with high-performance computing infrastructure to accelerate simulation, testing, and validation workflows across aerospace, energy, and defence domains — under full governance, traceability, and environmental accountability.

### 3.2 Objectives

| ID | Objective | KPI |
|----|-----------|-----|
| OBJ-01 | Deterministic AI Governance at HPC Scale | 100 % of AI artefacts gate-validated before operational use |
| OBJ-02 | Frontier Simulation Acceleration | ≥ 10× speed-up vs. baseline full-fidelity simulation |
| OBJ-03 | Certification-Grade AI for Safety-Critical Domains | ≥ 3 AI models qualified through evidence-gated pipeline |
| OBJ-04 | Sovereign European AI–HPC Integration | 100 % of safety-critical workloads on EuroHPC nodes |
| OBJ-05 | Sustainability-Aware HPC Utilisation | CO₂-per-inference metric tracked for all production models |

### 3.3 Ambition & Novelty

AI-BOOST goes beyond incremental improvement. It targets structural integration of AI governance, HPC infrastructure, and certification workflows into a single, auditable, European-sovereign pipeline. The ambition is not merely to use HPC for AI — but to make AI-on-HPC certification-grade, traceable, and environmentally accountable.

**Novel elements:**
- Deterministic AI governance pipeline (PATH → MTL) native to EuroHPC
- Mixed-boundary simplex classification applied to AI model qualification
- Capillary Merit Index (CMI) for contributor attribution in HPC-scale projects
- Sustainability tracking integrated at the HPC job level

### 3.4 EuroHPC JU Alignment

- European AI sovereignty
- Industrial uptake of HPC
- Skills and talent development
- Frontier AI Grand Challenge scope: large-scale AI models on pre-exascale/exascale systems

---

## 4. Framework Cross-References

| Reference | Location |
|-----------|----------|
| IDEALE-ESG framework | `README.md` (sections “1. Project Concept”–“4. Framework Cross-References”) |
| Mixed-boundary simplex | `simplex-contract.yaml` |
| Contributions taxonomy | `contributions-registry.yaml` |
| ESSA regulatory framework | `ESSA/essa-regulatory-framework.yaml` |
| Governance kernel | `00-PROGRAM/PLUMA/` |
