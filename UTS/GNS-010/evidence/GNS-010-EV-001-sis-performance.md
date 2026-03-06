# GNS-010-EV-001 — Signal-In-Space (SIS) Performance Report

*Evidence of GNSS Signal-In-Space performance for UTS domain 010 (Mission Systems), covering Galileo Open Service and EGNOS SBAS overlay.*

---

| Metadata          | Value                                                                       |
| ----------------- | --------------------------------------------------------------------------- |
| Evidence ID       | GNS-010-EV-001                                                              |
| Title             | SIS Performance Report                                                      |
| Artefact          | GNS-010                                                                     |
| UTS Domain        | 010 — Mission Systems                                                       |
| CCTLS Phase       | P070 — Flight Tests (CERT)                                                  |
| Version           | 1.0.0                                                                       |
| Status            | DRAFT                                                                       |
| Author            | Amedeo Pelliccia                                                            |
| Machine-readable  | [`GNS-010-EV-001-sis-performance.yaml`](GNS-010-EV-001-sis-performance.yaml) |
| Date              | 2026-02-27                                                                  |

---

## 1. Purpose

This evidence document demonstrates compliance of the GNSS Signal-In-Space (SIS) performance with the requirements applicable to Mission Systems under UTS domain 010.  It covers the four canonical GNSS performance dimensions:

1. **Accuracy** — position and timing error bounds,
2. **Availability** — fraction of time the service is usable,
3. **Continuity** — probability that the service continues without interruption,
4. **Integrity** — ability to provide timely warnings of unusable navigation information.

---

## 2. Applicable Specifications

| Document                        | Reference                         | Role                          |
| ------------------------------- | --------------------------------- | ----------------------------- |
| Galileo OS SIS ICD              | EUSPA-SDD-0026                    | Signal definition & ranging   |
| Galileo OS SDD                  | EUSPA-SDD-0014                    | Service-level performance spec|
| EGNOS SDD                       | EUSPA-SDD-0008                    | SBAS augmentation spec        |
| ICAO Annex 10 Vol I             | §3.7 — GNSS                       | ICAO SARPs for GNSS           |
| EUROCAE ED-259                  | GNSS-based positioning systems    | System performance standard   |
| RTCA DO-229                     | MOPS for GNSS receiving equipment | Receiver minimum requirements |
| EASA AMC 20-28                  | Airborne GNSS Receivers           | Acceptable Means of Compliance|

---

## 3. Performance Evidence

### 3.1 Accuracy

| Metric                  | Requirement         | Measured / Claimed      | Compliance |
| ----------------------- | ------------------- | ----------------------- | ---------- |
| Horizontal position (95%) | ≤ 4 m (Galileo OS) | ≤ 3.2 m               | ✔ PASS     |
| Vertical position (95%) | ≤ 8 m (Galileo OS)  | ≤ 6.5 m               | ✔ PASS     |
| Timing accuracy (95%)   | ≤ 30 ns             | ≤ 24 ns               | ✔ PASS     |

> Values are representative targets to be replaced with measured campaign data at activation.

### 3.2 Availability

| Service              | Requirement | Claimed  | Period           | Compliance |
| -------------------- | ----------- | -------- | ---------------- | ---------- |
| Galileo OS (single-freq) | ≥ 99.5 % | ≥ 99.7 % | 12-month average | ✔ PASS     |
| EGNOS (LPV-200)      | ≥ 99.0 %    | ≥ 99.3 % | 12-month average | ✔ PASS     |

### 3.3 Continuity

| Service              | Requirement              | Claimed               | Compliance |
| -------------------- | ------------------------ | --------------------- | ---------- |
| Galileo OS           | ≥ 99.979 % / 15 s        | ≥ 99.985 % / 15 s    | ✔ PASS     |
| EGNOS (LPV-200)      | ≥ 1 − 8 × 10⁻⁶ / 15 s  | ≥ 1 − 5 × 10⁻⁶ / 15 s | ✔ PASS  |

### 3.4 Integrity

| Metric              | Requirement                    | Claimed                        | Compliance |
| ------------------- | ------------------------------ | ------------------------------ | ---------- |
| SISA (E1-B/C, 95%)  | ≤ 3.0 m                        | ≤ 2.4 m                       | ✔ PASS     |
| SISMA               | Consistent with SISA bound     | Within SISA declared bound     | ✔ PASS     |
| TTA (alert limit)   | ≤ 6 s (en-route) / ≤ 2 s (APV) | ≤ 5.8 s / ≤ 1.8 s            | ✔ PASS     |
| Integrity Risk      | ≤ 1 × 10⁻⁷ / h (en-route)     | ≤ 6 × 10⁻⁸ / h               | ✔ PASS     |

---

## 4. Measurement Methodology

| Step | Activity                                              | Tool / Method                         |
| ---- | ----------------------------------------------------- | ------------------------------------- |
| 1    | SIS ranging-error data collection                     | Reference receiver network (IGS/MGEX) |
| 2    | SISA/SISMA derivation                                 | Statistical processing per Galileo OS SDD §5 |
| 3    | Availability / continuity computation                 | 12-month sliding window, per ICAO Annex 10 §3.7.3 |
| 4    | Integrity risk assessment                             | Fault tree analysis, per EUROCAE ED-259 §7 |
| 5    | TTA demonstration                                     | Injection test bench (signal-in-the-loop) |

---

## 5. Traceability

```
GNS-010-EV-001 (SIS Performance)
    │
    ├── derives_from: GNS-010-MP-001 (Mission Profile & Trace)
    │
    ├── verifies:     GNS-010-REQ-001 (GNSS SIS Performance Requirements)
    │
    └── supports:     UTS-010 domain certification package
```

---

## 6. Open Items / Limitations

| OI ID        | Description                                               | Status  |
| ------------ | --------------------------------------------------------- | ------- |
| OI-GNS-001   | Replace representative values with actual test campaign results | OPEN |
| OI-GNS-002   | Validate EGNOS LPV-200 continuity at northern European airports | OPEN |
| OI-GNS-003   | Confirm Galileo HAS (High Accuracy Service) overlay compatibility | OPEN |

---

## 7. Conclusion

The GNSS Signal-In-Space performance evidence package (GNS-010-EV-001) demonstrates that the claimed SIS performance bounds for Galileo Open Service and EGNOS SBAS overlay meet or exceed the applicable requirements across all four performance dimensions (accuracy, availability, continuity, integrity).

Open items OI-GNS-001 through OI-GNS-003 must be closed before this evidence token transitions from DRAFT to CONFIRMED status.

---

## Related Artefacts

| File                                                                          | Purpose                                             |
| ----------------------------------------------------------------------------- | --------------------------------------------------- |
| [`GNS-010-EV-001-sis-performance.yaml`](GNS-010-EV-001-sis-performance.yaml) | Machine-readable evidence token                     |
| [`../README.md`](../README.md)                                                | GNS-010 artefact overview                           |
| [`../gns-010-token-manifest.yaml`](../gns-010-token-manifest.yaml)            | CCTLS token manifest                                |
| [`../../uts-taxonomy.yaml`](../../uts-taxonomy.yaml)                          | UTS domain taxonomy — domain 010                    |
