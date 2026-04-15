---

# innovation-and-impact.yaml
# Machine-readable specification for DEL-04 Innovation and Impact.
# Programme: AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
# Section: Impact → Measures to Maximise Impact
# Reference: AI-BOOST/DEL-04-innovation-and-impact.md
# Author: Amedeo Pelliccia

schema_version: "1.0.0"
document_type: innovation_and_impact
last_updated: "2026-02-25T00:00:00Z"

# ─────────────────────────────────────────────
# 1. Deliverable Metadata
# ─────────────────────────────────────────────
deliverable:
  id: DEL-04
  title: Innovation and Impact
  section: "Impact → Measures to Maximise Impact"
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
# 2. Expected Impact
# ─────────────────────────────────────────────
impact:
  scientific:
    - id: SCI-01
      area: Sovereign Frontier AI
      outcome: >
        First EU-sovereign ≥ 400 B parameter MoE model trained
        entirely on EuroHPC infrastructure.
      indicator: "Peer-reviewed publication; model card published"
    - id: SCI-02
      area: Certification-Grade AI Governance
      outcome: >
        Deterministic governance pipeline (PATH → MTL) validated for
        safety-critical AI in regulated sectors.
      indicator: "≥ 3 AI models gate-qualified; methodology adopted by ≥ 1 standards body"
    - id: SCI-03
      area: Quantum-Augmented Expert Routing
      outcome: >
        Novel quantum-classical hybrid approach to expert selection
        and trajectory optimisation.
      indicator: "≥ 2 peer-reviewed publications on quantum manifold methodology"
    - id: SCI-04
      area: Multilingual Regulatory NLP
      outcome: >
        Balanced 24-language training with regulatory domain specialists.
      indicator: "Benchmark scores published; MMLU-EU extension contributed upstream"

  economic:
    - id: ECO-01
      area: European AI Industry Competitiveness
      outcome: >
        Reduction of strategic dependency on non-EU frontier model providers.
      indicator: "≥ 2 EU industrial partners adopting GAIA-EU outputs"
    - id: ECO-02
      area: HPC Service Market Expansion
      outcome: >
        Demonstration of certification-grade AI workloads on EuroHPC.
      indicator: "≥ 1 new commercial HPC service offering derived from project toolchain"
    - id: ECO-03
      area: Aerospace Certification Cost Reduction
      outcome: >
        AI-accelerated simulation reducing certification cycle time.
      indicator: "≥ 30 % reduction in simulation-to-certification elapsed time (demonstrated)"
    - id: ECO-04
      area: AI Act Compliance Tooling
      outcome: >
        Reusable compliance-by-design framework for GPAI model providers.
      indicator: "Open-source compliance toolkit released"

  societal:
    - id: SOC-01
      area: European Digital Sovereignty
      outcome: >
        Reduced dependency on extra-EU AI infrastructure for critical sectors.
      indicator: "Policy brief published; uptake metric tracked"
    - id: SOC-02
      area: Environmental Accountability
      outcome: >
        CO₂-per-inference tracking normalised across HPC workloads.
      indicator: "Sustainability dashboard public; methodology contributed to Green Deal Digital"
    - id: SOC-03
      area: Skills and Talent Development
      outcome: >
        Training of next-generation EU researchers in frontier AI + HPC.
      indicator: "≥ 10 doctoral/postdoctoral researchers trained; open courseware published"
    - id: SOC-04
      area: Multilingual Access
      outcome: >
        Equal-quality AI services across EU official languages.
      indicator: "Language parity scores published for all 24 EU languages"

# ─────────────────────────────────────────────
# 3. Dissemination Plan
# ─────────────────────────────────────────────
dissemination:
  audiences:
    - id: AUD-SCI
      label: Scientific community
      channels: [peer-reviewed journals, conferences, preprint servers]
    - id: AUD-IND
      label: Industry (aerospace, energy, defence)
      channels: [trade conferences, bilateral workshops, demonstrators]
    - id: AUD-POL
      label: Policy makers and regulators
      channels: [policy briefs, regulatory sandboxes, standardisation bodies]
    - id: AUD-PUB
      label: General public
      channels: [project website, social media, press releases]
    - id: AUD-OSS
      label: Open-source / developer community
      channels: [GitHub, Hugging Face, Zenodo]

  publication_strategy:
    open_access: true
    oa_compliance: "Horizon Europe Article 17"
    preprint_policy: "arXiv or HAL within one week of submission"
    target_venues:
      - name: "NeurIPS / ICML / ICLR"
        type: conference
        relevance: "Frontier AI architecture, MoE scaling"
      - name: "ACL / EMNLP"
        type: conference
        relevance: "Multilingual NLP, regulatory language"
      - name: "SC (Supercomputing)"
        type: conference
        relevance: "HPC scaling, distributed training"
      - name: "Aerospace journals (AIAA, CEAS)"
        type: journal
        relevance: "Certification-grade AI for aerospace"
      - name: "Nature Machine Intelligence"
        type: journal
        relevance: "High-impact cross-disciplinary"

  conference_target: "≥ 4 international conferences per year"

# ─────────────────────────────────────────────
# 4. Exploitation Plan
# ─────────────────────────────────────────────
exploitation:
  pathways:
    - id: EXP-01
      result: "GAIA-EU model weights (open)"
      route: "Open release on Hugging Face under permissive licence"
      owner: coordinator
      timeline: "M24 (initial), M36 (final)"
    - id: EXP-02
      result: "Deterministic governance pipeline"
      route: "Integration into AMPEL360 certification framework; licensing to industrial partners"
      owner: coordinator
      timeline: "M18 onwards"
    - id: EXP-03
      result: "Regulatory NLP benchmarks (MMLU-EU)"
      route: "Contribution to MLCommons; adoption by EU AI Office for evaluation"
      owner: "coordinator + NLP partner"
      timeline: "M12 onwards"
    - id: EXP-04
      result: "AI Act compliance toolkit"
      route: "Open-source release; commercial support offering by SME partners"
      owner: "SME partner(s)"
      timeline: "M24 onwards"
    - id: EXP-05
      result: "HPC training recipes"
      route: "Publication as reproducible pipelines on EuroHPC documentation"
      owner: "HPC partner"
      timeline: "M18 onwards"
    - id: EXP-06
      result: "CO₂-per-inference methodology"
      route: "Standardisation proposal to CEN/CENELEC; integration with Digital Product Passport"
      owner: "coordinator + sustainability partner"
      timeline: "M24 onwards"

  ip_strategy:
    default_licence_code: Apache-2.0
    default_licence_data: CC-BY-4.0
    protected_results_protocol: "60-day consortium opt-in window before open publication"
    joint_ownership: "Horizon Europe default rules (Regulation (EU) 2021/695, Article 40)"
    access_rights_duration: "project duration + 5 years"
    ip_governance_ref: contributions-registry.yaml

  standardisation:
    - body: CEN/CENELEC
      group: "JTC 21 AI"
      contribution: "AI governance pipeline specification; deterministic gating methodology"
    - body: "EUROCAE / SAE"
      group: "ED-12C / DO-178C AI supplement"
      contribution: "Certification-grade AI evidence packages for aerospace"
    - body: ISO
      group: "ISO/IEC 42001 AI Management"
      contribution: "Alignment evidence for AI management system"
    - body: "W3C / OASIS"
      group: "ML model documentation"
      contribution: "GPAI model card schema extension"
    - body: ECSS
      group: "Space segment AI"
      contribution: "Quantum-augmented expert module specification"

# ─────────────────────────────────────────────
# 5. Communication Plan
# ─────────────────────────────────────────────
communication:
  objectives:
    - "Raise awareness of European AI sovereignty and the role of EuroHPC in frontier AI"
    - "Engage stakeholders across scientific, industrial, regulatory, and public audiences"
    - "Demonstrate impact through measurable outcomes (publications, adoptions, policy influence)"

  channels:
    - channel: Project website
      frequency: continuous
      responsibility: "coordinator (WP lead)"
    - channel: "Social media (LinkedIn, X/Twitter, Mastodon)"
      frequency: "≥ 2 posts/week"
      responsibility: communication officer
    - channel: Newsletter
      frequency: quarterly
      responsibility: communication officer
    - channel: Press releases
      frequency: "at key milestones (M6, M18, M36)"
      responsibility: coordinator
    - channel: Public demonstrators
      frequency: "annual (M12, M24, M36)"
      responsibility: technical leads
    - channel: Policy briefs
      frequency: biannual
      responsibility: policy engagement lead

  kpis:
    - metric: Peer-reviewed publications
      target_m36: "≥ 10"
    - metric: Conference presentations
      target_m36: "≥ 12"
    - metric: Website unique visitors
      target_m36: "≥ 50 000"
    - metric: Social media followers (total)
      target_m36: "≥ 5 000"
    - metric: Media mentions
      target_m36: "≥ 20"
    - metric: Policy briefs distributed
      target_m36: "≥ 4"
    - metric: Open-source downloads (models + code)
      target_m36: "≥ 10 000"

# ─────────────────────────────────────────────
# 6. Innovation Potential
# ─────────────────────────────────────────────
innovation:
  dimensions:
    - dimension: technological
      description: >
        First EU-sovereign frontier MoE model with integrated
        certification gating; quantum-augmented expert routing.
    - dimension: process
      description: >
        Deterministic AI governance pipeline (PATH → MTL) replacing
        ad-hoc model evaluation with evidence-gated admissibility.
    - dimension: organisational
      description: >
        Capillary Merit Index (CMI) enabling fair attribution and
        incentive structures in HPC-scale multi-partner projects.
    - dimension: regulatory
      description: >
        AI Act compliance-by-design framework moving regulation from
        post-hoc audit to integrated engineering practice.
    - dimension: environmental
      description: >
        CO₂-per-inference metric integrated at HPC job level, enabling
        sustainability-aware model selection and deployment.

  readiness:
    - result: GAIA-EU foundation model
      current_trl: 2
      target_trl: 5
      innovation_type: product
    - result: "Governance pipeline (PATH → MTL)"
      current_trl: 3
      target_trl: 6
      innovation_type: process
    - result: AI Act compliance toolkit
      current_trl: 2
      target_trl: 6
      innovation_type: service
    - result: "CO₂-per-inference framework"
      current_trl: 2
      target_trl: 5
      innovation_type: process
    - result: Quantum-augmented expert module
      current_trl: 1
      target_trl: 3
      innovation_type: research

  barriers:
    - barrier: HPC allocation delays
      likelihood: medium
      impact: high
      mitigation: "Early allocation request; fallback to national HPC centres"
    - barrier: "Regulatory uncertainty (AI Act delegated acts)"
      likelihood: medium
      impact: medium
      mitigation: "Active participation in standardisation; adaptive compliance framework"
    - barrier: Model scaling challenges
      likelihood: medium
      impact: high
      mitigation: "Staged scaling strategy (S1→S2→S3); Chinchilla-optimal compute schedule"
    - barrier: IP conflicts within consortium
      likelihood: low
      impact: medium
      mitigation: "Clear background IP register; 60-day opt-in publication protocol"
    - barrier: Recruitment of specialised AI/HPC talent
      likelihood: high
      impact: medium
      mitigation: "Competitive salaries; remote-first policy; partnership with EU doctoral networks"

# ─────────────────────────────────────────────
# 7. Sustainability Beyond the Project
# ─────────────────────────────────────────────
sustainability:
  mechanisms:
    - mechanism: Open-source community
      description: >
        Model weights, training recipes, and governance tools maintained
        as open-source projects.
      timeline: "M24 onwards"
    - mechanism: Industrial licensing
      description: >
        Commercial licensing of certification-grade governance pipeline
        to aerospace and energy sectors.
      timeline: "M30 onwards"
    - mechanism: Standardisation embedding
      description: >
        Governance methodology embedded in CEN/CENELEC and EUROCAE
        standards.
      timeline: "M18–M48"
    - mechanism: Follow-on funding
      description: >
        Preparation of follow-on proposals under Horizon Europe
        Cluster 4 and Digital Europe Programme.
      timeline: "M30 onwards"
    - mechanism: EuroHPC continuation
      description: >
        Integration of training recipes into EuroHPC service portfolio.
      timeline: "M36 onwards"

  post_project:
    model_hosting:
      platform: "Hugging Face + Zenodo mirror"
      minimum_years: 10
    code_maintenance:
      responsible: coordinator
      minimum_years: 3
    data_preservation_ref: DEL-03
    community_governance: "Transition to community governance model (e.g., Linux Foundation AI) if adoption threshold reached"

# ─────────────────────────────────────────────
# 8. Revision History
# ─────────────────────────────────────────────
revision_history:
  - version: "0.1"
    date: "2026-02-25"
    milestone: M6
    description: Initial Innovation and Impact plan
---

# DEL-04 — Innovation and Impact

**Deliverable ID:** DEL-04
**Section:** Impact → Measures to Maximise Impact
**Programme:** AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
**Author:** Amedeo Pelliccia
**Status:** Draft
**Due:** M6 (initial), updated at M18 and M36

---

## 1. Expected Impact

### 1.1 Scientific Impact

AI-BOOST will produce foundational advances in three domains:

| ID | Impact Area | Expected Outcome | Indicator |
|----|-------------|-------------------|-----------|
| SCI-01 | Sovereign Frontier AI | First EU-sovereign ≥ 400 B parameter MoE model trained entirely on EuroHPC infrastructure | Peer-reviewed publication; model card published |
| SCI-02 | Certification-Grade AI Governance | Deterministic governance pipeline (PATH → MTL) validated for safety-critical AI in regulated sectors | ≥ 3 AI models gate-qualified; methodology adopted by ≥ 1 standards body |
| SCI-03 | Quantum-Augmented Expert Routing | Novel quantum-classical hybrid approach to expert selection and trajectory optimisation | ≥ 2 peer-reviewed publications on quantum manifold methodology |
| SCI-04 | Multilingual Regulatory NLP | Balanced 24-language training with regulatory domain specialists | Benchmark scores published; MMLU-EU extension contributed upstream |

### 1.2 Economic and Technological Impact

| ID | Impact Area | Expected Outcome | Indicator |
|----|-------------|-------------------|-----------|
| ECO-01 | European AI Industry Competitiveness | Reduction of strategic dependency on non-EU frontier model providers | ≥ 2 EU industrial partners adopting GAIA-EU outputs |
| ECO-02 | HPC Service Market Expansion | Demonstration of certification-grade AI workloads on EuroHPC | ≥ 1 new commercial HPC service offering derived from project toolchain |
| ECO-03 | Aerospace Certification Cost Reduction | AI-accelerated simulation reducing certification cycle time | ≥ 30 % reduction in simulation-to-certification elapsed time (demonstrated) |
| ECO-04 | AI Act Compliance Tooling | Reusable compliance-by-design framework for GPAI model providers | Open-source compliance toolkit released |

### 1.3 Societal Impact

| ID | Impact Area | Expected Outcome | Indicator |
|----|-------------|-------------------|-----------|
| SOC-01 | European Digital Sovereignty | Reduced dependency on extra-EU AI infrastructure for critical sectors | Policy brief published; uptake metric tracked |
| SOC-02 | Environmental Accountability | CO₂-per-inference tracking normalised across HPC workloads | Sustainability dashboard public; methodology contributed to Green Deal Digital |
| SOC-03 | Skills and Talent Development | Training of next-generation EU researchers in frontier AI + HPC | ≥ 10 doctoral/postdoctoral researchers trained; open courseware published |
| SOC-04 | Multilingual Access | Equal-quality AI services across EU official languages | Language parity scores published for all 24 EU languages |

---

## 2. Dissemination Plan

### 2.1 Target Audiences

| Audience | Channel | Key Messages |
|----------|---------|--------------|
| Scientific community | Peer-reviewed journals, conferences, preprint servers | Novel architectures, benchmarks, quantum-augmented methods |
| Industry (aerospace, energy, defence) | Trade conferences, bilateral workshops, demonstrators | Certification-grade AI, cost/time savings, compliance tooling |
| Policy makers and regulators | Policy briefs, regulatory sandboxes, standardisation bodies | AI sovereignty, AI Act alignment, EACST integration |
| General public | Project website, social media, press releases | EU AI leadership, sustainability, multilingual access |
| Open-source / developer community | GitHub, Hugging Face, Zenodo | Code, models, datasets, documentation |

### 2.2 Publication Strategy

- **Open Access:** All peer-reviewed publications will be published Open Access (Gold OA or Green OA via preprint + accepted manuscript) in compliance with Horizon Europe Article 17.
- **Preprints:** All papers deposited on arXiv or HAL within one week of submission.
- **Target venues:**

| Venue | Type | Relevance |
|-------|------|-----------|
| NeurIPS / ICML / ICLR | Conference | Frontier AI architecture, MoE scaling |
| ACL / EMNLP | Conference | Multilingual NLP, regulatory language |
| SC (Supercomputing) | Conference | HPC scaling, distributed training |
| Aerospace journals (AIAA, CEAS) | Journal | Certification-grade AI for aerospace |
| Nature Machine Intelligence | Journal | High-impact cross-disciplinary |

### 2.3 Conference Participation

The consortium will present at a minimum of **4 international conferences per year**, covering AI, HPC, aerospace, and regulatory domains.

---

## 3. Exploitation Plan

### 3.1 Exploitation Pathways

| ID | Result | Exploitation Route | Owner | Timeline |
|----|--------|-------------------|-------|----------|
| EXP-01 | GAIA-EU model weights (open) | Open release on Hugging Face under permissive licence | Coordinator | M24 (initial), M36 (final) |
| EXP-02 | Deterministic governance pipeline | Integration into AMPEL360 certification framework; licensing to industrial partners | Coordinator | M18 onwards |
| EXP-03 | Regulatory NLP benchmarks (MMLU-EU) | Contribution to MLCommons; adoption by EU AI Office for evaluation | Coordinator + NLP partner | M12 onwards |
| EXP-04 | AI Act compliance toolkit | Open-source release; commercial support offering by SME partners | SME partner(s) | M24 onwards |
| EXP-05 | HPC training recipes | Publication as reproducible pipelines on EuroHPC documentation | HPC partner | M18 onwards |
| EXP-06 | CO₂-per-inference methodology | Standardisation proposal to CEN/CENELEC; integration with Digital Product Passport | Coordinator + sustainability partner | M24 onwards |

### 3.2 Intellectual Property Strategy

- **Background IP** is documented in the Consortium Agreement with clear access-rights provisions.
- **Foreground IP** is classified using the project's [`contributions-registry.yaml`](../contributions-registry.yaml) taxonomy:
  - **Open results** (default): code, model weights, benchmarks, documentation → Apache 2.0 / CC BY 4.0.
  - **Protected results** (exception): patentable inventions or commercially sensitive algorithms → consortium decision with 60-day opt-in window before open publication.
- **Joint ownership** follows Horizon Europe default rules (Regulation (EU) 2021/695, Article 40).
- **Access rights for exploitation** are granted royalty-free to all consortium partners for project duration and 5 years post-project.

### 3.3 Standardisation Activities

| Body | Standard / Working Group | Contribution |
|------|--------------------------|-------------|
| CEN/CENELEC | JTC 21 AI | AI governance pipeline specification; deterministic gating methodology |
| EUROCAE / SAE | ED-12C / DO-178C AI supplement | Certification-grade AI evidence packages for aerospace |
| ISO | ISO/IEC 42001 AI Management | Alignment evidence for AI management system |
| W3C / OASIS | ML model documentation | GPAI model card schema extension |
| ECSS | Space segment AI | Quantum-augmented expert module specification |

---

## 4. Communication Plan

### 4.1 Communication Objectives

1. **Raise awareness** of European AI sovereignty and the role of EuroHPC in frontier AI.
2. **Engage stakeholders** across scientific, industrial, regulatory, and public audiences.
3. **Demonstrate impact** through measurable outcomes (publications, adoptions, policy influence).

### 4.2 Communication Channels

| Channel | Frequency | Responsibility |
|---------|-----------|----------------|
| Project website | Continuous | Coordinator (WP lead) |
| Social media (LinkedIn, X/Twitter, Mastodon) | ≥ 2 posts/week | Communication officer |
| Newsletter | Quarterly | Communication officer |
| Press releases | At key milestones (M6, M18, M36) | Coordinator |
| Public demonstrators | Annual (M12, M24, M36) | Technical leads |
| Policy briefs | Biannual | Policy engagement lead |

### 4.3 Visual Identity

A consistent visual identity (logo, colour palette, templates) will be established by M3 and applied across all communication materials. All outputs will acknowledge EuroHPC JU funding per GA requirements.

### 4.4 Metrics and Monitoring

| KPI | Target (M36) | Measurement |
|-----|-------------|-------------|
| Peer-reviewed publications | ≥ 10 | Publication tracker |
| Conference presentations | ≥ 12 | Event log |
| Website unique visitors | ≥ 50 000 | Analytics |
| Social media followers (total) | ≥ 5 000 | Platform analytics |
| Media mentions | ≥ 20 | Media monitoring service |
| Policy briefs distributed | ≥ 4 | Distribution log |
| Open-source downloads (models + code) | ≥ 10 000 | Repository analytics |

---

## 5. Innovation Potential

### 5.1 Innovation Dimensions

| Dimension | Description |
|-----------|-------------|
| **Technological** | First EU-sovereign frontier MoE model with integrated certification gating; quantum-augmented expert routing |
| **Process** | Deterministic AI governance pipeline (PATH → MTL) replacing ad-hoc model evaluation with evidence-gated admissibility |
| **Organisational** | Capillary Merit Index (CMI) enabling fair attribution and incentive structures in HPC-scale multi-partner projects |
| **Regulatory** | AI Act compliance-by-design framework moving regulation from post-hoc audit to integrated engineering practice |
| **Environmental** | CO₂-per-inference metric integrated at HPC job level, enabling sustainability-aware model selection and deployment |

### 5.2 Innovation Readiness

| Result | Current TRL | Target TRL (M36) | Innovation Type |
|--------|-------------|-------------------|-----------------|
| GAIA-EU foundation model | TRL 2 | TRL 5 | Product |
| Governance pipeline (PATH → MTL) | TRL 3 | TRL 6 | Process |
| AI Act compliance toolkit | TRL 2 | TRL 6 | Service |
| CO₂-per-inference framework | TRL 2 | TRL 5 | Process |
| Quantum-augmented expert module | TRL 1 | TRL 3 | Research |

### 5.3 Barriers to Innovation and Mitigation

| Barrier | Likelihood | Impact | Mitigation |
|---------|-----------|--------|------------|
| HPC allocation delays | Medium | High | Early allocation request; fallback to national HPC centres |
| Regulatory uncertainty (AI Act delegated acts) | Medium | Medium | Active participation in standardisation; adaptive compliance framework |
| Model scaling challenges | Medium | High | Staged scaling strategy (S1→S2→S3); Chinchilla-optimal compute schedule |
| IP conflicts within consortium | Low | Medium | Clear background IP register; 60-day opt-in publication protocol |
| Recruitment of specialised AI/HPC talent | High | Medium | Competitive salaries; remote-first policy; partnership with EU doctoral networks |

---

## 6. Sustainability Beyond the Project

### 6.1 Long-Term Sustainability Strategy

| Mechanism | Description | Timeline |
|-----------|-------------|----------|
| Open-source community | Model weights, training recipes, and governance tools maintained as open-source projects | M24 onwards |
| Industrial licensing | Commercial licensing of certification-grade governance pipeline to aerospace and energy sectors | M30 onwards |
| Standardisation embedding | Governance methodology embedded in CEN/CENELEC and EUROCAE standards | M18–M48 |
| Follow-on funding | Preparation of follow-on proposals under Horizon Europe Cluster 4 and Digital Europe Programme | M30 onwards |
| EuroHPC continuation | Integration of training recipes into EuroHPC service portfolio | M36 onwards |

### 6.2 Post-Project Commitments

- **Model hosting:** Open model weights hosted on Hugging Face and mirrored on Zenodo for minimum 10 years.
- **Code maintenance:** Core governance pipeline maintained for minimum 3 years post-project by coordinator.
- **Data preservation:** All published datasets preserved per the Data Management Plan ([`DEL-03`](DEL-03-data-management-plan.md)) — minimum 10 years on Zenodo.
- **Community governance:** Transition to community governance model (e.g., Linux Foundation AI) if adoption threshold reached.

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`innovation-and-impact.yaml`](innovation-and-impact.yaml) | Machine-readable specification: impact pathways, dissemination plan, exploitation routes, innovation readiness |
| [`DEL-03-data-management-plan.md`](DEL-03-data-management-plan.md) | Data Management Plan — data preservation and open-access policies |
| Root [`README.md`](../README.md) | Profile-level reference under Current Focus |
| [`simplex-contract.yaml`](../simplex-contract.yaml) | Evidence-gated admissibility framework referenced in governance pipeline |
| [`contributions-registry.yaml`](../contributions-registry.yaml) | IP and contribution classification for exploitation strategy |
| [`EACST/eacst-regulatory-framework.yaml`](../EACST/eacst-regulatory-framework.yaml) | Regulatory framework for aerospace domain — standardisation alignment |
