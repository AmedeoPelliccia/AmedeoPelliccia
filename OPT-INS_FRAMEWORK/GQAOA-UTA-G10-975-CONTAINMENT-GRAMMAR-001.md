# GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001

**G10.975 — Containment Grammar for the QCSAA Taxonomy Range (G10.970–G10.979)**

| Metadata | Value |
|----------|-------|
| **Document ID** | GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001 |
| **Version** | 0.2.0 |
| **Status** | draft-controlled |
| **UTA Domain** | G10 — Governance / Quantum-Computing Safety, Assurance, Authority (QCSAA) |
| **UTA Range** | 900–999 (QCSAA: 970–979 controlled-prohibition entities) |
| **Doctrine** | Containment as Grammar — boundary form without personhood claim |
| **Companion (registry)** | [`GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`](GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml) |
| **Companion (BREX)** | [`GQAOA-UTA-G10-975-BREX-RULES-001.yaml`](GQAOA-UTA-G10-975-BREX-RULES-001.yaml) |
| **Evidence schema** | [`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml) |
| **Lead location** | Naples, Campania, Italy |
| **Lead jurisdiction** | Italy / European Union |
| **Last updated** | 2026-04-25 |

---

## 0. Naples-Led Jurisdictional Posture

This containment grammar is operated under **Naples-led governance** within the GQAOA / OPT-INS_FRAMEWORK programme.

| Aspect | Value |
|--------|-------|
| **Lead location** | Naples, Campania, Italy |
| **Lead jurisdiction** | Italy / European Union |
| **Regulatory posture** | Apply applicable Naples municipal, Italian national, and European Union requirements jointly. Where requirements overlap, the **stricter** safety or containment control governs. |
| **Constitutional ceiling** | This grammar may not weaken any ESSA Safety-First invariant, nor any Italian or EU safety/containment instrument that is stricter than the rules below. |

---

## 1. Purpose

G10.975 specifies the **containment grammar** for entities registered in the QCSAA range (G10.970–G10.979). It defines:

- The six-state containment lattice and its allowed transitions;
- The naming controls (permitted, descriptive, controlled-prohibition);
- The interpretive-note requirements (the *monstrum* framing);
- The quarantine exit criteria;
- The cross-link to the LC01 / KNOT uncertainty register;
- The disambiguation against AEROSPACEMODEL-ASIT-NIB-SPEC-001 (Non-Inference Boundaries);
- The signed-YAML Evidence Package format;
- The enforcement authority and acceptance criteria.

G10.975 is a **grammar**, not a policy. It governs *how* entities in the QCSAA range may be named, stated, transitioned, and recorded. Substantive policy lives in linked instruments (registry, BREX, regency authority, evidence packages).

---

## 2. Scope, Disambiguation, and NIB Boundary

**In scope:** any entity whose UTA code falls in `G10.970`–`G10.979`.

**Disambiguation against NIB (`AEROSPACEMODEL-ASIT-NIB-SPEC-001`):**

Containment and Non-Inference Boundaries (NIB) do **related but distinct** work:

| Concept | Question answered | Locus |
|---------|-------------------|-------|
| **Containment (this spec)** | *Where* may the entity run, and *under what state*? | Lifecycle / operational |
| **NIB** | *What* may the entity infer, and *across which boundary*? | Inferential / epistemic |

An entity may be `CONTAINED_ACTIVE` (containment) and still subject to NIB constraints on what it may infer. Containment and NIB compose; neither subsumes the other.

**QCSAA code mapping (informative; normative in the registry):**

| Code | Permitted descriptive name |
|------|----------------------------|
| G10.971 | Zero-Gene Generative Agents (ZGGA) |
| G10.972 | Coherence-Lattice Inference Surfaces |
| G10.973 | Topological Evidence Reasoners |
| G10.974 | Persistent-Homology Decision Aids |
| G10.975 | *(this grammar — meta-entry)* |
| G10.976 | Quantum-Augmented Adjudication Surfaces |
| G10.977 | Coherence-Window Safety Monitors |
| G10.978 | Regency Authority Specification (forward ref §7) |
| G10.979 | Federation Conformance Surfaces |

`G10.970` is reserved as the range anchor.

---

## 3. Containment Lattice (Six States)

The six-state containment lattice separates **lifecycle position** (OBSERVE_ONLY → CONTAINED_ACTIVE) from **unresolved-concern position** (QUARANTINED, REGENCY_REVIEW), plus an end state (RETIRED).

| State | Code | Kind | Meaning |
|-------|------|------|---------|
| `OBSERVE_ONLY` | OBS | lifecycle | Registered, observed; no operational coupling permitted. |
| `SANDBOXED` | SBX | lifecycle | Permitted to run inside a controlled sandbox with full provenance capture. |
| `BOUNDED_PILOT` | BPL | lifecycle | Permitted in a scoped pilot with explicit safety envelope and rollback plan. |
| `CONTAINED_ACTIVE` | ACT | lifecycle | Permitted in production-class operation under continuous containment evidence. |
| `QUARANTINED` | QRN | hold (orthogonal) | Operational use suspended pending evidence review. |
| `REGENCY_REVIEW` | RGN | hold (orthogonal) | Held for regency-body adjudication (see §7). |
| `RETIRED` | RET | end | Withdrawn from operational consideration. |

`QUARANTINED` and `REGENCY_REVIEW` are **orthogonal** holds: an entity may enter either from any lifecycle state, and exits return it to a designated lifecycle state per §5 / §7.

### 3.1 State Transition Matrix

Allowed transitions are exactly those listed below. Any other transition is prohibited.

| From → To | OBS | SBX | BPL | ACT | QRN | RGN | RET |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **OBS**   | —   | ✓   | —   | —   | ✓   | ✓   | ✓   |
| **SBX**   | ✓   | —   | ✓   | —   | ✓   | ✓   | ✓   |
| **BPL**   | ✓   | ✓   | —   | ✓   | ✓   | ✓   | ✓   |
| **ACT**   | —   | ✓   | ✓   | —   | ✓†  | ✓   | ✓   |
| **QRN**   | ✓   | ✓   | ✓   | —   | —   | ✓   | ✓   |
| **RGN**   | ✓   | ✓   | ✓   | ✓‡  | ✓   | —   | ✓   |
| **RET**   | ✓§  | —   | —   | —   | —   | ✓   | —   |

Notes:

- **†** `ACT → QRN` MAY occur **automatically** on a recognised safety signal (see §5). All other ACT downgrades require regency review.
- **‡** `RGN → ACT` is permitted only when regency adjudication explicitly authorises return to active containment with stated residual-risk acceptance.
- **§** `RET → OBS` (rehabilitation) is permitted only via prior `RET → RGN → OBS`. Direct `RET → OBS` is prohibited.

```
                ┌───────────────┐
                │  OBSERVE_ONLY │◄───────────┐
                └──────┬────────┘            │
                       │ promote             │
                       ▼                     │
                ┌───────────────┐            │
                │   SANDBOXED   │◄──┐        │
                └──────┬────────┘   │        │
                       │ promote    │ down   │
                       ▼            │ grade  │
                ┌───────────────┐   │        │
                │ BOUNDED_PILOT │───┘        │
                └──────┬────────┘            │
                       │ promote             │
                       ▼                     │
                ┌───────────────┐            │
                │CONTAINED_ACTIVE│           │
                └──────┬────────┘            │
                       │                     │
        safety-signal  │  governance-trigger │
              ▼        ▼                     │
       ┌───────────┐ ┌────────────────┐      │
       │QUARANTINED│ │REGENCY_REVIEW  │──────┤
       └─────┬─────┘ └───────┬────────┘      │
             │               │               │
             └──────► RETIRED ◄──────────────┘
```

### 3.2 Default state on registration

New QCSAA entries SHALL default to `OBSERVE_ONLY` unless the registry explicitly records a higher initial state with regency evidence.

---

## 4. Naming Controls

### 4.1 Permitted Descriptive Names

Each QCSAA entry MUST declare a single **permitted descriptive name** — a neutral functional term mapped to its UTA code in the registry. The mapping table in §2 is normative when reproduced in `GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`. "Zero-Gene Generative Agents" is the permitted descriptive name for **G10.971**.

### 4.2 Descriptive-only variants

Variant phrasings that preserve neutral functional meaning are descriptive-only. They MUST cross-reference the canonical descriptive name in the registry.

### 4.3 Interpretive Note — the *monstrum* framing

Where authored content uses boundary-form vocabulary (e.g. "monster", "monstrum", "leviathan", "chimera") in connection with a QCSAA entity, an **interpretive note** SHALL accompany the first occurrence in the document. The interpretive note MUST:

- State that the term is used in the Latin sense of *monstrum* (a sign or boundary marker), not as a moral or personhood claim;
- Identify the UTA code being described;
- Reference this grammar (`G10.975`) and the registry entry.

The interpretive-note requirement keeps boundary-form language available for legitimate descriptive use (e.g. discussing what is *outside* the containment envelope) without leaking into moral or personhood claims.

### 4.4 Prohibited Names — Controlled Prohibition

The QCSAA range maintains a list of **prohibited names** (operational synonyms that historically carry moral, personhood, or sensational connotations). These names are **reserved for controlled prohibition**: they MAY be quoted only inside an explicit prohibition context (e.g. "the term *X* is prohibited under G10.975 §4.4"). Any other appearance is a violation.

This dual function — *reserved for controlled prohibition* rather than simply forbidden — is intentional: it lets the grammar quote prohibited terms when prohibiting them, without self-violating.

### 4.5 No prohibited-name occurrence outside controlled prohibition contexts

Authored content downstream of this grammar MUST NOT contain prohibited-name occurrences outside controlled prohibition contexts. The validator (§12) enforces this rule.

---

## 5. Quarantine — Triggers, Record, and Exit Criteria

### 5.1 Triggers

`QUARANTINED` MAY be entered:

- **Automatically** on a recognised safety signal at `CONTAINED_ACTIVE` (per §3.1 note †);
- **Manually** by STK-SAFETY or STK-GOV at any lifecycle state.

### 5.2 Record fields (required)

Each quarantine event SHALL record: entity UTA code, prior state, trigger source, safety signal reference (if automatic), opening timestamp, opener (STK identity), residual-risk hypothesis, and evidence-package pointer.

### 5.3 Exit criteria

Quarantine is lifted **only** when **all** of the following hold:

1. Evidence reviewed by **STK-SAFETY** (sufficiency) and **STK-GOV** (authority);
2. Residual risk shown ≤ the LC01 `Residual_Target` declared on the matching KNOT entry (see §6);
3. Exit destination state explicitly authorised — by default `SANDBOXED`; promotion above `SANDBOXED` requires regency review;
4. Evidence Package signed and registered per §8;
5. Ledger gate satisfied per §10.

Failure of any criterion blocks exit. Direct exit to `CONTAINED_ACTIVE` is prohibited.

---

## 6. LC01 / KNOT Mapping

Every QCSAA entity in `REGENCY_REVIEW` — and every entity that has ever held `QUARANTINED` — SHALL map to a corresponding entry in the LC01 KNOT register:

```
G10.97x   ⇄   KNOT-G10.97x-<seq>
```

The KNOT entry SHALL carry a matching `Residual_Target`. Quarantine exit and regency adjudication consume the KNOT's `Residual_Target` as the threshold of §5.3 (2). This mapping welds G10.975 into the wider GQAOA uncertainty register.

---

## 7. Regency Authority

Regency-body composition, quorum, adjudication procedure, and conflict-of-interest rules are specified in **G10.978 — Regency Authority Specification** (forward reference; see §2 mapping). Until G10.978 is published, regency review SHALL be conducted by STK-GOV acting jointly with STK-SAFETY, with full evidence registration per §8.

Escalation to regency review is triggered by:

- An ACT-state safety signal that is not resolvable within the §5 quarantine path;
- A naming control violation (§4) that may have entered authored downstream content;
- An evidence package whose sufficiency is contested by STK-SAFETY or STK-GOV;
- Any controlled-prohibition violation under §4.4–§4.5.

---

## 8. Evidence Package Format

Evidence Packages SHALL be **signed YAML** documents conforming to:

[`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml)

Required content (enforced by the schema):

- `entity_uta_code` (one of G10.970–G10.979);
- `prior_state`, `target_state` (from §3);
- `transition_kind` (lifecycle, hold-entry, hold-exit, retire);
- `evidence_items[]` (each with type, reference, hash);
- `signatures[]` (STK-SAFETY, STK-GOV minimum; STK-REGENCY when applicable);
- `knot_ref` (when §6 applies);
- `lc01_residual_target` (when §6 applies);
- `interpretive_note_present` (boolean; required `true` when boundary-form vocabulary is used).

The format is signed YAML to align with the surrounding UTA practice (YAML registries + CSV ledgers) and to preserve human-readable diff against authored documents.

---

## 9. BREX Rules — Examples and Authority

The full BREX rule set is published in `GQAOA-UTA-G10-975-BREX-RULES-001.yaml`. Two exemplar rules are reproduced inline for reviewer convenience:

```yaml
# Example 1 — containment metadata required
- id: BREX-G10.975-001
  rule: "Every QCSAA registry entry SHALL declare containment_state ∈ {OBS,SBX,BPL,ACT,QRN,RGN,RET}."
  scope: GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml
  severity: error

# Example 2 — interpretive note required on monster-alias
- id: BREX-G10.975-004
  rule: >
    Any authored occurrence of a boundary-form term ("monster", "monstrum",
    "leviathan", "chimera") referencing a G10.97x entity SHALL be accompanied
    by an interpretive note per §4.3 on first occurrence in the document.
  scope: authored_content
  severity: error
```

The BREX file additionally carries rules for naming controls, state transitions, evidence sufficiency, quarantine exit, regency escalation, LC01/KNOT mapping, and ledger gates.

---

## 10. Ledger Gate

No QCSAA state transition is operationally effective until the corresponding Evidence Package has been registered against the GQAOA ledger. The ledger gate is the final acceptance criterion (§12) and is enforced by `BREX-G10.975-LEDGER`.

---

## 11. Enforcement Authority

**STK-GOV** is the enforcement authority for this grammar.

No G10.970–G10.979 entity may be treated as operational without containment evidence registered through STK-GOV. STK-GOV acts in coordination with STK-SAFETY for safety-signal adjudication and with the regency body (G10.978) for cases escalated under §7.

Within the Naples-led jurisdictional posture (§0), STK-GOV applies the stricter of municipal, Italian, and EU controls when they overlap.

---

## 12. Acceptance Criteria

A QCSAA artefact set is accepted when **all** of the following hold:

1. Every registry entry declares a permitted descriptive name and a containment state from §3.
2. Every state transition recorded in the ledger is allowed by the §3.1 matrix.
3. Every `CONTAINED_ACTIVE` entry has a current Evidence Package signed by STK-SAFETY and STK-GOV.
4. Every entity that has ever held `QUARANTINED` or `REGENCY_REVIEW` maps to a KNOT entry with a matching `Residual_Target` (§6).
5. Every Evidence Package validates against `schemas/G10.975-evidence-package.schema.yaml`.
6. **No prohibited-name occurrence appears outside a controlled prohibition context** (§4.5).
7. Every authored use of boundary-form vocabulary carries an interpretive note (§4.3).
8. The ledger gate (§10) is satisfied for every effective transition.
9. The validator `tools/validators/validate_g10_975.py` exits zero against the package.

---

*G10.975 v0.2.0 — containment grammar, Naples-led, Italian / EU jurisdictional layering, constitutionally subordinate to ESSA Safety-First invariants and to any stricter applicable instrument.*
