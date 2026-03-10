"""
AMPEL360 — Aerospace Model for Product and Engineering Lifecycles (360°)
=========================================================================

An end-to-end aerospace lifecycle architecture that governs the design,
engineering, certification, operation, and continuous digital
traceability of aircraft systems and programmes.

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
