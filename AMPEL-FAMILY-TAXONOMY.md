---
schema_version: "1.0.0"
document_type: taxonomy
document_id: AMPEL-FAM-TAX-001
status: consolidated baseline
last_updated: "2026-04-15"
scope: full product taxonomy — aerial and spatial domains
---

# AMPEL Family — Unified Taxonomy & Framework Naming

**Status:** consolidated baseline · **Date:** 2026-04-15 · **Scope:** full product taxonomy across aerial and spatial domains, with OPT-IN / OPT-INS framework naming rules.

---

## 1. Two Repositories

| Repository | Domain | Products |
|---|---|---|
| **AIRCRAFTMODEL** | Aerial (atmospheric, crewed aircraft) | AMPEL360-Q100 (two configurations: WTW, BWB) |
| **AEROSPACEMODEL** | Spatial (space) | AMPEL360-Q10, GAIA, ROBBBO-T |

---

## 2. Framework Naming Rule

| Domain | Framework name | Meaning |
|---|---|---|
| Aerial | **OPT-IN** | Base framework |
| Spatial | **OPT-INS** | **OPT-IN + S (Space SIM)** — the trailing S is the Space SIM qualifier, **not plural** |

`OPT-INS` is a single qualified framework name extending `OPT-IN` with space-simulation capability (orbital mechanics, vacuum/thermal, radiation, microgravity, RPO, reentry).

---

## 3. Designator Rule

"Q100", "Q10" are **quotient designators**, not passenger counts.

- **Q100** — the AMPEL360 aerial product quotient. Has two sibling configurations (WTW, BWB).
- **Q10** — the AMPEL360 spatial crewed-shuttle product quotient.

---

## 4. AIRCRAFTMODEL — Aerial Repository

### AMPEL360-Q100

One product, two sibling **configurations** sharing one OPT-IN framework instance.

| Configuration | Geometry | Key divergence drivers |
|---|---|---|
| **WTW** (Wing-Tube-Wing) | Conventional cylindrical fuselage + wing | Canonical ATA-53/57; conventional pressure vessel; under-wing/aft propulsor |
| **BWB** (Blended Wing Body) | Non-cylindrical centerbody + blended outer wing | Non-cylindrical pressure vessel; BLI propulsion; wide-cabin egress; coupled aeroelastics |

```
AIRCRAFTMODEL/
└── AMPEL360-Q100/
    ├── OPT-IN_FRAMEWORK/           # Shared across WTW & BWB (5-axis O/P/T/I/N)
    └── CONFIGURATIONS/
        ├── WTW/
        └── BWB/                    # Cross-links to the BWB specifics node
```

---

## 5. AEROSPACEMODEL — Spatial Repository

Three products, each with its own OPT-IN_FRAMEWORK instance, all grouped under the `OPT-INS/` Space SIM wrapper.

### 5.1 AMPEL360-Q10 — Crewed shuttle-type spacecraft

- **Mission:** space travel / space tourism
- **Regulatory anchor:** FAA AST 14 CFR Part 460; ECSS; NASA-STD-3001
- **Seed KNOTs:** MISS-001 mission class; LAUNCH-001 launch mode; TPS-001 thermal protection; ECLSS-001 loop closure; ABORT-001 crew escape; CERT-001 cert path; PAX-001 spaceflight-participant framework

### 5.2 GAIA — Space stations and habitats

- **Mission:** orbital / deep-space human habitation
- **Regulatory anchor:** ECSS-E/Q/M; NASA-STD-3001; ISS heritage
- **Seed KNOTs:** ORBIT-001 architecture; ECLSS-001 regenerative loop; RAD-001 radiation protection; MOD-001 docking/berthing standard; DUR-001 crew rotation; EVA-001 airlock architecture; CERT-001 human-rating path

### 5.3 ROBBBO-T — Unmanned platforms

- **Missions:** COMMS, SAT, REPAIR, DEBRIS
- **Regulatory anchor:** ECSS; IADC debris mitigation; ITU for comms
- **Seed KNOTs:** AUTO-001 autonomy level; RPO-001 proximity operations; CAPTURE-001 capture mechanism; DEBRIS-001 IADC compliance; COMMS-001 ITU filing; PROP-001 propulsion; CYBER-001 uplink security

```
AEROSPACEMODEL/
└── OPT-INS/                        # "OPT-IN + S (Space SIM)"
    ├── AMPEL360-Q10/OPT-IN_FRAMEWORK/
    ├── GAIA/OPT-IN_FRAMEWORK/
    └── ROBBBO-T/OPT-IN_FRAMEWORK/
```

---

## 6. Shared 5-Axis Topology

Every OPT-IN / OPT-INS instance carries the same five axes. Chapter IDs within the axes differ by domain:

| Axis | Aerial (Q100) chapter set | Spatial (Q10/GAIA/ROBBBO-T) chapter set |
|---|---|---|
| O-ORGANIZATIONS | ATA 00–05 | Mission-equivalent (ECSS-M) |
| P-PROGRAMS | ATA 06–12 | Mission-equivalent (ECSS-M) |
| T-TECHNOLOGIES_ON_BOARD_SYSTEMS | ATA 20–80 (full ATA iSpec 2200) | ECLSS, TPS, GNC, OMS/RCS, EVA, comms, power |
| I-INFRASTRUCTURES | Ground support, H₂ GSE, airport | Launch, range, recovery, ground segment |
| N-NEURAL_NETWORKS | Ledger, DPP, governance | Ledger, DPP, governance |

---

## 7. Corrections Applied (audit trail)

1. "Q100" and "Q10" are **quotient designators**, not passenger counts. (Earlier "Q10 ≈ 10 pax" inference was wrong.)
2. BWB and WTW are **sibling configurations of Q100**, not separate products.
3. Q10 is a **crewed space-travel shuttle**, not a smaller aircraft.
4. Q10 belongs to the **AEROSPACEMODEL** repo, not under the aircraft `CRAFT_CREWED/AMPEL/` path.
5. AMPEL family spans **two repositories**: AIRCRAFTMODEL (aerial) and AEROSPACEMODEL (spatial).
6. ROBBBO-T is **unmanned**.
7. **OPT-INS** is `OPT-IN + S (Space SIM)` — the S is a Space SIM qualifier, **not a plural**.

---

## 8. Open Decisions

- Whether to migrate the existing `OPT-IN_FRAMEWORK/I-INFRASTRUCTURES/AMPEL360/SPECIFICS/BWB/` node under `AIRCRAFTMODEL/AMPEL360-Q100/CONFIGURATIONS/BWB/`, or keep it at root and cross-link.
- Whether an aircraft-variant-numbering ladder exists below Q100 (Q90, Q110, etc.) that should reserve folder slots now.
- Whether GAIA and ROBBBO-T should share any infrastructure axis content (e.g., ground segment) via a family-level overlay.
