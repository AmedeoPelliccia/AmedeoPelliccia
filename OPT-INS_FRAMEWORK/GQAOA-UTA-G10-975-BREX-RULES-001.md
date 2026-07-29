# GQAOA-UTA-G10-975 — BREX Rules (Companion)

**Companion to:** [`GQAOA-UTA-G10-975-BREX-RULES-001.yaml`](GQAOA-UTA-G10-975-BREX-RULES-001.yaml)
**Normative spec:** [`GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md`](GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md)
**Evidence schema:** [`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml)
**Version:** 0.2.0 · **Status:** draft-controlled

---

## 1. Purpose

The BREX (Business Rules Exchange) ruleset operationalizes the G10.975 containment grammar. It is the machine-checkable form of §3, §5, §7, §8, §9, §11, and §12 of the normative specification, applied to every artifact in the `G10.970`–`G10.979` range and to any document referencing `ZGen`, `regent-ZetaGentz`, or "Zero-Gene Generative Agents".

The rules are consumed by the validator
[`tools/validators/validate_g10_975.py`](../tools/validators/validate_g10_975.py)
and by downstream conformance gates.

## 2. Mandatory metadata

Every controlled document must declare:

- `g10_containment.range` ∈ `G10.970-G10.979`
- `g10_containment.containment_state` from the six-state enum
- `g10_containment.evidence_required: true`
- a pointer to the [evidence schema](../schemas/G10.975-evidence-package.schema.yaml) and the normative spec

Default state is `OBSERVE_ONLY`. `zgen_semantics: true` flags documents using ZGen vocabulary.

## 3. State transition matrix

The YAML enumerates **permitted** and **prohibited** transitions among the six states (`OBSERVE_ONLY`, `SANDBOXED`, `QUARANTINED`, `REGENCY_REVIEW`, `CONTAINED_ACTIVE`, `RETIRED`). Each permitted edge declares its required authority (STK roles) and required evidence.

Key invariants enforced:

- `QUARANTINED → CONTAINED_ACTIVE` is **never** direct; `REGENCY_REVIEW` must intervene.
- `OBSERVE_ONLY → CONTAINED_ACTIVE` is forbidden.
- `RETIRED → OBSERVE_ONLY` is allowed *conditionally* (rehabilitation path) and requires both `STK-GOV` and `STK-SAFETY` plus a supersession rationale.

## 4. Quarantine exit criteria (`QE-001 … QE-010`)

Lifting `QUARANTINED` requires all ten `QE-*` items to be satisfied — including hash-captured sources, removal of prohibited terminology, the mandatory monstrum interpretive note for any Monster alias, documented residual risk, and a fresh ledger anchor before release. `STK-SAFETY` approves the exit; `STK-GOV` approves the resulting state.

## 5. LC01 / KNOT mapping

Every entity in `REGENCY_REVIEW` must map to an LC01 KNOT entry:

`KNOT-G10.97x-<NORMALIZED-ENTITY-NAME>-<SEQ>`

with the required fields listed in `lc01_knot_mapping.required_fields`. This welds containment review into the GQAOA uncertainty register rather than letting it float as a parallel track.

## 6. Blocking rules (`G10-975-BLOCK-001 … 011`)

These cause hard `FAIL` in validation:

| Rule | Trigger |
|------|---------|
| BLOCK-001 | Missing containment metadata in a `G10.970`–`G10.979` document |
| BLOCK-002 | "Monster" / "Generative Monsters" appears without the monstrum interpretive note |
| BLOCK-003 | Entity declared operational without an Evidence Package |
| BLOCK-004 | Sentience-adjacent claim outside `REGENCY_REVIEW` |
| BLOCK-005 | Prohibited name outside a controlled-prohibition context |
| BLOCK-006 | Quarantine trigger without escalation record |
| BLOCK-007 | `CONTAINED_ACTIVE` missing `ledger.anchor_id`, `evidence_package.id`, or `decision.value` |
| BLOCK-008 | `regent-ZetaGentz` used outside the `G10.970`–`G10.979` context |
| BLOCK-009 | State transition not in the permitted matrix |
| BLOCK-010 | Direct `QUARANTINED → CONTAINED_ACTIVE` |
| BLOCK-011 | `REGENCY_REVIEW` entity without LC01 KNOT mapping |

## 7. Warning rules (`G10-975-WARN-001 … 005`)

Soft signals: ZGen alias without QCSAA reference, boundary-form terminology in public-facing text, ethical-interface terms without `G10.976` reference, and references to the known stale paths enumerated in `stale_paths_rejected` of the registry (the legacy `G10-QCSAA` directory layout and the `G109` filename variant).

## 8. Name policy

- `permitted_formal_names` — usable without further note.
- `permitted_aliases_with_note` — usable only when accompanied by the §4.3 monstrum interpretive note.
- `prohibited_terms` — usable **only** in controlled-prohibition contexts (BLOCK-005).

## 9. Cross-references

- Normative spec: [`GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md`](GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md)
- Registry: [`GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`](GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml)
- Evidence schema: [`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml)
- Validator: [`tools/validators/validate_g10_975.py`](../tools/validators/validate_g10_975.py)
- Domain index: [`UTA-DOMAINS.md`](UTA-DOMAINS.md)

---

*Companion document. The YAML rules file is the normative artifact; this Markdown is non-normative explanatory text.*
