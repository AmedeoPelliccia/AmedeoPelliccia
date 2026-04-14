---
##############################################################################
# sensorium.yaml
# SENSORIUM — Multi-Sensory Cryptographic Composition
# AEROSPACEMODEL MCC Specification Series — SPEC-008
##############################################################################

document_id: AEROSPACEMODEL-MCC-SPEC-008
document_type: multi_sensory_cryptographic_specification
title: "SENSORIUM — Multi-Sensory Cryptographic Composition"
version: "0.1.0"
schema_version: "1.0.0"
status: draft
parent: AEROSPACEMODEL-MCC-SPEC-001
related_documents:
  - id: AEROSPACEMODEL-MCC-SPEC-000
    file: "AEROSPACEMODEL/MCC/POST-SEXTIN-PRINCIPLE.md"
    relationship: foundational_axiom
  - id: AEROSPACEMODEL-MCC-SPEC-007
    title: "MUSIC-MCC"
    relationship: parent_specialisation
  - id: PLUMA-GAI-HIV-001
    file: "00-PROGRAM/PLUMA-GAI/H.I.V.md"
    relationship: analogue_sensing_layer
  - id: PLUMA-GAI-VBZ-001
    file: "00-PROGRAM/PLUMA-GAI/VibidratAZIONE.md"
    relationship: restoration_layer
last_updated: "2026-04-04T00:00:00Z"

##############################################################################
# 0  The Post-Sextin Principle
##############################################################################

post_sextin_principle:
  statement: "𝒫 ∩ ℰ = ∅"
  description: >
    Payload and expression occupy disjoint dimensions. In audio, velocity
    carries data while melody, harmony, rhythm, texture carry emotion.
    This principle is sense-agnostic and applies to any perceptual channel
    where humans distinguish intensity from identity.
  generalisation: >
    SENSORIUM generalises MUSIC-MCC from one sense to all six.
    Intensity is the universal steganographic channel.

##############################################################################
# 1  Six Channels
##############################################################################

channels:
  - index: 1
    name: Auditory
    latin: audītus
    symbol: "𝔸"
    receptor: Cochlea
    intensity_dimension: "Velocity / amplitude"
    expression_dimension: "Pitch, melody, harmony, rhythm"

  - index: 2
    name: Haptic
    latin: tāctus
    symbol: "ℍ"
    receptor: Mechanoreceptors
    intensity_dimension: "Pressure / vibration magnitude"
    expression_dimension: "Texture, location, gesture"

  - index: 3
    name: Optic
    latin: vīsus
    symbol: "𝕆"
    receptor: Retina
    intensity_dimension: "Luminance / contrast"
    expression_dimension: "Hue, saturation, shape, motion"

  - index: 4
    name: Olfactory
    latin: olfactus
    symbol: "𝔽"
    receptor: Olfactory epithelium
    intensity_dimension: "Concentration"
    expression_dimension: "Molecular identity (scent profile)"
    steganographic_priority: high    # low temporal resolution → high capacity

  - index: 5
    name: Gustatory
    latin: gustātus
    symbol: "𝔾"
    receptor: Taste buds
    intensity_dimension: "Intensity"
    expression_dimension: "Taste identity (flavour profile)"
    steganographic_priority: high    # low temporal resolution → high capacity

  - index: 6
    name: Proprioceptive
    latin: sensus motūs
    symbol: "ℙ"
    receptor: "Muscle spindles, vestibular"
    intensity_dimension: "Effort / acceleration"
    expression_dimension: "Posture, direction, coordination"

##############################################################################
# 2  Emotive Vector — Definition 35
##############################################################################

emotive_vector:
  definition: 35
  name: "Emotive Vector"
  formula: "ε = (κ_𝔸, κ_ℍ, κ_𝕆, κ_𝔽, κ_𝔾, κ_ℙ)"
  domain: "κᵢ ∈ {0, …, 99}"
  description: >
    An emotive expression is a vector of sensory intensities in
    six-dimensional SENSORIUM space. The radar polygon of ε IS the
    geometric signature of the emotion — not a representation, but
    its mathematical definition.

  scalar_properties:
    magnitude:
      formula: "‖ε‖ = √(Σ κᵢ²)"
      interpretation: "Total sensory intensity; measures arousal level"
    dominant_sense:
      formula: "argmax(κᵢ)"
      interpretation: "The channel that leads the experience"
    centroid:
      formula: "μ = (Σ κᵢ) / 6"
      interpretation: "Mean activation; measures emotional breadth"
    entropy:
      formula: "H(ε) = −Σ p̂ᵢ log p̂ᵢ  where  p̂ᵢ = κᵢ / Σκ"
      interpretation: "Distribution uniformity; high in Estasi, low in Nostalgia"

  steganographic_capacity:
    per_channel:
      formula: "C_i(ε) = 99 − κᵢ"
      interpretation: "Residual intensity headroom for payload embedding"
    total:
      formula: "C_total(ε) = Σ C_i(ε) = 594 − Σ κᵢ"
      interpretation: >
        Total steganographic headroom. Estasi → minimum; Malinconia → maximum.
        Carrier state selection is a security parameter of the composition.

##############################################################################
# 3  Canonical Emotion Catalogue
##############################################################################

canonical_emotions:

  - id: SENSO-EMO-001
    name_it: Gioia
    name_en: Joy
    vector:
      auditory:       85
      haptic:         60
      optic:          90
      olfactory:      45
      gustatory:      70
      proprioceptive: 80
    magnitude: 180
    dominant_sense: Optic
    description: >
      Bright, expansive, rhythmic. High visual and auditory intensity,
      moderate warmth across all senses. The body moves. All senses present.
    steganographic_note: "Moderate capacity; chemical channels (𝔽=45, 𝔾=70) usable"

  - id: SENSO-EMO-002
    name_it: Serenità
    name_en: Serenity
    vector:
      auditory:       50
      haptic:         45
      optic:          55
      olfactory:      40
      gustatory:      38
      proprioceptive: 48
    magnitude: 118
    dominant_sense: Optic
    description: >
      Still and open. Low total activation; no channel dominates strongly.
      The body is present but unhurried. Maximum available steganographic headroom
      across all channels.
    steganographic_note: "High capacity; all channels well below saturation"

  - id: SENSO-EMO-003
    name_it: Malinconia
    name_en: Melancholy
    vector:
      auditory:       30
      haptic:         20
      optic:          55
      olfactory:      25
      gustatory:      15
      proprioceptive: 30
    magnitude: 80
    dominant_sense: Optic
    description: >
      A thin blue shape. Vision remains — the world is seen — but haptic and
      gustatory signals fade. The body is quiet; taste is absent.
      Highest total steganographic headroom of all canonical states.
    steganographic_note: "Maximum total capacity; low arousal, wide embedding bandwidth"

  - id: SENSO-EMO-004
    name_it: Terrore
    name_en: Terror
    vector:
      auditory:       90
      haptic:         95
      optic:          70
      olfactory:       5
      gustatory:        5
      proprioceptive: 92
    magnitude: 178
    dominant_sense: Haptic
    description: >
      Near-hexagon with chemical void. The body electrifies (haptic 95,
      proprioceptive 92, auditory 90). The slow chemical senses disappear.
      High arousal, but maximum headroom on olfactory and gustatory channels.
    steganographic_note: >
      Paradox state: high arousal yet maximum chemical channel capacity (𝔽=5, 𝔾=5).
      Viable carrier for high-bandwidth payloads on chemical channels.

  - id: SENSO-EMO-005
    name_it: Meraviglia
    name_en: Wonder
    vector:
      auditory:       55
      haptic:         35
      optic:          78
      olfactory:      25
      gustatory:      20
      proprioceptive: 68
    magnitude: 137
    dominant_sense: Optic
    description: >
      Asymmetric. Vision expands (78); the body orients (proprioceptive 68);
      sound is present but not dominant. Chemical senses recede.
      Wonder is the posture of seeing something new.
    steganographic_note: "Good capacity on haptic and chemical channels"

  - id: SENSO-EMO-006
    name_it: Tenerezza
    name_en: Tenderness
    vector:
      auditory:       40
      haptic:         85
      optic:          40
      olfactory:      32
      gustatory:      30
      proprioceptive: 60
    magnitude: 131
    dominant_sense: Haptic
    description: >
      Touch dominates. The voice softens (auditory 40). The body leans
      forward (proprioceptive 60). Chemical senses present, warm.
      Tenerezza is a state of proximity.
    steganographic_note: "Good capacity on auditory, optic, and chemical channels"

  - id: SENSO-EMO-007
    name_it: Estasi
    name_en: Ecstasy
    vector:
      auditory:       80
      haptic:         82
      optic:          85
      olfactory:      75
      gustatory:      78
      proprioceptive: 80
    magnitude: 186
    dominant_sense: Optic
    description: >
      The limit case. All channels near maximum. The sensorium is flooded.
      Minimum steganographic capacity — when everything is at maximum, no
      intensity gradient remains to hide data.
    steganographic_note: >
      PROHIBITED as carrier state (Rule S-002) for any non-trivial payload.
      Minimum C_total ≈ 594 − 480 = 114.

  - id: SENSO-EMO-008
    name_it: Nostalgia
    name_en: Nostalgia
    vector:
      auditory:       40
      haptic:         30
      optic:          40
      olfactory:      80
      gustatory:      60
      proprioceptive: 20
    magnitude: 117
    dominant_sense: Olfactory
    description: >
      A triangle pointing toward olfactory (80) and gustatory (60). The
      chemical senses dominate — aroma triggers memory. Vision blurs (40).
      The body stills (proprioceptive 20). Nostalgia is the state where
      smell and taste reconstruct what the eyes can no longer see.
    steganographic_note: "Maximum capacity on fast channels (ℍ, ℙ, 𝔸); chemical channels occupied"

##############################################################################
# 4  Steganographic Composition Rules
##############################################################################

composition_rules:

  - id: S-001
    name: Payload Orthogonality
    statement: >
      The payload MUST be encoded in the intensity dimension (κᵢ) of each
      channel. It MUST NOT alter the identity (expression) dimension.
      Violation destroys the experiential surface and renders the composition
      detectable.
    severity: MUST

  - id: S-002
    name: Carrier State Selection
    statement: >
      The carrier emotional state ε MUST be selected such that
      C_total(ε) ≥ B, where B is the payload bit-length. Estasi
      (SENSO-EMO-007) is PROHIBITED as a carrier for any non-trivial payload.
    severity: MUST

  - id: S-003
    name: Dominant Sense Integrity
    statement: >
      The dominant sense (argmax κᵢ) MUST NOT change between the plain
      surface and the steganographic composition. A shift in dominant sense
      is perceptible as an emotional shift and constitutes a detectable
      anomaly.
    severity: MUST

  - id: S-004
    name: Magnitude Tolerance
    statement: >
      The magnitude ‖ε‖ MAY change by at most ±3% without perceptible
      arousal shift in calibrated human observers. Payload embedding MUST be
      distributed across channels to stay within this tolerance.
    tolerance_percent: 3
    severity: MUST

  - id: S-005
    name: Chemical Channel Priority
    statement: >
      Olfactory (𝔽) and gustatory (𝔾) channels have the lowest temporal
      resolution. They are the highest-capacity steganographic channels when
      not assigned primary emotional role (κ_𝔽 < 50 AND κ_𝔾 < 50). In
      Terrore, both chemical channels near zero — maximum chemical channel
      capacity — making it a viable carrier despite high arousal.
    priority: high
    severity: SHOULD

##############################################################################
# 5  Axis Ordering Convention
##############################################################################

axis_ordering:
  description: >
    Six axes at 60° intervals. Chemosensory axes (𝔽, 𝔾) placed opposite
    physical-action axes (𝔸, ℍ), with optic and proprioceptive at vertical poles.
  order:
    - position: top
      channel: Optic
      symbol: "𝕆"
    - position: upper_right
      channel: Auditory
      symbol: "𝔸"
    - position: lower_right
      channel: Haptic
      symbol: "ℍ"
    - position: bottom
      channel: Proprioceptive
      symbol: "ℙ"
    - position: lower_left
      channel: Gustatory
      symbol: "𝔾"
    - position: upper_left
      channel: Olfactory
      symbol: "𝔽"

##############################################################################
# 6  Integration — PLUMA-GAI H.I.V. Correspondence
##############################################################################

pluma_gai_hiv_correspondence:
  description: >
    The SENSORIUM model maps onto the PLUMA-GAI canonical thread,
    extending the H.I.V. specification with a multi-sensory interpretation.
  mappings:
    - sensorium_channel: "𝔸 Auditory — signal propagation"
      hiv_analogue: "H₂ flow rate signal"
      pluma_gai_layer: TranshidreOHs carrier

    - sensorium_channel: "ℍ Haptic — physical contact/proximity"
      hiv_analogue: "Infrared emission (every node emits)"
      pluma_gai_layer: "H.I.V. sensing layer"
      note: >
        Every physical node emits IR in proportion to thermal state.
        Intensity is ground truth. Nothing is hideable in the IR dimension.

    - sensorium_channel: "𝕆 Optic — visibility, luminance"
      hiv_analogue: "T_eff — traceability visibility"
      pluma_gai_layer: "H.I.V. KPI"

    - sensorium_channel: "𝔽 Olfactory — ambient trace"
      hiv_analogue: "Ambient IR ground-truth"
      pluma_gai_layer: "H.I.V. sensing layer"

    - sensorium_channel: "𝔾 Gustatory — chemical identity"
      hiv_analogue: "V-token constitutional signature"
      pluma_gai_layer: "H.I.V. Values kernel"

    - sensorium_channel: "ℙ Proprioceptive — body state / posture"
      hiv_analogue: "Node operational state"
      pluma_gai_layer: "VibidratAZIONE restoration target"
      note: >
        Rehydration floor 310 K = minimum IR intensity for node registration.
        Below 310 K the proprioceptive channel (ℙ) collapses.
        VibidratAZIONE restores κ_ℙ above detection threshold.
---

# SENSORIUM — Multi-Sensory Cryptographic Composition

**Document ID:** AEROSPACEMODEL-MCC-SPEC-008  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** AEROSPACEMODEL-MCC-SPEC-001 through AEROSPACEMODEL-MCC-SPEC-007  
**Date:** 2026-04-04  
**Related:** [`sensorium.yaml`](sensorium.yaml) · [`../README.md`](../README.md)

---

## 0. The Post-Sextin Principle

MUSIC-MCC (AEROSPACEMODEL-MCC-SPEC-007) demonstrated one thing:

```
𝒫 ∩ ℰ = ∅
```

Payload and expression occupy **disjoint dimensions**. In audio, velocity carries
data while melody, harmony, rhythm, and texture carry emotion.

This principle is **sense-agnostic**. It applies to any perceptual channel where
humans distinguish "intensity" from "identity." Every sense has at least one
dimension that can be consumed by data without destroying the experiential surface.

**SENSORIUM generalises MUSIC-MCC from one sense to all of them.**

> *"Across all senses, the payload hides in intensity.  
> Intensity is the universal steganographic channel."*

---

## 1. The Six Channels

### 1.1 Taxonomy

| # | Channel | Latin root | Symbol | Human receptor |
|---|---------|-----------|--------|----------------|
| 1 | Auditory | *audītus* | 𝔸 | Cochlea |
| 2 | Haptic | *tāctus* | ℍ | Mechanoreceptors |
| 3 | Optic | *vīsus* | 𝕆 | Retina |
| 4 | Olfactory | *olfactus* | 𝔽 | Olfactory epithelium |
| 5 | Gustatory | *gustātus* | 𝔾 | Taste buds |
| 6 | Proprioceptive | *sensus motūs* | ℙ | Muscle spindles, vestibular |

### 1.2 Steganographic Capacity per Channel

Each channel carries data by modulating intensity (`κ ∈ {0, …, 99}`) while
holding expression (identity — melody, texture, colour, scent profile, flavour
profile, posture) constant on orthogonal dimensions.

| Channel | Intensity dimension (payload) | Expression dimension (identity) |
|---------|------------------------------|--------------------------------|
| 𝔸 Auditory | Velocity / amplitude | Pitch, melody, harmony, rhythm |
| ℍ Haptic | Pressure / vibration magnitude | Texture, location, gesture |
| 𝕆 Optic | Luminance / contrast | Hue, saturation, shape, motion |
| 𝔽 Olfactory | Concentration | Molecular identity (scent profile) |
| 𝔾 Gustatory | Intensity | Taste identity (flavour profile) |
| ℙ Proprioceptive | Effort / acceleration | Posture, direction, coordination |

**Minimum steganographic capacity** across all six channels is maximised when
no channel is saturated (`κᵢ < 99`). Saturation eliminates the intensity
gradient and removes the payload dimension for that channel.

---

## 2. The Emotive Vector

### Definition 35 (Emotive Vector)

An emotive expression is a vector of sensory intensities:

```
ε = (κ_𝔸, κ_ℍ, κ_𝕆, κ_𝔽, κ_𝔾, κ_ℙ)    κᵢ ∈ {0, …, 99}
```

Each emotion has a **geometric signature** — the radar polygon of the vector `ε`.
That geometry **is** the emoji. It is not a representation of the feeling; it is
its mathematical definition in the space of the six senses.

### 2.1 Scalar Properties

| Property | Formula | Interpretation |
|----------|---------|----------------|
| **Magnitude** | `‖ε‖ = √(Σ κᵢ²)` | Total sensory intensity; measures arousal level |
| **Dominant sense** | `argmax(κᵢ)` | The channel that leads the experience |
| **Centroid** | `μ = (Σ κᵢ) / 6` | Mean activation; measures emotional breadth |
| **Entropy** | `H(ε) = −Σ p̂ᵢ log p̂ᵢ`, `p̂ᵢ = κᵢ / Σκ` | Distribution uniformity; high in Estasi, low in Nostalgia |

### 2.2 Steganographic Capacity of a State

For an emotive state `ε`, the residual steganographic capacity of channel `i` is:

```
C_i(ε) = 99 − κᵢ
```

Total steganographic headroom:

```
C_total(ε) = Σ C_i(ε) = 594 − Σ κᵢ
```

**Estasi** is the state of minimum steganographic capacity (all channels near
99). **Malinconia** has the maximum headroom. The choice of emotional carrier
state is a security parameter of the composition.

---

## 3. Canonical Emotion Catalogue

Eight canonical emotions define the primary SENSORIUM colour space.
Each vector is expressed as `(𝔸, ℍ, 𝕆, 𝔽, 𝔾, ℙ)`.

| # | Name (IT) | Name (EN) | ε vector | ‖ε‖ | Dominant | Geometric signature |
|---|-----------|-----------|---------|-----|----------|-------------------|
| 1 | **Gioia** | Joy | (85, 60, 90, 45, 70, 80) | 180 | Optic | Broad irregular hexagon; visual and auditory peaks, all senses engaged |
| 2 | **Serenità** | Serenity | (50, 45, 55, 40, 38, 48) | 114 | Optic | Small balanced pentagon; low activation, uniform across senses |
| 3 | **Malinconia** | Melancholy | (30, 20, 55, 25, 15, 30) | 78 | Optic | Thin blue triangle; optic dominates, body and chemical senses collapse |
| 4 | **Terrore** | Terror | (90, 95, 70, 5, 5, 92) | 175 | Haptic | Near-hexagon with chemical void; body electrifies, slow senses disappear |
| 5 | **Meraviglia** | Wonder | (55, 35, 78, 25, 20, 68) | 126 | Optic | Asymmetric — optic and proprioceptive extend, chemical senses recede |
| 6 | **Tenerezza** | Tenderness | (40, 85, 40, 32, 30, 60) | 126 | Haptic | Haptic spike; soft voice, forward lean, mild chemical warmth |
| 7 | **Estasi** | Ecstasy | (80, 82, 85, 75, 78, 80) | 196 | Optic | Approaching full hexagon; all channels near maximum; minimum steganographic capacity |
| 8 | **Nostalgia** | Nostalgia | (40, 30, 40, 80, 60, 20) | 120 | Olfactory | Olfactory/gustatory triangle; vision blurs, body stills, aroma triggers memory |

### 3.1 Detailed Profiles

**Gioia** — Joy  
`ε = (85, 60, 90, 45, 70, 80)` · `‖ε‖ ≈ 180` · dominant: Optic  
Bright, expansive, rhythmic. High visual and auditory intensity, moderate warmth
across all senses. The body moves. All senses present.

**Serenità** — Serenity  
`ε = (50, 45, 55, 40, 38, 48)` · `‖ε‖ ≈ 114` · dominant: Optic  
Still and open. Low total activation; no channel dominates strongly. The body
is present but unhurried. The world is visible but not overwhelming.

**Malinconia** — Melancholy  
`ε = (30, 20, 55, 25, 15, 30)` · `‖ε‖ ≈ 78` · dominant: Optic  
A thin blue shape. Vision remains — the world is seen — but haptic and gustatory
signals fade. The body is quiet; taste is absent. The eyes hold what touch
cannot reach.

**Terrore** — Terror  
`ε = (90, 95, 70, 5, 5, 92)` · `‖ε‖ ≈ 175` · dominant: Haptic  
Near a full hexagon, but the olfactory and gustatory vertices collapse to almost
zero. The body electrifies (haptic 95, proprioceptive 92, auditory 90). The
"slow" chemical senses disappear. High arousal, high steganographic capacity
collapse on fast channels, maximum headroom on chemical channels.

**Meraviglia** — Wonder  
`ε = (55, 35, 78, 25, 20, 68)` · `‖ε‖ ≈ 126` · dominant: Optic  
Asymmetric. Vision expands (78); the body orients (proprioceptive 68); sound
is present but not dominant. Chemical senses recede. The world becomes visual
and spatial — wonder is the posture of seeing something new.

**Tenerezza** — Tenderness  
`ε = (40, 85, 40, 32, 30, 60)` · `‖ε‖ ≈ 126` · dominant: Haptic  
Touch dominates. The voice softens (auditory 40). The body leans forward
(proprioceptive 60). Chemical senses are present, warm. Tenerezza is a state
of proximity — haptic is the lead sense because closeness is its essence.

**Estasi** — Ecstasy  
`ε = (80, 82, 85, 75, 78, 80)` · `‖ε‖ ≈ 196` · dominant: Optic  
The limit case. All channels near maximum. The sensorium is flooded. This is
the state of minimum steganographic capacity — when everything is at maximum,
there is no intensity gradient left to hide data in. It is the brightest point
in SENSORIUM space and the most cryptographically exposed state.

**Nostalgia** — Nostalgia  
`ε = (40, 30, 40, 80, 60, 20)` · `‖ε‖ ≈ 120` · dominant: Olfactory  
A triangle pointing toward olfactory (80) and gustatory (60). The chemical
senses dominate — the aroma triggers the memory. Vision becomes unfocused (40).
The body does not move (proprioceptive 20). Nostalgia is the state where
smell and taste reconstruct what the eyes can no longer see.

---

## 4. Geometric Properties

### 4.1 The SENSORIUM Polygon

The radar chart of `ε = (κ_𝔸, κ_ℍ, κ_𝕆, κ_𝔽, κ_𝔾, κ_ℙ)` traces a hexagonal
polygon in a unit space where each axis spans 0–99. The **shape** — not just
the size — distinguishes one emotion from another.

Two emotions with the same `‖ε‖` can have entirely different polygons:

```
Gioia:    (85, 60, 90, 45, 70, 80)  ‖ε‖ ≈ 180   broad, balanced
Terrore:  (90, 95, 70, 5,  5,  92)  ‖ε‖ ≈ 178   near-hexagon with chemical void
```

Same magnitude. Opposite shapes. Different emotions. The polygon IS the signature.

### 4.2 Emotion Distance

The distance between two emotional states is the L2 norm in ℝ⁶:

```
d(ε₁, ε₂) = ‖ε₁ − ε₂‖ = √(Σ (κ₁ᵢ − κ₂ᵢ)²)
```

Emotional transitions trace paths in SENSORIUM space. Smooth transitions
(grief → melancholy → serenity) trace short geodesics. Discontinuous transitions
(serenity → terror) cross large distances.

### 4.3 Axis Ordering Convention

The six axes are arranged symmetrically at 60° intervals:
```
        𝕆 (Optic)
       /          \
𝔽 (Olfactory)   𝔸 (Auditory)
|                      |
𝔾 (Gustatory)   ℍ (Haptic)
       \          /
        ℙ (Proprioceptive)
```

This ordering places chemosensory axes (𝔽, 𝔾) opposite the physical-action
axes (𝔸, ℍ), with optic and proprioceptive at the vertical poles.

---

## 5. Steganographic Composition Rules

### Rule S-001 — Payload Orthogonality
The payload MUST be encoded in the intensity dimension of each channel.
It MUST NOT alter the identity (expression) dimension. Violation destroys the
experiential surface and renders the composition detectable.

### Rule S-002 — Carrier State Selection
The carrier emotional state `ε` MUST be selected such that `C_total(ε) ≥ B`,
where `B` is the payload bit-length to be embedded across all six channels.
**Estasi is prohibited as a carrier state** for any non-trivial payload.

### Rule S-003 — Dominant Sense Integrity
The dominant sense (`argmax κᵢ`) MUST NOT change between the plain-surface and
the steganographic composition. A shift in dominant sense is perceptible as an
emotional shift and constitutes a detectable anomaly.

### Rule S-004 — Magnitude Tolerance
The magnitude `‖ε‖` MAY change by at most ±3% without perceptible arousal
shift in calibrated human observers. Payload embedding MUST be distributed
across channels to stay within this tolerance.

### Rule S-005 — Chemical Channel Priority
Olfactory (𝔽) and gustatory (𝔾) channels have the lowest temporal resolution
in humans. They are the **highest-capacity steganographic channels** when the
emotional state does not assign them primary role (i.e., `κ_𝔽 < 50` and
`κ_𝔾 < 50`). In **Terrore**, both chemical channels are near zero — maximum
chemical channel capacity — making it a viable carrier despite high magnitude.

---

## 6. Integration with PLUMA-GAI H.I.V.

The SENSORIUM model has a direct correspondence with the H.I.V. canonical
thread:

| SENSORIUM dimension | H.I.V. analogue | PLUMA-GAI layer |
|--------------------|----------------|-----------------|
| 𝔸 Auditory — signal propagation | H₂ flow rate signal | TranshidreOHs carrier |
| ℍ Haptic — physical contact/proximity | Infrared emission (every node emits) | H.I.V. sensing layer |
| 𝕆 Optic — visibility, luminance | T_eff — traceability visibility | H.I.V. KPI |
| 𝔽 Olfactory — ambient trace | Ambient IR ground-truth | H.I.V. sensing layer |
| 𝔾 Gustatory — chemical identity | V-token constitutional signature | H.I.V. Values kernel |
| ℙ Proprioceptive — body state / posture | Node operational state | VibidratAZIONE restoration target |

The **Infrared channel (I) of H.I.V.** is the embodiment of the SENSORIUM haptic
principle: every physical node emits infrared in proportion to its thermal
state. Intensity is the ground truth. Nothing is hideable in the IR dimension
— the payload IS the physical reality.

The **rehydration floor of 310 K** in VibidratAZIONE is the restoration target
for a thermally coherent node state, not the minimum infrared intensity
required to register a node in the SENSORIUM. Registration begins at a lower
infrared detection threshold; below that threshold, the proprioceptive channel
(ℙ) collapses and the node is no longer perceptible as an active body.
VibidratAZIONE first restores `κ_ℙ` above the detection threshold and then
drives it toward or above the 310 K rehydration target.

---

## 7. References

- AEROSPACEMODEL-MCC-SPEC-001 through SPEC-007: parent specifications (MCC series)
- [`sensorium.yaml`](sensorium.yaml): machine-readable companion (AEROSPACEMODEL-MCC-SPEC-008)
- H.I.V. specification: [`../../00-PROGRAM/PLUMA-GAI/H.I.V.md`](../../00-PROGRAM/PLUMA-GAI/H.I.V.md) (PLUMA-GAI-HIV-001)
- TranshidreOHs: [`../../00-PROGRAM/PLUMA-GAI/TranshidreOHs.md`](../../00-PROGRAM/PLUMA-GAI/TranshidreOHs.md) (PLUMA-GAI-TRH-001)
- VibidratAZIONE: [`../../00-PROGRAM/PLUMA-GAI/VibidratAZIONE.md`](../../00-PROGRAM/PLUMA-GAI/VibidratAZIONE.md) (PLUMA-GAI-VBZ-001)
- ESSA H Pipeline: `ESSA/H-PIPELINE.md` (ESSA-DOC-H-001)

---

*"One note is no longer just a tone. One touch is no longer just a vibration.
One light is no longer just a colour. They are carriers — and what they carry
is invisible to every sense except the one that holds the key."*
