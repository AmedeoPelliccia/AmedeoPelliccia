# GNS-010 — EGNOS & Galileo Integration Specification

### Domain 010 — Mission Systems · UTS-TAX-001 v1.1

> **Artefact ID:** GNS-010
> **Version:** 0.1.0
> **Status:** DRAFT
> **Author:** Amedeo Pelliccia
> **Parent Domain:** 010 — Mission Systems (UTS-TAX-001 v1.1)
> **Parent Lifecycle:** EACST-STD-CCTLS-001 v0.3.0 · CLB-001-TOKEN
> **Frameworks:** ESSA · AMPEL360 · GAIA EU
> **Applicable Programmes:** Civil aviation (NPA/IFR), Urban Air Mobility (UAM), Reusable Space Platforms (RSP), Hybrid Transport (domain 092)

---

## 0. Purpose & Scope

This specification defines the requirements, performance bounds, certification pathway and CCTLS token model for onboarding **EGNOS** (European Geostationary Navigation Overlay Service) and **Galileo** as primary or augmented positioning, navigation and timing (PNT) sources within UTS domain 010 — Mission Systems.

It covers:

1. **Signal-in-Space (SIS) performance bounds** — the minimum and operational performance parameters that EGNOS and Galileo signals must meet for each UTS operational context.
2. **SBAS / augmentation certification** — compliance pathway with DO-229F / ED-259 for EGNOS and MOPS for Galileo-augmented operations.
3. **Dual-constellation interoperability** — GPS + Galileo combined navigation solution requirements, integrity monitoring and signal selection logic.
4. **EGNOS Safety-of-Life (SoL) service** — requirements for operations requiring EGNOS SoL certification (APV-I, LPV-200, NPA).
5. **Open Service (OS) and High Accuracy Service (HAS)** — Galileo OS and HAS usage requirements, including the Galileo HAS PPP-RTK integration roadmap.
6. **CCTLS token types and evidence** — the token model entries that this specification generates, linking to the CLB-001 baseline.

---

## 1. Reference Standards

| Standard | Title | Applicability |
|---|---|---|
| **DO-229F** | Minimum Operational Performance Standards for GPS/WAAS Airborne Equipment | EGNOS SBAS certification |
| **ED-259** | EUROCAE equivalent of DO-229 for EGNOS/European context | European regulatory baseline |
| **DO-235C** | Assessment of Navigation Systems | Interoperability assessment |
| **DO-316** | Minimum Operational Performance Standards for Global Navigation Satellite Systems (GNSS) Airborne Active Antenna Equipment | Antenna qualification |
| **RTCA DO-253D** | Minimum Operational Performance Standards for GPS Local Area Augmentation System Airborne Equipment | LAAS/GRAS if applicable |
| **Galileo OS SDD** | Galileo Open Service Signal-In-Space Interface Control Document | Signal performance definition |
| **Galileo HAS SDD** | Galileo High Accuracy Service Signal-In-Space Interface Control Document | HAS PPP-RTK performance |
| **ICAO Annex 10 Vol I** | Aeronautical Telecommunications — Radio Navigation Aids | Operational performance standards |
| **ICAO Doc 9849** | Global Navigation Satellite System (GNSS) Manual | System-level requirements |
| **ED-115** | MOPS for Galileo/GPS Airborne Receiving Equipment | Dual-constellation MOPS |
| **EASA AMC 20-28** | Airworthiness Criteria — GNSS Based Navigation | European certification AMC |
| **ISO 17894** | Ships and marine technology — Principles for GNSS augmentation | Applicable for maritime hybrid transport |

---

## 2. Signal-in-Space (SIS) Performance Bounds

### 2.1 Performance Parameters

PNT sources shall be characterised and bounded against the following SIS parameters. Values stated are **minimum required** for operational clearance; actual achieved values must be demonstrated through evidence pack GNS-010-EV-001.

| Parameter | Symbol | EGNOS SoL Service | Galileo OS (E1/E5) | Galileo HAS | Unit |
|---|---|---|---|---|---|
| **Horizontal Accuracy (95%)** | HPE₉₅ | ≤ 3.0 | ≤ 4.0 | ≤ 0.20 | m |
| **Vertical Accuracy (95%)** | VPE₉₅ | ≤ 4.0 | ≤ 8.0 | ≤ 0.40 | m |
| **Horizontal Protection Level** | HPL | ≤ 40.0 | — | — | m |
| **Vertical Protection Level** | VPL | ≤ 50.0 | — | — | m |
| **Time-to-First-Fix (cold)** | TTFF | ≤ 60 | ≤ 100 | ≤ 100 | s |
| **Signal Availability** | Avail | ≥ 0.999 | ≥ 0.995 | ≥ 0.990 | ratio |
| **Continuity Risk** | — | ≤ 1×10⁻⁶ | ≤ 1×10⁻⁵ | ≤ 1×10⁻⁵ | per 150 s |
| **Integrity Risk** | — | ≤ 2×10⁻⁷ | — | — | per approach |
| **Time Accuracy (95%)** | TACC₉₅ | ≤ 30 | ≤ 30 | ≤ 10 | ns |
| **Carrier-to-Noise Density** | C/N₀ | ≥ 35 | ≥ 35 | ≥ 37 | dBHz |

### 2.2 Operational Context Bounds

Performance requirements vary by operational context (UTS CLB-001 bindings):

| Operation Context | Required Service Level | Min HPE₉₅ | Min VPE₉₅ | Integrity Source |
|---|---|---|---|---|
| `FLIGHT` — En-route | Galileo OS | ≤ 95 m | N/A | RAIM (FDE) |
| `FLIGHT` — Terminal | EGNOS OS or Galileo OS | ≤ 16 m | N/A | EGNOS augmentation |
| `FLIGHT` — APV-I | EGNOS SoL | ≤ 16 m | ≤ 20 m | EGNOS SoL HPL/VPL |
| `FLIGHT` — LPV-200 | EGNOS SoL | ≤ 16 m | ≤ 4.0 m | EGNOS SoL VPL ≤ 35 m |
| `FLIGHT` — UAM urban | Galileo HAS or EGNOS SoL | ≤ 1.5 m | ≤ 2.0 m | Dual-source + IMU |
| `LRE` — Launch/Re-entry | Galileo OS + INS hybrid | ≤ 10 m | ≤ 15 m | RAIM + INS |
| `LINE` — Ground ops | Galileo OS | ≤ 5 m | N/A | Receiver-level RAIM |

### 2.3 Alert Limits by Phase of Flight

| Phase | Horizontal Alert Limit (HAL) | Vertical Alert Limit (VAL) |
|---|---|---|
| En-route (oceanic) | 7.4 km | N/A |
| En-route (domestic) | 3.7 km | N/A |
| Terminal | 1.0 km | N/A |
| NPA | 556 m | N/A |
| APV-I | 40 m | 50 m |
| LPV-200 | 40 m | 35 m |
| CAT-I (augmented) | 40 m | 15 m |
| UAM hover/precision | 5 m | 5 m |

---

## 3. SBAS / Augmentation Certification (DO-229F / ED-259)

### 3.1 Certification Pathway

EGNOS-augmented operations require airborne equipment and operational procedures to comply with DO-229F (RTCA) and/or ED-259 (EUROCAE), as applicable per aircraft registration and operational territory.

```
Step 1: Receiver MOPS qualification (DO-229F Section 2)
        └─► GNS-010-EV-002 — SBAS Receiver Qualification Report

Step 2: Antenna MOPS qualification (DO-316)
        └─► GNS-010-EV-003 — Antenna Qualification Record

Step 3: System integration testing (DO-229F Section 3)
        └─► GNS-010-EV-004 — Integration Test Matrix (link to WI-070)

Step 4: Failure Mode and Effects Analysis (DO-229F Section 4)
        └─► GNS-010-EV-005 — GNSS FMEA Report (link to P020 HAZARD tokens)

Step 5: Flight test campaign (EASA AMC 20-28 / CCTLS P070)
        └─► TEST_CAMPAIGN-P070-EGNOS-SoL-001

Step 6: DOA sign-off (CCTLS P050)
        └─► DOA_SIGN-P050-GNS-010-001

Step 7: Operational approval (OpSpec / OPS authorisation)
        └─► TRAFFIC_CLEARANCE-P090-EGNOS-OPS-001
```

### 3.2 Equipment Classes (DO-229F)

| Class | Description | Operations Enabled |
|---|---|---|
| **Class Beta-1** | SBAS-capable, provides lateral + vertical guidance | APV-I, LPV-200 |
| **Class Beta-2** | SBAS + RAIM, FDE enabled | NPA + terminal |
| **Class Beta-3** | Beta-2 + dual-frequency (L1/L5 or E1/E5) | LPV-200 + CAT-I augmented |
| **Class Gamma** | Multi-constellation + dual-frequency + SBAS | UAM precision, hybrid transport |

Minimum class for AMPEL360 operations: **Class Beta-3**.

### 3.3 MOPS Compliance Matrix

| MOPS Requirement | DO-229F Reference | Verification Method | Evidence |
|---|---|---|---|
| Acquisition sensitivity | §2.1.1 | Lab test | GNS-010-EV-002 |
| Tracking sensitivity | §2.1.2 | Lab test | GNS-010-EV-002 |
| Position accuracy (static) | §2.2.1 | Sky simulator + field | GNS-010-EV-002 |
| Position accuracy (dynamic) | §2.2.2 | Flight test / HIL | GNS-010-EV-004 |
| SBAS message decoding | §2.3 | Protocol test bench | GNS-010-EV-002 |
| Protection level computation | §2.4 | Simulation + flight | GNS-010-EV-005 |
| Interference rejection | §2.5 | EMI/EMC test | GNS-010-EV-003 |
| RAIM/FDE | §2.6 | HIL simulation | GNS-010-EV-005 |
| Time-to-alarm | §2.7 | Protocol test | GNS-010-EV-002 |

---

## 4. Dual-Constellation Interoperability (GPS + Galileo)

### 4.1 Architecture

The dual-constellation navigation solution combines GPS (L1/L5) and Galileo (E1/E5a/E5b) in a tightly or loosely coupled architecture. The combined solution must be validated per ED-115.

```
┌─────────────────────────────────────────────────────┐
│           Navigation Processing Unit (NPU)           │
│                                                       │
│  ┌──────────────┐    ┌──────────────┐               │
│  │  GPS L1/L5   │    │ Galileo E1/  │               │
│  │  Receiver    │    │ E5a/E5b/E6   │               │
│  └──────┬───────┘    └──────┬───────┘               │
│         │                   │                        │
│         └─────────┬─────────┘                        │
│                   │  Combined GNSS solution           │
│         ┌─────────▼─────────┐                        │
│         │  EGNOS/SBAS       │  ← SoL corrections     │
│         │  Augmentation     │    via GEO satellites   │
│         └─────────┬─────────┘                        │
│                   │                                   │
│         ┌─────────▼─────────┐                        │
│         │  Galileo HAS      │  ← PPP-RTK corrections  │
│         │  Corrections (E6) │    sub-decimeter        │
│         └─────────┬─────────┘                        │
│                   │                                   │
│         ┌─────────▼─────────┐                        │
│         │  IMU / Baro       │  ← Hybridisation        │
│         │  Hybrid Filter    │    (EKF / UKF)          │
│         └─────────┬─────────┘                        │
│                   │  PNT output                       │
│                   ▼                                   │
│         Position · Velocity · Attitude · Time         │
└─────────────────────────────────────────────────────┘
```

### 4.2 Interoperability Requirements

| Requirement | Parameter | Threshold | Standard |
|---|---|---|---|
| Common time reference | GPS-Galileo Time Offset (GGTO) | Applied and bounded ≤ 50 ns | ICAO Annex 10 |
| Common geodetic datum | WGS-84 / GTRF alignment | Bias ≤ 3 cm | Galileo OS SDD |
| Signal-in-space compatibility | L1/E1 centre frequency | 1575.42 MHz (BPSK/CBOC) | RTCM SC-104 |
| Dual-frequency ionosphere | L1+L5 or E1+E5a iono-free | Iono correction applied | DO-229F §2.1.4 |
| Fault detection | Cross-constellation RAIM | Pmd ≤ 10⁻⁵ per hour | ED-115 |
| Signal selection logic | Satellite geometry (HDOP/VDOP) | HDOP ≤ 2.0, VDOP ≤ 3.0 | DO-229F §2.2 |
| Continuity | Dual-constellation combined | ≥ 0.9999 | ICAO Annex 10 |

### 4.3 RAIM / FDE Requirements

Receiver Autonomous Integrity Monitoring (RAIM) with Fault Detection and Exclusion (FDE) must be implemented for all operational contexts. Performance must meet:

- **RAIM availability:** ≥ 0.9999 for terminal and approach phases
- **FDE availability:** ≥ 0.999 for en-route through terminal
- **Alert latency:** ≤ 6 s (terminal), ≤ 10 s (en-route)
- **Missed detection probability (Pmd):** ≤ 10⁻³ per sample
- **False alert probability (Pfa):** ≤ 10⁻⁵ per hour

Dual-constellation RAIM provides approximately 2–4 additional satellites versus single-constellation, materially improving FDE availability in urban canyons and at high latitudes (> 55° N) — critical for Nordic and trans-polar AMPEL360 operations.

---

## 5. EGNOS Safety-of-Life (SoL) Service Requirements

### 5.1 SoL Service Overview

The EGNOS SoL service is broadcast on L1 (1575.42 MHz) via three geostationary satellites (PRN 120, 123, 136 as of 2026). It provides:

- **SBAS corrections** for GPS and Galileo (E1) ranging
- **Integrity bounds** (protection levels) meeting ICAO SARPS
- **Guaranteed continuity** of service declarations (NOTAM-like SoL NANU)
- **Service area:** ECAC states + extension to North Africa and Middle East

### 5.2 SoL Operational Requirements

| Requirement | Value | Reference |
|---|---|---|
| SoL receiver certification | DO-229F Class Beta-1 minimum | EASA AMC 20-28 |
| EGNOS SoL subscription | Not required (broadcast, free) | GSA/EUSPA |
| SBAS GEO tracking | Minimum 1 GEO tracked for SoL | DO-229F §2.3 |
| Service area confirmation | Confirmed via EGNOS NOTAM/NANU | EUSPA SIS portal |
| Misleading information rate | ≤ 2×10⁻⁷ per approach | ICAO Annex 10 |
| Continuity risk (approach) | ≤ 1×10⁻⁶ per 150 s | DO-229F |
| LPV-200 VPL bound | VPL ≤ 35 m continuously | EASA OPS |

### 5.3 SoL Service Monitoring

Programs using EGNOS SoL must implement:

1. **Pre-flight SoL availability check** — query EUSPA SISNET or NOTAM feed for SoL service area availability at destination (GNS-010-EV-006).
2. **In-flight SoL monitoring** — receiver must monitor SoL integrity messages continuously and revert to RAIM-only if SoL unavailable.
3. **NANU compliance** — all SoL outage NANUs within ±24 h of planned operation must be reviewed and documented.
4. **Reversionary navigation** — a non-GNSS backup (INS, DME/DME, VOR/DME) must be available and demonstrated for all SoL-dependent operations.

---

## 6. Open Service (OS) and High Accuracy Service (HAS)

### 6.1 Galileo Open Service (OS)

The Galileo OS is freely accessible on E1-B/C (data + pilot) and E5a/E5b. It provides:

- **Single-frequency (E1):** horizontal accuracy ≤ 4 m (95%), vertical ≤ 8 m
- **Dual-frequency (E1+E5a / E1+E5b):** iono-free, horizontal ≤ 3 m, vertical ≤ 6 m
- **Availability:** ≥ 99.5% globally (28-satellite constellation, full operational capability)
- **Authentication:** OSNMA (Open Service Navigation Message Authentication) — mandatory for UTS domain 020 cyber compliance

#### OSNMA Requirements

OSNMA provides cryptographic authentication of Galileo navigation messages, mitigating spoofing attacks. Requirements for AMPEL360 operations:

| Requirement | Threshold |
|---|---|
| OSNMA receiver support | Mandatory for `FLIGHT` and `LRE` contexts |
| Authentication latency | ≤ 30 s from cold start |
| Key chain refresh | Automatic via Galileo broadcast |
| OSNMA cross-link to P120 | CYB_CONTROL-P120-OSNMA-001 must be linked |

### 6.2 Galileo High Accuracy Service (HAS)

The Galileo HAS is broadcast on the E6-B channel and provides PPP-RTK (Precise Point Positioning — Real-Time Kinematic) corrections, achieving sub-decimetre accuracy without ground reference stations.

#### HAS Performance Targets

| Parameter | HAS Phase 1 (2024–2026) | HAS Phase 2 (2027+) | Unit |
|---|---|---|---|
| Horizontal accuracy (95%) | ≤ 0.20 | ≤ 0.10 | m |
| Vertical accuracy (95%) | ≤ 0.40 | ≤ 0.20 | m |
| Convergence time | ≤ 300 | ≤ 100 | s |
| Signal availability | ≥ 99.0 | ≥ 99.5 | % |
| Service area | Global | Global | — |
| Frequency | E6-B (1278.75 MHz) | E6-B | MHz |

#### HAS Integration Requirements for UTS 010

| Requirement | Detail |
|---|---|
| Receiver E6 capability | E6-B tracking with HAS decoder mandatory for HAS use |
| Convergence management | Operations must not commence precision phase until convergence confirmed (≤ 0.20 m CEP) |
| HAS + EGNOS SoL hybrid | Recommended for LPV-200 and UAM precision: HAS for accuracy, EGNOS SoL for integrity |
| HAS failure management | Automatic fallback to EGNOS SoL or dual-frequency OS if HAS signal lost |
| Latency | E6 HAS message latency ≤ 10 s; position update rate ≥ 1 Hz |

---

## 7. CCTLS Token Types & Evidence

### 7.1 Token Map for GNS-010

This specification generates the following CCTLS tokens within the CLB-001 framework:

| Token ID | Token Type | Phase | Status | Description |
|---|---|---|---|---|
| `MP-010-GNS-EGNOS-001` | `MISSION_PROFILE` | P010 | DRAFT | Mission profile for EGNOS SoL-dependent operations |
| `METHOD-P040-GNS-RAIM-001` | `METHOD` | P040 | DRAFT | RAIM/FDE analytical method specification |
| `MODEL_SPEC-P040-GNS-DUAL-001` | `MODEL_SPEC` | P040 | DRAFT | Dual-constellation navigation model (GPS+Galileo+EGNOS) |
| `VALIDATION_CASE-P040-GNS-LPV200-001` | `VALIDATION_CASE` | P040 | DRAFT | LPV-200 approach simulation validation case |
| `VALIDATION_CASE-P040-GNS-HAS-001` | `VALIDATION_CASE` | P040 | DRAFT | Galileo HAS convergence validation case |
| `SIM_RUN-P040-GNS-RAIM-AVAIL-001` | `SIM_RUN` | P040 | DRAFT | RAIM availability simulation — ECAC coverage |
| `SIM_RUN-P040-GNS-HAS-CONV-001` | `SIM_RUN` | P040 | DRAFT | HAS convergence time simulation |
| `DOA_SIGN-P050-GNS-010-001` | `DOA_SIGN` | P050 | DRAFT | DOA sign-off for dual-constellation GNSS integration |
| `COMPLIANCE_ITEM-P050-DO229F-001` | `COMPLIANCE_ITEM` | P050 | DRAFT | DO-229F MOPS compliance disposition |
| `COMPLIANCE_ITEM-P050-ED259-001` | `COMPLIANCE_ITEM` | P050 | DRAFT | ED-259 compliance disposition |
| `ICA_TASK-P080-GNS-ANTCAL-001` | `ICA_TASK` | P080 | DRAFT | GNSS antenna calibration ICA task |
| `ICA_TASK-P080-GNS-RECVTEST-001` | `ICA_TASK` | P080 | DRAFT | Receiver functional test ICA task |
| `TRAFFIC_CLEARANCE-P090-EGNOS-OPS-001` | `TRAFFIC_CLEARANCE` | P090 | DRAFT | EGNOS SoL operational approval reference |
| `CYB_CONTROL-P120-OSNMA-001` | `CYB_CONTROL` | P120 | DRAFT | OSNMA authentication control |
| `CYB_CONTROL-P120-GNSS-SPOOF-001` | `CYB_CONTROL` | P120 | DRAFT | GNSS spoofing / jamming mitigation control |

### 7.2 Minimum Evidence Package

The following evidence items are mandatory for GNS-010 package completeness and DOA sign-off:

| Evidence ID | Title | Links to | Acceptance Criterion |
|---|---|---|---|
| `GNS-010-EV-001` | SIS Performance Measurement Report | `SIM_RUN-P040-GNS-RAIM-AVAIL-001` | All SIS bounds in §2.1 demonstrated in operational area |
| `GNS-010-EV-002` | SBAS Receiver Qualification Report (DO-229F) | `COMPLIANCE_ITEM-P050-DO229F-001` | All MOPS §3.2 requirements PASS |
| `GNS-010-EV-003` | Antenna Qualification Record (DO-316) | `DOA_SIGN-P050-GNS-010-001` | EMI/EMC PASS; gain pattern within bounds |
| `GNS-010-EV-004` | System Integration Test Matrix | `VALIDATION_CASE-P040-GNS-LPV200-001` | All integration test cases PASS |
| `GNS-010-EV-005` | GNSS FMEA / RAIM Analysis Report | `HAZARD-P020-GNS-LOSS-001` | All failure modes covered; Pmd ≤ 10⁻³ |
| `GNS-010-EV-006` | SoL Pre-flight Availability Procedure | `ICA_TASK-P080-GNS-RECVTEST-001` | NANU check protocol documented and validated |
| `GNS-010-EV-007` | HAS Convergence Validation Report | `VALIDATION_CASE-P040-GNS-HAS-001` | Convergence ≤ 300 s; HPE ≤ 0.20 m (95%) |
| `GNS-010-EV-008` | OSNMA Integration & Cyber Test Report | `CYB_CONTROL-P120-OSNMA-001` | Authentication latency ≤ 30 s; spoof rejection verified |

### 7.3 Canonical Token Example — VALIDATION_CASE (P040)

```yaml
token:
  token_id:           "VALIDATION_CASE-P040-GNS-LPV200-001"
  token_type:         "VALIDATION_CASE"
  phase:              "P040"
  package_id:         "PKG-P040-METHODS"
  subpackage_id:      "SUBPKG-GNS-VALIDATION"
  aor_id:             "AOR-000300"
  title:              "LPV-200 approach simulation — EGNOS SoL + dual-constellation"
  version:            "0.1.0"
  checksum:           "sha3-512:pending"
  template_id:        "TPL-P040-VALIDATION-001"
  metadata_schema_id: "SCH-P040-VALIDATION-META-001"
  bindings:
    domain:            "AVIATION"
    operation_context: "FLIGHT"
    asset_state:       "AS_FLOWN"
    reuse_cycle_id:    null
    effectivity:       ["ALL"]
    variants:          ["EGNOS-SOL", "GALILEO-HAS-HYBRID"]
  uts_domain:      "010"
  uts_domain_type: "CORE"
  links:
    - rel: "verifies"
      target_token_id: "MODEL_SPEC-P040-GNS-DUAL-001"
    - rel: "supports"
      target_token_id: "DOA_SIGN-P050-GNS-010-001"
  status: "DRAFT"
  created_by: "GNC-Specialist"
  created_at: "2026-02-27T00:00:00Z"
  metadata:
    scenario:          "LPV-200 missed approach at 200ft DH, single GEO failure"
    constellations:    ["GPS-L1/L5", "GALILEO-E1/E5a", "EGNOS-SOL"]
    vpl_threshold_m:   35.0
    hpl_threshold_m:   40.0
    sample_duration_s: 3600
    pass_criteria:
      continuity_risk: "≤ 1e-6 per 150s"
      integrity_risk:  "≤ 2e-7 per approach"
      vpl_breach:      "0 breaches over 3600s"
```

### 7.4 DOA Sign-off Gate Check

The `DOA_SIGN-P050-GNS-010-001` token cannot transition to `CONFIRMED` unless:

```
ACTIVATION_POLICY:
  EXISTS(links[rel='supports' AND target.token_id='SIM_RUN-P040-GNS-RAIM-AVAIL-001'])
  AND EXISTS(links[rel='supports' AND target.token_id LIKE 'VALIDATION_CASE-P040-GNS-%'])
  AND ALL(children[token_type='COMPLIANCE_ITEM'].status IN ['CONFIRMED','ACTIVATED'])
  AND ALL(children[token_type='FINDING'].status = 'CLOSED')
  AND EXISTS(links[rel='supports' AND target.token_id='GNS-010-EV-002'])
  AND EXISTS(links[rel='supports' AND target.token_id='GNS-010-EV-005'])
```

---

## 8. Operational Limits of Use (LoU)

| Code | Limit | Enforcement |
|---|---|---|
| `LoU-010-GNS-001` | EGNOS SoL availability must be confirmed ≥ 1 h before departure for all SoL-dependent operations | Pre-flight check documented in GNS-010-EV-006; NANU archive retained |
| `LoU-010-GNS-002` | Dual-constellation (GPS+Galileo) mandatory for all `FLIGHT` and `LRE` contexts | Receiver qualification to ED-115 / DO-229F Class Beta-3 |
| `LoU-010-GNS-003` | OSNMA authentication must be active for all operations where domain 020 CYB_CONTROL is in force | Receiver must support OSNMA; authentication status logged per flight |
| `LoU-010-GNS-004` | Galileo HAS may only be used as primary positioning source after confirmed convergence | Convergence ≤ 0.20 m CEP; timeout fallback to EGNOS SoL or OS mandatory |
| `LoU-010-GNS-005` | LPV-200 and UAM precision operations require VPL ≤ 35 m continuously; operations must abort if VPL exceeds limit | Monitored in real-time; missed approach mandatory on VPL exceedance |
| `LoU-010-GNS-006` | Non-GNSS reversionary navigation must be demonstrated for all SoL-dependent routes | INS, DME/DME, or VOR/DME backup demonstrated per GNS-010-EV-004 |
| `LoU-010-GNS-007` | Any GNSS software / firmware update triggers re-execution of GNS-010-EV-002 (MOPS re-qualification) | Enforced via CM gate; token version increment mandatory |

---

## 9. Roles & Responsibilities

| Role | Responsibilities |
|---|---|
| **GNC Specialist** | Owns GNS-010 specification; authors VALIDATION_CASE and SIM_RUN tokens; leads RAIM/FDE analysis |
| **Mission Systems Engineer** | Integrates GNSS PNT output into mission planning; owns MISSION_PROFILE token |
| **Systems Integrator** | Leads system integration test campaign (GNS-010-EV-004); owns Integration Test Matrix |
| **Cybersecurity Architect** | Owns OSNMA integration (CYB_CONTROL-P120-OSNMA-001); reviews spoofing threat model |
| **Flight Test Engineer** | Plans and executes P070 flight test campaign for MOPS and LPV-200 validation |
| **DOA Authority** | Signs off DOA_SIGN-P050-GNS-010-001 upon closure of all COMPLIANCE_ITEM and FINDING tokens |

---

## 10. Artefact Structure

```
GNS-010/
├── README.md                                ← this file
├── gns-010-token-manifest.yaml              ← machine-readable token registry
├── evidence/
│   ├── GNS-010-EV-001-sis-performance/
│   ├── GNS-010-EV-002-do229f-qualification/
│   ├── GNS-010-EV-003-antenna-qualification/
│   ├── GNS-010-EV-004-integration-test/
│   ├── GNS-010-EV-005-fmea-raim/
│   ├── GNS-010-EV-006-sol-preflight-procedure/
│   ├── GNS-010-EV-007-has-convergence/
│   └── GNS-010-EV-008-osnma-cyber/
├── simulation/
│   ├── RAIM-availability-ECAC-model/
│   └── HAS-convergence-model/
├── reviews/
│   └── doa-signoff-checklist.md
└── CHANGELOG.md
```

---

## 11. Changelog

| Version | Date | Author | Summary |
|---|---|---|---|
| 0.1.0 | 2026-02-27 | Amedeo Pelliccia | Initial specification — EGNOS/Galileo onboarding into UTS domain 010 |

---

## 12. Glossary of Terms and Acronyms

### 12.1 Acronyms

| Acronym | Expansion |
|---|---|
| **AMC** | Acceptable Means of Compliance |
| **APV** | Approach with Vertical Guidance |
| **AoR** | Area of Responsibility |
| **ATM** | Air Traffic Management |
| **BPSK** | Binary Phase Shift Keying |
| **BCP** | Business Continuity Plan |
| **CAT-I** | Category I (precision approach minima) |
| **CBOC** | Composite Binary Offset Carrier (Galileo E1 modulation) |
| **CCTLS** | Common Civil Transport Lifecycle Standard |
| **CEP** | Circular Error Probable |
| **CLB** | Common Lifecycle Baseline |
| **C/N₀** | Carrier-to-Noise Density Ratio |
| **DAL** | Design Assurance Level |
| **DH** | Decision Height |
| **DME** | Distance Measuring Equipment |
| **DMU** | Digital Mock-Up |
| **DO** | Document (RTCA standard designation) |
| **DOA** | Design Office Authority |
| **ESSA** | European Union Space Safety Agency |
| **EASA** | European Union Aviation Safety Agency |
| **ECAC** | European Civil Aviation Conference |
| **ED** | EUROCAE Document |
| **EGNOS** | European Geostationary Navigation Overlay Service |
| **EKF** | Extended Kalman Filter |
| **EMC** | Electromagnetic Compatibility |
| **EMI** | Electromagnetic Interference |
| **ESG** | Environmental, Social and Governance |
| **EUROCAE** | European Organisation for Civil Aviation Equipment |
| **EUSPA** | European Union Agency for the Space Programme |
| **FDE** | Fault Detection and Exclusion |
| **FMEA** | Failure Modes and Effects Analysis |
| **GEO** | Geostationary Earth Orbit |
| **GGTO** | GPS-to-Galileo Time Offset |
| **GNC** | Guidance, Navigation and Control |
| **GNSS** | Global Navigation Satellite System |
| **GPS** | Global Positioning System |
| **GRAS** | Ground-Based Regional Augmentation System |
| **GSA** | European GNSS Agency (predecessor to EUSPA) |
| **GTRF** | Galileo Terrestrial Reference Frame |
| **HAL** | Horizontal Alert Limit |
| **HAS** | High Accuracy Service (Galileo) |
| **HDOP** | Horizontal Dilution of Precision |
| **HIL** | Hardware-in-the-Loop |
| **HPE** | Horizontal Position Error |
| **HPL** | Horizontal Protection Level |
| **ICAO** | International Civil Aviation Organization |
| **ICA** | Instructions for Continued Airworthiness |
| **IFR** | Instrument Flight Rules |
| **IMU** | Inertial Measurement Unit |
| **INS** | Inertial Navigation System |
| **IPC** | Illustrated Parts Catalogue |
| **IPL** | Illustrated Parts List (shop context) |
| **ITRF** | International Terrestrial Reference Frame |
| **LAAS** | Local Area Augmentation System |
| **LPV** | Localiser Performance with Vertical Guidance |
| **LRE** | Launch and Re-entry (operational context) |
| **MEO** | Medium Earth Orbit |
| **MOPS** | Minimum Operational Performance Standards |
| **MRO** | Maintenance, Repair and Overhaul |
| **NANU** | Notice Advisory to Navstar Users |
| **NPA** | Non-Precision Approach |
| **NPU** | Navigation Processing Unit |
| **NOTAM** | Notice to Air Missions |
| **ODD** | Operational Design Domain |
| **OSNMA** | Open Service Navigation Message Authentication |
| **OS** | Open Service (Galileo) |
| **Pfa** | Probability of False Alert |
| **Pmd** | Probability of Missed Detection |
| **PMU** | Physical Mock-Up |
| **PNT** | Positioning, Navigation and Timing |
| **PPP** | Precise Point Positioning |
| **PPP-RTK** | Precise Point Positioning — Real-Time Kinematic |
| **PRN** | Pseudo-Random Noise (satellite identifier code) |
| **RAIM** | Receiver Autonomous Integrity Monitoring |
| **RSP** | Reusable Space Platform |
| **RTCA** | Radio Technical Commission for Aeronautics |
| **RTCM** | Radio Technical Commission for Maritime Services |
| **SARPS** | Standards and Recommended Practices (ICAO) |
| **SBAS** | Satellite-Based Augmentation System |
| **SDD** | Service Definition Document / Signal-in-Space Interface Control Document |
| **SIS** | Signal-in-Space |
| **SISNET** | SIS Network (EUSPA real-time EGNOS data distribution service) |
| **SoL** | Safety-of-Life (EGNOS service level) |
| **SOTIF** | Safety of the Intended Functionality (ISO 21448) |
| **STM** | Space Traffic Management |
| **TACC** | Time Accuracy |
| **TTFF** | Time-to-First-Fix |
| **UAM** | Urban Air Mobility |
| **UKF** | Unscented Kalman Filter |
| **UTS** | Universal Transport System |
| **UTM** | Unmanned Traffic Management |
| **VAL** | Vertical Alert Limit |
| **VDOP** | Vertical Dilution of Precision |
| **VOR** | VHF Omnidirectional Range |
| **VPE** | Vertical Position Error |
| **VPL** | Vertical Protection Level |
| **WAAS** | Wide Area Augmentation System (US SBAS equivalent) |
| **WGS-84** | World Geodetic System 1984 |
| **XAI** | Explainable Artificial Intelligence |

---

### 12.2 Terms

| Term | Definition |
|---|---|
| **Alert Limit** | The maximum allowable navigation error beyond which an alert must be issued to the crew or system. Defined horizontally (HAL) and vertically (VAL). |
| **Continuity Risk** | The probability that the navigation system will suffer an unscheduled interruption during a critical phase of operation. |
| **Convergence** | The process by which a PPP or PPP-RTK solution achieves its specified accuracy after initial signal acquisition. |
| **Dual-Constellation** | A navigation solution that combines measurements from two independent GNSS constellations (e.g., GPS + Galileo). |
| **Integrity** | A measure of the trust that can be placed in the correctness of the information supplied by a navigation system. |
| **Protection Level** | A statistical bound on the navigation error, computed in real-time, that provides a confidence level consistent with the required integrity risk. |
| **Safety-of-Life (SoL)** | A service level that provides integrity-assured navigation suitable for safety-critical operations such as precision approaches. |
| **Signal-in-Space (SIS)** | The navigation signal as received by the user equipment, characterised by accuracy, availability, continuity and integrity parameters. |

---

## Related Artefacts

| File | Purpose |
|---|---|
| [`gns-010-token-manifest.yaml`](gns-010-token-manifest.yaml) | Machine-readable CCTLS token registry for GNS-010 |
| [`../../UTS/README.md`](../README.md) | UTS domain taxonomy (parent) |
| [`../../UTS/uts-taxonomy.yaml`](../uts-taxonomy.yaml) | Machine-readable taxonomy |
| [`../../EACST/CCTLS.md`](../../EACST/CCTLS.md) | Common Civil Transport Lifecycle Standard |
| [`../../EACST/cctls.yaml`](../../EACST/cctls.yaml) | CCTLS machine-readable specification |
