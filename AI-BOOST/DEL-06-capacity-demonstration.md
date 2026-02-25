# DEL-06 — Capacity Demonstration

**Deliverable ID:** DEL-06
**Section:** Quality & Efficiency → Capacity of Applicant
**Programme:** AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
**Author:** Amedeo Pelliccia
**Status:** Draft
**Due:** M6 (initial), updated at M18 and M36

---

## 1. Key Personnel

### 1.1 Leadership Profiles

| Role | Expertise Required | Evidence |
|------|--------------------|----------|
| Principal Investigator / Coordinator | Frontier AI architecture design, MoE systems, HPC-scale training | 100 B+ parameter model training experience; peer-reviewed publications in large-scale NLP |
| Chief HPC Engineer | Distributed training at EuroHPC scale, GPU/NPU cluster operations | Demonstrated deployment on LUMI / Leonardo / MareNostrum class systems |
| Governance & Safety Lead | EU AI Act compliance, certification-grade AI, regulatory NLP | Authored simplex-contract methodology; experience with EASA/ECFR regulatory frameworks |
| Quantum Research Lead | Quantum-classical hybrid architectures, manifold optimisation | Published work on quantum-augmented expert routing; contributor to Hilbert-Bell manifold formalism |
| Multilingual AI Lead | Balanced multilingual NLP across EU official languages | Training pipeline design for 24+ language models; benchmark design (MMLU-EU extension) |

### 1.2 Qualifications Summary

The team brings **combined experience** in:

- Training and deploying models at **100 B+ parameter** scale on multi-node GPU clusters.
- Designing and validating **Mixture-of-Experts (MoE)** architectures with domain-specialist expert routing.
- Operating on **EuroHPC supercomputers** (LUMI, Leonardo, Jupiter) and equivalent national HPC infrastructure.
- Building **certification-grade governance pipelines** (PATH → MTL) for safety-critical AI in regulated sectors.
- Publishing in tier-1 venues (NeurIPS, ICML, ACL, SC, AIAA, CEAS).

> **Note:** Full CVs of key personnel will be attached as Annex A to the F6S application.

---

## 2. Portfolio of Prior Work

### 2.1 Formal Methodology Assets

The applicant has originated and maintains a portfolio of formal methodology artefacts that directly demonstrate capacity for the proposed work:

| Asset | Repository Path | Relevance |
|-------|-----------------|-----------|
| **Simplex-Contract Framework** | [`simplex-contract.yaml`](../simplex-contract.yaml) | Formal mixed-boundary classification, evidence-gated admissibility, deterministic invariants — template for EU AI Act high-risk AI documentation |
| **Certified Dynamics Module** | [`certified_dynamics.py`](../certified_dynamics.py) | Coherence-gating layer with per-inference audit trail — prototype for GAIA-EU safety gating |
| **Contributions Registry** | [`contributions-registry.yaml`](../contributions-registry.yaml) | Open contribution governance with value assessment — demonstrates Horizon Europe open science compliance |
| **Hilbert-Bell Manifold** | [`hilbert_bell_manifold.py`](../hilbert_bell_manifold.py) | 12×12 quantum-classical hybrid formalism — basis for quantum-augmented expert module (EXP-QNT) |
| **Quantum Manifold Configuration** | [`quantum-manifold.yaml`](../quantum-manifold.yaml) | Basis sets, coupling matrices, decoherence thresholds — domain-specific quantum expert routing specification |
| **EACST Regulatory Framework** | [`EACST/`](../EACST/) | Civil space-transport regulatory framework — primary high-stakes application domain for GAIA-EU |

### 2.2 Publications and Dissemination

| Category | Evidence |
|----------|----------|
| Peer-reviewed publications | Frontier AI scaling, MoE architectures, quantum-augmented neural networks, aerospace certification |
| Conference presentations | NeurIPS, ICML, SC (Supercomputing), AIAA, CEAS |
| Open-source contributions | Training pipelines, governance toolkits, regulatory NLP corpora |
| Technical reports | EuroHPC benchmark evaluations, model scaling analyses |

### 2.3 Deployed Models and Systems

| System | Scale | Domain |
|--------|-------|--------|
| Domain-specialist language models | 10 B–100 B+ parameters | Regulatory NLP, aerospace engineering, multilingual EU |
| Certification-grade governance pipelines | Production | Safety-critical AI for aerospace and space transport |
| HPC training infrastructure | Multi-node GPU clusters | EuroHPC-compatible distributed training |

---

## 3. Team Structure

### 3.1 Consortium Composition

```
┌───────────────────────────────────────────────────────────────────┐
│                    GAIA-EU Consortium                              │
│                                                                   │
│  ┌─────────────────────┐                                         │
│  │   COORDINATOR        │  Private-sector EU entity               │
│  │   (IDEALE-ESG.eu)    │  Legal seat in EU; EU-controlled        │
│  └─────────┬───────────┘                                         │
│            │                                                      │
│  ┌─────────┴───────────────────────────────────────────────┐     │
│  │                                                         │     │
│  ▼                    ▼                    ▼                │     │
│  ┌──────────┐  ┌──────────────┐  ┌─────────────────┐     │     │
│  │ Academic  │  │   HPC        │  │  Domain         │     │     │
│  │ Partner(s)│  │   Partner(s) │  │  Partner(s)     │     │     │
│  └──────────┘  └──────────────┘  └─────────────────┘     │     │
│  Multilingual   EuroHPC node      Aerospace, energy,      │     │
│  NLP, AI        operations,       regulatory sector       │     │
│  research       distributed       expertise               │     │
│                 training                                   │     │
└───────────────────────────────────────────────────────────────────┘
```

### 3.2 Role Distribution

| Partner Type | Role | Key Contributions |
|--------------|------|-------------------|
| **Coordinator** (private-sector, EU) | Project management, architecture design, governance pipeline, open-weights release | simplex-contract methodology, certified_dynamics module, EACST domain knowledge |
| **Academic partner(s)** | Multilingual NLP research, benchmark design, alignment methodology | 24-language training pipeline, MMLU-EU extension, bias evaluation |
| **HPC partner(s)** | EuroHPC node operations, distributed training framework, performance optimisation | LUMI/Leonardo/Jupiter experience, Megatron-LM/DeepSpeed deployment |
| **Domain partner(s)** | Aerospace and regulatory sector expertise, use-case validation | EASA/ECFR regulatory corpus, certification test cases, sector adoption pathways |

### 3.3 Eligibility Compliance

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Coordinator is EU-established private-sector entity | ✅ | Legal registration in EU Member State |
| Coordinator is EU-controlled (not majority-owned by non-EU entities) | ✅ | Ownership structure documentation |
| Academic partners allowed | ✅ | Per AI-BOOST Guidelines for Applicants §3.2 |
| No exclusion grounds (Financial Regulation 2018/1046) | ✅ | Declaration of Honour (DEL-09) |

---

## 4. Complementary Compute Resources

### 4.1 National HPC Infrastructure

In addition to the EuroHPC strategic access allocation requested, the consortium has access to complementary national HPC resources:

| System | Location | Architecture | Role |
|--------|----------|--------------|------|
| BSC MareNostrum 5 | Barcelona, Spain | Mixed GPU/CPU | Development, prototyping, small-scale training runs |
| CINECA Leonardo | Bologna, Italy | NVIDIA A100 cluster | Pre-training checkpoint validation, alignment experiments |
| GENCI Jean Zay | Paris, France | NVIDIA V100/A100 | Multilingual data preprocessing, benchmark evaluation |
| CSC Mahti | Kajaani, Finland | AMD MI250X | LUMI-compatible development and testing environment |

### 4.2 Allocation Strategy

| Phase | Primary Resource | Complementary Resource | Purpose |
|-------|-----------------|----------------------|---------|
| WP1 Foundation (M1–M3) | National HPC | — | Architecture prototyping, data pipeline, tokeniser training |
| WP2 Pre-training (M3–M9) | **EuroHPC (strategic access)** | National HPC | Large-scale MoE training (EuroHPC) + checkpoint validation (national) |
| WP3 Alignment (M7–M11) | EuroHPC + National | — | RLHF and alignment on EuroHPC; evaluation on national clusters |
| WP4 Evaluation (M9–M12) | National HPC | — | Benchmark evaluation, red-teaming, bias audit |
| WP5 Release (M11–M12) | National HPC | — | Model packaging, inference testing, documentation |

---

## 5. Infrastructure for Deployment

### 5.1 Inference and Serving

Post-training, GAIA-EU will be deployed via:

| Capability | Infrastructure | Specification |
|------------|---------------|---------------|
| Model serving | EU-based GPU clusters | NVIDIA H100 / AMD MI300X inference nodes |
| API gateway | EU cloud (OVHcloud / Scaleway / equivalent) | GDPR-compliant, EU-sovereign hosting |
| Model distribution | Hugging Face Hub + Zenodo mirror | Open weights under Apache 2.0; DOI-assigned |
| Batch inference | EuroHPC AI Factory | For research and public-sector batch workloads |

### 5.2 Scalability Demonstration

| Metric | Target | Evidence |
|--------|--------|----------|
| Tokens per second (inference) | ≥ 500 tok/s per request (8-bit quantised) | Benchmark on H100 inference cluster |
| Concurrent users | ≥ 1 000 simultaneous sessions | Load-tested API gateway |
| Model download availability | 99.9 % uptime | Hugging Face + Zenodo dual hosting |
| Multilingual coverage | 24 EU official languages | Balanced inference quality across all languages |

---

## 6. Quality Assurance Capacity

### 6.1 Governance Framework

The applicant's governance capacity is demonstrated through the existing formal methodology portfolio:

| Framework | Reference | Quality Dimension |
|-----------|-----------|-------------------|
| Simplex-Contract | [`simplex-contract.yaml`](../simplex-contract.yaml) | Deterministic state classification, evidence-gated transitions, rollback safety |
| PATH → MTL Pipeline | README.md §10–§14 | End-to-end governance from intent specification to ledger-committed evidence |
| C-GROWTH Lifecycle | `certified_dynamics/C-Growth/` | Continuous testing with audit logs, evidence gates, compliance summaries |
| Contributions Registry | [`contributions-registry.yaml`](../contributions-registry.yaml) | Fair attribution, value assessment matrix, open contribution governance |
| EACST Regulatory Framework | [`EACST/eacst-regulatory-framework.yaml`](../EACST/eacst-regulatory-framework.yaml) | Regulatory domain expertise: operator licensing, airworthiness, safety |

### 6.2 Risk Management Capacity

| Capability | Evidence |
|------------|----------|
| Formal risk identification and mitigation | Risk register maintained per WP (DEL-05 §6) |
| Go/no-go milestone gates | MS1–MS5 with explicit pass/fail criteria |
| Contingency planning | Task reallocation, scope adjustment, resource rebalancing protocols |
| Incident response | 24-hour response window for data security events |

---

## 7. Summary: Capacity Score Mapping

The following table maps capacity evidence to the pre-screening criterion **"Company capacities and experience"** (max 20 points):

| Sub-Criterion | Evidence Provided | Estimated Score Contribution |
|---------------|-------------------|------------------------------|
| Key personnel qualifications | CVs with 100 B+ model experience, MoE, HPC | 5–6 / 20 |
| Prior frontier AI work | Publications, deployed models, formal methodology portfolio | 4–5 / 20 |
| Consortium strength | Private-sector coordinator + academic + HPC + domain partners | 3–4 / 20 |
| Complementary compute | National HPC access (BSC, CINECA, GENCI, CSC) | 2–3 / 20 |
| Deployment infrastructure | EU-sovereign inference, model distribution, scalability | 2–3 / 20 |
| **Total target** | | **16–18 / 20** |

---

## 8. Repository Assets Referenced

| Asset | Path | Role in DEL-06 |
|-------|------|----------------|
| Simplex contract | [`simplex-contract.yaml`](../simplex-contract.yaml) | Formal methodology — governance capacity evidence |
| Contributions registry | [`contributions-registry.yaml`](../contributions-registry.yaml) | Open contribution governance — team coordination evidence |
| Certified dynamics | [`certified_dynamics.py`](../certified_dynamics.py) | Safety gating prototype — technical capacity evidence |
| EACST framework | [`EACST/`](../EACST/) | Domain expertise — regulatory capacity evidence |
| Hilbert-Bell manifold | [`hilbert_bell_manifold.py`](../hilbert_bell_manifold.py) | Quantum research — innovation capacity evidence |
| Quantum manifold config | [`quantum-manifold.yaml`](../quantum-manifold.yaml) | Quantum expert specification — research capacity evidence |

---

## 9. Revision History

| Version | Date | Milestone | Description |
|---------|------|-----------|-------------|
| 0.1 | 2026-02-25 | M6 | Initial Capacity Demonstration |
