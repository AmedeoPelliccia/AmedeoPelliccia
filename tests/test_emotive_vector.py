"""
tests/test_emotive_vector.py — Emotive Vector (Definition 35) Validation
=========================================================================

Validates the EmotiveVector implementation against
AEROSPACEMODEL-MCC-SPEC-008 §2–§3.

Run with:  python -m pytest tests/test_emotive_vector.py -v
"""

from __future__ import annotations

import math

import pytest

from sensorium.emotive_vector import (
    CANONICAL_EMOTIONS,
    ESTASI,
    GIOIA,
    INTENSITY_MAX,
    INTENSITY_MIN,
    MALINCONIA,
    MAX_TOTAL_CAPACITY,
    MERAVIGLIA,
    NOSTALGIA,
    NUM_CHANNELS,
    SERENITA,
    TENEREZZA,
    TERRORE,
    EmotiveVector,
    SensoryChannel,
)


# ──────────────────────────────────────────────────────────────────────────────
# Domain validation (κᵢ ∈ {0, …, 99})
# ──────────────────────────────────────────────────────────────────────────────


class TestDomainValidation:
    """Ensure the intensity domain is enforced."""

    def test_minimum_boundary(self) -> None:
        v = EmotiveVector(0, 0, 0, 0, 0, 0)
        assert v.as_tuple() == (0, 0, 0, 0, 0, 0)

    def test_maximum_boundary(self) -> None:
        v = EmotiveVector(99, 99, 99, 99, 99, 99)
        assert v.as_tuple() == (99, 99, 99, 99, 99, 99)

    def test_below_minimum_raises(self) -> None:
        with pytest.raises(ValueError, match="outside domain"):
            EmotiveVector(-1, 0, 0, 0, 0, 0)

    def test_above_maximum_raises(self) -> None:
        with pytest.raises(ValueError, match="outside domain"):
            EmotiveVector(0, 0, 100, 0, 0, 0)

    def test_non_integer_raises(self) -> None:
        with pytest.raises(TypeError, match="must be int"):
            EmotiveVector(10.5, 0, 0, 0, 0, 0)  # type: ignore[arg-type]

    def test_each_channel_validated(self) -> None:
        """Every channel position rejects out-of-range values."""
        for i in range(NUM_CHANNELS):
            args = [50] * NUM_CHANNELS
            args[i] = 100
            with pytest.raises(ValueError):
                EmotiveVector(*args)


# ──────────────────────────────────────────────────────────────────────────────
# Scalar properties (§2.1)
# ──────────────────────────────────────────────────────────────────────────────


class TestMagnitude:
    """‖ε‖ = √(Σ κᵢ²)"""

    def test_zero_vector(self) -> None:
        v = EmotiveVector(0, 0, 0, 0, 0, 0)
        assert v.magnitude == 0.0

    def test_single_channel(self) -> None:
        v = EmotiveVector(99, 0, 0, 0, 0, 0)
        assert v.magnitude == pytest.approx(99.0)

    @pytest.mark.parametrize(
        "emotion,expected",
        [
            (GIOIA, 180),
            (SERENITA, 114),
            (MALINCONIA, 78),
            (TERRORE, 175),
            (MERAVIGLIA, 126),
            (TENEREZZA, 126),
            (ESTASI, 196),
            (NOSTALGIA, 120),
        ],
        ids=[
            "Gioia",
            "Serenità",
            "Malinconia",
            "Terrore",
            "Meraviglia",
            "Tenerezza",
            "Estasi",
            "Nostalgia",
        ],
    )
    def test_canonical_magnitudes(
        self, emotion: EmotiveVector, expected: int
    ) -> None:
        """Validate magnitudes from §3 Canonical Emotion Catalogue."""
        assert round(emotion.magnitude) == expected


class TestDominantSense:
    """argmax(κᵢ) — dominant channel."""

    def test_gioia_dominant_optic(self) -> None:
        assert GIOIA.dominant_sense == SensoryChannel.OPTIC

    def test_terrore_dominant_haptic(self) -> None:
        assert TERRORE.dominant_sense == SensoryChannel.HAPTIC

    def test_nostalgia_dominant_olfactory(self) -> None:
        assert NOSTALGIA.dominant_sense == SensoryChannel.OLFACTORY

    def test_tenerezza_dominant_haptic(self) -> None:
        assert TENEREZZA.dominant_sense == SensoryChannel.HAPTIC

    def test_estasi_dominant_optic(self) -> None:
        assert ESTASI.dominant_sense == SensoryChannel.OPTIC

    def test_tie_breaks_by_order(self) -> None:
        """When two channels tie, the first in canonical order wins."""
        v = EmotiveVector(50, 50, 0, 0, 0, 0)
        assert v.dominant_sense == SensoryChannel.AUDITORY


class TestCentroid:
    """μ = (Σ κᵢ) / 6"""

    def test_uniform_vector(self) -> None:
        v = EmotiveVector(30, 30, 30, 30, 30, 30)
        assert v.centroid == pytest.approx(30.0)

    def test_zero_vector(self) -> None:
        v = EmotiveVector(0, 0, 0, 0, 0, 0)
        assert v.centroid == pytest.approx(0.0)

    def test_gioia(self) -> None:
        expected = (85 + 60 + 90 + 45 + 70 + 80) / 6
        assert GIOIA.centroid == pytest.approx(expected)


class TestEntropy:
    """H(ε) = −Σ p̂ᵢ log p̂ᵢ"""

    def test_zero_vector_entropy_zero(self) -> None:
        v = EmotiveVector(0, 0, 0, 0, 0, 0)
        assert v.entropy == 0.0

    def test_uniform_maximum_entropy(self) -> None:
        """All channels equal → maximum entropy = ln(6)."""
        v = EmotiveVector(50, 50, 50, 50, 50, 50)
        assert v.entropy == pytest.approx(math.log(6))

    def test_single_channel_zero_entropy(self) -> None:
        """Only one channel active → zero entropy."""
        v = EmotiveVector(99, 0, 0, 0, 0, 0)
        assert v.entropy == pytest.approx(0.0)

    def test_estasi_higher_than_nostalgia(self) -> None:
        """Estasi is more uniform, so entropy should be higher."""
        assert ESTASI.entropy > NOSTALGIA.entropy


# ──────────────────────────────────────────────────────────────────────────────
# Steganographic capacity (§2.2)
# ──────────────────────────────────────────────────────────────────────────────


class TestSteganographicCapacity:
    """C_i(ε) = 99 − κᵢ  and  C_total(ε) = 594 − Σ κᵢ"""

    def test_per_channel_zero_vector(self) -> None:
        v = EmotiveVector(0, 0, 0, 0, 0, 0)
        caps = v.capacity_per_channel()
        assert all(c == INTENSITY_MAX for c in caps.values())

    def test_per_channel_max_vector(self) -> None:
        v = EmotiveVector(99, 99, 99, 99, 99, 99)
        caps = v.capacity_per_channel()
        assert all(c == 0 for c in caps.values())

    def test_total_zero_vector(self) -> None:
        v = EmotiveVector(0, 0, 0, 0, 0, 0)
        assert v.total_capacity == MAX_TOTAL_CAPACITY

    def test_total_max_vector(self) -> None:
        v = EmotiveVector(99, 99, 99, 99, 99, 99)
        assert v.total_capacity == 0

    def test_total_equals_sum_per_channel(self) -> None:
        caps = GIOIA.capacity_per_channel()
        assert GIOIA.total_capacity == sum(caps.values())

    def test_estasi_minimum_capacity(self) -> None:
        """Estasi has the lowest total capacity among canonical emotions."""
        estasi_cap = ESTASI.total_capacity
        for emotion in CANONICAL_EMOTIONS:
            assert emotion.total_capacity >= estasi_cap

    def test_malinconia_maximum_capacity(self) -> None:
        """Malinconia has the highest total capacity among canonical emotions."""
        malinconia_cap = MALINCONIA.total_capacity
        for emotion in CANONICAL_EMOTIONS:
            assert emotion.total_capacity <= malinconia_cap

    def test_terrore_chemical_channels(self) -> None:
        """Terrore has near-zero chemical channels → high chemical capacity."""
        caps = TERRORE.capacity_per_channel()
        assert caps[SensoryChannel.OLFACTORY] == 94
        assert caps[SensoryChannel.GUSTATORY] == 94


# ──────────────────────────────────────────────────────────────────────────────
# Canonical Emotion Catalogue (§3)
# ──────────────────────────────────────────────────────────────────────────────


class TestCanonicalCatalogue:
    """Validate the eight canonical emotions are correctly defined."""

    def test_catalogue_length(self) -> None:
        assert len(CANONICAL_EMOTIONS) == 8

    def test_gioia_vector(self) -> None:
        assert GIOIA.as_tuple() == (85, 60, 90, 45, 70, 80)

    def test_serenita_vector(self) -> None:
        assert SERENITA.as_tuple() == (50, 45, 55, 40, 38, 48)

    def test_malinconia_vector(self) -> None:
        assert MALINCONIA.as_tuple() == (30, 20, 55, 25, 15, 30)

    def test_terrore_vector(self) -> None:
        assert TERRORE.as_tuple() == (90, 95, 70, 5, 5, 92)

    def test_meraviglia_vector(self) -> None:
        assert MERAVIGLIA.as_tuple() == (55, 35, 78, 25, 20, 68)

    def test_tenerezza_vector(self) -> None:
        assert TENEREZZA.as_tuple() == (40, 85, 40, 32, 30, 60)

    def test_estasi_vector(self) -> None:
        assert ESTASI.as_tuple() == (80, 82, 85, 75, 78, 80)

    def test_nostalgia_vector(self) -> None:
        assert NOSTALGIA.as_tuple() == (40, 30, 40, 80, 60, 20)


# ──────────────────────────────────────────────────────────────────────────────
# Immutability
# ──────────────────────────────────────────────────────────────────────────────


class TestImmutability:
    """EmotiveVector is frozen — mutation raises."""

    def test_frozen(self) -> None:
        with pytest.raises(AttributeError):
            GIOIA.auditory = 0  # type: ignore[misc]


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────


class TestHelpers:
    """as_tuple / as_dict round-trip."""

    def test_as_dict_keys(self) -> None:
        d = GIOIA.as_dict()
        assert set(d.keys()) == set(SensoryChannel)

    def test_as_dict_values_match_tuple(self) -> None:
        d = GIOIA.as_dict()
        from sensorium.emotive_vector import CHANNEL_ORDER

        reconstructed = tuple(d[ch] for ch in CHANNEL_ORDER)
        assert reconstructed == GIOIA.as_tuple()
