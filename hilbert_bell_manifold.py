"""
hilbert_bell_manifold.py
========================
12×12 Intentional Hilbert–Bell Manifold implementation.

Implements the Quantum-Governed Topography described in README Part VI:
  • 12-dimensional admissible Hilbert subspace
  • Deterministic correction and transition operators
  • Selective data-mining with Relevance / Quality / Compliance predicate
  • Top-12 capacity bounding
  • Tunneled entanglement topography
  • Bell-bounded (CHSH ≤ 2) correlation envelope
  • Intentional Hamiltonian evolution

Three-Layer Architecture (§31):
  Layer 1 — Spatial Discretisation  : domain Ω partitioned into N cells
  Layer 2 — State Space (Hilbert)   : ℂ^N induced by discretisation
  Layer 3 — Physical Field          : tensorial (classical) or operator (quantum)

Quantum–Classical Boundary (§33):
  • Coherence Reduction Map R(ρ) — information-theoretic, not geometric
  • Local Projection Operator  P_i : H_i → ℝ^k
  • Decoherence Threshold  τ_decoherence ≪ τ_dynamics ⟹ classical treatment

Reference: quantum-manifold.yaml (schema_version 1.1.0)

Dependencies (core): none beyond the Python 3.10+ standard library.
Dependencies (demo): PyYAML — install via ``pip install pyyaml``.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable


# ──────────────────────────────────────────────
# 1. Basis State
# ──────────────────────────────────────────────

@dataclass
class BasisState:
    """One of the 12 ontological basis vectors |S_k⟩."""

    index: int
    label: str
    description: str = ""

    def ket(self) -> str:
        # Render ket labels as S1–S12 to match YAML/README, while keeping
        # `index` 0-based internally (S1 ↔ index 0, S12 ↔ index 11).
        return f"|S_{self.index + 1}⟩"


# ──────────────────────────────────────────────
# 2. Quantum State  |ψ⟩ = Σ α_k |S_k⟩
# ──────────────────────────────────────────────

class QuantumState:
    """Normalised state vector living in H_adm (dim ≤ 12)."""

    def __init__(self, amplitudes: list[complex], basis: list[BasisState]) -> None:
        if len(amplitudes) != len(basis):
            raise ValueError("Amplitude count must equal basis size.")
        self._basis = list(basis)
        self._amplitudes = list(amplitudes)
        self._normalize()

    # -- properties ----------------------------------------------------------

    @property
    def dim(self) -> int:
        return len(self._basis)

    @property
    def amplitudes(self) -> list[complex]:
        return list(self._amplitudes)

    @property
    def probabilities(self) -> list[float]:
        return [abs(a) ** 2 for a in self._amplitudes]

    # -- projection onto H_adm ----------------------------------------------

    def project(self) -> None:
        """Apply Π_adm (re-normalise within current basis)."""
        self._normalize()

    # -- internal ------------------------------------------------------------

    def set_amplitudes(self, amplitudes: list[complex]) -> None:
        """Replace amplitudes and re-normalise."""
        self._amplitudes = list(amplitudes)
        self._normalize()

    def _normalize(self) -> None:
        norm = math.sqrt(sum(abs(a) ** 2 for a in self._amplitudes))
        if norm == 0:
            raise ValueError("Zero-norm state is not physical.")
        self._amplitudes = [a / norm for a in self._amplitudes]


# ──────────────────────────────────────────────
# 3. Entanglement Topography
# ──────────────────────────────────────────────

@dataclass
class CouplingPair:
    """Tunneled entanglement coupling T_ij between two basis states."""

    i: int
    j: int
    t_ij: float
    label: str = ""


class EntanglementMatrix:
    """E_ij(t) = ℰ(S_i, S_j) — symmetric 12×12 coupling matrix."""

    def __init__(self, dim: int = 12) -> None:
        self._dim = dim
        self._matrix: list[list[float]] = [
            [0.0] * dim for _ in range(dim)
        ]

    def set_coupling(self, pair: CouplingPair) -> None:
        self._matrix[pair.i][pair.j] = pair.t_ij
        self._matrix[pair.j][pair.i] = pair.t_ij

    def get(self, i: int, j: int) -> float:
        return self._matrix[i][j]

    @property
    def dim(self) -> int:
        return self._dim

    @property
    def matrix(self) -> list[list[float]]:
        return [row[:] for row in self._matrix]


# ──────────────────────────────────────────────
# 4. Bell-Bounded Correlation Envelope
# ──────────────────────────────────────────────

CHSH_CLASSICAL_LIMIT = 2.0


def check_bell_bound(correlators: tuple[float, float, float, float]) -> bool:
    """Return True when |B_ij| = |⟨A₁B₁⟩+⟨A₁B₂⟩+⟨A₂B₁⟩−⟨A₂B₂⟩| ≤ 2."""
    a1b1, a1b2, a2b1, a2b2 = correlators
    b_value = a1b1 + a1b2 + a2b1 - a2b2
    return abs(b_value) <= CHSH_CLASSICAL_LIMIT


# ──────────────────────────────────────────────
# 5. Selective Data-Mining Operator Φ
# ──────────────────────────────────────────────

@dataclass
class DataCandidate:
    """A candidate datum to be evaluated by the selection predicate."""

    id: str
    payload: Any = None
    relevance: float = 0.0
    quality: float = 0.0
    compliance: float = 0.0

    @property
    def score(self) -> float:
        return self.relevance * self.quality * self.compliance


def selection_predicate(
    candidate: DataCandidate,
    r_threshold: float = 0.5,
    q_threshold: float = 0.5,
    c_threshold: float = 0.5,
) -> bool:
    """f(d) = R(d) ∧ Q(d) ∧ C(d)."""
    return (
        candidate.relevance >= r_threshold
        and candidate.quality >= q_threshold
        and candidate.compliance >= c_threshold
    )


K_MAX = 12


def selective_mining(
    pool: list[DataCandidate],
    r_threshold: float = 0.5,
    q_threshold: float = 0.5,
    c_threshold: float = 0.5,
) -> list[DataCandidate]:
    """Φ₁₂(D) = TopK(D, score, 12) after predicate filtering."""
    filtered = [
        d for d in pool
        if selection_predicate(d, r_threshold, q_threshold, c_threshold)
    ]
    filtered.sort(key=lambda d: d.score, reverse=True)
    return filtered[:K_MAX]


# ──────────────────────────────────────────────
# 6. Deterministic Generative Core
# ──────────────────────────────────────────────

CorrectionFn = Callable[[Any, dict], Any]
TransitionFn = Callable[[Any, dict], Any]


@dataclass
class GovernedState:
    """S_t — the governed state at time-step t."""

    t: int = 0
    registers: dict = field(default_factory=dict)


class DeterministicCore:
    """Y_t = F(C(X_t, S_t), S_t) — no hidden entropy."""

    def __init__(
        self,
        correction: CorrectionFn,
        transition: TransitionFn,
    ) -> None:
        self._correction = correction
        self._transition = transition

    def step(self, x_t: Any, state: GovernedState) -> Any:
        corrected = self._correction(x_t, state.registers)
        y_t = self._transition(corrected, state.registers)
        state.t += 1
        return y_t


# ──────────────────────────────────────────────
# 7. Intentional Hamiltonian Evolution
# ──────────────────────────────────────────────

class HamiltonianEvolver:
    """Discrete-time approximate evolution under H = H_0 + H_int + H_intent.

    Uses a first-order (Euler) update with post-step renormalisation.
    This preserves norm but is not strictly unitary; for exact unitarity
    use matrix exponentiation of H.  Sufficient for the bounded
    12-dimensional admissible subspace at small dt.

    Each step:
      1. Evolve amplitudes via first-order update.
      2. Project back onto H_adm (re-normalise).
    """

    def __init__(
        self,
        entanglement: EntanglementMatrix,
        intent_weights: list[float] | None = None,
        dt: float = 0.01,
    ) -> None:
        dim = entanglement.dim
        self._entanglement = entanglement
        self._intent = intent_weights or [0.0] * dim
        if len(self._intent) != dim:
            raise ValueError("Intent weights must match basis dimension.")
        self._dt = dt

    def evolve(self, state: QuantumState) -> None:
        """One discrete step of Hamiltonian evolution + Π_adm projection."""
        dim = state.dim
        amps = state.amplitudes  # cache once (property returns a copy)
        new_amps: list[complex] = []
        for k in range(dim):
            # H_0 contribution (diagonal phase)
            phase_k = complex(0, -self._dt * self._intent[k])
            # H_int contribution (off-diagonal tunnelling)
            coupling_sum = complex(0, 0)
            for j in range(dim):
                if j != k:
                    t_kj = self._entanglement.get(k, j)
                    coupling_sum += t_kj * amps[j]
            phase_contribution = phase_k * amps[k]
            coupling_contribution = complex(0, -self._dt) * coupling_sum
            new_amp = amps[k] + phase_contribution + coupling_contribution
            new_amps.append(new_amp)
        state.set_amplitudes(new_amps)  # Π_adm re-normalisation


# ──────────────────────────────────────────────
# 8. Three-Layer Architecture
# ──────────────────────────────────────────────
#
# Layer 1 — Spatial Discretisation (domain partition)
# Layer 2 — State Space (induced Hilbert space)
# Layer 3 — Physical Field (classical tensor / quantum operator)
#
# These three levels are formally distinct.  The spatial
# discretisation *induces* a finite-dimensional Hilbert space
# but does not replace it conceptually.  The physical field
# acts *on* the state space, not on the spatial grid directly.
# ──────────────────────────────────────────────

@dataclass
class VoxelCell:
    """Layer 1 — one cell V_i in the spatial partition Ω = ⋃ V_i."""

    index: int
    label: str = ""
    regime: str = "quantum"  # "quantum" | "classical" | "hybrid"


class SpatialDomain:
    """Layer 1 — discrete partition of the physical domain Ω.

    Ω = ⋃_{i=1}^{N} V_i

    The partition induces, but is not identical to, the Hilbert space.
    L²(Ω) → ℂ^N  (quantum) or ℝ^N (classical).
    """

    def __init__(self) -> None:
        self._cells: list[VoxelCell] = []

    def add_cell(self, index: int, label: str = "", regime: str = "quantum") -> None:
        self._cells.append(VoxelCell(index=index, label=label, regime=regime))

    @property
    def cells(self) -> list[VoxelCell]:
        return list(self._cells)

    @property
    def size(self) -> int:
        return len(self._cells)

    def quantum_cells(self) -> list[VoxelCell]:
        return [c for c in self._cells if c.regime == "quantum"]

    def classical_cells(self) -> list[VoxelCell]:
        return [c for c in self._cells if c.regime == "classical"]

    def hybrid_cells(self) -> list[VoxelCell]:
        return [c for c in self._cells if c.regime == "hybrid"]


# ──────────────────────────────────────────────
# 9. Coherence Reduction Map  R(ρ)
# ──────────────────────────────────────────────
#
# The quantum-classical boundary is NOT a geometric surface.
# It is an information-theoretic map:
#
#   R(ρ) = coherence reduction mapping
#
# Implemented via:
#   • Local projection  P_i : H_i → R^k   (quantum → classical observables)
#   • Decoherence threshold  τ_decoherence ≪ τ_dynamics
#
# When τ_decoherence ≪ τ_dynamics for a cell, the density matrix
# ρ → diagonal form, and the cell can be treated classically.
# ──────────────────────────────────────────────

@dataclass
class CoherenceMetrics:
    """Coherence diagnostics for a single cell."""

    cell_index: int
    off_diagonal_norm: float  # ‖ρ − diag(ρ)‖_F
    tau_decoherence: float    # decoherence timescale
    tau_dynamics: float       # dynamical timescale
    regime: str = ""          # computed classification

    @property
    def is_classical(self) -> bool:
        return self.tau_decoherence < self.tau_dynamics * 0.01

    @property
    def is_quantum(self) -> bool:
        return self.tau_decoherence >= self.tau_dynamics


class CoherenceReductionMap:
    """R(ρ) — quantum-classical boundary as information reduction map.

    For each cell i, defines:
      P_i : H_i → R^k    (local projection operator)
      σ_classical = Tr(ρ T̂)   (classical observable extraction)

    The boundary is a dynamic threshold, not a geometric surface:
      τ_decoherence ≪ τ_dynamics  ⟹  cell treated classically
      τ_decoherence ≥ τ_dynamics  ⟹  cell requires quantum evolution
    """

    def project_to_classical(self, probabilities: list[float], cell_index: int) -> list[float]:
        """P_i : H_i → R^k — extract classical observables from quantum state.

        σ_classical = Tr(ρ T̂) — here simplified to the diagonal
        (probability) extraction, which is the natural classical limit.
        """
        if cell_index < 0 or cell_index >= len(probabilities):
            raise IndexError(f"Cell index {cell_index} out of range.")
        return [probabilities[cell_index]]

    def classify_regime(
        self,
        cell_index: int,
        off_diagonal_norm: float,
        tau_decoherence: float,
        tau_dynamics: float,
    ) -> CoherenceMetrics:
        """Classify a cell as quantum, classical, or hybrid based on
        the decoherence threshold criterion."""
        metrics = CoherenceMetrics(
            cell_index=cell_index,
            off_diagonal_norm=off_diagonal_norm,
            tau_decoherence=tau_decoherence,
            tau_dynamics=tau_dynamics,
        )
        if metrics.is_classical:
            metrics.regime = "classical"
        elif metrics.is_quantum:
            metrics.regime = "quantum"
        else:
            metrics.regime = "hybrid"
        return metrics

    def reduce(
        self,
        amplitudes: list[complex],
        tau_decoherence: float,
        tau_dynamics: float,
        cell_index: int = 0,
    ) -> tuple[list[float], str]:
        """Full coherence reduction: classify regime and extract state diagonal.

        Returns (state_diagonal, regime), where the state diagonal is the
        vector of |α_k|² (diagonal of ρ in the computational basis).
        """
        state_diagonal = [abs(a) ** 2 for a in amplitudes]
        n = len(amplitudes)
        # Frobenius norm of off-diagonal part: ‖ρ − diag(ρ)‖_F
        # For a pure state ρ = |ψ⟩⟨ψ|, off-diagonal entries are α_i α_j*.
        # ‖off-diag‖_F = sqrt( Σ_{i≠j} |α_i α_j*|² )
        off_diag_norm_sq = sum(
            abs(amplitudes[i]) ** 2 * abs(amplitudes[j]) ** 2
            for i in range(n)
            for j in range(n)
            if i != j
        )
        off_diag_norm = math.sqrt(off_diag_norm_sq)
        metrics = self.classify_regime(
            cell_index, off_diag_norm, tau_decoherence, tau_dynamics,
        )
        return state_diagonal, metrics.regime


# ──────────────────────────────────────────────
# 10. Full Manifold Orchestrator
# ──────────────────────────────────────────────

class HilbertBellManifold:
    """Top-level orchestrator for the 12×12 Intentional Hilbert–Bell Manifold.

    Integrates three formally distinct layers:
      Layer 1 — SpatialDomain        : physical domain partition Ω = ⋃ V_i
      Layer 2 — QuantumState + basis  : induced Hilbert space ℂ^N
      Layer 3 — HamiltonianEvolver    : physical field (operator on state space)

    Plus the quantum-classical boundary:
      CoherenceReductionMap R(ρ) — information-theoretic, not geometric.
    """

    def __init__(self) -> None:
        # -- Layer 1: spatial discretisation ---------------------------------
        self.domain = SpatialDomain()
        # -- Layer 2: state space (Hilbert) ----------------------------------
        self.basis: list[BasisState] = []
        self.state: QuantumState | None = None
        # -- Layer 3: physical field (operators) -----------------------------
        self.entanglement = EntanglementMatrix(K_MAX)
        self.evolver: HamiltonianEvolver | None = None
        # -- Quantum-classical boundary --------------------------------------
        self.coherence_map = CoherenceReductionMap()
        # -- audit -----------------------------------------------------------
        self._audit: list[dict] = []

    # -- setup ---------------------------------------------------------------

    def add_basis_state(self, index: int, label: str, description: str = "") -> None:
        if len(self.basis) >= K_MAX:
            raise ValueError(f"Cannot exceed K_max={K_MAX} basis states.")
        self.basis.append(BasisState(index=index, label=label, description=description))

    def set_coupling(self, pair: CouplingPair) -> None:
        self.entanglement.set_coupling(pair)

    def initialise_state(self, amplitudes: list[complex] | None = None) -> None:
        if len(self.basis) == 0:
            raise ValueError("Basis must be populated before state initialisation.")
        if amplitudes is None:
            # Equal superposition
            n = len(self.basis)
            amplitudes = [complex(1.0 / math.sqrt(n))] * n
        self.state = QuantumState(amplitudes, self.basis)

    def set_evolver(self, intent_weights: list[float] | None = None, dt: float = 0.01) -> None:
        self.evolver = HamiltonianEvolver(
            self.entanglement,
            intent_weights=intent_weights,
            dt=dt,
        )

    # -- evolution -----------------------------------------------------------

    def evolve(self, steps: int = 1) -> None:
        if self.evolver is None or self.state is None:
            raise ValueError("Evolver and state must be initialised.")
        for _ in range(steps):
            self.evolver.evolve(self.state)
            self._record_snapshot()

    def check_bell_bounds(self, correlators: tuple[float, float, float, float]) -> bool:
        result = check_bell_bound(correlators)
        self._audit.append({
            "event": "bell_check",
            "correlators": list(correlators),
            "passed": result,
            "timestamp": datetime.now().isoformat(),
        })
        return result

    # -- data mining ---------------------------------------------------------

    def mine(self, pool: list[DataCandidate], **kwargs: float) -> list[DataCandidate]:
        selected = selective_mining(pool, **kwargs)
        self._audit.append({
            "event": "data_mining",
            "pool_size": len(pool),
            "selected_count": len(selected),
            "timestamp": datetime.now().isoformat(),
        })
        return selected

    # -- coherence reduction (quantum-classical boundary) --------------------

    def reduce_to_classical(
        self,
        tau_decoherence: float,
        tau_dynamics: float,
    ) -> tuple[list[float], str]:
        """Apply coherence reduction map R(ρ) to the current state.

        Returns (state_diagonal, regime_classification), where state_diagonal
        is the vector of |α_k|² (diagonal of ρ in the computational basis).

        The boundary is an information-theoretic threshold:
          τ_decoherence ≪ τ_dynamics ⟹ ρ → diagonal ⟹ classical
          τ_decoherence ≥ τ_dynamics ⟹ full quantum evolution required
        """
        if self.state is None:
            raise ValueError("State must be initialised.")
        state_diagonal, regime = self.coherence_map.reduce(
            self.state.amplitudes, tau_decoherence, tau_dynamics,
        )
        self._audit.append({
            "event": "coherence_reduction",
            "regime": regime,
            "tau_decoherence": tau_decoherence,
            "tau_dynamics": tau_dynamics,
            "timestamp": datetime.now().isoformat(),
        })
        return state_diagonal, regime

    # -- audit ---------------------------------------------------------------

    def audit_trail(self) -> list[dict]:
        return list(self._audit)

    def export_audit(self, path: str) -> None:
        with open(path, "w") as fh:
            json.dump(self._audit, fh, indent=2)

    # -- internal ------------------------------------------------------------

    def _record_snapshot(self) -> None:
        if self.state is None:
            return
        self._audit.append({
            "event": "evolution_step",
            "probabilities": self.state.probabilities,
            "timestamp": datetime.now().isoformat(),
        })


# ──────────────────────────────────────────────
# Demo / self-test
# ──────────────────────────────────────────────

if __name__ == "__main__":
    import yaml  # type: ignore[import-untyped]

    # Load manifold config
    with open("quantum-manifold.yaml") as f:
        cfg = yaml.safe_load(f)

    manifold = HilbertBellManifold()

    # --- Layer 1: Spatial Discretisation ---
    for s in cfg["basis_states"]:
        idx = int(s["id"].replace("S", "")) - 1
        manifold.domain.add_cell(idx, s["label"], regime="quantum")

    # --- Layer 2: State Space (Hilbert) ---
    for s in cfg["basis_states"]:
        idx = int(s["id"].replace("S", "")) - 1
        manifold.add_basis_state(idx, s["label"], s.get("description", ""))

    # --- Layer 3: Physical Field (operators) ---
    for cp in cfg["entanglement"]["coupling_pairs"]:
        i = int(cp["pair"][0].replace("S", "")) - 1
        j = int(cp["pair"][1].replace("S", "")) - 1
        manifold.set_coupling(CouplingPair(i, j, cp["T_ij"], cp.get("label", "")))

    # Initialise equal superposition
    manifold.initialise_state()
    manifold.set_evolver(dt=0.01)

    # Evolve 10 steps
    manifold.evolve(steps=10)

    # Bell check (example correlators within classical limit)
    manifold.check_bell_bounds((0.5, 0.5, 0.5, -0.4))

    # --- Coherence Reduction Map R(ρ) ---
    # Case 1: τ_decoherence ≪ τ_dynamics  →  classical regime
    obs_cl, regime_cl = manifold.reduce_to_classical(
        tau_decoherence=0.001, tau_dynamics=1.0,
    )
    # Case 2: τ_decoherence ≈ τ_dynamics  →  quantum regime
    obs_qu, regime_qu = manifold.reduce_to_classical(
        tau_decoherence=1.0, tau_dynamics=1.0,
    )

    # Selective data mining demo
    pool = [
        DataCandidate("d1", relevance=0.9, quality=0.8, compliance=0.95),
        DataCandidate("d2", relevance=0.3, quality=0.9, compliance=0.7),
        DataCandidate("d3", relevance=0.7, quality=0.7, compliance=0.8),
    ]
    selected = manifold.mine(pool)

    # Report
    print("=== Hilbert–Bell Manifold Demo ===")
    print(f"Layer 1 cells   : {manifold.domain.size}")
    print(f"Layer 2 dim     : {len(manifold.basis)}")
    print(f"Final probs     : {[round(p, 4) for p in manifold.state.probabilities]}")
    print(f"R(ρ) classical  : regime={regime_cl}")
    print(f"R(ρ) quantum    : regime={regime_qu}")
    print(f"Mining selected : {len(selected)} / {len(pool)}")
    print(f"Audit entries   : {len(manifold.audit_trail())}")

    manifold.export_audit("/tmp/hilbert_bell_audit.json")
    print("Audit exported  : /tmp/hilbert_bell_audit.json")
