# DEL-03 — Data Management Plan

**Deliverable ID:** DEL-03
**Section:** Excellence → Data
**Programme:** AI-BOOST — Frontier AI Grand Challenge (GA 101135737, EuroHPC JU)
**Author:** Amedeo Pelliccia
**Status:** Draft
**Due:** M6 (initial), updated at M18 and M36

---

## 1. Data Summary

### 1.1 Purpose

This Data Management Plan (DMP) describes the data lifecycle for the AI-BOOST project: what data will be generated and collected, how it will be handled during and after the project, and how FAIR principles (Findable, Accessible, Interoperable, Reusable) are enforced at every stage.

### 1.2 Data Types and Origins

| ID | Dataset | Origin | Format | Est. Volume | Sensitivity |
|----|---------|--------|--------|-------------|-------------|
| DS-01 | HPC benchmark telemetry | Generated — EuroHPC runs | HDF5 / Parquet | ~50 TB/year | Internal |
| DS-02 | AI/ML model artefacts | Generated — training pipelines | ONNX / SafeTensors / YAML | ~5 TB/year | Internal |
| DS-03 | Quantum simulation outputs | Generated — hybrid quantum-classical runs | HDF5 / JSON | ~2 TB/year | Internal |
| DS-04 | Reference datasets (public) | Collected — open benchmarks | CSV / Parquet | ~500 GB | Public |
| DS-05 | Certified dynamics audit logs | Generated — admissibility engine | JSON | ~10 GB/year | Internal |
| DS-06 | Technical publications (S1000D modules) | Generated — documentation pipeline | XML / PDF | ~1 GB/year | Restricted |
| DS-07 | Environmental & lifecycle metrics | Generated — sustainability monitors | JSON / CSV | ~5 GB/year | Public |

### 1.3 Re-use of Existing Data

The project re-uses publicly available benchmark suites (DS-04) under their original open licences. No personal data is collected or re-used. Pre-trained foundation-model weights are used under their respective licences and are not redistributed.

---

## 2. FAIR Data Principles

### 2.1 Findable

- Every dataset is assigned a **persistent identifier** (DOI via Zenodo or institutional repository) upon publication.
- Machine-readable metadata follows the **DataCite 4.5** schema; project-specific metadata is captured in `data-management-plan.yaml` (companion artefact).
- A central **data catalogue** is maintained in the project repository, linking dataset IDs to their DOIs, versions, and access URLs.

### 2.2 Accessible

- Published datasets are deposited in **Zenodo** (CERN-hosted, European infrastructure) or an equivalent FAIR-compliant repository.
- Access protocols: HTTPS with standard authentication where required; no proprietary access mechanisms.
- Metadata remains accessible even if the dataset itself is restricted (tombstone policy).

### 2.3 Interoperable

- Standard open formats are used throughout (HDF5, Parquet, ONNX, JSON, XML).
- Vocabularies and ontologies:
  - AI/ML artefacts follow the **MLCommons** schema and **Hugging Face** model-card conventions.
  - Technical publications follow **S1000D** / **ATA iSpec 2200** standards.
  - Quantum simulation metadata follows the project's `quantum-manifold.yaml` schema.
- Cross-references between datasets use DOIs and internal dataset IDs (DS-XX).

### 2.4 Reusable

- Every published dataset includes a **licence declaration** (default: CC BY 4.0 for data, Apache 2.0 for code/models, unless otherwise required).
- Provenance is recorded via **hash-chained audit logs** (PATH → MTL pipeline) with immutable timestamps.
- Data quality is ensured through the project's **evidence-gated admissibility** framework (simplex-contract.yaml invariants).

---

## 3. Allocation of Resources

| Activity | Responsible Partner | Estimated Cost |
|----------|-------------------|----------------|
| Data storage (EuroHPC allocated) | Coordinator | Covered by HPC allocation |
| Zenodo deposits & DOI minting | Coordinator | Free (CERN infrastructure) |
| Data curation & metadata | WP lead per dataset | Staff effort (in-kind) |
| Long-term preservation (10 years) | Zenodo / institutional repo | Free tier / institutional |

---

## 4. Data Security

### 4.1 Classification

All datasets are classified on creation using the project's sensitivity taxonomy:

| Level | Label | Controls |
|-------|-------|----------|
| L0 | **Public** | Open access, no restrictions |
| L1 | **Internal** | Project-consortium access, encrypted at rest |
| L2 | **Restricted** | Named-access only, encrypted at rest and in transit, audit-logged |
| L3 | **Confidential** | Dual-use / export-controlled — handled per national regulations, not deposited in open repositories |

### 4.2 Technical Measures

- **Encryption:** AES-256 at rest; TLS 1.3 in transit.
- **Access control:** Role-based (RBAC) for consortium systems; SSH keys for HPC access.
- **Backup:** 3-2-1 strategy (3 copies, 2 media types, 1 off-site) for all L1+ datasets.
- **Integrity:** SHA-256 checksums recorded in audit logs; verified on every transfer.

### 4.3 Incident Response

Data breaches or integrity failures are reported to the coordinator within 24 hours, assessed for impact, and communicated to the EC Project Officer if L2+ data is affected.

---

## 5. Ethics and Legal Compliance

### 5.1 Personal Data

The project does **not** collect, process, or store personal data. If any dataset is later found to contain personally identifiable information (PII), it will be immediately quarantined, anonymised, or deleted in accordance with GDPR (Regulation (EU) 2016/679).

### 5.2 Intellectual Property

- Background IP is documented in the Consortium Agreement.
- Foreground IP arising from generated datasets and models is governed by the Grant Agreement and the project's `contributions-registry.yaml` classification.
- Open-access obligations under Horizon Europe Article 17 are met via Zenodo deposits with CC BY 4.0 licensing.

### 5.3 Export Control

Datasets classified L3 (Confidential / dual-use) are handled per EU Regulation 2021/821 (dual-use export control). Such data is never deposited in open repositories.

---

## 6. Data Sharing and Long-Term Preservation

### 6.1 Open Access Strategy

- **Default open:** All results not subject to IP protection or security classification are published open access.
- **Embargo period:** Up to 6 months for competitive results; metadata is published immediately.
- **Repository:** Zenodo (primary), with mirroring to institutional repositories where required by partners.

### 6.2 Preservation

- Published datasets are preserved for a **minimum of 10 years** after project end (Zenodo guarantees 20-year retention backed by CERN infrastructure).
- File formats are chosen for long-term readability (HDF5, Parquet, JSON, XML — all open, widely supported).
- Metadata and provenance records are self-contained (no external dependency for interpretation).

### 6.3 Data Destruction

Intermediate data not selected for publication (e.g., failed experiment runs, scratch-space files) is deleted within 12 months of project end. Deletion is logged.

---

## 7. Versioning and Updates

This DMP is a **living document**:

| Version | Milestone | Scope |
|---------|-----------|-------|
| v0.1 | M6 | Initial DMP (this document) |
| v1.0 | M18 | Mid-term update: actual volumes, new datasets, access statistics |
| v2.0 | M36 | Final DMP: preservation confirmation, DOI catalogue, lessons learned |

Updates are tracked in `data-management-plan.yaml` (`revision_history` field).

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`data-management-plan.yaml`](data-management-plan.yaml) | Machine-readable DMP specification: datasets, FAIR mappings, security levels, preservation policies |
| Root [`README.md`](../README.md) | Profile-level reference under Current Focus |
| [`simplex-contract.yaml`](../simplex-contract.yaml) | Evidence-gated admissibility framework used for data quality assurance |
| [`contributions-registry.yaml`](../contributions-registry.yaml) | IP and contribution governance for generated artefacts |
