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
| **FIDITA** *(historical)* | **Fully-Integrated Design / Industrialisation / Test Articles** | *Which physical/virtual articles realise a frozen baseline at a given epoch?* | Industrialisation lead | Configuration-of-record snapshot |

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

## 5. FIDITA — *(historical)* Fully-Integrated Design / Industrialisation / Test Articles

- **Definition.** A **FIDITA** is a *frozen, fully-integrated baseline
  snapshot* — design definition + industrialisation package + the physical
  or virtual test article that realises it — taken at a specific programme
  epoch.
- **Historical note.** The FIDITA construct predates the current Model /
  CSP / OTAPC split. It is retained because legacy programme records,
  qualification dossiers, and supplier data packages reference FIDITA
  identifiers, and traceability to those records is non-negotiable. New
  programmes use Models + CSP + OTAPC primarily and emit FIDITA snapshots
  only at major freeze points.
- **Why it is parallel to Models.** A Model evolves continuously; a FIDITA
  is immutable once issued. Multiple FIDITAs can co-exist for the same
  Model configuration — for example, the article used for static test, the
  article used for fatigue test, and the article flown for certification
  credit — each frozen at a different epoch.
- **Owned by.** Industrialisation lead, with sign-off from Chief Engineer
  (design integrity), Quality (conformance), and Test (utilisation plan).
- **Lifecycle.** Created → frozen → utilised → archived. Never edited
  in place; superseded by a new FIDITA with explicit traceability.
- **Typical artifacts.** As-designed configuration list, as-built
  configuration list, deviation log, qualification test plan and report
  bundle, article serial register.
- **Relationship to other layers.**
  - Snapshots the **Model** configuration at its freeze epoch.
  - Provides the conformance evidence the **CSP** consumes at gates.
  - Carries a manifest of **OTAPC**-mandated invariants present in the
    article.

---

## 6. Side-by-Side Comparison

| Dimension | **Model** | **CSP** | **OTAPC** | **FIDITA** *(hist.)* |
|---|---|---|---|---|
| Question answered | What | How (certify & deliver) | Where models overlap | What was frozen, when |
| Scope | One product line | One programme × one authority | An intersection of ≥2 lines/configs | One epoch of one configuration |
| Mutability | Evolving | Revised per gate | Revised per overlap change | **Immutable once frozen** |
| Owner | Chief Engineer | Programme Director | Principal Architect | Industrialisation Lead |
| Primary anchor | Engineering definition | Regulation + plan | Cross-cutting architecture | Configuration-of-record |
| Cardinality vs. product | 1 : 1 with a product line | n : 1 (per authority/scope) | m : n across products | n : 1 (per freeze epoch) |
| Reviewed at | Design reviews | Certification gates | Architecture board | Freeze events only |
| Repository surface | Top-level repo (`AIRCRAFTMODEL`, …) | `00-PROGRAM/…/CSP/` | `00-PROGRAM/…/OTAPC/` | `00-PROGRAM/…/FIDITA/` *(legacy)* |

---

## 7. Worked Example — `AMPEL360-Q100`

| Layer | Instance for `AMPEL360-Q100` |
|---|---|
| **Model** | `AIRCRAFTMODEL/AMPEL360-Q100/` with configurations `WTW` and `BWB` |
| **CSP** | e.g. `CSP-Q100-EASA-CS25` (EASA pax) and `CSP-Q100-FAA-Part25` (FAA pax) — same Model, two parallel certification programmes |
| **OTAPC** | e.g. `OTAPC-OPT-IN×OPT-INS-COMPUTE` (shared quantum/classical compute spine with `AMPEL360-Q10`); `OTAPC-Q100-WTW×BWB-AVIONICS` (commonality charter between the two configurations) |
| **FIDITA** *(hist.)* | e.g. `FIDITA-Q100-WTW-STATIC-2027Q3`, `FIDITA-Q100-WTW-FATIGUE-2028Q1`, `FIDITA-Q100-BWB-IRON-BIRD-2028Q4` |

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
