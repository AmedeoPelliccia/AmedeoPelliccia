"""
AMPEL.py — Regulatory Profile Selector
=======================================
ESSA-DOC-AMPEL-001 runtime component.

Allows users to select a regulatory profile at runtime:
  • EASA-Q100  — Civil Aviation (CS-25 / DO-178C / EASA)
  • SPACE-Q10  — Spacecraft (ECSS / ESA / EU-2021-696)
  • DO-178C    — Software Assurance Profile Resolver (DAL-adaptive)

The selected profile dynamically configures:
  • Artefact templates    (required documentation at each lifecycle gate)
  • Validation rules      (checks that must pass before gate transition)
  • Constraints           (invariants and hard limits enforced by the engine)

Demo repository : https://github.com/AmedeoPelliccia/AMPEL360-AI-studio
Live demo app   : https://ais-pre-qgodcoewjywuhs2glepnfo-324605324739.europe-west2.run.app/

Coding conventions: stdlib only; dataclasses, Enum, type hints.
Parent document: ESSA-DOC-AMPEL-001 (ESSA/ampel.yaml).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, List, Optional, Tuple


# ──────────────────────────────────────────────────────────────────────────────
# 1. ENUMERATIONS
# ──────────────────────────────────────────────────────────────────────────────

class RegulatoryProfile(Enum):
    """Canonical regulatory profiles supported by AMPEL."""
    EASA_Q100 = "EASA-Q100"   # Civil aviation — CS-25 / EASA / DO-178C
    SPACE_Q10 = "SPACE-Q10"   # Spacecraft — ECSS / ESA / EU-2021-696
    DO_178C   = "DO-178C"     # Software assurance resolver (DAL A–E)


class Severity(Enum):
    """Validation rule severity levels."""
    INFO    = "INFO"
    WARN    = "WARN"
    FAIL    = "FAIL"


class GateType(Enum):
    """Lifecycle gate identifiers (CCTLS / AMPEL360)."""
    INTERPRET = "INTERPRET"
    CONFIRM   = "CONFIRM"
    ACTIVATE  = "ACTIVATE"
    PUBLISH   = "PUBLISH"


# ──────────────────────────────────────────────────────────────────────────────
# 2. CORE DATA STRUCTURES
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class ArtefactTemplate:
    """A documentation artefact required at a specific lifecycle gate."""
    template_id: str
    name: str
    standard_ref: str          # e.g. "DO-178C Table A-1", "CS 25.1309"
    gate: GateType
    token: str                 # H-pipeline token: H_EVIDENCE / H_SIGNOFF / etc.
    dal_scope: List[str] = field(default_factory=list)   # e.g. ["A","B","C"]
    notes: str = ""


@dataclass
class ValidationRule:
    """A check that must pass before a gate transition is allowed."""
    rule_id: str
    description: str
    check: str                 # Human-readable check specification
    severity: Severity
    gate: GateType
    dal_scope: List[str] = field(default_factory=list)
    fail_threshold: str = ""
    warn_threshold: str = ""
    reference: str = ""


@dataclass
class Constraint:
    """An invariant or hard limit enforced by the engine."""
    constraint_id: str
    description: str
    value_type: str            # e.g. "boolean", "numeric", "categorical"
    hard_limit: str            # Machine-checkable expression
    source_standard: str
    is_waivable: bool = False
    waiver_token: str = "H_EXCEPTION"


@dataclass
class ProfileConfig:
    """Complete runtime configuration for one regulatory profile."""
    profile: RegulatoryProfile
    document_id: str
    title: str
    regulatory_authority: str
    standards: List[str]
    templates: List[ArtefactTemplate]
    validation_rules: List[ValidationRule]
    constraints: List[Constraint]
    activated_at: Optional[str] = None

    def summary(self) -> str:
        return (
            f"Profile  : {self.profile.value}\n"
            f"Doc ID   : {self.document_id}\n"
            f"Authority: {self.regulatory_authority}\n"
            f"Standards: {', '.join(self.standards)}\n"
            f"Templates: {len(self.templates)}\n"
            f"Rules    : {len(self.validation_rules)}\n"
            f"Constraints: {len(self.constraints)}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# 3. PROFILE BUILDERS
# ──────────────────────────────────────────────────────────────────────────────

def _build_easa_q100() -> ProfileConfig:
    """
    EASA-Q100 — Civil Aviation Profile.
    Source: ESSA/ampel360-q100.yaml + ESSA/AMPEL360-Q100.md
    """
    templates = [
        ArtefactTemplate(
            "Q100-TPL-01", "Failure Hazard Analysis (FHA)",
            "CS 25.1309", GateType.INTERPRET, "H_HAZARD",
            dal_scope=["A", "B", "C"],
            notes="Must tokenise to H_HAZARD before P010 gate closes.",
        ),
        ArtefactTemplate(
            "Q100-TPL-02", "Preliminary System Safety Assessment (PSSA)",
            "CS 25.1309 / AMC 25.1309", GateType.INTERPRET, "H_CONSTRAINT",
            dal_scope=["A", "B"],
            notes="Decompose H_HAZARD into H_CONSTRAINT for sub-systems.",
        ),
        ArtefactTemplate(
            "Q100-TPL-03", "System Safety Assessment (SSA)",
            "CS 25.1309", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "Q100-TPL-04", "Design Organisation Approval (DOA) Sign-off",
            "Part-21 Subpart J", GateType.CONFIRM, "H_SIGNOFF",
            notes="Authority chain: H_SIGNOFF per CS-25 subpart.",
        ),
        ArtefactTemplate(
            "Q100-TPL-05", "Software Development Plan (SDP)",
            "DO-178C Table A-1", GateType.INTERPRET, "H_EVIDENCE",
            dal_scope=["A", "B", "C", "D"],
        ),
        ArtefactTemplate(
            "Q100-TPL-06", "Software Verification Plan (SVP)",
            "DO-178C Table A-2", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "Q100-TPL-07", "Continued Airworthiness Instructions (ICA)",
            "Part-M / Part-145", GateType.PUBLISH, "H_UPDATE",
            notes="ICA generation triggers H_UPDATE → H_ENVELOPE re-evaluation.",
        ),
    ]

    rules = [
        ValidationRule(
            "Q100-RULE-01", "Cyclomatic complexity per function",
            "CC per function must not exceed threshold",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="> 10", warn_threshold="8–10",
            reference="DO-178C / PR-VAL-CC-01",
        ),
        ValidationRule(
            "Q100-RULE-02", "No recursion in DAL A/B code",
            "Recursion forbidden in DAL A and B avionics modules",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="recursion_present",
            reference="DO-178C / PR-VAL-CC-02",
        ),
        ValidationRule(
            "Q100-RULE-03", "Function length",
            "Effective lines of code per function",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="> 60 lines", warn_threshold="50–60 lines",
            reference="DO-178C / PR-VAL-CC-03",
        ),
        ValidationRule(
            "Q100-RULE-04", "No dynamic memory allocation",
            "malloc/free/realloc absent in generated DAL A/B skeleton",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="dynamic_allocation_present",
            reference="MISRA-C:2012 Rule 21.3 / PR-VAL-CC-05",
        ),
        ValidationRule(
            "Q100-RULE-05", "Control-flow nesting depth",
            "Nesting depth of control structures",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="> 4", warn_threshold="> 3",
            reference="DO-178C / PR-VAL-CC-06",
        ),
        ValidationRule(
            "Q100-RULE-06", "PSAC approval present",
            "Plan for Software Aspects of Certification must be approved",
            Severity.FAIL, GateType.INTERPRET, ["A", "B", "C", "D"],
            fail_threshold="PSAC_absent",
            reference="DO-178C Table A-1 / PR-VAL-ART-00",
        ),
    ]

    constraints = [
        Constraint(
            "Q100-CON-01",
            "Safety envelope must satisfy CS 25.1309 catastrophic event probability",
            "numeric", "P_catastrophic < 1e-9 per flight hour",
            "CS 25.1309", is_waivable=False,
        ),
        Constraint(
            "Q100-CON-02",
            "All H_REQ must trace to CS-25 compliance matrix item",
            "boolean", "H_REQ.cs25_ref IS NOT NULL",
            "CS-25 / Part-21", is_waivable=False,
        ),
        Constraint(
            "Q100-CON-03",
            "DOA sign-off required before ACTIVATE gate",
            "boolean", "H_SIGNOFF.doa_authority IS NOT NULL",
            "Part-21 Subpart J", is_waivable=False,
        ),
        Constraint(
            "Q100-CON-04",
            "Hydrogen integration evidence required at P060",
            "boolean", "H_EVIDENCE.hydrogen_integration IS NOT NULL",
            "EASA Special Condition H2", is_waivable=True,
        ),
    ]

    return ProfileConfig(
        profile=RegulatoryProfile.EASA_Q100,
        document_id="ESSA-DOC-AMPEL360-Q100-001",
        title="AMPEL360 Q100 — Aviation Profile (EASA / CS-25)",
        regulatory_authority="European Union Aviation Safety Agency (EASA)",
        standards=["CS-25", "Part-21", "DO-178C", "DO-254", "Part-M", "Part-145"],
        templates=templates,
        validation_rules=rules,
        constraints=constraints,
    )


def _build_space_q10() -> ProfileConfig:
    """
    SPACE-Q10 — Spacecraft Profile.
    Source: ESSA/ampel360-q10.yaml + ESSA/AMPEL360-Q10.md
    """
    templates = [
        ArtefactTemplate(
            "Q10-TPL-01", "Mission Hazard Analysis (probabilistic risk)",
            "ECSS-Q-ST-40C", GateType.INTERPRET, "H_HAZARD",
            notes="Mission objectives → probabilistic risk decomposition.",
        ),
        ArtefactTemplate(
            "Q10-TPL-02", "Safety Envelope v1.0 (five dimensions)",
            "ECSS-E-ST-10-04C", GateType.INTERPRET, "H_ENVELOPE",
            notes="RANGE_SAFETY / ORBITAL_DEBRIS / COLLISION_AVOIDANCE / REENTRY_SAFETY / HUMAN_OVERRIDE",
        ),
        ArtefactTemplate(
            "Q10-TPL-03", "Frequency-Consequence (F-C) Matrix",
            "ECSS-Q-ST-40C §5", GateType.CONFIRM, "H_EVIDENCE",
        ),
        ArtefactTemplate(
            "Q10-TPL-04", "Launch Licence (H_SIGNOFF)",
            "EU-2021-696 / National Licensing Framework", GateType.ACTIVATE, "H_SIGNOFF",
            notes="Must be present before P050 gate closes.",
        ),
        ArtefactTemplate(
            "Q10-TPL-05", "Range Safety Clearance",
            "ECSS-E-ST-10-04C / Range Authority", GateType.ACTIVATE, "H_SIGNOFF",
        ),
        ArtefactTemplate(
            "Q10-TPL-06", "Conjunction/CDM Assessment Report",
            "ESA Space Debris Mitigation Guidelines", GateType.CONFIRM, "H_EVIDENCE",
            notes="CDM result out-of-envelope → H_UPDATE → H_ENVELOPE re-evaluation.",
        ),
        ArtefactTemplate(
            "Q10-TPL-07", "Post-Mission Debris Assessment",
            "ESA Space Debris Mitigation / COSPAR", GateType.PUBLISH, "H_EVIDENCE",
            notes="25-year deorbit compliance evidence.",
        ),
    ]

    rules = [
        ValidationRule(
            "Q10-RULE-01", "25-year deorbit compliance",
            "Orbital decay / active deorbit plan must demonstrate ≤ 25-year reentry",
            Severity.FAIL, GateType.CONFIRM, [],
            fail_threshold="residual_orbital_lifetime > 25 years",
            reference="ESA Space Debris Mitigation Guidelines",
        ),
        ValidationRule(
            "Q10-RULE-02", "Casualty expectation below threshold",
            "Surviving debris casualty expectation Ec must be < 1e-4 per mission",
            Severity.FAIL, GateType.CONFIRM, [],
            fail_threshold="Ec >= 1e-4",
            reference="ECSS-Q-ST-40C / COSPAR",
        ),
        ValidationRule(
            "Q10-RULE-03", "Launch licence present at P050",
            "National launch licence must be issued (H_SIGNOFF) before ACTIVATE gate",
            Severity.FAIL, GateType.ACTIVATE, [],
            fail_threshold="launch_licence_absent",
            reference="EU-2021-696 / National Licensing Framework",
        ),
        ValidationRule(
            "Q10-RULE-04", "FMEA / FTA evidence present",
            "Failure Mode and Effects Analysis or Fault Tree Analysis registered as H_EVIDENCE",
            Severity.FAIL, GateType.CONFIRM, [],
            fail_threshold="H_EVIDENCE.fmea_fta_absent",
            reference="ECSS-Q-ST-30-02C",
        ),
        ValidationRule(
            "Q10-RULE-05", "Probability of collision (Pc) within envelope",
            "Each conjunction event Pc must be below H_ENVELOPE threshold",
            Severity.WARN, GateType.CONFIRM, [],
            fail_threshold="Pc > H_ENVELOPE.Pc_threshold",
            reference="ESA CDM Policy",
        ),
    ]

    constraints = [
        Constraint(
            "Q10-CON-01",
            "Orbital lifetime must comply with 25-year rule",
            "numeric", "residual_orbital_lifetime <= 25 years",
            "ESA Space Debris Mitigation Guidelines", is_waivable=True,
        ),
        Constraint(
            "Q10-CON-02",
            "All H_HAZARD must bind to one of the five safety dimensions",
            "categorical",
            "H_HAZARD.dimension IN {RANGE_SAFETY, ORBITAL_DEBRIS, COLLISION_AVOIDANCE, REENTRY_SAFETY, HUMAN_OVERRIDE}",
            "ECSS-E-ST-10-04C", is_waivable=False,
        ),
        Constraint(
            "Q10-CON-03",
            "Launch authority H_SIGNOFF required before ACTIVATE",
            "boolean", "H_SIGNOFF.launch_authority IS NOT NULL",
            "EU-2021-696", is_waivable=False,
        ),
        Constraint(
            "Q10-CON-04",
            "Spectrum coordination confirmed (ITU) where applicable",
            "boolean", "H_CONSTRAINT.itu_spectrum_confirmed OR NOT applies",
            "ITU Radio Regulations", is_waivable=True,
        ),
    ]

    return ProfileConfig(
        profile=RegulatoryProfile.SPACE_Q10,
        document_id="ESSA-DOC-AMPEL360-Q10-001",
        title="AMPEL360 Q10 — Spacecraft Profile (ESA / ECSS)",
        regulatory_authority="European Space Agency (ESA) / European Commission",
        standards=["ECSS-E-ST-10-04C", "ECSS-Q-ST-40C", "EU-2021-696",
                   "ESA-Space-Debris-Mitigation", "COSPAR", "ITU-Radio-Regulations"],
        templates=templates,
        validation_rules=rules,
        constraints=constraints,
    )


def _build_do178c() -> ProfileConfig:
    """
    DO-178C — Software Assurance Profile Resolver.
    Source: ESSA/ampel360-pr.yaml + ESSA/AMPEL360-PR.md
    DAL-adaptive: rules tagged by applicable DAL level.
    """
    templates = [
        ArtefactTemplate(
            "PR-TPL-00", "Plan for Software Aspects of Certification (PSAC)",
            "DO-178C Table A-1", GateType.INTERPRET, "H_EVIDENCE",
            dal_scope=["A", "B", "C", "D"],
            notes="Primary DO-178C planning document. Absent → blocks INTERPRET gate.",
        ),
        ArtefactTemplate(
            "PR-TPL-01", "System Safety Analysis (SAR/FHA/PSSA/SSA output)",
            "DO-178C system-level input", GateType.INTERPRET, "H_EVIDENCE",
            dal_scope=["A", "B", "C", "D"],
        ),
        ArtefactTemplate(
            "PR-TPL-02", "Software Development Plan (SDP)",
            "DO-178C Table A-1", GateType.INTERPRET, "H_EVIDENCE",
            dal_scope=["A", "B", "C", "D"],
        ),
        ArtefactTemplate(
            "PR-TPL-03", "Software Verification Plan (SVP)",
            "DO-178C Table A-2", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "PR-TPL-04", "Software Requirements Standards",
            "DO-178C Table A-3", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "PR-TPL-05", "Software Design Standards",
            "DO-178C Table A-4", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "PR-TPL-06", "Software Code Standards (language subset rules)",
            "DO-178C Table A-5", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "PR-TPL-07", "Tool Qualification Plan (TQP) — DO-330 tools",
            "DO-330 Table A-1", GateType.CONFIRM, "H_EVIDENCE",
            dal_scope=["A", "B"],
            notes="Absent at DAL A/B → blocks CONFIRM gate.",
        ),
        ArtefactTemplate(
            "PR-TPL-08", "Static Analysis Report (complexity + MISRA scan) per unit",
            "DO-178C Table A-7", GateType.ACTIVATE, "H_EVIDENCE",
            dal_scope=["A", "B", "C"],
        ),
        ArtefactTemplate(
            "PR-TPL-09", "Unit Test Results with MC/DC coverage table",
            "DO-178C Table A-7", GateType.ACTIVATE, "H_EVIDENCE",
            dal_scope=["A", "B"],
        ),
        ArtefactTemplate(
            "PR-TPL-10", "Software Conformity Review (SCR) record",
            "DO-178C Table A-8", GateType.PUBLISH, "H_SIGNOFF",
            dal_scope=["A", "B", "C"],
        ),
    ]

    rules = [
        # Code complexity
        ValidationRule(
            "PR-VAL-CC-01", "Cyclomatic complexity per function",
            "Cyclomatic complexity check per function unit",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="> 10 (DAL A/B), > 15 (DAL C)",
            warn_threshold="8–10 (DAL A/B), 12–15 (DAL C)",
            reference="DO-178C / PR-VAL-CC-01",
        ),
        ValidationRule(
            "PR-VAL-CC-02", "Call stack depth and recursion",
            "Recursion forbidden; static stack bound must be derivable",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="recursion_present",
            warn_threshold="static_bound_not_derivable",
            reference="DO-178C / PR-VAL-CC-02",
        ),
        ValidationRule(
            "PR-VAL-CC-03", "Function length",
            "Lines of effective code per function",
            Severity.FAIL, GateType.CONFIRM, ["A", "B", "C"],
            fail_threshold="> 60 LoC (DAL A/B), > 80 LoC (DAL C)",
            warn_threshold="50–60 LoC (DAL A/B)",
            reference="DO-178C / PR-VAL-CC-03",
        ),
        ValidationRule(
            "PR-VAL-CC-04", "Number of parameters per function",
            "Excessive function parameters increase coupling risk",
            Severity.FAIL, GateType.CONFIRM, ["A", "B", "C"],
            fail_threshold="> 8", warn_threshold="7–8",
            reference="MISRA-C:2012 Dir 4.6 / PR-VAL-CC-04",
        ),
        ValidationRule(
            "PR-VAL-CC-05", "Dynamic memory allocation forbidden",
            "malloc/free/realloc must not appear in DAL A/B skeleton",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="dynamic_alloc_present",
            reference="MISRA-C:2012 Rule 21.3 / PR-VAL-CC-05",
        ),
        ValidationRule(
            "PR-VAL-CC-06", "Control-flow nesting depth",
            "Nesting depth of control flow constructs",
            Severity.FAIL, GateType.CONFIRM, ["A", "B", "C"],
            fail_threshold="> 4 (DAL A/B), > 5 (DAL C)",
            warn_threshold="> 3 (DAL A/B)",
            reference="DO-178C / PR-VAL-CC-06",
        ),
        # Required artefact presence
        ValidationRule(
            "PR-VAL-ART-00", "PSAC must be approved before INTERPRET gate",
            "Plan for Software Aspects of Certification (PSAC) present and approved",
            Severity.FAIL, GateType.INTERPRET, ["A", "B", "C", "D"],
            fail_threshold="PSAC_absent",
            reference="DO-178C Table A-1",
        ),
        ValidationRule(
            "PR-VAL-ART-07", "Tool Qualification Plan required for DO-330 tools at DAL A/B",
            "TQP must cover all qualification-basis tools",
            Severity.FAIL, GateType.CONFIRM, ["A", "B"],
            fail_threshold="TQP_absent",
            reference="DO-330 Table A-1",
        ),
        # MISRA-C
        ValidationRule(
            "PR-VAL-MA-01", "MISRA Compliance Process document present",
            "MISRA_Compliance_Process document issued before CONFIRM gate",
            Severity.FAIL, GateType.CONFIRM, ["A", "B", "C"],
            fail_threshold="MISRA_process_doc_absent",
            reference="MISRA C:2012 / PR-VAL-MA-01",
        ),
    ]

    constraints = [
        Constraint(
            "PR-CON-01",
            "Resolver SHALL NOT generate activable control logic",
            "boolean", "output.is_activable == False",
            "ESSA-DOC-AMPEL360-PR-001 §Safety Boundary", is_waivable=False,
        ),
        Constraint(
            "PR-CON-02",
            "H_ENVELOPE must be signed before any generation step",
            "boolean", "H_ENVELOPE.signed == True",
            "ESSA-DOC-AMPEL360-PR-001 §Required Inputs", is_waivable=False,
        ),
        Constraint(
            "PR-CON-03",
            "Language derivation must be registered as H_EVIDENCE on the artefact",
            "boolean", "language_artefact.H_EVIDENCE_ref IS NOT NULL",
            "PR-LANG-01 / PR-LANG-02", is_waivable=False,
        ),
        Constraint(
            "PR-CON-04",
            "No language recommendation final without H_SIGNOFF (responsible engineer)",
            "boolean", "language_recommendation.H_SIGNOFF IS NOT NULL",
            "PR-LANG-02", is_waivable=False,
        ),
    ]

    return ProfileConfig(
        profile=RegulatoryProfile.DO_178C,
        document_id="ESSA-DOC-AMPEL360-PR-001",
        title="AMPEL360 Profile Resolver — DO-178C / DAL-Adaptive",
        regulatory_authority="EASA / FAA (joint applicability per DO-178C §1.1)",
        standards=["DO-178C", "DO-254", "DO-330", "DO-331", "MISRA-C:2012",
                   "ECSS-E-ST-40C"],
        templates=templates,
        validation_rules=rules,
        constraints=constraints,
    )


# ──────────────────────────────────────────────────────────────────────────────
# 4. PROFILE REGISTRY
# ──────────────────────────────────────────────────────────────────────────────

_PROFILE_BUILDERS: Dict[RegulatoryProfile, object] = {
    RegulatoryProfile.EASA_Q100: _build_easa_q100,
    RegulatoryProfile.SPACE_Q10: _build_space_q10,
    RegulatoryProfile.DO_178C:   _build_do178c,
}


# ──────────────────────────────────────────────────────────────────────────────
# 5. PROFILE SELECTOR
# ──────────────────────────────────────────────────────────────────────────────

class ProfileSelector:
    """
    Runtime regulatory profile selector.

    Usage::

        selector = ProfileSelector()
        config = selector.select(RegulatoryProfile.EASA_Q100)
        print(config.summary())
        passed, report = selector.validate({"PSAC_absent": False, ...})
    """

    def __init__(self) -> None:
        self._active: Optional[ProfileConfig] = None

    # ── selection ─────────────────────────────────────────────────────────────

    def select(self, profile: RegulatoryProfile) -> ProfileConfig:
        """
        Activate *profile* and return its configuration.

        The returned :class:`ProfileConfig` exposes ``.templates``,
        ``.validation_rules``, and ``.constraints`` ready for use.
        """
        builder = _PROFILE_BUILDERS[profile]
        config = builder()                   # type: ignore[operator]
        config.activated_at = datetime.now(timezone.utc).isoformat()
        self._active = config
        return config

    @property
    def active_profile(self) -> Optional[ProfileConfig]:
        """The currently active :class:`ProfileConfig`, or *None*."""
        return self._active

    # ── introspection ─────────────────────────────────────────────────────────

    def list_templates(self, gate: Optional[GateType] = None) -> List[ArtefactTemplate]:
        """Return templates for the active profile, optionally filtered by gate."""
        if self._active is None:
            raise RuntimeError("No profile selected. Call select() first.")
        templates = self._active.templates
        if gate is not None:
            templates = [t for t in templates if t.gate == gate]
        return templates

    def list_rules(
        self,
        severity: Optional[Severity] = None,
        dal: Optional[str] = None,
    ) -> List[ValidationRule]:
        """Return validation rules, optionally filtered by severity or DAL level."""
        if self._active is None:
            raise RuntimeError("No profile selected. Call select() first.")
        rules = self._active.validation_rules
        if severity is not None:
            rules = [r for r in rules if r.severity == severity]
        if dal is not None:
            rules = [r for r in rules if not r.dal_scope or dal in r.dal_scope]
        return rules

    def list_constraints(self, waivable: Optional[bool] = None) -> List[Constraint]:
        """Return constraints, optionally filtered by waivability."""
        if self._active is None:
            raise RuntimeError("No profile selected. Call select() first.")
        constraints = self._active.constraints
        if waivable is not None:
            constraints = [c for c in constraints if c.is_waivable == waivable]
        return constraints

    # ── validation ────────────────────────────────────────────────────────────

    def validate(self, state: Dict[str, object]) -> Tuple[bool, List[Dict]]:
        """
        Run all validation rules against *state*.

        *state* is a dict of check-name → value.  A rule fires when its
        ``check`` key is present in *state* and equals the ``fail_threshold``
        value (exact string match).  Rules whose check key is absent in
        *state* are skipped (treated as PASS).

        Returns ``(all_passed: bool, report: list[dict])``.
        """
        if self._active is None:
            raise RuntimeError("No profile selected. Call select() first.")

        report: List[Dict] = []
        all_passed = True

        for rule in self._active.validation_rules:
            check_key = rule.check.replace(" ", "_").lower()
            # Try the rule's check key directly; fall back to rule_id key
            raw = state.get(check_key, state.get(rule.rule_id))
            if raw is None:
                report.append({
                    "rule_id": rule.rule_id,
                    "result": "SKIP",
                    "reason": "check key not present in state",
                })
                continue

            fired = str(raw) == rule.fail_threshold
            if fired and rule.severity == Severity.FAIL:
                all_passed = False
            report.append({
                "rule_id": rule.rule_id,
                "description": rule.description,
                "result": rule.severity.value if fired else "PASS",
                "check_value": raw,
                "threshold": rule.fail_threshold,
                "reference": rule.reference,
            })

        return all_passed, report

    # ── export ────────────────────────────────────────────────────────────────

    def export_config(self, filepath: str = "profile_config.json") -> None:
        """Serialise the active profile configuration to *filepath* as JSON."""
        if self._active is None:
            raise RuntimeError("No profile selected. Call select() first.")
        data = asdict(self._active)
        # Enum values need to be serialised as strings
        data["profile"] = self._active.profile.value
        for tmpl in data["templates"]:
            tmpl["gate"] = tmpl["gate"].value if hasattr(tmpl["gate"], "value") else tmpl["gate"]
        for rule in data["validation_rules"]:
            rule["severity"] = rule["severity"].value if hasattr(rule["severity"], "value") else rule["severity"]
            rule["gate"] = rule["gate"].value if hasattr(rule["gate"], "value") else rule["gate"]
        try:
            with open(filepath, "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2)
            print(f"[Export] Profile config saved to {filepath}")
        except OSError as exc:
            print(f"[Export] Failed to save profile config: {exc}")

    @staticmethod
    def available_profiles() -> List[str]:
        """Return the names of all registered regulatory profiles."""
        return [p.value for p in RegulatoryProfile]


# ──────────────────────────────────────────────────────────────────────────────
# 6. QUICK-START DEMO  (python AMPEL.py)
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    selector = ProfileSelector()

    print("=" * 65)
    print("AMPEL Regulatory Profile Selector — Demo")
    print(f"Available profiles: {selector.available_profiles()}")
    print("Demo repo : https://github.com/AmedeoPelliccia/AMPEL360-AI-studio")
    print("Live app  : https://ais-pre-qgodcoewjywuhs2glepnfo-324605324739.europe-west2.run.app/")
    print("=" * 65)

    # ── EASA-Q100 ─────────────────────────────────────────────────────────────
    q100 = selector.select(RegulatoryProfile.EASA_Q100)
    print(f"\n{q100.summary()}")

    confirm_templates = selector.list_templates(gate=GateType.CONFIRM)
    print(f"\nTemplates at CONFIRM gate ({len(confirm_templates)}):")
    for t in confirm_templates:
        print(f"  [{t.template_id}] {t.name}  ({t.standard_ref})")

    fail_rules = selector.list_rules(severity=Severity.FAIL)
    print(f"\nFAIL-severity rules ({len(fail_rules)}):")
    for r in fail_rules:
        print(f"  [{r.rule_id}] {r.description}")

    hard_constraints = selector.list_constraints(waivable=False)
    print(f"\nNon-waivable constraints ({len(hard_constraints)}):")
    for c in hard_constraints:
        print(f"  [{c.constraint_id}] {c.hard_limit}")

    # Validation run — state may use rule_id as key (direct fallback in validate()).
    # Supplying the fail_threshold value as the state value triggers a FAIL;
    # any other value gives a PASS.
    print("\n── Validation run (EASA-Q100, simulated state) ──")
    simulated_state = {
        "Q100-RULE-01": "> 10",       # FAIL: function exceeds complexity threshold
        "Q100-RULE-02": "false",       # PASS: no recursion detected
        "Q100-RULE-06": "PSAC_absent", # FAIL: PSAC not yet present
    }
    passed, rpt = selector.validate(simulated_state)
    for entry in rpt:
        if entry.get("result") != "SKIP":
            print(f"  {entry['rule_id']:20s}  {entry['result']}")
    print(f"  Overall: {'PASS' if passed else 'FAIL'}")

    # ── SPACE-Q10 ─────────────────────────────────────────────────────────────
    q10 = selector.select(RegulatoryProfile.SPACE_Q10)
    print(f"\n{q10.summary()}")

    # ── DO-178C ───────────────────────────────────────────────────────────────
    pr = selector.select(RegulatoryProfile.DO_178C)
    print(f"\n{pr.summary()}")
    dal_b_rules = selector.list_rules(dal="B")
    print(f"  Rules applicable to DAL B: {len(dal_b_rules)}")

    print("\n[Done] All three profiles exercised successfully.")
