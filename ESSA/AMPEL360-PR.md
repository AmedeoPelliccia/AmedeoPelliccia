# AMPEL360 Profile Resolver

**AMPEL360 — Profile Resolver (DO-178C / DAL-Adaptive Governed Component Generation)**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL360-PR-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Method — Resolver Component |
| **Parent** | ESSA-DOC-AMPEL360-001 ([AMPEL360.md](AMPEL360.md)) |
| **Companion** | [`ampel360-pr.yaml`](ampel360-pr.yaml) |
| **Related** | [`AMPEL360-Q100.md`](AMPEL360-Q100.md) · [`H-PIPELINE.md`](H-PIPELINE.md) · [`SAFETY-FIRST.md`](SAFETY-FIRST.md) |
| **Domain** | Avionics / Safety-Critical Embedded Software (DAL A–E) |
| **Regulatory Authority** | EASA / DO-178C / DO-254 / DO-330 / DO-331 |
| **Last Updated** | 2026-03-01 |

---

## Core Principle

> **Detect. Derive. Govern. Generate.**
>
> The Profile Resolver does not choose a language by preference.
> It derives the only admissible option from the existing certified stack, DAL, and toolchain constraints.
> It then generates governed artefacts — skeleton + evidence hooks + traceability — never free code.

The Profile Resolver is a **component of AMPEL360**, not a standalone AI tool. It operates inside the H-pipeline and is inhibited by every H-pipeline gate invariant.

---

## 1. Scope and Safety Boundary

The Profile Resolver addresses **navigation / autopilot / flight management software** at **DAL A or B** under DO-178C.

**Safety boundary (non-negotiable):**

- The resolver **SHALL NOT** generate activable control logic (guidance laws, command signals, fault modes).
- The resolver **SHALL** generate: interfaces, contracts, skeletons, test harness, traceability tokens, and DO-178C data item templates.
- All output is **governed artefact material** — subject to human engineering review, independent verification, and authority sign-off before any activation.
- The `H_ENVELOPE` must be established and signed **before** any resolver output is produced.

---

## 2. Inputs — What the Resolver Must Receive

| Input | Description | Token |
|-------|-------------|-------|
| **Domain** | NAV / AP / FMS / FD / … | Context |
| **DAL** | A, B, C, D, or E (from approved safety assessment) | `H_HAZARD` → drives DAL |
| **Platform** | CPU, RTOS, toolchain, memory/timing constraints | `H_CONSTRAINT` |
| **Existing codebase** | Language, coding standards, qualified tools already in use | `H_CONSTRAINT` |
| **Profile** | Active AMPEL360 domain profile (e.g. `Q100`) | Profile ID |
| **H_ENVELOPE** | Active safety envelope (signed) | `H_ENVELOPE` |
| **H_REQ** | Safety requirements derived from FHA/PSSA/SSA | `H_REQ` |

If any of these inputs is missing or unsigned, the resolver **SHALL NOT** proceed (inhibited by gate invariant PR-INH-001).

---

## 3. Language Derivation Rule

The resolver **derives** the admissible language from constraints; it does not opine.

### Derivation Algorithm

```
IF  existing certified codebase/toolchain present
THEN  use existing language (no change imposed)

ELSE IF  DAL = A or B  AND  no existing stack
  IF  formal methods / SPARK Ada qualified in target toolchain
  THEN  recommend Ada/SPARK (ECSS-E-ST-40C or toolchain qualification evidence)
  ELSE  recommend C with MISRA-C subset + compiler qualification under DO-330
        (language_subset: MISRA-C:2012 mandatory rules at minimum)

ELSE IF  model-based approach available (SCADE / Simulink + TargetLink)
THEN  recommend model-based code generation under DO-331 supplement
      (tool qualification: DO-330 TQL-1 or TQL-2 per DAL)

ELSE  flag as UNRESOLVED → human decision required (H_EXCEPTION)
```

**Rule PR-LANG-01:** The resolver output SHALL include the derivation path (which rule fired and why), registered as `H_EVIDENCE` on the language selection artefact.

**Rule PR-LANG-02:** No language recommendation is final until it carries an `H_SIGNOFF` from the responsible engineer and an `H_CONSTRAINT` confirming toolchain qualification status.

---

## 4. What the Resolver Generates

The resolver produces **governed artefact material** only — not flight-ready code.

### 4.1 Component Interface and Contracts

- Input/output signal declarations with physical units, ranges, and resolution
- Pre-conditions and post-conditions (design-by-contract style)
- Invariants derived from `H_REQ`
- Stubs for integration boundaries

All registered as `H_REQ`-linked design artefacts.

### 4.2 Deterministic Skeleton

- Structural skeleton of the component (module/unit boundary, function signatures)
- No guidance law logic, no command computation, no fault management decision logic
- Placeholder bodies with `NOT_IMPLEMENTED` assertion that blocks compilation if left unfilled
- Coding-standard annotations (MISRA-C rule applicability, or Ada aspect clauses)

Skeleton is **not activable** until engineering review and `H_EVIDENCE` (unit test, static analysis, code review) are attached.

### 4.3 Test Harness

- Test framework scaffold (unit test structure)
- Boundary value cases derived from `H_REQ` ranges and `H_CONSTRAINT` limits
- Coverage measurement hooks (MC/DC instrumentation placeholders for DAL A/B)
- Test results template aligned to DO-178C Table A-7 (software testing)

### 4.4 Traceability Tokens

- Bidirectional trace links: `H_REQ ↔ design artefact ↔ code unit ↔ test case`
- Tokenised as CCTLS-compatible traceability records
- Gaps flagged as `H_EXCEPTION` until resolved

### 4.5 DO-178C Data Item Templates

Templates for the following DO-178C data items (populated with project-specific values from inputs):

| DO-178C Data Item | Table | Template Produced |
|-------------------|-------|-------------------|
| Software Development Plan (SDP) | A-1 | Structure + DAL-specific objectives checklist |
| Software Requirements Standards | A-3 | Derived from `H_REQ` and `H_CONSTRAINT` |
| Software Design Standards | A-4 | Coding standard + architecture rules |
| Software Code Standards | A-5 | Language subset rules (MISRA-C / Ada) |
| Software Verification Plan (SVP) | A-2 | Test strategy + coverage objectives |
| Traceability data | A-5 | `H_REQ → design → code → test` matrix |

---

## 5. H-Pipeline Inhibitors

The resolver enforces four constitutional inhibitors. If any condition is not met, the corresponding operation is **blocked by construction**.

| ID | Inhibitor | Condition | Blocked Operation |
|----|-----------|-----------|-------------------|
| **PR-INH-001** | `¬H_ENVELOPE` → BLOCKED | No signed H_ENVELOPE present | All resolver output generation |
| **PR-INH-002** | `¬TRACE(H_REQ → H_ENVELOPE)` → BLOCKED | H_REQ not traceable to active H_ENVELOPE | CONFIRM gate (phase advance) |
| **PR-INH-003** | `¬H_EVIDENCE(safety_critical)` → BLOCKED | No verified evidence on safety-critical artefact | ACTIVATE gate (artefact activation) |
| **PR-INH-004** | `¬H_SIGNOFF(authority)` → BLOCKED | No authority sign-off (responsible engineer + DOA) | PUBLISH gate (release to operations) |

**Rule PR-INH-005 (generation inhibitor):** If the requested generation scope falls outside the boundary defined in §1 (i.e. the resolver is asked to generate control logic), the request **SHALL** be rejected and logged as `H_EXCEPTION` with mandatory human escalation.

---

## 6. Gate Alignment (DO-178C × CCTLS)

| CCTLS Gate | DO-178C Equivalent | Active H-tokens | Resolver Output Produced |
|------------|-------------------|-----------------|--------------------------|
| **INTERPRET** | Planning phase (SDP/SVP approved) | `H_ENVELOPE`, `H_REQ`, `H_CONSTRAINT` | Language derivation, interface contracts |
| **CONFIRM** | Requirements review complete | `H_REQ`, `H_HAZARD` | Skeleton, test harness, traceability tokens |
| **ACTIVATE** | Verification objective met | `H_EVIDENCE`, `H_EXCEPTION` cleared | DO-178C data item templates finalised |
| **PUBLISH** | SOI review passed | `H_SIGNOFF` | Compliance bundle released |

**Gate rule:** The resolver output at each gate is conditioned on all prior gates being in PASS state. A BLOCKED gate propagates forward — no downstream output is produced.

---

## 7. What the Profile Resolver Is Not

| Not | Is |
|-----|-----|
| An AI autopilot code generator | A governed skeleton + evidence + traceability generator |
| A substitute for qualified toolchain | A lifecycle method operating over qualified tools |
| A certification tool | A method producing ALPC-ready compliance bundles for DO-178C SOI review |
| An autonomous system | A human-authority-confirmed generator — every output requires engineering review and sign-off |
| A PLM or ALM system | The lifecycle governance layer that integrates into PLM/ALM at phase gates |

---

## 8. Formal Definition

Let:
- `D` = DAL level (A–E)
- `S` = existing certified stack (language, toolchain, RTOS)
- `H` = active H_ENVELOPE (safety envelope)
- `R` = set of `H_REQ` traceable to `H`
- `P` = active AMPEL360 domain profile

The Profile Resolver function:

```
PR(D, S, H, R, P) = {
  PRECONDITION:
    H ≠ ∅  ∧  Signed(H)                    -- envelope exists and is signed
    ∧ ∀ rᵢ ∈ R: Traceable(rᵢ, H)          -- all requirements trace to envelope

  DERIVE:
    lang = LanguageDerivation(D, S)          -- rule PR-LANG-01 applied

  GENERATE:
    { Interfaces(R),                         -- contracts and stubs
      Skeleton(lang, R),                     -- deterministic skeleton only
      TestHarness(D, R),                     -- MC/DC-ready for DAL A/B
      TraceTokens(R, Skeleton),              -- bidirectional traceability
      DO178C_Templates(D, P) }               -- data item templates

  POSTCONDITION:
    ∀ output ∈ GENERATE: ¬Activable          -- no output is activable
    ∀ output ∈ GENERATE: RequiresReview      -- engineering review mandatory
    ∀ output ∈ GENERATE: RequiresSignoff(H_SIGNOFF)  -- authority sign-off mandatory

  BLOCKED if any PRECONDITION false           -- inhibitors PR-INH-001–005
}
```

---

## 9. Relationship to Constitutional Instruments

| Instrument | Profile Resolver Role |
|------------|----------------------|
| **ESSA-CONST-001** | Resolver satisfies CI-003 (Deterministic Gates), CI-004 (Machine-Verifiable Conformance) |
| **ESSA-DOC-AMPEL360-001** | Resolver is a functional sub-component of AMPEL360 |
| **ESSA-DOC-AMPEL360-Q100-001** | Q100 profile activates the resolver for EASA/DO-178C context |
| **ESSA-DOC-H-001** | Resolver operates inside the H-pipeline; every output is H-token-linked |
| **ESSA-DOC-SF-001** | Safety-first: resolver generation is H_ENVELOPE-gated (SF-RULE-01) |
| **ESSA-STD-CCTLS-001** | Resolver output maps to CCTLS phase gates INTERPRET → CONFIRM → ACTIVATE → PUBLISH |
