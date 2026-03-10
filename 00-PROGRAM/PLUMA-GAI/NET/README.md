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
