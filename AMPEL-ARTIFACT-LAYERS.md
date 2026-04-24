---
schema_version: "1.0.0"
document_type: framework-reference
document_id: AMPEL-ART-LAY-001
status: consolidated baseline
last_updated: "2026-04-24"
scope: distinguishes the four parallel baseline artifact classes used across AMPEL programmes
companion_docs:
  - AMPEL-FAMILY-TAXONOMY.md
  - GLOSSARY_FOUNDATIONAL.md
  - ESSA/AMPEL360-ARCH-SPEC.md
---

# AMPEL — Parallel Baseline Artifact Layers

**Status:** consolidated baseline · **Date:** 2026-04-24

This document distinguishes the four artifact classes that run as **parallel baselines**
across AMPEL programmes. They are *not* alternatives — each answers a different
question and each is owned by a different authority. A given product (e.g.
`AMPEL360-Q100`) is described simultaneously by **all four**.

> The product-line taxonomy itself (Models) is already normalised in
> [`AMPEL-FAMILY-TAXONOMY.md`](./AMPEL-FAMILY-TAXONOMY.md). This document
> positions the other three layers around it.

---

## 1. The Four Layers at a Glance

| Layer | Full name | Answers the question | Owner | Primary baseline |
|---|---|---|---|---|
| **Models** | Product-line repositories | *What are we building?* | Chief Engineer (per repo) | Product / configuration |
| **CSP** | **Certifiable Strategies and Programmes** | *How do we get it certified and into service?* | Programme Director / Certification Authority interface | Certification & programme |
| **OTAPC** | **Overlap-Top Architectures Project Charters** | *Which cross-cutting architectures span multiple models, and who governs the overlap?* | Principal Architect (cross-product) | Architecture-overlap charter |
| **FIDITA** | **Full Identical Digital Implementation of Twin Architecture** | *Which fully-identical digital-twin implementation realises a frozen baseline at a given epoch?* | Industrialisation lead + Digital Twin lead | Configuration-of-record snapshot |

The four layers run **in parallel**: a change can land in any one without
forcing the others to re-baseline, but each layer publishes traceability
links to the others.

---

## 2. Models — product-line baselines *(already documented)*

- **Definition.** A *Model* is a top-level repository scoping one engineering
  domain and the products inside it.
- **Examples.** `AIRCRAFTMODEL` (aerial), `AEROSPACEMODEL` (spatial).
- **Contains.** Products (`AMPEL360-Q100`, `AMPEL360-Q10`, `GAIA`,
  `ROBBBO-T`), each with its own configurations (e.g. `WTW`, `BWB`) and a
  shared `OPT-IN` / `OPT-INS` framework instance.
- **Baseline cadence.** Tracks the engineering definition; changes when the
  product definition changes (geometry, ATA chapters, framework axes).
- **Canonical reference.** [`AMPEL-FAMILY-TAXONOMY.md`](./AMPEL-FAMILY-TAXONOMY.md).

> Models say **what** exists. They do not, by themselves, declare a
> certification path, an overlap with sibling architectures, or a frozen
> physical article.

---

## 3. CSP — Certifiable Strategies and Programmes

- **Definition.** A **CSP** is a programme-level baseline that binds a Model
  (or one of its configurations) to:
  1. a **regulatory anchor** (e.g. EASA CS-25, FAA AST 14 CFR Part 460,
     ECSS-E/Q/M, NASA-STD-3001),
  2. a **certification strategy** (means of compliance, credit plan,
     test/analysis split, alternative means),
  3. a **programme plan** (gates, milestones, decision authorities, funding
     envelope).
- **Why it is parallel to Models.** Two CSPs can target the *same* Model
  configuration under different authorities (e.g. EASA vs. FAA) or different
  service entries (passenger vs. cargo). Conversely, one CSP can apply
  consistently across two configurations of the same Model when the means of
  compliance is shared.
- **Owned by.** Programme Director, in liaison with the Certification
  Authority focal point. Engineering provides evidence; CSP owns the
  argument.
- **Lifecycle.** Reviewed at every certification gate (PDR, CDR, TRR, TC,
  EIS). Revisions issued when regulation, scope, or means of compliance
  change.
- **Typical artifacts.** Certification Plan, Compliance Checklist,
  Means-of-Compliance Matrix, Issue Papers, Type Certification Data Sheet
  (TCDS) draft, programme master schedule.
- **Relationship to other layers.**
  - Cites a **Model** configuration as the subject.
  - Consumes **OTAPC** clauses where cross-cutting architectures introduce
    novelty requiring special-condition negotiation.
  - Locks **FIDITA** snapshots as the configuration-of-record at each gate.

---

## 4. OTAPC — Overlap-Top Architectures Project Charters

- **Definition.** An **OTAPC** is a charter for an architecture pattern that
  *overlaps the top* of two or more Models (or two or more configurations
  inside one Model). It governs the *overlap surface* itself, not either
  endpoint.
- **Examples of overlap surfaces.**
  - Quantum/classical compute fabric shared by `AMPEL360-Q100` and
    `AMPEL360-Q10` (the `ACQUA` continuum).
  - `OPT-IN` ↔ `OPT-INS` framework bridge (aerial ↔ spatial).
  - Common ECLSS heritage between `AMPEL360-Q10` and `GAIA`.
  - Cross-configuration commonality between `WTW` and `BWB` (shared avionics
    spine, divergent pressure vessels).
- **Why it is parallel to Models.** A Model owns a single product line;
  an OTAPC owns an *intersection* that no single Model can authoritatively
  ratify. Without OTAPCs, overlap decisions get re-litigated inside each
  Model.
- **Owned by.** Principal Architect with co-signature from each affected
  Model's Chief Engineer.
- **Lifecycle.** Issued at architecture-overlap discovery; revised when the
  set of participating Models, configurations, or shared interfaces changes.
- **Typical artifacts.** Charter (scope, parties, decision rights), shared
  interface control document (ICD), commonality matrix, divergence register,
  arbitration log.
- **Relationship to other layers.**
  - Names the **Models** and **configurations** it overlaps.
  - Feeds **CSPs** with the special-conditions content for cross-cutting
    novelty (e.g. quantum-assisted means of compliance).
  - Anchors the cross-Model invariants that **FIDITA** snapshots must
    preserve.

---

## 5. FIDITA — Full Identical Digital Implementation of Twin Architecture

- **Definition.** A **FIDITA** is a *frozen, byte-identical digital
  implementation of a Model configuration's full twin architecture* —
  design definition + industrialisation package + the running digital-twin
  implementation that mirrors the as-built / as-flown article — captured
  at a specific programme epoch.
- **Why "identical".** A FIDITA **SHALL** be bit-for-bit reproducible from
  the artifacts it cites: re-running the build from the cited Model commit,
  industrialisation package, and twin manifest reproduces an identical
  digital implementation. This reproducibility is what makes a FIDITA
  admissible as configuration-of-record.
- **Why it is parallel to Models.** A Model evolves continuously; a FIDITA
  is immutable once issued. Multiple FIDITAs can co-exist for the same
  Model configuration — for example the implementation snapshot used for
  static-test correlation, the one used for fatigue correlation, the one
  flown for certification credit, and the one mirrored in operations —
  each frozen at a different epoch.
- **Owned by.** Industrialisation lead and Digital Twin lead jointly,
  with sign-off from Chief Engineer (design integrity), Quality
  (conformance), and Test (utilisation plan).
- **Lifecycle.** Created → frozen → utilised → archived. Never edited
  in place; superseded by a new FIDITA with explicit `supersedes:`
  traceability.
- **Typical artifacts.** As-designed configuration list, as-built
  configuration list, deviation log, twin manifest (image digests,
  simulator versions, dataset hashes), qualification test plan and report
  bundle, article serial register.
- **Taxonomy anchor.** G4 (DTCEC — Digital Twin, Cloud &amp; Edge Computing)
  in the UTA taxonomy.
- **Relationship to other layers.**
  - Snapshots the **Model** configuration at its freeze epoch.
  - Provides the conformance evidence the **CSP** consumes at gates.
  - Carries a manifest of **OTAPC**-mandated invariants present in the
    twin implementation.

---

## 6. Side-by-Side Comparison

| Dimension | **Model** | **CSP** | **OTAPC** | **FIDITA** |
|---|---|---|---|---|
| Question answered | What | How (certify & deliver) | Where models overlap | What was frozen, when |
| Scope | One product line | One programme × one authority | An intersection of ≥2 lines/configs | One epoch of one configuration |
| Mutability | Evolving | Revised per gate | Revised per overlap change | **Immutable once frozen** |
| Owner | Chief Engineer | Programme Director | Principal Architect | Industrialisation Lead |
| Primary anchor | Engineering definition | Regulation + plan | Cross-cutting architecture | Configuration-of-record |
| Cardinality vs. product | 1 : 1 with a product line | n : 1 (per authority/scope) | m : n across products | n : 1 (per freeze epoch) |
| Reviewed at | Design reviews | Certification gates | Architecture board | Freeze events only |
| Repository surface | Top-level repo (`AIRCRAFTMODEL`, …) | `00-PROGRAM/…/CSP/` | `00-PROGRAM/…/OTAPC/` | `00-PROGRAM/…/FIDITA/` |

---

## 7. Worked Example — `AMPEL360-Q100`

| Layer | Instance for `AMPEL360-Q100` |
|---|---|
| **Model** | `AIRCRAFTMODEL/AMPEL360-Q100/` with configurations `WTW` and `BWB` |
| **CSP** | e.g. `CSP-Q100-EASA-CS25` (EASA pax) and `CSP-Q100-FAA-Part25` (FAA pax) — same Model, two parallel certification programmes |
| **OTAPC** | e.g. `OTAPC-OPT-IN×OPT-INS-COMPUTE` (shared quantum/classical compute spine with `AMPEL360-Q10`); `OTAPC-Q100-WTW×BWB-AVIONICS` (commonality charter between the two configurations) |
| **FIDITA** | e.g. `FIDITA-Q100-WTW-STATIC-2027Q3`, `FIDITA-Q100-WTW-FATIGUE-2028Q1`, `FIDITA-Q100-BWB-IRON-BIRD-2028Q4` |

A change request walks every layer: which Models it touches, which CSPs need
re-argumentation, which OTAPCs it perturbs, and which (if any) FIDITAs it
invalidates.

---

## 8. Authoring Rules

1. **Never collapse layers.** Do not put certification arguments into Model
   READMEs, or overlap charters into CSPs. Cross-link instead.
2. **Every artifact declares its layer** in its front-matter
   (`document_type: model | csp | otapc | fidita`).
3. **Identifiers are namespaced** — `Q100-…`, `OTAPC-…`, `CSP-…`, `FIDITA-…`
   — and never reused across layers.
4. **FIDITA is append-only.** Corrections are issued as a new FIDITA with a
   `supersedes:` field; the original is retained.
5. **OTAPCs require multilateral sign-off** by every Model they touch.
   A unilateral OTAPC is a Model-internal architecture note, not an OTAPC.

---

## 9. Differentiation vs. Competitor "Concept Baseline + Evidence Plan" Duality

Most competing programmes — incumbent OEMs running clean-sheet concepts and
the wave of well-funded entrants chasing hydrogen, BWB, or quantum-assisted
aerospace — organise their work around **two axes only**:

- a **Concept Baseline** (a frozen point design with a configuration-of-record), and
- an **Evidence Plan** (a cert/test/credit roadmap pointing at that baseline).

This duality is structurally weak in five specific places. The
Models / CSP / OTAPC / FIDITA decomposition is engineered to fix each one.
This section names the failure modes and the corresponding AMPEL invariants
so the difference is auditable, not rhetorical.

### 9.1 Failure modes of the two-axis approach

| # | Competitor failure mode | What actually goes wrong |
|---|---|---|
| F1 | **Single-authority lock-in** | One Concept Baseline ⇒ one cert path. Adding a second authority (FAA after EASA, or military after civil) forces a re-baseline, dragging unrelated engineering with it. |
| F2 | **Overlap is everyone's and no one's** | Cross-product commonality (shared compute, shared ECLSS, shared cabin) is owned by neither product team; conflicts are escalated ad hoc or frozen by default into divergence. |
| F3 | **Evidence drifts from article** | The Evidence Plan cites "the baseline"; meanwhile three different test articles diverge from each other and from the design intent. Drift is discovered at qualification, not before. |
| F4 | **Configuration immutability is faked** | "Frozen" baselines are edited in place under change-control bureaucracy; lineage is reconstructed from PLM diffs rather than asserted by the artifact. |
| F5 | **Concept-novelty tax is invisible** | Quantum, hybrid-electric, BWB pressure-vessel, BLI — each demands special conditions. The Evidence Plan absorbs them silently, so the *novelty surface* itself is never a reviewable artifact. |

### 9.2 How AMPEL closes each gap

| # | AMPEL invariant | Mechanism | Where enforced |
|---|---|---|---|
| F1 | **n CSPs per Model are first-class.** | CSP cardinality is `n : 1` (per authority/scope). EASA and FAA programmes can run *concurrently* against an unchanged Model. | §1 cardinality row; §3 |
| F2 | **Overlap has its own owner and its own charter.** | OTAPCs are multilateral, co-signed by every affected Chief Engineer; a unilateral overlap document is explicitly *not* an OTAPC. | §4; Authoring Rule 5 |
| F3 | **Articles are typed, plural, and snapshot-bound.** | Multiple FIDITAs co-exist for the same configuration (static, fatigue, iron-bird, flight-test); each carries as-designed + as-built lists and a deviation log. | §5; §7 worked example |
| F4 | **Immutability is asserted by the artifact, not by process.** | FIDITA is append-only; corrections are *new* FIDITAs with an explicit `supersedes:` link. Lineage is queryable, not reconstructed. | §5; Authoring Rule 4 |
| F5 | **Novelty surface is a named OTAPC.** | Every cross-cutting novelty (e.g. `OTAPC-OPT-IN×OPT-INS-COMPUTE`) is a charter that CSPs *cite* when arguing special conditions, making the novelty tax visible and reviewable. | §4; §7 |

### 9.3 The differentiation, stated as a contract

A competitor's two-axis stack answers:
> *"Here is the design. Here is how we will prove it."*

The AMPEL four-layer stack answers four orthogonal questions and refuses to
let any single artifact answer more than one:

> *"Here is the **product line** (Model). Here are the **certification
> programmes** running against it, possibly in parallel under different
> authorities (CSPs). Here are the **architecture overlaps** with our other
> product lines, governed multilaterally (OTAPCs). Here are the **frozen,
> byte-identical digital-twin implementations** that realise it at named
> epochs (FIDITAs)."*

That orthogonality is the moat. It is what lets a single change request be
walked across all four layers deterministically (§7), instead of being
absorbed into a monolithic baseline whose semantics quietly drift.

### 9.4 Concept Baseline → AMPEL mapping (for reviewers from competitor stacks)

Reviewers familiar only with the two-axis vocabulary should read the mapping
both ways:

| Competitor concept | AMPEL equivalent | Note |
|---|---|---|
| Concept Baseline (point design) | **Model** + the latest **FIDITA** for the configuration in question | A Model is *evolving*; the FIDITA is the frozen, byte-identical digital-twin snapshot the competitor would call "the baseline". |
| Configuration-of-record | **FIDITA** | Append-only, with explicit `supersedes:` lineage. |
| Evidence Plan | **CSP** (one of possibly several) | One CSP per authority/scope; not a single document. |
| Cross-product commonality memo | **OTAPC** | Must be multilateral; otherwise it is a Model-internal note. |
| Special-conditions package | Clauses inside a **CSP** sourced from one or more **OTAPCs** | The novelty surface is itself a reviewable charter. |

### 9.5 Evidence that this distinction holds — verification per layer

The four-layer split is only meaningful if each layer can be independently
verified. The verification programme below is the public commitment behind
the differentiation; CSPs are the place where each row is operationalised
into auditable evidence.

| Layer | Verification artifact | Independent test of the differentiation |
|---|---|---|
| **Model** | Taxonomy conformance check against `AMPEL-FAMILY-TAXONOMY.md` | A Model that mutates without a corresponding CSP/OTAPC/FIDITA touch is flagged: differentiation requires that engineering edits do not silently consume certification or overlap budget. |
| **CSP** | Means-of-Compliance Matrix + gate minutes from the Certification Authority | Two CSPs against the same Model must reach gates *independently*; if one drags the other, the n:1 invariant has failed. |
| **OTAPC** | Multilateral sign-off log + divergence register | An OTAPC with a single signatory is rejected by definition; an unsigned overlap surfacing in a CSP is a finding. |
| **FIDITA** | As-designed vs. as-built reconciliation + `supersedes:` chain | Any in-place edit to a published FIDITA is a process failure; the chain must be reconstructable from the artifacts alone, with no reliance on PLM history. |

Together these checks make the differentiation **falsifiable**: each row is
something a competitor running a Concept-Baseline + Evidence-Plan stack
provably cannot demonstrate, because their architecture does not name the
required artifact in the first place.
