# TRAUMACODEDRAMA — Dramatic-Arc Steganographic Protocol

**Document ID:** AEROSPACEMODEL-MCC-SPEC-009  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM)  
**Date:** 2026-04-04  
**Related:** [`traumacodedrama.yaml`](traumacodedrama.yaml) · [`SENSORIUM.md`](SENSORIUM.md) · [`../README.md`](../README.md)

---

## 0. Principle

SENSORIUM (SPEC-008) hides data in the **intensity** of sensory channels while
the **identity** (expression) remains unaltered.

TRAUMACODEDRAMA advances this by one derivative:

> **Data is not hidden in the emotional state `ε`.  
> Data is hidden in the transition between consecutive emotional states `Δε`.**

The cover is the dramatic arc. The drama is not the container of the data — the
drama **is** the encoding protocol.

```
𝒟 ∩ 𝒯 = ∅
```

Dramaturgical intent and encoded transitions occupy disjoint perceptual
dimensions. A sudden emotional shift (serenità → terrore) reads as a plot twist
to the observer; to the decoder it is a data word. Dramatic transitions are
*expected* — they are the structural vocabulary of storytelling. This expectation
is the steganographic cover.

---

## 1. The Transition Channel

### Definition 36 (Transition Vector)

Given two consecutive emotional states `εᵢ₋₁` and `εᵢ`, the transition vector is:

```
Δεᵢ = εᵢ − εᵢ₋₁ = (Δκ_𝔸, Δκ_ℍ, Δκ_𝕆, Δκ_𝔽, Δκ_𝔾, Δκ_ℙ)
```

where `Δκⱼ ∈ {−99, …, +99}` for each channel `j ∈ {𝔸, ℍ, 𝕆, 𝔽, 𝔾, ℙ}`.

### Definition 37 (MonKBit Encoding)

The payload word at transition `i` is encoded in the magnitude of the
transition vector:

```
κᵢ = f(‖Δεᵢ‖)
```

where:
- `‖Δεᵢ‖ = √(Σ Δκⱼ²)` is the L2 norm of the transition
- `f` is the agreed encoding function mapping `[0, 99√6]` to the payload symbol space
- `κᵢ` is the MonKBit — the payload unit at position `i`

The **direction** of the transition vector `Δεᵢ/‖Δεᵢ‖` encodes the
*dramaturgical intent* (which sense leads the shift). The **magnitude** encodes
the data word. These two quantities are orthogonal: changing the magnitude does
not change the direction, and the experienced emotion only notices direction.

### 1.1 Capacity per Transition

For a transition between states `ε₀` and `ε₁`, the maximum payload capacity
(in nats, using natural log) is:

```
C_transition = log(‖Δε_max‖ / resolution)
```

where `resolution` is the minimum perceptible intensity change (empirically
≈ 5 units per channel in calibrated settings).

The **Epitasis** (Act II, peak tension) maximises capacity because dramatic
confrontations permit the largest emotional swings. A transition from serenità
(magnitude 114) to terrore (magnitude 175) has `‖Δε‖ ≈ 185` — near the
theoretical maximum for the canonical catalogue.

---

## 2. The Three-Act Encoding Structure

Classical Greek tragedy provides three structural layers that map precisely onto
a cryptographic transport protocol:

| Dramatic Act | Greek term | Encoding role | Cryptographic function |
|---|---|---|---|
| Act I | **Protasis** | Header | Establish baseline `ε₀`, seed, channel parameters |
| Act II | **Epitasis** | Payload | Maximum transition variance → maximum capacity |
| Act III | **Katharsis** | Footer | Convergence, CRC, channel closure |

### 2.1 Protasis — Header

The **Protasis** establishes the communicative ground:

- **`ε₀`** — the initial emotional state (seed state); agreed out-of-band or
  derivable from a shared key
- **`seed`** — a 256-bit initialisation value that determines `f` (the
  MonKBit encoding function) for this dramatic instance
- **Channel ID** — identifies which of the six SENSORIUM channels carry data
  vs. which carry pure dramaturgical intent
- **Act I transitions** must be small (`‖Δε‖ < threshold_protasis`) so that
  the narrative establishes normality before the crisis

```
Protasis contract:
  ε₀:            agreed initial state
  seed:           sha3-256:hex  (determines f for this dramatic instance)
  active_channels: subset of {𝔸, ℍ, 𝕆, 𝔽, 𝔾, ℙ}
  max_Δε_act_I:  ‖Δε‖ ≤ 30  (normality: no sudden shifts)
```

### 2.2 Epitasis — Payload

The **Epitasis** carries the information:

- Transitions are unconstrained in magnitude (subject only to the reachable
  state space: each `κⱼ ∈ {0, …, 99}`)
- Each transition `Δεᵢ` in Act II encodes one payload word `κᵢ = f(‖Δεᵢ‖)`
- The direction of each transition is chosen to be dramaturgically plausible
  (the encoder selects the *nearest* emotionally credible state at the target
  magnitude — this is the **nearest-drama constraint**)
- **Maximum capacity** is at the climax: the single largest-magnitude
  transition of the drama encodes the most significant payload word

```
Epitasis contract:
  transitions:    N payload-carrying transitions
  each Δεᵢ:      direction = dramaturgically plausible
                  magnitude = f⁻¹(κᵢ)  (encodes payload word κᵢ)
  climax:         argmax(‖Δεᵢ‖) is the peak transition; encoder places MSW here
```

### 2.3 Katharsis — Footer

The **Katharsis** closes the protocol:

- Transitions converge back toward a resolution state `ε_final`
- The final transition `Δε_final = ε_final − ε_{N−1}` carries the CRC/checksum
- `‖Δε_final‖` must encode a valid CRC word (the encoder adjusts the magnitude
  of the resolution transition to embed the checksum without disturbing the
  sense of emotional closure — a small adjustment is experientially plausible
  as individual variation in how different observers experience resolution)
- After Katharsis: `‖ε_final − ε₀‖` SHOULD be small (arc closure invariant —
  the drama returns near its starting emotional register)

```
Katharsis contract:
  resolution_state: ε_final
  crc_transition:  Δε_final carries CRC word in its magnitude
  arc_closure:     ‖ε_final − ε₀‖ ≤ arc_closure_threshold  (default: 30)
```

---

## 3. Canonical Dramaturgies

Three canonical dramatic arcs illustrate the protocol. Each arc is a sequence of
named canonical emotional states from SENSORIUM SPEC-008.

### 3.1 Perdita — Loss

**Arc:** Serenità → Tenerezza → Malinconia → Terrore → `ε_vuoto` → Nostalgia → Serenità

| Act | Transition | Direction | `‖Δε‖` | Role |
|-----|-----------|-----------|---------|------|
| I (Protasis) | Serenità → Tenerezza | Haptic rise | ≈ 60 | Establish baseline; small payload |
| II (Epitasis) | Tenerezza → Malinconia | Collapse | ≈ 80 | Payload word 1 |
| II (Epitasis) | Malinconia → Terrore | Explosive rise | ≈ 185 | **Climax: MSW** |
| II (Epitasis) | Terrore → `ε_vuoto` | Total collapse | ≈ 175 | Payload word 3 |
| III (Katharsis) | `ε_vuoto` → Nostalgia | Chemical recovery | ≈ 80 | Footer / CRC |
| III (Katharsis) | Nostalgia → Serenità | Arc closure | ≈ 20 | Seal |

`ε_vuoto` is defined as `(5, 5, 5, 5, 5, 5)` — near-zero on all channels, the
state of sensory absence.

**Steganographic profile:** Maximum capacity at the Malinconia → Terrore
climax. The dramatic plausibility of sudden terror in a loss narrative provides
full cover for the MSW. The Katharsis uses a chemosensory recovery (nostalgia
as memory re-surfacing) — small residual transitions that carry the CRC without
disturbing the sense of grief's resolution.

### 3.2 Rinascita — Rebirth

**Arc:** Malinconia → Serenità → Meraviglia → Gioia → Estasi → Tenerezza → Serenità

| Act | Transition | Direction | `‖Δε‖` | Role |
|-----|-----------|-----------|---------|------|
| I (Protasis) | Malinconia → Serenità | Optic opening | ≈ 55 | Establish baseline |
| II (Epitasis) | Serenità → Meraviglia | Optic + proprioceptive | ≈ 45 | Payload word 1 |
| II (Epitasis) | Meraviglia → Gioia | Full-body expansion | ≈ 95 | Payload word 2 |
| II (Epitasis) | Gioia → Estasi | Flood | ≈ 45 | Payload word 3 (near-saturation warning) |
| III (Katharsis) | Estasi → Tenerezza | Haptic settling | ≈ 90 | CRC |
| III (Katharsis) | Tenerezza → Serenità | Arc closure | ≈ 30 | Seal |

**Steganographic profile:** The Gioia → Estasi transition has lower capacity
(both states are high-magnitude, so the transition is small). The Katharsis
Estasi → Tenerezza carries the CRC with high capacity (large magnitude
transition that is dramatically plausible as intensity fading into warmth).
Decoder note: Estasi (magnitude 196) is the highest-magnitude state; the
transition *away* from it has high `‖Δε‖` even to a still-bright state.

### 3.3 Metamorfosi — Transformation

**Arc:** Terrore → Malinconia → Meraviglia → Tenerezza → Nostalgia → Gioia → Serenità

| Act | Transition | Direction | `‖Δε‖` | Role |
|-----|-----------|-----------|---------|------|
| I (Protasis) | Terrore → Malinconia | Shock subsides | ≈ 155 | Establish baseline (large but expected) |
| II (Epitasis) | Malinconia → Meraviglia | Discovery | ≈ 115 | Payload word 1 |
| II (Epitasis) | Meraviglia → Tenerezza | Contact | ≈ 45 | Payload word 2 |
| II (Epitasis) | Tenerezza → Nostalgia | Chemical shift | ≈ 90 | Payload word 3 |
| III (Katharsis) | Nostalgia → Gioia | Expansion | ≈ 115 | CRC |
| III (Katharsis) | Gioia → Serenità | Arc closure | ≈ 90 | Seal |

**Steganographic profile:** The Protasis starts with a large-magnitude
transition (terror subsiding) which is dramaturgically expected at the opening
of a transformation story. This gives the header a wide seed-encoding window.
The Katharsis Nostalgia → Gioia transition is unusually large for a footer —
it is credible as the narrative payoff of transformation. The decoder uses the
`arc_closure` invariant to verify: `‖ε_final − ε₀‖ = ‖Serenità − Terrore‖ ≈ 155`,
which is large — this arc *does not return to its starting register* by design.
The arc_closure invariant is relaxed for Metamorfosi (set `arc_closure_threshold = 200`).

---

## 4. Encoding Rules

### Rule D-001 — Transition Primacy
Data MUST be encoded in `‖Δεᵢ‖` (transition magnitude), NOT in `εᵢ` (state
magnitude). Any component of the payload that correlates with absolute state
values rather than state differences is a protocol violation.

### Rule D-002 — Nearest-Drama Constraint
For each payload-carrying transition, the encoder MUST select the target state
`εᵢ` such that:
1. `‖εᵢ − εᵢ₋₁‖ = f⁻¹(κᵢ)` (magnitude matches payload word)
2. `εᵢ` is the canonical state nearest to this magnitude in the direction of
   dramaturgical intent (preserving the arc's emotional logic)

Violation of the nearest-drama constraint is detectable as emotionally
implausible state sequences.

### Rule D-003 — Act II Climax Placement
The payload word with the highest value (MSW — most significant word) MUST be
placed at the transition with the maximum dramatic magnitude (the climax).
This aligns maximum information density with maximum narrative tension.

### Rule D-004 — Katharsis CRC
The final transition before arc closure MUST carry a valid CRC/checksum of the
entire payload. The CRC word's magnitude is adjusted in `±resolution` steps
(resolution ≈ 5 units per channel) without changing the sense of the closure.

### Rule D-005 — Arc Closure Invariant
`‖ε_final − ε₀‖ ≤ arc_closure_threshold`  
Default: 30. May be relaxed (up to 200) for transformation arcs (Metamorfosi
archetype) where non-return to baseline is part of the dramatic intent. The
threshold MUST be declared in the Protasis header.

### Rule D-006 — Vuoto Guard
The `ε_vuoto` state `(5, 5, 5, 5, 5, 5)` is the reserved minimum-signal state
and is permitted ONLY in Act II transitions. It MUST NOT appear as `ε₀` or
`ε_final`. Transitions to or from `ε_vuoto` carry the maximum theoretical
`‖Δε‖` in their respective channel axes and should be reserved for the highest-
capacity payload words.

---

## 5. Decoder Protocol

Given a sequence of emotional states `[ε₀, ε₁, …, εₙ]`:

1. **Identify acts:** Determine Protasis / Epitasis / Katharsis boundaries by
   `‖Δεᵢ‖` profile. Protasis = low-variance prefix; Katharsis = convergent suffix;
   Epitasis = all transitions between.

2. **Extract seed:** The Protasis carries `seed` in the Act I transition magnitudes
   using a pre-shared extraction function.

3. **Recover `f`:** Derive the encoding function from `seed`.

4. **Decode payload:** For each Epitasis transition `i`: `κᵢ = f(‖Δεᵢ‖)`.

5. **Verify CRC:** Apply `f` to the Katharsis CRC transition and compare with
   `CRC(κ₁, …, κ_N)`.

6. **Verify arc closure:** Check `‖εₙ − ε₀‖ ≤ arc_closure_threshold`. Fail if
   threshold is exceeded without a Metamorfosi flag in the Protasis header.

---

## 6. Integration with SENSORIUM

TRAUMACODEDRAMA extends SENSORIUM (SPEC-008) at the compositional level:

| Layer | Unit | What is encoded |
|-------|------|-----------------|
| SENSORIUM | State `ε` | Steganographic payload in channel intensities (within one state) |
| TRAUMACODEDRAMA | Transition `Δε` | Steganographic payload in transition magnitudes (across state sequences) |

The two layers are orthogonal: a TRAUMACODEDRAMA arc can additionally embed
intra-state SENSORIUM payloads in each `εᵢ`, achieving a **two-layer encoding**
where:
- Inner layer (SENSORIUM): payload in `κᵢ` values within each state
- Outer layer (TRAUMACODEDRAMA): payload in `‖Δεᵢ‖` values between states

The two payloads are fully independent by the Post-Sextin / Transition Primacy
principles.

---

## 7. References

- AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM): parent specification
- [`traumacodedrama.yaml`](traumacodedrama.yaml): machine-readable companion (AEROSPACEMODEL-MCC-SPEC-009)
- [`SENSORIUM.md`](SENSORIUM.md): base emotive vector definitions
- Classical dramatic theory: Aristotle's *Poetics*, III Acts structure (Protasis / Epitasis / Katharsis)
- H.I.V. specification: [`../../00-PROGRAM/PLUMA-GAI/H.I.V.md`](../../00-PROGRAM/PLUMA-GAI/H.I.V.md)

---

*"The drama is not the container of the data.  
The drama is the encoding protocol.  
The arc dramatic IS the channel."*
