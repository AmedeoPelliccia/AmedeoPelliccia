# DEL-02 — State of the Art & Methodology

**Deliverable:** DEL-02  
**Application section:** Excellence → State of the Art + Methodology  
**Priority:** Critical  
**Parent strategy:** [`AI-BOOST/README.md`](README.md) (PR #8)  
**Status:** Draft  

---

## 1. State of the Art

### 1.1 Frontier AI Models — Global Landscape

As of early 2026 the frontier of large language models is defined by a small number of proprietary, non-European systems:

| Model | Organisation | Parameters | Architecture | Open Weights |
|-------|-------------|-----------|--------------|-------------|
| GPT-5 | OpenAI (US) | undisclosed (est. >1 T) | dense + MoE hybrid | No |
| Claude 3.5 Opus | Anthropic (US) | undisclosed | dense transformer | No |
| Gemini 2.0 Ultra | Google DeepMind (US) | undisclosed (est. >1 T MoE) | multi-modal MoE | No |
| Llama 3.1 405B | Meta (US) | 405 B | dense transformer | Yes (community) |
| DeepSeek-V3 | DeepSeek (CN) | 671 B total (37 B active) | MoE | Yes |
| Mixtral 8×22B | Mistral AI (FR/EU) | 176 B total (39 B active) | sparse MoE | Yes |

**Key observation:** No EU-sovereign model exists at the 400 B+ parameter frontier. Mixtral is the closest European contender but remains an order of magnitude below frontier scale. All 400 B+ open-weight models originate outside the EU, creating strategic dependency across regulated sectors (aerospace, healthcare, energy, defence).

### 1.2 Mixture-of-Experts — Architecture State of the Art

Sparse Mixture-of-Experts (MoE) architectures have become the dominant paradigm for frontier scaling:

- **Switch Transformer** (Google, 2022): demonstrated that sparsely-activated expert routing can scale to trillions of parameters while keeping per-token compute constant.
- **Mixtral** (Mistral AI, 2023–2024): proved that smaller MoE models can match or exceed dense models several times their active parameter count.
- **DBRX** (Databricks, 2024): fine-grained expert routing with 16 experts per layer, 4 active per token.
- **DeepSeek-V3** (DeepSeek, 2024–2025): 671 B total parameters with 37 B active, demonstrating efficient training on commodity GPU clusters via multi-head latent attention and auxiliary-loss-free load balancing.

Despite these advances, current MoE models share critical gaps relevant to the EU:

1. **Multilingual EU coverage**: no model is trained with balanced representation across all 24 EU official languages; most are English-dominant with incidental multilingual capability.
2. **Regulatory domain specialisation**: safety-critical sectors (aviation, space transport, energy regulation) are underrepresented in training corpora and evaluation benchmarks.
3. **Explainability in safety-critical contexts**: no frontier model provides auditable inference pathways compatible with EU AI Act transparency obligations for high-risk AI systems.
4. **EU sovereignty**: all 400 B+ models are trained on non-EU infrastructure under non-EU legal jurisdiction.

### 1.3 Quantum-Augmented Architectures — Research Frontier

Recent work in quantum-classical hybrid computation offers potential efficiency gains for specific sub-tasks:

- **Hilbert-Bell manifold formalism** (planned research module `hilbert_bell_manifold.py`, not yet part of this repository): a 12×12 spatial-quantum coupling framework with three-layer architecture (SpatialDomain, QuantumState, HamiltonianEvolver) and coherence-reduction mapping R(ρ) that classifies states as quantum, classical, or hybrid based on decoherence thresholds.
- **Quantum specialist expert configuration** (planned schema file `quantum-manifold.yaml`, not yet part of this repository): schema 1.1.0 specification for basis sets, coupling matrices, and decoherence parameters applicable to trajectory optimisation and manifold learning in expert routing.

These represent a novel research track — not a production dependency — for the quantum-augmented expert module (EXP-QNT) of GAIA-EU.

---

## 2. Methodology

### 2.1 GAIA-EU Architecture

**GAIA-EU** (General Aerospace Intelligence Architecture — European Union) is designed as a ≥ 400 B parameter sparse Mixture-of-Experts transformer with domain-specialist expert routing:

```
┌─────────────────────────────────────────────────────┐
│                    GAIA-EU (≥ 400B MoE)             │
│                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │ EXP-REG  │ │ EXP-ML   │ │ EXP-SCI  │            │
│  │Regulatory│ │Multilingu.│ │Scientific│            │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘            │
│       │             │            │                   │
│  ┌────┴─────┐ ┌────┴─────┐                         │
│  │ EXP-SAFE │ │ EXP-QNT  │                         │
│  │Safety/AI │ │Quantum   │                         │
│  │Act Gate  │ │(research)│                         │
│  └────┬─────┘ └────┬─────┘                         │
│       │             │                               │
│  ┌────┴─────────────┴──────────────────────┐        │
│  │      Expert Router (top-k gating)       │        │
│  └────────────────┬────────────────────────┘        │
│                   │                                 │
│  ┌────────────────┴────────────────────────┐        │
│  │   Coherence Gating Layer                │        │
│  │   (adapted from certified_dynamics)     │        │
│  └─────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────┘
```

**Expert modules:**

| Expert | Domain | Training data sources |
|--------|--------|----------------------|
| EXP-REG | Regulatory & legal (EACST, EASA, EUR-Lex) | EUR-Lex corpus, EASA AMC/GM library, ICAO annexes |
| EXP-ML | Multilingual (all 24 EU official languages + ICAO/EASA technical) | OSCAR multilingual corpus, EuroParl, national regulatory corpora |
| EXP-SCI | Scientific & engineering (aerospace, space, energy) | arXiv, PubMed, engineering standards (S1000D, ATA iSpec 2200) |
| EXP-SAFE | Safety certification (EU AI Act, EACST Parts, simplex gating) | EU AI Act text, EACST Parts catalogue, simplex-contract invariants |
| EXP-QNT | Quantum-augmented (trajectory, optimisation — research track) | Quantum computing literature, Hilbert-Bell manifold configuration |

**Coherence gating layer:** Conceptually modelled on a planned `certified_dynamics` module and `CertifiedAdmissibleSpace` abstraction, this layer provides per-inference safety classification. It evaluates whether each output satisfies domain-specific admissibility constraints before being returned to the user, providing the audit trail required by EU AI Act Article 53 (GPAI transparency).

### 2.2 Training Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Parallelism framework | Megatron-LM + DeepSpeed | Industry standard for 400 B+ scale; 3D parallelism (tensor, pipeline, data) |
| Precision | BF16 mixed precision | Optimal throughput on AMD MI300X and NVIDIA H100/A100 GPU architectures |
| Optimiser sharding | ZeRO Stage 3 | Memory-efficient optimiser state partitioning across thousands of GPUs |
| Checkpointing | Distributed async checkpointing | Fault tolerance for multi-week training runs on shared HPC infrastructure |
| Communication | InfiniBand NDR/XDR | Low-latency all-reduce required for MoE expert synchronisation |

**Target EuroHPC systems:**

| System | Location | GPU Architecture | Suitability |
|--------|----------|-----------------|-------------|
| MareNostrum 5 (ACC) | BSC, Spain | NVIDIA H100 | Primary training cluster |
| LUMI-G | CSC, Finland | AMD MI250X / MI300X | MoE expert parallelism |
| Leonardo Booster | CINECA, Italy | NVIDIA A100 | Data preprocessing + fine-tuning |
| Jupiter | JSC, Germany | NVIDIA GH200 | Large-batch evaluation + inference |

**Estimated compute:** ~10.7 M GPU-hours over 12 months (staged training: 70 B → 200 B → 400 B+).

### 2.3 Data Pipeline

**Tokeniser:** Multilingual Byte-Pair Encoding (BPE) with 256 k vocabulary, trained on a balanced sample across all 24 EU official languages plus ICAO/EASA technical English.

**Data sources and mix:**

| Source | Domain | Estimated tokens | Purpose |
|--------|--------|-----------------|---------|
| Common Crawl EU subset | General web (EU domains) | ~2 T | Base language modelling |
| OSCAR (EU languages) | Cleaned multilingual web text | ~1.5 T | Multilingual balance |
| EUR-Lex | EU legislation, case law | ~50 B | Regulatory expert (EXP-REG) |
| EASA AMC/GM + ICAO docs | Aviation safety regulation | ~5 B | Aviation domain (EXP-REG, EXP-SAFE) |
| arXiv + PubMed | Scientific literature | ~200 B | Scientific expert (EXP-SCI) |
| EuroParl proceedings | Parliamentary multilingual | ~10 B | Multilingual alignment (EXP-ML) |
| National regulatory corpora | Member state regulations | ~20 B | Multilingual regulatory (EXP-ML, EXP-REG) |

**Curation pipeline:**
1. Deduplication (MinHash + exact-match at document and paragraph level).
2. Quality filtering (perplexity scoring, language ID, content safety).
3. GDPR compliance: automated PII detection and removal; no personal data retained.
4. Domain-specific enrichment: regulatory cross-references, citation graph extraction for EUR-Lex and EASA corpora.

### 2.4 Scaling Strategy

Training follows a **Chinchilla-optimal compute schedule** with staged model scaling:

| Stage | Model size | Active params | Training tokens | Purpose |
|-------|-----------|---------------|----------------|---------|
| S1 | 70 B (dense seed) | 70 B | ~1.4 T | Architecture validation, hyperparameter search |
| S2 | 200 B (MoE, 8 experts) | ~50 B | ~2.0 T | Expert routing calibration, load balancing |
| S3 | 400 B+ (MoE, 16+ experts) | ~80 B | ~4.0 T | Full frontier training, multilingual + domain experts |

**Learning rate schedule:** Linear warmup (2 000 steps) → cosine decay to 10 % of peak LR.  
**Batch size ramp:** Start at 2 M tokens, ramp to 16 M tokens over first 10 % of training.

### 2.5 Evaluation Framework

GAIA-EU will be evaluated against frontier models on a comprehensive benchmark suite:

| Benchmark | Scope | Purpose |
|-----------|-------|---------|
| **MMLU-EU** (extension) | Regulatory subtasks across 24 EU languages | Multilingual knowledge + regulatory domain |
| **Regulatory NLP Suite** | EACST Parts compliance QA, EUR-Lex article retrieval, AMC/GM interpretation | Domain-specific safety-critical reasoning |
| **Aerospace Engineering Tasks** | Structural analysis, trajectory optimisation, certification document QA | Engineering expert capability |
| **TruthfulQA (EU)** | Factual accuracy on EU-specific topics | Truthfulness and bias detection |
| **BBQ Bias Benchmark (EU)** | Bias measurement adapted for EU cultural and linguistic contexts | Fairness across EU populations |
| **EU AI Act Compliance** | Annex XI documentation completeness, transparency report generation | Regulatory self-assessment |
| **Multilingual MT-Bench** | Open-ended generation quality across EU languages | Generation quality parity |

**Target performance:** Outperform leading open-weight models (Llama 3.1 405B, DeepSeek-V3) on all EU-domain benchmarks; match or exceed proprietary models (GPT-5, Claude 3.5 Opus) on regulatory NLP and multilingual tasks.

---

## 3. Novelty and Differentiation

| Dimension | Current SotA | GAIA-EU Advance |
|-----------|-------------|-----------------|
| EU sovereignty | No 400 B+ EU model | First EU-sovereign frontier model trained entirely on EuroHPC |
| Regulatory AI | Generic LLMs applied post-hoc | Domain-specialist experts (EXP-REG, EXP-SAFE) trained on structured regulatory corpora |
| Safety gating | External guardrails | Integrated coherence gating layer (certified_dynamics pattern) with per-inference audit trail |
| Multilingual parity | English-dominant | Balanced 24-language training with dedicated multilingual expert (EXP-ML) |
| Quantum-augmented | Separate quantum computing tools | Research-track quantum manifold expert (EXP-QNT) for trajectory and optimisation sub-tasks |
| EU AI Act compliance | Retrofitted documentation | Compliance by design: GPAI model card, Annex XI documentation, transparency report built into training pipeline |

---

## 4. Repository Assets Referenced

| Asset | Path | Role in DEL-02 |
|-------|------|---------------|
| Hilbert-Bell manifold | [`hilbert_bell_manifold.py`](../hilbert_bell_manifold.py) | Quantum-augmented manifold formalism — basis for EXP-QNT expert module |
| Quantum manifold config | [`quantum-manifold.yaml`](../quantum-manifold.yaml) | Basis sets, coupling matrices, decoherence thresholds for quantum expert |
| Certified dynamics (planned) | Planned asset (not yet in repo) | Coherence gating layer design pattern — admissibility classification (future implementation) |
| Simplex contract | [`simplex-contract.yaml`](../simplex-contract.yaml) | Formal safety contract methodology — gating invariants |

---

## 5. Key References

1. Fedus, W., Zoph, B., Shazeer, N. (2022). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity.* JMLR.
2. Jiang, A.Q. et al. (2024). *Mixtral of Experts.* Mistral AI Technical Report.
3. DeepSeek-AI. (2024). *DeepSeek-V3 Technical Report.*
4. Hoffmann, J. et al. (2022). *Training Compute-Optimal Large Language Models* (Chinchilla). DeepMind.
5. Shoeybi, M. et al. (2020). *Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism.* arXiv:1909.08053.
6. Rajbhandari, S. et al. (2020). *ZeRO: Memory Optimizations Toward Training Trillion Parameter Models.* SC20.
7. European Parliament and Council. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act.*
8. EuroHPC JU. (2024). *AI-BOOST Guidelines for Applicants — Frontier AI Grand Challenge.*
