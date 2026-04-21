---
##############################################################################
# pluma-gai-net.yaml
# PLUMA-GAI NET — Performant Link Ubiquitous Map Architecture
# Ground–Aerospace Infrared Networks Integration Layer
##############################################################################

document_id: PLUMA-GAI-NET-001
document_type: network_architecture_extension
title: "PLUMA-GAI NET — Performant Link Ubiquitous Map Architecture"
subtitle: "Ground–Aerospace Infrared Networks"
lifecycle_stage: "System Integration Layer"
version: "0.1.0"
schema_version: "1.0.0"
status: draft
parent: PLUMA-GAI-001
last_updated: "2026-02-28T12:00:00Z"

purpose: >
  PLUMA-GAI NET is a network-centric extension of PLUMA-GAI introducing a
  high-performance, ubiquitous, infrared-augmented communication and sensing
  mesh spanning ground, air, and space. It is not merely a communication
  system; it is a mapped, governed, performance-bounded link architecture
  embedded into the programme lifecycle. The network is lifecycle-governed,
  not merely engineered.

one_line_definition: >
  PLUMA-GAI NET is a sovereign ground–air–space infrared mesh with lifecycle
  governance binding AMPEL360, GAIA, and ground infrastructure through a
  deterministic, performance-characterised, ubiquitous topological map of
  trust, capacity, and coherence.

##############################################################################
# 1  Architectural Positioning
##############################################################################

architectural_positioning:
  parent_architecture: PLUMA-GAI-001
  nature: fork_and_extension
  description: >
    PLUMA-GAI NET extends the two-node GAIA ↔ AMPEL360 governed channel into
    a full network architecture. It binds all three programme tiers through a
    mapped, infrared-augmented communication and sensing mesh.

  binds:
    - node: AMPEL360
      scope: "Aircraft + RSP (all flight regimes including re-entry)"
    - node: GAIA
      scope: "Satellite assets + quantum processing + UAS fleet"
    - node: GROUND
      scope: "Mission control, data centres, IR sensor grids"

##############################################################################
# 2  System Overview — Network Layers
##############################################################################

network_layers:

  - layer: 0
    name: "Physical"
    description: "IR emitters, detectors, optics, cryogenic sensors"
    elements:
      - IR emitters (MWIR / LWIR / NIR — see ir_strategy)
      - Infrared detectors and focal plane arrays
      - Optical terminals (space-to-ground, cross-link)
      - Cryogenic sensors (integrated with AMPEL360 LH₂ monitoring)

  - layer: 1
    name: "Link Protocol"
    description: "Optical modulation, forward error correction, framing"
    elements:
      - Optical modulation scheme (PPM / DPSK / coherent)
      - Forward Error Correction (FEC)
      - Frame synchronisation and link establishment

  - layer: 2
    name: "Integrity & Security"
    description: "Hash, signature, optional QKD — inherits from AMP-GAI-CORE"
    elements:
      - SHA3-512 integrity hashing
      - Digital signatures (ECDSA-P384 minimum)
      - QKD optional overlay (ETSI GS QKD 014)
    inherits_from: AMP-GAI-CORE

  - layer: 3
    name: "Deterministic Routing Map"
    description: "Latency-aware, trust-aware dynamic routing topology"
    elements:
      - Topological map (ubiquitous map — see net_node schema)
      - Latency-bounded path selection
      - Trust score-weighted routing decisions
      - Degradation-aware re-routing

  - layer: 4
    name: "Lifecycle Governance Binding"
    description: "PLUMA control — the novel layer making this lifecycle-governed"
    elements:
      - Phase-gated link certification (per PLUMA-GAI P000–P100)
      - Evidence-bound performance characterisation
      - Gating condition linkage (network-side)
      - DOA authority for network topology changes
    note: >
      Layer 4 is the architectural novelty. The network is lifecycle-governed:
      every link is certified, phase-gated, and evidence-bound.

  - layer: 5
    name: "Autonomy Interface"
    description: "AA-093 autonomy nodes operating over the NET"
    elements:
      - AA-093 bounded autonomy connections
      - Swarm / fleet coordination policies (GAIA-side)
      - Pre-loaded autonomy decisions for blackout periods
      - Fallback policy execution without network

##############################################################################
# 3  Ubiquitous Map Architecture
##############################################################################

ubiquitous_map:
  description: >
    "Ubiquitous Map" means: every node in the network is identified,
    geolocated (4D: space + time), envelope-bounded, and
    performance-characterised. It is a continuously updated topological
    map of trust, capacity, and coherence.

  node_properties:
    - identified           # unique node_id
    - geolocated_4d        # lat, lon, alt_km, epoch UTC
    - envelope_bounded     # performance_envelope with certified limits
    - performance_characterised  # latency, bandwidth, jitter, trust score

  update_frequency:
    description: "Map updates must be bounded and traceable"
    max_update_interval_s: 1     # for safety-relevant positions
    telemetry_push: true
    consensus_required: false     # advisory map; AMPEL authoritative on-board

  schema_ref: "NET_NODE.schema.json"

##############################################################################
# 4  Performance Model
##############################################################################

performance_model:

  parameters:
    - parameter: latency
      property: "Deterministic upper bound per link per regime"
      control: hard_maximum

    - parameter: bandwidth
      property: "Mode-dependent allocation"
      control: envelope_ceiling

    - parameter: jitter
      property: "Envelope-bounded"
      control: hard_maximum

    - parameter: packet_loss
      property: "Threshold-triggered degradation mode"
      control: degradation_trigger

    - parameter: thermal_noise
      property: "IR-calibrated compensation"
      control: calibration_model

  flight_regime_profiles:

    - regime: subsonic_civil
      description: "Normal civil flight below FL450"
      latency_ms_max: 150
      bandwidth_mbps_min: 200
      jitter_ms_max: 30
      ir_link_available: true
      blackout_risk: none

    - regime: high_altitude_cruise
      description: "High-altitude cruise above FL450 (stratosphere)"
      latency_ms_max: 200
      bandwidth_mbps_min: 100
      jitter_ms_max: 50
      ir_link_available: true
      blackout_risk: low
      note: "Reduced atmospheric attenuation; higher optical link margin"

    - regime: ascent_boost
      description: "Ascent and boost phase (RSP)"
      latency_ms_max: 100
      bandwidth_mbps_min: 50
      jitter_ms_max: 20
      ir_link_available: conditional
      blackout_risk: low_to_medium
      note: "Dynamic thermal environment; link acquisition may require re-pointing"

    - regime: re_entry_plasma
      description: "Re-entry plasma environment (RSP)"
      latency_ms_max: null       # blackout: no latency guarantee
      bandwidth_mbps_min: 0
      jitter_ms_max: null
      ir_link_available: false
      blackout_risk: critical
      degradation_state: 2       # AMPEL_LOCAL_CONTROL
      note: "Plasma blackout. Pre-loaded autonomy decisions required. See rsp_reentry_model."

    - regime: leo_crosslink
      description: "LEO satellite crosslink operations (GAIA)"
      latency_ms_max: 300
      bandwidth_mbps_min: 500
      jitter_ms_max: 100
      ir_link_available: true
      blackout_risk: low
      note: "Optical crosslinks; atmospheric attenuation absent in space segment"

##############################################################################
# 5  Infrared Strategy
##############################################################################

ir_strategy:

  wavelength_bands:
    - band: NIR
      range_um: "0.75–1.4"
      use_cases:
        - "Short-range optical communication links"
        - "Initial acquisition and tracking"
      atmospheric_window: good
      detector_technology: "InGaAs focal plane arrays"

    - band: SWIR
      range_um: "1.4–3.0"
      use_cases:
        - "Ground-to-air optical communications"
        - "Fuel cell anomaly signature detection"
        - "LH₂ micro-leak detection (2.7 µm absorption / emission band — upper SWIR)"
      atmospheric_window: moderate
      detector_technology: "Extended-InGaAs / HgCdTe"

    - band: MWIR
      range_um: "3.0–5.0"
      use_cases:
        - "Cryogenic thermal gradient mapping (LH₂ tank cold plume, 3–5 µm)"
        - "Engine exhaust and combustion thermal imaging"
        - "Broad-spectrum hydrogen flame detection (ancillary to 2.7 µm SWIR)"
      atmospheric_window: good
      detector_technology: "InSb / HgCdTe cooled arrays"

    - band: LWIR
      range_um: "8.0–14.0"
      use_cases:
        - "RSP re-entry heat envelope supervision (TPS)"
        - "Long-range environmental monitoring"
        - "Structural hot-spot detection"
      atmospheric_window: good
      detector_technology: "HgCdTe / microbolometer arrays"

  band_selection_policy: >
    Primary sensing: SWIR (2.7 µm) for LH₂ micro-leak detection;
    MWIR (3–5 µm) for cryo thermal mapping and exhaust imaging;
    LWIR (8–14 µm) for TPS / structural. Primary communication:
    NIR / SWIR for ground-air optical links. Selection is
    regime-dependent; band strategy is formally documented in
    IR_LINK_BUDGET.yaml (future deliverable).

  ampel360_applications:
    - "LH₂ tank micro-leak detection (SWIR 2.7 µm — hydrogen absorption / emission band)"
    - "Cryogenic thermal gradient mapping (MWIR 3–5 µm)"
    - "Fuel cell anomaly signatures (SWIR / MWIR)"
    - "RSP re-entry heat envelope supervision (LWIR 8–14 µm; TPS)"

  gaia_applications:
    - "Satellite optical crosslinks (NIR / SWIR directional)"
    - "Secure narrow-beam communications (NIR)"
    - "Anti-interference directional control (narrow FOV)"
    - "Earth observation thermal layer (LWIR; sat payload)"

  ir_dual_role:
    sensor_modality: true
    communication_modality: true
    note: >
      Infrared serves both as a sensor modality (detecting physical
      phenomena) and as a communication modality (carrying data). The
      lifecycle evidence chain must cover both roles for each function.

##############################################################################
# 6  Deterministic Fallback Doctrine
##############################################################################

fallback_doctrine:
  critical_rule: >
    AMPEL must remain safe without GAIA NET. The network is advisory to
    flight-critical operation; on-board AMPEL logic is never dependent on
    NET availability.

  degradation_states:

    - state: 0
      name: "FULL_NOMINAL"
      description: "Full IR + Classical + QKD"
      ir_link: operational
      classical_link: operational
      qkd: operational
      gaia_binding: full
      autonomy: full_advisory
      certification_status: pre_certified

    - state: 1
      name: "IR_DEGRADED"
      description: "IR degraded; classical secure link operational"
      ir_link: degraded
      classical_link: operational
      qkd: conditional
      gaia_binding: advisory_only
      autonomy: advisory_only
      degradation_trigger:
        - ir_thermal_noise_exceeded
        - atmospheric_attenuation_threshold
        - optical_terminal_reacquisition
      certification_status: pre_certified

    - state: 2
      name: "LOCAL_AMPEL_AUTONOMY"
      description: "Network unavailable; local AMPEL autonomy only"
      ir_link: unavailable
      classical_link: unavailable
      qkd: unavailable
      gaia_binding: none
      autonomy: local_certified_only
      degradation_trigger:
        - channel_loss
        - plasma_blackout
        - coherence_loss
      certification_status: pre_certified

    - state: 3
      name: "SAFE_ENVELOPE_HOLD"
      description: "Safe envelope hold — ultimate fallback"
      ir_link: unavailable
      classical_link: unavailable
      qkd: unavailable
      gaia_binding: none
      autonomy: none
      degradation_trigger:
        - integrity_fail
        - anomaly_unresolved
        - operator_commanded
      certification_status: pre_certified
      note: >
        AMPEL enters its certified safe envelope. No external inputs accepted.
        This state must be recoverable only by DOA-authorised operator action.

##############################################################################
# 7  RSP Re-entry Integration
##############################################################################

rsp_reentry_model:
  description: >
    During re-entry the plasma sheath causes RF and optical link blackout.
    PLUMA-GAI NET must predict blackout windows, switch routing topology,
    and pre-load autonomy decisions.

  blackout_prediction:
    method: "Aerothermodynamic model coupled with link budget simulation"
    inputs:
      - re_entry_trajectory_vector
      - vehicle_geometry_and_orientation
      - atmospheric_density_profile
      - ir_wavelength_band_attenuation_vs_plasma_density
    outputs:
      - blackout_start_time_utc
      - blackout_duration_s
      - recovery_time_utc
      - confidence_interval
    model_ref: "RE_ENTRY_BLACKOUT_MODEL.yaml"  # future deliverable

  topology_switching:
    description: >
      Before predicted blackout window, routing topology is pre-configured
      to State 2 (LOCAL_AMPEL_AUTONOMY). All GAIA advisory functions are
      suspended. Transition must occur with margin before blackout.
    pre_transition_margin_s: 30
    triggers:
      - blackout_predicted_within_margin
      - ir_signal_attenuation_threshold_crossed

  autonomy_preloading:
    description: >
      GAIA computes and uploads a bounded autonomy decision package to
      AMPEL360 before the blackout window. The package contains pre-certified
      contingency decision trees valid for the predicted blackout duration.
    upload_deadline_before_blackout_s: 60
    package_validity_s_max: 3600
    aa_093_ref: "AA-093-RSP-REENTRY"
    coupling_required:
      - aerothermodynamic_models
      - link_budget_simulations
      - autonomy_envelope_preparation

##############################################################################
# 8  Critical Technical Fork Points
##############################################################################

fork_points:
  description: >
    Formal definition of these fork points is required to complete the
    PLUMA-GAI NET specification. Each is an open engineering question that
    must be resolved and evidence-bound before certification.
  items:
    - id: FP-NET-001
      title: "IR wavelength band strategy (MWIR vs LWIR vs NIR)"
      status: open
      description: >
        Formal selection of wavelength bands per function and regime.
        Must be resolved in IR_LINK_BUDGET.yaml with atmospheric attenuation
        data and detector sensitivity characterisation.
      responsible: Design Authority

    - id: FP-NET-002
      title: "Atmospheric attenuation compensation model"
      status: open
      description: >
        Model for compensating IR attenuation under varying atmospheric
        conditions (humidity, cloud, aerosol loading). Must cover all
        flight regimes including re-entry.
      responsible: Analysis

    - id: FP-NET-003
      title: "Optical terminal pointing accuracy limits"
      status: open
      description: >
        Maximum acceptable pointing error for each optical link class
        (ground-air, air-space, crosslink). Drives optical terminal
        mechanical design and control loop requirements.
      responsible: Design Authority

    - id: FP-NET-004
      title: "Plasma interference mitigation for RSP"
      status: open
      description: >
        Strategy and evidence for maintaining integrity verification
        capability through or around the plasma blackout envelope.
        Coupled with aerothermodynamic models and link budget.
      responsible: Safety

    - id: FP-NET-005
      title: "Certification boundary: network advisory vs flight-critical loop"
      status: open
      description: >
        Formal demarcation of which NET outputs may influence flight-critical
        functions and which are advisory only. Maps to DAL allocation and
        governs AMPEL360 execution rights.
      responsible: DOA

##############################################################################
# 9  Deliverables
##############################################################################

deliverables:
  - id: NET-DEL-01
    title: "PLUMA-GAI NET Specification (normative)"
    file: "00-PROGRAM/PLUMA-GAI/NET/pluma-gai-net.yaml"
    content: "Layer stack, performance model, IR strategy, fallback doctrine, RSP model, fork points"
    status: draft

  - id: NET-DEL-02
    title: "Net Node Schema"
    file: "00-PROGRAM/PLUMA-GAI/NET/NET_NODE.schema.json"
    content: "JSON Schema for the net_node data structure (ubiquitous map node)"
    status: draft

  - id: NET-DEL-03
    title: "IR Link Budget Parametric Model"
    file: "00-PROGRAM/PLUMA-GAI/NET/IR_LINK_BUDGET.yaml"
    content: "Band selection, atmospheric attenuation, link margin calculations"
    status: planned

  - id: NET-DEL-04
    title: "Re-entry Blackout Predictive Model"
    file: "00-PROGRAM/PLUMA-GAI/NET/RE_ENTRY_BLACKOUT_MODEL.yaml"
    content: "Aerothermodynamic coupling, window prediction, topology switching"
    status: planned

  - id: NET-DEL-05
    title: "Ground-Space Topology Optimisation Framework"
    file: "00-PROGRAM/PLUMA-GAI/NET/TOPOLOGY_OPT.yaml"
    content: "Trust-latency-aware routing, optimisation objectives, GAIA integration"
    status: planned

  - id: NET-DEL-06
    title: "Certification Cross-Mapping"
    file: "00-PROGRAM/PLUMA-GAI/NET/CERT_CROSS_MAP.yaml"
    content: "CS-25 + spaceflight special conditions + EU AI Act Article 6 cross-mapping"
    status: planned
---

# PLUMA-GAI NET
## Performant Link Ubiquitous Map Architecture — Ground–Aerospace Infrared Networks Integration Layer

**Document ID:** PLUMA-GAI-NET-001  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** PLUMA-GAI-001  
**Last Updated:** 2026-02-28

> **One-line definition:** PLUMA-GAI NET is a sovereign ground–air–space infrared mesh with lifecycle governance binding AMPEL360, GAIA, and ground infrastructure through a deterministic, performance-characterised, ubiquitous topological map of trust, capacity, and coherence.

---

## 1. Architectural Positioning

PLUMA-GAI NET is a **network-centric extension of PLUMA-GAI**. It is not merely a communication system — it is a mapped, governed, performance-bounded link architecture embedded into the programme lifecycle.

It extends the two-node GAIA ↔ AMPEL360 governed channel into a full three-tier network:

| Node | Scope |
|------|-------|
| AMPEL360 | Aircraft + RSP (all flight regimes including re-entry) |
| GAIA | Satellite assets + quantum processing + UAS fleet |
| GROUND | Mission control, data centres, IR sensor grids |

The architectural novelty is **Layer 4 (Lifecycle Governance Binding)**: the network is lifecycle-governed, not merely engineered. Every link is certified, phase-gated, and evidence-bound under PLUMA-GAI P000–P100.

---

## 2. Layer Stack

```
Layer 5 – Autonomy Interface         (AA-093 nodes; pre-loaded blackout decisions)
Layer 4 – Lifecycle Governance Binding  ← THE NOVEL LAYER
Layer 3 – Deterministic Routing Map  (latency + trust aware)
Layer 2 – Integrity & Security       (SHA3-512, signature, QKD optional)
Layer 1 – Link Protocol              (optical modulation, FEC, framing)
Layer 0 – Physical                   (IR emitters, detectors, optics, cryo sensors)
```

| Layer | Name | Key Elements |
|-------|------|-------------|
| 0 | Physical | IR emitters / detectors, optical terminals, cryogenic sensors |
| 1 | Link Protocol | Optical modulation (PPM/DPSK/coherent), FEC, frame sync |
| 2 | Integrity & Security | SHA3-512, ECDSA-P384, QKD optional (inherits AMP-GAI-CORE) |
| 3 | Deterministic Routing Map | Trust-score-weighted, latency-bounded topology |
| 4 | Lifecycle Governance Binding | Phase-gated certification, DOA authority, evidence binding |
| 5 | Autonomy Interface | AA-093 connections, pre-loaded re-entry decision packages |

---

## 3. Ubiquitous Map Architecture

**"Ubiquitous Map"** means every node in the network is:
- **Identified** — unique `node_id`
- **Geolocated (4D)** — lat, lon, alt_km, epoch UTC
- **Envelope-bounded** — certified performance limits
- **Performance-characterised** — latency, bandwidth, jitter, trust score

This forms a **continuously updated topological map of trust, capacity, and coherence**.

Node schema: `NET_NODE.schema.json`

### Example Net Node

```yaml
net_node:
  node_id: "AMP-GAI-NET-A001"
  domain: ["air"]
  node_type: AMPEL360_AIRCRAFT
  position_4d:
    lat: 48.856
    lon: 2.352
    alt_km: 12.5
    epoch: "2026-02-28T12:00:00Z"
  link_capabilities:
    infrared_comm: true
    infrared_sensing: true
    ir_bands: [MWIR, SWIR]
    classical_rf: true
    qkd_capable: optional
  performance_envelope:
    latency_ms_max: 150
    bandwidth_mbps: 200
    jitter_ms_max: 30
  trust_score: 0.99
  lifecycle_status: certified
```

---

## 4. Performance Model

Performance is **not static** — it is tied to flight regime:

| Regime | Latency Max | Bandwidth Min | Jitter Max | IR Link | Blackout Risk |
|--------|------------|--------------|-----------|---------|--------------|
| Subsonic civil | 150 ms | 200 Mbps | 30 ms | ✓ | None |
| High-altitude cruise | 200 ms | 100 Mbps | 50 ms | ✓ | Low |
| Ascent / boost | 100 ms | 50 Mbps | 20 ms | Conditional | Low–medium |
| Re-entry plasma | No guarantee | 0 | No guarantee | ✗ | **Critical** |
| LEO crosslink | 300 ms | 500 Mbps | 100 ms | ✓ | Low |

Key parameters:

| Parameter | Control |
|-----------|---------|
| Latency | Deterministic hard maximum |
| Bandwidth | Mode-dependent ceiling |
| Jitter | Envelope-bounded |
| Packet loss | Threshold-triggered degradation |
| Thermal noise | IR-calibrated compensation |

---

## 5. Infrared Strategy

Infrared serves a **dual role**: sensor modality and communication modality.

### Band Selection

| Band | Range | Primary Uses | Atmospheric Window |
|------|-------|-------------|-------------------|
| NIR | 0.75–1.4 µm | Short-range optical comms, acquisition | Good |
| SWIR | 1.4–3.0 µm | Ground-to-air optical comms, fuel cell anomaly, LH₂ micro-leak (2.7 µm) | Moderate |
| MWIR | 3.0–5.0 µm | Cryo thermal mapping (LH₂ cold plume), engine exhaust thermal imaging | Good |
| LWIR | 8.0–14.0 µm | RSP TPS heat envelope, structural hot-spots | Good |

### AMPEL360 IR Applications
- LH₂ tank micro-leak detection (SWIR 2.7 µm — hydrogen absorption/emission band)
- Cryogenic thermal gradient mapping (MWIR 3–5 µm)
- Fuel cell anomaly signatures (SWIR / MWIR)
- RSP re-entry heat envelope supervision (LWIR 8–14 µm; TPS)

### GAIA IR Applications
- Satellite optical crosslinks (NIR / SWIR directional)
- Secure narrow-beam communications (NIR)
- Anti-interference directional control (narrow FOV)
- Earth observation thermal layer (LWIR; sat payload)

---

## 6. Deterministic Fallback Doctrine

> **Critical rule: AMPEL must remain safe without GAIA NET.**

The network is advisory to flight-critical operation; on-board AMPEL logic is never dependent on NET availability.

| State | Name | Description | Gaia Binding |
|-------|------|-------------|-------------|
| 0 | FULL_NOMINAL | Full IR + Classical + QKD | Full |
| 1 | IR_DEGRADED | IR degraded; classical secure | Advisory only |
| 2 | LOCAL_AMPEL_AUTONOMY | Network unavailable; AMPEL local only | None |
| 3 | SAFE_ENVELOPE_HOLD | Ultimate fallback; certified safe envelope | None |

Each state is **pre-certified**. Transitions are deterministic.

---

## 7. RSP Re-entry Integration

During re-entry the plasma sheath causes RF and optical link blackout. PLUMA-GAI NET must:

1. **Predict blackout windows** — aerothermodynamic model + link budget simulation
2. **Switch routing topology** — pre-configured to State 2 before blackout (30 s margin)
3. **Pre-load autonomy decisions** — GAIA uploads bounded decision package 60 s before blackout

Coupling required:
- Aerothermodynamic models
- Link budget simulations (IR attenuation vs plasma density)
- Autonomy envelope preparation (AA-093-RSP-REENTRY)

---

## 8. Critical Technical Fork Points

These open engineering questions must be resolved and evidence-bound before certification:

| ID | Title | Responsible | Status |
|----|-------|-------------|--------|
| FP-NET-001 | IR wavelength band strategy (MWIR vs LWIR vs NIR) | Design Authority | Open |
| FP-NET-002 | Atmospheric attenuation compensation model | Analysis | Open |
| FP-NET-003 | Optical terminal pointing accuracy limits | Design Authority | Open |
| FP-NET-004 | Plasma interference mitigation for RSP | Safety | Open |
| FP-NET-005 | Certification boundary: network advisory vs flight-critical loop | DOA | Open |

---

## 9. Deliverables

| ID | Title | File | Status |
|----|-------|------|--------|
| NET-DEL-01 | PLUMA-GAI NET Specification (normative) | `pluma-gai-net.yaml` | Draft |
| NET-DEL-02 | Net Node Schema | `NET_NODE.schema.json` | Draft |
| NET-DEL-03 | IR Link Budget Parametric Model | `IR_LINK_BUDGET.yaml` | Planned |
| NET-DEL-04 | Re-entry Blackout Predictive Model | `RE_ENTRY_BLACKOUT_MODEL.yaml` | Planned |
| NET-DEL-05 | Ground-Space Topology Optimisation Framework | `TOPOLOGY_OPT.yaml` | Planned |
| NET-DEL-06 | Certification Cross-Mapping (CS-25 + spaceflight + AI Act) | `CERT_CROSS_MAP.yaml` | Planned |

---

## 10. Files in this Directory

| File | Purpose |
|------|---------|
| `README.md` | This document — human-readable PLUMA-GAI NET specification |
| `pluma-gai-net.yaml` | Machine-readable normative PLUMA-GAI NET specification |
| `NET_NODE.schema.json` | JSON Schema for the ubiquitous map `net_node` data structure |

---

## 11. References

- Parent: `00-PROGRAM/PLUMA-GAI/pluma-gai.yaml` (PLUMA-GAI-001)
- Channel ICD: `00-PROGRAM/PLUMA-GAI/AMP-GAI-ICD-v0.1.0.yaml`
- Autonomy assurance: `UTS/AA-093/aa-093-assurance-case.yaml`
- ESSA lifecycle standard: `ESSA/cctls.yaml` (ESSA-STD-CCTLS-001)
