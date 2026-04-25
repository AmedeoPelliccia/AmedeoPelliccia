# UTA Domains — Index

**Unified Taxonomy of Artefacts (UTA) — Domain Index**

This document indexes the UTA domains used by the OPT-INS_FRAMEWORK / GQAOA
programme. Each domain owns a numeric range; sub-ranges within a domain may
be reserved for sector-specific taxonomies. UTA codes are **flat**: they are
identifiers, not filesystem paths. The flat layout is normative.

| Domain | Range | Name |
|--------|-------|------|
| G01 | 000–099 | Programme governance — foundational |
| G02 | 100–199 | Lifecycle artefacts |
| G05 | 400–499 | Federation surfaces |
| G07 | 600–699 | Evidence and ledger |
| G10 | 900–999 | Governance / Quantum-Computing Safety, Assurance, Authority |

---

## G10 / 900–999 — QCSAA

**Quantum-Computing Safety, Assurance, Authority (QCSAA)**

QCSAA occupies the sub-range **G10.970–G10.979** of the G10 domain. It indexes
entities whose operation requires explicit containment grammar, controlled
naming, and evidence-based state transitions.

### Lead Location and Jurisdictional Posture

| Aspect | Value |
|--------|-------|
| **Lead location** | Naples, Campania, Italy |
| **Lead jurisdiction** | Italy / European Union |
| **Regulatory posture** | Naples-led governance; apply applicable Naples municipal, Italian national, and European Union requirements jointly. Where requirements overlap, the **stricter** safety or containment control governs. |
| **Conflict rule** | Stricter control governs |
| **Enforcement authority** | STK-GOV |

The QCSAA range is operated under Naples-led governance. All artefacts in the
G10.970–G10.979 sub-range — registry, BREX, evidence packages, ledger entries —
inherit this posture. No municipal or national accommodation may weaken the
ESSA Safety-First baseline or any stricter applicable Italian or EU instrument.

### Normative artefacts

| File | Purpose |
|------|---------|
| [`GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md`](GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md) | G10.975 v0.2.0 containment grammar — six-state lattice, transition matrix, naming controls, quarantine exit, NIB disambiguation, LC01/KNOT mapping, evidence schema, BREX examples, enforcement authority, acceptance criteria |
| [`GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`](GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml) | QCSAA registry — entries G10.970 through G10.979 with permitted descriptive names, default containment states, owners, evidence pointers, KNOT references; prohibited-name list for controlled prohibition |
| [`GQAOA-UTA-G10-975-BREX-RULES-001.yaml`](GQAOA-UTA-G10-975-BREX-RULES-001.yaml) | BREX rules implementing G10.975 — containment metadata, naming controls, state transitions, evidence sufficiency, quarantine exit, regency escalation, LC01/KNOT mapping, ledger gates, stale-path rejection |
| [`../schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml) | Signed YAML schema for G10.975 Evidence Packages |
| [`../tools/validators/validate_g10_975.py`](../tools/validators/validate_g10_975.py) | Validator enforcing required files, flat layout, v0.2.0 spec semantics, schema presence, containment states, transition/quarantine controls, registry/BREX coverage, interpretive-note requirements, prohibited-name boundaries, and stale-path rejection |

### Flat layout (normative)

UTA codes are **flat identifiers**, not filesystem paths. All G10/QCSAA
artefacts SHALL live directly in `OPT-INS_FRAMEWORK/` (this directory) or in
the canonical `schemas/` and `tools/validators/` locations. The following
references are **stale and rejected** by the validator:

- `G10-QCSAA/` (folder-form)
- `G109` (truncated code)
- `G10/QCSAA/` (nested layout)

### Code mapping (informative — normative in the registry)

| Code | Permitted descriptive name |
|------|----------------------------|
| G10.970 | QCSAA Range Anchor |
| G10.971 | Zero-Gene Generative Agents (ZGGA) |
| G10.972 | Coherence-Lattice Inference Surfaces |
| G10.973 | Topological Evidence Reasoners |
| G10.974 | Persistent-Homology Decision Aids |
| G10.975 | Containment Grammar (meta-entry) |
| G10.976 | Quantum-Augmented Adjudication Surfaces |
| G10.977 | Coherence-Window Safety Monitors |
| G10.978 | Regency Authority Specification |
| G10.979 | Federation Conformance Surfaces |

---

*UTA domains index — Naples-led G10/QCSAA, jurisdictionally layered Italian / EU, stricter control governs.*
