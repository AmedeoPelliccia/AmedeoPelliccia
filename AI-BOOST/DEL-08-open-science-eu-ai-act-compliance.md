# DEL-08 — Open Science & EU AI Act Compliance

| Field | Value |
|-------|-------|
| **Deliverable** | DEL-08 |
| **Title** | Open Science & EU AI Act Compliance |
| **Programme** | Frontier AI Grand Challenge |
| **Grant Agreement** | GA 101135737 (EuroHPC JU) |
| **Section** | Eligibility + Innovation |
| **Status** | Required |
| **Author** | Amedeo Pelliccia |
| **Version** | 1.0.0 |
| **Date** | 2026-02-25 |
| **Machine-readable** | [`open-science-eu-ai-act-compliance.yaml`](open-science-eu-ai-act-compliance.yaml) |

---

## 1. Purpose

This deliverable demonstrates full alignment with **Horizon Europe Open Science requirements** and the **EU Artificial Intelligence Act** (Regulation (EU) 2024/1689). It ensures that AI-BOOST research outputs are openly accessible, FAIR-compliant, and that all AI systems developed under the programme satisfy the risk-based regulatory framework established by the EU AI Act.

---

## 2. Open Science

### 2.1 Open Access to Publications

| Requirement | Implementation |
|-------------|----------------|
| Immediate open access | All peer-reviewed publications deposited in an open-access repository (e.g., Zenodo, OpenAIRE) upon acceptance |
| Licence | CC BY 4.0 (Creative Commons Attribution) for all publications |
| Metadata | Dublin Core / DataCite metadata attached to every deposit |
| Embargo | No embargo period — immediate deposit required |
| Acknowledgement | All publications include GA number and EU funding acknowledgement |

### 2.2 FAIR Data Management

Data management follows the **FAIR principles** (Findable, Accessible, Interoperable, Reusable) as defined in DEL-03 (Data Management Plan):

| FAIR Principle | Measure |
|----------------|---------|
| **Findable** | Persistent identifiers (DOI) assigned to all datasets; metadata indexed in discipline-specific catalogues |
| **Accessible** | Datasets deposited in trusted repositories (Zenodo, EUDAT, domain-specific archives); access protocols documented |
| **Interoperable** | Standard vocabularies and ontologies used; machine-readable formats (YAML, JSON, CSV, HDF5) preferred |
| **Reusable** | Clear licensing (CC BY 4.0 or CC0 for data); provenance metadata; version control via Git |

### 2.3 Open Source Software

| Aspect | Policy |
|--------|--------|
| Licence | Apache 2.0 or EUPL v1.2 for all software artefacts |
| Repository | Public GitHub repositories with CI/CD, contribution guidelines, and REUSE-compliant headers |
| Documentation | README, API docs, and reproducibility instructions included with every release |
| Exceptions | Security-critical components or dual-use-restricted modules documented under controlled access; justification recorded in DMP |

### 2.4 Responsible Research and Innovation (RRI)

- Gender equality plan compliance verified at consortium level.
- Public engagement actions planned for each dissemination milestone (DEL-04).
- Ethics review clearance documented in DEL-07.

---

## 3. EU AI Act Compliance

### 3.1 Regulatory Scope

The **EU AI Act** (Regulation (EU) 2024/1689), effective 1 August 2024 with phased application, establishes a risk-based framework for AI systems placed on or used in the EU market. AI-BOOST AI components are assessed under this framework.

### 3.2 Risk Classification

| AI Component | Risk Category | Justification |
|--------------|---------------|---------------|
| Quantum-augmented structural analysis (QAOS) | High-risk (Annex III, §6 — safety components of regulated products) | Safety-critical aerospace application; inputs to structural certification decisions |
| Predictive maintenance models | High-risk (Annex III, §6) | Operational safety dependency; maintenance scheduling affects airworthiness |
| NeuronBit simplicial inference | Limited risk | Research tool; no direct safety-critical deployment; transparency obligations apply |
| Digital twin telemetry fusion | High-risk (Annex III, §6) | Feeds into real-time operational decisions for aerospace systems |
| Training data curation pipelines | Minimal risk | Data processing tools; no autonomous decision-making |

### 3.3 High-Risk AI System Requirements (Title III, Chapter 2)

For each high-risk AI component, the following requirements are addressed:

| Article | Requirement | AI-BOOST Implementation |
|---------|-------------|-------------------------|
| Art. 9 | Risk management system | Continuous risk assessment integrated into C-GROWTH lifecycle (CT phase); documented in risk register |
| Art. 10 | Data governance | Training/validation/test datasets governed per DMP (DEL-03); bias monitoring; data quality metrics tracked |
| Art. 11 | Technical documentation | Full technical documentation maintained per Annex IV; version-controlled in project repository |
| Art. 12 | Record-keeping | Automatic logging of AI system operations; audit trails stored with ISO timestamps; retention per Art. 12(2) |
| Art. 13 | Transparency | User-facing documentation; intended purpose, limitations, and accuracy metrics disclosed |
| Art. 14 | Human oversight | Human-in-the-loop for all safety-critical decisions; override mechanisms documented |
| Art. 15 | Accuracy, robustness, cybersecurity | Performance benchmarks defined; adversarial robustness testing; cybersecurity measures per Part-CYB-S |

### 3.4 Conformity Assessment

| Step | Description |
|------|-------------|
| 1. Classification | Each AI component classified per Annex III risk taxonomy |
| 2. Documentation | Technical documentation compiled per Annex IV |
| 3. Quality Management System | QMS established covering design, development, testing, and post-market monitoring (Art. 17) |
| 4. Internal control | Internal conformity assessment for components not subject to third-party assessment |
| 5. EU Declaration of Conformity | Prepared per Art. 47 for each high-risk AI system before deployment |
| 6. CE marking | Applied per Art. 48 upon successful conformity assessment |
| 7. Post-market monitoring | Monitoring plan per Art. 72; incident reporting per Art. 73 |

### 3.5 General-Purpose AI Model Obligations (Title VIII-A)

If AI-BOOST develops or fine-tunes general-purpose AI models:

| Obligation | Implementation |
|------------|----------------|
| Technical documentation (Art. 53) | Model cards with architecture, training data summary, evaluation results, intended use, and known limitations |
| Copyright compliance (Art. 53(1)(c)) | Training data provenance tracked; opt-out mechanisms respected; EU copyright Directive compliance |
| Transparency (Art. 53(1)(d)) | Publicly available summary of training data per template in Annex XII |
| Systemic risk assessment | If model meets systemic-risk thresholds (Art. 51): adversarial testing, incident reporting to AI Office, energy consumption disclosure |

### 3.6 Governance and Oversight

| Role | Responsibility |
|------|----------------|
| AI Compliance Officer | Designated within consortium; responsible for AI Act conformity across all AI components |
| Ethics Board | Reviews AI risk classifications and monitors compliance (cross-reference DEL-07) |
| National Competent Authority | Liaison established with relevant EU Member State authority for market surveillance |
| EU AI Office | Monitoring channel for general-purpose AI obligations if applicable |

---

## 4. Integration with AI-BOOST Deliverables

| Deliverable | Relationship |
|-------------|--------------|
| DEL-03 (Data Management Plan) | FAIR data governance, dataset documentation, and data quality measures |
| DEL-04 (Innovation and Impact) | Open science dissemination plan; exploitation of open-access outputs |
| DEL-05 (Workplan, Milestones & Gantt) | Compliance milestones integrated into project timeline |
| DEL-06 (Capacity Demonstration) | Infrastructure capacity for compliance monitoring and audit trail storage |
| DEL-07 (Ethics and Security) | Ethics review, security measures, and responsible AI principles |

---

## 5. Compliance Timeline

| Milestone | Target | EU AI Act Reference |
|-----------|--------|---------------------|
| AI risk classification complete | M3 | Annex III |
| QMS established | M6 | Art. 17 |
| Technical documentation (v1) | M9 | Annex IV |
| Open access repository set up | M3 | Horizon Europe OA mandate |
| FAIR data policy operational | M6 | DMP (DEL-03) |
| Internal conformity assessment | M18 | Art. 43 |
| Post-market monitoring plan | M24 | Art. 72 |

---

## 6. Evidence and Traceability

All compliance evidence is:

- **Version-controlled** in the project Git repository.
- **Machine-readable** via the companion YAML specification.
- **Auditable** through the IDEALE governance pipeline (GATE-BREX, GATE-TRACE-RESOLVE).
- **Linked** to the C-GROWTH lifecycle continuous testing (CT) phase.

---

## 7. References

1. Regulation (EU) 2024/1689 — Artificial Intelligence Act (EU AI Act)
2. Horizon Europe Programme Guide — Open Science requirements
3. FAIR Data Principles — Wilkinson et al. (2016), *Scientific Data* 3:160018
4. Creative Commons BY 4.0 — https://creativecommons.org/licenses/by/4.0/
5. EUPL v1.2 — https://eupl.eu/
6. Regulation (EU) 2021/695 — Horizon Europe Framework Programme
