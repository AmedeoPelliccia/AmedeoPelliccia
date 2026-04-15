---
schema_version: "1.0.0"
document_type: framework-index
document_id: AIRCRAFTMODEL-Q100-OPT-IN-001
status: draft
last_updated: "2026-04-15"
---

# AMPEL360-Q100 — OPT-IN Framework (singular, AERIAL)

One framework instance shared across Q100 configurations (WTW, BWB).

## Axes

- `O-ORGANIZATIONS/` — ATA 00–05 (6 chapters)
- `P-PROGRAMS/` — ATA 06–12 (7 chapters)
- `T-TECHNOLOGIES_ON_BOARD_SYSTEMS/` — 14 sub-axes, 49 ATA chapters
- `I-INFRASTRUCTURES/` — 6 chapters (support/H2 GSE/facilities)
- `N-NEURAL_NETWORKS/` — 2 chapters (ledger, program slot)

**Total: 70 chapters**, each with seed subject `XX-00-general` carrying SSOT (LC01–LC14) + PUB/AMM/CSDB+EXPORT+IETP.

## Product-level LC01

See [`LC01_PROBLEM_STATEMENT/`](LC01_PROBLEM_STATEMENT/).

## Five Axes

| Axis | Scope | Aerial Chapter Set |
|------|-------|--------------------|
| **O** — Organizations | Organisational structure, roles, responsibilities | ATA 00–05 |
| **P** — Programs | Programme management, scheduling, lifecycle | ATA 06–12 |
| **T** — Technologies / On-Board Systems | All on-board systems and technologies | ATA 20–80 (full ATA iSpec 2200) |
| **I** — Infrastructures | Ground support, hydrogen ground-support equipment, airport | Ground support, H₂ GSE, airport |
| **N** — Neural Networks | Digital ledger, DPP, governance AI | Ledger, DPP, governance |

## Designator

**Q100** is a **quotient designator**, not a passenger count.

## Configurations

- **WTW** (Wing-Tube-Wing)
- **BWB** (Blended Wing Body)

Configuration-specific content lives under `../CONFIGURATIONS/WTW/` and `../CONFIGURATIONS/BWB/`.
