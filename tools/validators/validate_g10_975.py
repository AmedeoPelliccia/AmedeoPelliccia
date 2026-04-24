#!/usr/bin/env python3
"""
G10.975 containment grammar validator.

Validates:
- canonical flat UTA path is used
- stale G10-QCSAA directory path is not introduced
- stale G109 path is not referenced outside controlled rejection lists
- G10.975 specification exists
- UTA-DOMAINS.md links to the spec
- registry and BREX files exist
- 970-979 ZGen/regent-ZetaGentz containment semantics are explicit
- monster alias has mandatory interpretive note
- containment states are defined
- quarantine / regency / evidence sections exist
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

STALE_PATHS = [
    "OPT-INS_FRAMEWORK/G10-QCSAA/",
    "GQAOA-UTA-G109-G10-975-CONTAINMENT-GRAMMAR-001.md",
]

REQUIRED_SPEC_TERMS = [
    "G10.975",
    "Containment Grammar",
    "G10.970–G10.979",
    "ZGen",
    "regent-ZetaGentz",
    "Zero-Gene",
    "QUARANTINED",
    "REGENCY_REVIEW",
    "Evidence Package",
    "STK-GOV",
    "STK-SAFETY",
]

REQUIRED_STATES = [
    "OBSERVE_ONLY",
    "SANDBOXED",
    "QUARANTINED",
    "REGENCY_REVIEW",
    "CONTAINED_ACTIVE",
    "RETIRED",
]

REQUIRED_FILES = [
    SPEC,
    REGISTRY,
    BREX,
    UTA_DOMAINS,
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


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(errors, message):
    errors.append(f"FAIL: {message}")


def warn(warnings, message):
    warnings.append(f"WARN: {message}")


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

    for term in REQUIRED_SPEC_TERMS:
        if term not in text:
            fail(errors, f"Missing required term in spec: {term}")

    for state in REQUIRED_STATES:
        if state not in text:
            fail(errors, f"Missing containment state in spec: {state}")

    required_note = '"Monster" is used in the original sense of monstrum'
    if "Generative Monsters" in text and required_note not in text:
        fail(errors, "Generative Monsters alias appears without mandatory interpretive note")

    required_sections = [
        "## 7. Regency Escalation",
        "## 8. Evidence Package",
        "## 9. BREX / Validation Rules",
        "## 10. Registry Requirements",
        "## 12. Acceptance Criteria",
    ]

    for section in required_sections:
        if section not in text:
            fail(errors, f"Missing required spec section: {section}")


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

    for item in required:
        if item not in text:
            fail(errors, f"UTA-DOMAINS.md missing required G10 reference: {item}")


def validate_registry(errors):
    if not REGISTRY.exists():
        return

    text = read(REGISTRY)

    required = [
        "G10.970",
        "G10.971",
        "G10.972",
        "G10.973",
        "G10.974",
        "G10.975",
        "G10.976",
        "G10.977",
        "G10.978",
        "G10.979",
        "regent-ZetaGentz",
        "OBSERVE_ONLY",
        "monster_alias_requires_interpretive_note",
    ]

    for item in required:
        if item not in text:
            fail(errors, f"Registry missing required item: {item}")


def validate_brex(errors):
    if not BREX.exists():
        return

    text = read(BREX)

    required = [
        "G10-975-BLOCK-001",
        "G10-975-BLOCK-002",
        "G10-975-BLOCK-003",
        "G10-975-BLOCK-004",
        "G10-975-BLOCK-005",
        "G10-975-WARN-004",
        "G10-975-WARN-005",
        "prohibited_terms",
    ]

    for item in required:
        if item not in text:
            fail(errors, f"BREX file missing required item: {item}")


def strip_allowed_prohibition_sections(text: str) -> str:
    """
    Remove controlled sections where prohibited terms are allowed to appear:
    - spec section 4.4
    - BREX prohibited_terms list
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
