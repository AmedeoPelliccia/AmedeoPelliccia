# CT — Continuous Testing

Phase output from the C-GROWTH lifecycle for `certified_dynamics.py`.

## Test Run

- **Module**: `certified_dynamics.py` (simulation + certification + audit)
- **Visualization**: `plot_dynamics.py` (trajectory plot + compliance summary)
- **Scenario**: Urban Air Mobility — eVTOL noise compliance (CS-23)
- **Result**: 3/3 evaluations FULLY_ADMISSIBLE (100% compliance rate)

## Generated Artifacts

| File                       | Description                                              |
|----------------------------|----------------------------------------------------------|
| `audit_log.json`           | Full audit trail with ISO timestamps and state vectors   |
| `evidence_gates.json`      | Evidence gate registry with fulfillment status and URIs  |
| `compliance_summary.json`  | Executive summary: compliance rate, status distribution  |
| `noise_compliance_plot.png`| 2D trajectory chart: state vs. regulatory boundary       |

## Reproducing

```bash
cd <repo_root>
python certified_dynamics.py   # → audit_log.json, evidence_gates.json
python plot_dynamics.py        # → noise_compliance_plot.png, compliance_summary.json
```
