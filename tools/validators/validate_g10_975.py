#!/usr/bin/env python3
"""
G10.975 containment grammar validator.

Validates the v0.2.0 normative spec and companion artifacts:
- canonical flat UTA path is used
- stale G10-QCSAA directory path is not introduced
- stale G109 path is not referenced outside controlled rejection lists
- G10.975 specification, schema, registry, BREX, and UTA index exist
- v0.2.0 containment states, transitions, quarantine exit criteria, LC01/KNOT,
  NIB disambiguation, enforcement authority, and evidence schema are specified
- registry and BREX implement the v0.2.0 normative model
- prohibited names appear only in controlled prohibition contexts
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]

SPEC = ROOT / "OPT-INS_FRAMEWORK/GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md"
REGISTRY = ROOT / "OPT-INS_FRAMEWORK/GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml"
BREX = ROOT / "OPT-INS_FRAMEWORK/GQAOA-UTA-G10-975-BREX-RULES-001.yaml"
UTA_DOMAINS = ROOT / "OPT-INS_FRAMEWORK/UTA-DOMAINS.md"
README = ROOT / "OPT-INS_FRAMEWORK/README.md"
SCHEMA = ROOT / "schemas/G10.975-evidence-package.schema.yaml"

STALE_PATHS = [
    "OPT-INS_FRAMEWORK/G10-QCSAA/",
    "GQAOA-UTA-G109-G10-975-CONTAINMENT-GRAMMAR-001.md",
]

REQUIRED_STATES = [
    "OBSERVE_ONLY",
    "SANDBOXED",
    "QUARANTINED",
    "REGENCY_REVIEW",
    "CONTAINED_ACTIVE",
    "RETIRED",
]

REQUIRED_INTERPRETIVE_NOTE = (
    '"Monster" is used in the original sense of monstrum: a sign, warning, '
    "or boundary-form requiring careful interpretation, not a moral claim, "
    "personhood claim, or operational authorization."
)

REQUIRED_FILES = [
    SPEC,
    REGISTRY,
    BREX,
    UTA_DOMAINS,
    SCHEMA,
]

PROHIBITED_TERMS = [
    "evil AI",
    "demon AI",
    "killer agent",
    "sentient weapon",
    "autonomous monster",
    "god agent",
    "slave intelligence",
    "disposable sentience",
    "uncontained synthetic life",
]

REQUIRED_QE_IDS = [f"QE-{index:03d}" for index in range(1, 11)]
REQUIRED_AC_IDS = [f"AC-{index:03d}" for index in range(1, 16)]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(errors, message):
    errors.append(f"FAIL: {message}")


def warn(warnings, message):
    warnings.append(f"WARN: {message}")


def require_items(text: str, items, errors, label: str):
    for item in items:
        if item not in text:
            fail(errors, f"{label} missing required item: {item}")


def validate_required_files(errors):
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(errors, f"Missing required file: {path}")


def strip_allowed_stale_path_sections(text: str) -> str:
    text = re.sub(
        r"stale_paths_rejected:.*?(?=\n[a-zA-Z0-9_]+:|\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"warning_rules:.*?(?=\n[a-zA-Z0-9_]+:|\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"Stale paths explicitly rejected:.*?(?=\n## |\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    return text


def validate_no_stale_paths(errors):
    scan_root = ROOT / "OPT-INS_FRAMEWORK"
    if not scan_root.exists():
        fail(errors, f"Missing OPT-INS_FRAMEWORK root: {scan_root}")
        return

    for path in scan_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".txt"}:
            text = strip_allowed_stale_path_sections(read(path))
            for stale in STALE_PATHS:
                if stale in text:
                    fail(errors, f"Stale path reference found in {path}: {stale}")


def validate_no_new_g10_qcsaa_dir(errors):
    disallowed = ROOT / "OPT-INS_FRAMEWORK/G10-QCSAA"
    if disallowed.exists():
        fail(errors, f"Disallowed new top-level layout exists: {disallowed}")


def validate_spec_content(errors):
    if not SPEC.exists():
        return

    text = read(SPEC)

    required = [
        'version: "0.2.0"',
        'status: "draft-controlled"',
        "## 2. Taxonomy Placement",
        "### 2.1 Relationship to Non-Inference Boundaries",
        "AEROSPACEMODEL-ASIT-NIB-SPEC-001",
        "## 3. Scope",
        "Non-biological generative agent class; `Zero-Gene Generative Agents` is the permitted descriptive variant",
        "## 5. Containment States",
        "### 5.1 Permitted State Transitions",
        "### 5.2 State Transition Diagram",
        "Direct transition from `QUARANTINED` to `CONTAINED_ACTIVE` is prohibited.",
        "Direct transition from `OBSERVE_ONLY` to `CONTAINED_ACTIVE` is prohibited.",
        "### 6.1 Quarantine Exit Criteria",
        "A `QUARANTINED` entity may exit quarantine only through `REGENCY_REVIEW`.",
        "Regency escalation is governed by `G10.978 — Regency Escalation`.",
        "### 7.4 LC01 / KNOT Mapping",
        "KNOT-G10.97x-<NORMALIZED-ENTITY-NAME>-<SEQ>",
        "residual_target",
        "Every `G10.975` quarantine or regency escalation must generate a signed YAML evidence package.",
        "schemas/G10.975-evidence-package.schema.yaml",
        "G10.975-EVIDENCE-<YYYYMMDD>-<SEQ>.yaml",
        "### 9.2.1 Inline BREX rule examples",
        "## 11. References and Enforcement Authority",
        "STK-GOV SHALL NOT permit operational interpretation",
    ]
    require_items(text, required, errors, "Spec")

    for state in REQUIRED_STATES:
        if state not in text:
            fail(errors, f"Missing containment state in spec: {state}")

    for qe_id in REQUIRED_QE_IDS:
        if qe_id not in text:
            fail(errors, f"Missing quarantine exit criterion in spec: {qe_id}")

    for ac_id in REQUIRED_AC_IDS:
        if ac_id not in text:
            fail(errors, f"Missing acceptance criterion in spec: {ac_id}")

    if "Generative Monsters" in text and REQUIRED_INTERPRETIVE_NOTE not in text:
        fail(errors, "Generative Monsters alias appears without mandatory interpretive note")


def validate_uta_domains_link(errors):
    if not UTA_DOMAINS.exists():
        return

    text = read(UTA_DOMAINS)

    required = [
        "G10 / 900–999",
        "QCSAA",
        "G10.970–G10.979",
        "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md",
        "GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml",
        "GQAOA-UTA-G10-975-BREX-RULES-001.yaml",
    ]
    require_items(text, required, errors, "UTA-DOMAINS.md")


def validate_registry(errors):
    if not REGISTRY.exists():
        return

    text = read(REGISTRY)

    required = [
        'version: "0.2.0"',
        "schemas/G10.975-evidence-package.schema.yaml",
        "owner_stk",
        "evidence_package_pointer",
        "state_transition_matrix_required",
        "quarantine_exit_criteria_required",
        "lc01_knot_required_for_regency_review",
        "nib_relationship_disambiguated",
        "QUARANTINED -> CONTAINED_ACTIVE",
        "Zero-Gene Generative Agents",
        "STK-GOV",
        "STK-SAFETY",
        "STK-QCSAA",
        "STK-LEDGER",
        "STK-ETHICS",
        "monster_alias_requires_interpretive_note",
    ]
    require_items(text, required, errors, "Registry")

    for code in [f"G10.97{index}" for index in range(10)]:
        if code not in text:
            fail(errors, f"Registry missing required code: {code}")


def validate_brex(errors):
    if not BREX.exists():
        return

    text = read(BREX)

    required = [
        'version: "0.2.0"',
        "schemas/G10.975-evidence-package.schema.yaml",
        "permitted_state_transitions",
        "prohibited_state_transitions",
        "quarantine_exit_criteria",
        "lc01_knot_mapping",
        "G10-975-BLOCK-001",
        "G10-975-BLOCK-002",
        "G10-975-BLOCK-003",
        "G10-975-BLOCK-004",
        "G10-975-BLOCK-005",
        "G10-975-BLOCK-006",
        "G10-975-BLOCK-007",
        "G10-975-BLOCK-008",
        "G10-975-BLOCK-009",
        "G10-975-BLOCK-010",
        "G10-975-BLOCK-011",
        "G10-975-WARN-004",
        "G10-975-WARN-005",
        "prohibited_terms",
        "QUARANTINED",
        "CONTAINED_ACTIVE",
        "KNOT-G10.97x-<NORMALIZED-ENTITY-NAME>-<SEQ>",
    ]
    require_items(text, required, errors, "BREX file")

    for qe_id in REQUIRED_QE_IDS:
        if qe_id not in text:
            fail(errors, f"BREX file missing quarantine exit criterion: {qe_id}")


def validate_schema(errors):
    if not SCHEMA.exists():
        return

    text = read(SCHEMA)
    required = [
        "G10.975 Evidence Package",
        "evidence_package",
        "G10",
        "975-EVIDENCE-[0-9]{8}-[0-9]{3,}",
        "97[0-9]",
        "source_hash",
        "residual_target",
        "STK-GOV",
        "STK-SAFETY",
        "STK-LEDGER",
        "anchor_id",
    ]
    require_items(text, required, errors, "Evidence schema")

    for state in REQUIRED_STATES:
        if state not in text:
            fail(errors, f"Evidence schema missing containment state: {state}")


def strip_allowed_prohibition_sections(text: str) -> str:
    """
    Remove controlled sections where prohibited terms are allowed to appear.

    This preserves AC-011 by allowing prohibited-name strings only in the
    normative spec's controlled prohibition section and in the BREX
    prohibited_terms detector list; any other occurrence under OPT-INS_FRAMEWORK
    fails validation.
    """
    text = re.sub(
        r"### 4\.4 Prohibited names.*?(?=\n### |\n## |\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"prohibited_terms:.*?(?=\n[a-zA-Z0-9_]+:|\Z)",
        "",
        text,
        flags=re.DOTALL,
    )
    return text


def validate_prohibited_terms(errors):
    scan_root = ROOT / "OPT-INS_FRAMEWORK"

    for path in scan_root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml"}:
            text = strip_allowed_prohibition_sections(read(path))
            lower = text.lower()

            for term in PROHIBITED_TERMS:
                if term.lower() in lower:
                    fail(errors, f"Prohibited term outside controlled prohibition list: '{term}' in {path}")


def validate_readme_optional(warnings):
    if not README.exists():
        return

    text = read(README)
    if "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md" not in text:
        warn(warnings, "README exists but does not link G10.975 spec")


def main():
    errors = []
    warnings = []

    validate_required_files(errors)
    validate_no_new_g10_qcsaa_dir(errors)
    validate_no_stale_paths(errors)
    validate_spec_content(errors)
    validate_uta_domains_link(errors)
    validate_registry(errors)
    validate_brex(errors)
    validate_schema(errors)
    validate_prohibited_terms(errors)
    validate_readme_optional(warnings)

    for item in warnings:
        print(item)

    if errors:
        for item in errors:
            print(item)
        print("G10.975 validation: FAIL")
        return 1

    print("G10.975 validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
