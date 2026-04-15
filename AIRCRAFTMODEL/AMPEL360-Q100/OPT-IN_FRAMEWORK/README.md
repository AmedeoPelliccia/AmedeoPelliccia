---
schema_version: "1.0.0"
document_type: framework-index
document_id: AIRCRAFTMODEL-Q100-OPT-IN-001
status: draft
last_updated: "2026-04-15"
---

# OPT-IN Framework — AMPEL360-Q100

> Shared 5-axis framework instance for the AMPEL360-Q100 aerial product.
> Both sibling configurations (WTW and BWB) share this single OPT-IN instance.

## Five Axes

| Axis | Scope | Aerial Chapter Set |
|------|-------|--------------------|
| **O** — Organizations | Organisational structure, roles, responsibilities | ATA 00–05 |
| **P** — Programs | Programme management, scheduling, lifecycle | ATA 06–12 |
| **T** — Technologies / On-Board Systems | All on-board systems and technologies | ATA 20–80 (full ATA iSpec 2200) |
| **I** — Infrastructures | Ground support, hydrogen ground-support equipment, airport | Ground support, H₂ GSE, airport |
| **N** — Neural Networks | Digital ledger, DPP, governance AI | Ledger, DPP, governance |

## Designator

**Q100** is a **quotient designator**, not a passenger count. It identifies the AMPEL360 aerial product quotient.

## Configurations

This framework is shared by two sibling configurations:

- **WTW** (Wing-Tube-Wing) — conventional cylindrical fuselage + wing geometry
- **BWB** (Blended Wing Body) — non-cylindrical centerbody + blended outer wing geometry

Configuration-specific content lives under `../CONFIGURATIONS/WTW/` and `../CONFIGURATIONS/BWB/`.

## Regulatory Alignment

- **CS-25 / Part-25** — primary airworthiness standard
- **Part-21** — Design Organisation Approval (DOA)
- **DO-178C / DO-254** — software and hardware assurance

## Related

- [AMPEL Family Taxonomy](../../../AMPEL-FAMILY-TAXONOMY.md)
- [ESSA AMPEL360-Q100 Profile](../../../ESSA/AMPEL360-Q100.md)
