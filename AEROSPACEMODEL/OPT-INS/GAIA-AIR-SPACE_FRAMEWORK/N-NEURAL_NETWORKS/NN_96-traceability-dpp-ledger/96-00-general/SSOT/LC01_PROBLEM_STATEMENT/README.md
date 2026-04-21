# LC01 — Problem Statement (NN-96 Traceability / DPP / Ledger · 96-00-general)

Uncertainty orchestration for **NN_96 Traceability / Digital Product Passport / Ledger** at chapter level within the GAIA space station / habitat.

## Scope

DPP schema definition, traceability ledger architecture (SHA-256 hash chain), component provenance tracking, lifecycle event recording, cross-domain interoperability across GAIA subsystems, and audit & compliance reporting (ITAR/EAR export control, end-of-life circularity).

## Files

- `KNOTS.csv` — 6 seed KNOTs (DPP schema, ledger architecture, provenance, lifecycle events, interoperability, audit)
- `KNU_PLAN.csv` — 12 knowledge units with target locations under the chapter tree
- `TIMELINE.csv` — 6 chapter-level milestones
- `RACI.csv` — per-KNOT responsibilities
- `TOKENOMICS_TT.yaml` — 800 TT pool total across 6 KNOTs
- `AWARDS_TT.csv` — distribution ledger (populated at closure)

## Dependencies

| Direction | Target | Rationale |
|-----------|--------|-----------|
| Up | `KNOT-GAIA-MISS-001` | Mission class drives traceability depth & regulatory regime |
| Up | `KNOT-GAIA-GOV-001` | Governance framework sets DPP mandatory fields |
| Across | `NN_95` (AI/ML models) | Model provenance & versioning feed the DPP ledger |
| Across | `NN_98` (reserved program slot) | Future programme extensions may add DPP categories |
| Across | `SYS_*` (all subsystems) | Every subsystem produces parts requiring DPP entries |
| Across | `LC14_RETIREMENT_CIRCULARITY` | End-of-life DPP closure and recycling chain-of-custody |
| External | EU DPP Regulation (ESPR) | Digital Product Passport regulatory baseline |
| External | ITAR/EAR | Export-controlled DPP overlay for defence-adjacent items |
