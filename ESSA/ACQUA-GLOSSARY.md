# ACQUA — Glossary and Acronyms

**Operational, Architectural, and Computational Terminology**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-ACQUA-GLOSS-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Glossary |
| **Parent** | ESSA-DOC-ACQUA-001 ([ACQUA.md](ACQUA.md)) |
| **Companion** | [`acqua-glossary.yaml`](acqua-glossary.yaml) |
| **Related** | [`ACQUA.md`](ACQUA.md) · [`QQQ.md`](QQQ.md) · [`ANNEX-A-glossary.md`](ANNEX-A-glossary.md) |
| **Last Updated** | 2026-03-10 |

---

## Purpose

This glossary standardizes the terminology used in the ACQUA (Aerospace Computational Quantum Universal Architecture) framework and the QQQ (Quasi–Quanto–Quantum) regime model.

All terms defined herein **SHALL** be interpreted consistently across mission, system, computational, quantum, and governance layers of the architecture.

---

## A

### ACQUA — Aerospace Computational Quantum Universal Architecture

Multilayer architectural framework integrating aerospace infrastructure, classical computing, artificial intelligence, and quantum technologies within a governed operational system.

Within this repository's architectural framing, ACQUA is also the **quantum
joining ecosystems companion assy** — the companion assembly that joins
mission, system, compute, quantum, and governance ecosystems into a single
architectural continuum.

```
ACQUA = ⟨ L_M, L_S, L_C, L_Q, L_G ⟩
```

See [`ACQUA.md`](ACQUA.md).

---

### Actuator

Device that converts computational commands into physical actions.

Examples:
- Thrusters
- Control surfaces
- Reaction wheels
- Robotic mechanisms

---

### Algorithmic Control

Deterministic or probabilistic algorithms governing system behavior.

---

### AOCS — Attitude and Orbit Control System

Subsystem responsible for spacecraft orientation and orbit control.

---

## C

### Coherence (`Λ`)

Degree of synchronization or correlated behavior across system components.

One of the four variables in the QQQ structural regime parameter:

```
λ = αC + βI + γΛ - δO
```

High coherence (`Λ`) drives the system toward the **Quantum** regime.

---

### Compute Layer (`L_C`)

Architectural layer responsible for data processing, state estimation, prediction, and decision-making.

Integrates three computational paradigms:

| Paradigm | QQQ Regime | Formula |
|----------|------------|---------|
| Deterministic | Quasi | `x_{t+1} = f(x_t, u_t)` |
| Probabilistic | Quanto | `P(X_{t+1} \| X_t)` |
| Quantum-enhanced | Quantum | `\|ψ(t)⟩ = U(t)\|ψ₀⟩` |

---

### Control Function

Mathematical mapping describing system evolution:

```
x_{t+1} = f(x_t, u_t)
```

Characteristic of the **Quasi** (deterministic) regime.

---

### Coupling (`C`)

Degree of interaction among subsystems within a complex system.

One of the four variables in the QQQ structural regime parameter. High coupling contributes to higher `λ`, potentially shifting the system toward more advanced regimes.

---

### Cyber-Physical System (CPS)

Integrated system combining computational elements with physical processes.

---

## D

### Data Acquisition

Process of collecting data from sensors, telemetry streams, and external systems.

Modeled as:

```
D(t) = Φ(H, t)
```

where `H = { h_1, h_2, ..., h_n }` is the hardware set.

---

### Deterministic Computing

Computation producing reproducible results from identical inputs.

Characteristic of the **Quasi** regime.

---

### Digital Twin

Dynamic computational model replicating a physical system's behavior.

Operates primarily in the **Quanto** regime (probabilistic adaptation and ML-based prediction).

---

### Dissipation (`O`)

Loss of energy, structure, or coherence due to noise, friction, or entropy.

One of the four variables in the QQQ structural regime parameter. High dissipation lowers `λ`, driving the system toward the **Quasi** regime.

---

## F

### FDIR — Fault Detection, Isolation and Recovery

Autonomous subsystem responsible for identifying and mitigating failures.

---

## G

### GNC — Guidance, Navigation and Control

System responsible for vehicle trajectory and orientation.

---

### Governance Layer (`L_G`)

Architectural layer responsible for policy enforcement, safety assurance, compliance, configuration control, and traceability.

Acts as a transversal constraint over all other layers:

```
L_G ⊣ { L_M, L_S, L_C, L_Q }
```

---

## H

### HPC — High Performance Computing

Computational infrastructure used for large-scale simulation and data processing.

---

## I

### ICD — Interface Control Document

Technical document specifying interfaces between subsystems.

---

### Information Density (`I`)

Measure of information processed or exchanged within the system.

One of the four variables in the QQQ structural regime parameter:

```
λ = αC + βI + γΛ - δO
```

---

## L

### Layer

Functional abstraction level within the ACQUA architecture.

ACQUA defines five layers:

| # | Layer | Symbol |
|---|-------|--------|
| 1 | Mission Layer | `L_M` |
| 2 | System Layer | `L_S` |
| 3 | Compute Layer | `L_C` |
| 4 | Quantum Layer | `L_Q` |
| 5 | Governance Layer | `L_G` |

---

## M

### Mission Authority

Entity responsible for mission objectives and operational decision-making.

Has **Accountable (A)** authority over operational objectives.

---

### Mission Layer (`L_M`)

Defines operational goals, mission scenarios, constraints, and success criteria.

```
L_M = { G, K, Ω, Σ }
```

where `G` = Goals, `K` = KPIs, `Ω` = operational constraints, `Σ` = mission scenarios.

---

## O

### Operational Envelope

Range of environmental and operational conditions under which a system operates safely.

---

### Optimization

Process of determining the best solution within defined constraints.

Applied at multiple levels in ACQUA: classical optimization in `L_C`, quantum optimization in `L_Q`.

---

## Q

### QKD — Quantum Key Distribution

Cryptographic protocol exploiting quantum properties to distribute encryption keys with information-theoretic security.

Hosted in the **Quantum Layer** (`L_Q`).

---

### QQQ Framework — Quasi–Quanto–Quantum

Conceptual model describing three regimes of system organization.

| Regime | Character | Central Idea |
|--------|-----------|--------------|
| **Quasi** | Deterministic rule-based | state → unique outcome |
| **Quanto** | Probabilistic adaptive | state → distribution of outcomes |
| **Quantum** | Coherent correlated | state → coherent amplitudes |

See [`QQQ.md`](QQQ.md).

---

### Quantum Layer (`L_Q`)

Architectural layer integrating quantum technologies: sensing, optimization, simulation, and communication.

```
L_Q = { Q_s, Q_o, Q_c, Q_n }
```

| Symbol | Function |
|--------|----------|
| `Q_s` | Quantum sensing |
| `Q_o` | Quantum optimization |
| `Q_c` | Quantum computing |
| `Q_n` | Quantum networking |

---

### Quantum Optimization

Application of quantum algorithms to solve complex optimization problems more efficiently than classical methods.

---

### Quantum State

Mathematical representation of a quantum system state as a vector in Hilbert space:

```
|ψ⟩
```

Evolution governed by:

```
iℏ ∂/∂t |ψ⟩ = Ĥ|ψ⟩
```

---

## R

### Requirement Traceability

Ability to link requirements to design, implementation, and verification artefacts.

Formal traceability chain in ACQUA:

```
G_i → R_i → S_i → C_i → Q_i → V_i
```

---

## S

### Sensor

Device measuring environmental or system variables.

Examples:
- Optical sensors
- Radar
- Inertial sensors
- Quantum sensors

---

### State Estimation

Process of inferring the internal state of a system from observations.

Performed in the **Compute Layer** (`L_C`) via state estimation function `X̂`.

---

### System Layer (`L_S`)

Defines the physical architecture of platforms, sensors, actuators, and networks.

```
L_S = { P, S, A, N, I }
```

where `P` = Platforms, `S` = Sensors, `A` = Actuators, `N` = Networks, `I` = Interfaces.

---

## T

### Telemetry

Transmission of measurement data from remote systems to control centres.

---

### Traceability

Capability to track relationships among requirements, system elements, and verification evidence.

See: Requirement Traceability.

---

### TRL — Technology Readiness Level

Scale (1–9) used to assess the maturity of a technology or system component.

---

## V

### Validation

Confirmation that the system fulfils its intended operational purpose.

Final element `V_i` in the ACQUA traceability chain.

---

### Verification

Confirmation that a system satisfies specified requirements.

---

## Architectural Summary

The ACQUA architecture is formally expressed as:

```
ACQUA = ⟨ L_M, L_S, L_C, L_Q, L_G ⟩
```

| Symbol | Layer | Governing Authority |
|--------|-------|---------------------|
| `L_M` | Mission Layer | Mission Authority / Programme Board |
| `L_S` | System Layer | Engineering Authority / Chief Systems Engineer |
| `L_C` | Compute Layer | Software Authority / Avionics Authority |
| `L_Q` | Quantum Layer | Quantum Systems Authority / Advanced Technology Authority |
| `L_G` | Governance Layer | Governance Board / Safety / Compliance / CCB |

---

## Regime Parameter Summary

System behavior across QQQ regimes is governed by:

```
λ = αC + βI + γΛ - δO
```

| Symbol | Meaning | Effect on λ |
|--------|---------|-------------|
| `C` | Coupling | Increases λ |
| `I` | Information density | Increases λ |
| `Λ` | Coherence | Increases λ |
| `O` | Dissipation | Decreases λ |

| Condition | Regime |
|-----------|--------|
| `λ < λ₁` | **Quasi** — deterministic control |
| `λ₁ ≤ λ < λ₂` | **Quanto** — probabilistic adaptive systems |
| `λ ≥ λ₂` | **Quantum** — coherent coordination |
