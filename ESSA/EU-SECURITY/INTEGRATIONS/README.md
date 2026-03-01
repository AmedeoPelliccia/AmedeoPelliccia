# EU-SECURITY — INTEGRATIONS

**Integration Registry: EU-SECURITY Controls ↔ CIVIL-PLATFORMS Token Packages**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-SEC-INT-001 |
| **Version** | v0.1-draft |
| **Status** | Draft |
| **Parent** | ESSA-SEC-MCSC-001 |

---

## Purpose

This directory contains integration artefacts that formally link EU-SECURITY MCSC controls to CIVIL-PLATFORMS (CCTLS) token packages.

Each integration artefact specifies:

- Which CCTLS packages are affected
- Which MCSC controls apply
- The linkage pattern (mandatory or conditional)
- Evidence requirements for ALPC certification

---

## Integration Index

| ID | CCTLS Package(s) | MCSC Controls | Linkage | Description |
|----|-----------------|---------------|---------|-------------|
| INT-001 | PKG-P020-* | MCSC-ETH-03, MCSC-RES-01 | Mandatory | Safety envelope tokens must reference non-maleficence and resilience controls |
| INT-002 | PKG-P050-DOA-SIGNOFF | MCSC-ACC-02, MCSC-ETH-01 | Mandatory | DOA sign-off must carry authority trace and approval |
| INT-003 | PKG-P080-OCCURRENCE | MCSC-ACC-03 | Mandatory | Occurrence reports must link to root cause closure |
| INT-004 | PKG-P030-SUPPLY, PKG-P030-TRACE-HOOKS | MCSC-SCI-01, MCSC-SCI-02 | Mandatory | Supply chain nodes require provenance hooks |
| INT-005 | PKG-P090-MISSION-CONTROL | MCSC-HOB-03, MCSC-ETH-02 | Mandatory | Mission activation requires human confirmation and defined override path |
| INT-006 | PKG-P120-CYBER, PKG-P120-RESILIENCE | All MCSC-RES-* | Mandatory | Cyber/resilience packages must cover all resilience controls |
| INT-007 | All packages | MCSC-ETH-04 | Mandatory | All transitions must be written to MTLdg |
| INT-008 | PKG-P060-PRODUCT-CONFORMITY | MCSC-SCI-03 | Mandatory | Third-party components require conformity declaration before ACTIVATE |

---

## Related Artefacts

| File | Purpose |
|------|---------|
| [`../README.md`](../README.md) | EU-SECURITY branch — Minimum Common Security Constitution |
| [`../../README.md`](../../README.md) | ESSA Constitutional Root Document |
| [`../../cctls.yaml`](../../cctls.yaml) | CCTLS lifecycle standard |
