# TranshidreOHs — Multi-Modal Hydrogen Transport Layer

**Document ID:** PLUMA-GAI-TRH-001  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** PLUMA-GAI-001 ([README.md](README.md))  
**Companion:** [`transhidreOHs.yaml`](transhidreOHs.yaml)  
**Related:** [`H.I.V.md`](H.I.V.md) · [`VibidratAZIONE.md`](VibidratAZIONE.md)  
**Last Updated:** 2026-04-01

---

## 1. Purpose

TranshidreOHs is the carrier layer of the PLUMA-GAI canonical thread.  Its
function is to transport hydrogen — in liquid or gaseous form — across
programme domains and to carry fibre-optic data throughput alongside it.

> **Stack position:** TranshidreOHs is the infrastructure layer that feeds
> H.I.V.  The stack reads: **TranshidreOHs → H.I.V.**

TranshidreOHs reframes logistics as a traceability problem: by viewing social
exclusion as a transport and traceability failure, the resolution shifts from
the subjective (culture) to the objective (engineering).

---

## 2. Name Decomposition

| Segment | Meaning |
|---------|---------|
| **Trans** | Transport / across / through |
| **hidre** | Hydre → Hydro → Hydrogen (H₂) |
| **OHs** | Hydroxyl marker (–OH) indicating the molecular hydrogen chain |

The compound name signals a multi-phase, multi-modal carrier: gaseous H₂,
liquid H₂ (LH₂), and the hydroxyl chemistry of hydrogen-rich transport systems.

---

## 3. Transport Modes

TranshidreOHs supports three transport modes, all governed under PLUMA-GAI:

| Mode | Medium | Use Case | ATA Chapter |
|------|--------|----------|-------------|
| **LH₂ Cryo** | Liquid hydrogen at cryogenic temperature | AMPEL360 Q100 BWB fuel system | ATA 28 |
| **GH₂ Pipeline** | Gaseous hydrogen pipeline | Ground infrastructure, fuelling stations | N/A |
| **Fibre-optic co-carry** | Optical fibre bundled with H₂ conduit | Co-transport of data and energy metadata | N/A |

The third mode — fibre-optic co-carry — is the mechanism by which energy
metadata (hydrogen flow rate) and communication data (throughput) are bound
together into a single carrier package that H.I.V. can hash and stamp.

---

## 4. Carrier Package

A TranshidreOHs carrier package contains:

```yaml
carrier_package:
  package_id: "TRH-<UUID>"
  timestamp_utc: "ISO-8601Z"
  hydrogen_flow_rate_kg_s: <number>
  fiber_optic_throughput_gbps: <number>
  integrity_hash: "sha3-512:hex"
  origin_node: "<node_id>"
  destination_node: "<node_id>"
```

This package is the input to the H.I.V. Energy-Data Handshake (interface
HIV-IFC-001).  H.I.V. takes the carrier package, measures the infrared
temperature of the flow, attaches a V-token, and produces a VSED packet.

---

## 5. Safety Invariants

1. **No carrier without traceability:** every carrier package MUST carry an
   `integrity_hash` computed over all payload fields.
2. **Cryogenic safety:** LH₂ transport MUST comply with AMPEL360 cryogenic
   safety envelope (ATA 28 / ATA 71 / ATA 73) and PLUMA-GAI LH₂ safety
   constraints.
3. **Co-carry integrity:** fibre-optic throughput measurements MUST be
   synchronised with hydrogen flow measurements to within 1 s.
4. **Leak detection:** LH₂ micro-leak detection via SWIR (2.7 µm) is mandatory
   for all cryo-mode segments (see PLUMA-GAI NET §5.1).

---

## 6. Event Boundary Abstraction

When the essentiality of the carrier is abstracted — reducing all physical
transport modes to their minimal, indivisible representation — what remains is
the **event boundary**: the single transition point at which the hydrogen
carrier state hands off to the H.I.V. specification layer.

### 6.1 Definition

> **Event boundary** (TranshidreOHs): the irreducible surface at which the
> carrier's energy-data state is fully determined and ready for handoff.
> All prior transport complexity (cryo routing, pipeline pressure, fibre
> dispersion) is compressed to a single event.

The event boundary is characterised by four and only four values:

```yaml
event_boundary:
  boundary_id: "TRH-EB-<UUID>"
  timestamp_utc: "ISO-8601Z"           # single point in time — not a duration
  energy_state_hash: "sha3-512:hex"    # complete thermodynamic state, compressed
  data_state_hash: "sha3-512:hex"      # complete data channel state, compressed
```

All carrier-internal fields (`hydrogen_flow_rate_kg_s`,
`fiber_optic_throughput_gbps`, etc.) are deterministically derivable from the
`energy_state_hash`.  At the boundary, they need not be re-transmitted.

### 6.2 Consequence: Superconductor Vector Channel

When TranshidreOHs is operated in its event-boundary abstraction, the resulting
channel to H.I.V. (interface HIV-IFC-001) becomes a **superconductor vector**:

| Property | Physical Carrier | Event-Boundary Abstraction |
|----------|-----------------|---------------------------|
| Carrier resistance | Finite (transport losses, latency) | **Zero** — boundary is instantaneous |
| Signal loss | Possible (dispersion, leak) | **Zero** — state is hash-locked |
| Latency contribution | Non-zero | **Zero** — single event, no duration |
| T_eff at channel | Finite | **→ ∞** — by construction |

The term *superconductor vector* is precise: the channel is *superconducting*
(zero resistance) and *vectorial* (directed, carrying a state rather than a
flow).

See `H.I.V.md` §4.3 for the full channel specification under this abstraction.

---

## 7. Interface to H.I.V.

TranshidreOHs exposes one upstream interface to the H.I.V. layer:

| Field | Detail |
|-------|--------|
| **Interface ID** | HIV-IFC-001 (Energy-Data Handshake) |
| **Output A** | `hydrogen_flow_rate_kg_s` |
| **Output B** | `fiber_optic_throughput_gbps` |
| **Handshake target** | H.I.V. layer (PLUMA-GAI-HIV-001) |
| **Transformation at H.I.V.** | Hash metadata + attach V-token → VSED |

---

## 8. References

- H.I.V. specification: [`H.I.V.md`](H.I.V.md)
- PLUMA-GAI LH₂ energy chain: `README.md` §7.1
- PLUMA-GAI NET infrared strategy: `NET/README.md` §5
- ESSA H Pipeline: `ESSA/H-PIPELINE.md`
- ATA 28 (Fuel), ATA 71 (Power Plant), ATA 73 (Engine Fuel and Control)
