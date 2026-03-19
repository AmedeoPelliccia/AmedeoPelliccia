# DEL-07 — Ethics and Security

**Deliverable ID:** DEL-07
**Section:** Ethics → Ethics and Security
**Programme:** AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
**Author:** Amedeo Pelliccia
**Status:** Draft
**Due:** M6 (initial), updated at M18 and M36

---

## 1. Ethical Framework

### 1.1 Guiding Principles

AI-BOOST adheres to the following ethical principles throughout all project phases:

| ID | Principle | Description | Reference |
|----|-----------|-------------|-----------|
| ETH-01 | Human Agency and Oversight | AI systems remain under meaningful human control; no fully autonomous safety-critical decisions without human-in-the-loop | EU AI Act Art. 14; ALTAI §1 |
| ETH-02 | Technical Robustness and Safety | Models are validated through evidence-gated pipelines before deployment in safety-critical domains | Simplex-contract.yaml INV-001–INV-003 |
| ETH-03 | Privacy and Data Governance | All training data complies with GDPR; personal data is minimised, pseudonymised, or excluded | GDPR Art. 5, 25 |
| ETH-04 | Transparency | Model architectures, training data sources, and evaluation results are publicly documented | EU AI Act Art. 53 (GPAI transparency) |
| ETH-05 | Diversity, Non-Discrimination, and Fairness | Multilingual training ensures balanced performance across all 24 EU official languages; bias audits are conducted per work package | EU AI Act Recital 70 |
| ETH-06 | Societal and Environmental Well-Being | Environmental footprint (CO₂-per-inference) is tracked and reported; sustainability targets are set per HPC job | Green Deal Digital alignment |
| ETH-07 | Accountability | All AI artefacts are traceable through the PATH → MTL governance pipeline with immutable audit trails | Simplex-contract.yaml execution model |

### 1.2 Alignment with EU AI Act

| EU AI Act Category | AI-BOOST Classification | Justification |
|--------------------|------------------------|---------------|
| General-Purpose AI (GPAI) | Yes — GAIA-EU is a frontier foundation model | Training compute exceeds GPAI threshold; open-weights release triggers GPAI provider obligations |
| High-Risk AI System | Domain-dependent — high-risk when deployed in aerospace certification (Annex III) | Simplex-contract evidence gating satisfies conformity assessment requirements |
| Prohibited AI Practices | Not applicable | No social scoring, real-time biometric identification, or manipulation techniques |

---

## 2. Dual-Use Assessment

### 2.1 Dual-Use Risk Analysis

| ID | Risk Category | Description | Likelihood | Impact | Mitigation |
|----|---------------|-------------|------------|--------|------------|
| DU-01 | Military application of simulation acceleration | AI surrogate models could accelerate weapons system design | Low | High | Export-control screening of consortium partners; restricted model variants for defence-adjacent use cases |
| DU-02 | Adversarial misuse of open-weights model | Open-weights release could enable generation of harmful content | Medium | Medium | Red-teaming prior to release (WP4); safety fine-tuning; responsible release protocol |
| DU-03 | Surveillance capability | Multilingual NLP could be repurposed for mass surveillance | Low | High | No biometric processing capability; data processing agreements prohibit surveillance use |

### 2.2 Export Control Compliance

| Requirement | Status | Evidence |
|-------------|--------|----------|
| EU Dual-Use Regulation (EU) 2021/821 screening | ✅ Planned | All consortium partners screened; no listed entities |
| US EAR/ITAR assessment (for international collaborations) | ✅ Planned | No US-origin controlled technology used in core pipeline |
| End-use monitoring | ✅ Planned | Responsible use license terms for model distribution |

---

## 3. Data Protection

### 3.1 GDPR Compliance

| Aspect | Approach | Reference |
|--------|----------|-----------|
| Legal basis for data processing | Legitimate interest (Art. 6(1)(f)) for research; consent where required | GDPR Art. 6 |
| Data minimisation | Training corpora use publicly available, non-personal data; personal data excluded or pseudonymised | GDPR Art. 5(1)(c) |
| Data subject rights | Procedures for access, rectification, erasure requests documented in DMP (DEL-03) | GDPR Art. 15–22 |
| Data Protection Impact Assessment (DPIA) | Conducted before training on any dataset containing personal data | GDPR Art. 35 |
| Data Protection Officer (DPO) | Designated within coordinator organisation | GDPR Art. 37 |
| Cross-border data transfers | All training and inference on EU-based infrastructure (EuroHPC nodes); no extra-EU data transfers for safety-critical workloads | GDPR Chapter V |

### 3.2 Training Data Ethics

| Criterion | Requirement | Verification Method |
|-----------|-------------|---------------------|
| Copyright compliance | All training data sources licensed or public domain | Data provenance registry (DEL-03) |
| Consent verification | Consent obtained where data includes user-generated content | Consent audit trail |
| Bias assessment | Training data audited for demographic, linguistic, and geographic bias | Bias evaluation report per WP |
| Opt-out mechanism | Content creators can request exclusion from training corpora | Opt-out request process documented |

---

## 4. Security

### 4.1 Information Security Framework

| Domain | Measure | Standard |
|--------|---------|----------|
| Access control | Role-based access to HPC resources, model weights, and training data | ISO 27001 Annex A.9 |
| Data encryption | At-rest (AES-256) and in-transit (TLS 1.3) for all project data | ISO 27001 Annex A.10 |
| Audit logging | All access to model artefacts and training infrastructure logged with immutable audit trail | ISO 27001 Annex A.12 |
| Incident response | Security incident response plan with 24-hour notification window | ISO 27001 Annex A.16; NIS2 Art. 23 |
| Supply chain security | Third-party dependencies audited; software bill of materials (SBOM) maintained | ISO 27001 Annex A.15 |

### 4.2 Model Security

| Threat | Mitigation | Evidence |
|--------|------------|----------|
| Model poisoning | Training data provenance verification; anomaly detection in training loss curves | Data provenance registry |
| Model extraction | Rate limiting on inference API; watermarking of model outputs | API security policy |
| Adversarial inputs | Adversarial robustness testing during WP4 evaluation phase | Red-team evaluation report |
| Prompt injection | Input sanitisation layer; output filtering for safety-critical deployments | Safety filter specification |

### 4.3 HPC Security

| Aspect | Requirement | Compliance |
|--------|-------------|------------|
| EuroHPC acceptable use policy | All usage compliant with EuroHPC JU security and acceptable use policies | Signed AUP per consortium partner |
| Multi-tenancy isolation | Training jobs isolated from other HPC users via container and namespace boundaries | Container security policy |
| Data sovereignty | All safety-critical data remains on EU-based infrastructure | Data residency verification |

---

## 5. Responsible AI Governance

### 5.1 Ethics Review Process

| Stage | Activity | Responsible |
|-------|----------|-------------|
| Pre-training | Ethics self-assessment; DPIA if personal data involved; dual-use screening | Governance & Safety Lead |
| During training | Continuous monitoring of training outputs for harmful content generation capability | Governance & Safety Lead + ML team |
| Pre-release | Red-teaming; bias audit; safety evaluation; responsible release checklist | Full consortium review |
| Post-release | Community feedback monitoring; incident response; model update protocol | Coordinator + community |

### 5.2 Ethics Advisory

| Mechanism | Description |
|-----------|-------------|
| Internal ethics review | Governance & Safety Lead reviews all WP outputs for ethical compliance |
| External ethics advisory board | Independent ethics experts consulted at M6, M18, M36 milestones |
| National ethics committee | Engagement with relevant national ethics bodies where consortium partners are based |

---

## 6. Environmental Ethics

| Aspect | Commitment | Metric |
|--------|------------|--------|
| Carbon footprint tracking | CO₂ emissions tracked per training run and per inference request | kg CO₂e per 1M tokens |
| Renewable energy preference | HPC allocations prioritise nodes powered by renewable energy | % renewable energy in compute mix |
| Efficiency optimisation | Model architecture and training pipeline optimised for compute efficiency | FLOPs per quality point |
| Sustainability reporting | Environmental impact included in all public reporting and model cards | Sustainability section in model card |

---

## 7. Repository Assets Referenced

| Asset | Path | Role in DEL-07 |
|-------|------|----------------|
| Simplex contract | [`simplex-contract.yaml`](../simplex-contract.yaml) | Evidence-gated governance — ethics-by-design enforcement |
| Contributions registry | [`contributions-registry.yaml`](../contributions-registry.yaml) | Fair attribution — ethical contributor governance |
| EACST framework | [`EACST/`](../EACST/) | Regulatory domain — safety-critical ethics context |
| Data Management Plan | DEL-03 | GDPR compliance, data provenance, training data ethics |

---

## 8. Revision History

| Version | Date | Milestone | Description |
|---------|------|-----------|-------------|
| 0.1 | 2026-02-25 | M6 | Initial Ethics and Security stub |
