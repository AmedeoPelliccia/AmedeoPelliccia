"""
AMPEL360 — Aerospace Methods for Programming Engineering Lifecycle (360°)
=========================================================================

Deterministic lifecycle programming architecture that governs aerospace
systems from mission intent to end-of-life material recovery.

Document ID: AMPEL360-ARCH-SPEC-v2.0
Parent:      ESSA-DOC-AMPEL360-001
"""

from ampel360.resolver import (
    OperationalEnvironment,
    FunctionalMission,
    PayloadClassification,
    HumanPresence,
    OperationalContext,
    AMPEL360Profile,
    resolve_profile,
)

__all__ = [
    "OperationalEnvironment",
    "FunctionalMission",
    "PayloadClassification",
    "HumanPresence",
    "OperationalContext",
    "AMPEL360Profile",
    "resolve_profile",
]
