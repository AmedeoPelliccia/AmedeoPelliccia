# GNS-010 — Changelog

All notable changes to the EGNOS & Galileo Integration Specification.

## [0.2.0] — 2026-03-06

### Changed

- Major rewrite separating **creditable SoL/LPV claims**, **supplemental Galileo capabilities**, and **internal CCTLS/UTS/ESSA governance**.
- §0 Purpose & Scope — explicit three-tier distinction (certifiable baseline / supplemental non-creditable / internal governance).
- §1 Reference Standards — reorganised into four categories (external airworthiness, equipment MOPS, service definition documents, internal governance).
- §2 renamed to "PNT Source Characterisation and Operational Credit" — engineering parameters separated from certification claims; explicit creditable/non-creditable/informative columns.
- §3 renamed to "SBAS Airborne Compliance and Approval Path" — restructured around external regulatory pathway with internal evidence mapping.
- §5 EGNOS SoL — clarified relationship between regulatory and programme equipment requirements.
- §6 Galileo Supplemental Services — OS, OSNMA and HAS explicitly marked non-creditable unless separately approved.
- §7 CCTLS tokens — added `claim_class` field (INTERNAL_ONLY, CREDITABLE_CANDIDATE, NON_CREDITABLE) to all 16 tokens.
- §7.3 Evidence — EV-005 now links to `METHOD-P040-GNS-RAIM-001` (internal method token) instead of external HAZARD reference.
- §7.5 DOA activation policy — now includes EV-006 as required evidence.
- §8 Limits of Use — rewritten with governance-aware language.
- §12 Glossary — added governance note on ESSA and definitions for creditable/non-creditable/internal-only.
- Version bumped to 0.2.0; YAML manifest aligned.

## [0.1.0] — 2026-02-27

### Added

- Initial specification — EGNOS/Galileo onboarding into UTS domain 010.
- Signal-in-Space (SIS) performance bounds (§2).
- SBAS / augmentation certification pathway DO-229F / ED-259 (§3).
- Dual-constellation interoperability requirements GPS + Galileo (§4).
- EGNOS Safety-of-Life (SoL) service requirements (§5).
- Galileo Open Service (OS) and High Accuracy Service (HAS) requirements (§6).
- CCTLS token manifest with 15 tokens across phases P010–P120 (§7).
- Minimum evidence package — 8 evidence items (§7.2).
- Operational Limits of Use LoU-010-GNS-001 through LoU-010-GNS-007 (§8).
- Roles & responsibilities matrix (§9).
- Glossary of 90+ acronyms and 8 key terms (§12).
