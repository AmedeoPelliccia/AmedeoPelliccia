#!/usr/bin/env python3
"""
validate_g10_975.py — Validator for the G10.975 v0.2.0 containment grammar package.

Enforces:
  * Required files exist at the canonical flat layout.
  * Spec is at version "0.2.0" and carries the required v0.2.0 semantics
    (NIB disambiguation, transition matrix, quarantine exit criteria,
     G10.978 forward reference, LC01/KNOT mapping, signed YAML evidence
     format, inline BREX examples, enforcement authority, acceptance
     criteria, Naples-led jurisdiction posture).
  * Evidence schema is present and lists the seven containment states.
  * Registry covers G10.970–G10.979, declares allowed_states matching
    the spec, lists prohibited_names, and lists rejected stale paths.
  * BREX file covers required rule families.
  * No file in the package references any rejected stale path
    (G10-QCSAA, G109, G10/QCSAA/).

Exit code 0 on success, 1 on the first error.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OPT = REPO_ROOT / "OPT-INS_FRAMEWORK"
SCHEMAS = REPO_ROOT / "schemas"

SPEC_MD = OPT / "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md"
REGISTRY_YAML = OPT / "GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml"
BREX_YAML = OPT / "GQAOA-UTA-G10-975-BREX-RULES-001.yaml"
DOMAINS_MD = OPT / "UTA-DOMAINS.md"
EVIDENCE_SCHEMA = SCHEMAS / "G10.975-evidence-package.schema.yaml"

REQUIRED_FILES = [SPEC_MD, REGISTRY_YAML, BREX_YAML, DOMAINS_MD, EVIDENCE_SCHEMA]

REQUIRED_STATES = [
    "OBSERVE_ONLY",
    "SANDBOXED",
    "BOUNDED_PILOT",
    "CONTAINED_ACTIVE",
    "QUARANTINED",
    "REGENCY_REVIEW",
    "RETIRED",
]

REQUIRED_QCSAA_CODES = [f"G10.97{i}" for i in range(10)]

# Stale path references rejected by the validator. Each entry is a regex that
# matches the stale form *only* when not embedded in a legitimate identifier
# (e.g. the canonical filename `GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml`
# legitimately contains the substring "G10-QCSAA" as part of a longer token).
# We therefore require that the stale form appear at a token boundary as a
# folder/path-style reference, not as a fragment of a longer identifier.
REJECTED_PATTERNS = [
    # Folder-form `G10-QCSAA/` or standalone `G10-QCSAA` not preceded by `-UTA-`
    ("G10-QCSAA folder/standalone", re.compile(r"(?<![A-Za-z0-9-])G10-QCSAA(?![A-Za-z0-9-])")),
    # Truncated code `G109` not part of a longer code like G10.97x
    ("G109 truncated code", re.compile(r"(?<![A-Za-z0-9.])G109(?![0-9.])")),
    # Nested layout `G10/QCSAA/`
    ("G10/QCSAA/ nested layout", re.compile(r"G10/QCSAA/")),
]

# v0.2.0 semantics expected to be present in the spec
REQUIRED_SPEC_MARKERS = [
    ("version 0.2.0", re.compile(r'\bversion\b.*?["\']?0\.2\.0["\']?', re.IGNORECASE)),
    ("six-state lattice", re.compile(r"six[- ]state", re.IGNORECASE)),
    ("state transition matrix", re.compile(r"state\s+transition\s+matrix", re.IGNORECASE)),
    ("quarantine exit criteria", re.compile(r"quarantine[\s\S]{0,40}exit\s+criteria", re.IGNORECASE)),
    ("NIB disambiguation", re.compile(r"\bNIB\b", re.IGNORECASE)),
    ("G10.978 forward reference", re.compile(r"G10\.978", re.IGNORECASE)),
    ("LC01/KNOT mapping", re.compile(r"LC01[\s\S]{0,40}KNOT|KNOT[\s\S]{0,40}LC01", re.IGNORECASE)),
    ("signed YAML evidence", re.compile(r"signed\s+YAML", re.IGNORECASE)),
    ("inline BREX examples", re.compile(r"BREX-G10\.975-001|BREX-G10\.975-004", re.IGNORECASE)),
    ("enforcement authority STK-GOV", re.compile(r"STK-GOV", re.IGNORECASE)),
    ("acceptance criteria", re.compile(r"acceptance\s+criteria", re.IGNORECASE)),
    ("Naples lead location", re.compile(r"Naples,\s*Campania,\s*Italy", re.IGNORECASE)),
    ("Italy / EU jurisdiction", re.compile(r"Italy\s*/\s*European\s+Union", re.IGNORECASE)),
    ("stricter control governs", re.compile(r"stricter[\s\S]{0,80}governs", re.IGNORECASE)),
]

REQUIRED_BREX_RULE_IDS = [
    "BREX-G10.975-001",            # containment metadata
    "BREX-G10.975-002",            # permitted descriptive name
    "BREX-G10.975-003",            # uta_code regex
    "BREX-G10.975-004",            # interpretive note on boundary-form
    "BREX-G10.975-PROHIBITED-NAME",
    "BREX-G10.975-TRANSITION-MATRIX",
    "BREX-G10.975-AUTO-DOWNGRADE",
    "BREX-G10.975-EVIDENCE-SCHEMA",
    "BREX-G10.975-EVIDENCE-SIGNERS",
    "BREX-G10.975-EVIDENCE-ACTIVE",
    "BREX-G10.975-QUARANTINE-EXIT",
    "BREX-G10.975-REGENCY-ESCALATION",
    "BREX-G10.975-KNOT-MAPPING",
    "BREX-G10.975-LEDGER",
    "BREX-G10.975-STALE-PATHS",
]


def fail(msg: str) -> None:
    sys.stderr.write(f"[validate_g10_975] FAIL: {msg}\n")
    sys.exit(1)


def info(msg: str) -> None:
    sys.stdout.write(f"[validate_g10_975] {msg}\n")


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {p.relative_to(REPO_ROOT)}: {exc}")
        return ""  # unreachable


def check_required_files() -> None:
    for p in REQUIRED_FILES:
        if not p.is_file():
            fail(f"required file missing: {p.relative_to(REPO_ROOT)}")
    info("required files present at canonical flat layout")


def check_flat_layout() -> None:
    # No nested QCSAA folder under OPT-INS_FRAMEWORK
    for entry in OPT.iterdir():
        if entry.is_dir() and entry.name.lower().replace("_", "-") in {
            "g10-qcsaa",
            "qcsaa",
            "g10",
        }:
            fail(f"nested QCSAA folder forbidden: {entry.relative_to(REPO_ROOT)}")
    info("flat layout enforced (no nested QCSAA folders)")


def check_spec_semantics() -> None:
    text = read_text(SPEC_MD)
    for label, pattern in REQUIRED_SPEC_MARKERS:
        if not pattern.search(text):
            fail(f"spec missing required v0.2.0 marker: {label}")
    # All seven states named in spec
    for state in REQUIRED_STATES:
        if state not in text:
            fail(f"spec missing containment state: {state}")
    info("spec carries v0.2.0 semantics, all containment states, Naples posture")


def check_evidence_schema() -> None:
    text = read_text(EVIDENCE_SCHEMA)
    for state in REQUIRED_STATES:
        if state not in text:
            fail(f"evidence schema missing containment state: {state}")
    if "schemas/G10.975-evidence-package.schema.yaml" not in text:
        fail("evidence schema missing canonical $id reference")
    if "STK-" not in text:
        fail("evidence schema missing STK signer pattern")
    info("evidence schema present with all containment states (six-state lattice + RETIRED) and STK pattern")


def check_registry() -> None:
    text = read_text(REGISTRY_YAML)
    for code in REQUIRED_QCSAA_CODES:
        if code not in text:
            fail(f"registry missing UTA code: {code}")
    for state in REQUIRED_STATES:
        if state not in text:
            fail(f"registry missing allowed_state: {state}")
    if "prohibited_names" not in text:
        fail("registry missing prohibited_names section")
    if "rejected_paths" not in text:
        fail("registry missing rejected_paths section")
    if "Zero-Gene Generative Agents" not in text:
        fail("registry missing G10.971 permitted descriptive name (ZGGA)")
    if "Naples, Campania, Italy" not in text:
        fail("registry missing Naples lead_location")
    if "stricter" not in text.lower():
        fail("registry missing stricter-control regulatory_posture clause")
    info("registry covers G10.970–G10.979, allowed states, prohibited names, Naples posture")


def check_brex() -> None:
    text = read_text(BREX_YAML)
    for rid in REQUIRED_BREX_RULE_IDS:
        if rid not in text:
            fail(f"BREX rules missing required rule id: {rid}")
    info("BREX rules cover all required rule families")


def check_uta_domains_md() -> None:
    text = read_text(DOMAINS_MD)
    if "G10 / 900–999 — QCSAA" not in text and "G10 / 900-999 — QCSAA" not in text:
        fail("UTA-DOMAINS.md missing 'G10 / 900–999 — QCSAA' section")
    if "Naples, Campania, Italy" not in text:
        fail("UTA-DOMAINS.md missing Naples lead location")
    if "Italy / European Union" not in text:
        fail("UTA-DOMAINS.md missing Italy / European Union jurisdiction")
    if "stricter" not in text.lower():
        fail("UTA-DOMAINS.md missing stricter-control posture")
    for fname in [
        "GQAOA-UTA-G10-975-CONTAINMENT-GRAMMAR-001.md",
        "GQAOA-UTA-G10-QCSAA-REGISTRY-001.yaml",
        "GQAOA-UTA-G10-975-BREX-RULES-001.yaml",
        "schemas/G10.975-evidence-package.schema.yaml",
    ]:
        if fname not in text:
            fail(f"UTA-DOMAINS.md missing link to {fname}")
    info("UTA-DOMAINS.md indexes G10/QCSAA with Naples posture and required links")


def check_no_stale_paths() -> None:
    # Walk only the package files we control.
    files_to_scan = [SPEC_MD, REGISTRY_YAML, BREX_YAML, DOMAINS_MD, EVIDENCE_SCHEMA]
    # Files MAY legitimately quote the stale paths only inside an explicit
    # rejection narrative. We detect that narrative by the presence of
    # `rejected_paths:` (YAML) or the literal phrase "stale and rejected"
    # (Markdown). Files that carry such a narrative are exempt; all others
    # are rejected on any token-boundary occurrence.
    for fpath in files_to_scan:
        text = read_text(fpath)
        has_rejection_narrative = (
            "rejected_paths:" in text
            or "stale and rejected" in text.lower()
            or "BREX-G10.975-STALE-PATHS" in text
        )
        if has_rejection_narrative:
            continue
        for label, pattern in REJECTED_PATTERNS:
            m = pattern.search(text)
            if m:
                fail(
                    f"stale path matching '{label}' (matched: {m.group(0)!r}) "
                    f"in {fpath.relative_to(REPO_ROOT)}"
                )
    info("no stale paths (G10-QCSAA, G109, G10/QCSAA/) outside controlled rejection narratives")


def main() -> int:
    info(f"repository root: {REPO_ROOT}")
    check_required_files()
    check_flat_layout()
    check_spec_semantics()
    check_evidence_schema()
    check_registry()
    check_brex()
    check_uta_domains_md()
    check_no_stale_paths()
    info("OK — G10.975 v0.2.0 package validates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
