"""
tests/test_profile_resolution.py — Profile Resolution Validation
=================================================================

Validates the deterministic profile resolver described in
AMPEL360-ARCH-SPEC-v2.0 §9, §11.

Run with:  python -m pytest tests/test_profile_resolution.py -v
"""

from __future__ import annotations

import pytest

from ampel360.resolver import (
    AMPEL360Profile,
    FunctionalMission,
    HumanPresence,
    OperationalContext,
    OperationalEnvironment,
    PayloadClassification,
    resolve_profile,
    _max_dal,
    _most_restrictive_disclosure,
)


# ──────────────────────────────────────────────────────────────────────────────
# §9.7 Reference Profile — Q100 (Passenger Aircraft)
# ──────────────────────────────────────────────────────────────────────────────

class TestQ100Profile:
    """AIR.PAX_TRANSPORT.CIVIL_PUBLIC.EASA-Q100"""

    @pytest.fixture()
    def profile(self) -> AMPEL360Profile:
        return resolve_profile(
            env=OperationalEnvironment.AIR,
            func=FunctionalMission.PAX_TRANSPORT,
            payload=PayloadClassification.CIVIL_PUBLIC,
            overlay="EASA-Q100",
        )

    def test_profile_id(self, profile: AMPEL360Profile) -> None:
        assert profile.profile_id == "AIR.PAX_TRANSPORT.CIVIL_PUBLIC.EASA-Q100"

    def test_axes(self, profile: AMPEL360Profile) -> None:
        assert profile.environment == OperationalEnvironment.AIR
        assert profile.function == FunctionalMission.PAX_TRANSPORT
        assert profile.payload_class == PayloadClassification.CIVIL_PUBLIC

    def test_human_presence_derived(self, profile: AMPEL360Profile) -> None:
        assert profile.human_presence == HumanPresence.HOB

    def test_civil_context(self, profile: AMPEL360Profile) -> None:
        assert profile.operational_context == OperationalContext.CIVIL

    def test_disclosure_full(self, profile: AMPEL360Profile) -> None:
        assert profile.disclosure_mode == "FULL"

    def test_risk_threshold(self, profile: AMPEL360Profile) -> None:
        assert profile.constraints["risk_threshold"] <= 1e-9

    def test_dal_a(self, profile: AMPEL360Profile) -> None:
        assert profile.constraints["dal_level"] == "A"

    def test_human_override_required(self, profile: AMPEL360Profile) -> None:
        assert profile.constraints["human_override"] is True

    def test_query_relaxation_allowed(self, profile: AMPEL360Profile) -> None:
        assert profile.constraints["query_relaxation"] is True

    def test_air_templates_present(self, profile: AMPEL360Profile) -> None:
        assert "ICA_PRESENCE_GATE" in profile.templates
        assert "EFFECTIVITY_COMPLETENESS_CHECK" in profile.templates

    def test_pax_templates_present(self, profile: AMPEL360Profile) -> None:
        assert "CABIN_SAFETY_TEMPLATE" in profile.templates
        assert "SURVIVABILITY_REQUIREMENT" in profile.templates

    def test_easa_overlay_template(self, profile: AMPEL360Profile) -> None:
        assert "EASA_CS25_COMPLIANCE_TEMPLATE" in profile.templates

    def test_do178c_ruleset(self, profile: AMPEL360Profile) -> None:
        assert "DO_178C_DAL_A_RULESET" in profile.rulesets


# ──────────────────────────────────────────────────────────────────────────────
# §9.7 Reference Profile — Q10 (Uncrewed Spacecraft)
# ──────────────────────────────────────────────────────────────────────────────

class TestQ10Profile:
    """SPACE.CARGO_ONLY.COMMERCIAL_SENSITIVE.SPACE-Q10"""

    @pytest.fixture()
    def profile(self) -> AMPEL360Profile:
        return resolve_profile(
            env=OperationalEnvironment.SPACE,
            func=FunctionalMission.CARGO_ONLY,
            payload=PayloadClassification.COMMERCIAL_SENSITIVE,
            overlay="SPACE-Q10",
        )

    def test_profile_id(self, profile: AMPEL360Profile) -> None:
        assert profile.profile_id == "SPACE.CARGO_ONLY.COMMERCIAL_SENSITIVE.SPACE-Q10"

    def test_axes(self, profile: AMPEL360Profile) -> None:
        assert profile.environment == OperationalEnvironment.SPACE
        assert profile.function == FunctionalMission.CARGO_ONLY
        assert profile.payload_class == PayloadClassification.COMMERCIAL_SENSITIVE

    def test_nhob(self, profile: AMPEL360Profile) -> None:
        assert profile.human_presence == HumanPresence.NHOB

    def test_disclosure_redacted(self, profile: AMPEL360Profile) -> None:
        assert profile.disclosure_mode == "REDACTED"

    def test_space_templates(self, profile: AMPEL360Profile) -> None:
        assert "CONJUNCTION_EVIDENCE_LOOP" in profile.templates
        assert "ORBIT_REGIME_APPLICABILITY" in profile.templates

    def test_cargo_templates(self, profile: AMPEL360Profile) -> None:
        assert "THIRD_PARTY_HARM_ENVELOPE" in profile.templates
        assert "CARGO_HAZARD_CLASSIFICATION" in profile.templates

    def test_ecss_ruleset(self, profile: AMPEL360Profile) -> None:
        assert "ECSS_Q_ST_40C_RULESET" in profile.rulesets

    def test_human_override_not_required(self, profile: AMPEL360Profile) -> None:
        assert profile.constraints["human_override"] is False


# ──────────────────────────────────────────────────────────────────────────────
# §9.7 Reference Profile — Defense Payload in Space
# ──────────────────────────────────────────────────────────────────────────────

class TestDefenseSpaceProfile:
    """SPACE.CARGO_ONLY.DEFENSE_CLASSIFIED.SPACE-Q10-DEF"""

    @pytest.fixture()
    def profile(self) -> AMPEL360Profile:
        return resolve_profile(
            env=OperationalEnvironment.SPACE,
            func=FunctionalMission.CARGO_ONLY,
            payload=PayloadClassification.DEFENSE_CLASSIFIED,
            overlay="SPACE-Q10-DEF",
            context=OperationalContext.DEFENSE,
        )

    def test_profile_id(self, profile: AMPEL360Profile) -> None:
        assert profile.profile_id == "SPACE.CARGO_ONLY.DEFENSE_CLASSIFIED.SPACE-Q10-DEF"

    def test_defense_context(self, profile: AMPEL360Profile) -> None:
        assert profile.operational_context == OperationalContext.DEFENSE

    def test_attestation_only(self, profile: AMPEL360Profile) -> None:
        assert profile.disclosure_mode == "ATTESTATION_ONLY"

    def test_no_query_relaxation(self, profile: AMPEL360Profile) -> None:
        assert profile.constraints["query_relaxation"] is False

    def test_defense_templates(self, profile: AMPEL360Profile) -> None:
        assert "ROE_ENGAGEMENT_CONSTRAINTS" in profile.templates
        assert "CIVILIAN_PROTECTION_INVARIANTS" in profile.templates
        assert "POST_EVENT_AUDITABILITY" in profile.templates

    def test_defense_rulesets(self, profile: AMPEL360Profile) -> None:
        assert "ENGAGEMENT_AUTHORIZED_ENVELOPE_RULE" in profile.rulesets
        assert "CIVILIAN_PROTECTION_CONSTRAINT_RULE" in profile.rulesets

    def test_provenance_watermarking(self, profile: AMPEL360Profile) -> None:
        assert "PROVENANCE_WATERMARKING_RULE" in profile.rulesets


# ──────────────────────────────────────────────────────────────────────────────
# Constraint merge logic (§11.4)
# ──────────────────────────────────────────────────────────────────────────────

class TestConstraintMerge:
    """Validate most-restrictive-wins merge strategy."""

    def test_dal_level_a_wins(self) -> None:
        assert _max_dal("C", "A") == "A"
        assert _max_dal("A", "E") == "A"

    def test_dal_level_same(self) -> None:
        assert _max_dal("B", "B") == "B"

    def test_disclosure_attestation_wins(self) -> None:
        assert _most_restrictive_disclosure("FULL", "ATTESTATION_ONLY") == "ATTESTATION_ONLY"
        assert _most_restrictive_disclosure("REDACTED", "FULL") == "REDACTED"

    def test_disclosure_same(self) -> None:
        assert _most_restrictive_disclosure("FULL", "FULL") == "FULL"


# ──────────────────────────────────────────────────────────────────────────────
# Axis derivation invariants
# ──────────────────────────────────────────────────────────────────────────────

class TestAxisInvariants:
    """Validate that axis derivation follows spec invariants."""

    def test_pax_always_hob(self) -> None:
        for env in OperationalEnvironment:
            for payload in PayloadClassification:
                p = resolve_profile(env, FunctionalMission.PAX_TRANSPORT, payload, "TEST")
                assert p.human_presence == HumanPresence.HOB

    def test_cargo_always_nhob(self) -> None:
        for env in OperationalEnvironment:
            for payload in PayloadClassification:
                p = resolve_profile(env, FunctionalMission.CARGO_ONLY, payload, "TEST")
                assert p.human_presence == HumanPresence.NHOB

    def test_defense_classified_no_query_relaxation(self) -> None:
        for env in OperationalEnvironment:
            for func in FunctionalMission:
                p = resolve_profile(env, func, PayloadClassification.DEFENSE_CLASSIFIED, "TEST")
                assert p.constraints["query_relaxation"] is False

    def test_defense_classified_attestation_only(self) -> None:
        for env in OperationalEnvironment:
            for func in FunctionalMission:
                p = resolve_profile(env, func, PayloadClassification.DEFENSE_CLASSIFIED, "TEST")
                assert p.disclosure_mode == "ATTESTATION_ONLY"

    def test_base_kernel_always_present(self) -> None:
        p = resolve_profile(
            OperationalEnvironment.AIR,
            FunctionalMission.PAX_TRANSPORT,
            PayloadClassification.CIVIL_PUBLIC,
            "TEST",
        )
        assert "H_PIPELINE_GATE_CHECK" in p.templates
        assert "SAFETY_ENVELOPE_VALID" in p.rulesets

    def test_all_profiles_have_authority_signoff(self) -> None:
        for env in OperationalEnvironment:
            for func in FunctionalMission:
                for payload in PayloadClassification:
                    p = resolve_profile(env, func, payload, "TEST")
                    assert p.constraints["require_authority"] is True
