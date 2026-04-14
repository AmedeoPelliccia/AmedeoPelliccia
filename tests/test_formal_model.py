"""
tests/test_formal_model.py — Formal Model Validation
=====================================================

Validates the Ephemeral Interface Formal Model described in
FORMAL-MODEL.md and formal-model.yaml.

Run with:  python -m pytest tests/test_formal_model.py -v
"""

from __future__ import annotations

import math

import pytest

from formal_model import (
    ActivationFunction,
    CostLedger,
    EphemeralInterface,
    FormalModel,
    LifecycleState,
    ResidualTrace,
    SimplicialStructure,
    _norm,
)


# ──────────────────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────────────────

@pytest.fixture()
def model() -> FormalModel:
    """Default formal model with θ=1.0, decay_rate=0.5."""
    return FormalModel(
        theta=1.0,
        decay_rate=0.5,
        assembly_base_cost=10.0,
        decay_base_cost=1.0,
        reactivation_base_cost=3.0,
    )


@pytest.fixture()
def structure() -> SimplicialStructure:
    """Simple 2-simplex structure."""
    return SimplicialStructure(
        label="test-K",
        simplices=[
            frozenset({0, 1}),
            frozenset({1, 2}),
            frozenset({0, 1, 2}),
        ],
    )


@pytest.fixture()
def stimulus() -> list[float]:
    return [2.0, 3.0, 1.0]


@pytest.fixture()
def seed() -> list[float]:
    return [1.0, 0.5, 2.0]


# ──────────────────────────────────────────────────────────────────────────────
# SimplicialStructure
# ──────────────────────────────────────────────────────────────────────────────

class TestSimplicialStructure:
    def test_dimension_2simplex(self, structure: SimplicialStructure) -> None:
        assert structure.dimension == 2

    def test_dimension_empty(self) -> None:
        k = SimplicialStructure(label="empty")
        assert k.dimension == -1

    def test_label(self, structure: SimplicialStructure) -> None:
        assert structure.label == "test-K"


# ──────────────────────────────────────────────────────────────────────────────
# ActivationFunction
# ──────────────────────────────────────────────────────────────────────────────

class TestActivationFunction:
    def test_score_computation(self) -> None:
        af = ActivationFunction(theta=1.0)
        s = [2.0, 3.0]
        a = [0.5, 0.8]
        # 2.0*0.5 + 3.0*0.8 = 1.0 + 2.4 = 3.4
        assert af.score(s, a) == pytest.approx(3.4)

    def test_can_reactivate_above_threshold(self) -> None:
        af = ActivationFunction(theta=1.0)
        assert af.can_reactivate([2.0, 3.0], [0.5, 0.8]) is True

    def test_cannot_reactivate_below_threshold(self) -> None:
        af = ActivationFunction(theta=5.0)
        assert af.can_reactivate([1.0, 1.0], [0.1, 0.1]) is False

    def test_cannot_reactivate_at_threshold(self) -> None:
        af = ActivationFunction(theta=2.0)
        # score = 1.0*1.0 + 1.0*1.0 = 2.0, not strictly greater
        assert af.can_reactivate([1.0, 1.0], [1.0, 1.0]) is False

    def test_channel_mismatch_raises(self) -> None:
        af = ActivationFunction(theta=1.0)
        with pytest.raises(ValueError, match="Channel count mismatch"):
            af.score([1.0, 2.0], [0.5])

    def test_theta_must_be_positive(self) -> None:
        with pytest.raises(ValueError, match="positive"):
            ActivationFunction(theta=0.0)


# ──────────────────────────────────────────────────────────────────────────────
# Assembly
# ──────────────────────────────────────────────────────────────────────────────

class TestAssembly:
    def test_state_vector(self, model: FormalModel,
                          stimulus: list, seed: list,
                          structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        expected = [2.0 * 1.0, 3.0 * 0.5, 1.0 * 2.0]
        assert iface.state_vector == expected

    def test_active_state(self, model: FormalModel,
                          stimulus: list, seed: list,
                          structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        assert iface.state == LifecycleState.ACTIVE

    def test_magnitude_positive(self, model: FormalModel,
                                stimulus: list, seed: list,
                                structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        assert iface.magnitude > 0

    def test_cost_recorded(self, model: FormalModel,
                           stimulus: list, seed: list,
                           structure: SimplicialStructure) -> None:
        model.assemble(stimulus, seed, structure)
        assert model.costs.assembly_total == 10.0

    def test_dimension_mismatch_raises(self, model: FormalModel,
                                       structure: SimplicialStructure) -> None:
        with pytest.raises(ValueError, match="Dimension mismatch"):
            model.assemble([1.0, 2.0], [1.0], structure)

    def test_structure_label_preserved(self, model: FormalModel,
                                       stimulus: list, seed: list,
                                       structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        assert iface.structure_label == "test-K"


# ──────────────────────────────────────────────────────────────────────────────
# Decay
# ──────────────────────────────────────────────────────────────────────────────

class TestDecay:
    def test_decay_produces_residual(self, model: FormalModel,
                                     stimulus: list, seed: list,
                                     structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        assert isinstance(trace, ResidualTrace)

    def test_interface_state_after_decay(self, model: FormalModel,
                                         stimulus: list, seed: list,
                                         structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        model.decay(iface)
        assert iface.state == LifecycleState.RESIDUAL

    def test_magnitude_zero_after_decay(self, model: FormalModel,
                                        stimulus: list, seed: list,
                                        structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        model.decay(iface)
        assert iface.magnitude == 0.0

    def test_trace_dimension_matches_seed(self, model: FormalModel,
                                          stimulus: list, seed: list,
                                          structure: SimplicialStructure) -> None:
        """INV-FM-04: dim(r) = dim(z)."""
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        assert trace.dimension == len(seed)

    def test_trace_is_unit_vector(self, model: FormalModel,
                                  stimulus: list, seed: list,
                                  structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        norm = _norm(trace.values)
        assert norm == pytest.approx(1.0, abs=1e-9)

    def test_affinities_in_range(self, model: FormalModel,
                                  stimulus: list, seed: list,
                                  structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        for a in trace.affinities:
            assert 0.0 <= a <= 1.0

    def test_decay_cost_recorded(self, model: FormalModel,
                                  stimulus: list, seed: list,
                                  structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        model.decay(iface)
        assert model.costs.decay_total > 0

    def test_cannot_decay_latent(self, model: FormalModel) -> None:
        iface = EphemeralInterface(
            state_vector=[1.0, 2.0],
            stimulus=[1.0, 1.0],
            structure_label="test",
            state=LifecycleState.LATENT,
        )
        with pytest.raises(ValueError, match="Cannot decay"):
            model.decay(iface)

    def test_cannot_decay_residual(self, model: FormalModel) -> None:
        iface = EphemeralInterface(
            state_vector=[1.0, 2.0],
            stimulus=[1.0, 1.0],
            structure_label="test",
            state=LifecycleState.RESIDUAL,
        )
        with pytest.raises(ValueError, match="Cannot decay"):
            model.decay(iface)


# ──────────────────────────────────────────────────────────────────────────────
# Reactivation
# ──────────────────────────────────────────────────────────────────────────────

class TestReactivation:
    def test_reactivation_succeeds(self, model: FormalModel,
                                    stimulus: list, seed: list,
                                    structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        # Use a strong stimulus to exceed threshold
        new_stimulus = [5.0, 5.0, 5.0]
        reactivated = model.reactivate(new_stimulus, trace)
        assert reactivated.state == LifecycleState.REACTIVATED

    def test_reactivation_denied_below_threshold(self, model: FormalModel) -> None:
        """INV-FM-02: No reactivation if A(s', r) ≤ θ."""
        trace = ResidualTrace(
            values=[1.0, 0.0, 0.0],
            affinities=[0.1, 0.1, 0.1],
        )
        with pytest.raises(ValueError, match="Reactivation denied"):
            model.reactivate([0.5, 0.5, 0.5], trace)

    def test_reactivation_cost_recorded(self, model: FormalModel,
                                         stimulus: list, seed: list,
                                         structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        model.reactivate([5.0, 5.0, 5.0], trace)
        assert model.costs.reactivation_total == 3.0

    def test_reactivated_can_decay_again(self, model: FormalModel,
                                          stimulus: list, seed: list,
                                          structure: SimplicialStructure) -> None:
        iface = model.assemble(stimulus, seed, structure)
        trace = model.decay(iface)
        reactivated = model.reactivate([5.0, 5.0, 5.0], trace)
        trace2 = model.decay(reactivated)
        assert isinstance(trace2, ResidualTrace)
        assert reactivated.state == LifecycleState.RESIDUAL


# ──────────────────────────────────────────────────────────────────────────────
# Similarity & Cost Invariant
# ──────────────────────────────────────────────────────────────────────────────

class TestSimilarityAndCost:
    def test_identical_stimuli_similarity_one(self) -> None:
        s = [1.0, 2.0, 3.0]
        assert FormalModel.similarity(s, s) == pytest.approx(1.0)

    def test_orthogonal_stimuli_similarity_zero(self) -> None:
        s1 = [1.0, 0.0]
        s2 = [0.0, 1.0]
        assert FormalModel.similarity(s1, s2) == pytest.approx(0.0)

    def test_opposite_stimuli_similarity_negative(self) -> None:
        s1 = [1.0, 0.0]
        s2 = [-1.0, 0.0]
        assert FormalModel.similarity(s1, s2) == pytest.approx(-1.0)

    def test_zero_vector_similarity(self) -> None:
        assert FormalModel.similarity([0.0, 0.0], [1.0, 2.0]) == 0.0

    def test_cost_invariant_holds(self, model: FormalModel) -> None:
        """INV-FM-01: C_r ≤ C_a when sim(s, s') > θ."""
        # reactivation_base_cost (3.0) < assembly_base_cost (10.0)
        assert model.check_cost_invariant([1.0, 2.0, 3.0],
                                          [1.0, 2.0, 3.0]) is True

    def test_cost_invariant_trivially_true_below_threshold(self) -> None:
        """When sim < θ, invariant is trivially satisfied."""
        m = FormalModel(theta=0.99)
        assert m.check_cost_invariant([1.0, 0.0], [0.0, 1.0]) is True


# ──────────────────────────────────────────────────────────────────────────────
# Full Lifecycle Integration
# ──────────────────────────────────────────────────────────────────────────────

class TestFullLifecycle:
    def test_assemble_decay_reactivate_decay(self) -> None:
        """Complete lifecycle: LATENT → ACTIVE → DECAYING → RESIDUAL → REACTIVATED → DECAYING → RESIDUAL."""
        model = FormalModel(theta=0.5, decay_rate=0.3)
        structure = SimplicialStructure(
            label="lifecycle-K",
            simplices=[frozenset({0, 1})],
        )
        stimulus = [3.0, 4.0]
        seed = [1.0, 1.0]

        # Assembly
        iface = model.assemble(stimulus, seed, structure)
        assert iface.state == LifecycleState.ACTIVE

        # Decay
        trace = model.decay(iface)
        assert iface.state == LifecycleState.RESIDUAL
        assert trace.dimension == len(seed)

        # Reactivation with similar stimulus
        new_stimulus = [3.5, 4.5]
        reactivated = model.reactivate(new_stimulus, trace)
        assert reactivated.state == LifecycleState.REACTIVATED

        # Second decay
        trace2 = model.decay(reactivated)
        assert reactivated.state == LifecycleState.RESIDUAL
        assert trace2.dimension == len(seed)

        # Costs accumulated
        assert model.costs.assembly_total == 10.0
        assert model.costs.decay_total > 0
        assert model.costs.reactivation_total == 3.0

    def test_decay_rate_validation(self) -> None:
        with pytest.raises(ValueError, match="decay_rate"):
            FormalModel(decay_rate=0.0)
        with pytest.raises(ValueError, match="decay_rate"):
            FormalModel(decay_rate=1.0)
        with pytest.raises(ValueError, match="decay_rate"):
            FormalModel(decay_rate=1.5)


# ──────────────────────────────────────────────────────────────────────────────
# CostLedger
# ──────────────────────────────────────────────────────────────────────────────

class TestCostLedger:
    def test_initial_zero(self) -> None:
        ledger = CostLedger()
        assert ledger.assembly_total == 0.0
        assert ledger.decay_total == 0.0
        assert ledger.reactivation_total == 0.0

    def test_accumulation(self) -> None:
        ledger = CostLedger()
        ledger.record_assembly(5.0)
        ledger.record_assembly(5.0)
        ledger.record_decay(2.0)
        ledger.record_reactivation(1.5)
        assert ledger.assembly_total == 10.0
        assert ledger.decay_total == 2.0
        assert ledger.reactivation_total == 1.5
