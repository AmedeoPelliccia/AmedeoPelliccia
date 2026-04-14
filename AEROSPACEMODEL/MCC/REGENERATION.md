---
##############################################################################
# REGENERATION.md
# REGENERATION — Assembly Regeneration Protocol
# AEROSPACEMODEL MCC Specification Series — SPEC-011
##############################################################################

document_id: AEROSPACEMODEL-MCC-SPEC-011
document_type: assembly_regeneration_protocol
title: "REGENERATION — Assembly Regeneration Protocol"
version: "0.1.0"
schema_version: "1.0.0"
status: draft
parent: AEROSPACEMODEL-MCC-SPEC-008
related_documents:
  - id: AEROSPACEMODEL-MCC-SPEC-008
    file: "AEROSPACEMODEL/MCC/SENSORIUM.md"
    relationship: parent_sensory_layer
  - id: AEROSPACEMODEL-MCC-SPEC-010
    file: "AEROSPACEMODEL/MCC/EGI.md"
    relationship: sibling_specialisation
last_updated: "2026-04-14T00:00:00Z"

##############################################################################
# 0  Core Principle
##############################################################################

core_principle:
  regeneration_function: "ℛ(σ) ≅ A₀"
  description: >
    Cognitive assemblies need not be stored in full — only a minimal
    persistence kernel 𝒦 must survive. Given a reactivation stimulus σ
    drawn from the SENSORIUM channel space, the regeneration rule set ℛ
    reconstructs a functionally equivalent assembly from 𝒦.
  axiom: >
    "Preserve the seed, not the tree.
    The protocol regenerates what persistence compresses."

##############################################################################
# 1  Definitions
##############################################################################

definitions:

  - definition: 41
    name: Regeneration Rule Set
    symbol: "ℛ"
    description: >
      A finite set of deterministic or probabilistic rules that, given a
      reactivation stimulus σ, produce a cognitive assembly functionally
      equivalent to a prior assembly. Two assemblies are functionally
      equivalent if they produce indistinguishable output for all inputs
      in the operational domain.
    formal: "ℛ(σ) ≅ A₀  ⟺  ∀x ∈ 𝒟 : ℛ(σ)(x) = A₀(x)"

  - definition: 42
    name: Reactivation Stimulus
    symbol: "σ"
    description: >
      A multimodal vector drawn from the SENSORIUM channel space. Each
      component σⱼ corresponds to one of the six sensory channels
      {𝔸, ℍ, 𝕆, 𝔽, 𝔾, ℙ}. A stimulus may be strong in one channel or
      arise from a cooperative sum of individually sub-threshold channels.
    components: "(σ_𝔸, σ_ℍ, σ_𝕆, σ_𝔽, σ_𝔾, σ_ℙ)"
    domain: "σⱼ ∈ [0, 99] for each channel j"
    cooperative_threshold: >
      A channel j is individually sub-threshold when σⱼ < τⱼ, but the
      assembly may still be reactivated when Σ(σⱼ / τⱼ) ≥ 1 (cooperative
      sum criterion).

  - definition: 43
    name: Persistence Kernel
    symbol: "𝒦"
    description: >
      The minimal subset of an assembly's state that is sufficient for
      reconstruction via ℛ. The kernel is NOT the assembly itself; it is
      the compressed seed from which a functionally equivalent assembly
      can be regenerated.
    relation_to_E2: >
      Axiom E2 (Minimal Persistence) asserts that 𝒦 exists and that
      |𝒦| ≪ |A₀| in the general case. The goal of the protocol is to
      identify, transmit, and protect 𝒦 rather than A₀.

---

# REGENERATION — Assembly Regeneration Protocol

**AEROSPACEMODEL-MCC-SPEC-011** · Draft · v0.1.0

---

## 0 · Core Principle

```
ℛ(σ) ≅ A₀
```

Cognitive assemblies need not be stored in full — only a minimal persistence
kernel `𝒦` must survive. Given a reactivation stimulus `σ` drawn from the
SENSORIUM channel space, the regeneration rule set `ℛ` reconstructs a
functionally equivalent assembly from `𝒦`.

> *"Preserve the seed, not the tree.
> The protocol regenerates what persistence compresses."*

---

## 1 · Definitions

### Definition 41 — Regeneration Rule Set (`ℛ`)

A finite set of deterministic or probabilistic rules that, given a
reactivation stimulus `σ`, produce a cognitive assembly functionally
equivalent to a prior assembly. Two assemblies are **functionally equivalent**
if they produce indistinguishable output for all inputs in the operational
domain.

```
ℛ(σ) ≅ A₀  ⟺  ∀x ∈ 𝒟 : ℛ(σ)(x) = A₀(x)
```

### Definition 42 — Reactivation Stimulus (`σ`)

A multimodal vector drawn from the SENSORIUM channel space. Each component
`σⱼ` corresponds to one of the six sensory channels `{𝔸, ℍ, 𝕆, 𝔽, 𝔾, ℙ}`.

```
σ = (σ_𝔸, σ_ℍ, σ_𝕆, σ_𝔽, σ_𝔾, σ_ℙ)    σⱼ ∈ [0, 99]
```

A stimulus may be strong in one channel or arise from a **cooperative sum** of
individually sub-threshold channels:

> A channel `j` is individually sub-threshold when `σⱼ < τⱼ`, but the
> assembly may still be reactivated when `Σ(σⱼ / τⱼ) ≥ 1` (cooperative sum
> criterion).

### Definition 43 — Persistence Kernel (`𝒦`)

The **minimal** subset of an assembly's state that is sufficient for
reconstruction via `ℛ`. The kernel is NOT the assembly itself; it is the
compressed seed from which a functionally equivalent assembly can be
regenerated.

Axiom **E2** (Minimal Persistence) asserts that `𝒦` exists and that
`|𝒦| ≪ |A₀|` in the general case. The goal of the protocol is to identify,
transmit, and protect `𝒦` rather than `A₀`.

---

## 2 · Axioms

| ID | Name | Statement |
|----|------|-----------|
| **E1** | Functional Equivalence | Two assemblies `A` and `A′` are functionally equivalent (`A ≅ A′`) iff `∀x ∈ 𝒟 : A(x) = A′(x)`. |
| **E2** | Minimal Persistence | For every assembly `A₀` there exists `𝒦` with `|𝒦| ≪ |A₀|` such that `ℛ(σ)` applied to `𝒦` yields a functionally equivalent assembly. |

---

## 3 · Cooperative Reactivation

A reactivation stimulus `σ` need not exceed the threshold in any single
sensory channel. The cooperative sum criterion allows sub-threshold channels
to combine:

```
Σⱼ (σⱼ / τⱼ) ≥ 1
```

| Channel | Symbol |
|---------|--------|
| Auditory | `𝔸` |
| Haptic | `ℍ` |
| Optic | `𝕆` |
| Olfactory | `𝔽` |
| Gustatory | `𝔾` |
| Proprioceptive | `ℙ` |

**Example:** If `τ_𝔸 = 40` and `τ_𝕆 = 50`, then `σ = (20, 0, 30, 0, 0, 0)`
gives `Σ = 20/40 + 30/50 = 0.5 + 0.6 = 1.1 ≥ 1` → reactivation occurs even
though neither channel alone exceeds its threshold.

---

## Integration

REGENERATION extends the MCC stack with a **persistence and recall** layer.
Where EGI (SPEC-010) addresses ephemeral lifecycle dynamics, REGENERATION
addresses how assemblies survive beyond dissolution — through minimal kernels
rather than full-state storage.

The three concepts form a pipeline:

1. **Persistence Kernel** (`𝒦`) — compress the assembly to its minimal seed
2. **Reactivation Stimulus** (`σ`) — a SENSORIUM-space vector triggers recall
3. **Regeneration Rule Set** (`ℛ`) — deterministic/probabilistic rules
   reconstruct a functionally equivalent assembly

See [`SENSORIUM.md`](SENSORIUM.md) for the six-channel model and
[`EGI.md`](EGI.md) for the ephemeral lifecycle that precedes regeneration.
