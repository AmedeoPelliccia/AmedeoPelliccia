# DOA Sign-off Checklist — GNS-010

> **Token:** `DOA_SIGN-P050-GNS-010-001`
> **Artefact:** GNS-010 — EGNOS & Galileo Integration Specification
> **Status:** DRAFT

---

## Gate Check — Prerequisites for CONFIRMED Status

The following conditions must all be satisfied before `DOA_SIGN-P050-GNS-010-001` may transition from DRAFT to CONFIRMED.

### Token Dependencies

- [ ] `SIM_RUN-P040-GNS-RAIM-AVAIL-001` — RAIM availability simulation complete and linked
- [ ] `VALIDATION_CASE-P040-GNS-LPV200-001` — LPV-200 validation case complete and linked
- [ ] `VALIDATION_CASE-P040-GNS-HAS-001` — HAS convergence validation case complete and linked
- [ ] `COMPLIANCE_ITEM-P050-DO229F-001` — DO-229F compliance CONFIRMED or ACTIVATED
- [ ] `COMPLIANCE_ITEM-P050-ED259-001` — ED-259 compliance CONFIRMED or ACTIVATED
- [ ] All FINDING tokens under GNS-010 — status CLOSED

### Evidence Package

- [ ] `GNS-010-EV-001` — SIS Performance Measurement Report accepted
- [ ] `GNS-010-EV-002` — SBAS Receiver Qualification Report (DO-229F) — all MOPS PASS
- [ ] `GNS-010-EV-003` — Antenna Qualification Record (DO-316) — EMI/EMC PASS
- [ ] `GNS-010-EV-004` — System Integration Test Matrix — all test cases PASS
- [ ] `GNS-010-EV-005` — GNSS FMEA / RAIM Analysis Report — all failure modes covered
- [ ] `GNS-010-EV-006` — SoL Pre-flight Availability Procedure — validated
- [ ] `GNS-010-EV-007` — HAS Convergence Validation Report — convergence ≤ 300 s
- [ ] `GNS-010-EV-008` — OSNMA Integration & Cyber Test Report — auth latency ≤ 30 s

### Operational Approval

- [ ] `TEST_CAMPAIGN-P070-EGNOS-SoL-001` — flight test campaign complete
- [ ] `TRAFFIC_CLEARANCE-P090-EGNOS-OPS-001` — operational approval obtained

---

## Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| DOA Authority | ___________________ | __________ | ___________________ |
| GNC Specialist | ___________________ | __________ | ___________________ |
| Mission Systems Engineer | ___________________ | __________ | ___________________ |
