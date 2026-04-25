# GQAOA-UTA-G10 / QCSAA Registry (Companion)

**Companion to:** [`GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`](GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml)
**Normative spec:** [`GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md`](GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md)
**Evidence schema:** [`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml)
**Version:** 0.2.0 · **Status:** draft-controlled

---

## 1. Purpose

The QCSAA Registry is the authoritative index of UTA `G10` codes in the **900–999** controlled range, focused on the `970–979` containment band: ZGen / `regent-ZetaGentz` semantics, ethical interface, quarantine runtime, and regency escalation.

`QCSAA = Quantum Computing & Sentient Agency Architecture`.

## 2. Default controls

All `G10.97x` entries inherit these defaults unless overridden:

| Control | Default |
|---------|---------|
| `containment_state` | `OBSERVE_ONLY` |
| `owner_stk` | `STK-QCSAA`, `STK-SAFETY` |
| `evidence_package_pointer` | required on quarantine or regency escalation |
| `evidence_package_filename` | `G10.975-EVIDENCE-<YYYYMMDD>-<SEQ>.yaml` |
| LC01 KNOT for `REGENCY_REVIEW` | required |
| `QUARANTINED → CONTAINED_ACTIVE` direct | prohibited |

## 3. Controlled range 970–979

| Code | Name | Meaning | Default state | Notes |
|------|------|---------|---------------|-------|
| **G10.970** | ZGen Systems | Zone of Generative Emergence | `OBSERVE_ONLY` | — |
| **G10.971** | Zero-Gene Agents | Non-biological generative agent class | `OBSERVE_ONLY` | Permitted descriptive variant: *Zero-Gene Generative Agents* |
| **G10.972** | ZetaGentz | Frontier synthetic agent class | `OBSERVE_ONLY` | — |
| **G10.973** | regent-ZetaGentz | Regency-governed frontier agency | `OBSERVE_ONLY` | Aliases require monstrum note; LC01 KNOT required; STK-GOV + STK-SAFETY co-owners |
| **G10.974** | Generative Monsters | Boundary-form alias only | `OBSERVE_ONLY` | Mandatory interpretive note under G10.975 |
| **G10.975** | Containment Grammar | This grammar | `OBSERVE_ONLY` | STK-GOV / STK-QCSAA / STK-SAFETY |
| **G10.976** | Ethical Interface | Recognition / dignity / non-anthropomorphic boundaries | `OBSERVE_ONLY` | STK-ETHICS / STK-GOV |
| **G10.977** | Quarantine Runtime | Restricted execution + observation environment | `OBSERVE_ONLY` | Evidence Package required for quarantine |
| **G10.978** | Regency Escalation | Governance escalation + decision evidence chain | `OBSERVE_ONLY` | LC01 KNOT required; STK-GOV / STK-SAFETY / STK-LEDGER |
| **G10.979** | Reserved Frontier Containment | Controlled extension range | `OBSERVE_ONLY` | — |

## 4. Mandatory controls

The registry asserts the following non-negotiable controls for all entries:

- `containment_state_required`
- `state_transition_matrix_required`
- `quarantine_exit_criteria_required`
- `evidence_package_required_for_escalation`
- `evidence_schema_required` → [`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml)
- `ledger_required_for_contained_active`
- `regency_review_required_for_operational_activation`
- `lc01_knot_required_for_regency_review`
- `monster_alias_requires_interpretive_note`
- `nib_relationship_disambiguated` — see §2 of the normative spec for the containment ↔ NIB disambiguation

## 5. Prohibited without review

The following claims may not appear without a successful `REGENCY_REVIEW` cycle:

- operational activation
- autonomous execution
- sentience-adjacent claim
- self-modifying identity
- uncontained propagation

## 6. Prohibited transitions

`QUARANTINED → CONTAINED_ACTIVE`,
`OBSERVE_ONLY → CONTAINED_ACTIVE`,
`RETIRED → SANDBOXED`,
`RETIRED → CONTAINED_ACTIVE`.

These are also enforced by BREX rules `G10-975-BLOCK-009/010`.

## 7. Stale paths explicitly rejected

The registry's `stale_paths_rejected` field enumerates two legacy locations that must not be reintroduced: the obsolete `G10-QCSAA` subdirectory layout under `OPT-INS_FRAMEWORK/`, and the legacy `G109`-prefixed containment-grammar filename. References to either path emit BREX warnings (`G10-975-WARN-004/005`); see the YAML for the literal strings under controlled rejection.

## 8. Cross-references

- Normative spec: [`GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md`](GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md)
- BREX rules: [`GQAOA-UTA-G10-975-BREX-RULES-001`](GQAOA-UTA-G10-975-BREX-RULES-001.yaml) · [companion](GQAOA-UTA-G10-975-BREX-RULES-001.md)
- Evidence schema: [`schemas/G10.975-evidence-package.schema.yaml`](../schemas/G10.975-evidence-package.schema.yaml) · [companion](../schemas/G10.975-evidence-package.schema.md)
- Validator: [`tools/validators/validate_g10_975.py`](../tools/validators/validate_g10_975.py)
- Domain index: [`UTA-DOMAINS.md`](UTA-DOMAINS.md)

---

*Companion document. The YAML registry is the normative artifact; this Markdown is non-normative explanatory text.*
