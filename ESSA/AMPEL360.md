# AMPEL360

**Assisted Methods for Programming ESSA Lifecycles**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL360-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Method |
| **Parent** | ESSA-DOC-AMPEL-001 ([AMPEL.md](AMPEL.md)) |
| **Companion** | [`ampel360.yaml`](ampel360.yaml) |
| **Related** | [`AMPEL.md`](AMPEL.md) · [`H-PIPELINE.md`](H-PIPELINE.md) · [`ESSA-AGENCY-CONSTITUTION.md`](ESSA-AGENCY-CONSTITUTION.md) · [`cctls.yaml`](cctls.yaml) |
| **Last Updated** | 2026-03-01 |

---

## Constitutional Constraint (inherited)

> Evolutionary Change ⊆ Valid(H_Envelope)

All AMPEL360 lifecycle transitions are subject to this invariant. No transition may exit the active `H_ENVELOPE`. An out-of-envelope candidate is **non-activable by construction**.

---

## 1. Position in the Stack

```
European Sovereign Systems Architecture  (Tier 1 — Constitutional Substrate)
    ↓
ESSA  (Tier 2 — Constitutional Framework)
    ↓
AMPEL  (Evolutionary Engine — abstract method)
    ↓
AMPEL360  (Lifecycle Programming Engine — this document)
    ↓
Sector Profiles  (Aviation · Space · RSP · Autonomy · Critical Industrial Chains)
```

**AMPEL** defines the general method for programming evolutionary loops within Safety-First governance.

**AMPEL360** is its concrete instantiation for the ESSA lifecycle (P000–P120). "360" is not marketing — it denotes:

| "360" Dimension | Meaning |
|----------------|---------|
| **Full lifecycle coverage** | P000 through P120 — all eleven phases |
| **Cross-chain integration** | Industrial + Digital + Engineering + Authority + Test + Operations + Mission + Reporting |
| **Closed feedback loop** | Operations (P080) → `H_UPDATE` → `H_ENVELOPE` version increment |
| **Profile extensibility** | Sector profiles tighten, never weaken, the ESSA baseline |
| **Governance + mission coherence** | Safety-first doctrine enforced at every gate |

> **360 = complete state-cycle closure.**

---

## 2. What AMPEL360 Is Not

| Not | Is |
|-----|----|
| An AI model | A lifecycle orchestration kernel |
| A PLM (Product Lifecycle Management) system | A governance layer that can integrate PLM/ALM/CAE |
| A document repository | A deterministic transition engine with evidence linkage |
| A regulatory body | The execution method operating under ESSA constitutional authority |

AMPEL360 can integrate PLM, ALM, and CAE toolchains — but it governs transitions; it does not replace them.

---

## 3. Core Engine Responsibilities

### 3.1 Safety-Driven Activation

`H_ENVELOPE` activates the ProgressChain. No phase transition may begin until the active envelope version is established and all prior H-tokens are linked and signed off.

### 3.2 Deterministic Gates

```
INTERPRET → CONFIRM → ACTIVATE → PUBLISH
```

Each gate maps to an active H-token set (as defined in [`H-PIPELINE.md`](H-PIPELINE.md)). A gate is blocked if any required H-token is missing, unsigned, or orphaned.

### 3.3 Security Overlay

AMPEL360 applies the EU-SECURITY MCSC controls at mandatory phases (P020, P050, P080, P090, P120) as an integrity overlay over the safety backbone:

| Control Type | Role in AMPEL360 |
|-------------|-----------------|
| Integrity | Prevents unauthorised mutation of H-tokens |
| Authority | Validates `H_SIGNOFF` provenance |
| Audit | Generates non-repudiable transition records |
| Non-repudiation | Binds every `ACTIVATE` gate to an authority identity |

### 3.4 Conformance Automation (ALPC-ready)

AMPEL360 produces machine-verifiable compliance bundles at each gate:

- All required H-tokens present and linked
- All mandatory EU-SECURITY controls linked per phase
- `H_SIGNOFF` present for every `H_EVIDENCE` record
- No orphaned H-token in the graph

These bundles are the input to the ALPC certification operator (see `ESSA-CONST-001` §6).

### 3.5 Evolutionary Loop Programming

Controlled updates via `H_UPDATE → H_SIGNOFF → H_ENVELOPE` version increment. See [`AMPEL.md`](AMPEL.md) §4.5 for the full Envelope Update procedure.

---

## 4. Full Lifecycle Coverage (P000–P120)

AMPEL360 is active across all eleven CCTLS phases:

| Phase | Name | AMPEL360 Role |
|-------|------|--------------|
| P000 | Digital Baseline | Establish initial `H_ENVELOPE`; derive `H_REQ` from governance inputs |
| P010 | Concept | Hazard identification (`H_HAZARD`); envelope validation |
| P020 | Architecture & Requirements | `H_REQ` tokenisation; MCSC-ETH-03, MCSC-RES-01 mandatory |
| P030 | Industrial Chain | Supply-chain `H_CONSTRAINT` binding; ESG evidence |
| P040 | Engineering | Design artefacts bounded by `H_CONSTRAINT`; DMU/PMU as `H_EVIDENCE` |
| P050 | Authority & Compliance | DOA closure (`H_SIGNOFF`); MCSC-ACC-02, MCSC-ETH-01 mandatory |
| P060 | Integration | Cross-chain coherence check; all H-tokens linked |
| P070 | Test | Test campaigns registered as `H_EVIDENCE`; `H_SIGNOFF` per campaign |
| P080 | Operations | ICA/MRO/occurrences; MCSC-ACC-03, MCSC-SCI-01 mandatory; feedback classification |
| P090 | Mission | Mission control; MCSC-HOB-03, MCSC-ETH-02 mandatory; `H_UPDATE` if safety-relevant |
| P100 | Reporting | Consolidated evidence; SII scoring; all `H_SIGNOFF` confirmed |
| P120 | Baseline Update | Baseline increment; MCSC-RES-* mandatory; `H_ENVELOPE` version increment |

---

## 5. Formal Definition

Let:

- **L** = ESSA Lifecycle (P000–P120)
- **H** = Human Safety Envelope (active `H_ENVELOPE` version)
- **S** = Security Invariants (MCSC controls, active per phase)
- **T** = Token Graph (all H-tokens and their links)

Then AMPEL360 is the function:

```
AMPEL360(L) = {
  ∀ phase pᵢ ∈ L:
    Tokens(pᵢ) ⊆ Valid(H)           -- envelope constraint
    ∧ MCSC(pᵢ) ⊆ S                  -- security invariant
    ∧ Complete(T, pᵢ)               -- no orphaned tokens
    ∧ Signed(H_SIGNOFF, pᵢ)        -- authority confirmed
  ∀ transition tᵢ → tᵢ₊₁:
    Gate(tᵢ → tᵢ₊₁) = PASS         iff all above conditions hold
    Gate(tᵢ → tᵢ₊₁) = BLOCKED      otherwise
}
```

**Gate invariant:** any artefact that cannot satisfy all four conditions **SHALL NOT** be activated.

---

## 6. Relationship to Constitutional Instruments

| Instrument | AMPEL360 Role |
|------------|--------------|
| **ESSA-CONST-001** (ESSA-Agency Constitution) | AMPEL360 satisfies CI-001 (Safety Primacy), CI-002 (Security Governance), CI-003 (Deterministic Gates), CI-004 (Machine-Verifiable Conformance), CI-005 (Feedback Integration) |
| **ESSA-DOC-AMPEL-001** (AMPEL) | AMPEL360 is the concrete lifecycle instantiation of the AMPEL method; inherits all five loop elements and the formal invariant |
| **ESSA-DOC-H-001** (H Pipeline) | AMPEL360 operates the H Pipeline across all eleven phases; every gate maps to its H-token set |
| **ESSA-DOC-SIS-001** (SIS) | AMPEL360 is the operational engine that produces SIS; SIS is achieved when AMPEL360 operates correctly across all eleven phases |
| **ESSA-DOC-SF-001** (Safety-First Doctrine) | AMPEL360 enforces SF-RULE-01 through SF-RULE-06 at every phase boundary |
| **ESSA-STD-CCTLS-001** (CCTLS) | AMPEL360 lifecycle phases map directly to CCTLS phase registry (P000–P120) |
| **EU-SECURITY** (MCSC) | AMPEL360 applies MCSC mandatory linkages at P020, P050, P080, P090, P120 |
