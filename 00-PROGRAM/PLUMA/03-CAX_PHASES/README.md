# 03-CAX_PHASES/README.md
# CAx Phase Artifacts
#
# This directory holds toolchain provenance artifacts referenced by
# run_manifest_ref in gating conditions (simplex-contract.yaml §5).
#
# Each run manifest links a gating condition to:
#   - The analysis/test tool used
#   - Input data hash
#   - Output report hash
#   - Execution timestamp
#   - Operator/engineer ID
#
# Example manifest entry:
#
#   - gate_id: SC-LH2-001
#     tool: ABAQUS 2025.1
#     input_hash: sha256:abc123...
#     output_hash: sha256:def456...
#     timestamp: "2026-03-01T10:00:00Z"
#     operator: engineer@ampel360.eu
