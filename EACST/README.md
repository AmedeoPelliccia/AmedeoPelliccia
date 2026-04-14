---
# eacst-regulatory-framework.yaml
# Machine-readable specification for the European Agency for Civil Space
# Transportation (EACST) regulatory framework.
# Reference: EACST/README.md §1–§12
# Author: Amedeo Pelliccia
# Aligned with EU Space Act (2025) safety/resilience/sustainability pillars
# and IDEALE-ESG Aerospace pillar governance.

schema_version: "1.0.0"
document_type: regulatory_framework_specification
last_updated: "2026-02-25T00:00:00Z"

# ─────────────────────────────────────────────
# 1. Agency Identity
# ─────────────────────────────────────────────
agency:
  name: European Agency for Civil Space Transportation
  acronym: EACST
  mission: >
    Ensure safe, resilient, and sustainable civil space transportation
    in Europe, with harmonised licensing and oversight for operators
    and reusable platforms, and full integration with European airspace
    and space-traffic-management regimes.
  legal_basis:
    - EU Space Act (safety, resilience, sustainability pillars)
    - Airspace integration frameworks (Eurocontrol/SES, EASA interfaces)
  licensing_model: performance_based   # safety objectives + AMC/GM

# ─────────────────────────────────────────────
# 2. Regulated Domain
# ─────────────────────────────────────────────
scope:
  included:
    - id: SCOPE-LRE
      domain: Launch and re-entry operations
      description: >
        Operations from European territory and/or by EU-established
        operators, including extraterritorial licensing hooks.

    - id: SCOPE-RSP
      domain: Reusable space platforms
      description: >
        RLVs, spaceplanes, reusable stages and their continued
        airworthiness / maintenance systems.

    - id: SCOPE-SPP
      domain: Spaceports and ranges
      description: >
        Ground safety, hazardous operations, interface with
        aviation ATM/UTM.

    - id: SCOPE-SCL
      domain: Crew licensing and training organisations
      description: >
        Professional crew licensing, spaceflight participant
        safety/training, training organisation approvals.

    - id: SCOPE-REG
      domain: Operator registry and supervision
      description: >
        Occurrence reporting, safety management systems (SMS),
        compliance audits.

    - id: SCOPE-SUS
      domain: Sustainability constraints
      description: >
        Debris prevention during ascent/re-entry, controlled
        disposal, environmental footprint reporting.

  excluded:
    - id: EXCL-MIL
      domain: Military space operations
      reason: Remain under national/EU defence frameworks.

    - id: EXCL-SAT
      domain: Pure satellite service provision
      reason: >
        Not tied to transport; covered by EU Space Act horizontal
        regime and other bodies.

# ─────────────────────────────────────────────
# 3. Regulatory Parts (Minimum Viable Set)
# ─────────────────────────────────────────────
parts:
  - id: Part-STO
    title: Space Transportation Operator
    domain: Operator licensing & SMS
    covers:
      - Licence basis
      - Safety management system (SMS)
      - Safety case
      - Financial responsibility / insurance
      - Security baseline
      - Occurrence reporting
    phase: A   # introduced in Phase A

  - id: Part-LRE
    title: Launch and Re-entry Safety
    domain: Launch/re-entry safety
    covers:
      - Trajectory safety
      - Public risk criteria
      - Flight safety system expectations
      - Range coordination
    phase: A

  - id: Part-RSP
    title: Reusable Space Platform
    domain: Reusable platform approval
    covers:
      - Design approval basis for reuse-critical items
      - Configuration control
      - Life limits
      - Refurbishment standards
    phase: B

  - id: Part-CAW-S
    title: Continued Airworthiness — Space
    domain: Continued airworthiness
    covers:
      - CAMO-equivalent for space platforms
      - Maintenance programme approval
      - Reliability and trend monitoring
    phase: B

  - id: Part-MRO-S
    title: Maintenance Organisations — Space
    domain: Maintenance organisations
    covers:
      - Part-145-like approvals for reuse refurbishment/overhaul
      - Human factors
      - Tooling standards
      - NDT standards
    phase: B

  - id: Part-SPP
    title: Spaceport and Range Licensing
    domain: Spaceport/range licensing
    covers:
      - Hazardous operations
      - Propellant handling
      - Emergency planning
      - Interface with ATM/airspace closures
    phase: A

  - id: Part-SCL
    title: Space Crew Licensing
    domain: Crew licensing & training organisations
    covers:
      - Crew categories (flight crew, participants, ground roles)
      - Medical requirements
      - Recurrent training
      - Training organisation approvals
    phase: C

  - id: Part-STO-ORA
    title: Space Training Organisation Requirements
    domain: Training organisation approvals
    covers:
      - Training programme approval
      - Instructor qualification
      - Facility standards
      - Record keeping
    phase: C

  - id: Part-SUST
    title: Sustainability and Debris
    domain: Sustainability & debris
    covers:
      - Debris mitigation plans
      - Controlled disposal requirements
      - Environmental footprint reporting
      - EU Space Label compliance marks
    phase: A

  - id: Part-CYB-S
    title: Cyber Resilience — Space
    domain: Cyber resilience
    covers:
      - Baseline cybersecurity requirements
      - Risk assessment methodology
      - Alignment with EU resilience pillar
    phase: B

# ─────────────────────────────────────────────
# 4. Operator Registry Schema
# ─────────────────────────────────────────────
registry:
  name: EU Civil Space Transport Registry
  description: >
    Unified registry serving as the enforcement backbone for
    authorisation, registration, and supervision of civil space
    transport operators.
  fields:
    - operator_id
    - licence_scope
    - authorised_vehicles_platforms
    - approved_spaceports_ranges
    - platform_configuration_baseline
    - controlled_changes_log
    - occurrence_reports
    - safety_directives
    - stm_sst_linkage

# ─────────────────────────────────────────────
# 5. Crew Categories
# ─────────────────────────────────────────────
crew_categories:
  - id: CREW-FC
    category: Space Transport Flight Crew
    type: professional
    requirements:
      - Licensing
      - Medical certification
      - Proficiency checks

  - id: CREW-SP
    category: Spaceflight Participants
    type: non-professional
    requirements:
      - Minimum training
      - Informed consent
      - Emergency preparedness

  - id: CREW-GS
    category: Ground Safety Critical Roles
    type: professional
    roles:
      - Range safety officer
      - Hazardous operations supervisor
      - Mission director
    requirements:
      - Competency frameworks
      - Recurrent checks

# ─────────────────────────────────────────────
# 6. Continued Airworthiness Requirements
# ─────────────────────────────────────────────
continued_airworthiness:
  description: >
    The key regulatory innovation for reusable space platforms.
    Without lifecycle airworthiness, reusable systems remain
    regulated like one-off rockets.
  requirements:
    - Approved maintenance programme (life limits, inspection intervals, refurbishment criteria)
    - Configuration and build standard regime (as-flown vs as-maintained reconciliation)
    - Mandatory NDT/inspection qualification for refurbishment shops
    - Reliability programmes (trend monitoring, anomaly classification, recurring defect control)
    - Human factors and tool control (aviation MRO equivalent)

# ─────────────────────────────────────────────
# 7. Sustainability Requirements
# ─────────────────────────────────────────────
sustainability:
  description: >
    Transport-grade sustainability requirements converting
    EU Space Act aspirations into enforceable rules.
  requirements:
    - Debris prevention during ascent/re-entry (fragmentation control, passivation, controlled disposal)
    - Re-entry casualty-risk governance and controlled corridors (STM/ATM integration)
    - Environmental reporting for launches (local impact + lifecycle accounting)
    - EU Space Label compliance marks operationalised through licence privileges

# ─────────────────────────────────────────────
# 8. Organisational Directorates
# ─────────────────────────────────────────────
directorates:
  - id: DIR-01
    name: Rulemaking & Standards
    scope: Parts + AMC/GM development

  - id: DIR-02
    name: Certification & Licensing
    scope: Operators, platforms, spaceports

  - id: DIR-03
    name: Continued Airworthiness & Maintenance Oversight
    scope: Reusable platform lifecycle management

  - id: DIR-04
    name: Operations Oversight & Safety Data
    scope: Occurrence reporting, safety directives

  - id: DIR-05
    name: Training & Human Factors
    scope: Crew licensing, training organisation approval

  - id: DIR-06
    name: Sustainability & Debris Compliance
    scope: Debris mitigation, environmental footprint

  - id: DIR-07
    name: Registry & Digital Systems
    scope: Operator registry, configuration ledger, STM/SST interfaces

  - id: DIR-08
    name: International & Legal
    scope: Outer Space Treaty coordination, cross-recognition

# ─────────────────────────────────────────────
# 9. Implementation Roadmap
# ─────────────────────────────────────────────
roadmap:
  - phase: A
    timeline: "0–18 months"
    title: Foundation
    deliverables:
      - Registry stand-up
      - Part-STO Light (interim operator authorisation)
      - Uncrewed launch/re-entry licensing
      - Spaceport licensing (Part-SPP)
      - Occurrence reporting framework
      - Part-SUST baseline

  - phase: B
    timeline: "18–36 months"
    title: Reusability Unlock
    deliverables:
      - Part-RSP (reusable platform approval)
      - Part-CAW-S (continued airworthiness)
      - Part-MRO-S (maintenance organisations)
      - Part-CYB-S (cyber resilience)
      - STM coordination requirements formalised

  - phase: C
    timeline: "36–60 months"
    title: Crewed Operations
    deliverables:
      - Part-SCL (crew licensing)
      - Part-STO-ORA (training organisations)
      - Crewed suborbital/point-to-point licensing
      - Full crew licensing regime

# ─────────────────────────────────────────────
# 10. Institutional Options
# ─────────────────────────────────────────────
institutional_options:
  - id: OPT-NEW
    name: New agency (EACST)
    parent: DG DEFIS
    pros:
      - Clean mandate
      - Purpose-built staff
    cons:
      - Longer stand-up time
      - New institutional overhead

  - id: OPT-EASA
    name: EASA extension ("EASA-Space Transportation")
    parent: EASA
    pros:
      - Fastest lifecycle/AMC/GM culture deployment
      - Existing institutional infrastructure
    cons:
      - Mandate expansion politically heavy
      - Risk of aviation-centric bias

  - id: OPT-HYBRID
    name: Hybrid (EASA + EACST split)
    parent: DG DEFIS / EASA
    split:
      easa_handles:
        - Crew licensing and training
        - ATM interfaces
      eacst_handles:
        - Launch/re-entry licensing
        - Continued airworthiness for reusables
    pros:
      - Minimises duplication
      - Dedicated transport authority
    cons:
      - Coordination overhead between agencies
    recommendation: >
      If the EU Space Act proceeds with authorisation/registration/supervision
      at EU level, the hybrid option often minimises duplication while still
      creating a dedicated transport authority.

# ─────────────────────────────────────────────
# 11. Institutional Context
# ─────────────────────────────────────────────
institutional_context:
  existing_bodies:
    - name: EUSPA
      role: EU Space Programme implementation (Galileo, Copernicus, GOVSATCOM, SST)
      gap: Not structured as a transport safety regulator

    - name: EASA
      role: Aviation regulation; higher airspace operations discussions
      gap: No dedicated EU-level HAO/space-transport regime in force

    - name: ESA
      role: Technology/programme development and investment
      gap: Technical agency, not a regulator

  alignment:
    eu_space_act:
      pillars:
        - safety
        - resilience_cybersecurity
        - sustainability
      relevance: >
        EACST operationalises the EU Space Act's transport-related
        obligations into enforceable implementing rules.
---


# European Agency for Civil Space Transportation (EACST)

*A foundational concept to close Europe's civil space-transport regulatory gaps (training, reusable maintenance, sustainability constraints, operator registry, etc.).*

---

## 1. Problem Statement: What's Missing Today

Europe has **strong capability builders** (ESA, national agencies) and **strong space programme operators** (EU Space Programme / EUSPA), but **no single, specialised EU-level civil regulator for space transportation** end-to-end (launch → re-entry → reuse → continued airworthiness → crew licensing → operator oversight). ESA itself explicitly positions as a *technical* agency rather than a regulator.

At the same time, the European Commission has moved toward an EU-level rulebook via the **EU Space Act (proposal launched 25 June 2025)**, structured around **safety, resilience/cybersecurity, and sustainability** (including debris mitigation and environmental considerations).
The proposal is widely framed as addressing **fragmentation across Member States** and introducing EU-level **authorisation/registration/supervision** concepts.

**Gap:** the EU Space Act is fundamentally a *horizontal* framework for space activities/services; civil **space transportation** needs a *vertical* regulator with aviation-grade lifecycle oversight (training + maintenance + operations + incident reporting + configuration control) that can produce enforceable implementing rules and means of compliance.

---

## 2. Mission and Scope of EACST

**Mission:** Ensure **safe, resilient, and sustainable** civil space transportation in Europe, with **harmonised licensing and oversight** for operators and reusable platforms, and full integration with European airspace and space-traffic-management regimes.

**Regulated domain (civil):**

- **Launch and re-entry operations** from European territory and/or by EU-established operators (including operations abroad by EU operators, via extraterritorial licensing hooks, if politically chosen).
- **Reusable space platforms** (RLVs/spaceplanes/reusable stages) and their **continued airworthiness / maintenance systems**.
- **Spaceports/ranges** (ground safety, hazardous operations, interface with aviation ATM/UTM).
- **Crew licensing + training organisations** (professional crew) and **participant safety/training** (spaceflight participants).
- **Operator registry and supervision**, occurrence reporting, safety management systems (SMS), and compliance audits.
- **Sustainability constraints** for transport operations (debris prevention during ascent/re-entry, controlled disposal, environmental footprint reporting where applicable).

**Explicit exclusions (recommended):**

- Military space operations (remain national/EU defence frameworks).
- Pure satellite service provision not tied to transport (covered by EU Space Act horizontal regime + other bodies).

---

## 3. Institutional Mapping: What Exists, What EACST Adds

**EUSPA (today):** implements the EU Space Programme and associated security/exploitation roles (e.g., Galileo/EGNOS, Copernicus user uptake, GOVSATCOM/IRIS², EU SST front desk). It is not structured as a transport safety regulator.

**EASA (today):** aviation regulator; already touches "higher airspace operations" discussions and issues safety notices linked to uncontrolled re-entries, but there is **no dedicated EU-level HAO/space-transport regime in force**.

**ESA (today):** technology/programme development and investment (including reusability initiatives), not a regulator.

**EACST adds (proposed):** the missing **competent authority for civil space transportation**, capable of:

- issuing **operator licences** and **vehicle/platform approvals**;
- enforcing **continued airworthiness** for reusable systems;
- certifying **training organisations** and licensing **crew**;
- operating a unified **EU civil space transport operator registry**;
- running **oversight, audits, occurrence reporting**, and safety data analysis.

---

## 4. Regulatory Architecture (Pragmatic EU Design)

### 4.1. Legal Basis

- **Basic Regulation** establishing EACST as an EU Agency, with implementing powers aligned to:

  - EU Space Act obligations (safety/resilience/sustainability) for transport operators;
  - airspace integration frameworks (Eurocontrol/SES, EASA interoperability interfaces), by delegation or joint rulemaking.

### 4.2. "Performance-Based" Licensing as the Core Pattern

Adopt a **performance-based** approach (safety objectives + acceptable means of compliance), similar in philosophy to modern launch/re-entry licensing regimes elsewhere (e.g., the FAA's consolidated Part 450 approach).
For Europe, this fits well with the established **AMC/GM** model used in aviation (predictable compliance pathways + flexibility for innovation).

---

## 5. The Missing Rulebooks EACST Should Publish (Minimum Viable Set)

A workable structure is to publish implementing rules as **"Parts"** (aviation-style), plus AMC/GM:

| Domain | Proposed Part | What It Covers (Examples) |
|--------|---------------|---------------------------|
| Operator licensing & SMS | **Part-STO** (Space Transportation Operator) | licence basis, SMS, safety case, financial responsibility/insurance, security baseline, reporting |
| Launch/re-entry safety | **Part-LRE** | trajectory safety, public risk criteria, flight safety system expectations, range coordination |
| Reusable platform approval | **Part-RSP** (Reusable Space Platform) | design approval basis for reuse-critical items, configuration control, life limits, refurbishment standards |
| Continued airworthiness | **Part-CAW-S** | CAMO-equivalent for space platforms, maintenance programme approval, reliability & trend monitoring |
| Maintenance organisations | **Part-MRO-S** | Part-145-like approvals for reuse refurbishment/overhaul, human factors, tooling, NDT standards |
| Spaceport/range licensing | **Part-SPP** | hazardous ops, propellant handling, emergency planning, interface with ATM/airspace closures |
| Crew licensing & training orgs | **Part-SCL / Part-STO-ORA** | crew categories, medical, recurrent training, training organisation approvals |
| Sustainability & debris | **Part-SUST** | debris mitigation plans, controlled disposal requirements, environmental footprint reporting hooks aligned to EU Space Act sustainability pillar |
| Cyber resilience | **Part-CYB-S** | baseline cybersecurity/risk assessment consistent with EU resilience pillar |

---

## 6. Operator Registry: What "Good" Looks Like

EACST should operate a unified **EU Civil Space Transport Registry** with:

- **Operator ID**, licence scope, authorised vehicles/platforms, approved spaceports/ranges;
- **platform configuration baseline** + controlled changes (continued airworthiness concept);
- **occurrence reporting** and safety directives;
- linkage to **STM/SST services** (EU-level tracking/coordination obligations under EU Space Act's safety direction).

This is not just a database—it is the enforcement backbone that makes "authorisation / registration / supervision" real in daily operations (the direction that EU Space Act materials explicitly signal).

---

## 7. Reusable Platform Maintenance: The Key Regulatory Innovation

The single biggest "new" domain versus traditional space governance is **continued airworthiness for reusables**.

EACST should require each reusable platform/operator to have:

- an approved **Maintenance Programme** (life limits, inspection intervals, refurbishment criteria);
- a **Configuration & Build Standard** regime (as-flown vs as-maintained reconciliation);
- mandatory **NDT/inspection qualification** for refurbishment shops;
- reliability programmes (trend monitoring, anomaly classification, recurring defect control);
- human factors + tool control requirements akin to aviation MRO.

This is the "Part-M ecosystem" for space transport—without it, reusable systems remain regulated like one-off rockets, which breaks economically and operationally.

---

## 8. Civil Training Procedures: Harmonise Before Traffic Scales

EACST should define **crew categories** and training minima:

- **Space Transport Flight Crew** (professional): licensing, medical, proficiency checks.
- **Spaceflight Participants**: minimum training + informed consent rules + emergency preparedness.
- **Ground safety critical roles**: range safety officer, hazardous ops supervisor, mission director—competency frameworks + recurrent checks.

This aligns with the reality flagged in "higher airspace operations" roadmapping: EU needs dedicated regimes as operations emerge.

---

## 9. Sustainability Constraints: Make It Enforceable, Not Aspirational

The EU Space Act proposal foregrounds sustainability (debris mitigation and environmental aspects).
EACST should convert that into transport-grade requirements:

- debris prevention during ascent/re-entry (fragmentation control, passivation, controlled disposal);
- re-entry casualty-risk governance and controlled corridors (with STM/ATM integration);
- environmental reporting for launches (local environmental impact + lifecycle accounting hooks where proportionate);
- incentives: "EU Space Label" style compliance marks can be operationalised through licence privileges.

---

## 10. Organisational Design (Lean but Complete)

**Directorates (minimal):**

1. **Rulemaking & Standards** (Parts + AMC/GM)
2. **Certification & Licensing** (operators, platforms, spaceports)
3. **Continued Airworthiness & Maintenance Oversight**
4. **Operations Oversight & Safety Data** (occurrence reporting, directives)
5. **Training & Human Factors**
6. **Sustainability & Debris Compliance**
7. **Registry & Digital Systems** (operator registry, configuration ledger, interfaces to STM/SST)
8. **International & Legal** (Outer Space Treaty state-responsibility coordination; cross-recognition)

---

## 11. Fast Implementation Roadmap (So It Doesn't Stall)

**Phase A (0–18 months):**

- Stand up the **registry** + interim "Part-STO Light" for operator authorisation.
- Start with **uncrewed** launch/re-entry + spaceport licensing + occurrence reporting.

**Phase B (18–36 months):**

- Introduce **Part-RSP / Part-CAW-S / Part-MRO-S** for reusable systems (the economic unlock).
- Formalise STM coordination requirements (EU Space Act safety pillar operationalised).

**Phase C (36–60 months):**

- Expand to **crewed** suborbital/point-to-point and full crew licensing regime.

---

## 12. Three Viable Institutional Options (Politically Realistic)

1. **New agency (EACST)** under DG DEFIS: clean mandate, purpose-built staff.
2. **EASA extension ("EASA-Space Transportation")**: fastest to deploy lifecycle/AMC/GM culture, but mandate expansion is politically heavy.
3. **Hybrid**: EASA handles crew/training/ATM interfaces; EACST handles launch/re-entry licensing + continued airworthiness for reusables.

If the EU Space Act proceeds with authorisation/registration/supervision at EU level, the **hybrid** often minimises duplication while still creating a dedicated transport authority.

---

## References

- [EU Space Act — Defence Industry and Space — European Union](https://defence-industry-space.ec.europa.eu/eu-space-act_en)
- [EU Space Act — European Parliament Briefing](https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/775922/EPRS_BRI%282025%29775922_EN.pdf)
- [About EUSPA — EU Agency for the Space Programme](https://www.euspa.europa.eu/about)
- [EASA Proposal for a Roadmap on Higher Space Operations](https://horizoneuropencpportal.eu/sites/default/files/2024-05/easa-proposal-for-a-roadmap-on-higher-space-operations-2023.pdf)
- [ESA Commercialisation Gateway — Reusable Space Transportation](https://commercialisation.esa.int/2025/06/reusable-space-transportation-takes-step-forward-with-esa/)
- [14 CFR Part 450 — Launch and Reentry License (FAA)](https://www.ecfr.gov/current/title-14/chapter-III/subchapter-C/part-450)
- [Space Traffic Management — European Commission](https://defence-industry-space.ec.europa.eu/eu-space/space-traffic-management_en)
- [ESA in Talks with SpaceX on Space Junk — Reuters](https://www.reuters.com/technology/space/europe-agency-says-it-is-talks-with-spacex-tackling-space-junk-2024-10-24/)

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`eacst-regulatory-framework.yaml`](eacst-regulatory-framework.yaml) | Machine-readable EACST specification: Parts catalogue, registry schema, implementation phases, institutional options |
| Root [`README.md`](../README.md) | Profile-level reference to EACST under Current Focus |
