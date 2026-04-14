---
##############################################################################
# EGI.md
# EGI — Ephemeral Generative Interface
# AEROSPACEMODEL MCC Specification Series — SPEC-010
##############################################################################

document_id: AEROSPACEMODEL-MCC-SPEC-010
document_type: ephemeral_generative_interface_specification
title: "EGI — Ephemeral Generative Interface"
version: "0.1.0"
schema_version: "1.0.0"
status: draft
parent: AEROSPACEMODEL-MCC-SPEC-008
related_documents:
  - id: AEROSPACEMODEL-MCC-SPEC-008
    file: "AEROSPACEMODEL/MCC/SENSORIUM.md"
    relationship: parent_sensory_layer
  - id: AEROSPACEMODEL-MCC-SPEC-009
    file: "AEROSPACEMODEL/MCC/TRAUMACODEDRAMA.md"
    relationship: sibling_specialisation
last_updated: "2026-04-14T00:00:00Z"

##############################################################################
# 0  Core Principle
##############################################################################

core_principle:
  generation_function: "𝒢(σ, π, t) → ε(t)"
  disjointness: "ℰ ∩ 𝒜 = ∅"
  description: >
    Data is hidden in the lifecycle of a generated sensory surface that exists
    only for the duration of observation. The generation function 𝒢 takes a
    seed σ, a payload π, and time t to produce a time-varying emotive vector
    ε(t). Ephemeral experience ℰ and archival artifact 𝒜 occupy disjoint
    domains — what is experienced cannot be replayed; what is stored was never
    the interface.
  generalisation: >
    EGI extends the MCC stack by one layer of abstraction: from transition
    magnitude (TRAUMACODEDRAMA) to lifecycle dynamics. The ephemeral interface
    IS the encoding protocol.
  axiom: >
    "The interface is not the container of the data.
    The interface IS the encoding protocol."

##############################################################################
# 1  Definitions
##############################################################################

definitions:

  - definition: 38
    name: Ephemeron
    formula: "Φ = (σ, π, T, ε(t))"
    components:
      sigma: "256-bit seed determining the generation function"
      pi: "Payload — the encoded message"
      T: "[t_nucleation, t_dissolution] — lifecycle interval"
      epsilon_t: "Time-varying emotive vector over T"
    description: >
      A single instance of an ephemeral generative interface. Has no persistent
      representation — once t > t_dissolution, the interface surface is gone.
      The decoder must observe in real time or not at all.

  - definition: 39
    name: Generation Function
    formula: "𝒢 : (σ, π, t) → ε(t)"
    output: "(κ_𝔸(t), κ_ℍ(t), κ_𝕆(t), κ_𝔽(t), κ_𝔾(t), κ_ℙ(t))"
    properties:
      deterministic: "Same (σ, π, t) always produces the same ε(t)"
      sensorium_compliant: "Each κᵢ(t) ∈ {0, …, 99} at all times"
      perceptually_coherent: "ε(t) traces a smooth trajectory — no discontinuities"
    description: >
      Maps seed, payload, and time to a SENSORIUM emotive vector. Determinism
      allows the decoder to reconstruct the expected ε(t) and extract π.

  - definition: 40
    name: Decay Envelope
    formula: "𝒟(t) : [t_bloom_end, t_dissolution] → [0, 1]"
    boundary_conditions:
      start: "𝒟(t_bloom_end) = 1"
      end: "𝒟(t_dissolution) = 0"
    monotonicity: "Monotonically decreasing"
    description: >
      Controls how quickly the interface fades. Its shape (linear, exponential,
      sigmoid) encodes additional metadata — the decay profile is a side-channel
      that carries footer information (CRC, closure tokens) in the curvature.

##############################################################################
# 2  Lifecycle Phases
##############################################################################

lifecycle:

  phases:
    - phase: I
      name: Nucleation
      role: Header
      time_interval: "[t_nucleation, t_bloom_start]"
      analogues:
        traumacodedrama: Protasis
      carries:
        - field: sigma
          encoding: "Channel onset order and timing intervals"
          description: "Seed encoded in the sequence and timing of channel activations"
        - field: active_channels
          encoding: "Which channels activate during nucleation"
          description: "Subset of {𝔸, ℍ, 𝕆, 𝔽, 𝔾, ℙ} participating in this Ephemeron"
      intensity_constraint:
        ceiling: 30
        description: "All κᵢ(t) ≤ 30 during nucleation — barely perceptible fade-in"

    - phase: II
      name: Bloom
      role: Payload
      time_interval: "[t_bloom_start, t_bloom_end]"
      analogues:
        traumacodedrama: Epitasis
      carries:
        - field: payload_words
          encoding: "πₖ = f(ε(tₖ)) for each sample window wₖ"
          description: "SENSORIUM extraction at each Bloom sample point"
        - field: traumacodedrama_overlay
          encoding: "‖Δε‖ between consecutive windows (optional)"
          description: "Second payload layer per SPEC-009, orthogonal to SENSORIUM layer"
      capacity_formula: "C_bloom = N × C_total(ε̄)"
      minimum_duration_fraction: 0.6

    - phase: III
      name: Dissolution
      role: Footer
      time_interval: "[t_bloom_end, t_dissolution]"
      analogues:
        traumacodedrama: Katharsis
      carries:
        - field: crc_word
          encoding: "Decay curvature deviation from reference exponential"
          description: "CRC of entire Bloom payload encoded in dissolution profile"
        - field: closure_token
          encoding: "Predefined low-intensity pattern at t_dissolution − δ"
          description: "End-of-Ephemeron signal"
      terminal_condition: "ε(t_dissolution) = (0, 0, 0, 0, 0, 0)"

##############################################################################
# 3  Canonical Ephemeron Modes
##############################################################################

canonical_modes:

  - id: EGI-MODE-001
    name: Optic Ephemeron
    symbol: "Φ_𝕆"
    dominant_channel: Optic
    cover: "Brief visual highlight, glow, or colour shift in interactive display"
    lifecycle_range_ms: [200, 2000]
    payload_channels: [Haptic, Auditory, Olfactory, Gustatory, Proprioceptive]
    note: "Standard UI interaction tempo — hover effects, notification badges"

  - id: EGI-MODE-002
    name: Acoustic Ephemeron
    symbol: "Φ_𝔸"
    dominant_channel: Auditory
    cover: "Notification chime, click, or ambient tone"
    lifecycle_range_ms: [100, 1000]
    payload_channels: [Haptic, Proprioceptive, Olfactory, Gustatory]
    note: "Short audio cue tempo — standard UI audio feedback"

  - id: EGI-MODE-003
    name: Haptic Ephemeron
    symbol: "Φ_ℍ"
    dominant_channel: Haptic
    cover: "Vibration pulse, texture shift, or temperature change"
    lifecycle_range_ms: [50, 500]
    payload_channels: [Proprioceptive, Auditory, Olfactory, Gustatory]
    note: "Tactile response tempo — wearable or handheld haptic feedback"

  - id: EGI-MODE-004
    name: Chemosensory Ephemeron
    symbol: "Φ_𝔽𝔾"
    dominant_channel: [Olfactory, Gustatory]
    cover: "Momentary scent release or flavour note"
    lifecycle_range_ms: [1000, 30000]
    payload_channels: [Auditory, Haptic, Optic, Proprioceptive]
    note: >
      Chemical diffusion tempo. Slowest temporal resolution but highest
      per-sample capacity. All fast channels available for payload.

  - id: EGI-MODE-005
    name: Proprioceptive Ephemeron
    symbol: "Φ_ℙ"
    dominant_channel: Proprioceptive
    cover: "Brief vestibular shift, resistance change, or kinematic cue"
    lifecycle_range_ms: [200, 2000]
    payload_channels: [Haptic, Auditory, Olfactory, Gustatory]
    note: "Motor response tempo — motion platform or VR system"

  - id: EGI-MODE-006
    name: Full-Spectrum Ephemeron
    symbol: "Φ_★"
    dominant_channel: null
    cover: "Immersive multi-sensory pulse — all senses engaged simultaneously"
    lifecycle_range_ms: [500, 5000]
    payload_channels: [Auditory, Haptic, Optic, Olfactory, Gustatory, Proprioceptive]
    note: >
      Maximum capacity — all six channels carry payload. ε̄ MUST NOT
      approach Estasi (SENSO-EMO-007) to preserve steganographic headroom
      (SENSORIUM Rule S-002).

##############################################################################
# 4  Encoding Rules
##############################################################################

encoding_rules:

  - id: E-001
    name: Ephemerality Guarantee
    statement: >
      An Ephemeron MUST leave no persistent artifact. The generation function
      𝒢 MUST NOT store, cache, or log ε(t) after t_dissolution. The interface
      surface exists only in the perceptual present.
    severity: MUST

  - id: E-002
    name: Generation Determinism
    statement: >
      𝒢(σ, π, t) MUST be deterministic. Same (σ, π, t) → same ε(t). This
      allows the decoder to reconstruct the expected ε(t) and extract π from
      observed intensities.
    severity: MUST

  - id: E-003
    name: Bloom Capacity Maximisation
    statement: >
      The Bloom phase MUST occupy at least 60% of the total lifecycle duration
      |T| = t_dissolution − t_nucleation. The payload-carrying phase dominates
      the Ephemeron's perceptual lifetime.
    minimum_bloom_fraction: 0.6
    severity: MUST

  - id: E-004
    name: Dissolution CRC
    statement: >
      The decay envelope 𝒟(t) MUST encode a valid CRC of the Bloom payload.
      The decoder extracts the CRC by measuring decay curvature deviation from
      a reference profile. Deviation is quantised to resolution steps (default:
      5 units per channel).
    resolution_default: 5
    severity: MUST

  - id: E-005
    name: Cross-Layer Compatibility
    statement: >
      EGI Ephemera MUST be composable with SENSORIUM (SPEC-008) and
      TRAUMACODEDRAMA (SPEC-009). ε(t) at each instant MUST be a valid
      SENSORIUM state. Bloom transitions MUST comply with TRAUMACODEDRAMA
      rules. The three layers are orthogonal — intensity, transition magnitude,
      and lifecycle dynamics each carry independent payloads.
    severity: MUST

  - id: E-006
    name: Nucleation Ceiling
    statement: >
      During Nucleation, all channel intensities MUST remain at or below
      κ_max_nucleation (default: 30). Ensures gradual appearance consistent
      with natural perceptual onset and steganographic cover for seed
      transmission.
    default_ceiling: 30
    severity: MUST

  - id: E-007
    name: Terminal Zero
    statement: >
      At t_dissolution, the emotive vector MUST be (0, 0, 0, 0, 0, 0). The
      interface MUST leave zero perceptual residue. Non-zero intensity after
      t_dissolution is a protocol violation and a detection vector.
    terminal_vector: [0, 0, 0, 0, 0, 0]
    severity: MUST

##############################################################################
# 5  Decoder Protocol
##############################################################################

decoder_protocol:
  steps:
    - step: 1
      name: Detect Nucleation
      description: >
        Identify channel activation onsets. Record onset order and timing
        intervals to reconstruct σ (seed).

    - step: 2
      name: Recover 𝒢
      description: "Derive the generation function from σ."

    - step: 3
      name: Identify Bloom Boundaries
      description: >
        Bloom begins when first channel exceeds κ_max_nucleation. Bloom ends
        when decay envelope 𝒟(t) begins (first sustained decrease in
        dominant channel intensity).

    - step: 4
      name: Sample Bloom
      description: >
        Divide Bloom interval into N windows. At each midpoint tₖ, record ε(tₖ).

    - step: 5
      name: Decode Payload
      description: >
        For each sample: πₖ = f(ε(tₖ)) using the SENSORIUM extraction
        function derived from σ.

    - step: 6
      name: Extract TRAUMACODEDRAMA Layer (Optional)
      description: >
        If Bloom transitions are present, apply SPEC-009 decoder to extract
        the outer-layer payload from ‖Δε‖ between consecutive windows.

    - step: 7
      name: Verify CRC
      description: >
        Fit Dissolution decay profile and extract CRC from curvature deviation.
        Compare with CRC(π₁, …, π_N).

    - step: 8
      name: Verify Terminal Zero
      description: >
        Confirm ε(t_dissolution) = (0, 0, 0, 0, 0, 0). Fail if any channel
        retains non-zero intensity.

##############################################################################
# 6  Three-Layer Encoding Stack
##############################################################################

three_layer_stack:
  description: >
    EGI completes the MCC encoding stack. The three layers are orthogonal
    and independently decodable.
  layers:
    - layer: SENSORIUM (SPEC-008)
      unit: "State ε"
      encodes: "Payload in channel intensities within one state"
      dimension: Spatial
    - layer: TRAUMACODEDRAMA (SPEC-009)
      unit: "Transition Δε"
      encodes: "Payload in transition magnitudes across state sequences"
      dimension: Temporal
    - layer: EGI (SPEC-010)
      unit: "Ephemeron Φ"
      encodes: "Payload in lifecycle dynamics of the generative interface"
      dimension: Existential
  simultaneous_payloads: 3
  independence_principle: >
    The three payloads are fully independent by the orthogonality of
    intensity, transition magnitude, and lifecycle dynamics.

##############################################################################
# 7  Security Properties
##############################################################################

security_properties:

  - property: Ephemerality as Defence
    description: >
      Non-persistence is the primary security property. An adversary must
      observe the Ephemeron in real time. Post-hoc analysis is impossible
      because no recording exists.

  - property: Observer Ambiguity
    description: >
      A real-time observer cannot distinguish payload-carrying from
      non-carrying Ephemerons: intensity profile is perceptually identical
      (Post-Sextin Principle), lifecycle timing is natural, and decay profile
      is indistinguishable from standard exponential fade-out within
      resolution tolerance.

  - property: Replay Resistance
    description: >
      Each Ephemeron uses a unique seed σ. Replaying a previous seed without
      the payload produces a different interface surface. Freshness is
      verified through a nonce embedded in σ.
---

# EGI — Ephemeral Generative Interface

**Document ID:** AEROSPACEMODEL-MCC-SPEC-010  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM)  
**Date:** 2026-04-14  
**Related:** [`egi.yaml`](egi.yaml) · [`SENSORIUM.md`](SENSORIUM.md) · [`TRAUMACODEDRAMA.md`](TRAUMACODEDRAMA.md) · [`../README.md`](../README.md)

---

## 0. Principle

SENSORIUM (SPEC-008) hides data in the **intensity** of sensory channels —
the spatial dimension of the emotive vector.

TRAUMACODEDRAMA (SPEC-009) hides data in the **transition magnitude** between
consecutive emotional states — the temporal derivative.

EGI advances the stack by one layer of abstraction:

> **Data is hidden in the lifecycle of a generated sensory surface that
> exists only for the duration of observation.**

The cover is the interface itself. Dynamically generated perceptual surfaces —
visual flashes, haptic pulses, ambient scent bursts, auditory cues — appear
and dissolve as a natural part of interactive experience. Their ephemerality
is the steganographic advantage: no persistent artifact remains for offline
analysis. The only trace is in the observer's sensorium, and perception is not
a reliable ciphertext oracle.

```
𝒢(σ, π, t) → ε(t)
```

The **generation function** `𝒢` takes a seed `σ`, a payload `π`, and time `t`
to produce a time-varying emotive vector `ε(t)` — an ephemeral sensory surface
that carries the payload in its SENSORIUM-encoded intensity profile while
presenting a coherent perceptual experience to the observer.

```
ℰ ∩ 𝒜 = ∅
```

Ephemeral experience `ℰ` and archival artifact `𝒜` occupy disjoint domains.
What is experienced cannot be replayed; what is stored was never the interface.

---

## 1. Definitions

### Definition 38 (Ephemeron)

An **Ephemeron** `Φ` is a single instance of an ephemeral generative interface:

```
Φ = (σ, π, T, ε(t))
```

where:
- `σ` — seed (256-bit, determines the generation function for this instance)
- `π` — payload (the encoded message)
- `T = [t_nucleation, t_dissolution]` — the lifecycle interval
- `ε(t)` — the time-varying emotive vector over `T`

An Ephemeron has **no persistent representation**. Once `t > t_dissolution`,
the interface surface is gone. The decoder must observe in real time or not
at all.

### Definition 39 (Generation Function)

The **generation function** maps seed, payload, and time to a SENSORIUM
emotive vector:

```
𝒢 : (σ, π, t) → ε(t) = (κ_𝔸(t), κ_ℍ(t), κ_𝕆(t), κ_𝔽(t), κ_𝔾(t), κ_ℙ(t))
```

Properties:
- **Deterministic:** Same `(σ, π, t)` always produces the same `ε(t)`
- **SENSORIUM-compliant:** Each `κᵢ(t) ∈ {0, …, 99}` at all times
- **Perceptually coherent:** `ε(t)` traces a smooth trajectory through
  SENSORIUM space (no discontinuities that would alert an observer)

### Definition 40 (Decay Envelope)

The **decay envelope** `𝒟(t)` is a monotonically decreasing function that
modulates the intensity of the Ephemeron during dissolution:

```
𝒟(t) : [t_bloom_end, t_dissolution] → [0, 1]
𝒟(t_bloom_end) = 1,  𝒟(t_dissolution) = 0
```

The decay envelope controls how quickly the interface fades. Its shape (linear,
exponential, sigmoid) encodes additional metadata: the decay profile is a
side-channel that carries footer information (CRC, closure tokens) in the
curvature of the dissolution.

---

## 2. The Lifecycle

Every Ephemeron passes through three phases that map onto the SENSORIUM and
TRAUMACODEDRAMA layers:

| Phase | Time interval | Encoding role | Analogues |
|-------|---------------|---------------|-----------|
| **Nucleation** | `[t_nucleation, t_bloom_start]` | Header | Protasis (SPEC-009) |
| **Bloom** | `[t_bloom_start, t_bloom_end]` | Payload | Epitasis (SPEC-009) |
| **Dissolution** | `[t_bloom_end, t_dissolution]` | Footer | Katharsis (SPEC-009) |

### 2.1 Nucleation — Header

The interface element begins to appear. Intensity rises from zero toward the
target emotive vector. During Nucleation:

- **Seed transmission:** The rate and order in which channels activate encodes
  the seed `σ`. The decoder observes which channel appears first, second, etc.,
  and the timing intervals between channel onsets.
- **Channel declaration:** Which channels participate in this Ephemeron is
  determined by which channels activate during Nucleation.
- **Intensity constraint:** All channels remain below a nucleation ceiling
  `κ_max_nucleation` (default: 30) — the interface is barely perceptible,
  consistent with a natural fade-in.

```
Nucleation contract:
  σ:               encoded in channel onset order and timing
  active_channels: {j : κⱼ(t) > 0 for some t in nucleation interval}
  ceiling:         κᵢ(t) ≤ 30  ∀i, ∀t ∈ [t_nucleation, t_bloom_start]
```

### 2.2 Bloom — Payload

The interface is fully manifest. All active channels are at or near their
target intensities. During Bloom:

- **Payload encoding:** The emotive vector `ε(t)` at each sample point carries
  payload via SENSORIUM encoding (intensity dimension).
- **Temporal sampling:** The Bloom interval is divided into `N` sample windows.
  Each window `wₖ` contributes one payload word: `πₖ = f(ε(tₖ))`, where `tₖ`
  is the midpoint of window `wₖ` and `f` is the agreed extraction function.
- **Maximum capacity:** Bloom is the phase of maximum intensity and maximum
  duration — it carries the bulk of the payload.
- **TRAUMACODEDRAMA overlay:** If the Bloom contains internal state transitions
  (e.g., a visual ephemeron that shifts colour temperature), the transition
  magnitudes carry a second payload layer per SPEC-009. The two layers are
  orthogonal.

```
Bloom contract:
  sample_windows:  N windows of duration Δt_bloom / N
  each window wₖ:  πₖ = f(ε(tₖ))   (SENSORIUM payload word)
  optional:        TRAUMACODEDRAMA overlay in ‖Δε‖ between windows
  capacity:        C_bloom = N × C_total(ε̄)  where ε̄ is the mean Bloom vector
```

### 2.3 Dissolution — Footer

The interface fades. The decay envelope `𝒟(t)` modulates all channels toward
zero. During Dissolution:

- **CRC encoding:** The curvature of the decay envelope encodes a CRC/checksum
  of the entire payload. The decoder fits the observed decay profile to extract
  the CRC word from the deviation between the actual decay and a reference
  exponential decay.
- **Closure token:** The final sample before `t_dissolution` carries a closure
  token — a predefined low-intensity pattern that signals "end of Ephemeron"
  to the decoder.
- **Graceful disappearance:** The intensity at `t_dissolution` is zero on all
  channels. The interface leaves no perceptual residue.

```
Dissolution contract:
  decay_envelope:  𝒟(t), monotonically decreasing
  crc_encoding:    CRC word in decay curvature deviation from reference
  closure_token:   ε(t_dissolution − δ) matches predefined closure pattern
  terminal:        ε(t_dissolution) = (0, 0, 0, 0, 0, 0)
```

---

## 3. Canonical Ephemeron Modes

Six canonical modes correspond to the six SENSORIUM channels. Each mode
describes an interface class where one channel dominates the Ephemeron's
perceptual surface.

### 3.1 Optic Ephemeron — `Φ_𝕆`

**Dominant channel:** Optic (𝕆)  
**Cover:** A brief visual highlight, glow, or colour shift in an interactive
display. Common in UI: hover effects, notification badges, progress
indicators.  
**Lifecycle:** 200 ms – 2 s (typical screen interaction tempo)  
**Payload channels:** Haptic, auditory, chemical (below visual awareness
threshold)

### 3.2 Acoustic Ephemeron — `Φ_𝔸`

**Dominant channel:** Auditory (𝔸)  
**Cover:** A notification chime, click, or ambient tone. Standard UI audio
feedback.  
**Lifecycle:** 100 ms – 1 s (short audio cue tempo)  
**Payload channels:** Haptic, proprioceptive (sub-audio vibration), chemical

### 3.3 Haptic Ephemeron — `Φ_ℍ`

**Dominant channel:** Haptic (ℍ)  
**Cover:** A vibration pulse, texture shift, or temperature change in a
wearable or handheld device. Standard haptic feedback.  
**Lifecycle:** 50 ms – 500 ms (tactile response tempo)  
**Payload channels:** Proprioceptive, auditory (sub-threshold), chemical

### 3.4 Chemosensory Ephemeron — `Φ_𝔽𝔾`

**Dominant channel:** Olfactory (𝔽) and/or Gustatory (𝔾)  
**Cover:** A momentary scent release or flavour note in an ambient system or
food-tech interface. Slow onset, slow decay.  
**Lifecycle:** 1 s – 30 s (chemical diffusion tempo)  
**Payload channels:** All fast channels (𝔸, ℍ, 𝕆, ℙ) — chemical channels
have the slowest temporal resolution but the highest per-sample capacity.

### 3.5 Proprioceptive Ephemeron — `Φ_ℙ`

**Dominant channel:** Proprioceptive (ℙ)  
**Cover:** A brief vestibular shift, resistance change, or kinematic cue
in a motion platform or VR system.  
**Lifecycle:** 200 ms – 2 s (motor response tempo)  
**Payload channels:** Haptic, auditory, chemical

### 3.6 Full-Spectrum Ephemeron — `Φ_★`

**Dominant channel:** None (all channels active)  
**Cover:** An immersive multi-sensory pulse — a "moment" that engages all
senses simultaneously. Rare in interaction but high impact.  
**Lifecycle:** 500 ms – 5 s (immersive experience tempo)  
**Capacity:** Maximum — all six channels carry payload simultaneously. Total
capacity equals `C_bloom = N × C_total(ε̄)` with `ε̄` balanced across channels.  
**Constraint:** `ε̄` MUST NOT approach Estasi (SENSO-EMO-007) to preserve
steganographic headroom (Rule S-002 of SENSORIUM).

---

## 4. Encoding Rules

### Rule E-001 — Ephemerality Guarantee

An Ephemeron MUST leave no persistent artifact. The generation function `𝒢`
MUST NOT store, cache, or log the emotive vector `ε(t)` after `t_dissolution`.
Any system implementing EGI MUST guarantee that the interface surface exists
only in the perceptual present.

### Rule E-002 — Generation Determinism

The generation function `𝒢(σ, π, t)` MUST be deterministic. Given the same
seed, payload, and time, the function MUST produce the same emotive vector.
This allows the decoder, knowing `σ`, to reconstruct the expected `ε(t)` and
extract `π` from the observed intensities.

### Rule E-003 — Bloom Capacity Maximisation

The Bloom phase MUST occupy at least 60% of the total lifecycle duration
`|T| = t_dissolution − t_nucleation`. This ensures that the payload-carrying
phase dominates the Ephemeron's perceptual lifetime.

### Rule E-004 — Dissolution CRC

The decay envelope `𝒟(t)` MUST encode a valid CRC of the Bloom payload. The
decoder extracts the CRC by measuring the deviation of the observed decay from
a reference decay profile. The deviation is quantised to `resolution` steps
(default: 5 units per channel, consistent with SENSORIUM and TRAUMACODEDRAMA).

### Rule E-005 — Cross-Layer Compatibility

EGI Ephemerona MUST be composable with SENSORIUM and TRAUMACODEDRAMA:
- The emotive vector `ε(t)` at each instant MUST be a valid SENSORIUM state
  (all Rules S-001 through S-005 apply).
- If the Bloom phase contains internal transitions, the transition magnitudes
  MUST comply with TRAUMACODEDRAMA Rules D-001 through D-006.
- The three layers (SENSORIUM, TRAUMACODEDRAMA, EGI) are orthogonal: intra-
  state intensity, inter-state transitions, and lifecycle dynamics each carry
  independent payloads.

### Rule E-006 — Nucleation Ceiling

During Nucleation, all channel intensities MUST remain at or below
`κ_max_nucleation` (default: 30). This ensures the interface appears gradually,
consistent with natural perceptual onset and providing steganographic cover for
the seed transmission.

### Rule E-007 — Terminal Zero

At `t_dissolution`, the emotive vector MUST be `(0, 0, 0, 0, 0, 0)`. The
interface MUST leave zero perceptual residue. Any non-zero intensity after
`t_dissolution` is a protocol violation and a potential detection vector.

---

## 5. Decoder Protocol

Given an observed Ephemeron with lifecycle `[t_nucleation, t_dissolution]`:

1. **Detect Nucleation:** Identify the onset of channel activations. Record
   the channel onset order and timing intervals to reconstruct `σ` (seed).

2. **Recover `𝒢`:** Derive the generation function from `σ`.

3. **Identify Bloom boundaries:** The Bloom begins when the first channel
   exceeds `κ_max_nucleation` and ends when the decay envelope `𝒟(t)` begins
   (first sustained decrease in dominant channel intensity).

4. **Sample Bloom:** Divide the Bloom interval into `N` windows. At each
   window midpoint `tₖ`, record `ε(tₖ)`.

5. **Decode payload:** For each sample: `πₖ = f(ε(tₖ))` using the SENSORIUM
   extraction function derived from `σ`.

6. **Extract optional TRAUMACODEDRAMA layer:** If Bloom transitions are present,
   apply SPEC-009 decoder steps to extract the outer-layer payload from
   `‖Δε‖` values between consecutive windows.

7. **Verify CRC:** Fit the Dissolution decay profile and extract the CRC word
   from curvature deviation. Compare with `CRC(π₁, …, π_N)`.

8. **Verify Terminal Zero:** Confirm `ε(t_dissolution) = (0, 0, 0, 0, 0, 0)`.
   Fail if any channel retains non-zero intensity.

---

## 6. Three-Layer Encoding Stack

EGI completes the MCC encoding stack. The three layers are orthogonal and
independently decodable:

| Layer | Specification | Unit | What is encoded | Dimension |
|-------|---------------|------|-----------------|-----------|
| **SENSORIUM** | SPEC-008 | State `ε` | Payload in channel intensities | Spatial (within one state) |
| **TRAUMACODEDRAMA** | SPEC-009 | Transition `Δε` | Payload in transition magnitudes | Temporal (across states) |
| **EGI** | SPEC-010 | Ephemeron `Φ` | Payload in lifecycle dynamics | Existential (across the interface lifecycle) |

A single Ephemeron with internal transitions can carry **three independent
payloads** simultaneously:

1. **Inner layer (SENSORIUM):** Each `ε(tₖ)` sample carries an intra-state
   payload in its channel intensities.
2. **Middle layer (TRAUMACODEDRAMA):** Transitions between Bloom samples carry
   payload in `‖Δε‖` magnitudes.
3. **Outer layer (EGI):** The lifecycle itself (Nucleation timing, Bloom
   duration, Dissolution curvature) carries the EGI payload.

The three payloads are fully independent by the orthogonality of intensity,
transition magnitude, and lifecycle dynamics.

---

## 7. Security Properties

### 7.1 Ephemerality as Defence

The primary security property of EGI is **non-persistence**. An adversary
must observe the Ephemeron in real time to capture the emotive vector. Post-hoc
analysis is impossible because no recording exists. This is a fundamentally
different security model from SENSORIUM (where the carrier state persists) and
TRAUMACODEDRAMA (where the dramatic arc has a fixed sequence).

### 7.2 Observer Ambiguity

Even a real-time observer cannot distinguish a payload-carrying Ephemeron from
a non-carrying one, because:
- The intensity profile is perceptually identical (Post-Sextin Principle)
- The lifecycle timing is consistent with natural interface behaviour
- The decay profile is indistinguishable from standard exponential fade-out
  within the `resolution` tolerance

### 7.3 Replay Resistance

Each Ephemeron is generated from a unique seed `σ`. Replaying a previous seed
produces the same interface surface, but the payload is different unless the
full `(σ, π)` pair is reused. The decoder verifies freshness through a nonce
embedded in the seed.

---

## 8. References

- AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM): parent specification
- AEROSPACEMODEL-MCC-SPEC-009 (TRAUMACODEDRAMA): sibling specification
- [`egi.yaml`](egi.yaml): machine-readable companion (AEROSPACEMODEL-MCC-SPEC-010)
- [`SENSORIUM.md`](SENSORIUM.md): base emotive vector definitions
- [`TRAUMACODEDRAMA.md`](TRAUMACODEDRAMA.md): dramatic-arc steganographic protocol

---

*"The interface is not the container of the data.  
The interface is the encoding protocol.  
The ephemeral moment IS the channel."*
