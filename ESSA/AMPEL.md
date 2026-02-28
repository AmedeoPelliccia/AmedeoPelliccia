# AMPEL

**Assisted Methods for Programming Evolutionary Loops**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Method |
| **Parent** | ESSA-CONST-001 ([ESSA-AGENCY-CONSTITUTION.md](ESSA-AGENCY-CONSTITUTION.md)) |
| **Companion** | [`ampel.yaml`](ampel.yaml) |
| **Related** | [`H-PIPELINE.md`](H-PIPELINE.md) · [`SAFETY-FIRST.md`](SAFETY-FIRST.md) · [`SIS.md`](SIS.md) · [`cctls.yaml`](cctls.yaml) |
| **Last Updated** | 2026-02-28 |

---

## Constitutional Constraint

> Evolutionary Change ⊆ Valid(H_Envelope)

No evolutionary step produced by AMPEL may exit the valid region of the active `H_ENVELOPE`. An out-of-envelope change candidate is **non-activable by construction**.

---

## 1. Nature

AMPEL is **not**:

- A product
- A brand
- An AI tool

AMPEL **is**:

> A structural method for programming evolutionary loops within a Safety-First governance framework.

Its operating properties are:

| Property | Definition |
|----------|------------|
| **Controlled Evolution** | Change is initiated and bounded by safety invariants, not by performance pressure |
| **Governed Change** | Every transition is authorised through the CCTLS governance kernel (INTERPRET → CONFIRM → ACTIVATE → PUBLISH) |
| **Envelope-Bounded Adaptation** | No candidate design, configuration, or process update may exit the active `H_ENVELOPE` |
| **Integrated Feedback** | Operational evidence flows back into the loop and may trigger envelope updates (`H_UPDATE`) |

---

## 2. The Evolutionary Loop (EL)

An **Evolutionary Loop** is the ProgressChain with closed-loop feedback:

```
H_ENVELOPE
    ↓
Requirements  (H_REQ derivation)
    ↓
Design  (bounded by H_CONSTRAINT)
    ↓
Evidence  (H_EVIDENCE: test · analysis · operational)
    ↓
Authority  (H_SIGNOFF — DOA closure)
    ↓
Release  (ACTIVATE gate — envelope validated)
    ↓
Operation  (P080 — ICA/MRO/mission)
    ↓
Feedback  (occurrences, performance, incidents)
    ↓
H_UPDATE  (if safety-relevant)
    ↓
H_ENVELOPE  (version increment → loop restart)
```

**Critical distinction:** The Evolutionary Loop is **not free change**. It is change **contained by invariants**. Each iteration must satisfy the same constitutional constraints as the first.

---

## 3. Assisted Methods

"Assisted" in AMPEL means **human-authority-confirmed, tool-augmented** — not autonomous.

| Method | Scope | Constraint |
|--------|-------|------------|
| **Assisted Generation** | Requirements, design candidates, artefact drafts | Output must be within H_ENVELOPE before presentation |
| **Assisted Analysis** | Hazard analysis, impact analysis, safety case evaluation | Results must be traceable as H_EVIDENCE |
| **Assisted Simulation** | DMU/PMU, mission simulation, digital twin runs | Outputs registered as H_EVIDENCE linked to H_REQ |
| **Assisted Evaluation** | Conformance checking, ALPC certification, SII scoring | Machine-verifiable; no narrative substitution |
| **Assisted Impact Analysis** | Change impact across all eight H-Pipeline chains | Mandatory before any CONFIRM gate |

**Non-negotiable rule:** All assisted outputs operate under `H_ENVELOPE` as primary constraint. If an assisted method proposes a candidate that violates the envelope, **activation is blocked** — the method does not override the envelope.

---

## 4. Programming the Evolutionary Loop

"Programming" the loop means defining its five formal elements:

### 4.1 States

Discrete, tokenised lifecycle states. Each state carries:

- An active `H_ENVELOPE` version
- A set of open `H_REQ` and `H_CONSTRAINT` tokens
- A completeness status (% of `H_EVIDENCE` linked and signed off)

### 4.2 Transitions

State transitions are permissible only when:

1. The CCTLS gate condition is satisfied (forward direction)
2. The candidate remains within the active `H_ENVELOPE` (envelope check)
3. Authority (`H_SIGNOFF`) is present for all gate-relevant evidence

Transitions that fail either condition are **inhibited**.

### 4.3 Inhibitors

An inhibitor blocks a transition when:

| Inhibitor Condition | Effect |
|--------------------|--------|
| Candidate exits H_ENVELOPE | Transition blocked; candidate is non-activable |
| Missing H_SIGNOFF on any H_EVIDENCE | ACTIVATE gate blocked |
| Open H_EXCEPTION without H_SIGNOFF | CONFIRM gate blocked |
| Orphaned H-token (no upward link) | Loop consistency violation; system halts |

### 4.4 Feedback

Feedback enters the loop from the Operations Chain (P080) and Mission Chain (P090). It is classified as:

- **Non-safety-relevant** — logged; no loop restart required
- **Safety-relevant** — generates `H_UPDATE`; triggers envelope re-evaluation; may restart the loop from the Requirements step

### 4.5 Envelope Update

When `H_UPDATE` is accepted by authority (`H_SIGNOFF` on update):

1. `H_ENVELOPE` version increments
2. All dependent `H_REQ`, `H_CONSTRAINT`, and `H_EVIDENCE` tokens are re-evaluated
3. Any candidate that was valid under the previous envelope is re-checked against the new one
4. Invalid candidates are **withdrawn from activation** (non-activable under new envelope)

---

## 5. AMPEL Within ESSA

ESSA defines the constitutional architecture. AMPEL is the **evolutionary engine** operating within it.

```
European Sovereign Systems Architecture  (Tier 1 — Constitutional Substrate)
    ↓
ESSA  (Tier 2 — Constitutional Framework)
    ↓
AMPEL  (Evolutionary Engine — this document)
    ↓
Sector Profiles  (Aviation · Space · RSP · Autonomy · Critical Industrial Chains)
```

| Layer | Role |
|-------|------|
| **ESSA** | Defines constitutional limits, invariants, and safety-first doctrine |
| **AMPEL** | Executes governed evolution within those limits; manages loop states, transitions, inhibitors, feedback |
| **Sector Profiles** | Tighten AMPEL parameters for their domain; cannot weaken ESSA constitutional baseline |

**AMPEL does not replace ESSA governance. AMPEL operates under it.**

---

## 6. Safety-First Implication

In AMPEL, evolution does **not** seek maximum efficiency. It seeks:

> **Improvement within Human Safety — constrained, evidence-backed, authority-confirmed.**

Formal invariant:

```
Evolutionary Change ⊆ Valid(H_Envelope)
```

This means:

- The method learns from incidents — every `H_UPDATE` carries the operational evidence that generated it
- The method does **not** optimise by violating the envelope
- Performance gains are a **consequence** of safe evolution, not its objective
- If an optimisation path requires exiting the envelope, the path is rejected — the envelope is revised first (through proper `H_UPDATE` → `H_SIGNOFF` → envelope increment), then the optimisation is re-evaluated

---

## 7. Relationship to Constitutional Instruments

| Instrument | AMPEL Role |
|------------|------------|
| **ESSA-CONST-001** (ESSA-Agency Constitution) | AMPEL satisfies CI-001 (Safety Primacy), CI-003 (Deterministic Gates), CI-005 (Feedback Integration) |
| **ESSA-DOC-SF-001** (Safety-First Doctrine) | AMPEL is the operational method that enforces safety-first in the generative loop |
| **ESSA-DOC-H-001** (H Pipeline) | AMPEL operates the H Pipeline: each loop iteration generates, validates, and updates H-tokens |
| **ESSA-DOC-SIS-001** (Structural Integration State) | AMPEL contributes to SIS-C-005 (Operational Feedback) and SIS-C-001 (Safety Envelope Generation) |
| **ESSA-STD-CCTLS-001** (CCTLS) | AMPEL loop transitions map directly to CCTLS gate sequence (INTERPRET → CONFIRM → ACTIVATE → PUBLISH) |
