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
| 2 | **Serenità** | Serenity | (50, 45, 55, 40, 38, 48) | 118 | Optic | Small balanced pentagon; low activation, uniform across senses |
| 3 | **Malinconia** | Melancholy | (30, 20, 55, 25, 15, 30) | 80 | Optic | Thin blue triangle; optic dominates, body and chemical senses collapse |
| 4 | **Terrore** | Terror | (90, 95, 70, 5, 5, 92) | 178 | Haptic | Near-hexagon with chemical void; body electrifies, slow senses disappear |
| 5 | **Meraviglia** | Wonder | (55, 35, 78, 25, 20, 68) | 137 | Optic | Asymmetric — optic and proprioceptive extend, chemical senses recede |
| 6 | **Tenerezza** | Tenderness | (40, 85, 40, 32, 30, 60) | 131 | Haptic | Haptic spike; soft voice, forward lean, mild chemical warmth |
| 7 | **Estasi** | Ecstasy | (80, 82, 85, 75, 78, 80) | 186 | Optic | Approaching full hexagon; all channels near maximum; minimum steganographic capacity |
| 8 | **Nostalgia** | Nostalgia | (40, 30, 40, 80, 60, 20) | 117 | Olfactory | Olfactory/gustatory triangle; vision blurs, body stills, aroma triggers memory |

### 3.1 Detailed Profiles

**Gioia** — Joy  
`ε = (85, 60, 90, 45, 70, 80)` · `‖ε‖ ≈ 180` · dominant: Optic  
Bright, expansive, rhythmic. High visual and auditory intensity, moderate warmth
across all senses. The body moves. All senses present.

**Serenità** — Serenity  
`ε = (50, 45, 55, 40, 38, 48)` · `‖ε‖ ≈ 118` · dominant: Optic  
Still and open. Low total activation; no channel dominates strongly. The body
is present but unhurried. The world is visible but not overwhelming.

**Malinconia** — Melancholy  
`ε = (30, 20, 55, 25, 15, 30)` · `‖ε‖ ≈ 80` · dominant: Optic  
A thin blue shape. Vision remains — the world is seen — but haptic and gustatory
signals fade. The body is quiet; taste is absent. The eyes hold what touch
cannot reach.

**Terrore** — Terror  
`ε = (90, 95, 70, 5, 5, 92)` · `‖ε‖ ≈ 178` · dominant: Haptic  
Near a full hexagon, but the olfactory and gustatory vertices collapse to almost
zero. The body electrifies (haptic 95, proprioceptive 92, auditory 90). The
"slow" chemical senses disappear. High arousal, high steganographic capacity
collapse on fast channels, maximum headroom on chemical channels.

**Meraviglia** — Wonder  
`ε = (55, 35, 78, 25, 20, 68)` · `‖ε‖ ≈ 137` · dominant: Optic  
Asymmetric. Vision expands (78); the body orients (proprioceptive 68); sound
is present but not dominant. Chemical senses recede. The world becomes visual
and spatial — wonder is the posture of seeing something new.

**Tenerezza** — Tenderness  
`ε = (40, 85, 40, 32, 30, 60)` · `‖ε‖ ≈ 131` · dominant: Haptic  
Touch dominates. The voice softens (auditory 40). The body leans forward
(proprioceptive 60). Chemical senses are present, warm. Tenerezza is a state
of proximity — haptic is the lead sense because closeness is its essence.

**Estasi** — Ecstasy  
`ε = (80, 82, 85, 75, 78, 80)` · `‖ε‖ ≈ 186` · dominant: Optic  
The limit case. All channels near maximum. The sensorium is flooded. This is
the state of minimum steganographic capacity — when everything is at maximum,
there is no intensity gradient left to hide data in. It is the brightest point
in SENSORIUM space and the most cryptographically exposed state.

**Nostalgia** — Nostalgia  
`ε = (40, 30, 40, 80, 60, 20)` · `‖ε‖ ≈ 117` · dominant: Olfactory  
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

The **rehydration floor of 310 K** in VibidratAZIONE is the minimum infrared
intensity required to register a node in the SENSORIUM: below 310 K, the
proprioceptive channel (ℙ) collapses and the node is no longer perceptible
as an active body. VibidratAZIONE restores `κ_ℙ` to a level above the
detection threshold.

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
