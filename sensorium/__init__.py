"""
SENSORIUM — Multi-Sensory Cryptographic Composition
=====================================================

Python implementation of AEROSPACEMODEL-MCC-SPEC-008.

Provides the :class:`EmotiveVector` (Definition 35) and the eight
canonical emotions that define the primary SENSORIUM colour space.
"""

from sensorium.emotive_vector import (
    CANONICAL_EMOTIONS,
    CHANNEL_ORDER,
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

__all__ = [
    "EmotiveVector",
    "SensoryChannel",
    "CHANNEL_ORDER",
    "NUM_CHANNELS",
    "INTENSITY_MIN",
    "INTENSITY_MAX",
    "MAX_TOTAL_CAPACITY",
    "GIOIA",
    "SERENITA",
    "MALINCONIA",
    "TERRORE",
    "MERAVIGLIA",
    "TENEREZZA",
    "ESTASI",
    "NOSTALGIA",
    "CANONICAL_EMOTIONS",
]
