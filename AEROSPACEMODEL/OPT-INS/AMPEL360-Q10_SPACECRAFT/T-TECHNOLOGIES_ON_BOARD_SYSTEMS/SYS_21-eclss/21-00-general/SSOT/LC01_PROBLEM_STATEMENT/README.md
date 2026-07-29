# LC01 — Problem Statement (SYS-21 ECLSS · 21-00-general)

Uncertainty orchestration for **SYS_21 Environmental Control & Life Support** at chapter level within the Q10 crewed space-tourism shuttle.

## Scope

Atmosphere composition, CO₂ removal, humidity management, cabin pressure integrity, consumables sizing, and emergency response modes for all mission duration classes.

## Files

- `KNOTS.csv` — 6 seed KNOTs (atmosphere, CO₂ removal, humidity, pressure, consumables, emergency)
- `KNU_PLAN.csv` — 12 knowledge units with target locations under the chapter tree
- `TIMELINE.csv` — 6 chapter-level milestones
- `RACI.csv` — per-KNOT responsibilities
- `TOKENOMICS_TT.yaml` — 800 TT pool total across 6 KNOTs
- `AWARDS_TT.csv` — distribution ledger (populated at closure)

## Dependencies

| Direction | Target | Rationale |
|-----------|--------|-----------|
| Up | `KNOT-Q10-MISS-001` | Mission class drives duration & orbit |
| Up | `KNOT-Q10-ECLSS-001` | Product-level loop-closure decision |
| Across | `SYS_52` (hatches) | Pressure boundary & leak paths |
| Across | `SYS_53` (pressure boundary / structural shell) | Cabin pressure integrity depends on the structural pressure vessel |
| Across | `SYS_30` (thermal) | Heat rejection for ECLSS equipment |
| Across | `SYS_35` (breathing gas) | O₂ supply & EVA pre-breathe |
| Across | `SYS_28` (propellant) | Consumables sizing and emergency constraints vary with mission propellant profile |
| Across | `SYS_26` (fire) | Atmosphere inerting & detection |
| Across | `SYS_25` (crew) | Metabolic loads & accommodation |
