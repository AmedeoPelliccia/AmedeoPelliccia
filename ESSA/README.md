# ESSA

**European Safety and Security Agency**

*A Civil Sovereign Lifecycle Governance Authority*

| Metadata | Value |
|----------|-------|
| **Version** | v1.0-draft |
| **Status** | Constitutional Root Document |
| **Scope** | Aviation · Space · Reusable Platforms · Autonomous Systems · Critical Industrial Chains |
| **Nature** | Federated Safety-First Lifecycle Governance Architecture |

> **Institutional Declaration**
>
> The European Safety and Security Agency (ESSA) operates under a **Safety-First Doctrine**.
> Safety defines mission objectives and generative requirements.
> Security ensures integrity, resilience, and accountability of all safety-critical systems.
>
> *ESSA advances in safety. ESSA protects in security.*

> **Three-Tier ESSA Architecture**
>
> The acronym ESSA resolves at three complementary levels:
>
> | Tier | Level | Full Name | Role |
> |------|-------|-----------|------|
> | 1 | Constitutional Architecture | **European Sovereign Systems Architecture** | The abstract constitutional framework governing lifecycle integrity, certification, and ethical invariants across all sovereign domains |
> | 2 | Institutional Agency | **European Safety and Security Agency** | The civil institutional umbrella — safety mission + security governance — sitting between constitutional architecture and domain implementations |
> | 3 | Domain Implementation | **European Union Space Safety Agency** | The canonical space-based, civil-platforms implementation documented in [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml) |
>
> ESSA (European Safety and Security Agency) is a **governance artefact and institutional model** within the IDEALE-ESG / AMPEL framework. It is **not** currently an enacted EU agency in the legal framework of the European Union. Some analogous functions are performed by the **European Union Agency for the Space Programme (EUSPA)** under the EU Space Programme Regulation (2021/696) and EU Space Act proposals.

---

## 1. Purpose

ESSA defines the constitutional digital architecture for governing aerospace and strategic industrial life cycles under European civil, sovereign, and ethical principles.

ESSA does **not** regulate products.
ESSA governs process integrity, accountability, traceability, and resilience across the entire lifecycle continuum.

**Safety is the primary generative objective** under ESSA.
All derived requirements, design artefacts, and operational transitions **MUST** demonstrate preservation of defined safety invariants prior to activation.
Security governs the integrity of those invariants.
Certification validates their preservation.

### 1.1 Three-Layer Constitutional Hierarchy

The internal structure of ESSA is constitutionally ordered:

| Layer | Name | Function |
|-------|------|----------|
| **Mission Layer** | **Safety** | Defines envelopes, derives requirements, validates evidence, manages incidents, coordinates cross-border safety, oversees autonomous systems |
| **Governance Layer** | **Security** | Governs artefact integrity, change control, cyber resilience, industrial supply chain protection, authority and baseline control |
| **Execution Layer** | **Lifecycle & Operations** | CCTLS lifecycle standard, ALPC certification engine, LCOS runtime, AoR governance, MTLdg ledger |

**Constitutional rule:**
Security **never** redefines the mission.
Security **ensures** that the mission is never corrupted.

### 1.2 Civil Scope

ESSA governs the safety and security of:

- **Aviation** — civil and sovereign aircraft lifecycle
- **Space** — launch, orbital, reusable platforms, end-of-life
- **Reusable Platforms** — RSP lifecycle and refurbishment cycles
- **Autonomous Systems** — AI-assisted operations with human override guarantees
- **Critical Industrial Chains** — supply chain integrity and accountability

### 1.3 Security Clarification

Security in ESSA is **governance of system integrity**, not militarisation.

The EU-SECURITY branch (MCSC) governs:
- Artefact integrity and hash traceability
- Change control and baseline authority
- Cyber resilience for lifecycle-critical systems
- Industrial supply chain assurance
- Autonomous system oversight boundaries

It is a **civil regulatory abstraction**, not a defence or intelligence mechanism.

It enables:

- Safety-bounded synthesis of requirements and design
- Deterministic certification
- Federated interoperability
- Ethical enforcement by design
- Sovereign operational projection

---

## 2. Foundational Doctrine

Any aerospace or strategic system can be represented as a discretised, traceable and certifiable process graph.

Engineering is continuous.
Certification requires discreteness.
**Safety drives generation.**

ESSA formalises two interlocked transformations.

**Safety-first generative pipeline:**

```
Safety Envelope (S)
→ Derived Requirements  [R = f(S)]
→ Restricted Design Space  [D ⊆ Valid(S)]
→ Bounded Optimisation  [Optimise(O) subject to S preserved]
→ Invariant Validation
```

**Lifecycle discretisation pipeline:**

```
Continuous Process
→ Discrete Lifecycle States
→ Tokenised Artefacts
→ Linked Evidence Graph
→ Validated Invariants
→ Certifiable System
```

Certification is not narrative.
Certification is **S-preservation verification** over a governed graph.

---

## 3. Architectural Structure

ESSA is composed of two federated branches and governed by the three-layer constitutional hierarchy.

### Institutional Architecture Mapping

| Component | Role under ESSA |
|-----------|----------------|
| **CIVIL-PLATFORMS** | Operational technical arm — CCTLS lifecycle standard, AoR governance, token graph |
| **EU-SECURITY** | Constitutional integrity layer — MCSC controls protecting safety envelope integrity |
| **ALPC** | Certification operator — deterministic S-preservation validation |
| **LCOS** | Executable engine — runtime validation, packaging, and lifecycle operating system |
| **ESSA** | Institutional umbrella — safety mission + security governance + execution coordination |

---

### 3.1 CIVIL-PLATFORMS

**Path:** `ESSA/CIVIL-PLATFORMS/LC-STD/CCTLS`

**Canonical artefacts:** [`CCTLS.md`](CCTLS.md) · [`cctls.yaml`](cctls.yaml) · [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml)

Defines the operational lifecycle standard:

- Lifecycle domains P000–P120
- AoR (Area of Responsibility) governance model
- Deterministic state machine: INTERPRET → CONFIRM → ACTIVATE → PUBLISH
- Token graph model
- ESG measurable overlay
- DMU/PMU integration
- DOA, CE, ICA, MRO, Mission Operations governance

CCTLS converts lifecycle activity into:

- Governed tokens
- Linked evidence
- Controlled transitions
- Immutable baselines

The civil-platforms space-based implementation is fully specified in:

| Artefact | Description |
|----------|-------------|
| [`cctls.yaml`](cctls.yaml) | Machine-readable CCTLS v0.3.0 — phases P000–P120, token schema, package registry, validation rules |
| [`CCTLS.md`](CCTLS.md) | Human-readable CCTLS specification |
| [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml) | Parts catalogue, registry schema, roadmap, institutional options (space agency fork) |
| [`ANNEX-A-glossary.md`](ANNEX-A-glossary.md) | NORMATIVE — MTL/MTLdg/DOF glossary |
| [`annex-a-glossary.yaml`](annex-a-glossary.yaml) | Machine-readable ANNEX-A terms catalogue |

---

### 3.2 EU-SECURITY

**Path:** `ESSA/EU-SECURITY/INTEGRATIONS`

**Canonical artefact:** [`EU-SECURITY/README.md`](EU-SECURITY/README.md)

EU-SECURITY defines the **Minimum Common Security Constitution (MCSC)**.

It is **not** combat doctrine.
It is a regulatory abstraction ensuring:

- Ethical invariants
- Accountability
- Resilience
- Supply chain integrity
- Human oversight boundaries
- Sovereign interoperability

EU-SECURITY operates as an **overlay**, not a parallel lifecycle.

It extends CIVIL-PLATFORMS through machine-checkable control registries.

---

### 3.3 ESSA-Agency Constitution

**Canonical artefacts:** [`ESSA-AGENCY-CONSTITUTION.md`](ESSA-AGENCY-CONSTITUTION.md) · [`essa-agency-constitution.yaml`](essa-agency-constitution.yaml)

**Document ID:** `ESSA-CONST-001`

The ESSA-Agency Constitution is the **constitutional bridge instrument** that:

- Positions ESSA-Agency between ESSA-Architecture and sector agencies (EUSSA – the ESSA space-domain implementation, Aviation, RSP, Autonomy)
- Formalises the Safety=Mission / Security=Governance separation
- Establishes the doctrine: *Advance in Safety, Protect in Security*
- Defines the agentic operating model (safety envelopes as first-class artefacts)
- Specifies profile extensibility (`PROFILE-AVIATION-CS25`, `PROFILE-SPACE-SAFETY`, `PROFILE-RSP-REUSE-CYCLES`, `PROFILE-AUTONOMY-ASSURANCE`, `PROFILE-CRITICAL-INDUSTRIAL-CHAINS`)
- Enumerates seven constitutional invariants (CI-001 through CI-007)
- Mandates the ALPC certification operator for machine-verifiable conformance

---

### 3.4 Structural Integration State (SIS)

**Canonical artefacts:** [`SIS.md`](SIS.md) · [`sis.yaml`](sis.yaml)

**Document ID:** `ESSA-DOC-SIS-001`

The **Structural Integration State** is the constitutional condition achieved when architecture, governance, safety mission, and security invariants operate coherently within a unified lifecycle graph.

Seven conditions must hold simultaneously (SIS-C-001 through SIS-C-007):
Safety Envelope Generation · Bounded Design · Integrity Governance · Invariant Certification · Operational Feedback · Traced Authority · Federated Interoperability

SIS is measured by the **Structural Integration Index (SII)** across five dimensions: Ontological · Normative · Operational · Ethical · Technological.

Priority ordering: **Safety > Security > Performance** — without exception.

---

### 3.5 Total Cross-Chain H Pipeline

**Canonical artefacts:** [`H-PIPELINE.md`](H-PIPELINE.md) · [`h-pipeline.yaml`](h-pipeline.yaml)

**Document ID:** `ESSA-DOC-H-001`

The **Total Cross-Chain H Pipeline** is the Human-Safety end-to-end backbone — the operational implementation of the Safety-First Doctrine across all lifecycle chains and phases.

> No deliverable is activable unless it is linked to the H pipeline.

The H Pipeline defines eight cross-chain scopes (Industrial · Digital · Engineering · Authority · Test · Operations · Mission · Reporting), each mapped to its canonical CCTLS phase(s), and a minimum H-token ontology:

| Token | Role |
|-------|------|
| `H_ENVELOPE` | Non-negotiable safety bounds — must exist before any derivation |
| `H_HAZARD` | Identified hazard linked to the envelope |
| `H_REQ` | Safety requirement derived from envelope or hazard |
| `H_CONSTRAINT` | Operational/architectural constraint derived from requirement |
| `H_EVIDENCE` | Verifiable proof (test · analysis · operational) |
| `H_EXCEPTION` | Controlled deviation — requires mitigation, rollback, and `H_SIGNOFF` |
| `H_UPDATE` | Envelope update from operational occurrence — triggers re-validation |
| `H_SIGNOFF` | Authority acceptance — required on every evidence before activation |

The mandatory traceability topology is: `H_ENVELOPE → H_HAZARD → H_REQ → H_CONSTRAINT → H_EVIDENCE → H_SIGNOFF`, with an operational feedback loop (`occurrence → H_UPDATE → H_ENVELOPE`) and a controlled exception path.

Gate invariant: any artefact that cannot produce a complete `H_ENVELOPE → … → H_SIGNOFF` chain **SHALL NOT** be activated.

---

### 3.6 AMPEL — Assisted Methods for Programming Evolutionary Loops

**Canonical artefacts:** [`AMPEL.md`](AMPEL.md) · [`ampel.yaml`](ampel.yaml)

**Document ID:** `ESSA-DOC-AMPEL-001`

**AMPEL** is the evolutionary engine operating within ESSA's constitutional framework — the structural method for programming evolutionary loops under Safety-First governance.

> **Formal invariant:** `Evolutionary Change ⊆ Valid(H_Envelope)`

AMPEL is not a product, brand, or AI tool. It defines:

- **The Evolutionary Loop (EL)**: `H_ENVELOPE → Requirements → Design → Evidence → Authority → Release → Operation → Feedback → H_UPDATE → H_ENVELOPE` — the ProgressChain with closed-loop feedback, contained by invariants
- **Five Assisted Methods**: Generation · Analysis · Simulation · Evaluation · Impact Analysis — each tool-augmented, human-authority-confirmed, envelope-bounded
- **Five Loop Programming Elements**: States · Transitions · Inhibitors · Feedback · Envelope Update
- **ESSA placement**: `ESSA (Constitution) → AMPEL (Evolutionary Engine) → Sector Profiles (Aviation · Space · RSP · Autonomy)`

Evolution does not seek maximum efficiency. It seeks improvement within Human Safety — an out-of-envelope candidate is non-activable by construction.

---

### 3.7 AMPEL360 — Assisted Methods for Programming ESSA Lifecycles

**Canonical artefacts:** [`AMPEL360.md`](AMPEL360.md) · [`ampel360.yaml`](ampel360.yaml)

**Document ID:** `ESSA-DOC-AMPEL360-001`

**AMPEL360** is the concrete lifecycle instantiation of AMPEL — the **programmable execution layer** for ESSA lifecycle architectures. It is not abstract: it governs the ESSA lifecycle (P000–P120) end-to-end.

> **"360" = complete state-cycle closure** — full lifecycle coverage (P000–P120), cross-chain integration, closed feedback loop, profile extensibility, and governance + mission coherence.

AMPEL360 implements five core responsibilities:

- **Safety-Driven Activation** — `H_ENVELOPE` activates the ProgressChain; no phase begins without an established envelope
- **Deterministic Gates** — `INTERPRET → CONFIRM → ACTIVATE → PUBLISH`; any gate is blocked when required H-tokens are missing, unsigned, or orphaned
- **Security Overlay** — MCSC controls mandatory at P020, P050, P080, P090, P120 (integrity · authority · audit · non-repudiation)
- **Conformance Automation** — machine-verifiable ALPC-ready compliance bundles at each gate
- **Evolutionary Loop Programming** — `H_UPDATE → H_SIGNOFF → H_ENVELOPE` version increment

**Formal gate invariant:** any artefact that cannot satisfy envelope constraint ∧ security invariant ∧ token completeness ∧ authority confirmation **SHALL NOT** be activated.

AMPEL360 is the operational engine that produces the Structural Integration State (SIS): when AMPEL360 operates correctly across all eleven phases, SIS is achieved.

### 3.8 AMPEL360 Domain Profiles

AMPEL360 is a single kernel with **profile-adaptive** specialisations per regulatory domain. Each profile tightens AMPEL360 parameters; no profile weakens the ESSA baseline.

| Profile | Domain | Authority | Canonical Artefacts |
|---------|--------|-----------|---------------------|
| **AMPEL360 Q100** | Civil Aviation (~100 pax) | EASA / CS-25 / Part-21 | [`AMPEL360-Q100.md`](AMPEL360-Q100.md) · [`ampel360-q100.yaml`](ampel360-q100.yaml) |
| **AMPEL360 Q10** | Spacecraft / Orbital / Reusable | ESA / ECSS / EU Space Reg | [`AMPEL360-Q10.md`](AMPEL360-Q10.md) · [`ampel360-q10.yaml`](ampel360-q10.yaml) |

**Document IDs:** `ESSA-DOC-AMPEL360-Q100-001` · `ESSA-DOC-AMPEL360-Q10-001`

---

## 4. Discretisation Principle

ESSA enforces controlled discretisation.

Continuous development is transformed into:

- Discrete state tokens
- Quantified artefacts
- Structured transitions
- Enforced invariants

Discretisation **SHALL** balance:

- Certifiability
- Operational fluidity
- Administrative burden

Too coarse → unverifiable.
Too granular → bureaucratic collapse.

Optimal resolution enables automation and ethical enforcement.

---

## 5. Governance Model

ESSA governance relies on:

- Unique token identity
- Cryptographic integrity (sha3-512)
- Schema versioning
- Mandatory link semantics
- Authority-bound transitions
- Confirm → Activate gating
- Immutable baselines
- Audit-ready graph topology

No activation without confirmation.
No publication without invariant validation.

---

## 6. Certification Layer (ALPC Alignment)

ALPC functions as the **Certification Operator** over ESSA process graphs.

It evaluates:

- Structural completeness
- Traceability coverage
- Evidence sufficiency
- EU-SECURITY control coverage
- Phase coherence
- Baseline integrity

Certification becomes deterministic conformance validation.

---

## 7. Ethical Commitment

ESSA embeds ethics as executable constraints.

Minimum ethical commitments **SHALL** include:

- Traceable authority
- Human override paths
- Non-maleficence constraints
- Transparent auditability
- Supply chain accountability
- Resilience under stress

Ethics is enforced at gate level, not declared rhetorically.

---

## 8. Venture Interface

ESSA enables venture development while preserving constitutional invariants.

It provides:

- A sovereign governance substrate
- A lifecycle operating framework
- Deterministic validation engines (LCOS)
- Federated interoperability

Commercial layers **MAY** build upon ESSA.
They **SHALL NOT** weaken its core invariants.

---

## 9. Long-Term Vision

ESSA seeks to:

- Decouple industrial intelligence from ecological degradation
- Enable sovereign digital engineering
- Provide ethical outward projection of capability
- Establish interoperable European lifecycle governance

ESSA is not static.
It is a federated constitutional architecture.

---

## 10. Safety-First Constitutional Clause

> **Safety SHALL be treated as the primary generative objective in all lifecycle design processes governed under ESSA.**
>
> All derived requirements, design artefacts, and operational transitions **MUST** demonstrate preservation of defined safety invariants prior to activation.
>
> Security governs the integrity of those invariants.
> Certification validates their preservation.
> No element of the lifecycle graph **SHALL** be activated if safety coverage is incomplete.

**Institutional Declaration (ESSA Safety-First Doctrine):**

> The European Safety and Security Agency (ESSA) operates under a Safety-First Doctrine.
> Safety defines mission objectives and generative requirements.
> Security ensures integrity, resilience, and accountability of all safety-critical systems.

### Three-Layer Constitutional Hierarchy

| Layer | Concept | Role |
|-------|---------|------|
| **Mission Layer** | **Safety** | Defines envelopes · derives requirements · validates evidence · manages incidents · coordinates cross-border safety · oversees autonomy |
| **Governance Layer** | **Security** | Governs artefact integrity · change control · cyber resilience · industrial chain protection · baseline authority |
| **Execution Layer** | **Lifecycle & Operations** | CCTLS · ALPC · LCOS · AoR · MTLdg |

**Constitutional rule:** Security never redefines the mission. Security ensures the mission is never corrupted.

### Security Clarification

Security in ESSA is **governance of system integrity, not militarisation**.

The EU-SECURITY (MCSC) layer is a civil regulatory abstraction:
- It does **not** impose military command structures.
- It does **not** activate defence or intelligence mandates.
- It **does** protect the integrity of safety invariants from corruption, interference, or circumvention.

### Safety vs Security — Architectural Ordering

| Concept | Role |
|---------|------|
| **Safety** | Primary generative objective — defines the envelope within which all design, operation, and certification proceeds |
| **Security** | Governance of safety envelope integrity — protects safety invariants from corruption, interference, or circumvention |

Safety precedes security in the generative order.
Security exists to preserve what safety defines.

The formal model is specified in [`SAFETY-FIRST.md`](SAFETY-FIRST.md) and [`safety-first.yaml`](safety-first.yaml).

---

## 11. Glossary of Terminology and Acronyms

---

### ALPC

**Aerospace Life Process Certification Standard**

Certification operator validating conformance of ESSA lifecycle graphs. Evaluates structural completeness, traceability coverage, evidence sufficiency, EU-SECURITY control coverage, phase coherence, and baseline integrity.

---

### AoR

**Area of Responsibility**

Governed lifecycle unit represented by a portal card and associated tokens. Required fields: `aor_id`, `title`, `phase`, `domain`, `owner_role`, `audience_role`, `lifecycle_deliverable_product`, `bindings`, `template_id`, `metadata_schema_id`.

---

### Baseline (BL)

Immutable, signed state of a governed process graph at a specific lifecycle point. Formal definition: `Baseline := { ledger_snapshot_id, artifact_set }`.

---

### CCTLS

**Controlled Convergent Token Lifecycle System**

Lifecycle governance standard (document ID: ESSA-STD-CCTLS-001, v0.3.0) defining tokens, states, and graph topology across phases P000–P120. Specified in [`cctls.yaml`](cctls.yaml) and [`CCTLS.md`](CCTLS.md).

---

### CE

**Conformité Européenne**

European product compliance marking process integrated within lifecycle governance (phase P060).

---

### DMU

**Digital Mock-Up**

Digital representation of product geometry and structure. Governed under phase P040.

---

### DOA

**Design Organisation Approval**

Authority-bound approval function within lifecycle governance. Governed under phase P050 via token type `DOA_SIGN`.

---

### ESG

**Environmental, Social, Governance**

Measured sustainability overlay integrated into lifecycle tokens and chain nodes. Measured on chains (P030) and operations/MRO (P080); consolidated in P100.

---

### ESSA

**ESSA** is used in this document as a three-tier acronym:

- **Tier 1 — European Sovereign Systems Architecture** (this document layer — constitutional digital substrate)
- **Tier 2 — European Safety and Security Agency** (institutional mission and governance layer)
- **Tier 3 — European Union Space Safety Agency** (space-domain execution fork; also referenced as EUSSA to disambiguate from the tier-2 acronym)

The canonical space-based civil-platforms fork is documented in [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml).

---

### EU-SECURITY

Regulatory abstraction layer defining the **Minimum Common Security Constitution (MCSC)** controls. Operates as an overlay over CIVIL-PLATFORMS. Documented in [`EU-SECURITY/README.md`](EU-SECURITY/README.md).

---

### EUSPA

**European Union Agency for the Space Programme**

Enacted EU agency under Regulation (EU) 2021/696. Normative counterpart of the ESSA space-based fork. Performs analogous functions for Galileo, Copernicus, GOVSATCOM, and EU SST.

---

### ICA

**Instructions for Continued Airworthiness**

Operational lifecycle documentation governing in-service maintenance. Token type `ICA_TASK` under phase P080.

---

### LCOS

**Life Cycle Operating System**

Executable runtime layer validating, packaging, and enforcing lifecycle conformance over ESSA process graphs.

---

### MCSC

**Minimum Common Security Constitution**

Set of ethical and resilience invariants applied across lifecycle domains via the EU-SECURITY overlay.

---

### MRO

**Maintenance, Repair and Overhaul**

Operational lifecycle domain for in-service support and refurbishment. Governed under phase P080.

---

### MTL / MTLdg

**Meta Transformation Law / Master Teknia Ledger**

MTL: formal contract defining invariant transformation between input and output state. MTLdg: append-only authoritative registry storing artefact identity, contract binding, implementation hash, verification status, authority signature, and lifecycle state. Fully specified in [`ANNEX-A-glossary.md`](ANNEX-A-glossary.md).

---

### PMU

**Process Mock-Up**

Simulation and numerical modelling domain supporting validation. Governed under phase P040.

---

### P000–P120

Lifecycle domain identifiers defining operational scope within CCTLS:

| Phase | Name |
|-------|------|
| P000 | Registry & Governance |
| P010 | Scope & Operational Context |
| P020 | Safety & Risk Envelope |
| P030 | Logistics & Industrial Chains |
| P040 | Numerical & Simulation Methods (DMU+PMU) |
| P050 | Design Office Authority (DOA sign) |
| P060 | Product/Tool Quality & Conformity (CE) |
| P070 | Flight Tests (CERT) |
| P080 | In-Service + ICAs + MRO |
| P090 | Mission Ops & Traffic / Range Control |
| P100 | ESG Reporting & Transparency |
| P110 | RESERVED |
| P120 | Cyber & Resilience (Cross-cutting) |

---

### Token

Governed lifecycle artefact with unique ID, version, hash (sha3-512), bindings, and graph links. Required fields: `token_id`, `token_type`, `phase`, `package_id`, `subpackage_id`, `aor_id`, `title`, `version`, `checksum`, `template_id`, `metadata_schema_id`, `bindings`, `links`, `children`, `status`.

---

### Transition

Governed state change between lifecycle statuses (`DRAFT → CONFIRMED → ACTIVATED → PUBLISHED → OBSOLETE`) subject to invariant validation.

---

### Invariant

Machine-verifiable condition that **SHALL** hold across lifecycle states for certification.

---

### Safety Envelope (S)

The complete set of safety invariants (`HAZARD` + `SAF_OBJ` tokens at P020) that define the bounded space within which all derived requirements, design artefacts, and operational transitions must operate. No design candidate **SHALL** be evaluated if it violates any element of S. Formally specified in [`SAFETY-FIRST.md`](SAFETY-FIRST.md).

---

### Safety-First

Architectural principle establishing safety as the **primary generative objective** under ESSA. Requirements are derived from S. Design space is restricted to D ⊆ Valid(S). Optimisation operates subject to S being preserved. Governed by SF-RULE-01 through SF-RULE-06. See the constitutional clause in §10 and [`SAFETY-FIRST.md`](SAFETY-FIRST.md).

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml) | Machine-readable ESSA space-agency specification: Parts catalogue, registry schema, implementation phases, institutional options |
| [`cctls.yaml`](cctls.yaml) | Machine-readable CCTLS v0.3.0 lifecycle standard |
| [`CCTLS.md`](CCTLS.md) | Human-readable CCTLS specification |
| [`ANNEX-A-glossary.md`](ANNEX-A-glossary.md) | NORMATIVE — ANNEX-A: Glossary of MTL/MTLdg/DOF concepts |
| [`annex-a-glossary.yaml`](annex-a-glossary.yaml) | Machine-readable ANNEX-A terms catalogue |
| [`EU-SECURITY/README.md`](EU-SECURITY/README.md) | EU-SECURITY branch — Minimum Common Security Constitution (MCSC) |
| [`SAFETY-FIRST.md`](SAFETY-FIRST.md) | Safety-First Doctrine — formal generative model, CCTLS token rules, agentic AI contract, constitutional clause |
| [`safety-first.yaml`](safety-first.yaml) | Machine-readable companion — ESSA-DOC-SF-001 safety-first formal model and normative rules |
| [`CASE.md`](CASE.md) | Case study — ESSA-ESSA conceptual demonstrator: European Sovereign Systems Architecture applied to a European Union Space Safety Agency (12-section structural analysis) |
| [`case.yaml`](case.yaml) | Machine-readable companion — ESSA-CASE-001 structural model: problem dimensions, architectural mappings, operational model, ethical constraints, and governance conclusions |
| Root [`README.md`](../README.md) | Profile-level reference to ESSA under Current Focus |
