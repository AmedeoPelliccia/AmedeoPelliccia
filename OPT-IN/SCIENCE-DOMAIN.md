# OPT-IN Science Domain Architecture

**Science as a Domain and Subdomains within the OPT-IN 5-Axis Topology**

| Metadata | Value |
|----------|-------|
| **Document ID** | STD-OPTIN-SCI-001 |
| **Version** | v1.0.0 |
| **Status** | Normative Draft |
| **Standard** | STD-OPTIN-001 — OPT-IN Framework Standard v1.1 |
| **Parent** | STD-OPTIN-001 |
| **Companion** | [`science-domain.yaml`](science-domain.yaml) |
| **IDEALE Cross-Reference** | I · A · E · D · L · E₂ (all pillars) |
| **Last Updated** | 2026-03-11 |

---

## 1. Purpose and Scope

This document formalises **Science** as a **domain** within the OPT-IN 5-axis topology and decomposes it into **seven subdomains**, each instantiating the same five axes (O, P, T, I, N) with domain-specific content.

Science is the generative substrate of all IDEALE pillars. It does not sit alongside Information, Defense, Energy, Aerospace, Logistics, and Economy — it **underlies all of them**. This document captures that relationship structurally, enabling:

- Automated cross-pillar traceability between scientific evidence and engineering artefacts
- Governance-grade provenance for research outputs entering the PATH → MTL pipeline
- OPT-IN axis instantiation for every scientific subdomain, enabling programme-level audit

---

## 2. Science Domain Position in OPT-IN

The OPT-IN 5-axis topology (O–P–T–I–N) is the universal programme management structure. Applied to Science:

```
OPT-IN Axis          Science Instantiation
─────────────────────────────────────────────────────────────────────────
O — Organizations    Research institutions, national labs, EU agencies,
                     universities, industry R&D consortia, standards bodies
P — Programs         Horizon Europe, EIC, ERC, national research programmes,
                     EU missions, EuroHPC JU, GAIA-AIR research tracks
T — Technologies     Scientific methods, quantum computing, AI/ML-augmented
                     discovery, simulation, instrumentation, FAIR data tools
I — Infrastructures  EuroHPC, EOSC (European Open Science Cloud), national
                     research data repositories, observatories, test labs
N — Neural Networks  AI-augmented literature review, quantum-accelerated
                     simulation, NBT-gate-enhanced scientific inference,
                     QSN-based knowledge discovery pipelines
─────────────────────────────────────────────────────────────────────────
```

### Invariant

> Science Domain artefacts entering the PATH → MTL pipeline must be anchored to at least one OPT-IN axis instantiation and carry an admissibility classification (C1–C6) before entering any IDEALE pillar baseline.

---

## 3. Science Subdomains

The Science domain decomposes into seven subdomains. Each subdomain maps to one or more IDEALE pillars and is governed by the same OPT-IN structure.

### Subdomain Index

| ID | Subdomain | Primary IDEALE Pillars | OPT-IN Profile |
|----|-----------|------------------------|----------------|
| SCI-01 | Quantum Science & Technology | A · I · D | `sci-01-quantum-TLI.yaml` |
| SCI-02 | Climate & Earth Science | E · A · L | `sci-02-climate-earth-TLI.yaml` |
| SCI-03 | Life Sciences & Biotechnology | E · L · E₂ | `sci-03-life-sciences-TLI.yaml` |
| SCI-04 | Materials Science & Engineering | A · E · L | `sci-04-materials-TLI.yaml` |
| SCI-05 | Computer Science & Informatics | I · A · D | `sci-05-computer-science-TLI.yaml` |
| SCI-06 | Space Science & Astrophysics | A · D · I | `sci-06-space-science-TLI.yaml` |
| SCI-07 | Social & Behavioural Science | E₂ · L · I | `sci-07-social-science-TLI.yaml` |

---

### SCI-01 — Quantum Science & Technology

**Scope:** Quantum computing, quantum sensing, quantum communication, quantum algorithms, and their integration with classical aerospace systems via NBT gates.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | CERN, NIST, Fraunhofer IAF, IQM, QuTech, EU Quantum Flagship consortia |
| **P** | EU Quantum Flagship, EIC Accelerator Quantum Track, AQUA-V programme |
| **T** | Variational quantum algorithms, error correction, QSN inference, quantum sensing arrays |
| **I** | EuroHPC quantum partitions, QPU access via HPCQS, quantum-classical hybrid clusters |
| **N** | NBT gates bridging QSN outputs to classical ESSA pipeline; quantum-augmented manifold computation |

**IDEALE cross-impact:**
- **A:** Quantum simulation of structural mechanics and propulsion fluid dynamics
- **I:** Quantum-encrypted data sovereignty for CSDB and digital product passports
- **D:** Quantum-secure communications for dual-use systems

---

### SCI-02 — Climate & Earth Science

**Scope:** Climate modelling, Earth observation, atmospheric science, geophysics, and their integration into aerospace operational envelopes and ESG constraints.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | ECMWF, Copernicus programme, ESA EO, IPCC, national meteorological services |
| **P** | EU Mission on Adaptation to Climate Change, Destination Earth, Copernicus Climate Change Service |
| **T** | Climate reanalysis models, Earth observation data fusion, atmospheric emission tracking |
| **I** | Copernicus DIAS, EOSC climate data spaces, EuroHPC Destination Earth infrastructure |
| **N** | AI-augmented climate pattern recognition, NBT-enhanced atmospheric state inference |

**IDEALE cross-impact:**
- **E:** Climate impact functions embedded in TLAR energy balance nodes
- **A:** Operational envelope constraints from climate models (wind, temperature, icing)
- **L:** Climate-adjusted supply chain routing and LH₂ distribution logistics

---

### SCI-03 — Life Sciences & Biotechnology

**Scope:** Biological systems, medical research, biotechnology, human factors in aerospace, and biologically-inspired engineering.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | EMA, ECDC, EMBL, biotech consortia, aerospace human factors institutes |
| **P** | EU4Health, Innovative Health Initiative, crew health programmes, biomimetics research |
| **T** | Genomics, bioinformatics, human-systems integration (HSI) methods, biosensor arrays |
| **I** | ELIXIR research infrastructure, European Genome-phenome Archive, human factors test labs |
| **N** | AI-assisted drug discovery, biosignal processing via QSN inference, cognitive load modelling |

**IDEALE cross-impact:**
- **A:** Crew health and human factors in cockpit design (ATA 25, 35) and AMPEL360 Q100 life support
- **L:** Bio-inspired supply chain optimisation and circular economy material cycles
- **E₂:** Biotechnology contribution assets in evidence markets

---

### SCI-04 — Materials Science & Engineering

**Scope:** Advanced materials (composites, metamaterials, smart materials), nanoscience, surface science, and their application to aerospace structures and propulsion.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | DLR, ONERA, CIRA, materials research institutes, Airbus Research, Fraunhofer |
| **P** | Clean Aviation JU, Key Enabling Technologies (KETs) programme, Materials 2030 |
| **T** | Composite manufacturing, additive manufacturing, materials modelling (DFT, MD), NDT |
| **I** | European Materials Modelling Council (EMMC) platform, EUDAT research data infrastructure |
| **N** | AI-driven materials discovery, ML interatomic potentials, quantum chemistry simulation |

**IDEALE cross-impact:**
- **A:** Structural materials for AMPEL360 Q100 BWB airframe (ATA 51–57) and H₂ tanks
- **E:** LH₂ tank materials, insulation, and cryogenic systems (ATA 28)
- **L:** DPP-compliant material traceability from raw material to retirement

---

### SCI-05 — Computer Science & Informatics

**Scope:** Algorithms, software engineering, data science, artificial intelligence, cybersecurity, and formal methods for safety-critical systems.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | INRIA, CWI, Turing Institute, EU AI regulatory bodies, ENISA, EASA AI task forces |
| **P** | EU AI Act implementation, Horizon Europe Digital cluster, DEP (Digital Europe Programme) |
| **T** | Formal verification, model-based engineering, deterministic AI (DWGE), certified ML |
| **I** | EuroHPC JU, GAIA data lakes, CSDB platforms, S1000D toolchains, FAIR data infrastructure |
| **N** | Foundation model governance, QSN inference engines, NBT gate architectures |

**IDEALE cross-impact:**
- **I:** Direct substrate of the Information pillar — DWGE, PATH → MTL, deterministic AI governance
- **A:** Avionics software (DO-178C/DO-254), flight management systems (ATA 22, 34, 46)
- **D:** Cybersecurity for dual-use systems, formal verification of safety-critical logic

---

### SCI-06 — Space Science & Astrophysics

**Scope:** Orbital mechanics, planetary science, astrophysics, space weather, and the scientific return from space infrastructure.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | ESA, CNES, DLR, national space agencies, ESAC, science instrument consortia |
| **P** | ESA Voyage 2050, Cosmic Vision, GAIA constellation science programme, Copernicus |
| **T** | Orbital simulation, space weather modelling, telescope optics, deep-space communications |
| **I** | ESAC data archives, ESA ground stations, GAIA constellation infrastructure, EUSOC |
| **N** | AI-assisted astrophysical data reduction, quantum-accelerated orbital optimisation |

**IDEALE cross-impact:**
- **A:** QAOS (Quantum Aerospace Operating System), AQUA-V programme, orbital logistics
- **D:** Space situational awareness, dual-use satellite technology, export control
- **I:** Space-origin data feeds into IDEALE data sovereignty infrastructure

---

### SCI-07 — Social & Behavioural Science

**Scope:** Economics, sociology, behavioural economics, human factors, governance science, and the social dynamics of technology adoption.

| OPT-IN Axis | Instantiation |
|-------------|--------------|
| **O** | EUI (European University Institute), JRC (Joint Research Centre), social science networks |
| **P** | Horizon Europe Cluster 2 (Culture, Creativity, Inclusive Society), Capillary Merit research |
| **T** | Behavioural modelling, econometrics, governance simulation, contribution scoring models |
| **I** | CESSDA (Social Science Data Infrastructure), SHARE (longitudinal health and retirement study) |
| **N** | Agent-based simulation, AI-assisted policy analysis, merit-weighted contribution algorithms |

**IDEALE cross-impact:**
- **E₂:** Capillary Merit Index (CMI), Teknia Token incentive design, evidence market governance
- **L:** Supply chain social risk modelling, ESG Social enforcement (S pillar)
- **I:** Human factors in information architecture and governance system design

---

## 4. Cross-Domain Governance

### 4.1 IDEALE Pillar Impact Matrix

| Science Subdomain | I | D | E | A | L | E₂ |
|-------------------|---|---|---|---|---|----|
| SCI-01 Quantum    | ● | ● | ○ | ● | ○ | ○  |
| SCI-02 Climate    | ○ | ○ | ● | ● | ● | ○  |
| SCI-03 Life Sci   | ○ | ○ | ● | ○ | ● | ●  |
| SCI-04 Materials  | ○ | ○ | ● | ● | ● | ○  |
| SCI-05 CS/IT      | ● | ● | ○ | ● | ○ | ○  |
| SCI-06 Space Sci  | ● | ● | ○ | ● | ○ | ○  |
| SCI-07 Social Sci | ● | ○ | ○ | ○ | ● | ●  |

*● = primary impact · ○ = secondary impact*

### 4.2 PATH → MTL Integration

Scientific artefacts entering a downstream IDEALE programme must traverse the PATH → MTL pipeline:

```
Scientific Output
    ↓  DWGE intent-lock (semantic normalisation)
Approved Research Artefact
    ↓  Template assignment (ATA chapter / lifecycle phase)
Headed Artefact (traceable to OPT-IN axis + subdomain)
    ↓  Evidence gate (INV-001: must cite K_full(t))
Model Update (Δ knowledge, Δ uncertainty)
    ↓  TEKNIA Ledger (contribution attribution, TT reward)
Registered Science Evidence Asset
```

### 4.3 Contribution Classification

Science contributions are classified under the C1–C6 taxonomy:

| Type | Category | Example |
|------|----------|---------|
| C1 | Direct co-authorship | Joint paper on QSN architectures |
| C2 | Conceptual inspiration | Climate model feeding TLAR node |
| C3 | Licensed dataset | EuroHPC benchmark results |
| C4 | Public domain reference | IPCC climate scenario data |
| C5 | Tool/method reuse | Open-source materials modelling code |
| C6 | Review / validation | Peer review of quantum algorithm |

### 4.4 ESG Enforcement in Science Domain

| ESG | Science Mechanism |
|-----|------------------|
| **E** | Climate impact scoring for research infrastructure (HPC energy use), LCA for materials research |
| **S** | Capillary Merit Index (CMI) for researchers, fair attribution (C1–C6), open access mandates |
| **G** | Deterministic governance via DWGE, hash-chained evidence, monotonic safety invariants |

---

## 5. Governance Boundary

The Science domain boundary conditions:

- **Enters IDEALE** through: evidence packages, qualified models, certified datasets, contribution assets
- **Does not bypass** the PATH → MTL pipeline or DWGE intent-lock layer
- **Is governed by** STD-OPTIN-001 invariants and ESSA constitutional constraints
- **Cannot weaken** downstream sector profile constraints (sector profiles tighten; Science feeds in)

---

## 6. References

| Reference | Document |
|-----------|----------|
| OPT-IN Framework Standard | STD-OPTIN-001 v1.1 |
| PATH → MTL Pipeline | STD-PATH-MTL-001 |
| ESSA Constitutional Layer | ESSA-CONST-001 |
| IDEALE Portal Architecture | README.md §IDEALE Portal |
| Capillary Merit Index | README.md §Trace Threads |
| CCTLS Lifecycle | EACST-STD-CCTLS-001 |
| AMPEL360 Lifecycle | ESSA-DOC-AMPEL360-001 |
| Contribution Taxonomy | contributions-registry.yaml |
