# EGI — Ephemeral Generative Interface

**Document ID:** AEROSPACEMODEL-MCC-SPEC-010  
**Version:** 0.1.0  
**Status:** Draft  
**Parent:** AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM)  
**Date:** 2026-04-14  
**Related:** [`egi.yaml`](egi.yaml) · [`SENSORIUM.md`](SENSORIUM.md) · [`TRAUMACODEDRAMA.md`](TRAUMACODEDRAMA.md) · [`../README.md`](../README.md)

---

## 0. Principle

SENSORIUM (SPEC-008) hides data in the **intensity** of sensory channels.
TRAUMACODEDRAMA (SPEC-009) hides data in the **transitions** between emotional
states.

EGI adds a temporal dimension:

> **Emotive vectors are generated ephemerally — they exist only during the
> rendering window and leave no recoverable artefact after expiry.**

The generative process is forward-only. Past sessions cannot be reconstructed
from present state.

```
𝒢 ∩ 𝒫 = ∅   ∧   ∂𝒢/∂t → 0 as t → t_expire
```

Generative surface and persistent trace occupy disjoint domains. What is
generated is experienced. What has expired is forgotten. What is forgotten
cannot be extracted.

---

## 1. The Ephemeral Session

### Definition 38 (Ephemeral Session)

An ephemeral session is a bounded rendering context:

```
𝒮_eph = (sid, k_eph, ε₀, t_start, t_expire, Γ)
```

where:
- `sid` — unique, non-reusable session identifier
- `k_eph` — ephemeral key, derived per-session, destroyed at `t_expire`
- `ε₀` — initial emotive vector from SENSORIUM canonical catalogue
- `t_start` — session start timestamp
- `t_expire` — session expiry timestamp; `t_expire − t_start = TTL`
- `Γ` — generative function producing the emotive sequence

All session state is destroyed at `t_expire`. No artefact persists.

### Definition 39 (Generative Function)

The generative function produces the next emotive vector:

```
εᵢ = Γ(k_eph, εᵢ₋₁, i)
```

`Γ` is deterministic and key-sensitive: different `k_eph` values yield
perceptually distinct but structurally valid emotive sequences. `Γ` MUST
preserve SENSORIUM domain constraints (`κⱼ ∈ {0, …, 99}` for all channels).

### Definition 40 (Rendering Window)

```
W = [t_start, t_expire)
```

The half-open time interval during which the session is active. Outside `W`,
session state is undefined (destroyed).

### Definition 41 (Ephemeral Key)

```
k_eph = HKDF-SHA3-256(k_master, sid, context)
```

A session-scoped key derived from the master key, the session ID, and optional
context. `k_eph` is held only in volatile memory and is zeroised at `t_expire`.

**Forward secrecy:** compromise of `k_master` after session expiry does NOT
reveal past `k_eph` values if `sid` is not retained — and `sid` retention is
prohibited by Rule E-003.

**Key isolation:** each session's `k_eph` is independent; compromise of one
session does not affect any other.

---

## 2. Session Lifecycle

### Phase 1 — Initiation

Derive `k_eph` from `k_master` and a fresh `sid`. Select `ε₀` from the
SENSORIUM canonical catalogue or from a TRAUMACODEDRAMA Protasis state. Set
TTL. Instantiate `Γ` with `k_eph`.

```
Initiation contract:
  input:   k_master, sid (fresh), ε₀, TTL
  output:  𝒮_eph
  post:    sid is discarded immediately after k_eph derivation
```

### Phase 2 — Generation

Iteratively produce emotive vectors `εᵢ = Γ(k_eph, εᵢ₋₁, i)` for each
rendering tick within the window `W`.

Constraints:
- Only `εᵢ₋₁` is held in memory — no full-sequence buffering
- Each `εᵢ` MUST satisfy SENSORIUM domain constraints
- If a TRAUMACODEDRAMA arc is active, `Δεᵢ` magnitudes MUST comply with act
  constraints

```
Generation contract:
  memory:  εᵢ₋₁ only (single-step look-back)
  output:  εᵢ per rendering tick
  invariant: ∀j: κⱼ ∈ {0, …, 99}
```

### Phase 3 — Expiry

At `t_expire` (or on explicit close):

1. Zeroise `k_eph` (overwrite with zeros)
2. Clear `εᵢ₋₁` from volatile memory
3. Destroy `Γ` internal state
4. Discard `sid` (MUST NOT be logged or retained)
5. Emit `session_closed` signal to consuming interface

```
Expiry contract:
  post:    all session state = 0
  signal:  session_closed
  guarantee: no session artefact persists beyond t_expire
```

### TTL Constraints

| Parameter | Value |
|-----------|-------|
| Minimum TTL | 1 second |
| Default TTL | 300 seconds (5 minutes) |
| Maximum TTL | 86400 seconds (24 hours) |
| TTL = 0 | INVALID |
| TTL = ∞ | PROHIBITED |

---

## 3. Generative Rendering Protocol

### Step 1 — Seed

The consumer requests a session with desired `ε₀` and TTL. The EGI layer
derives `k_eph` and instantiates `Γ`.

### Step 2 — Stream

At each rendering tick (frame, sample, pulse), the EGI layer computes
`εᵢ = Γ(k_eph, εᵢ₋₁, i)` and emits it to the consumer. The consumer renders
the emotive vector on its output channels.

Tick rates depend on the dominant output channel:

| Channel | Symbol | Tick rate (Hz) |
|---------|--------|----------------|
| Auditory | 𝔸 | 60 |
| Haptic | ℍ | 60 |
| Optic | 𝕆 | 60 |
| Olfactory | 𝔽 | 0.5 |
| Gustatory | 𝔾 | 0.5 |
| Proprioceptive | ℙ | 30 |

Fast channels (𝔸, ℍ, 𝕆) tick at perceptual frame rates. Slow channels (𝔽, 𝔾)
tick at the temporal resolution of chemosensory perception.

### Step 3 — Dissolve

When `t` reaches `t_expire`, the EGI layer generates a dissolution fade:

```
ε_dissolve(t) = εᵢ × max(0, (t_expire − t) / fade_duration)
```

- Default fade duration: 10% of TTL
- Maximum fade duration: 30 seconds

This prevents abrupt perceptual discontinuity at session end. All channels
decay smoothly toward zero.

### Step 4 — Destroy

After fade completes, session state is destroyed per Phase 3 (§2). The
consuming interface receives `session_closed` and MUST NOT attempt further
reads.

---

## 4. Interface Contract

### `open_session`

| Parameter | Type | Description |
|-----------|------|-------------|
| `ε₀` | EmotiveVector | Initial emotive vector from SENSORIUM catalogue |
| `ttl` | Duration | Session time-to-live |
| `channels` | Set\<Channel\> | Active SENSORIUM channels (default: all six) |
| `context` | bytes (optional) | Optional context for key derivation |
| **Returns** | SessionHandle | Opaque handle for the active session |

**Errors:** `INVALID_TTL`, `INVALID_VECTOR`, `KEY_DERIVATION_FAILURE`

### `next_vector`

| Parameter | Type | Description |
|-----------|------|-------------|
| `session_handle` | SessionHandle | Active session handle |
| **Returns** | (EmotiveVector, step, remaining_ttl) | Next εᵢ, step index, time remaining |

**Errors:** `SESSION_EXPIRED`, `SESSION_CLOSED`

### `close_session`

| Parameter | Type | Description |
|-----------|------|-------------|
| `session_handle` | SessionHandle | Active session handle |
| `immediate` | bool | If true, skip fade and destroy immediately (default: false) |
| **Returns** | acknowledged | Confirmation of closure |

**Errors:** `SESSION_NOT_FOUND`

---

## 5. Encoding Rules

### Rule E-001 — Ephemeral Isolation
Each EGI session MUST use a unique ephemeral key `k_eph` derived from a fresh
session identifier `sid`. Reuse of `sid` or `k_eph` across sessions is a
protocol violation.

### Rule E-002 — Forward Destruction
At session expiry (`t_expire`) or explicit close, ALL session state (`k_eph`,
`εᵢ₋₁`, `Γ` internal state) MUST be destroyed. Destruction means overwriting
with zeros, not merely freeing memory. No session artefact may persist beyond
`t_expire`.

### Rule E-003 — Session ID Non-Retention
The session identifier `sid` MUST NOT be logged, stored, or transmitted after
session creation. `sid` exists only to derive `k_eph` and is discarded
immediately after derivation.

### Rule E-004 — Single-Step Look-Back
During the Generation phase, only the immediately preceding emotive vector
`εᵢ₋₁` MAY be held in volatile memory. Full-sequence buffering is prohibited.
At any point during the session, only two vectors (`εᵢ₋₁` and `εᵢ`) are
simultaneously recoverable.

### Rule E-005 — Domain Preservation
Every emotive vector `εᵢ` produced by `Γ` MUST satisfy SENSORIUM domain
constraints: `κⱼ ∈ {0, …, 99}` for all channels `j`. The generative function
MUST clamp or reject out-of-domain outputs before delivery.

### Rule E-006 — Fade Continuity
The dissolution fade (§3, Step 3) MUST produce a perceptually continuous decay.
The maximum per-tick change during fade MUST NOT exceed the SENSORIUM magnitude
tolerance (±3% of `‖ε‖` per tick). Abrupt channel zeroing is prohibited.

### Rule E-007 — TTL Finitude
Every EGI session MUST have a finite, non-zero TTL. Infinite sessions are
prohibited. Maximum TTL is 86400 seconds (24 hours). Implementations SHOULD
default to 300 seconds.

---

## 6. Security Properties

### Forward Secrecy

Compromise of `k_master` after a session has expired and `sid` has been
discarded does NOT reveal the session's `k_eph` or any emotive vectors
generated during the session.

**Mechanism:** `k_eph = HKDF(k_master, sid, context)`. Without `sid` (which is
destroyed at session creation per E-003), `k_eph` cannot be re-derived even
with `k_master`.

### Ephemeral Integrity

During an active session, the emotive sequence is deterministic and verifiable:
a second instance with the same `(k_eph, ε₀, i)` produces the identical `εᵢ`.
After expiry, this verification is no longer possible (`k_eph` is destroyed).

Integrity is ephemeral by design. Post-session verification requires a witness
commitment (hash of the sequence) captured during the session by an external
observer.

### Anti-Replay

Session IDs are unique and non-reusable. Replaying a `sid` to re-derive
`k_eph` is detectable because `sid` is discarded at derivation time (E-003) —
any attempt to re-present a `sid` implies an illegitimate copy.

### No-Persistence Guarantee

EGI provides a best-effort guarantee that session state does not persist beyond
`t_expire`. Implementations MUST use secure memory erasure. The specification
does NOT guarantee protection against hardware-level memory forensics
(cold-boot attacks, DRAM remanence) — these are out of scope.

---

## 7. Integration with SENSORIUM and TRAUMACODEDRAMA

### SENSORIUM (SPEC-008)

EGI consumes SENSORIUM emotive vectors as its atomic unit. Every `εᵢ` generated
by an EGI session is a valid SENSORIUM vector (Definition 35) and may be used as
input to any SENSORIUM-aware system.

| Layer | Role |
|-------|------|
| SENSORIUM (SPEC-008) | Defines emotive vector space and domain constraints |
| EGI (SPEC-010) | Generates ephemeral traversals through the emotive vector space |

SENSORIUM defines the vector space. EGI defines the ephemeral generative
traversal of that space.

### TRAUMACODEDRAMA (SPEC-009)

An EGI session MAY generate emotive sequences that conform to a TRAUMACODEDRAMA
dramatic arc. When a TRAUMACODEDRAMA arc is active within an EGI session, the
generative function `Γ` MUST respect act-level transition constraints:

- **Protasis:** `‖Δε‖ ≤ 30`
- **Epitasis:** unconstrained
- **Katharsis:** convergent

### Three-Layer Composition — Ephemeral Dramatic Arc

When all three specifications are combined, a three-layer encoding is achieved:

| Layer | Specification | Encodes |
|-------|---------------|---------|
| 1 | SENSORIUM | Payload in channel intensities within each state |
| 2 | TRAUMACODEDRAMA | Payload in transition magnitudes across states |
| 3 | EGI | Ephemeral session envelope — forward secrecy wrapper |

The EGI layer ensures that the entire dramatic arc is non-reconstructible after
session expiry. The three layers are independent: SENSORIUM encodes in state
intensity, TRAUMACODEDRAMA encodes in transition magnitude, and EGI provides the
ephemeral session lifecycle that destroys all evidence of both encodings.

---

## 8. References

- AEROSPACEMODEL-MCC-SPEC-008 (SENSORIUM): parent specification
- AEROSPACEMODEL-MCC-SPEC-009 (TRAUMACODEDRAMA): sibling specialisation
- [`egi.yaml`](egi.yaml): machine-readable companion (AEROSPACEMODEL-MCC-SPEC-010)
- [`SENSORIUM.md`](SENSORIUM.md): base emotive vector definitions
- [`TRAUMACODEDRAMA.md`](TRAUMACODEDRAMA.md): dramatic-arc steganographic protocol
- HKDF: RFC 5869 — HMAC-based Extract-and-Expand Key Derivation Function
- SHA3-256: FIPS 202 — SHA-3 Standard

---

*"What is generated is experienced.  
What has expired is forgotten.  
What is forgotten cannot be extracted."*
