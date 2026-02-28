# ESSA — Safety-First Doctrine

**Safety as the Primary Generative Objective in Lifecycle Governance**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-SF-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Doctrine |
| **Parent** | ESSA Constitutional Root Document ([README.md](README.md)) |
| **Companion** | [`safety-first.yaml`](safety-first.yaml) |
| **Last Updated** | 2026-02-28 |

---

## Preamble

Safety and security are not synonyms.
They are **functionally distinct** and **architecturally ordered**:

| Concept | Role in ESSA |
|---------|-------------|
| **Safety** | The **primary generative objective** — defines the envelope within which all design, operation, and certification proceeds |
| **Security** | **Governance of the integrity of that envelope** — protects safety invariants from corruption, interference, or circumvention |

This separation is not terminological.
It is **architectural**.

Safety precedes security in the generative order.
Security exists to preserve what safety defines.

---

## 1. Core Principle

Safety is **not** a constraint checked after design.

Safety is the **generative objective** that shapes the design space.

Traditional engineering flow:

```
Requirements → Design → Test → Verify Safety
```

ESSA Safety-First generative flow:

```
Safety Envelope
→ Derived Requirements
→ Restricted Design Space
→ Bounded Optimisation
→ Invariant Validation
```

Safety becomes the **primary objective function**.
Not a constraint term appended at the end of an optimisation problem.

---

## 2. Formal Generative Model

Let:

| Symbol | Meaning |
|--------|---------|
| **S** | Safety invariant set |
| **R** | Derived requirements |
| **D** | Design space |
| **O** | Optimisation goals (performance, cost, efficiency) |

The safety-first generative model is defined as:

```
R = f(S)

D ⊆ Valid(S)

Optimise(O)  subject to  S is preserved
```

**Consequences:**

- No requirement **SHALL** be generated without a traceable safety invariant as its source.
- No design candidate **SHALL** be evaluated if it violates any element of S.
- Optimisation **SHALL** operate exclusively within the safety-valid design space.
- Safety bounds **SHALL NOT** be relaxed to achieve optimisation targets.

---

## 3. CCTLS Implementation

In CCTLS token graph terms, the formal model maps as follows:

| Model Element | CCTLS Realisation | Phase |
|---------------|------------------|-------|
| S — Safety invariant set | `HAZARD` + `SAF_OBJ` tokens | P020 |
| R = f(S) — Derived requirements | Requirement tokens with `derives_from` link to P020 | P010, P020 |
| D ⊆ Valid(S) — Design space restriction | Design tokens require `supports` link to SAF_OBJ | P040, P050 |
| Optimise(O) subject to S | Certification test tokens verify S coverage | P070 |
| S preservation in operation | In-service tokens linked to safety objectives via ICA chain | P080 |

### 3.1 Token Linkage Rules (Normative)

The following rules **SHALL** apply to all lifecycle graphs governed under ESSA:

**SF-RULE-01** — Safety Primacy
: Every `SAF_OBJ` token **SHALL** be generated at P020 before any design token is created at P040 or P050.

**SF-RULE-02** — Requirement Traceability
: Every requirement token **SHALL** carry a `derives_from` link to at least one `SAF_OBJ` token.

**SF-RULE-03** — Design Coverage
: Every design token at P040/P050 **SHALL** carry a `supports` link to at least one `SAF_OBJ` token.

**SF-RULE-04** — Confirm Gate Enforcement
: The CONFIRM gate **SHALL** fail if the safety coverage graph is incomplete (i.e., any SAF_OBJ has no supporting design token).

**SF-RULE-05** — No Self-Relaxation
: No automated process or AI agent **SHALL** modify the safety invariant set S without explicit human authority (MCSC-HOB-03) and DOA sign-off (P050 DOA_SIGN token).

**SF-RULE-06** — Preservation in Operation
: Every `ICA_TASK` and `MRO_JOB` token at P080 **SHALL** carry a `preserves` link to the `SAF_OBJ` tokens it maintains.

### 3.2 Safety Coverage Graph

```
P020: SAF_OBJ ─────────────────────────────────────────────────────┐
                │ (derives_from)                                    │
P010/P020:  REQUIREMENT ────────────────────────────────────────┐  │ (preserves)
                │ (supports)                                     │  │
P040/P050:  DESIGN / DOA_SIGN ──────────────────────────────┐   │  │
                │ (verifies)                                 │   │  │
P070:       TEST_REPORT ─────────────────────────────────┐  │   │  │
                │                                         │  │   │  │
P080:       ICA_TASK / MRO_JOB ──────────────────────────┘──┘───┘──┘
                │                                         (preserves)
P100:       ESG_REPORT ──────────────────────── (consolidates)
```

Safety traceability is **continuous** across the lifecycle.
No phase is exempt from the safety coverage obligation.

---

## 4. Agentic AI Contract

If LCOS includes generative AI components, the following contract **SHALL** apply.

An ESSA-governed AI agent:

| Obligation | Rule |
|------------|------|
| Ingest safety invariant set before generating | Agent **SHALL** receive S as read-only input at initialisation |
| Generate only within bounded design manifold | Agent **SHALL NOT** produce candidates outside D ⊆ Valid(S) |
| Produce traceable justification links | Every generated token **SHALL** carry `derives_from` or `supports` links to S |
| Flag safety uncertainty explicitly | Agent **SHALL** emit a `SAF_UNCERTAINTY` marker on any output where S coverage is partial |
| Never self-relax safety bounds | Agent **SHALL NOT** modify, override, or propose relaxation of S without human authority |

This prevents **creative drift**: the tendency of unconstrained generative processes to optimise performance at the expense of safety invariants.

The AI agent operates as a **bounded synthesis engine**, not a free design oracle.

---

## 5. Institutional Consequence

### 5.1 Agency Identity and Mission

The European Safety and Security Agency (ESSA) operates as a **Civil Sovereign Lifecycle Governance Authority**.

Institutional declaration:

> **The European Safety and Security Agency (ESSA) operates under a Safety-First Doctrine.**
> Safety defines mission objectives and generative requirements.
> Security ensures integrity, resilience, and accountability of all safety-critical systems.
>
> *ESSA advances in safety. ESSA protects in security.*

If ESSA-ESSA is safety-first, the agency mission statement becomes:

> **The generation, validation, and continuous preservation of safety envelopes for European space and aerospace systems.**

### 5.2 Three-Layer Constitutional Hierarchy

The internal structure of ESSA is constitutionally ordered across three layers:

| Layer | Name | Function |
|-------|------|----------|
| **Mission Layer** | **Safety** | Defines envelopes · derives requirements · validates evidence · manages incidents · coordinates cross-border safety · oversees autonomous systems |
| **Governance Layer** | **Security** | Governs artefact integrity · change control · cyber resilience · industrial chain protection · baseline authority |
| **Execution Layer** | **Lifecycle & Operations** | CCTLS lifecycle standard · ALPC certification engine · LCOS runtime · AoR governance · MTLdg ledger |

**Constitutional rule** (canonical: [README.md §1.1](README.md)):
Security **never** redefines the mission.
Security **ensures** that the mission is never corrupted.

### 5.3 Civil Scope

ESSA governs the safety and security of:

- **Aviation** — civil and sovereign aircraft lifecycle
- **Space** — launch, orbital, reusable platforms, end-of-life
- **Reusable Platforms** — RSP lifecycle and refurbishment cycles
- **Autonomous Systems** — AI-assisted operations with human override guarantees
- **Critical Industrial Chains** — supply chain integrity and accountability

### 5.4 Security Clarification

Security in ESSA is **governance of system integrity, not militarisation**.

The EU-SECURITY (MCSC) layer is a civil regulatory abstraction:
- It does **not** impose military command structures.
- It does **not** activate defence or intelligence mandates.
- It **does** protect the integrity of safety invariants from corruption, interference, or circumvention.

This is architecturally essential: without this explicit declaration, the word "Security" in a European institutional context tends to activate defence, intelligence, and strategic sovereignty agendas — which would subordinate the safety mission to political governance. This doctrine prevents that capture.

### 5.5 Function Reframing

This reframes the three core functions:

| Function | Traditional Model | Safety-First Model |
|----------|------------------|--------------------|
| **Safety** | Validation step at end of design | **Primary generative driver** — defines the design space |
| **Security** | Access and threat control | **Governance of safety envelope integrity** — protects S from corruption |
| **Certification** | Narrative conformance assessment | **Invariant validation** — confirms S is preserved across the lifecycle graph |

Generation becomes **safety-bounded synthesis**.
Certification becomes **S-preservation verification**.
Security becomes **S-integrity governance**.

---

## 6. Strategic Differentiation

| Optimisation Target | Conventional Systems | ESSA |
|--------------------|---------------------|------|
| Primary objective | Performance / cost / capability | **Safety envelope robustness** |
| Secondary objective | Safety (constraint or post-hoc check) | Performance inside the safety-valid design space |
| Certification model | Narrative compliance | Deterministic invariant validation |
| AI role | Unconstrained generative agent | Bounded synthesis agent within Valid(S) |

This differentiation is **philosophically distinct** and aligns with:

- European regulatory culture (precautionary and evidence-based)
- Public legitimacy (verifiable, not asserted, safety)
- Ethical projection (safety-first standards are exportable by architecture)

---

## 7. Constitutional Clause

The following clause is hereby inserted into the ESSA Constitutional Root Document (README.md §10-bis):

> **Safety SHALL be treated as the primary generative objective in all lifecycle design processes governed under ESSA.**
>
> All derived requirements, design artefacts, and operational transitions **MUST** demonstrate preservation of defined safety invariants prior to activation.
>
> Security governs the integrity of those invariants.
> Certification validates their preservation.
> No element of the lifecycle graph **SHALL** be activated if safety coverage is incomplete.

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`safety-first.yaml`](safety-first.yaml) | Machine-readable companion — ESSA-DOC-SF-001 formal model, token rules, agentic contract |
| [`README.md`](README.md) | ESSA Constitutional Root Document (§10-bis Safety-First Clause) |
| [`cctls.yaml`](cctls.yaml) | CCTLS lifecycle standard — token types and phase definitions |
| [`EU-SECURITY/README.md`](EU-SECURITY/README.md) | MCSC controls — security as integrity governance of safety envelope |
| [`CASE.md`](CASE.md) | ESSA-ESSA case study — §3-bis Safety-First Architecture |
| [`ANNEX-A-glossary.md`](ANNEX-A-glossary.md) | MTL/MTLdg/DOF normative glossary |
