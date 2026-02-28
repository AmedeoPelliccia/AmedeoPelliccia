# GNS-010 — Mission Systems: GNSS / Navigation Artefact

*UTS domain-010 token artefact covering navigation, guidance and signal-in-space performance for EGNOS and Galileo integration.*

---

| Metadata         | Value                                                                 |
| ---------------- | --------------------------------------------------------------------- |
| Artefact ID      | GNS-010                                                               |
| UTS Domain       | 010 — Mission Systems                                                 |
| Version          | 1.0.0                                                                 |
| Status           | DRAFT                                                                 |
| Author           | Amedeo Pelliccia                                                      |
| Machine-readable | [`gns-010-token-manifest.yaml`](gns-010-token-manifest.yaml)         |
| Parent standard  | EACST-STD-CCTLS-001                                                   |
| Cross-references | UTS/README.md · UTS/uts-taxonomy.yaml · EACST/cctls.yaml             |

---

## 1. Purpose

This artefact captures the **Mission Systems** token package for the Universal Transport System (UTS) domain **010**.  It governs the navigation, guidance and control (GNC) evidence produced during certification and operational phases, with particular focus on:

- **GNSS signal-in-space (SIS) performance** for Galileo and EGNOS,
- mission profile traceability,
- real-time sensor integration validation.

---

## 2. Scope

| Aspect              | Detail                                                                         |
| ------------------- | ------------------------------------------------------------------------------ |
| **Systems covered** | GNSS receivers, INS/GNSS integration, EGNOS SBAS overlay, Galileo OS/CS/HAS   |
| **Performance axes**| Accuracy · Availability · Continuity · Integrity (SISA/SISMA)                 |
| **Lifecycle phases**| P040 (Simulation & DMU) · P070 (Flight Tests / Cert) · P090 (Mission Ops)     |
| **Regulatory hooks**| ICAO Annex 10 · EUROCAE ED-259 · RTCA DO-229 · EASA AMC 20-28                |

---

## 3. Evidence Registry

| Evidence ID            | Title                              | Phase | Status |
| ---------------------- | ---------------------------------- | ----- | ------ |
| GNS-010-EV-001         | SIS Performance Report             | P070  | DRAFT  |

Full evidence files are in [`evidence/`](evidence/).

---

## 4. Token Manifest Summary

The machine-readable token manifest ([`gns-010-token-manifest.yaml`](gns-010-token-manifest.yaml)) contains:

- artefact identity and CCTLS bindings,
- phase and package assignments,
- evidence token registry,
- validation links to EACST-STD-CCTLS-001.

---

## 5. Key Terms (UTS-010)

| Term            | Definition                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------- |
| **SIS**         | Signal In Space — the navigation signal broadcast from satellite to user equipment            |
| **SISA**        | Signal-In-Space Accuracy — statistical bound on the SIS ranging error                        |
| **SISMA**       | Signal-In-Space Monitoring Accuracy — accuracy of the integrity monitoring residual          |
| **EGNOS**       | European Geostationary Navigation Overlay Service — SBAS augmentation over Europe            |
| **Galileo OS**  | Galileo Open Service — free-to-air civil navigation signal (E1/E5a/E5b/E6)                   |
| **TTA**         | Time To Alert — maximum elapsed time before an out-of-tolerance alert is broadcast           |
| **HPL / VPL**   | Horizontal / Vertical Protection Level — integrity bound computed by the receiver            |
| **GNC**         | Guidance, Navigation and Control                                                              |

---

## 6. Operational Limits

- Navigation evidence is valid within the EGNOS service area (ECAC + adjacent regions) unless explicitly extended.
- SIS performance claims are referenced to the Galileo/EGNOS SDD and SiSPer published by EUSPA.
- Any deviation from the stated accuracy / integrity budget requires a separate safety assessment (UTS-000).

---

## Related Artefacts

| File                                                                         | Purpose                                              |
| ---------------------------------------------------------------------------- | ---------------------------------------------------- |
| [`gns-010-token-manifest.yaml`](gns-010-token-manifest.yaml)                 | Machine-readable token manifest (CCTLS)              |
| [`evidence/GNS-010-EV-001-sis-performance.md`](evidence/GNS-010-EV-001-sis-performance.md) | SIS Performance Evidence (human-readable)   |
| [`evidence/GNS-010-EV-001-sis-performance.yaml`](evidence/GNS-010-EV-001-sis-performance.yaml) | SIS Performance Evidence (machine-readable) |
| [`../../UTS/uts-taxonomy.yaml`](../uts-taxonomy.yaml)                        | UTS domain taxonomy — domain 010 definition          |
| [`../../EACST/cctls.yaml`](../../EACST/cctls.yaml)                           | CCTLS lifecycle standard                             |
