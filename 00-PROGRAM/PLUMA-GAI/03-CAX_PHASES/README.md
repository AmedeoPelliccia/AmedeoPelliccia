# 03-CAX_PHASES/README.md
# PLUMA-GAI CAX Phase Artefacts
#
# This directory holds computer-aided processing (CAX) run manifests
# linked from gating conditions defined in pluma-gai.yaml.
#
# Each run manifest records toolchain provenance for a specific gating
# condition, ensuring deterministic traceability from analysis tool to
# certification evidence (INV-GAI-002).
#
# Manifest fields:
#
#   gate_id        : gating condition ID from pluma-gai.yaml §9
#   phase          : PLUMA-GAI phase (P000–P110)
#   tool           : CAX tool name and version
#   input_hash     : SHA3-512 hash of analysis input data
#   output_hash    : SHA3-512 hash of analysis output report
#   timestamp      : ISO-8601 execution timestamp (UTC)
#   operator       : engineer or automated agent identifier
#   status         : open | submitted | accepted | rejected
#
# Example manifest entry:
#
#   - gate_id: GAI-SC-LH2-001
#     phase: P020
#     tool: "ABAQUS 2025.1"
#     input_hash: "sha3-512:..."
#     output_hash: "sha3-512:..."
#     timestamp: "2026-03-01T10:00:00Z"
#     operator: "engineer@ampel360.eu"
#     status: open
#
# Naming convention: <gate_id>-run-manifest.yaml
#   e.g. GAI-SC-LH2-001-run-manifest.yaml
#
# Active gating conditions requiring CAX manifests (from pluma-gai.yaml):
#
#   GAI-SC-LH2-001  LH2 tank structural integrity (FEM / crash test)      P020
#   GAI-SC-LH2-002  LH2 leak detection and isolation (FMEA / test)        P020
#   GAI-SC-RSP-001  RSP TPS software supervision (thermal model)          P020
#   GAI-SC-RSP-002  RSP abort decision tree (Monte Carlo / HIL)           P030
#   GAI-AA-UAS-001  GAIA UAS swarm autonomy (AA-093 assurance case)       P080
#   GAI-QC-001      GAIA quantum-classical bridge determinism (bench)     P060
