# ESSA — TD-ISA: Technical Data Integrity, Standardization, and Automation

**A Proposed Entity for Common Technical Data Governance**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-TDISA-001 |
| **Version** | v0.2-draft |
| **Status** | Entity Proposal |
| **Parent** | ESSA-CONST-001 ([ESSA-AGENCY-CONSTITUTION.md](ESSA-AGENCY-CONSTITUTION.md)) |
| **Companion** | [`td-isa.yaml`](td-isa.yaml) |
| **Related** | [`UFATO.md`](UFATO.md) · [`SAFETY-FIRST.md`](SAFETY-FIRST.md) · [`CCTLS.md`](CCTLS.md) · [`IPSN.md`](IPSN.md) |
| **Last Updated** | 2026-04-14 |

---

## 0. Preamble

Across aviation and other high-consequence industries, technical information is
often produced through different authoring traditions, visual conventions,
coding logics, and procedural philosophies. Even when the operational intent is
the same, the representation of that intent may vary significantly between
organisations, platforms, and legacy systems.

This fragmentation creates unnecessary complexity for:

- maintenance technicians who must interpret tasks across different documentary systems,
- authors and illustrators who must re-express similar technical intent in multiple formats,
- operators and MRO organisations seeking interoperability,
- digital toolchains that depend on consistent structure and semantics,
- future automation systems that require stable, machine-readable, and trustworthy data.

TD-ISA is proposed as a dedicated entity focused on establishing a common
framework for the integrity, standardisation, and automation-readiness of
technical data.

---

## 1. Mission Statement

> **TD-ISA advances technical data integrity, standardisation, and automation
> to improve safety, interoperability, efficiency, and operational reliability
> across digital engineering and technical publication ecosystems.**

---

## 2. Core Mission: Three Pillars

TD-ISA is organised around three interdependent pillars:

### 2.1 Technical Data Integrity

Ensuring consistency, traceability, accuracy, and governance of technical
information across its lifecycle.

| Concern | What TD-ISA Addresses |
|---------|----------------------|
| Consistency | Same operational intent produces semantically equivalent content regardless of authoring origin |
| Traceability | Every technical datum links to its source requirement, safety objective, or engineering authority |
| Accuracy | Content validation against structured rules, not narrative review alone |
| Governance | Version control, change authority, baseline management, and audit readiness |

### 2.2 Standardisation

Promoting shared authoring rules, visual conventions, safety semantics, and
digital presentation principles.

| Concern | What TD-ISA Addresses |
|---------|----------------------|
| Authoring rules | Sentence structure, controlled vocabulary, procedural clarity |
| Visual conventions | Colour coding, line weights, callout styles, safety cue rendering |
| Safety semantics | Invariant severity hierarchy (DANGER / WARNING / CAUTION / NOTE) |
| Presentation | Digital display behaviour, accessibility, interaction logic |

TD-ISA references and governs the **UFATO** standard
(ESSA-STD-UFATO-001) as its core representation framework:
universal form for presentation; adaptive technical organisation for content
structure.

### 2.3 Automation

Enabling technical content to be more easily validated, reused, processed,
and integrated into automated and semi-automated operational environments.

| Concern | What TD-ISA Addresses |
|---------|----------------------|
| Machine readability | Structured semantic markup, typed metadata, machine-parseable rules |
| Validation logic | Automated BREX / Schematron / schema checks at authoring and build time |
| Content reuse | Modular data modules with stable identifiers and applicability filtering |
| Workflow integration | API-ready publication artefacts, CI/CD-compatible build pipelines |

---

## 3. Strategic Objective

The objective is **not** to rigidly standardise every technical chapter or
every engineering architecture.

The objective is to define a **universal representation framework** while
preserving **technology-specific flexibility** in content structure.

> **Universal form. Adaptive technical organisation.**

This is the strategic equilibrium:

- Strong standardisation where **cognitive consistency and safety** matter most.
- Controlled flexibility where **engineering reality** demands it.

---

## 4. Why It Matters

A stronger common framework would:

| Benefit | Impact Area |
|---------|-------------|
| Save time | Authoring, translation, cross-fleet maintenance |
| Reduce costs | Fewer format conversions, less rework, smaller training burden |
| Reduce interpretation errors | Uniform safety cues, controlled vocabulary, consistent layout |
| Improve training transferability | Technicians trained on one system can read another |
| Improve content reuse | Modular data modules shareable across programmes |
| Reduce aircraft-on-ground exposure | Faster access to correct, unambiguous maintenance data |
| Strengthen safety and security | Invariant safety semantics, traceable content governance |
| Improve interoperability | OEMs, suppliers, operators, and MROs share a common data language |
| Enable automation | Machine-readable, validated, structured data for digital workflows |

---

## 5. Economic Argument: The Documentary Retraining Problem

The strongest economic justification for TD-ISA lies in a distinction that is
rarely made explicit:

> **The industry is not only paying to train for the aircraft.
> It is also paying to train for the documentary differences around the aircraft.**

Today, training a maintenance technician, author, or SME involves not only
the technical system itself, but also the specific way each manufacturer,
variant, or platform **represents** that system in its publications. This
creates cost at three levels.

### 5.1 Cost of Formation (Initial Training)

Training hours are consumed not only by the technical system, but also by:

- documentary logic and navigation philosophy,
- coding systems and numbering conventions,
- colour schemes and visual symbology,
- procedural voice and structure,
- variant-specific documentary differences.

Every organisation that publishes differently adds formation overhead that has
**nothing to do with the aircraft itself**.

### 5.2 Cost of Transition (Cross-Platform Adaptation)

Each transition between:

- aircraft model or variant,
- OEM or constructor,
- operator or MRO organisation,
- documentary platform or legacy system,

introduces an **adaptation curve** that consumes time and reduces initial
efficiency — even when the underlying technical competence already exists.

### 5.3 Cost of Operational Friction (In-Service Impact)

When technicians, instructors, authors, or SMEs must mentally translate
between different documentary frameworks during operations, the result is:

- longer reading and interpretation times,
- more frequent need for refresher actions,
- higher dependence on specific prior experience,
- increased probability of doubt or misinterpretation,
- reduced ability to reuse competences across fleets.

### 5.4 The Core Insight

If the **representation** were significantly more standardised, training
could concentrate on what genuinely matters:

- the technology,
- the architecture of the system,
- the real operational risks,
- the safe execution of the task.

And **not** on relearning, each time, a new documentary grammar.

> **Standardised technical representation would not eliminate technical
> training. It would eliminate unnecessary retraining on how different
> organisations choose to represent the same maintenance intent.**

### 5.5 Scale of Impact

This cost is not marginal. It is **multiplicative** across:

| Multiplier | Effect |
|------------|--------|
| Mixed fleets | Each fleet type may carry a different documentary philosophy |
| Variants within type | Sub-variant documentary differences compound the problem |
| Multi-OEM MROs | MRO organisations serving multiple constructors pay the cost for each |
| Personnel rotation | Every technician transition restarts the adaptation curve |
| Recurrent training | Documentary differences must be refreshed alongside technical content |
| Digital expansion | New IETP platforms introduce additional interaction-logic differences |

A common representation framework would **dramatically reduce training
overhead, accelerate cross-platform readiness, and improve operational
efficiency** across the entire aviation ecosystem.

### 5.6 Formula

```
Total Training Cost = Technical Training (necessary)
                    + Documentary Retraining (reducible)

TD-ISA Target: minimise Documentary Retraining → 0
               by maximising representational commonality.
```

The savings potential is proportional to the number of **documentary
boundaries** a workforce must cross. For large operators, multi-type MROs,
and global supply chains, this represents a **structural cost reduction
opportunity**.

---

## 6. Workstreams

TD-ISA operates through five main workstreams:

```
┌──────────────────────────────────────────────────────────────────────────┐
│                          TD-ISA WORKSTREAMS                              │
│                                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                    │
│  │ WS-1         │  │ WS-2         │  │ WS-3         │                    │
│  │ Authoring    │  │ Represent-   │  │ Digital      │                    │
│  │ Integrity    │  │ ation Stds   │  │ Readability  │                    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                    │
│         │                 │                 │                             │
│         └────────┬────────┴────────┬────────┘                            │
│                  │                 │                                      │
│  ┌──────────────┐│  ┌──────────────┐│                                    │
│  │ WS-4         ││  │ WS-5         ││                                    │
│  │ Technology-  ││  │ Automation   ││                                    │
│  │ Specific     ││  │ Enablement   ││                                    │
│  │ Profiles     ││  │              ││                                    │
│  └──────────────┘│  └──────────────┘│                                    │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.1 WS-1 — Authoring Integrity

Controlled terminology, procedural clarity, semantic consistency, and
traceable content governance.

| Deliverable | Description | UFATO Binding |
|-------------|-------------|---------------|
| Controlled vocabulary register | Master BREX dictionary with domain extensions | UF-CT-01 through UF-CT-04 |
| Authoring style guide | Sentence length, voice, mood, conditional nesting rules | UF-AR-01 through UF-AR-06 |
| Content governance model | Change authority, review cycles, baseline rules | CCTLS gate sequence |
| Traceability matrix template | Requirement → content → evidence chain | H-Pipeline H_REQ / H_EVIDENCE |

### 5.2 WS-2 — Representation Standards

Harmonised rules for visual hierarchy, colour coding, line conventions,
illustration semantics, and safety cue presentation.

| Deliverable | Description | UFATO Binding |
|-------------|-------------|---------------|
| Safety severity scheme | Invariant DANGER / WARNING / CAUTION / NOTE rendering | UFATO §4.3 |
| Visual hierarchy specification | Heading mapping, step numbering, table captioning | UF-VH-01 through UF-VH-06 |
| Illustration standard | Line weights, callout conventions, greyscale legibility | UF-IC-01 through UF-IC-04 |
| Colour scheme annex | Day-mode and night-mode palettes with WCAG AA compliance | UF-VH-05, UF-VH-06 |

### 5.3 WS-3 — Digital Readability and Interaction

Standards for display behaviour on tablets, laptops, and maintenance-oriented
digital interfaces.

| Deliverable | Description | UFATO Binding |
|-------------|-------------|---------------|
| IETP interaction specification | Breadcrumbs, hyperlinks, effectivity filtering, undo | UF-IL-01 through UF-IL-05 |
| Responsive display guidelines | Minimum text sizes, contrast ratios, touch targets | UF-VH-04, UF-VH-05, UF-IC-04 |
| Offline-mode specification | Baseline preservation, sync logic, conflict resolution | UF-IL-05 |
| Accessibility conformance profile | WCAG 2.1 AA mapping for maintenance environments | UF-VH-04, UF-VH-05 |

### 5.4 WS-4 — Technology-Specific Profiles

Adaptable chaptering and content structuring models for conventional aircraft,
hydrogen systems, fuel cells, high-voltage architectures, AI-assisted systems,
and future aerospace configurations.

| Deliverable | Description | UFATO Binding |
|-------------|-------------|---------------|
| Chapter Scheme registry | Technology-domain chapter decompositions registered in AGGIX | AS-GOV-01 through AS-GOV-05 |
| Hydrogen (LH₂) profile | Chapters 28H/28V/28R, 73H/73C/73E | UFATO §5.2.2 |
| High-voltage profile | Chapters 24E/24B/24G | UFATO §5.2.3 |
| AI-assisted systems profile | Chapters 45A/45X/45M | UFATO §5.2.4 |
| Domain Glossary Extension (DGE) template | Structured term registration for new technology domains | UFATO §5.3 |

### 5.5 WS-5 — Automation Enablement

Machine-readable patterns, validation logic, structured semantics, and
interoperability rules that support digital workflows and automation.

| Deliverable | Description | Integration |
|-------------|-------------|-------------|
| BREX validation rule set | Schematron / XSD rules for automated authoring checks | S1000D BREX + UFATO Layer 1 |
| Publication build pipeline specification | CI/CD-compatible IETP build with automated link-checking | CCTLS PUBLISH gate |
| Structured metadata schema | YAML/JSON sidecar schemas for data modules | AGGIX PUB / CFG resource types |
| Interoperability API specification | REST/GraphQL interfaces for cross-system content exchange | AGGIX URI resolution |
| Machine-learning data extraction patterns | Structured patterns for training data extraction from tech pubs | ESSA AI governance |

---

## 7. Placement in the ESSA Stack

TD-ISA operates as a **cross-cutting entity** within ESSA governance:

```
ESSA-CONST-001 (Constitutional Root)
         │
         ├── ESSA-Agency (Institutional Mission)
         │        │
         │        ├── Sector Execution Authorities (EUSSA, etc.)
         │        │
         │        └── TD-ISA (Technical Data Governance Entity)
         │                │
         │                ├── WS-1 Authoring Integrity
         │                ├── WS-2 Representation Standards
         │                ├── WS-3 Digital Readability
         │                ├── WS-4 Technology-Specific Profiles
         │                └── WS-5 Automation Enablement
         │
         ├── CCTLS (Lifecycle Standard)
         │
         ├── UFATO (Publication Governance Standard)
         │       ↑ governed by TD-ISA
         │
         └── SAFETY-FIRST (Doctrine)
```

**Key relationship:** UFATO (ESSA-STD-UFATO-001) is the **primary technical
standard** that TD-ISA governs and advances. TD-ISA provides the
institutional authority, workstream structure, and cross-industry coordination
that UFATO's rules require for effective adoption.

---

## 8. Institutional Positioning

TD-ISA may be framed as one of the following, depending on its intended
level of authority, governance, and participation:

| Form | Description | Governance Model |
|------|-------------|------------------|
| **Institute** | Permanent research and standards body | Board-directed, funded R&D agenda |
| **Council** | Advisory body with industry representation | Rotating chair, consensus-based recommendations |
| **Foundation** | Non-profit entity with open-access mandate | Membership-funded, public deliverables |
| **Standards Initiative** | Focused working group within an existing body | Time-bound charter, deliverable-driven |
| **Cross-Industry Working Body** | Multi-stakeholder coordination mechanism | Federated participation, shared governance |

The recommended initial framing is a **Standards Initiative** under ESSA
governance, with a pathway to institutionalisation as a **Council** or
**Foundation** once workstream deliverables reach maturity.

---

## 9. Integration Points

### 9.1 With ESSA Governance

| ESSA Artefact | TD-ISA Binding |
|---------------|----------------|
| ESSA-Agency Constitution | TD-ISA operates under ESSA-Agency institutional authority |
| CCTLS gate sequence | TD-ISA workstream deliverables follow INTERPRET → CONFIRM → ACTIVATE → PUBLISH |
| H-Pipeline (H_ENVELOPE) | WS-1 traceability extends H-token chains into publication content |
| AGGIX registry | WS-4 Chapter Schemes and WS-5 metadata schemas registered as CFG/PUB resources |
| UFATO (ESSA-STD-UFATO-001) | TD-ISA's primary technical standard — governs Layer 1 + Layer 2 rules |
| SPEC-PELS-014 lifecycle | Publication artefact states align with PELS engineering/product states |
| Safety-First Doctrine | WS-2 safety semantics are derived from SAFETY-FIRST invariants |

### 9.2 With External Standards and Bodies

| Standard / Body | Relationship |
|-----------------|-------------|
| S1000D Steering Committee | WS-1/WS-2 rules align with and extend S1000D BREX and presentation specs |
| ATA e-Business Group | WS-4 conventional-aircraft profile maps to ATA iSpec 2200 |
| SAE International (ARP4754A, ARP4761) | WS-1 traceability compatible with system development and safety assessment processes |
| EASA / FAA | WS-4 technology-specific profiles support certification data packages |
| ISO TC20/SC1 (Aerospace terminology) | WS-1 controlled vocabulary harmonised with ISO aerospace terminology |
| W3C (WCAG) | WS-3 accessibility rules conform to WCAG 2.1 AA |
| DO-178C / DO-330 (RTCA) | WS-4 AI-assisted systems profile references software/tool qualification |

---

## 10. Conformance and Governance

### 10.1 Workstream Maturity Levels

Each workstream progresses through defined maturity levels:

| Level | Label | Criteria |
|-------|-------|----------|
| **M0** | Proposed | Workstream scope and deliverables defined |
| **M1** | In Development | Deliverables in INTERPRET or CONFIRM state |
| **M2** | Published | Deliverables in ACTIVATE or PUBLISH state |
| **M3** | Adopted | Deliverables in operational use by at least one external organisation |
| **M4** | Institutionalised | Deliverables incorporated into formal industry standards |

### 10.2 Current Maturity Assessment

| Workstream | Level | Status |
|------------|-------|--------|
| WS-1 Authoring Integrity | M1 | UFATO Layer 1 authoring rules defined |
| WS-2 Representation Standards | M1 | UFATO Layer 1 visual/safety semantics defined |
| WS-3 Digital Readability | M1 | UFATO Layer 1 interaction logic defined |
| WS-4 Technology-Specific Profiles | M1 | UFATO Layer 2 reference Chapter Schemes defined |
| WS-5 Automation Enablement | M0 | Scope defined; deliverables pending |

---

## 11. What TD-ISA Is Not

1. **Not a replacement for S1000D, ATA iSpec 2200, or any existing standard.**
   TD-ISA coordinates and extends; it does not supplant.
2. **Not a software product.** TD-ISA defines standards, rules, and governance
   frameworks. Implementation is the responsibility of CSDB, IETP, and
   toolchain providers.
3. **Not a regulatory authority.** TD-ISA proposes and governs standards;
   certification authority remains with EASA, FAA, and equivalent bodies.
4. **Not limited to aviation.** While aviation is the primary domain, TD-ISA's
   principles apply to any high-consequence industry where technical data
   integrity, standardisation, and automation are critical.

---

## 12. Closing Statement

Technical data should not remain fragmented where common understanding is
essential.

By aligning integrity, representation, and automation-readiness, TD-ISA would
help transform technical publications from isolated documentation products
into a **shared operational language** for safer and more efficient industrial
execution.

---

## 13. Revision History

| Version | Date | Change |
|---------|------|--------|
| v0.1-draft | 2026-04-14 | Initial entity proposal. |
| v0.2-draft | 2026-04-14 | Added §5 Economic Argument: The Documentary Retraining Problem. |
