# DOA Sign-off Checklist — GNS-010

> **Token:** `DOA_SIGN-P050-GNS-010-001`
> **Artefact:** GNS-010 — EGNOS & Galileo Integration Specification
> **Status:** DRAFT

**Note:** this checklist governs the internal design sign-off only. It does not replace competent-authority approval or external certification processes.

---

## Gate Check — Prerequisites for CONFIRMED Status

The following conditions must all be satisfied before `DOA_SIGN-P050-GNS-010-001` may transition from DRAFT to CONFIRMED.

### Token Dependencies

- [ ] `SIM_RUN-P040-GNS-RAIM-AVAIL-001` — RAIM availability simulation complete and linked
- [ ] `VALIDATION_CASE-P040-GNS-LPV200-001` — LPV-200 validation case complete and linked
- [ ] `VALIDATION_CASE-P040-GNS-HAS-001` — HAS convergence validation case complete and linked
- [ ] `COMPLIANCE_ITEM-P050-DO229F-001` — DO-229F compliance CONFIRMED or ACTIVATED
- [ ] `COMPLIANCE_ITEM-P050-ED259-001` — DFMC / equivalent compliance CONFIRMED or ACTIVATED
- [ ] All FINDING tokens under GNS-010 — status CLOSED

### Evidence Package

- [ ] `GNS-010-EV-001` — PNT Source Characterisation Report accepted
- [ ] `GNS-010-EV-002` — SBAS Receiver Qualification Report — applicable requirements dispositioned
- [ ] `GNS-010-EV-003` — Antenna Qualification Record — EMI/EMC and performance within declared limits
- [ ] `GNS-010-EV-004` — System Integration Test Matrix — all applicable cases executed and dispositioned
- [ ] `GNS-010-EV-005` — GNSS FMEA / Integrity Analysis Report — failure modes, monitoring and reversion logic covered
- [ ] `GNS-010-EV-006` — SoL Pre-flight Service Status Procedure — protocol documented and validated
- [ ] `GNS-010-EV-007` — HAS Convergence Validation Report — convergence criteria and fallback logic validated
- [ ] `GNS-010-EV-008` — OSNMA Integration & Cyber Test Report — authentication handling and spoof-resilience verified

### Operational Approval

- [ ] `TEST_CAMPAIGN-P070-EGNOS-SoL-001` — validation campaign complete
- [ ] `TRAFFIC_CLEARANCE-P090-EGNOS-OPS-001` — external operational approval reference obtained

---

## Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| DOA Authority (internal design approval role) | ___________________ | __________ | ___________________ |
| GNC Specialist | ___________________ | __________ | ___________________ |
| Mission Systems Engineer | ___________________ | __________ | ___________________ |
