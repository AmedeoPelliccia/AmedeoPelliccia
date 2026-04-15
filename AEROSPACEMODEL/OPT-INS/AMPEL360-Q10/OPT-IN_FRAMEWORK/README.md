---
schema_version: "1.0.0"
document_type: framework-index
document_id: AEROSPACEMODEL-Q10-OPT-IN-001
status: draft
last_updated: "2026-04-15"
---

# AMPEL360-Q10 — OPT-IN Framework (Space SIM context)

Q10 crewed space-tourism shuttle. Full 5-axis scaffold with spacecraft-adapted chapter set.

## Designator

**Q10** is a **quotient designator**, not a passenger count. It identifies the AMPEL360 spatial crewed-shuttle product quotient.

## Regulatory Anchor

- **FAA AST 14 CFR Part 460** — human spaceflight requirements
- **ECSS** — European Cooperation for Space Standardization
- **NASA-STD-3001** — crew health and performance standards

## Axes

| Axis | Chapters | Scope |
|------|----------|-------|
| `O-ORGANIZATIONS/` | 6 | Policy & org |
| `P-PROGRAMS/` | 7 | Dimensions, handling, servicing |
| `T-TECHNOLOGIES_ON_BOARD_SYSTEMS/` | 21 | ECLSS, GNC, TPS, Main Prop, OMS, RCS, Abort, Reentry, etc. |
| `I-INFRASTRUCTURES/` | 6 | Launch, range, recovery, ground segment, training, propellant |
| `N-NEURAL_NETWORKS/` | 2 | Traceability / DPP / ledger, program slot |

Total: **42 chapters**, each with one seed subject `XX-00-general` carrying SSOT (LC01–LC14) and PUB/AMM/CSDB+EXPORT+IETP.

## Product-level LC01

See [`LC01_PROBLEM_STATEMENT/`](LC01_PROBLEM_STATEMENT/) for 7 seed KNOTs and 2,100 TT reward pool.

## Seed KNOTs

| KNOT ID | Domain |
|---------|--------|
| MISS-001 | Mission class |
| LAUNCH-001 | Launch mode |
| TPS-001 | Thermal protection |
| ECLSS-001 | Loop closure |
| ABORT-001 | Crew escape |
| CERT-001 | Certification path |
| PAX-001 | Spaceflight-participant framework |

## Related

- [OPT-INS wrapper](../../README.md)
- [ESSA AMPEL360-Q10 Profile](../../../../ESSA/AMPEL360-Q10.md)
- [AMPEL Family Taxonomy](../../../../AMPEL-FAMILY-TAXONOMY.md)
