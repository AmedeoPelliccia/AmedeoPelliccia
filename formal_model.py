"""
formal_model.py
===============
Ephemeral Interface Formal Model — Assembly / Decay / Reactivation.

Reference implementation for the three-phase lifecycle described in
FORMAL-MODEL.md and formal-model.yaml:

  1. Assembly   — I_t = Assemble(s, z, K)
  2. Decay      — Decay(I_t) -> r
  3. Reactivation — I_t' = Reactivate(s', r)  iff  A(s, r) > θ

The model extends the simplicial partitioning framework (README §3) with
cost accounting and multi-channel activation gating.

Dependencies: none beyond Python 3.10+ standard library.

Run tests:  python -m pytest tests/test_formal_model.py -v
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional, Sequence


# ──────────────────────────────────────────────
# 1. Lifecycle States
# ──────────────────────────────────────────────

class LifecycleState(Enum):
    """State machine for the ephemeral interface lifecycle."""
    LATENT = "LATENT"
    ACTIVE = "ACTIVE"
    DECAYING = "DECAYING"
    RESIDUAL = "RESIDUAL"
    REACTIVATED = "REACTIVATED"


# ──────────────────────────────────────────────
# 2. Data Structures
# ──────────────────────────────────────────────

@dataclass
class SimplicialStructure:
    """Temporary simplicial structure K over domain Ω.

    A lightweight representation: list of simplices (each simplex is a
    frozenset of vertex indices) plus an optional label.
    """
    label: str
    simplices: List[frozenset] = field(default_factory=list)

    @property
    def dimension(self) -> int:
        """Maximum simplex dimension (|σ| - 1)."""
        if not self.simplices:
            return -1
        return max(len(s) - 1 for s in self.simplices)


@dataclass
class ResidualTrace:
    """Structural signature left behind after interface decay.

    Attributes
    ----------
    values : list[float]
        The trace vector in ℝ^d (same dimensionality as the latent seed).
    affinities : list[float]
        Per-channel affinity α_c ∈ [0, 1] encoding how strongly each
        channel of the original stimulus was imprinted.
    origin_timestamp : str
        ISO-8601 timestamp of the original assembly.
    """
    values: List[float]
    affinities: List[float]
    origin_timestamp: str = ""

    @property
    def dimension(self) -> int:
        return len(self.values)


@dataclass
class EphemeralInterface:
    """An ephemeral interface I_t assembled from stimulus, seed, and structure.

    Attributes
    ----------
    state_vector : list[float]
        The interface state in ℝ^d.
    stimulus : list[float]
        The stimulus s that triggered assembly.
    structure_label : str
        Label of the simplicial structure K used during assembly.
    state : LifecycleState
        Current lifecycle state.
    magnitude : float
        Current magnitude ‖I_t‖ (decreases during decay).
    assembly_timestamp : str
        ISO-8601 timestamp of assembly.
    """
    state_vector: List[float]
    stimulus: List[float]
    structure_label: str
    state: LifecycleState = LifecycleState.ACTIVE
    magnitude: float = 0.0
    assembly_timestamp: str = ""

    def __post_init__(self) -> None:
        if self.magnitude == 0.0:
            self.magnitude = _norm(self.state_vector)
        if not self.assembly_timestamp:
            self.assembly_timestamp = datetime.now().isoformat()


# ──────────────────────────────────────────────
# 3. Activation Function
# ──────────────────────────────────────────────

class ActivationFunction:
    """Multi-channel affinity-based activation with threshold gating.

    A(s, r) = Σ_c (s_c · α_c)

    Reactivation is permitted iff A(s, r) > θ.
    """

    def __init__(self, theta: float) -> None:
        if theta <= 0:
            raise ValueError("Threshold θ must be positive.")
        self.theta = theta

    def score(self, stimulus: Sequence[float],
              affinities: Sequence[float]) -> float:
        """Compute activation score A(s, r) = Σ_c (s_c · α_c)."""
        if len(stimulus) != len(affinities):
            raise ValueError(
                f"Channel count mismatch: stimulus has {len(stimulus)} "
                f"channels, affinities has {len(affinities)}."
            )
        return sum(s_c * a_c for s_c, a_c in zip(stimulus, affinities))

    def can_reactivate(self, stimulus: Sequence[float],
                       affinities: Sequence[float]) -> bool:
        """Return True iff A(s, r) > θ."""
        return self.score(stimulus, affinities) > self.theta


# ──────────────────────────────────────────────
# 4. Cost Accounting
# ──────────────────────────────────────────────

@dataclass
class CostLedger:
    """Tracks cumulative costs for assembly, decay, and reactivation.

    Invariant INV-FM-01: C_r ≤ C_a when sim(s, s') > θ.
    """
    assembly_total: float = 0.0
    decay_total: float = 0.0
    reactivation_total: float = 0.0

    def record_assembly(self, cost: float) -> None:
        self.assembly_total += cost

    def record_decay(self, cost: float) -> None:
        self.decay_total += cost

    def record_reactivation(self, cost: float) -> None:
        self.reactivation_total += cost


# ──────────────────────────────────────────────
# 5. Formal Model (Orchestrator)
# ──────────────────────────────────────────────

class FormalModel:
    """Ephemeral Interface Formal Model.

    Implements the three core operations:
      - Assemble(s, z, K) → I_t
      - Decay(I_t) → r
      - Reactivate(s', r) → I_t'  (iff A(s', r) > θ)

    Parameters
    ----------
    theta : float
        Reactivation threshold for the activation function.
    decay_rate : float
        Multiplicative decay rate per step (0 < rate < 1).
    assembly_base_cost : float
        Base cost for a full assembly operation.
    decay_base_cost : float
        Base cost for a single decay step.
    reactivation_base_cost : float
        Base cost for a reactivation operation.
    """

    def __init__(
        self,
        theta: float = 1.0,
        decay_rate: float = 0.5,
        assembly_base_cost: float = 10.0,
        decay_base_cost: float = 1.0,
        reactivation_base_cost: float = 3.0,
    ) -> None:
        if not (0.0 < decay_rate < 1.0):
            raise ValueError("decay_rate must be in (0, 1).")
        self.activation = ActivationFunction(theta)
        self.decay_rate = decay_rate
        self.assembly_base_cost = assembly_base_cost
        self.decay_base_cost = decay_base_cost
        self.reactivation_base_cost = reactivation_base_cost
        self.costs = CostLedger()

    # ── Assembly ──────────────────────────────

    def assemble(
        self,
        stimulus: List[float],
        seed: List[float],
        structure: SimplicialStructure,
    ) -> EphemeralInterface:
        """I_t = Assemble(s, z, K).

        The interface state vector is the element-wise product of the
        stimulus-modulated seed, constrained by the structure dimension.
        """
        if len(stimulus) != len(seed):
            raise ValueError(
                f"Dimension mismatch: stimulus dim {len(stimulus)} != "
                f"seed dim {len(seed)}."
            )
        # State vector: stimulus modulates the seed
        state = [s_i * z_i for s_i, z_i in zip(stimulus, seed)]
        self.costs.record_assembly(self.assembly_base_cost)

        return EphemeralInterface(
            state_vector=state,
            stimulus=list(stimulus),
            structure_label=structure.label,
            state=LifecycleState.ACTIVE,
        )

    # ── Decay ─────────────────────────────────

    def decay(self, interface: EphemeralInterface) -> ResidualTrace:
        """Decay(I_t) -> r.

        Applies exponential decay until magnitude drops below 1 % of
        the original.  Returns the residual trace.

        Invariant INV-FM-03: ‖I_t‖ decreases monotonically.
        """
        if interface.state not in (LifecycleState.ACTIVE,
                                   LifecycleState.REACTIVATED):
            raise ValueError(
                f"Cannot decay interface in state {interface.state.value}."
            )
        interface.state = LifecycleState.DECAYING

        original_magnitude = interface.magnitude
        threshold = original_magnitude * 0.01  # 1 % residual

        steps = 0
        while interface.magnitude > threshold:
            interface.magnitude *= self.decay_rate
            steps += 1
            self.costs.record_decay(self.decay_base_cost)

        interface.state = LifecycleState.RESIDUAL
        interface.magnitude = 0.0  # fully decayed

        # Residual trace preserves direction (unit vector) and affinities
        norm = _norm(interface.state_vector)
        if norm > 0:
            trace_values = [v / norm for v in interface.state_vector]
        else:
            trace_values = list(interface.state_vector)

        # Affinities: normalised absolute stimulus values → [0, 1]
        max_s = max((abs(v) for v in interface.stimulus), default=1.0)
        if max_s == 0.0:
            max_s = 1.0
        affinities = [min(abs(v) / max_s, 1.0) for v in interface.stimulus]

        return ResidualTrace(
            values=trace_values,
            affinities=affinities,
            origin_timestamp=interface.assembly_timestamp,
        )

    # ── Reactivation ──────────────────────────

    def reactivate(
        self,
        stimulus: List[float],
        trace: ResidualTrace,
    ) -> EphemeralInterface:
        """I_t' = Reactivate(s', r)  iff  A(s', r) > θ.

        Raises ValueError if the activation threshold is not exceeded
        (INV-FM-02).
        """
        if not self.activation.can_reactivate(stimulus, trace.affinities):
            score = self.activation.score(stimulus, trace.affinities)
            raise ValueError(
                f"Activation score {score:.4f} does not exceed "
                f"threshold {self.activation.theta:.4f}. "
                f"Reactivation denied (INV-FM-02)."
            )

        # Reactivated state vector: stimulus modulates the residual trace
        state = [s_i * r_i for s_i, r_i in zip(stimulus, trace.values)]
        self.costs.record_reactivation(self.reactivation_base_cost)

        return EphemeralInterface(
            state_vector=state,
            stimulus=list(stimulus),
            structure_label="reactivated",
            state=LifecycleState.REACTIVATED,
        )

    # ── Similarity ────────────────────────────

    @staticmethod
    def similarity(s1: Sequence[float], s2: Sequence[float]) -> float:
        """Cosine similarity between two stimulus vectors.

        Returns a value in [-1, 1].  Used for cost constraint
        checking: C_r ≤ C_a only if sim(s, s') > θ.
        """
        dot = sum(a * b for a, b in zip(s1, s2))
        n1 = _norm(s1)
        n2 = _norm(s2)
        if n1 == 0.0 or n2 == 0.0:
            return 0.0
        return dot / (n1 * n2)

    def check_cost_invariant(
        self,
        original_stimulus: Sequence[float],
        new_stimulus: Sequence[float],
    ) -> bool:
        """Verify INV-FM-01: C_r ≤ C_a when sim(s, s') > θ.

        Returns True if the invariant holds.  The invariant is trivially
        satisfied when similarity is below the threshold (full assembly
        is expected in that case).
        """
        sim = self.similarity(original_stimulus, new_stimulus)
        if sim > self.activation.theta:
            return self.reactivation_base_cost <= self.assembly_base_cost
        return True  # not applicable — full assembly expected


# ──────────────────────────────────────────────
# Utilities
# ──────────────────────────────────────────────

def _norm(v: Sequence[float]) -> float:
    """Euclidean norm of a vector."""
    return math.sqrt(sum(x * x for x in v))
