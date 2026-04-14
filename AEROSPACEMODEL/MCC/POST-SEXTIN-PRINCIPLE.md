# The Post-Sextin Principle — Payload / Expression Disjointness

**Document ID:** AEROSPACEMODEL-MCC-SPEC-000  
**Version:** 0.1.0  
**Status:** Draft  
**Date:** 2026-04-14  
**Related:** [`post-sextin-principle.yaml`](post-sextin-principle.yaml) · [`SENSORIUM.md`](SENSORIUM.md) · [`TRAUMACODEDRAMA.md`](TRAUMACODEDRAMA.md) · [`EGI.md`](EGI.md)

---

## 0. The Axiom

```
𝒫 ∩ ℰ = ∅
```

**Payload and expression occupy disjoint dimensions.**

In any perceptual channel where humans distinguish *intensity* from *identity*,
intensity is the steganographic degree of freedom and identity is the
experiential surface. Altering intensity does not alter identity; altering
identity does not alter intensity. The two sets share no element.

This is the **Post-Sextin Principle** — the zeroth axiom of the MCC
specification series. Every MCC specification restates it at a higher level of
abstraction. The axiom is invariant; only the embedding domain changes.

---

## 1. Formal Definitions

### Definition 0 (Perceptual Channel)

A **perceptual channel** `𝕊` is a sensory modality that admits a decomposition
into an intensity dimension and an identity dimension:

```
𝕊 = (I_𝕊, X_𝕊)
```

- `I_𝕊` — the scalar magnitude axis (amplitude, luminance, pressure, …)
- `X_𝕊` — the qualitative feature space (pitch, hue, texture, …)

### Definition 1 (Payload Space)

The **payload space** `𝒫` is the set of all bit-strings embeddable as intensity
modulations within a composition without altering the identity dimension:

```
𝒫 ⊂ I_𝕊
```

### Definition 2 (Expression Space)

The **expression space** `ℰ` is the set of perceptual qualities that constitute
the experiential surface of a composition. Expression lives in the identity
dimension:

```
ℰ ⊂ X_𝕊
```

### Definition 3 (Disjointness Axiom)

```
𝒫 ∩ ℰ = ∅
```

No element belongs to both the payload space and the expression space. This is
the formal statement of the Post-Sextin Principle.

### Definition 4 (Steganographic Capacity)

```
C(𝕊) = |I_𝕊| − I_used
```

The residual intensity headroom in channel `𝕊` after the expressive surface has
been composed. This is the maximum payload bandwidth without perceptual
disruption.

---

## 2. Sense-Specific Instantiations

The principle is **sense-agnostic**. It names no specific modality. It names a
structural separation that recurs in every channel where humans distinguish
intensity from identity:

| Channel | Symbol | Intensity dimension | Identity dimension |
|---|---|---|---|
| Auditory | `𝔸` | Velocity / amplitude | Pitch, melody, harmony, rhythm, timbre |
| Haptic | `ℍ` | Pressure / vibration magnitude | Texture, location, gesture |
| Optic | `𝕆` | Luminance / contrast | Hue, saturation, shape, motion |
| Olfactory | `𝔽` | Concentration | Molecular identity (scent profile) |
| Gustatory | `𝔾` | Intensity | Taste identity (flavour profile) |
| Proprioceptive | `ℙ` | Effort / acceleration | Posture, direction, coordination |

The auditory case (MUSIC-MCC, SPEC-007) was the original single-sense instance.
SENSORIUM (SPEC-008) generalised it to all six channels. The principle itself
is independent of both — it applies to any future channel that admits an
`(I, X)` decomposition.

---

## 3. Generalisation Hierarchy

Each MCC specification restates the Post-Sextin Principle at a higher level of
abstraction:

| Layer | Spec | Domain | Disjointness |
|---|---|---|---|
| **Intensity** | SENSORIUM (SPEC-008) | Six senses: `ε = (κ_𝔸, κ_ℍ, κ_𝕆, κ_𝔽, κ_𝔾, κ_ℙ)` | `𝒫 ∩ ℰ = ∅` — intensity vector vs. identity vector |
| **Transitions** | TRAUMACODEDRAMA (SPEC-009) | Transition magnitudes across state sequences | `𝒟 ∩ 𝒯 = ∅` — transition magnitude vs. dramaturgical intent |
| **Lifecycle** | EGI (SPEC-010) | Lifecycle dynamics of ephemeral interfaces | `ℰ ∩ 𝒜 = ∅` — ephemeral experience vs. archival artifact |

The three layers are **orthogonal** by construction. A single ephemeral
interface (EGI) with internal state transitions (TRAUMACODEDRAMA) and per-state
intensity profiles (SENSORIUM) carries **three independent payloads**
simultaneously — one per layer — because each layer's payload and expression
spaces are disjoint in their own dimension.

---

## 4. Consequences

### C-001 — Orthogonal Layering

Because each layer operates in a disjoint dimension, the three MCC layers —
SENSORIUM (intensity), TRAUMACODEDRAMA (transitions), EGI (lifecycle) — can
carry independent payloads simultaneously without mutual interference.

### C-002 — Undetectability Bound

A composition that satisfies `𝒫 ∩ ℰ = ∅` and stays within the magnitude
tolerance (±3 %, Rule S-004) is indistinguishable from a composition without
payload to any observer whose perception operates on the identity dimension
only.

### C-003 — Carrier State as Security Parameter

Steganographic capacity `C_total(ε) = 594 − Σ κᵢ`. The choice of carrier
emotional state determines the available payload bandwidth. Estasi (maximum
arousal) minimises capacity; Malinconia (low arousal) maximises it. Carrier
state selection is a security parameter of the composition, not an aesthetic
choice.

### C-004 — Sense Agnosticism

The principle names no specific sense. Any future perceptual channel that
admits an intensity/identity decomposition inherits the axiom and all its
consequences without modification.

---

## 5. Origin

The principle was first observed in the auditory domain: MIDI velocity
(intensity) carries data while melody, harmony, rhythm, and texture (identity)
carry emotion. The observation that velocity modulation is imperceptible to
human listeners — while identity modulation is immediately perceived — led to
the separation axiom.

The name **Post-Sextin** denotes the principle's position beyond (post) the
six-sense (sextin) generalisation: it was discovered in one sense, generalised
to six in SENSORIUM, and then recognised as sense-agnostic — valid for any
perceptual channel, including channels not yet enumerated.

---

## 6. References

- AEROSPACEMODEL-MCC-SPEC-007 (MUSIC-MCC): single-sense origin
- AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM): multi-sense generalisation — [`SENSORIUM.md`](SENSORIUM.md)
- AEROSPACEMODEL-MCC-SPEC-009 (TRAUMACODEDRAMA): derivative extension — [`TRAUMACODEDRAMA.md`](TRAUMACODEDRAMA.md)
- AEROSPACEMODEL-MCC-SPEC-010 (EGI): lifecycle extension — [`EGI.md`](EGI.md)
- [`post-sextin-principle.yaml`](post-sextin-principle.yaml): machine-readable companion

---

*"Intensity is the universal steganographic channel.  
Identity is the experiential surface.  
The two never meet."*
