# PLUMA-GAI-NET — Stack Diagrams & Topological Network Graphics

**Document ID:** PLUMA-GAI-NET-DIAG-001  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** PLUMA-GAI-NET-001 ([pluma-gai-net.yaml](pluma-gai-net.yaml))  
**Related:** [`../H.I.V.md`](../H.I.V.md) · [`../TranshidreOHs.md`](../TranshidreOHs.md) · [`../VibidratAZIONE.md`](../VibidratAZIONE.md)  
**Last Updated:** 2026-04-02

---

## 1. PLUMA-GAI Canonical Stack

The canonical programme stack shows the three-layer PLUMA-GAI thread embedded
within the parent lifecycle architecture and feeding forward to the NET layer.

```mermaid
flowchart TB
    PG["PLUMA-GAI\nProgramme Lifecycle Governance\nPLUMA-GAI-001"]

    subgraph THREAD ["PLUMA-GAI Canonical Thread (TranshidreOHs → H.I.V. → VibidratAZIONE)"]
        direction TB
        TRH["TranshidreOHs\nMulti-Modal Carrier Layer\nLH₂ · GH₂ · Fibre-optic co-carry\nPLUMA-GAI-TRH-001"]
        HIV["H.I.V.\nHydrogen · Infrared · Values\nEnergy-Sense-Value Specification\nVSED packet · V-token · T_eff\nPLUMA-GAI-HIV-001"]
        VBZ["VibidratAZIONE\nOperational Restoration Actuator\nTeknia Token · Equity Injection\n310 K rehydration floor\nPLUMA-GAI-VBZ-001"]
        TRH -->|"HIV-IFC-001\nEnergy-Data Handshake\ncarrier package → VSED"| HIV
        HIV -->|"HIV-IFC-002\nOperational Trigger\nInfrared_Sensing < Threshold"| VBZ
        VBZ -->|"Closed loop\nrestored nodes → T_eff ↑"| TRH
    end

    NET["PLUMA-GAI NET\nGround–Aerospace IR Mesh\nPLUMA-GAI-NET-001"]

    PG --> THREAD
    THREAD --> NET
```

---

## 2. PLUMA-GAI-NET Layer Stack (L0–L5)

The six-layer NET architecture, with Layer 4 (Lifecycle Governance Binding) as
the novel element distinguishing this from a standard network stack.

```mermaid
flowchart TB
    L5["Layer 5 — Autonomy Interface\nAA-093 bounded connections\nSwarm / fleet coordination (GAIA)\nPre-loaded autonomy for blackout periods"]
    L4["Layer 4 — Lifecycle Governance Binding  ★ NOVEL\nPhase-gated link certification (P000–P100)\nEvidence-bound performance characterisation\nDOA authority for topology changes"]
    L3["Layer 3 — Deterministic Routing Map\nTrust-latency-aware ubiquitous map\nLatency-bounded path selection\nDegradation-aware re-routing"]
    L2["Layer 2 — Integrity & Security\nSHA3-512 · ECDSA-P384 minimum\nQKD optional overlay (ETSI GS QKD 014)\nInherits from AMP-GAI-CORE"]
    L1["Layer 1 — Link Protocol\nOptical modulation (PPM / DPSK / coherent)\nForward Error Correction (FEC)\nFrame sync and link establishment"]
    L0["Layer 0 — Physical\nIR emitters (NIR · SWIR · MWIR · LWIR)\nFocal plane arrays and detectors\nOptical terminals · Cryogenic sensors"]

    L5 --> L4 --> L3 --> L2 --> L1 --> L0
```

### IR Band Allocation (Layer 0)

```
  NIR   0.75–1.4 µm  ──── Short-range comms · acquisition/tracking
  SWIR  1.4–3.0 µm   ──── Ground-air comms · LH₂ leak detect (2.7 µm)
  MWIR  3.0–5.0 µm   ──── Cryo thermal mapping · exhaust imaging
  LWIR  8.0–14.0 µm  ──── RSP TPS supervision · structural hot-spots
```

---

## 3. Topological Network — Ground · Air · Space

The three-tier ubiquitous map node topology with link types and IR bands.

```mermaid
graph TB
    subgraph SPACE ["  SPACE  —  LEO / GEO  "]
        GAIA["GAIA\nQuantum · Satellite assets · UAS fleet\nNode type: space_compute"]
        SAT2["SAT-B\nConst. node n\nCrosslink"]
    end

    subgraph AIR ["  AIR  —  0–100 km  "]
        AMP["AMPEL360\nCivil LH₂ aviation · RSP\nNode type: vehicle"]
        UAS["UAS Fleet\nSwarm nodes\nNode type: uas"]
        RSP["RSP (ascent/re-entry)\nNode type: rsp_vehicle\n⚠ Plasma blackout risk"]
    end

    subgraph GROUND ["  GROUND  "]
        MCC["Mission Control Centre\nNode type: ground_mcc"]
        DC["Sovereign Data Centre\nNode type: ground_compute"]
        IR_GRID["IR Sensor Grid\nSWIR/MWIR ground arrays\nNode type: ground_sensor"]
        H2_INF["H₂ Infrastructure\nTranshidreOHs ground nodes\nNode type: ground_h2"]
    end

    GAIA <-->|"LEO crosslink\nNIR/SWIR optical\n≤300 ms · ≥500 Mbps"| SAT2
    GAIA <-->|"Space-ground optical\nNIR/SWIR\nFull nominal"| MCC
    GAIA <-->|"Advisory channel\nAMP-GAI-CORE\nSHA3-512 · QKD optional"| AMP
    AMP  <-->|"Air-ground optical\nSWIR/MWIR\n≤150 ms · ≥200 Mbps"| MCC
    AMP  <-->|"Swarm coordination\nNIR narrow-beam"| UAS
    RSP  <-->|"Pre-blackout handoff\n→ LOCAL_AMPEL_AUTONOMY"| AMP
    MCC  ---  DC
    MCC  ---  IR_GRID
    MCC  ---  H2_INF
    IR_GRID -.->|"Passive IR sensing\nSWIR/MWIR/LWIR"| AMP
    IR_GRID -.->|"Passive IR sensing"| RSP
    H2_INF -->|"HIV-IFC-001\ncarrier package"| AMP
```

### Ubiquitous Map Node Properties

Every node in the topology is characterised by four mandatory properties:

```
node_id          ── unique identifier (string)
geolocation_4d   ── lat · lon · alt_km · epoch_utc  (updated ≤ 1 s for safety nodes)
performance_envelope
  ├── latency_ms_max
  ├── bandwidth_mbps_min
  ├── jitter_ms_max
  └── trust_score      (0.0 – 1.0)
ir_emission_profile
  ├── band            (NIR / SWIR / MWIR / LWIR)
  └── t_eff_kelvin    ── physical ground truth; cannot be falsified
```

---

## 4. Event Boundary / Superconductor Vector Channel

Illustrates the transition from standard carrier mode to event-boundary
(superconductor vector) mode on HIV-IFC-001.

```mermaid
flowchart LR
    subgraph STD ["Standard Mode"]
        direction TB
        TRH_S["TranshidreOHs\nstandard carrier"]
        IFC_S["HIV-IFC-001\nboundary_mode = false\nR > 0 · loss > 0 · latency > 0"]
        TRH_S -->|"hydrogen_flow_rate_kg_s\nfiber_optic_throughput_gbps"| IFC_S
    end

    subgraph EB ["Event-Boundary Mode  ⚡ Superconductor Vector"]
        direction TB
        TRH_E["TranshidreOHs\n@ event boundary\nboundary_id · timestamp_utc\nenergy_state_hash · data_state_hash"]
        IFC_E["HIV-IFC-001\nboundary_mode = true\nR = 0 · loss = 0 · latency = 0"]
        HIV_E["H.I.V. input\ncarrier_state_hash → VSED\nT_eff → ∞  (by construction)"]
        TRH_E -->|"carrier_state_hash\n(replaces all flow fields)"| IFC_E
        IFC_E --> HIV_E
    end

    STD -.->|"compression\nto essentiality"| EB
```

**T_eff formula collapse at event boundary:**

```
Standard:   T_eff = (verified / total) × (1 / mean_latency_s)
Boundary:   T_eff = (verified / total) × lim(latency → 0) = ∞
```

INV-HIV-SV enforces: when `boundary_mode = true`, channel MUST carry
`carrier_state_hash` and MUST NOT carry individual flow fields.

---

## 5. Degradation State Machine

The four-state deterministic fallback doctrine for PLUMA-GAI NET.

```mermaid
stateDiagram-v2
    [*] --> FULL_NOMINAL : system startup / DOA recovery

    FULL_NOMINAL : FULL_NOMINAL (State 0)\nIR + Classical + QKD\nFull GAIA binding\nAll links operational
    IR_DEGRADED  : IR_DEGRADED (State 1)\nIR degraded\nClassical secure link operational\nGAIA advisory only
    LOCAL_AMPEL  : LOCAL_AMPEL_AUTONOMY (State 2)\nNetwork unavailable\nLocal AMPEL certified logic\nBlackout / channel loss
    SAFE_HOLD    : SAFE_ENVELOPE_HOLD (State 3)\nAll links unavailable\nNo external inputs accepted\nDOA recovery only

    FULL_NOMINAL --> IR_DEGRADED    : IR attenuation / optical reacquisition
    IR_DEGRADED  --> FULL_NOMINAL   : IR link restored
    IR_DEGRADED  --> LOCAL_AMPEL    : channel loss / plasma blackout
    LOCAL_AMPEL  --> IR_DEGRADED    : link recovered
    LOCAL_AMPEL  --> SAFE_HOLD      : integrity fail / anomaly unresolved
    SAFE_HOLD    --> FULL_NOMINAL   : DOA-authorised operator recovery
```

**Pre-entry transition rule (RSP re-entry):**

```
T − 60 s  ──  GAIA uploads bounded autonomy decision package to AMPEL360
T − 30 s  ──  Routing pre-configured to State 2 (LOCAL_AMPEL_AUTONOMY)
T  0 s    ──  Plasma blackout begins (RF + optical blocked)
T + Δ s   ──  Blackout clears; link recovery sequence starts → State 1
```

---

## 6. Full PLUMA-GAI-NET Integration Map

Complete integration picture: programme lifecycle, canonical thread, network
layers, and node topology — one diagram.

```mermaid
flowchart TB
    subgraph LIFECYCLE ["PLUMA-GAI Lifecycle (P000–P100)"]
        P000["P000 Intent"] --> P010["P010 Req"] --> P020["P020 Safety"]
        P020 --> P030["P030 Arch"] --> P040["P040 Impl"]
        P040 --> P050["P050 Verif"] --> P060["P060 Valid"]
        P060 --> P070["P070 Cert"] --> P080["P080 Ops"]
        P080 --> P090["P090 Monitor"] --> P100["P100 Change → P000"]
    end

    subgraph CANONICAL ["Canonical Thread"]
        CT_TRH["TranshidreOHs\nCarrier"] -->|"HIV-IFC-001"| CT_HIV["H.I.V.\nSpec"]
        CT_HIV -->|"HIV-IFC-002"| CT_VBZ["VibidratAZIONE\nRestore"]
        CT_VBZ -.->|"T_eff ↑"| CT_TRH
    end

    subgraph NET_STACK ["PLUMA-GAI NET Layers"]
        NS5["L5 Autonomy"] --> NS4["L4 Governance ★"]
        NS4 --> NS3["L3 Routing"] --> NS2["L2 Security"]
        NS2 --> NS1["L1 Protocol"] --> NS0["L0 Physical (IR)"]
    end

    subgraph TOPO ["Node Topology"]
        N_GAIA["GAIA (Space)"] <--> N_AMP["AMPEL360 (Air)"]
        N_AMP <--> N_MCC["MCC (Ground)"]
        N_GAIA <--> N_MCC
        N_AMP <--> N_UAS["UAS Fleet"]
    end

    LIFECYCLE -->|"governs"| CANONICAL
    CANONICAL -->|"feeds"| NET_STACK
    NET_STACK -->|"maps"| TOPO
    TOPO -.->|"T_eff telemetry"| LIFECYCLE
```

---

## 7. References

- PLUMA-GAI-NET specification: [`pluma-gai-net.yaml`](pluma-gai-net.yaml)
- Canonical thread specifications: [`../TranshidreOHs.md`](../TranshidreOHs.md) · [`../H.I.V.md`](../H.I.V.md) · [`../VibidratAZIONE.md`](../VibidratAZIONE.md)
- Net node schema: [`NET_NODE.schema.json`](NET_NODE.schema.json)
- Development plan: [`DEV-PLAN.md`](DEV-PLAN.md)
- PLUMA-GAI programme: [`../README.md`](../README.md)
