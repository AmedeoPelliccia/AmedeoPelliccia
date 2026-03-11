# SPEC-ATA-CFS-001 — ATA Constituent Framework Specification

**ATA Constituent Framework (ATA-CFS): Transition from Industrial Chapters to Scientific Domain Architecture**

| Metadata | Value |
|----------|-------|
| **Document ID** | SPEC-ATA-CFS-001 |
| **Version** | 1.0.0 |
| **Status** | Normative Draft |
| **Parent** | STD-OPTIN-SCI-001 |
| **Companion** | [`ata-cfs-spec.yaml`](ata-cfs-spec.yaml) |
| **ATA Registry** | [`Full-ATA-CHAPTERS-Top-Level-Instructions-list.json`](Full-ATA-CHAPTERS-Top-Level-Instructions-list.json) |
| **OPT-IN Cross-Reference** | [`../OPT-IN/SCIENCE-DOMAIN.md`](../OPT-IN/SCIENCE-DOMAIN.md) |
| **Last Updated** | 2026-03-11 |

---

## 1. Purpose and Scope

This specification formalises the **ATA Constituent Framework (ATA-CFS)**: the structural bridge between legacy ATA iSpec 2200 industrial chapter numbering and the scientific domain architecture defined in `STD-OPTIN-SCI-001`.

**ATA-CFS enables:**

1. **Historical continuity** — every ATA chapter becomes a Constituent Chapter (CC) that preserves industrial knowledge and acts as a provenance anchor
2. **Scientific extension** — Constituent Chapter Articles (CCAs) introduce forward-compatible specialisations (e.g. hydrogen systems, digital twins) without breaking historical numbering
3. **Unique identification** — the UID scheme (`AnXXSSSS`) provides machine-addressable identifiers for every article instance, enabling full traceability through the PATH → MTL pipeline
4. **OPT-IN axis integration** — each CC/CCA can be anchored to one or more OPT-IN axes (O/P/T/I/N) and mapped to a Science subdomain (SCI-01 through SCI-07)

---

## 2. Definitions

| Term | Definition |
|------|-----------|
| **Constituent Chapter (CC)** | Root domain unit derived from a legacy ATA chapter (e.g. `ATA 28` → `CC28`). Acts as the knowledge container and historical anchor for all derivative articles. |
| **Constituent Chapter Article (CCA)** | A derived unit within a CC. Represents a specific functional abstraction, specialisation, or module within the domain. A CCA may cover classical ATA sub-chapters (A0–A5) or scientific extensions (A6–A9). |
| **Article 0 (A0)** | The foundational article within a CC. Reserved for the base ontology of the domain: general definitions, carrier properties, energy physics, or analogous domain primitives. |
| **Classical Articles (A1–A5)** | CCAs that map directly to existing ATA sub-chapter divisions. These inherit the full normative weight of the original ATA specification. |
| **Extension Articles (A6–A9)** | CCAs reserved for scientific, forward-compatible, or technology-evolution extensions (e.g. hydrogen carriers, digital twins, autonomous logistics). These are not present in the original ATA numbering; they extend the framework while preserving backward compatibility. |
| **Meta-System Article (A9)** | The A9 slot is conventionally reserved for digital twin, simulation, and system-level analytics artefacts that span all other articles in the CC. |
| **UID (Unique Identifier)** | A machine-addressable token of the form `AnXXSSSS` identifying a specific article instance within the framework. |

---

## 3. Naming Rules

### 3.1 Constituent Chapter (CC)

| Field | Rule |
|-------|------|
| **Input** | ATA Standard Chapter number (`ATA XX`) |
| **Output** | `CCXX` |
| **Logic** | Direct 1:1 mapping. No deviation allowed. Leading zeros preserved (e.g. `ATA 05` → `CC05`). |

**Examples:**

| ATA Chapter | CC Code |
|-------------|---------|
| `ATA 28` | `CC28` |
| `ATA 34` | `CC34` |
| `ATA 05` | `CC05` |

### 3.2 Constituent Chapter Article (CCA)

| Field | Rule |
|-------|------|
| **Input** | ATA sub-chapter code (`ATA XXn`) or logical equivalent |
| **Output** | `CCAXX-An` |
| **Breakdown** | `XX` = parent chapter ID; `n` = article ordinal (0–9) |

**Examples:**

| ATA Sub-chapter | CCA Code | Role |
|-----------------|---------|------|
| `ATA 280` | `CCA28-A0` | Prime Consumable / Energy Carrier (foundational) |
| `ATA 281` | `CCA28-A1` | Storage Architecture |
| `ATA 282` | `CCA28-A2` | Distribution & Flow Dynamics |
| `ATA 285` | `CCA28-A5` | Refueling & Offloading Interfaces |
| *(extension)* | `CCA28-A6` | Future Energy Carriers (H₂/He) |
| *(extension)* | `CCA28-A9` | Energy System Digital Twin |

### 3.3 Unique Identifier (UID)

| Field | Rule |
|-------|------|
| **Pattern** | `AnXXSSSS` |
| **`A`** | Fixed literal token (Article) |
| **`n`** | Article ordinal (0–9) |
| **`XX`** | Parent chapter number (01–99, two digits) |
| **`SSSS`** | Reserved space for lineage/sub-variant (default `0000`; populated during instantiation) |

**Examples:**

| CCA Code | UID (default instance) | Note |
|----------|----------------------|------|
| `CCA28-A0` | `A0280000` | Foundational article |
| `CCA28-A6` | `A6280000` | Extension — hydrogen carriers |
| `CCA28-A9` | `A9280000` | Meta-system — digital twin |
| `CCA34-A0` | `A0340000` | Navigation — foundational article |

---

## 4. Inheritance Rules

### INH-001 — Semantic Continuity

> Every CCA **must** maintain semantic traceability to its parent CC. A CCA cannot define concepts outside the knowledge domain of its CC.

*A CCA under CC28 (Fuel/Energy) may not introduce avionics logic — that belongs under CC34 or CC42.*

### INH-002 — Scope Propagation

> The technical scope of the CC (e.g. "Fuel") limits and constrains the scope of all its derived CCAs. No CCA may claim a scope broader than its parent CC.

*Extension articles (A6–A9) expand **within** the CC domain into new technology spaces; they do not escape the domain.*

### INH-003 — Versioning Independence with Stability Inheritance

> The version of a CCA is independent of the version of its parent CC. However, the CCA inherits the **stability state** of its CC: if the CC is `deprecated`, all its CCAs are automatically considered `deprecated-pending-migration`.

### INH-004 — OPT-IN Axis Inheritance

> Every CC inherits the OPT-IN axis instantiation of its parent Science subdomain. A CCA may specialise (narrow) the axis instantiation but not override it.

*CC28 maps to OPT-IN Science subdomains SCI-02 (Climate & Earth Science) and SCI-04 (Materials Science & Engineering) for classical articles, and SCI-01 (Quantum Science & Technology) for A6–A9 extension articles involving hydrogen and digital twins.*

---

## 5. Traceability Rules

| Origin | Destination | Relation | Cardinality |
|--------|------------|---------|-------------|
| `ATA XX` | `CCXX` | Historical Anchor | 1:1 |
| `ATA XXn` | `CCAXX-An` | Derivation | 1:1 |
| `CCAXX-An` | `AnXXSSSS` | Instantiation | 1:N |
| `CCXX` | OPT-IN Science Subdomain | Domain Mapping | 1:N |
| `AnXXSSSS` | PATH → MTL artefact | Evidence Chain | 1:1 |

**Traceability invariant (TRACE-INV-001):**

> Every UID instance (`AnXXSSSS` with non-zero `SSSS`) **must** resolve to a registered artefact in the PATH → MTL pipeline before a downstream certification gate (P050 or later in EACST-STD-CCTLS-001) can be closed.

---

## 6. Article Ordinal Convention

| Ordinal | Role | ATA Correspondence | Extension Type |
|---------|------|--------------------|---------------|
| **A0** | Foundational / Ontology | `ATA XX0` | Classical — base definitions |
| **A1** | Storage / Architecture | `ATA XX1` | Classical — primary storage structure |
| **A2** | Distribution / Flow | `ATA XX2` | Classical — fluid/energy distribution |
| **A3** | Jettison / Emergency | `ATA XX3` | Classical — emergency / safety subsystem |
| **A4** | Indication / Sensing | `ATA XX4` | Classical — sensors and quantification |
| **A5** | Interface / Servicing | `ATA XX5` | Classical — ground ops / external interface |
| **A6** | Future Carrier Extension | *(reserved)* | Scientific — novel energy carriers |
| **A7** | Thermal Management | *(reserved)* | Scientific — thermal coupling integration |
| **A8** | Autonomous / Unmanned | *(reserved)* | Scientific — automated logistics |
| **A9** | Meta-System / Digital Twin | *(reserved)* | Scientific — system-level simulation |

---

## 7. Integration with OPT-IN Science Domain

The ATA-CFS architecture is the **implementation layer** of the OPT-IN Science Domain Architecture (`STD-OPTIN-SCI-001`). Each CC maps to one or more Science subdomains:

| CC Range | ATA Domain | Primary Science Subdomain | Secondary Science Subdomains |
|----------|-----------|--------------------------|------------------------------|
| CC05–CC12 | General / Airworthiness | SCI-07 (Social & Behavioural) | SCI-05 (Computer Science) |
| CC21–CC26 | Air Systems | SCI-04 (Materials) | SCI-02 (Climate) |
| CC27–CC29 | Fuel / Energy | SCI-04 (Materials) · SCI-02 (Climate) | SCI-01 (Quantum — for H₂/A6+) |
| CC31–CC36 | Avionics | SCI-05 (Computer Science) | SCI-01 (Quantum) |
| CC45–CC46 | Central Maintenance / Info | SCI-05 (Computer Science) | SCI-06 (Space Science) |
| CC51–CC57 | Structures | SCI-04 (Materials) | SCI-02 (Climate) |
| CC71–CC80 | Powerplant | SCI-04 (Materials) · SCI-02 (Climate) | SCI-01 (Quantum — for future propulsion) |

---

## 8. CI/CD Validation Rules

The following rules are machine-enforced in CI/CD pipelines:

| Rule ID | Check | Severity |
|---------|-------|---------|
| `CFS-VAL-001` | Every CC must have an `A0` article defined | ERROR |
| `CFS-VAL-002` | UID pattern must match `^A[0-9][0-9]{2}[0-9]{4}$` | ERROR |
| `CFS-VAL-003` | CCA scope must not reference concepts outside parent CC domain | WARNING |
| `CFS-VAL-004` | Extension articles (A6–A9) must declare `extension_type` field | ERROR |
| `CFS-VAL-005` | Every UID with `SSSS ≠ 0000` must resolve to a PATH→MTL artefact | ERROR |
| `CFS-VAL-006` | CC must declare at least one OPT-IN Science subdomain mapping | WARNING |

---

## 9. References

| Reference | Document |
|-----------|---------|
| OPT-IN Science Domain Architecture | `OPT-IN/SCIENCE-DOMAIN.md` (STD-OPTIN-SCI-001) |
| OPT-IN Framework Standard | STD-OPTIN-001 v1.1 |
| ATA iSpec 2200 | ATA iSpec 2200 (2020) |
| S1000D Issue 5.0 | S1000D Issue 5.0 |
| AMPEL360 ATA Registry | `ATA/Full-ATA-CHAPTERS-Top-Level-Instructions-list.json` |
| ESSA CCTLS Standard | EACST-STD-CCTLS-001 |
| AMPEL360 Lifecycle | ESSA-DOC-AMPEL360-001 |
| PATH → MTL Pipeline | STD-PATH-MTL-001 |
