---
schema_version: "1.0.0"
document_type: framework-wrapper-index
document_id: AEROSPACEMODEL-OPT-INS-001
status: draft
last_updated: "2026-04-15"
---

# OPT-INS — Space SIM Framework Wrapper

> **OPT-INS** = **OPT-IN + S (Space SIM)**
>
> The trailing **S** is the Space SIM qualifier, **not** a plural.
> OPT-INS extends the base OPT-IN framework with space-simulation capability:
> orbital mechanics, vacuum/thermal, radiation, microgravity, RPO, reentry.

## Products

Three products, each with its own OPT-IN_FRAMEWORK instance inside this OPT-INS wrapper:

| Product | Type | Mission |
|---------|------|---------|
| **AMPEL360-Q10** | Crewed shuttle-type spacecraft | Space travel / space tourism |
| **GAIA** | Space stations and habitats | Orbital / deep-space human habitation |
| **ROBBBO-T** | Unmanned platforms | COMMS, SAT, REPAIR, DEBRIS |

## Directory Layout

```
OPT-INS/
├── AMPEL360-Q10/
│   └── OPT-IN_FRAMEWORK/
├── GAIA/
│   └── OPT-IN_FRAMEWORK/
└── ROBBBO-T/
    └── OPT-IN_FRAMEWORK/
```

## Shared 5-Axis Topology (Spatial Chapter Set)

| Axis | Spatial Chapter Set |
|------|---------------------|
| **O** — Organizations | Mission-equivalent (ECSS-M) |
| **P** — Programs | Mission-equivalent (ECSS-M) |
| **T** — Technologies / On-Board Systems | ECLSS, TPS, GNC, OMS/RCS, EVA, comms, power |
| **I** — Infrastructures | Launch, range, recovery, ground segment |
| **N** — Neural Networks | Ledger, DPP, governance |

## Related

- [AMPEL Family Taxonomy](../../AMPEL-FAMILY-TAXONOMY.md)
- [AEROSPACEMODEL root](../README.md)
- [AIRCRAFTMODEL (aerial domain)](../../AIRCRAFTMODEL/README.md)
