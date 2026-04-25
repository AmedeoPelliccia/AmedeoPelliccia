---
schema_version: "1.0.0"
document_type: repository-index
document_id: AIRCRAFTMODEL-IDX-001
status: draft
last_updated: "2026-04-15"
---

# AIRCRAFTMODEL — Aerial Domain Repository

> Atmospheric, crewed-aircraft products governed by the **OPT-IN** framework.

## Products

| Product | Quotient | Description |
|---------|----------|-------------|
| **AMPEL360-Q100** | Q100 | Hydrogen-electric aircraft — two sibling configurations (WTW, BWB) |

## Directory Layout

```
AIRCRAFTMODEL/
└── AMPEL360-Q100/
    ├── OPT-IN_FRAMEWORK/       # Shared 5-axis framework (O/P/T/I/N)
    └── CONFIGURATIONS/
        ├── WTW/                # Wing-Tube-Wing configuration
        └── BWB/                # Blended Wing Body configuration
```

## Framework

All products in this repository use the **OPT-IN** base framework. The five axes are:

| Axis | Chapter Set |
|------|-------------|
| **O** — Organizations | ATA 00–05 |
| **P** — Programs | ATA 06–12 |
| **T** — Technologies / On-Board Systems | ATA 20–80 (full ATA iSpec 2200) |
| **I** — Infrastructures | Ground support, H₂ GSE, airport |
| **N** — Neural Networks | Ledger, DPP, governance |

## Related Documents

- [AMPEL Family Taxonomy](../AMPEL-FAMILY-TAXONOMY.md)
- [ESSA AMPEL360-Q100 Profile](../ESSA/AMPEL360-Q100.md)
- [AEROSPACEMODEL (spatial domain)](../AEROSPACEMODEL/README.md)
