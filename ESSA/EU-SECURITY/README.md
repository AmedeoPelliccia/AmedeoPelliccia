# EU-SECURITY

**Minimum Common Security Constitution (MCSC)**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-SEC-MCSC-001 |
| **Version** | v0.1-draft |
| **Status** | Draft |
| **Parent** | ESSA Constitutional Root Document |
| **Path** | `ESSA/EU-SECURITY/INTEGRATIONS` |
| **Nature** | Security Overlay — not a parallel lifecycle |

---

## 1. Purpose

EU-SECURITY defines the **Minimum Common Security Constitution (MCSC)**: the set of ethical and resilience invariants that **SHALL** apply across all lifecycle domains governed by ESSA.

EU-SECURITY is **not** combat doctrine.
EU-SECURITY is **not** a parallel lifecycle.

EU-SECURITY is a **regulatory abstraction layer** that extends CIVIL-PLATFORMS through machine-checkable control registries.

---

## 2. Scope

EU-SECURITY applies as an **overlay** to all ESSA lifecycle phases (P000–P120) and to all CIVIL-PLATFORMS implementations, including the space-based fork documented in [`../essa-regulatory-framework.yaml`](../essa-regulatory-framework.yaml).

Controls defined herein are referenced by token links of the form:

```yaml
links:
  - rel: verified_by
    target_token_id: MCSC-CTRL-<id>
```

Any token in any phase **MAY** link to EU-SECURITY controls.
Tokens in phases P020, P050, and P090 **SHALL** include at least one EU-SECURITY control link where applicable.

---

## 3. Minimum Common Security Constitution (MCSC)

The MCSC constitutes the non-negotiable floor for all governed lifecycle instances.

### 3.1 Ethical Invariants

| Control ID | Invariant | Enforcement Point |
|------------|-----------|-------------------|
| MCSC-ETH-01 | Traceable authority: every activation token **SHALL** carry a resolvable authority reference | CONFIRM gate |
| MCSC-ETH-02 | Human override path: every autonomous or AI-assisted decision **SHALL** have a defined human override procedure | CONFIRM gate |
| MCSC-ETH-03 | Non-maleficence: no token activation **SHALL** produce an output that degrades safety invariants without explicit authority approval | ACTIVATE gate |
| MCSC-ETH-04 | Transparent auditability: all state transitions **SHALL** be written to the Master Teknia Ledger (MTLdg) | All transitions |

### 3.2 Accountability Controls

| Control ID | Control | Enforcement Point |
|------------|---------|-------------------|
| MCSC-ACC-01 | Every lifecycle token **SHALL** carry an owner role (`owner_role`) and an authority signature | Token schema |
| MCSC-ACC-02 | Configuration changes **SHALL** be approved by a designated authority before ACTIVATE | CONFIRM gate |
| MCSC-ACC-03 | Occurrence reports (`OCC_REPORT`) **SHALL** be linked to root cause analysis within the defined review period | P080 |

### 3.3 Resilience Controls

| Control ID | Control | Enforcement Point |
|------------|---------|-------------------|
| MCSC-RES-01 | Each critical lifecycle phase **SHALL** have an associated Business Continuity Plan (BCP) token (`BCP_ITEM`) | P120 |
| MCSC-RES-02 | Recovery tests (`RECOVERY_TEST`) **SHALL** be executed and linked to the BCP at least once per baseline cycle | P120 |
| MCSC-RES-03 | No single-point-of-failure **SHALL** exist in the token activation chain for safety-critical phases | Architecture review |

### 3.4 Supply Chain Integrity

| Control ID | Control | Enforcement Point |
|------------|---------|-------------------|
| MCSC-SCI-01 | All chain nodes (`CHAIN_NODE`) in P030 **SHALL** carry provenance trace hooks (`TRACE_HOOK`) | P030 |
| MCSC-SCI-02 | Suppliers with access to safety-critical processes **SHALL** be assessed against MCSC-ETH-01 through MCSC-ETH-04 | P030 contracting |
| MCSC-SCI-03 | Third-party components **SHALL** include a conformity declaration (`CE_DECL` or equivalent) prior to ACTIVATE | P060 |

### 3.5 Human Oversight Boundaries

| Control ID | Control | Enforcement Point |
|------------|---------|-------------------|
| MCSC-HOB-01 | AI-generated artefacts **SHALL** be classified as `GENERATED` and require independent verification before certification | ANNEX-A lifecycle states |
| MCSC-HOB-02 | Generative tools **SHALL NOT** operate inside the execution boundary as defined in ANNEX-A | Architecture invariant |
| MCSC-HOB-03 | All safety-critical ACTIVATE transitions **SHALL** require human confirmation | CONFIRM → ACTIVATE gate |

### 3.6 Sovereign Interoperability

| Control ID | Control | Enforcement Point |
|------------|---------|-------------------|
| MCSC-SOV-01 | Lifecycle data **SHALL** be stored in sovereignty-compliant infrastructure aligned with EU data governance frameworks | Registry |
| MCSC-SOV-02 | Interoperability interfaces **SHALL** be documented and versioned as part of the token graph | Integration artefacts |
| MCSC-SOV-03 | Cross-border data exchanges **SHALL** respect EU cybersecurity baseline controls (aligned with Part-CYB-S) | P120 |

---

## 4. Integration with CIVIL-PLATFORMS

EU-SECURITY controls are exposed to CIVIL-PLATFORMS via the **INTEGRATIONS** registry.

Integration artefacts are documented in [`INTEGRATIONS/`](INTEGRATIONS/).

### 4.1 Control Linkage Pattern

Any CCTLS token **MAY** carry EU-SECURITY control references:

```yaml
links:
  - rel: verified_by
    target_token_id: MCSC-ETH-01
  - rel: verified_by
    target_token_id: MCSC-ACC-02
```

### 4.2 Mandatory Linkages by Phase

| Phase | Mandatory EU-SECURITY Controls |
|-------|-------------------------------|
| P020 | MCSC-ETH-03, MCSC-RES-01 |
| P050 | MCSC-ACC-02, MCSC-ETH-01 |
| P080 | MCSC-ACC-03, MCSC-SCI-01 |
| P090 | MCSC-HOB-03, MCSC-ETH-02 |
| P120 | All MCSC-RES-* controls |

---

## 5. Alignment with ALPC

ALPC certification evaluation **SHALL** include EU-SECURITY control coverage assessment:

- Completeness: all mandatory linkages per §4.2 **SHALL** be present
- Sufficiency: each referenced control **SHALL** have associated evidence token
- Coherence: control linkage graph **SHALL** be acyclic and authority-bound

---

## 6. Governance

EU-SECURITY controls are versioned independently of CCTLS phases.

Control registry updates **SHALL**:

1. Increment the `ESSA-SEC-MCSC-001` version
2. Be reviewed by the ESSA Constitutional Authority
3. Be linked to affected CCTLS phase packages via a `DIRECTIVE` token in P080

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`INTEGRATIONS/`](INTEGRATIONS/) | Integration artefacts linking EU-SECURITY controls to CIVIL-PLATFORMS token packages |
| [`../README.md`](../README.md) | ESSA Constitutional Root Document |
| [`../cctls.yaml`](../cctls.yaml) | CCTLS lifecycle standard (CIVIL-PLATFORMS branch) |
| [`../CCTLS.md`](../CCTLS.md) | Human-readable CCTLS specification |
| [`../essa-regulatory-framework.yaml`](../essa-regulatory-framework.yaml) | Space-based civil-platforms fork |
| [`../ANNEX-A-glossary.md`](../ANNEX-A-glossary.md) | NORMATIVE — MTL/MTLdg/DOF/lifecycle states glossary |
