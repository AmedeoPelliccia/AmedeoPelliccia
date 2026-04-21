---
schema_version: "1.0.0"
document_type: repository-index
document_id: AEROSPACEMODEL-IDX-001
status: draft
last_updated: "2026-04-15"
---

# AEROSPACEMODEL — Spatial Domain Repository

> Space products governed by the **OPT-INS** (OPT-IN + S for Space SIM) framework.

## Products

| Product | Type | Mission |
|---------|------|---------|
| **AMPEL360-Q10** | Crewed shuttle-type spacecraft | Space travel / space tourism |
| **GAIA** | Space stations and habitats | Orbital / deep-space human habitation |
| **ROBBBO-T** | Unmanned platforms | COMMS, SAT, REPAIR, DEBRIS |

## Directory Layout

```
AEROSPACEMODEL/
├── MCC/                              # Multi-Channel Cryptographic Composition
└── OPT-INS/                          # "OPT-IN + S (Space SIM)" wrapper
    ├── AMPEL360-Q10/OPT-IN_FRAMEWORK/
    ├── GAIA/OPT-IN_FRAMEWORK/
    └── ROBBBO-T/OPT-IN_FRAMEWORK/
```

## Framework

All spatial products use **OPT-INS** — the OPT-IN base framework extended with the Space SIM qualifier (orbital mechanics, vacuum/thermal, radiation, microgravity, RPO, reentry). The trailing **S** is a qualifier, **not** a plural.

Each product has its own OPT-IN_FRAMEWORK instance inside the OPT-INS wrapper.

## Related Documents

- [AMPEL Family Taxonomy](../AMPEL-FAMILY-TAXONOMY.md)
- [OPT-INS Framework Wrapper](OPT-INS/README.md)
- [AIRCRAFTMODEL (aerial domain)](../AIRCRAFTMODEL/README.md)
- [MCC Specification Series](MCC/README.md)
