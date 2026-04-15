# LC02 — System Requirements (NN-96 Traceability / DPP / Ledger · 96-00-general)

System-level requirements for **NN_96 Traceability / Digital Product Passport / Ledger** within the GAIA programme.

## Scope

This lifecycle-phase folder captures baselined requirements for:

- DPP canonical data schema and field set (mandatory / optional classification)
- Ledger throughput, latency, and data-integrity requirements
- Component provenance data-capture points and mandatory attestation fields
- Cross-domain API contract requirements traced to the AGGIX URI scheme

## Files

| File | KNU | Description |
|------|-----|-------------|
| `DPP_SCHEMA_REQUIREMENTS.yaml` | KNU-GAIA-DPP-96-REQ-001 | DPP schema field set with mandatory/optional classification — primary deliverable for KNOT-GAIA-DPP-96-001 |

## Traceability

| KNU ID | KNOT | Acceptance Criteria | Status |
|--------|------|---------------------|--------|
| KNU-GAIA-DPP-96-REQ-001 | KNOT-GAIA-DPP-96-001 | DPP schema field set baselined with mandatory/optional classification | BASELINED |
| KNU-GAIA-DPP-96-REQ-002 | KNOT-GAIA-DPP-96-002 | Ledger throughput latency and integrity requirements specified | PLANNED |
| KNU-GAIA-DPP-96-REQ-003 | KNOT-GAIA-DPP-96-003 | Provenance data capture points and mandatory attestation fields specified | PLANNED |
| KNU-GAIA-DPP-96-REQ-004 | KNOT-GAIA-DPP-96-005 | API contract requirements traced to AGGIX URI scheme and subsystem manifest | PLANNED |

## Dependencies

| Direction | Target | Rationale |
|-----------|--------|-----------|
| Up | LC01_PROBLEM_STATEMENT | Problem scope and KNOT definitions |
| Up | KNOT-GAIA-GOV-001 | Governance framework sets DPP mandatory fields |
| Down | LC04_DESIGN_DEFINITION | Requirements flow down to design |
| Down | LC06_VERIFICATION | Requirements are verified against test procedures |
| Across | LC03_SAFETY_RELIABILITY | Safety-critical fields feed FMEA |
| External | EU ESPR Regulation | Digital Product Passport regulatory baseline |
| External | ITAR/EAR | Export-control classification overlay |
