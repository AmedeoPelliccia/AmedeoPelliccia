"""
ampel360.resolver — Deterministic Profile Resolver
===================================================

Implements the three-axis profile constructor and deterministic resolution
logic described in AMPEL360-ARCH-SPEC-v2.0 §9 and §11.

Axis resolution order (structural):
  1. Environment  (AIR | SPACE)
  2. Function     (PAX_TRANSPORT | CARGO_ONLY)
  3. Payload      (CIVIL_PUBLIC | COMMERCIAL_SENSITIVE | EXPORT_CONTROLLED | DEFENSE_CLASSIFIED)
  4. Regulatory overlay (named)

Merge strategy: most-restrictive-wins on all safety and security gates.

Coding conventions: stdlib only; dataclasses, Enum, type hints.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional, Set


# ──────────────────────────────────────────────────────────────────────────────
# 1. CORE ENUMERATIONS  (§11.1)
# ──────────────────────────────────────────────────────────────────────────────

class OperationalEnvironment(Enum):
    """Axis A — Operational Environment."""
    AIR = "AIR"
    SPACE = "SPACE"


class FunctionalMission(Enum):
    """Axis B — Functional Mission."""
    PAX_TRANSPORT = "PAX_TRANSPORT"
    CARGO_ONLY = "CARGO_ONLY"


class PayloadClassification(Enum):
    """Axis C — Payload Classification."""
    CIVIL_PUBLIC = "CIVIL_PUBLIC"
    COMMERCIAL_SENSITIVE = "COMMERCIAL_SENSITIVE"
    EXPORT_CONTROLLED = "EXPORT_CONTROLLED"
    DEFENSE_CLASSIFIED = "DEFENSE_CLASSIFIED"


class HumanPresence(Enum):
    """AMPEL360-SPLIT — Human Presence Safety Ontology (§7)."""
    HOB = "HUMAN_ON_BOARD"
    NHOB = "NO_HUMAN_ON_BOARD"


class OperationalContext(Enum):
    """Civil vs Defence operational context (§8)."""
    CIVIL = "CIVIL"
    DEFENSE = "DEFENSE"


# Disclosure modes ordered from least to most restrictive.
_DISCLOSURE_ORDER = ["FULL", "REDACTED", "ATTESTATION_ONLY"]

# DAL levels ordered from least to most restrictive (E < D < C < B < A).
_DAL_ORDER = ["E", "D", "C", "B", "A"]


# ──────────────────────────────────────────────────────────────────────────────
# 2. PROFILE OBJECT  (§11.2)
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class AMPEL360Profile:
    """Complete resolved profile produced by :func:`resolve_profile`."""

    profile_id: str = ""
    environment: Optional[OperationalEnvironment] = None
    function: Optional[FunctionalMission] = None
    payload_class: Optional[PayloadClassification] = None
    human_presence: Optional[HumanPresence] = None
    operational_context: OperationalContext = OperationalContext.CIVIL
    regulatory_overlay: str = ""
    templates: Set[str] = field(default_factory=set)
    rulesets: Set[str] = field(default_factory=set)
    constraints: Dict[str, Any] = field(default_factory=dict)
    disclosure_mode: str = "FULL"


# ──────────────────────────────────────────────────────────────────────────────
# 3. CONSTRAINT MERGE HELPERS  (§11.4)
# ──────────────────────────────────────────────────────────────────────────────

def _most_restrictive_disclosure(a: str, b: str) -> str:
    """Return the more restrictive of two disclosure modes."""
    idx_a = _DISCLOSURE_ORDER.index(a) if a in _DISCLOSURE_ORDER else 0
    idx_b = _DISCLOSURE_ORDER.index(b) if b in _DISCLOSURE_ORDER else 0
    return _DISCLOSURE_ORDER[max(idx_a, idx_b)]


def _max_dal(a: str, b: str) -> str:
    """Return the higher (stricter) of two DAL levels."""
    idx_a = _DAL_ORDER.index(a) if a in _DAL_ORDER else 0
    idx_b = _DAL_ORDER.index(b) if b in _DAL_ORDER else 0
    return _DAL_ORDER[max(idx_a, idx_b)]


def _merge_constraint(key: str, existing: Any, incoming: Any) -> Any:
    """
    Merge a single constraint value according to the most-restrictive-wins
    strategy (§11.4).
    """
    if key == "risk_threshold":
        return min(existing, incoming)
    if key == "dal_level":
        return _max_dal(str(existing), str(incoming))
    if key in ("require_authority", "human_override"):
        return existing or incoming
    if key == "disclosure_mode":
        return _most_restrictive_disclosure(str(existing), str(incoming))
    if key == "query_relaxation":
        return existing and incoming
    # Default: prefer incoming (last-writer-wins for unknown keys)
    return incoming


def _merge_constraints(
    target: Dict[str, Any],
    source: Dict[str, Any],
) -> None:
    """Merge *source* constraints into *target* in place."""
    for key, value in source.items():
        if key in target:
            target[key] = _merge_constraint(key, target[key], value)
        else:
            target[key] = value


# ──────────────────────────────────────────────────────────────────────────────
# 4. AXIS PACK LOADERS  (§9.6)
# ──────────────────────────────────────────────────────────────────────────────

def _load_base_kernel() -> AMPEL360Profile:
    """Step 1 — Load the base kernel (common to all profiles)."""
    return AMPEL360Profile(
        templates={
            "H_PIPELINE_GATE_CHECK",
            "SECURITY_INTEGRITY_CHECK",
            "INTERPRET_CONFIRM_ACTIVATE_PUBLISH_SM",
        },
        rulesets={
            "SAFETY_ENVELOPE_VALID",
            "TOKEN_GRAPH_COMPLETE",
            "AUTHORITY_SIGNOFF_PRESENT",
        },
        constraints={
            "risk_threshold": 1e-7,
            "require_authority": True,
            "human_override": False,
            "query_relaxation": True,
            "disclosure_mode": "FULL",
        },
    )


def _apply_env_pack(profile: AMPEL360Profile, env: OperationalEnvironment) -> None:
    """Apply environment axis pack (§9.6 ENV effects)."""
    if env == OperationalEnvironment.AIR:
        profile.templates |= {
            "ICA_PRESENCE_GATE",
            "EFFECTIVITY_COMPLETENESS_CHECK",
            "OPERATOR_TRANSFER_TEMPORAL_MODEL",
        }
        profile.rulesets |= {
            "ICA_PRESENCE_RULE",
            "MSN_TAIL_APPLICABILITY_RULE",
            "LEASING_STATE_MACHINE_RULE",
        }
        _merge_constraints(profile.constraints, {
            "risk_threshold": 1e-9,
        })
    else:  # SPACE
        profile.templates |= {
            "CONJUNCTION_EVIDENCE_LOOP",
            "ORBIT_REGIME_APPLICABILITY",
            "REENTRY_SAFETY_CONSTRAINT",
        }
        profile.rulesets |= {
            "CONJUNCTION_EVIDENCE_RULE",
            "ORBIT_REGIME_RULE",
            "REENTRY_SAFETY_RULE",
        }
        _merge_constraints(profile.constraints, {
            "risk_threshold": 1e-4,
        })


def _apply_func_pack(profile: AMPEL360Profile, func: FunctionalMission) -> None:
    """Apply function axis pack (§9.6 FUNC effects)."""
    if func == FunctionalMission.PAX_TRANSPORT:
        profile.templates |= {
            "SURVIVABILITY_REQUIREMENT",
            "HUMAN_OVERRIDE_REQUIREMENT",
            "CABIN_SAFETY_TEMPLATE",
        }
        profile.rulesets |= {
            "PUBLISH_GATE_SAFETY_REPORT_REQUIRED",
            "EVACUATION_COMPLIANCE_RULE",
            "HUMAN_FACTORS_RULE",
        }
        _merge_constraints(profile.constraints, {
            "human_override": True,
            "dal_level": "A",
        })
    else:  # CARGO_ONLY
        profile.templates |= {
            "THIRD_PARTY_HARM_ENVELOPE",
            "CARGO_HAZARD_CLASSIFICATION",
            "DANGEROUS_GOODS_TEMPLATE",
        }
        profile.rulesets |= {
            "GROUND_RISK_CONTAINMENT_RULE",
            "CARGO_FIRE_SUPPRESSION_RULE",
            "PAYLOAD_RESTRAINT_RULE",
        }
        _merge_constraints(profile.constraints, {
            "human_override": False,
        })


def _apply_payload_pack(
    profile: AMPEL360Profile,
    payload: PayloadClassification,
) -> None:
    """Apply payload classification axis pack (§9.6 PAYLOAD effects)."""
    if payload == PayloadClassification.CIVIL_PUBLIC:
        _merge_constraints(profile.constraints, {
            "disclosure_mode": "FULL",
            "query_relaxation": True,
        })
    elif payload == PayloadClassification.COMMERCIAL_SENSITIVE:
        _merge_constraints(profile.constraints, {
            "disclosure_mode": "REDACTED",
            "query_relaxation": True,
        })
    elif payload == PayloadClassification.EXPORT_CONTROLLED:
        _merge_constraints(profile.constraints, {
            "disclosure_mode": "REDACTED",
            "query_relaxation": False,
        })
    elif payload == PayloadClassification.DEFENSE_CLASSIFIED:
        profile.rulesets |= {
            "FEDERATED_SEARCH_PUSHDOWN_RULE",
            "PROVENANCE_WATERMARKING_RULE",
        }
        _merge_constraints(profile.constraints, {
            "disclosure_mode": "ATTESTATION_ONLY",
            "query_relaxation": False,
        })


def _apply_defense_extension(profile: AMPEL360Profile) -> None:
    """Apply defence profile extension (§8)."""
    profile.templates |= {
        "ROE_ENGAGEMENT_CONSTRAINTS",
        "CIVILIAN_PROTECTION_INVARIANTS",
        "POST_EVENT_AUDITABILITY",
        "CLASSIFICATION_OVERLAY",
    }
    profile.rulesets |= {
        "ENGAGEMENT_AUTHORIZED_ENVELOPE_RULE",
        "CIVILIAN_PROTECTION_CONSTRAINT_RULE",
        "IMMUTABLE_DECISION_LOG_RULE",
    }


def _apply_regulatory_overlay(profile: AMPEL360Profile, overlay: str) -> None:
    """Apply a named regulatory overlay (§9.5 step 3)."""
    overlay_upper = overlay.upper()

    if "EASA" in overlay_upper or "Q100" in overlay_upper:
        profile.templates.add("EASA_CS25_COMPLIANCE_TEMPLATE")
        profile.rulesets.add("DO_178C_DAL_A_RULESET")
        _merge_constraints(profile.constraints, {
            "risk_threshold": 1e-9,
            "dal_level": "A",
            "require_authority": True,
        })

    if "SPACE" in overlay_upper or "Q10" in overlay_upper:
        profile.templates.add("ECSS_COMPLIANCE_TEMPLATE")
        profile.rulesets.add("ECSS_Q_ST_40C_RULESET")
        _merge_constraints(profile.constraints, {
            "risk_threshold": 1e-4,
        })

    if "DO-178C" in overlay_upper or "DO_178C" in overlay_upper:
        profile.rulesets.add("DO_178C_ARTEFACT_RULESET")

    if "DEF" in overlay_upper:
        _apply_defense_extension(profile)


# ──────────────────────────────────────────────────────────────────────────────
# 5. PROFILE RESOLVER  (§11.3)
# ──────────────────────────────────────────────────────────────────────────────

def resolve_profile(
    env: OperationalEnvironment,
    func: FunctionalMission,
    payload: PayloadClassification,
    overlay: str,
    context: OperationalContext = OperationalContext.CIVIL,
) -> AMPEL360Profile:
    """
    Deterministic profile resolution.

    Applies axis packs in order: ENV → FUNC → PAYLOAD → OVERLAY.
    Merge strategy: union templates, union rulesets, strictest constraint wins.

    Parameters
    ----------
    env : OperationalEnvironment
        Axis A — AIR or SPACE.
    func : FunctionalMission
        Axis B — PAX_TRANSPORT or CARGO_ONLY.
    payload : PayloadClassification
        Axis C — security/disclosure tier.
    overlay : str
        Named regulatory overlay (e.g. "EASA-Q100", "SPACE-Q10").
    context : OperationalContext
        Civil or Defence operational context (default: CIVIL).

    Returns
    -------
    AMPEL360Profile
        Fully resolved profile with merged templates, rulesets, and
        constraints.
    """
    profile = _load_base_kernel()

    # Step 2 — Apply axis packs in structural order
    profile.environment = env
    _apply_env_pack(profile, env)

    profile.function = func
    _apply_func_pack(profile, func)

    profile.payload_class = payload
    _apply_payload_pack(profile, payload)

    # Derive human presence from function axis (§7)
    profile.human_presence = (
        HumanPresence.HOB
        if func == FunctionalMission.PAX_TRANSPORT
        else HumanPresence.NHOB
    )

    # Apply operational context (§8)
    profile.operational_context = context
    if context == OperationalContext.DEFENSE:
        _apply_defense_extension(profile)

    # Step 3 — Apply named regulatory overlay (most restrictive wins)
    profile.regulatory_overlay = overlay
    _apply_regulatory_overlay(profile, overlay)

    # Compute composite profile_id (§9.4)
    profile.profile_id = f"{env.value}.{func.value}.{payload.value}.{overlay}"

    # Sync top-level disclosure_mode from merged constraints
    profile.disclosure_mode = profile.constraints.get(
        "disclosure_mode", profile.disclosure_mode
    )

    return profile
