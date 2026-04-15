---
schema_version: "1.0.0"
document_type: framework-index
document_id: AEROSPACEMODEL-ROBBBOT-OPT-IN-001
status: draft
last_updated: "2026-04-15"
---

# ROBBBO-T — OPT-IN Framework Instance

**Repo:** AEROSPACEMODEL · **Framework:** OPT-INS (OPT-IN + Space SIM) · **Product:** ROBBBO-T — Unmanned spacecraft

Mission lines: **COMMS**, **SAT**, **REPAIR**, **DEBRIS**. No crew onboard. Cert via ECSS, IADC debris mitigation, ITU (for COMMS).

## Topology (OPT-INS = 6 axes)

| Axis | Path |
|---|---|
| O-ORGANIZATIONS | [`O-ORGANIZATIONS/`](O-ORGANIZATIONS/) |
| P-PROGRAMS | [`P-PROGRAMS/`](P-PROGRAMS/) |
| T-TECHNOLOGIES_ON_BOARD_SYSTEMS | [`T-TECHNOLOGIES_ON_BOARD_SYSTEMS/`](T-TECHNOLOGIES_ON_BOARD_SYSTEMS/) |
| I-INFRASTRUCTURES | [`I-INFRASTRUCTURES/`](I-INFRASTRUCTURES/) |
| N-NEURAL_NETWORKS | [`N-NEURAL_NETWORKS/`](N-NEURAL_NETWORKS/) |
| **SPACE_SIM** | [`SPACE_SIM/`](SPACE_SIM/) — the explicit `S` of OPT-INS |

## Mission lines (product variants)

| Line | Scope | Path |
|---|---|---|
| COMMS  | Communication satellites and relay | [`MISSION_LINES/COMMS/`](MISSION_LINES/COMMS/)   |
| SAT    | General-purpose satellite buses    | [`MISSION_LINES/SAT/`](MISSION_LINES/SAT/)       |
| REPAIR | On-orbit servicing / refueling     | [`MISSION_LINES/REPAIR/`](MISSION_LINES/REPAIR/) |
| DEBRIS | Active debris removal              | [`MISSION_LINES/DEBRIS/`](MISSION_LINES/DEBRIS/) |

## Product-level LC01

See [`LC01_PROBLEM_STATEMENT/`](LC01_PROBLEM_STATEMENT/) — 7 seed KNOTs, **2,100 TT** reward pool.

| KNOT | Title | Pool |
|---|---|---|
| KNOT-RBT-AUTO-001    | Autonomy level per mission line             | 350 TT |
| KNOT-RBT-RPO-001     | Rendezvous & proximity operations envelope  | 350 TT |
| KNOT-RBT-CAPTURE-001 | Capture mechanism (arm/net/harpoon/magnet)  | 300 TT |
| KNOT-RBT-DEBRIS-001  | IADC debris mitigation compliance           | 300 TT |
| KNOT-RBT-COMMS-001   | ITU filing & frequency coordination         | 250 TT |
| KNOT-RBT-PROP-001    | Propulsion architecture per mission class   | 250 TT |
| KNOT-RBT-CYBER-001   | Uplink security & command authentication    | 300 TT |

## Related

- [OPT-INS wrapper](../../README.md)
- [AMPEL Family Taxonomy](../../../../AMPEL-FAMILY-TAXONOMY.md)
