# AGGIX — Aggregation + Global Infrastructure Exchange

**Resource Model & Interaction Protocol Specification**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AGGIX-001 |
| **Version** | v1.0-locked |
| **Status** | Normative — Definitions Locked |
| **Parent** | ESSA-DOC-GAIA-001 ([GAI-A.md](GAI-A.md)) |
| **Companion** | [`aggix.yaml`](aggix.yaml) |
| **Related** | [`GAI-A.md`](GAI-A.md) · [`AMPEL360.md`](AMPEL360.md) · [`IPSN.md`](IPSN.md) · [`cctls.yaml`](cctls.yaml) |
| **Last Updated** | 2026-04-06 |

---

## Constitutional Constraint (inherited)

> Evolutionary Change ⊆ Valid(H_Envelope)

All AGGIX operations inherit this invariant from GAI-A L0. No resource may be created, updated, or linked in a manner that violates the safety envelope.

---

## 1. Purpose

AGGIX is the **L2 trunk** of the GAI-A governance tree. It provides:

1. A **canonical resource registry** — typed, versioned, URI-addressed resources.
2. A **URI scheme** — globally unique, version-pinned identifiers for every governed artefact.
3. An **interaction protocol** — seven verbs with policy gates enforcing the eight tree rules.
4. The **physical substrate** — GAIA Grids as the infrastructure realization.

AGGIX is the layer where all domain branches (AMPEL, MARE-E, GAIR-SPACE, Robotics A+) register, share, certify, and govern their resources. Cross-branch sharing happens exclusively through AGGIX linking — never through copying (Tree Rule 8).

---

## 2. Position in the GAI-A Tree

```
L0  GAI-A (Root)
     │
L1  AMAR (Trunk) — mission authority
     │
L2  AGGIX (Trunk) — THIS DOCUMENT ← resource registry + infrastructure
     │
L3  AMPEL │ MARE-E │ GAIR-SPACE │ Robotics A+
```

AGGIX sits between mission governance (AMAR, L1) and domain execution (L3 branches). It provides the **common data plane** that all branches read from and write to.

---

## 3. Resource Types

AGGIX manages exactly **10 resource types**. Each type has a three-letter code used in URIs and APIs.

| # | Code | Resource Type | Description | Lifecycle Owner |
|---|------|---------------|-------------|-----------------|
| 1 | **DT** | Digital Twin | Real-time state model, simulation mirror | Programme |
| 2 | **AI** | AI Model | ML/DL model, inference pipeline, training artefact | Programme + Ethics Board |
| 3 | **DS** | Dataset | Structured data collection (telemetry, fleet, test) | Programme |
| 4 | **DPP** | Digital Product Passport | Per EU Ecodesign — lifecycle record | Regulatory |
| 5 | **ASM** | Assembly | Certified hardware/software component | Configuration Board |
| 6 | **FMU** | FMU/FMI Unit | Co-simulation functional mock-up unit | Systems Engineering |
| 7 | **EV** | Evidence | Certification evidence (test report, analysis, review) | Certification Authority |
| 8 | **PUB** | Publication | Technical publication (S1000D CSDB module) | Publications Authority |
| 9 | **CFG** | Configuration | Configuration item, baseline snapshot, software load | Configuration Board |
| 10 | **TKN** | Token | Teknia Token — contribution record, uncertainty reward | AGGIX Ledger |

### 3.1 Resource Type Properties

Every AGGIX resource carries these mandatory fields:

| Field | Type | Description |
|-------|------|-------------|
| `uri` | `aggix://…` | Canonical URI (see §4) |
| `type` | 3-letter code | One of: DT, AI, DS, DPP, ASM, FMU, EV, PUB, CFG, TKN |
| `version` | semver | Semantic version (major.minor.patch) |
| `status` | enum | `draft` → `confirmed` → `activated` → `published` → `deprecated` |
| `branch` | string | Owning L3 branch (or `global` for L2 resources) |
| `programme` | string | Programme instance identifier |
| `checksum` | sha3-512 | Content integrity hash |
| `created_at` | ISO 8601 | Creation timestamp |
| `updated_at` | ISO 8601 | Last modification timestamp |
| `parent_uri` | `aggix://…` | Parent resource (if hierarchical) |
| `certifications` | list | Attached certification evidence URIs |
| `constraints` | list | Inherited + own constraint set |

---

## 4. Canonical URI Scheme

```
aggix://{domain}/{branch}/{programme}/{type}/{id}@{version}
```

### 4.1 URI Components

| Component | Description | Constraints | Example |
|-----------|-------------|-------------|---------|
| `domain` | Top-level domain | Fixed: `gai-a.ampel` | `gai-a.ampel` |
| `branch` | L3 branch or `aggix` for global | `ampel`, `mare-e`, `gair-space`, `robotics-a-plus`, `aggix` | `ampel` |
| `programme` | Programme instance | Alphanumeric + hyphens | `q100` |
| `type` | Resource type code | 2–3 uppercase letters from §3 | `ASM` |
| `id` | Resource identifier | Alphanumeric + hyphens, unique within type+programme | `h2-pem-stack-001` |
| `version` | Semantic version | `major.minor.patch` | `1.2.0` |

### 4.2 URI Examples

```
# Aviation assembly
aggix://gai-a.ampel/ampel/q100/ASM/h2-pem-stack-001@1.2.0

# Aviation digital twin
aggix://gai-a.ampel/ampel/q100/DT/thermal-model-wing@3.0.1

# Aviation AI model
aggix://gai-a.ampel/ampel/q100/AI/predictive-maint-nn@2.1.0

# Aviation publication (S1000D)
aggix://gai-a.ampel/ampel/q100/PUB/amm-ata28-fuel@5.0.0

# Maritime assembly (same H₂ PEM stack — linked, not copied)
aggix://gai-a.ampel/mare-e/survey-platform/ASM/h2-pem-stack-001@1.2.0

# Space digital twin
aggix://gai-a.ampel/gair-space/constellation-alpha/DT/orbit-propagator@3.1.0

# Robotics assembly (multi-parent)
aggix://gai-a.ampel/robotics-a-plus/swarm-inspector/ASM/quadrotor-frame@1.0.0

# Global Teknia Token
aggix://gai-a.ampel/aggix/global/TKN/tt-contrib-001@1.0.0

# GAIA Grid node (global infrastructure)
aggix://gai-a.ampel/aggix/global/CFG/dc-munich-01@1.0.0

# Digital Product Passport
aggix://gai-a.ampel/ampel/q100/DPP/battery-passport-001@1.0.0

# Certification evidence
aggix://gai-a.ampel/ampel/q100/EV/do178c-test-report-028@2.0.0
```

### 4.3 URI Resolution Rules

1. **Immutability:** A versioned URI always resolves to the same content. Content changes require a new version.
2. **Cross-branch linking:** When resource `R` is shared across branches, it has ONE canonical URI. Other branches link to it — never copy.
3. **Deprecation:** Deprecated URIs still resolve but include `status: deprecated` and a `successor_uri` field.

---

## 5. Interaction Verbs

AGGIX defines exactly **7 interaction verbs**. Each verb passes through a **policy gate** that enforces the applicable tree rules before execution.

| # | Verb | Description | Policy Gate | Tree Rules Enforced |
|---|------|-------------|-------------|---------------------|
| 1 | **CREATE** | Register a new resource | Branch template compliance | Rule 1 (propagation), Rule 6 (template) |
| 2 | **READ** | Retrieve resource metadata + payload | Access-control (Gaia-X Self-Description) | — |
| 3 | **UPDATE** | Modify resource (creates new version) | Monotonic strengthening | Rule 2 (strengthening), Rule 7 (durability) |
| 4 | **SUBSCRIBE** | Establish live notification link | Access-control + rate-limit | Rule 8 (linking) |
| 5 | **DELEGATE** | Transfer governance authority | AMAR approval + delegation chain | Rule 5 (AMAR approval) |
| 6 | **CERTIFY** | Attach certification evidence | Upward certification check | Rule 4 (upward cert) |
| 7 | **DEPRECATE** | Mark resource as deprecated | Durability enforcement | Rule 7 (no deletion) |

### 5.1 Verb Semantics

#### CREATE

```
CREATE(uri, type, payload, branch, programme, constraints[])
  → GATE: template_compliance_check(type, branch)
  → GATE: constraint_propagation_check(constraints, parent_constraints)
  → RESULT: resource registered, version 1.0.0
```

#### READ

```
READ(uri, requester_identity)
  → GATE: access_control(requester_identity, resource.access_policy)
  → RESULT: resource metadata + payload (if authorized)
```

#### UPDATE

```
UPDATE(uri, delta, justification)
  → GATE: monotonic_strengthening(current.constraints, new.constraints)
  → GATE: version_increment(current.version) → new_version
  → RESULT: new version created, previous version preserved (Rule 7)
```

#### SUBSCRIBE

```
SUBSCRIBE(uri, subscriber_identity, callback_uri)
  → GATE: access_control(subscriber_identity, resource.access_policy)
  → GATE: rate_limit_check(subscriber_identity)
  → RESULT: notification link established
```

#### DELEGATE

```
DELEGATE(uri, from_authority, to_authority, scope)
  → GATE: amar_approval(delegation_request)
  → GATE: delegation_chain_validation(from → to)
  → RESULT: governance authority transferred within scope
```

#### CERTIFY

```
CERTIFY(uri, evidence_uri, standard, authority)
  → GATE: upward_certification_check(resource, evidence)
  → GATE: standard_applicability(resource.branch, standard)
  → RESULT: certification evidence attached, propagates upward
```

#### DEPRECATE

```
DEPRECATE(uri, successor_uri, justification)
  → GATE: durability_check(resource.history preserved)
  → GATE: successor_exists(successor_uri)
  → RESULT: status → deprecated, successor_uri linked
```

---

## 6. PATH → MTL as AGGIX Verb Chain

The existing PATH → MTL traceability pipeline maps directly to AGGIX verb sequences:

| PATH → MTL Stage | AGGIX Verb | Resource Type |
|-------------------|------------|---------------|
| **P** — Prompting | CREATE | DS (requirements dataset) |
| **A** — Approved | CERTIFY | EV (approval evidence) |
| **T** — Template | CREATE | CFG (template configuration) |
| **H** — Heading | UPDATE | PUB (publication heading) |
| **M** — Model | CREATE | DT / AI (model resource) |
| **T** — TEKNIA | CERTIFY | TKN (Teknia Token) |
| **L** — Ledger | SUBSCRIBE | TKN (ledger notification) |

---

## 7. GAIA Grids — Physical Infrastructure

GAIA Grids are the physical realization of AGGIX. They are registered as **CFG** (configuration) resources at the global level.

| Grid Type | Description | AGGIX Registration |
|-----------|-------------|-------------------|
| **Data Center** | Sovereign compute + storage | `aggix://…/aggix/global/CFG/dc-{location}@{ver}` |
| **Edge Node** | Proximity compute for real-time | `aggix://…/aggix/global/CFG/edge-{location}@{ver}` |
| **QKD Link** | Quantum key distribution channel | `aggix://…/aggix/global/CFG/qkd-{link-id}@{ver}` |
| **HPC Node** | EuroHPC supercomputing resource | `aggix://…/aggix/global/CFG/hpc-{site}@{ver}` |

---

## 8. Cross-Branch Sharing Protocol

When a resource serves multiple L3 branches (e.g., an H₂ PEM stack used by both AMPEL and MARE-E):

1. The resource is **CREATE**d once under its primary branch.
2. Secondary branches **SUBSCRIBE** to the canonical URI.
3. The resource's constraint set is the **union** of all subscribing branches' constraints (Rule 3).
4. **CERTIFY** must be called for each applicable standard — no standard is substituted or waived.
5. Changes via **UPDATE** automatically notify all subscribers.
6. The resource is never copied — only linked (Rule 8).

### 8.1 Multi-Certification Example

```
Resource: aggix://gai-a.ampel/ampel/q100/ASM/h2-pem-stack-001@1.2.0
Subscribers: [ampel/q100, mare-e/survey-platform]

Certifications required:
  AMPEL:  DO-178C DAL A, DO-254 DAL A, AS9100D, DO-160G, ARP 4761A
  MARE-E: IEC 61508 SIL 3, DNV-GL Type Approval, ISO 9001, IMO FSA

Resolution: ALL certifications carried simultaneously (strictest-wins)
```

---

## 9. Governance Primitives

AGGIX provides two foundational governance primitives used by all branches:

### 9.1 Capillary Merit

Merit-based contribution tracking that flows through the tree. Each contribution to a resource (design, review, test, fix) generates a **TKN** resource recording the actor, action, and uncertainty reduction achieved.

### 9.2 TraceThreads

Traceability threads that connect resources across the tree. A TraceThread is an ordered sequence of AGGIX URIs representing a requirement-to-evidence chain. TraceThreads are immutable once published and are the primary audit artefact for certification.

---

## 10. Normative References

- ESSA-DOC-GAIA-001 — GAI-A Capstone Specification
- ESSA-DOC-AMPEL360-001 — AMPEL360 Lifecycle Engine
- ESSA-DOC-IPSN-001 — Integrity / Provenance / Security / Non-repudiation
- Gaia-X Trust Framework v22.10
- IDS RAM 4.0
- W3C DID Core v1.0
- W3C Verifiable Credentials v2.0
- ISO 8000 (Data Quality)
- ISO 23247 (Digital Twin)
- OPC UA Part 1–14

---

## 11. Version History

| Version | Date | Change |
|---------|------|--------|
| v1.0-locked | 2026-04-06 | Initial release — resource model, URI scheme, interaction verbs locked |
