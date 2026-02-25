# AI-BOOST Frontier AI Grand Challenge — Application Strategy

*Strategy for responding to the [AI-BOOST Frontier AI Grand Challenge](https://aiboost-project.eu/) (GA 101135737, EuroHPC JU).*

**Submission deadline:** 13 April 2026 at 17:00 Brussels time  
**Award:** Up to 2.5 % of EuroHPC computing capacity for 1 year (strategic access)  
**Eligibility:** EU-established, EU-controlled industrial entity; 400B+ parameter frontier AI model; modular (MoE) architecture  

---

## 1. Challenge Summary

The **Frontier AI Grand Challenge** is a prize competition run under the AI-BOOST programme (Horizon Europe CL4-2023-HUMAN-01-CNECT) jointly steered by the European Commission and EuroHPC JU. It seeks a single winning proposal to:

- Train a frontier-scale AI model (≥ 400B parameters, mixture-of-experts or equivalent modular architecture) on EuroHPC supercomputers.
- Outperform state-of-the-art models on relevant benchmarks.
- Release open weights and technical documentation for the EU public, scientific, and business communities.
- Comply with the EU AI Act, EU AI Continent Action Plan, and the ApplyAI Strategy.
- Prioritise European values: multilingualism across all EU languages, explainability, bias mitigation, and robustness.

---

## 2. Strategic Positioning

### 2.1. Why This Repository's Work Matters

This repository is the knowledge anchor for a European AI ecosystem spanning:

| Asset | Relevance |
|-------|-----------|
| **EACST regulatory framework** | Defines the high-stakes aerospace/space-transport domain that demands trustworthy, explainable frontier AI for safety-critical rule interpretation, compliance auditing, and risk classification. |
| **AMPEL360 / simplex-contract** | Formal contract and lifecycle framework for mixed-boundary safety systems — a direct template for EU AI Act high-risk AI documentation. |
| **certified_dynamics + C-GROWTH** | Certified admissibility / gating module: demonstrates capability to build safety-gated AI pipelines aligned with EU AI Act transparency and auditability requirements. |
| **Quantum-manifold (Hilbert-Bell)** | Advanced research basis for novel model architectures (quantum-augmented manifolds → potential efficiency innovations at scale). |
| **contributions-registry** | Evidence of open contribution methodology, FAIR data principles, and transparent governance — required by Horizon Europe open science rules. |

### 2.2. Proposed Model Concept: **GAIA-EU** (General Aerospace Intelligence Architecture — European Union)

A European open frontier AI model purpose-built for:

- **Safety-critical domain intelligence** (aerospace, space transport, energy, defence-adjacent civilian systems).
- **Multilingual regulation interpretation** across all EU languages + technical domain languages (ICAO English, EASA AMC/GM conventions).
- **Explainability by design**: every inference step auditable against a structured regulatory knowledge graph (aligned with EACST Parts + simplex-contract gates).
- **Open weights + EU sovereignty**: model weights and training methodology published under open licence; training pipeline reproducible on EuroHPC systems.

**Architecture headline:**
- ≥ 400B parameter mixture-of-experts (MoE) transformer.
- Domain-specialist expert routing: aviation/space regulatory, multilingual EU, scientific/engineering, safety certification.
- Coherence gating layer adapted from the certified_dynamics admissibility module.
- Quantum-augmented manifold layer (research track) for trajectory and optimisation tasks.

---

## 3. Application Deliverables (Sub-Issues)

The following 9 deliverables map to the required sections of the F6S application form. Each should be tracked as a separate sub-issue.

| # | Sub-Issue Title | Application Section | Priority |
|---|-----------------|---------------------|----------|
| DEL-01 | **Project Concept & Objectives** | Excellence → Objectives & Ambition | Critical |
| DEL-02 | **State of the Art & Methodology** | Excellence → State of the Art + Methodology | Critical |
| DEL-03 | **Data Management Plan** | Excellence → Data Management | Critical |
| DEL-04 | **Innovation & Impact Statement** | Innovation and Impact | Critical |
| DEL-05 | **Workplan, Milestones & Gantt Chart** | Quality & Efficiency → Workplan | Critical |
| DEL-06 | **Capacity Demonstration** | Quality & Efficiency → Capacity of Applicant | Critical |
| DEL-07 | **HPC Resource Justification** | Challenge-specific: GPU hours, scaling, EuroHPC fit | Critical |
| DEL-08 | **Open Science & EU AI Act Compliance** | Eligibility + Innovation | Required |
| DEL-09 | **Declaration of Honour** | Mandatory attachment (administrative) | Required |

> **Note:** One GitHub sub-issue should be opened per deliverable above, referencing this README as the parent strategy document.

---

## 4. Deliverable Detail: Content Guidance

### DEL-01 — Project Concept & Objectives

**What to write:**
- State the problem: Europe has no sovereign frontier AI model at 400B+ scale. Strategic dependency on US/non-EU providers creates risk across regulated sectors (aerospace, healthcare, energy).
- Main objectives:
  1. Train GAIA-EU (≥ 400B MoE) on EuroHPC within 12 months.
  2. Outperform leading global models on EU-domain benchmarks (regulatory NLP, multilingual reasoning, safety-critical decision support).
  3. Release open weights + technical documentation under an EU-compatible open licence.
  4. Establish a replicable EuroHPC training pipeline for future EU frontier models.
- Expected outcomes: sovereign open frontier model; EU AI Act compliant high-risk AI system card; EU aerospace/space domain capability demonstrated.

**Link to repository assets:** EACST framework (use case), simplex-contract (formal methodology), certified_dynamics (safety gating).

---

### DEL-02 — State of the Art & Methodology

**What to write:**
- State of the art: GPT-4/5 (OpenAI), Claude Opus (Anthropic), Gemini (Google) dominate at frontier scale. European initiatives (Mistral, BLOOM, Falcon, OpenGPT-X) exist but none at 400B+ scale.
- Gaps addressed: multilingual coverage of all 24 EU official languages; domain specialisation for regulated sectors; explainability/transparency required for EU AI Act high-risk applications; open weights.
- Methodology:
  - MoE architecture with 8–16 expert modules, sparse activation (efficiency).
  - Scaling laws calibration: optimal token/parameter ratio per Chinchilla approach, adapted for domain-specialist data.
  - Training stack: open-source framework (e.g., Megatron-LM / DeepSpeed) optimised for EuroHPC GPU/NPU topology.
  - Alignment pipeline: EU-values RLHF, constitutional AI (explainability constraints), multilingual reward modelling.
  - Evaluation: MMLU-EU (EU-specific benchmark extension), legal/regulatory NLP tasks, multilingual reasoning, aerospace safety scenario tests.

---

### DEL-03 — Data Management Plan

**What to write:**
- Training data categories:
  - Multilingual web corpora (EU language balance): Common Crawl EU subset, OSCAR, CulturaX.
  - Regulatory/legal texts: EUR-Lex, EASA AMC/GM, ECFR Part 450, ESA documents, EU Space Act materials.
  - Scientific/engineering literature: open-access aerospace journals, arXiv, ESA technical reports.
  - Proprietary/licensed: to be negotiated with partners; excluded from open weights dataset.
- Data governance: FAIR principles (Findable, Accessible, Interoperable, Reusable); data cards per dataset; bias assessment and documentation.
- Storage: EuroHPC object storage + national data infrastructure; retention for reproducibility.
- Privacy: no personal data; GDPR-compliant curation pipeline.

---

### DEL-04 — Innovation & Impact Statement

**What to write:**
- Innovation:
  - First EU frontier model at 400B+ scale with open weights.
  - Novel coherence-gating layer (adapted from certified_dynamics) ensuring verifiable safety properties for high-risk AI applications.
  - Quantum-augmented specialist experts (research track) for optimisation and trajectory tasks — potential next-generation efficiency gains.
  - EU AI Act compliance by design: every model inference is auditable against structured regulatory knowledge graph.
- Impact on EU AI ecosystem:
  - Reduces strategic dependency on non-EU frontier AI by providing an EU-sovereign alternative.
  - Unlocks AI adoption in regulated sectors (aerospace, space, healthcare, energy) where US models cannot be used due to data sovereignty/compliance constraints.
  - Reference implementation for EU AI Act–compliant high-risk AI documentation.
  - Public availability to EU research community, public authorities, and businesses via EuroHPC AI Factory services.
- Sectors: aerospace (EACST framework), space transport regulation, energy, autonomous systems.
- Bonuses targeted:
  - ✅ Open-source approach including open weights (+1 point)
  - ✅ Multimodal + strong multilingual capabilities across EU languages (+2 points)
  - ✅ European dimension (+2 points)

---

### DEL-05 — Workplan, Milestones & Gantt Chart

**Phases:**

| Phase | Months | Activities |
|-------|--------|-----------|
| **WP1: Foundation** | M1–M3 | Data curation, architecture design, EuroHPC environment setup, tokeniser training |
| **WP2: Pre-training** | M3–M9 | Large-scale MoE pre-training runs on EuroHPC; scaling law validation; checkpoint management |
| **WP3: Alignment** | M7–M11 | Instruction tuning, RLHF, multilingual alignment, safety evaluation; coherence-gating integration |
| **WP4: Evaluation** | M9–M12 | Benchmark evaluation (MMLU-EU, regulatory NLP, aerospace tasks), red-teaming, bias audit |
| **WP5: Release** | M11–M12 | Open weights packaging, model card, technical report, Final Report submission |

**Milestones:**
- MS1 (M3): Architecture frozen; EuroHPC allocation confirmed; data pipeline operational.
- MS2 (M6): 50% pre-training compute consumed; intermediate checkpoints validated.
- MS3 (M9): Pre-training complete; alignment training initiated.
- MS4 (M11): Alignment complete; benchmark results exceed threshold on all criteria.
- MS5 (M12): Open weights released; Final Report submitted.

*(Gantt chart to be produced as Attachment 2 to the F6S application form.)*

---

### DEL-06 — Capacity Demonstration

**What to provide:**
- CVs of key personnel demonstrating experience with 100B+ parameter model training, MoE architectures, and large-scale HPC usage.
- Portfolio of prior work: publications, deployed models (reference AMPEL360 / simplex-contract formal methodology; quantum-manifold research; certified_dynamics safety pipeline).
- Team structure: private-sector entity as coordinator + academic/research partner(s) contributing multilingual and domain-specialist expertise.
- Complementary compute: national HPC resources (e.g., BSC MareNostrum, CINECA Leonardo, or equivalent) to complement EuroHPC allocation.
- Infrastructure: GPU clusters for inference deployment, model serving at scale post-training.

---

### DEL-07 — HPC Resource Justification

**What to write:**
- Target scale: 400B parameter MoE (effective active parameters ~50B per forward pass, full parameter count 400B+).
- Estimated GPU hours:
  - Pre-training: ~10M GPU-hours on H100/MI300X class hardware (calibrated to 1.5T token training dataset at optimal Chinchilla ratio).
  - Alignment/RLHF: ~500K GPU-hours.
  - Evaluation and red-teaming: ~200K GPU-hours.
  - Total: ~11M GPU-hours → consistent with 2.5% EuroHPC strategic access over 12 months.
- Why top-tier EuroHPC is essential: frontier-scale training requires interconnect bandwidth (InfiniBand NDR/XDR) and memory bandwidth (HBM3) not available at smaller scale; the model cannot be trained in fragments without quality degradation.
- System adaptability: training stack designed to be portable across LUMI (AMD MI300X), Leonardo (NVIDIA A100), Jupiter (Intel/NVIDIA hybrid) and upcoming EuroHPC AI-Factory systems.

---

### DEL-08 — Open Science & EU AI Act Compliance

**What to write:**
- Open science: open weights under Apache 2.0 or CC-BY-4.0 compatible licence; training code on GitHub under OSI-approved licence; dataset cards and model cards published; paper submitted to arXiv within 30 days of model release.
- EU AI Act compliance:
  - GAIA-EU is classified as a general-purpose AI model (GPAI) and also covers a high-risk application domain (aerospace/space regulatory AI).
  - Technical documentation per Annex XI / Article 53 of the EU AI Act.
  - Transparency report and conformity assessment pathway documented before deployment in regulated sector use cases.
  - Human oversight provisions in coherence-gating layer (certified_dynamics design pattern).
- Horizon Europe open science principles: FAIR data management plan (DEL-03), preprints, open datasets where IP-permissible.

---

### DEL-09 — Declaration of Honour

**Administrative requirement:**
- Download the Declaration of Honour from the AI-BOOST website: https://aiboost-project.eu/
- Complete and sign by the legal representative of the coordinating entity.
- Confirm compliance with all eligibility criteria (EU establishment, EU control, exclusion grounds clear under Financial Regulation 2018/1046).
- Attach as Attachment 1 to the F6S application form.

---

## 5. Pre-Screening Scoring Guide (60-point threshold)

| Criterion | Max Points | Our Target |
|-----------|-----------|------------|
| European Dimension | 15 | 14–15 (EU sovereignty angle, EACST/aerospace use case, open model for EU public) |
| Company capacities and experience | 20 | 16–18 (formal methodology portfolio, prior AI/engineering models, HPC experience) |
| Soundness of the proposal | 15 | 13–15 (detailed architecture, scaling plan, validated methodology) |
| Potential of adoption and scalability | 10 | 9–10 (regulated sectors demand + open weights availability) |
| **Total** | **60** | **52–58** |

---

## 6. Evaluation Criteria & Bonus Strategy (0–5 per criterion + bonuses)

| Criterion | Weight | Strategy |
|-----------|--------|---------|
| Excellence | 0–5 | Strong scientific merit via formal methodology (simplex-contract), novel coherence gating, quantum-augmented experts |
| Innovation and Impact | 0–5 | EU sovereignty narrative, regulated-sector impact, EACST framework integration, bonus targeting |
| Quality & Efficiency of Implementation | 0–5 | Detailed Gantt, proven team (100B+ model experience), clear EuroHPC resource plan |
| **Bonuses** | | Open weights (+1), Multimodal+multilingual all EU languages (+2), European dimension (+2) = **+5 points** |

Threshold: each criterion ≥ 3; total ≥ 10 (excl. bonuses). Target: **4.5 / 4.5 / 4.5 + 5 bonus = 18.5 effective points**.

---

## 7. Timeline & Action Plan

| Date | Action |
|------|--------|
| By 10 Mar 2026 | Draft DEL-01, DEL-02, DEL-06 completed and reviewed |
| By 20 Mar 2026 | DEL-03, DEL-04, DEL-07 completed |
| By 31 Mar 2026 | DEL-05 (Gantt + workplan tables) + DEL-08 completed |
| By 5 Apr 2026 | DEL-09 (Declaration of Honour) signed and ready |
| By 10 Apr 2026 | Full application assembled and reviewed on F6S platform (preview mode) |
| **13 Apr 2026, 17:00** | **SUBMISSION DEADLINE — submit via F6S** |

---

## 8. Key References

- [AI-BOOST Frontier AI Grand Challenge — F6S](https://www.f6s.com/ai-boost-frontier-ai-grand-challenge)
- [AI-BOOST Project website](https://aiboost-project.eu/)
- [EuroHPC JU — About](https://eurohpc-ju.europa.eu/)
- [EU AI Continent Action Plan](https://digital-strategy.ec.europa.eu/en/policies/ai-continent-action-plan)
- [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689)
- [Horizon Europe Open Science requirements](https://rea.ec.europa.eu/open-science_en)
- [EACST Regulatory Framework](../EACST/README.md) — primary use-case domain
- [simplex-contract.yaml](../simplex-contract.yaml) — formal methodology evidence
- [contributions-registry.yaml](../contributions-registry.yaml) — open contribution governance

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`application-strategy.yaml`](application-strategy.yaml) | Machine-readable strategy spec |
| [`../EACST/README.md`](../EACST/README.md) | Primary application domain (civil space transport regulation) |
| [`../simplex-contract.yaml`](../simplex-contract.yaml) | Formal safety contract methodology (capacity evidence) |
