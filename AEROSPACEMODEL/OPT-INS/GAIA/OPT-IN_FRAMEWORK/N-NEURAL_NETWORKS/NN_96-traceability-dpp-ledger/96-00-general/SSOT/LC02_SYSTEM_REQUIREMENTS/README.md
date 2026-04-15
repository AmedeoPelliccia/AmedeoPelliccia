# LC02 — System Requirements (NN-96 Traceability / DPP / Ledger · 96-00-general)

System-level requirements for **NN_96 Traceability / Digital Product Passport / Ledger** within the GAIA space station / habitat.

## Scope

Throughput, latency, data-integrity, provenance-capture, and API-contract requirements for the DPP ledger subsystem — covering DPP schema fields, ledger architecture (SHA-256 hash-chain / DAG), component provenance tracking, and cross-domain interoperability via the AGGIX URI scheme.

## Files

- `KNOTS.csv` — 4 requirement-bearing KNOTs (DPP schema, ledger architecture, provenance, interoperability)
- `KNU_PLAN.csv` — 4 REQ-type knowledge units with acceptance criteria and verification methods
- `TIMELINE.csv` — 4 requirement-review milestones
- `RACI.csv` — per-KNOT requirement responsibilities
- `TOKENOMICS_TT.yaml` — 550 TT pool total across 4 REQ KNUs
- `AWARDS_TT.csv` — distribution ledger (populated at closure)

## Dependencies

| Direction | Target | Rationale |
|-----------|--------|-----------|
| Up | `LC01_PROBLEM_STATEMENT` | Problem definitions and KNOT registry drive requirement derivation |
| Down | `LC04_DESIGN_DEFINITION` | Requirements flow down into design definitions |
| Down | `LC06_VERIFICATION` | Each requirement traces to a verification method |
| Across | `LC03_SAFETY_RELIABILITY` | Safety/FMEA findings feed back into requirement updates |
| Across | `LC05_ANALYSIS_MODELS` | Trade-study results (hash-chain vs DAG) refine performance requirements |
| External | EU DPP Regulation (ESPR) | Regulatory baseline for mandatory DPP fields |
| External | ITAR/EAR | Export-control overlay requirements |
