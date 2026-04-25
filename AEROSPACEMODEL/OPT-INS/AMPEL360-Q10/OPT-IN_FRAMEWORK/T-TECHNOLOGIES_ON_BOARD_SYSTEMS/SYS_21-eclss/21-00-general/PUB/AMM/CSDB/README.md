# CSDB — ATA 21-00 ECLSS (AMPEL360-Q10)

This `CSDB/` directory contains S1000D source structures for ATA 21-00 (`SYS_21-eclss/21-00-general/PUB/AMM`).

## Directory purpose

- `DM/` — Data Modules (procedural/descriptive content)
- `PM/` — Publication Modules
- `DML/` — Data Module List artifacts
- `BREX/` — Business rules exchange references
- `ICN/` — Information control numbers (illustrations/media metadata)
- `COMMON/` — Reusable/common CSDB components
- `APPLICABILITY/` — Applicability data modules (ACT/CCT-style effectivity control)

## DMC naming convention used

Example:

`DMC-AMPEL360Q10-A-21-00-00-00A-00WA-D_000-00_EN-US.xml`

Breakdown:

- `DMC` — Data Module Code prefix
- `AMPEL360Q10` — Model Identification Code (MIC)
- `A` — System difference code
- `21-00-00-00A` — ATA chapter/section breakdown for 21-00 scope
- `00WA` — Information code + variant (ACT-style applicability module)
- `D` — Item location code
- `_000-00` — Issue/in-work status
- `_EN-US` — Language (`en-US`)

## How to add new applicability data modules

1. Create a new XML file under `APPLICABILITY/` using the DMC pattern above.
2. Keep a complete `identAndStatusSection`:
   - `dmCode`, `language`, `issueInfo`, `issueDate`
   - `responsiblePartnerCompany` and originator metadata
3. Add ACT/CCT content with explicit effectivity dimensions:
   - model variant(s)
   - serial number range(s)
   - modification state (pre/post MOD)
4. Run local XML checks (`xmllint --noout`) before committing.

## Extending to other ATA chapters

Reuse the same pattern in sibling chapter CSDB paths (for example ATA 23, ATA 49), updating:

- ATA-coded DMC segments
- folder path chapter numbers
- applicability values (variants, serials, mods) for that system

## S1000D Issue 5.0 reference concepts

- **ACT** (Applicability Cross-reference Table): maps effectivity conditions to content usage.
- **CCT** (Condition Cross-reference Table): tracks condition statements referenced by applicability logic.
- **Effectivity**: defines where content applies (model, serial, modification, configuration).

## GitHub Actions validation

XML validation is automated by `.github/workflows/s1000d-schema-validation.yml`:

- triggers on XML changes under `AEROSPACEMODEL/`
- validates XML well-formedness with `xmllint --noout`
- optionally validates against XSDs placed in `AEROSPACEMODEL/schemas/`
