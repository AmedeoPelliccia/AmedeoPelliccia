---
deliverable:
  id: "DEL-02"
  title: "State of the Art & Methodology"
  version: "1.0.0"
  status: "Draft"
  authors: []
  date: "2026-03"
  work_package: "WP1"
  description: >
    Overview of the global frontier AI landscape and the methodology
    for the GAIA-AIR-EU architecture and training programme.

state_of_the_art:
  global_landscape:
    description: >
      Overview of the current frontier AI ecosystem and geopolitical
      distribution of large-scale foundation model development.

  us_frontier:
    providers:
      - organization: "OpenAI"
        models:
          - "GPT-5.4 Thinking"
          - "GPT-5.4 Pro"
      - organization: "Anthropic"
        models:
          - "Claude Opus 4.6"
          - "Claude Sonnet 4.6"
      - organization: "Google DeepMind"
        models:
          - "Gemini 3.1 Pro"

  east_asian_frontier:
    providers:
      - organization: "DeepSeek"
        models:
          - "DeepSeek-V3.2"
          - "DeepSeek-V3.2-Speciale"
      - organization: "Alibaba"
        models:
          - "Qwen3.5"
          - "Qwen3-Max-Thinking"
      - organization: "Z.ai"
        models:
          - "GLM-5"

  european_frontier:
    providers:
      - organization: "Mistral AI"
        models:
          - "Mistral Large"
          - "Mixtral"
      - organization: "Aleph Alpha"
        models:
          - "Luminous"
      - organization: "LAION / Open initiatives"
        models:
          - "Open-weight ecosystem"

  middle_east_sovereign:
    uae_models:
      - organization: "Technology Innovation Institute"
        models:
          - "Falcon-H1 Arabic"
      - organization: "MBZUAI / Inception / Cerebras"
        models:
          - "Jais 2"
      - organization: "G42 / MBZUAI"
        models:
          - "K2 Think V2"

    saudi_models:
      - organization: "HUMAIN / SDAIA"
        models:
          - "ALLaM"

  eu_gaps:
    description: >
      Structural gaps identified in the EU AI ecosystem relative to
      frontier-scale model development and deployment.

methodology:
  gaia_air_eu:
    full_name: "General Aerospace Intelligence Architecture — European Union"
    expert_modules:
      - "EXP-REG"
      - "EXP-ML"
      - "EXP-SCI"
      - "EXP-SAFE"
      - "EXP-QNT"

    coherence_gating:
      purpose: >
        Safety and reasoning validation layer for expert outputs
        prior to synthesis.

  moe_architecture:
    type: "Domain-specialist Mixture-of-Experts"

  quantum_augmented:
    status: "Exploratory research"
    description: >
      Investigation of quantum-assisted optimisation and inference
      acceleration methods.

  training_stack:
    description: >
      Distributed training pipeline integrating EuroHPC compute,
      curated datasets, and staged scaling.

  eurohpc_systems:
    systems:
      - hub_city: "Barcelona"
        system: "MareNostrum 5"
      - hub_city: "Kajaani"
        system: "LUMI"
      - hub_city: "Bologna"
        system: "Leonardo"
      - hub_city: "Jülich"
        system: "JUPITER"

  data_pipeline:
    description: >
      Multilingual corpus acquisition, curation, and regulatory
      compliance pipeline.

  scaling_strategy:
    description: >
      Progressive scaling roadmap targeting frontier-scale
      model capability.

  evaluation_framework:
    description: >
      Benchmarking across multilingual reasoning, scientific
      problem solving, and regulated-domain tasks.

novelty:
  - "Sovereign European frontier model architecture"
  - "Domain-specialised MoE design"
  - "Integrated safety and coherence gating"
  - "EuroHPC-native training pipeline"

repository_assets:
  - "architecture_specifications"
  - "training_recipes"
  - "evaluation_benchmarks"
  - "dataset_documentation"

references:
  core:
    - "Frontier model publications"
    - "EuroHPC technical documentation"
    - "EU AI Act regulatory material"

  east_asian_middle_east:
    - "DeepSeek documentation"
    - "Qwen research publications"
    - "GLM research publications"
    - "Falcon / Jais / ALLaM releases"
---


| Field | Value |
|-------|-------|
| **Deliverable** | DEL-02 |
| **Title** | State of the Art & Methodology |
| **Programme** | Frontier AI Grand Challenge |
| **Grant Agreement** | GA 101135737 (EuroHPC JU) |
| **Section** | Excellence → State of the Art + Methodology |
| **Priority** | Critical |
| **Status** | Draft |
| **Author** | Amedeo Pelliccia |
| **Version** | 1.0.0 |
| **Date** | 2026-03-10 |
| **Machine-readable** | [`sota-methodology.yaml`](sota-methodology.yaml) |

---

## 1. State of the Art

### 1.1 Frontier AI Models — Global Landscape

As of March 2026, the frontier of large language models is defined by a small number of proprietary systems alongside increasingly significant open-weight and sovereign alternatives across multiple regions:

| Model | Organisation | Parameters | Architecture | Open Weights |
|-------|-------------|-----------|--------------|-------------|
| GPT-5.4 family | OpenAI (US) | undisclosed (est. >1 T) | dense + MoE hybrid | No |
| Claude 4.6 family | Anthropic (US) | undisclosed | dense transformer | No |
| Gemini 3.1 family | Google DeepMind (US) | undisclosed (est. >1 T MoE) | multi-modal MoE | No |
| Llama 3.1 405B | Meta (US) | 405 B | dense transformer | Yes (community) |
| **DeepSeek-V3.2 / V3.2-Speciale** | DeepSeek (CN) | 671 B total (37 B active) | MoE | Yes |
| **Qwen3.5 / Qwen3-Max-Thinking** | Alibaba (CN) | undisclosed | MoE | Yes |
| **GLM-5** | Z.ai (CN) | undisclosed | dense + agentic | Yes |
| Mixtral 8×22B | Mistral AI (FR/EU) | 176 B total (39 B active) | sparse MoE | Yes |
| **Falcon-H1 Arabic** | TII (UAE) | undisclosed | dense transformer | Yes |
| **Jais 2** | MBZUAI / Inception / Cerebras (UAE) | undisclosed | dense transformer | Yes |
| **K2 Think V2** | MBZUAI / G42 / IFM (UAE) | undisclosed | reasoning system | Partial |
| **HUMAIN–ALLaM Stack** | HUMAIN / SDAIA (SA) | undisclosed | multimodal LLM | Via watsonx/DEEM |

**Key observation:** Beyond US and European frontier systems, the 2026 state of the art also includes major East Asian entrants such as DeepSeek-V3.2 / V3.2-Speciale, Qwen3.5 / Qwen3-Max-Thinking, and GLM-5, alongside an increasingly significant Middle East sovereign-model ecosystem including Falcon-H1 Arabic, Jais 2, K2 Think V2, and the Saudi HUMAIN–ALLaM stack. As of March 2026, no EU-sovereign model has been publicly documented at the 400 B+ scale. Mixtral is the closest European contender but remains an order of magnitude below frontier scale.

### 1.2 East Asian Frontier Entrants

East Asian AI development has matured substantially, with Chinese laboratories now producing systems that compete directly with Western frontier models on capability benchmarks:

**DeepSeek-V3.2 / V3.2-Speciale** — DeepSeek's latest official reasoning-first release, extending the V3 architecture with enhanced reasoning chains and chain-of-thought optimization. The open-weights release strategy positions DeepSeek as a key contributor to the open frontier ecosystem.

**Qwen3.5 / Qwen3-Max-Thinking** — Alibaba's current flagship family, with Qwen3-Max-Thinking extending capabilities with explicit reasoning optimization for complex multi-step problem solving. Notable for strong multilingual performance across Asian languages.

**GLM-5** — Z.ai's latest flagship model oriented toward long-horizon agentic engineering and systems tasks. Unlike general-purpose chat models, GLM-5 emphasizes sustained reasoning over extended interactions, making it particularly suited for software engineering and workflow automation.

### 1.3 Middle East Sovereign-Model Ecosystem

The Middle East has emerged as a serious sovereign-model cluster, not as a marginal regional footnote:

**Falcon-H1 Arabic** (TII, Abu Dhabi) — Explicitly positioned as establishing world-leading Arabic AI model capability. Open-weight release with specific optimization for Arabic language understanding and generation.

**Jais 2** (MBZUAI / Inception / Cerebras) — Arabic-first frontier model building upon the original Jais success, delivering enhanced Arabic-first capability through partnership with Cerebras for efficient training.

**K2 Think V2** (MBZUAI / G42 / IFM) — Sovereign reasoning system explicitly positioned to compete with Western reasoning models while maintaining regional sovereignty. Represents the UAE's entry into dedicated reasoning-focused frontier systems.

**HUMAIN–ALLaM Stack** (Saudi Arabia) — Public PIF material states that HUMAIN is building advanced AI models including ALLaM, described as a multimodal Arabic large language model co-developed with SDAIA. Organizations in Saudi Arabia can access ALLaM through watsonx and DEEM Cloud platforms, representing a hybrid accessibility model rather than a fully closed API-only system.

**Terminology note:** The term "Middle East sovereign-model ecosystem" is preferred over "proprietary Middle East models" because the UAE leaders (Falcon-H1 Arabic, Jais 2, K2 Think V2) are largely open or open-weight, while the clearest commercial/closed sovereign stack publicly signaled is HUMAIN.

### 1.4 Mixture-of-Experts — Architecture State of the Art

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

### 1.5 Quantum-Augmented Architectures — Research Frontier

Recent work in quantum-classical hybrid computation offers potential efficiency gains for specific sub-tasks:

- **Hilbert-Bell manifold formalism** (planned research module `hilbert_bell_manifold.py`): Explores quantum-classical hybrid states for trajectory optimisation via a 12×12 spatial-quantum coupling framework.
- **Quantum specialist expert configuration** (planned schema file `quantum-manifold.yaml`): Schema 1.1.0 specification for basis sets, coupling matrices, and decoherence.

**Note:** The quantum-augmented expert module (EXP-QNT) is an **exploratory research work package (non-critical to core deliverables)**. EXP-QNT will be developed in parallel; core model performance does not depend on its success.

---

## 2. Methodology

### 2.1 GAIA-AIR-EU Architecture — AI Infrastructure Reference

**GAIA-AIR-EU** (General Aerospace Intelligence Architecture — European Union) is designed as a ≥ 400 B parameter sparse Mixture-of-Experts transformer with domain-specialist expert routing:

```
┌─────────────────────────────────────────────────────┐
│                GAIA-AIR-EU (≥ 400B MoE)             │
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
│  │   (planned certified_dynamics module)  │        │
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

**Coherence gating layer:** Conceptually modelled on a planned `certified_dynamics` module and `CertifiedAdmissibleSpace` abstraction, this layer provides per-inference safety classification. It is designed specifically to support transparency and documentation obligations for General Purpose AI (GPAI) models under Regulation (EU) 2024/1689 (Annex XI), providing an auditable trail for safety-critical domain inferences.

### 2.2 Training Stack

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Parallelism framework | Megatron-LM + DeepSpeed | Industry standard for 400 B+ scale; 3D parallelism (tensor, pipeline, data) |
| Precision | BF16 mixed precision | Optimal throughput on AMD MI300X and NVIDIA H100/A100 GPU architectures |
| Optimiser sharding | ZeRO Stage 3 | Memory-efficient optimiser state partitioning across thousands of GPUs |
| Checkpointing | Distributed async checkpointing | Fault tolerance for multi-week training runs on shared HPC infrastructure |
| Communication | InfiniBand NDR/XDR | Low-latency all-reduce required for MoE expert synchronisation |

**Target EuroHPC systems:**

| System | Hosting Institution | Hub City | GPU Architecture | Suitability |
|--------|---------------------|----------|-----------------|-------------|
| MareNostrum 5 (ACC) | BSC | Barcelona | NVIDIA H100 | Primary training cluster |
| LUMI-G | CSC | Kajaani | AMD MI250X / MI300X | MoE expert parallelism |
| Leonardo Booster | CINECA | Bologna | NVIDIA Ampere-based GPUs | Data preprocessing + fine-tuning |
| Jupiter | JSC | Jülich | NVIDIA GH200 | Large-batch evaluation + inference |

*Note: The above are target platforms; final allocation is pending EuroHPC review. Training will be **distributed** across multiple sites with checkpoint synchronization and federated data preprocessing.*

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

GAIA-AIR-EU will be evaluated against frontier models on a comprehensive benchmark suite:

| Benchmark | Scope | Purpose |
|-----------|-------|---------|
| **MMLU-EU** (extension) | Regulatory subtasks across 24 EU languages | Multilingual knowledge + regulatory domain |
| **Regulatory NLP Suite** | EACST Parts compliance QA, EUR-Lex article retrieval, AMC/GM interpretation | Domain-specific safety-critical reasoning |
| **Aerospace Engineering Tasks** | Structural analysis, trajectory optimisation, certification document QA | Engineering expert capability |
| **TruthfulQA (EU)** | Factual accuracy on EU-specific topics | Truthfulness and bias detection |
| **BBQ Bias Benchmark (EU)** | Bias measurement adapted for EU cultural and linguistic contexts | Fairness across EU populations |
| **EU AI Act Compliance** | Annex XI documentation completeness, transparency report generation | Regulatory self-assessment |
| **Multilingual MT-Bench** | Open-ended generation quality across EU languages | Generation quality parity |

**Target performance:**
- **Open-weight models:** Outperform Llama 3.1 405B on MMLU-EU regulatory subtasks and DeepSeek-V3 on EU-domain engineering benchmarks.
- **Proprietary models:** Match GPT-5.4 Thinking / Pro and Claude Opus 4.6 / Sonnet 4.6 on dedicated EU regulatory NLP benchmarks (e.g., EACST QA, EUR-Lex retrieval) where domain-specialised MoE routing provides a competitive advantage.

---

## 3. Novelty and Differentiation

| Dimension | Current SotA | GAIA-AIR-EU Advance |
|-----------|-------------|-----------------|
| EU sovereignty | No 400 B+ EU model | First EU-sovereign frontier model trained entirely on EuroHPC |
| Regulatory AI | Generic LLMs applied post-hoc | Domain-specialist experts (EXP-REG, EXP-SAFE) trained on structured regulatory corpora |
| Safety gating | External guardrails | Integrated coherence gating layer (planned certified_dynamics design) with per-inference audit trail |
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

### Additional References — East Asian & Middle East Frontier Models

9. DeepSeek API Documentation. *DeepSeek-V3.2 Release.* [https://api-docs.deepseek.com/news/news251201](https://api-docs.deepseek.com/news/news251201)
10. Technology Innovation Institute (TII). *Falcon H1 Arabic AI Model Launched by Abu Dhabi's TII.* [https://www.tii.ae/news/abu-dhabis-tii-launches-falcon-h1-arabic-establishing-worlds-leading-arabic-ai-model](https://www.tii.ae/news/abu-dhabis-tii-launches-falcon-h1-arabic-establishing-worlds-leading-arabic-ai-model)
11. Public Investment Fund (PIF) Saudi Arabia. *HUMAIN Portfolio Overview.* [https://www.pif.gov.sa/en/our-investments/our-portfolio/humain/](https://www.pif.gov.sa/en/our-investments/our-portfolio/humain/)

