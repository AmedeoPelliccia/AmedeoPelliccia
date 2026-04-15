---
schema_version: "1.0.0"
document_type: framework-index
document_id: AEROSPACEMODEL-GAIA-OPT-IN-001
status: draft
last_updated: "2026-04-15"
---

# GAIA — OPT-IN Framework Instance

**Repo:** AEROSPACEMODEL · **Framework:** OPT-INS (OPT-IN + Space SIM) · **Product:** GAIA — Space stations & habitats

Long-duration orbital / deep-space crewed habitation. Regulatory anchors: ECSS-E/Q/M, NASA-STD-3001, ISS heritage, IDSS for docking.

## 6-axis topology

| Axis | Chapters | Scope |
|------|----------|-------|
| `O-ORGANIZATIONS/` | 6 | Policy & org |
| `P-PROGRAMS/` | 7 | Dimensions, handling, servicing |
| `T-TECHNOLOGIES_ON_BOARD_SYSTEMS/` | 27 | ECLSS, GNC, power, EVA, comms, radiation, robotics, etc. |
| `I-INFRASTRUCTURES/` | 6 | Ground support, launch, MCC, EVA training, logistics |
| `N-NEURAL_NETWORKS/` | 2 | Traceability / DPP / ledger, program slot |
| `S-SPACE_SIMULATIONS/` | 6 | Orbital mechanics, vacuum/thermal, radiation, microgravity, RPO, reentry |

Total: **54 chapters**, each with one seed subject `XX-00-general` carrying SSOT (LC01–LC14) and PUB/AMM/CSDB+EXPORT+IETP.

## Product-level LC01

See [`LC01_PROBLEM_STATEMENT/`](LC01_PROBLEM_STATEMENT/) for 7 seed KNOTs and 2,000 TT reward pool.

| KNOT | Title | Pool |
|---|---|---|
| KNOT-GAIA-ORBIT-001 | Target orbit & architecture (LEO / GEO / cislunar / Lagrange) | 300 TT |
| KNOT-GAIA-ECLSS-001 | Regenerative loop closure % | 400 TT |
| KNOT-GAIA-RAD-001 | Radiation protection & storm shelter | 300 TT |
| KNOT-GAIA-MOD-001 | Module & docking standard (IDSS / CBM) | 250 TT |
| KNOT-GAIA-DUR-001 | Crew rotation cadence & long-duration HF | 250 TT |
| KNOT-GAIA-EVA-001 | EVA cadence & airlock architecture | 250 TT |
| KNOT-GAIA-CERT-001 | Human-rating certification path | 250 TT |

## Related

- [OPT-INS wrapper](../../README.md)
- [AMPEL Family Taxonomy](../../../../AMPEL-FAMILY-TAXONOMY.md)
