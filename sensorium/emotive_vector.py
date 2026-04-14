"""
sensorium.emotive_vector — Emotive Vector (Definition 35)
==========================================================

Implements AEROSPACEMODEL-MCC-SPEC-008 §2: a six-dimensional emotive
vector in SENSORIUM space with scalar properties and steganographic
capacity metrics.

Each emotion is defined as a vector of sensory intensities:

    ε = (κ_𝔸, κ_ℍ, κ_𝕆, κ_𝔽, κ_𝔾, κ_ℙ)    κᵢ ∈ {0, …, 99}
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NUM_CHANNELS = 6
"""Number of sensory channels in SENSORIUM space."""

INTENSITY_MIN = 0
"""Minimum intensity value per channel."""

INTENSITY_MAX = 99
"""Maximum intensity value per channel."""

MAX_TOTAL_CAPACITY = NUM_CHANNELS * INTENSITY_MAX  # 594
"""Maximum total steganographic capacity (all channels at 0)."""


# ---------------------------------------------------------------------------
# Channel enum
# ---------------------------------------------------------------------------

class SensoryChannel(Enum):
    """The six SENSORIUM sensory channels, ordered per axis convention."""

    AUDITORY = "𝔸"
    HAPTIC = "ℍ"
    OPTIC = "𝕆"
    OLFACTORY = "𝔽"
    GUSTATORY = "𝔾"
    PROPRIOCEPTIVE = "ℙ"


# Canonical ordering used in vectors
CHANNEL_ORDER: Tuple[SensoryChannel, ...] = (
    SensoryChannel.AUDITORY,
    SensoryChannel.HAPTIC,
    SensoryChannel.OPTIC,
    SensoryChannel.OLFACTORY,
    SensoryChannel.GUSTATORY,
    SensoryChannel.PROPRIOCEPTIVE,
)


# ---------------------------------------------------------------------------
# EmotiveVector dataclass
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class EmotiveVector:
    """Definition 35 — Emotive Vector.

    An emotive expression is a vector of sensory intensities in
    six-dimensional SENSORIUM space.  The radar polygon of *ε* **is**
    the geometric signature of the emotion.

    Parameters
    ----------
    auditory : int
        κ_𝔸 — Auditory channel intensity (0–99).
    haptic : int
        κ_ℍ — Haptic channel intensity (0–99).
    optic : int
        κ_𝕆 — Optic channel intensity (0–99).
    olfactory : int
        κ_𝔽 — Olfactory channel intensity (0–99).
    gustatory : int
        κ_𝔾 — Gustatory channel intensity (0–99).
    proprioceptive : int
        κ_ℙ — Proprioceptive channel intensity (0–99).
    """

    auditory: int
    haptic: int
    optic: int
    olfactory: int
    gustatory: int
    proprioceptive: int

    def __post_init__(self) -> None:
        for name, val in self._as_pairs():
            if not isinstance(val, int):
                raise TypeError(
                    f"{name} must be int, got {type(val).__name__}"
                )
            if val < INTENSITY_MIN or val > INTENSITY_MAX:
                raise ValueError(
                    f"{name}={val} outside domain [{INTENSITY_MIN}, {INTENSITY_MAX}]"
                )

    # -- helpers ------------------------------------------------------------

    def _as_pairs(self) -> List[Tuple[str, int]]:
        """Return ``[(channel_name, κᵢ), …]`` in canonical order."""
        return [
            ("auditory", self.auditory),
            ("haptic", self.haptic),
            ("optic", self.optic),
            ("olfactory", self.olfactory),
            ("gustatory", self.gustatory),
            ("proprioceptive", self.proprioceptive),
        ]

    def as_tuple(self) -> Tuple[int, ...]:
        """Return ``(κ_𝔸, κ_ℍ, κ_𝕆, κ_𝔽, κ_𝔾, κ_ℙ)``."""
        return (
            self.auditory,
            self.haptic,
            self.optic,
            self.olfactory,
            self.gustatory,
            self.proprioceptive,
        )

    def as_dict(self) -> Dict[SensoryChannel, int]:
        """Return a mapping ``{SensoryChannel: κᵢ}``."""
        return dict(zip(CHANNEL_ORDER, self.as_tuple()))

    # -- scalar properties (§2.1) ------------------------------------------

    @property
    def magnitude(self) -> float:
        """‖ε‖ = √(Σ κᵢ²)  — total sensory intensity / arousal level."""
        return math.sqrt(sum(k * k for k in self.as_tuple()))

    @property
    def dominant_sense(self) -> SensoryChannel:
        """argmax(κᵢ) — the channel that leads the experience.

        Ties are broken by canonical channel order (auditory first).
        """
        vals = self.as_tuple()
        max_val = max(vals)
        idx = vals.index(max_val)
        return CHANNEL_ORDER[idx]

    @property
    def centroid(self) -> float:
        """μ = (Σ κᵢ) / 6  — mean activation / emotional breadth."""
        return sum(self.as_tuple()) / NUM_CHANNELS

    @property
    def entropy(self) -> float:
        """H(ε) = −Σ p̂ᵢ log p̂ᵢ  where p̂ᵢ = κᵢ / Σκ.

        Uses natural logarithm.  Returns 0.0 when total intensity is zero.
        """
        total = sum(self.as_tuple())
        if total == 0:
            return 0.0
        h = 0.0
        for k in self.as_tuple():
            if k > 0:
                p = k / total
                h -= p * math.log(p)
        return h

    # -- steganographic capacity (§2.2) ------------------------------------

    def capacity_per_channel(self) -> Dict[SensoryChannel, int]:
        """C_i(ε) = 99 − κᵢ  — residual headroom per channel."""
        return {
            ch: INTENSITY_MAX - k
            for ch, k in zip(CHANNEL_ORDER, self.as_tuple())
        }

    @property
    def total_capacity(self) -> int:
        """C_total(ε) = 594 − Σ κᵢ  — total steganographic headroom."""
        return MAX_TOTAL_CAPACITY - sum(self.as_tuple())


# ---------------------------------------------------------------------------
# §3  Canonical Emotion Catalogue
# ---------------------------------------------------------------------------

GIOIA = EmotiveVector(
    auditory=85, haptic=60, optic=90,
    olfactory=45, gustatory=70, proprioceptive=80,
)
"""SENSO-EMO-001 — Gioia (Joy). ‖ε‖ ≈ 180, dominant: Optic."""

SERENITA = EmotiveVector(
    auditory=50, haptic=45, optic=55,
    olfactory=40, gustatory=38, proprioceptive=48,
)
"""SENSO-EMO-002 — Serenità (Serenity). ‖ε‖ ≈ 114, dominant: Optic."""

MALINCONIA = EmotiveVector(
    auditory=30, haptic=20, optic=55,
    olfactory=25, gustatory=15, proprioceptive=30,
)
"""SENSO-EMO-003 — Malinconia (Melancholy). ‖ε‖ ≈ 78, dominant: Optic."""

TERRORE = EmotiveVector(
    auditory=90, haptic=95, optic=70,
    olfactory=5, gustatory=5, proprioceptive=92,
)
"""SENSO-EMO-004 — Terrore (Terror). ‖ε‖ ≈ 175, dominant: Haptic."""

MERAVIGLIA = EmotiveVector(
    auditory=55, haptic=35, optic=78,
    olfactory=25, gustatory=20, proprioceptive=68,
)
"""SENSO-EMO-005 — Meraviglia (Wonder). ‖ε‖ ≈ 126, dominant: Optic."""

TENEREZZA = EmotiveVector(
    auditory=40, haptic=85, optic=40,
    olfactory=32, gustatory=30, proprioceptive=60,
)
"""SENSO-EMO-006 — Tenerezza (Tenderness). ‖ε‖ ≈ 126, dominant: Haptic."""

ESTASI = EmotiveVector(
    auditory=80, haptic=82, optic=85,
    olfactory=75, gustatory=78, proprioceptive=80,
)
"""SENSO-EMO-007 — Estasi (Ecstasy). ‖ε‖ ≈ 196, dominant: Optic."""

NOSTALGIA = EmotiveVector(
    auditory=40, haptic=30, optic=40,
    olfactory=80, gustatory=60, proprioceptive=20,
)
"""SENSO-EMO-008 — Nostalgia (Nostalgia). ‖ε‖ ≈ 120, dominant: Olfactory."""

CANONICAL_EMOTIONS: Tuple[EmotiveVector, ...] = (
    GIOIA,
    SERENITA,
    MALINCONIA,
    TERRORE,
    MERAVIGLIA,
    TENEREZZA,
    ESTASI,
    NOSTALGIA,
)
"""All eight canonical emotions in catalogue order."""
