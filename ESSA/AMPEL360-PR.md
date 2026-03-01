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

## 5. DO-178C Validation Rules

The resolver enforces validation rules before confirming or activating any generated artefact. These rules are **mandatory** for DAL A/B and strongly recommended for DAL C/D. Each failing rule produces an `H_EXCEPTION` record that blocks the corresponding gate.

### 5.1 Code Complexity Rules

| Rule ID | Check | Threshold | DAL Scope | Blocked Gate |
|---------|-------|-----------|-----------|--------------|
| **PR-VAL-CC-01** | Cyclomatic complexity per function | ≤ 10 (DAL A/B), ≤ 15 (DAL C) | A, B, C | CONFIRM |
| **PR-VAL-CC-02** | Call-stack depth (no dynamic recursion) | Static bound derivable; recursion = `H_EXCEPTION` | A, B | CONFIRM |
| **PR-VAL-CC-03** | Function length | ≤ 60 lines of effective code (project standard may tighten) | A, B, C | CONFIRM |
| **PR-VAL-CC-04** | Number of parameters per function | ≤ 8 (MISRA-C:2012 Dir 4.6 guidance) | A, B, C | CONFIRM |
| **PR-VAL-CC-05** | Dynamic memory allocation | Forbidden in generated skeleton for DAL A/B (MISRA-C:2012 Rule 21.3) | A, B | CONFIRM |

**Rule PR-VAL-CC-01 rationale:** High cyclomatic complexity makes MC/DC coverage structurally expensive and error-prone; bounding it at skeleton generation enforces good design before code exists.

**Verification artefact:** static analysis report (e.g. LDRA, Polyspace, CodeSonar) with per-function complexity table, registered as `H_EVIDENCE` at the CONFIRM gate.

### 5.2 Required Artefact Presence Rules

The following artefacts **SHALL** be present and linked as `H_EVIDENCE` before the resolver advances any gate:

| Rule ID | Required Artefact | DO-178C Table | Applicable Gate | DAL Scope |
|---------|-------------------|---------------|-----------------|-----------|
| **PR-VAL-ART-01** | System Safety Analysis Report (SAR / FHA / PSSA / SSA output) | System-level input | INTERPRET | A, B, C, D |
| **PR-VAL-ART-02** | Software Development Plan (SDP) — approved | A-1 | INTERPRET → CONFIRM | A, B, C, D |
| **PR-VAL-ART-03** | Software Verification Plan (SVP) — approved | A-2 | INTERPRET → CONFIRM | A, B, C |
| **PR-VAL-ART-04** | Software Requirements Standards — issued | A-3 | CONFIRM | A, B, C |
| **PR-VAL-ART-05** | Software Design Standards — issued | A-4 | CONFIRM | A, B, C |
| **PR-VAL-ART-06** | Software Code Standards (including language-subset rules) — issued | A-5 | CONFIRM | A, B, C |
| **PR-VAL-ART-07** | Tool Qualification Plan (TQP) for all DO-330 tools | DO-330 Table A-1 | CONFIRM | A, B |
| **PR-VAL-ART-08** | Static Analysis Report (complexity + MISRA scan) per unit | A-7 | ACTIVATE | A, B, C |
| **PR-VAL-ART-09** | Unit Test Results with MC/DC coverage table | A-7 | ACTIVATE | A, B |
| **PR-VAL-ART-10** | Software Conformity Review (SCR) record | A-8 | PUBLISH | A, B, C |

**Rule PR-VAL-ART-01 — Safety Analysis Report:** The resolver **SHALL** verify that a signed Safety Analysis Report (`H_EVIDENCE` of type `safety_analysis_report`) is present and its DAL derivation matches the `D` input. If the SAR is absent or its DAL derivation does not match, the INTERPRET gate is **BLOCKED**.

**Rule PR-VAL-ART-07 — Tool Qualification:** For DAL A/B, all tools in the build chain that produce output not independently verified **SHALL** have a DO-330 Tool Qualification Plan registered as `H_EVIDENCE`. Missing TQP blocks the CONFIRM gate.

### 5.3 MISRA-C Compliance Validation Rules

Applicable when language derivation selects C (rule PR-LANG-01, branch MISRA-C). The resolver generates a **MISRA-C compliance manifest** alongside every skeleton.

#### 5.3.1 Mandatory Rules (DAL A/B — non-deviatable)

| Rule ID | MISRA-C:2012 Rule | Description | Resolver Action |
|---------|-------------------|-------------|-----------------|
| **PR-VAL-MC-01** | Rule 1.1 | Code shall conform to the selected C standard | Annotate skeleton header with `/* C99/C11 conformance required */` |
| **PR-VAL-MC-02** | Rule 2.2 | No dead code | Skeleton stubs flagged with NOT_IMPLEMENTED assertion — dead-code scanner must confirm zero dead paths post-fill |
| **PR-VAL-MC-03** | Rule 8.4 | Compatible declarations for external objects/functions | All external interfaces declared in generated header |
| **PR-VAL-MC-04** | Rule 11.3 | No cast between pointer-to-object and integer type | Skeleton type definitions use explicit sized types (`uint32_t`, etc.) |
| **PR-VAL-MC-05** | Rule 14.3 | Controlling expressions shall not be invariant | Placeholder conditionals must be replaced before CONFIRM |
| **PR-VAL-MC-06** | Rule 15.5 | Function returns a value at a single exit point | Skeleton functions generated with single exit point structure |
| **PR-VAL-MC-07** | Rule 17.2 | Recursion forbidden | Resolver rejects recursive call graphs; flags as `H_EXCEPTION` |
| **PR-VAL-MC-08** | Rule 21.3 | `malloc`/`free` forbidden | Skeleton contains no dynamic allocation; use of stdlib allocator triggers `H_EXCEPTION` |

#### 5.3.2 Required Directives (DAL A/B/C)

| Rule ID | MISRA-C:2012 Directive | Description | Resolver Action |
|---------|------------------------|-------------|-----------------|
| **PR-VAL-MD-01** | Dir 1.1 | All code shall be implemented in C (conforming to C99 or C11 with project-defined subset) | Language standard set in generated `coding_standards.h` guard |
| **PR-VAL-MD-02** | Dir 4.1 | Arithmetic shall not rely on implementation-defined behaviour | Fixed-width types enforced in skeleton signals |
| **PR-VAL-MD-03** | Dir 4.6 | All numerical values shall have explicit types | Signal declarations use typed constants only |
| **PR-VAL-MD-04** | Dir 4.7 | Return value of non-void functions shall be tested | Every call site in test harness checks return value |

#### 5.3.3 Compliance Manifest

The resolver produces a **MISRA-C Compliance Manifest** registered as `H_EVIDENCE` on the skeleton artefact. The manifest contains:

- Confirmation of mandatory/required rules applied at generation time
- List of any deviations requested (each deviation requires a **Deviation Record** with rationale, signed by responsible engineer = `H_SIGNOFF`)
- Placeholders for static analysis tool results (to be populated at CONFIRM gate)
- Reference to the Software Code Standards artefact (PR-VAL-ART-06)

**Rule PR-VAL-MC-DEVIATE:** No deviation from a MISRA-C mandatory rule is permitted for DAL A/B without a Deviation Record carrying `H_SIGNOFF`. Unsigned deviation requests block the CONFIRM gate (inhibitor PR-INH-002 applies).

---

## 6. H-Pipeline Inhibitors

The resolver enforces four constitutional inhibitors. If any condition is not met, the corresponding operation is **blocked by construction**.

| ID | Inhibitor | Condition | Blocked Operation |
|----|-----------|-----------|-------------------|
| **PR-INH-001** | `¬H_ENVELOPE` → BLOCKED | No signed H_ENVELOPE present | All resolver output generation |
| **PR-INH-002** | `¬TRACE(H_REQ → H_ENVELOPE)` → BLOCKED | H_REQ not traceable to active H_ENVELOPE | CONFIRM gate (phase advance) |
| **PR-INH-003** | `¬H_EVIDENCE(safety_critical)` → BLOCKED | No verified evidence on safety-critical artefact | ACTIVATE gate (artefact activation) |
| **PR-INH-004** | `¬H_SIGNOFF(authority)` → BLOCKED | No authority sign-off (responsible engineer + DOA) | PUBLISH gate (release to operations) |

**Rule PR-INH-005 (generation inhibitor):** If the requested generation scope falls outside the boundary defined in §1 (i.e. the resolver is asked to generate control logic), the request **SHALL** be rejected and logged as `H_EXCEPTION` with mandatory human escalation.

---

## 7. Gate Alignment (DO-178C × CCTLS)

| CCTLS Gate | DO-178C Equivalent | Active H-tokens | Resolver Output Produced |
|------------|-------------------|-----------------|--------------------------|
| **INTERPRET** | Planning phase (SDP/SVP approved) | `H_ENVELOPE`, `H_REQ`, `H_CONSTRAINT` | Language derivation, interface contracts |
| **CONFIRM** | Requirements review complete | `H_REQ`, `H_HAZARD` | Skeleton, test harness, traceability tokens |
| **ACTIVATE** | Verification objective met | `H_EVIDENCE`, `H_EXCEPTION` cleared | DO-178C data item templates finalised |
| **PUBLISH** | SOI review passed | `H_SIGNOFF` | Compliance bundle released |

**Gate rule:** The resolver output at each gate is conditioned on all prior gates being in PASS state. A BLOCKED gate propagates forward — no downstream output is produced.

---

## 8. What the Profile Resolver Is Not

| Not | Is |
|-----|-----|
| An AI autopilot code generator | A governed skeleton + evidence + traceability generator |
| A substitute for qualified toolchain | A lifecycle method operating over qualified tools |
| A certification tool | A method producing ALPC-ready compliance bundles for DO-178C SOI review |
| An autonomous system | A human-authority-confirmed generator — every output requires engineering review and sign-off |
| A PLM or ALM system | The lifecycle governance layer that integrates into PLM/ALM at phase gates |

---

## 9. Formal Definition

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

## 10. Relationship to Constitutional Instruments

| Instrument | Profile Resolver Role |
|------------|----------------------|
| **ESSA-CONST-001** | Resolver satisfies CI-003 (Deterministic Gates), CI-004 (Machine-Verifiable Conformance) |
| **ESSA-DOC-AMPEL360-001** | Resolver is a functional sub-component of AMPEL360 |
| **ESSA-DOC-AMPEL360-Q100-001** | Q100 profile activates the resolver for EASA/DO-178C context |
| **ESSA-DOC-H-001** | Resolver operates inside the H-pipeline; every output is H-token-linked |
| **ESSA-DOC-SF-001** | Safety-first: resolver generation is H_ENVELOPE-gated (SF-RULE-01) |
| **ESSA-STD-CCTLS-001** | Resolver output maps to CCTLS phase gates INTERPRET → CONFIRM → ACTIVATE → PUBLISH |
