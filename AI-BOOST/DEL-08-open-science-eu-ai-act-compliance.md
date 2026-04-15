---
# open-science-eu-ai-act-compliance.yaml
# Machine-readable specification for DEL-08: Open Science & EU AI Act Compliance
# Programme: Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
# Reference: AI-BOOST/DEL-08-open-science-eu-ai-act-compliance.md
# Author: Amedeo Pelliccia

schema_version: "1.0.0"
document_type: open_science_eu_ai_act_compliance
last_updated: "2026-02-25T00:00:00Z"

# ─────────────────────────────────────────────
# 1. Deliverable Metadata
# ─────────────────────────────────────────────
deliverable:
  id: DEL-08
  title: Open Science & EU AI Act Compliance
  programme: Frontier AI Grand Challenge
  grant_agreement: GA 101135737
  funding_body: EuroHPC JU
  section: Eligibility + Innovation
  status: Required
  version: "1.0.0"
  author: Amedeo Pelliccia
  date: "2026-02-25"

# ─────────────────────────────────────────────
# 2. Open Science
# ─────────────────────────────────────────────
open_science:
  open_access:
    policy: immediate_open_access
    repository:
      - Zenodo
      - OpenAIRE
    licence: CC-BY-4.0
    metadata_standard: Dublin Core / DataCite
    embargo: none
    acknowledgement_required: true

  fair_data:
    findable:
      - persistent_identifiers: DOI
      - metadata_indexed: discipline-specific catalogues
    accessible:
      - repositories:
          - Zenodo
          - EUDAT
      - access_protocols: documented
    interoperable:
      - vocabularies: standard ontologies
      - formats:
          - YAML
          - JSON
          - CSV
          - HDF5
    reusable:
      - licence: CC-BY-4.0 or CC0
      - provenance: metadata attached
      - version_control: Git

  open_source:
    licence:
      - Apache-2.0
      - EUPL-1.2
    repository: public GitHub
    requirements:
      - CI/CD pipelines
      - contribution guidelines
      - REUSE-compliant headers
      - README and API documentation
      - reproducibility instructions
    exceptions:
      scope: security-critical or dual-use-restricted modules
      policy: controlled access with documented justification in DMP

  responsible_research:
    gender_equality: consortium-level compliance verified
    public_engagement: planned per dissemination milestones (DEL-04)
    ethics_review: documented in DEL-07

# ─────────────────────────────────────────────
# 3. EU AI Act Compliance
# ─────────────────────────────────────────────
eu_ai_act:
  regulation: Regulation (EU) 2024/1689
  effective_date: "2024-08-01"
  framework: risk-based

  risk_classification:
    - component: Quantum-augmented structural analysis (QAOS)
      category: high-risk
      annex: III
      section: 6
      justification: >
        Safety-critical aerospace application; inputs to structural
        certification decisions.

    - component: Predictive maintenance models
      category: high-risk
      annex: III
      section: 6
      justification: >
        Operational safety dependency; maintenance scheduling
        affects airworthiness.

    - component: NeuronBit simplicial inference
      category: limited-risk
      justification: >
        Research tool; no direct safety-critical deployment;
        transparency obligations apply.

    - component: Digital twin telemetry fusion
      category: high-risk
      annex: III
      section: 6
      justification: >
        Feeds into real-time operational decisions for
        aerospace systems.

    - component: Training data curation pipelines
      category: minimal-risk
      justification: >
        Data processing tools; no autonomous decision-making.

  high_risk_requirements:
    - article: 9
      title: Risk management system
      implementation: >
        Continuous risk assessment integrated into C-GROWTH lifecycle
        (CT phase); documented in risk register.

    - article: 10
      title: Data governance
      implementation: >
        Training/validation/test datasets governed per DMP (DEL-03);
        bias monitoring; data quality metrics tracked.

    - article: 11
      title: Technical documentation
      implementation: >
        Full technical documentation maintained per Annex IV;
        version-controlled in project repository.

    - article: 12
      title: Record-keeping
      implementation: >
        Automatic logging of AI system operations; audit trails
        stored with ISO timestamps; retention per Art. 12(2).

    - article: 13
      title: Transparency
      implementation: >
        User-facing documentation; intended purpose, limitations,
        and accuracy metrics disclosed.

    - article: 14
      title: Human oversight
      implementation: >
        Human-in-the-loop for all safety-critical decisions;
        override mechanisms documented.

    - article: 15
      title: Accuracy, robustness, cybersecurity
      implementation: >
        Performance benchmarks defined; adversarial robustness
        testing; cybersecurity measures per Part-CYB-S.

  conformity_assessment:
    steps:
      - step: 1
        title: Classification
        description: Each AI component classified per Annex III risk taxonomy.

      - step: 2
        title: Documentation
        description: Technical documentation compiled per Annex IV.

      - step: 3
        title: Quality Management System
        description: >
          QMS established covering design, development, testing,
          and post-market monitoring (Art. 17).

      - step: 4
        title: Internal control
        description: >
          Internal conformity assessment for components not subject
          to third-party assessment.

      - step: 5
        title: EU Declaration of Conformity
        description: Prepared per Art. 47 for each high-risk AI system before deployment.

      - step: 6
        title: CE marking
        description: Applied per Art. 48 upon successful conformity assessment.

      - step: 7
        title: Post-market monitoring
        description: Monitoring plan per Art. 72; incident reporting per Art. 73.

  general_purpose_ai:
    applicable: conditional
    obligations:
      - title: Technical documentation
        article: 53
        implementation: >
          Model cards with architecture, training data summary,
          evaluation results, intended use, and known limitations.

      - title: Copyright compliance
        article: "53(1)(c)"
        implementation: >
          Training data provenance tracked; opt-out mechanisms
          respected; EU copyright Directive compliance.

      - title: Transparency
        article: "53(1)(d)"
        implementation: >
          Publicly available summary of training data per template
          in Annex XII.

      - title: Systemic risk assessment
        article: 51
        implementation: >
          If model meets systemic-risk thresholds: adversarial
          testing, incident reporting to AI Office, energy
          consumption disclosure.

  governance:
    - role: AI Compliance Officer
      responsibility: >
        Designated within consortium; responsible for AI Act
        conformity across all AI components.

    - role: Ethics Board
      responsibility: >
        Reviews AI risk classifications and monitors compliance
        (cross-reference DEL-07).

    - role: National Competent Authority
      responsibility: >
        Liaison established with relevant EU Member State authority
        for market surveillance.

    - role: EU AI Office
      responsibility: >
        Monitoring channel for general-purpose AI obligations
        if applicable.

# ─────────────────────────────────────────────
# 4. Cross-References
# ─────────────────────────────────────────────
cross_references:
  - deliverable: DEL-03
    title: Data Management Plan
    relationship: FAIR data governance, dataset documentation, and data quality measures

  - deliverable: DEL-04
    title: Innovation and Impact
    relationship: Open science dissemination plan; exploitation of open-access outputs

  - deliverable: DEL-05
    title: Workplan, Milestones & Gantt
    relationship: Compliance milestones integrated into project timeline

  - deliverable: DEL-06
    title: Capacity Demonstration
    relationship: Infrastructure capacity for compliance monitoring and audit trail storage

  - deliverable: DEL-07
    title: Ethics and Security
    relationship: Ethics review, security measures, and responsible AI principles

# ─────────────────────────────────────────────
# 5. Compliance Timeline
# ─────────────────────────────────────────────
compliance_timeline:
  - milestone: AI risk classification complete
    target_month: M3
    eu_ai_act_reference: Annex III

  - milestone: QMS established
    target_month: M6
    eu_ai_act_reference: Art. 17

  - milestone: Technical documentation (v1)
    target_month: M9
    eu_ai_act_reference: Annex IV

  - milestone: Open access repository set up
    target_month: M3
    reference: Horizon Europe OA mandate

  - milestone: FAIR data policy operational
    target_month: M6
    reference: DMP (DEL-03)

  - milestone: Internal conformity assessment
    target_month: M18
    eu_ai_act_reference: Art. 43

  - milestone: Post-market monitoring plan
    target_month: M24
    eu_ai_act_reference: Art. 72

# ─────────────────────────────────────────────
# 6. Evidence and Traceability
# ─────────────────────────────────────────────
evidence:
  version_control: Git
  machine_readable: true
  audit_pipeline:
    - GATE-BREX
    - GATE-TRACE-RESOLVE
  lifecycle_integration: C-GROWTH CT phase

# ─────────────────────────────────────────────
# 7. References
# ─────────────────────────────────────────────
references:
  - id: REF-01
    title: Regulation (EU) 2024/1689 — Artificial Intelligence Act
    type: regulation

  - id: REF-02
    title: Horizon Europe Programme Guide — Open Science requirements
    type: programme_guide

  - id: REF-03
    title: "FAIR Data Principles — Wilkinson et al. (2016), Scientific Data 3:160018"
    type: publication

  - id: REF-04
    title: Creative Commons BY 4.0
    url: "https://creativecommons.org/licenses/by/4.0/"
    type: licence

  - id: REF-05
    title: EUPL v1.2
    url: "https://eupl.eu/"
    type: licence

  - id: REF-06
    title: Regulation (EU) 2021/695 — Horizon Europe Framework Programme
    type: regulation
---

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
