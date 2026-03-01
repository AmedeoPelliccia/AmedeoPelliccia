# ESSA-Agency Constitution v0.1

**European Safety and Security Agency — Constitutional Bridge Layer**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-CONST-001 |
| **Version** | v0.1-draft |
| **Status** | Constitutional Instrument |
| **Nature** | Institutional Bridge — Sovereign Safety Mission Authority + Security Governance Overlay |
| **Doctrine** | Advance in Safety, Protect in Security |
| **Operating Mode** | Agentic · Extensible · Federated by Profiles |
| **Parent** | ESSA-STD-CCTLS-001 — ESSA Constitutional Root Standard |
| **Companion** | [`essa-agency-constitution.yaml`](essa-agency-constitution.yaml) |
| **Last Updated** | 2026-02-28 |

---

## Minimal Charter Statement

> The **European Safety and Security Agency (ESSA-Agency)** is the institutional bridge between the European Sovereign Systems Architecture and European sector safety agencies.
> It operates under a Safety-First doctrine: **advance in safety, protect in security**.
> Safety defines the agentic mission and drives requirement derivation and design generation.
> Security provides governance invariants ensuring integrity, resilience, accountability, and controlled interoperability across all safety-critical lifecycle artefacts and transitions.
> ESSA-Agency is extensible by profiles and enforced through deterministic conformance gates and machine-verifiable certification.

---

## 1. Placement in the Stack

```
European Sovereign Systems Architecture (ESSA-Architecture)
                    │
                    ▼
    EUROPEAN SAFETY AND SECURITY AGENCY (ESSA-Agency)
                    │
                    ▼
European Union Space Safety Agency (EUSSA — disambiguating alias for the ESSA space-domain implementation) + other sector agencies
       (Aviation · Space · RSP · Autonomy · Critical Chains)
```

| Tier | Layer | Name | Role |
|------|-------|------|------|
| 1 | Constitutional Architecture | **European Sovereign Systems Architecture** | Constitutional digital substrate — standards, token graph, lifecycle governance |
| 2 | Institutional Agency | **European Safety and Security Agency** | Institutional mission + governance layer |
| 3 | Sector Execution | **EUSSA + other sector agencies** | Domain-specific safety operations under ESSA-Agency mandates |

ESSA-Architecture provides the constitutional digital substrate.
ESSA-Agency provides the institutional mission and governance layer.
EUSSA (and other sector agencies) execute domain-specific safety operations using ESSA-Agency mandates and conformance requirements.

---

## 2. Mission–Governance Separation

### Safety = Mission (Advance)

ESSA-Agency exists to **advance safety** as the primary civil objective:

- Define and maintain Safety Envelopes
- Derive requirements from safety envelopes (safety-driven generation)
- Validate safety evidence and operational readiness
- Manage incidents, occurrences, lessons learned
- Coordinate cross-border safety continuity
- Oversee autonomous system safety boundaries

### Security = Governance (Protect)

Security is the constitutional mechanism that **preserves safety under stress**:

- Integrity of artefacts, baselines, and audit trails
- Authority binding, sign-off, non-repudiation
- Cyber resilience and incident response
- Supply-chain integrity and provenance controls
- Controlled disclosure and interoperable attestations
- Change control and baseline authority

**Non-negotiable rule:** Security mechanisms **cannot override** safety obligations. Security exists to protect them.

---

## 3. ESSA Doctrine

> **ESSA advances in safety. ESSA protects in security.**

Operationally:

| Stage | Doctrine Application |
|-------|---------------------|
| Generate | Inside safety bounds — derive requirements from Safety Envelope |
| Design | Bounded synthesis — valid design space is D ⊆ Valid(S) |
| Govern | Security invariants protect S from corruption or circumvention |
| Certify | Invariant validation over the lifecycle graph — not narrative |

---

## 4. Agentic and Extensible Operating Model

### 4.1 Agentic Mission Driver (Safety-First Generation)

ESSA-Agency operates an **agentic pipeline** in which:

- Safety Envelopes are first-class artefacts
- Requirements are derived from safety envelopes
- Design candidates are generated only within validated safety bounds
- Any candidate outside the envelope is **non-activable by construction**

### 4.2 Extensibility via Profiles

ESSA-Agency is extensible through **profiles**, not ad-hoc exceptions:

| Profile ID | Domain |
|------------|--------|
| `PROFILE-AVIATION-CS25` | Civil aviation — CS-25 large aeroplane category |
| `PROFILE-SPACE-SAFETY` | Space launch, orbital operations, STM |
| `PROFILE-RSP-REUSE-CYCLES` | Reusable space platforms — refurbishment lifecycle |
| `PROFILE-AUTONOMY-ASSURANCE` | AI-assisted and autonomous operations |
| `PROFILE-CRITICAL-INDUSTRIAL-CHAINS` | Supply-chain integrity and provenance |

**Profile rule:** Profiles **may tighten** controls. They **cannot weaken** the minimum constitutional baseline established in [`EU-SECURITY/README.md`](EU-SECURITY/README.md).

---

## 5. Governance Kernel (Deterministic Gates)

ESSA-Agency enforces deterministic lifecycle gates consistent with the CCTLS pattern:

```
INTERPRET → CONFIRM → ACTIVATE → PUBLISH
```

| Gate | Doctrine Alignment | Purpose |
|------|--------------------|---------|
| **INTERPRET** | Advance in Safety | Safety Envelope definition, requirement derivation |
| **CONFIRM** | Protect in Security | Evidence validation, security control check, authority sign-off |
| **ACTIVATE** | Protect in Security | Invariant validation — non-activable if S coverage incomplete |
| **PUBLISH** | Advance in Safety | Immutable baseline, interoperable attestation |

Safety advances at the **Interpret** and **Derive** stages.
Security is enforced at the **Confirm**, **Activate**, and **Publish** stages via invariant checks.

---

## 6. Conformance and Certification (ALPC Operator)

ESSA-Agency mandates a **certification operator (ALPC)** that validates:

- Safety-envelope presence and integrity
- Requirement derivation trace completeness
- Evidence sufficiency for safety claims
- Security control coverage (minimum common constitution)
- Baseline integrity, authority sign-off, audit completeness

**Certification output is machine-verifiable conformance**, not narrative. Defined in [`cctls.yaml`](cctls.yaml) and [`essa-regulatory-framework.yaml`](essa-regulatory-framework.yaml).

---

## 7. Relationship to EUSSA and Sector Agencies

EUSSA (European Union Space Safety Agency) becomes a **sector execution authority** that:

- Applies ESSA-Agency Safety Envelopes to space operations (STM, traffic, range safety)
- Reports occurrences and operational evidence back into the ESSA lifecycle graph
- Adopts ESSA-Agency EU-SECURITY governance overlay as minimum common baseline
- Packages auditable safety evidence bundles for cross-border interoperability

**ESSA-Agency remains the constitutional layer; EUSSA remains the domain executor.**

The same pattern extends to other sector agencies (Aviation, RSP, Autonomy, Critical Chains).

---

## 8. Constitutional Invariants

The following invariants are non-negotiable under ESSA-Agency governance:

1. **Safety Primacy** — Safety envelopes define the valid design space. No activation without S-preservation evidence.
2. **Security Non-Override** — Security mechanisms cannot override, bypass, or redefine safety obligations.
3. **Deterministic Gates** — Lifecycle transitions are governed by explicit INTERPRET → CONFIRM → ACTIVATE → PUBLISH gates.
4. **Profile Bounds** — Extensions via profiles cannot weaken the constitutional baseline.
5. **Machine Verifiability** — Conformance is validated computationally, not by narrative assertion.
6. **Civil Nature** — ESSA-Agency is a civil sovereign authority. It is not military. It is not an intelligence authority.
7. **Structural Integration** — Achieving coherence across architecture, governance, safety mission, and security invariants constitutes a **Structural Integration State (SIS)**. See [`SIS.md`](SIS.md).
