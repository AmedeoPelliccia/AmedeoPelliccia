# ESSA — Universal Form, Adaptive Technical Organization (UFATO)

**A Common Representation Framework with Technology-Specific Structural Flexibility**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-STD-UFATO-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Standard |
| **Parent** | ESSA-STD-CCTLS-001 ([CCTLS.md](CCTLS.md)) |
| **Companion** | [`ufato.yaml`](ufato.yaml) |
| **Related** | [`SAFETY-FIRST.md`](SAFETY-FIRST.md) · [`IPSN.md`](IPSN.md) · [`AMPEL360-ARCH-SPEC.md`](AMPEL360-ARCH-SPEC.md) |
| **Last Updated** | 2026-04-14 |

---

## 0. Preamble

Technical publications for aviation should not be rigid in the wrong place.

What **must** be universal is the way information is written and represented:
clear authoring rules, controlled terminology, safety semantics, visual hierarchy,
illustration conventions, colours, lines, icons, readability, and interaction logic.

What **must** remain adaptable is the technical chaptering and content structure
according to the technology involved: conventional aircraft, hydrogen systems,
fuel cells, high-voltage architectures, advanced sensing, AI-assisted systems,
and future configurations will not all fit naturally into the exact same
documentary decomposition.

UFATO defines the boundary between these two concerns.

---

## 1. Core Principle

> **Universal form. Adaptive technical organisation.**

Strong standardisation where cognitive consistency and safety matter most.
Controlled flexibility where engineering reality demands it.

This improves readability, interoperability, training efficiency, and reduces
the risk of interpretation errors across OEMs, suppliers, operators, and MRO
environments.

---

## 2. Scope and Applicability

UFATO governs the production of **Interactive Electronic Technical Publications
(IETPs)** and their source artefacts across all technology domains tracked by
ESSA, including but not limited to:

| Technology Domain | Exemplary Content |
|-------------------|-------------------|
| Conventional Aircraft | ATA 100 / iSpec 2200 chapters, AMM, IPC, WDM |
| Hydrogen Systems (LH₂) | Cryogenic storage, venting, refuelling procedures |
| PEM / SOFC Fuel Cells | Stack maintenance, MEA replacement, coolant loops |
| High-Voltage Architecture | HV bus isolation, arc-flash safety, battery management |
| Advanced Sensing & Avionics | LiDAR calibration, sensor fusion validation |
| AI-Assisted Systems | Model cards, decision-boundary documentation, XAI audit records |
| Autonomous / UAS | Remote-pilot procedures, detect-and-avoid calibration |
| Reusable Space Platforms | Turnaround inspections, thermal protection system refurbishment |

Applicability is controlled through the **AGGIX Publication (PUB)** resource
type and the AMPEL360 profile axis `technology_domain`.

---

## 3. Architecture: Two Layers

UFATO separates the publication system into two formally distinct layers:

```
┌──────────────────────────────────────────────────────────────────┐
│                  LAYER 1 — UNIVERSAL FORM                       │
│  (invariant across all technology domains)                      │
│                                                                  │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────────┐  │
│  │ Authoring  │ │ Terminology│ │ Safety     │ │ Visual &     │  │
│  │ Rules      │ │ Control    │ │ Semantics  │ │ Interaction  │  │
│  └────────────┘ └────────────┘ └────────────┘ └──────────────┘  │
├──────────────────────────────────────────────────────────────────┤
│                  LAYER 2 — ADAPTIVE STRUCTURE                   │
│  (technology-domain-specific chaptering)                         │
│                                                                  │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌──────────────┐  │
│  │ Chapter    │ │ Data Module│ │ Cross-ref  │ │ Technology   │  │
│  │ Schemes    │ │ Codes      │ │ Topology   │ │ Extensions   │  │
│  └────────────┘ └────────────┘ └────────────┘ └──────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

**Invariant:** Layer 1 rules are never overridden by Layer 2 choices.

---

## 4. Layer 1 — Universal Form (Normative)

Layer 1 establishes the **cognitive contract** between the publication and
every human reader. It is invariant across all technology domains.

### 4.1 Authoring Rules

| Rule ID | Rule | Rationale |
|---------|------|-----------|
| UF-AR-01 | One instruction per sentence. | Reduces ambiguity under stress. |
| UF-AR-02 | Active voice, imperative mood for procedural steps. | Unambiguous actor/action assignment. |
| UF-AR-03 | Sentences ≤ 25 words (target); ≤ 30 words (hard limit). | Cognitive load control (MIL-STD-38784). |
| UF-AR-04 | No nested conditionals beyond two levels. | Prevents decision-tree overload. |
| UF-AR-05 | Controlled vocabulary per BREX dictionary. | Eliminates synonym drift. |
| UF-AR-06 | Warnings / Cautions / Notes in strict precedence order before the step they govern. | Aligns with S1000D Issue 5+ and ATA conventions. |

### 4.2 Controlled Terminology

| Rule ID | Rule |
|---------|------|
| UF-CT-01 | Each concept has exactly one approved term within a given BREX scope. |
| UF-CT-02 | Abbreviations are expanded on first use per data module. |
| UF-CT-03 | Units follow SI with aviation-conventional exceptions (ft, kts, NM) explicitly declared. |
| UF-CT-04 | Technology-domain-specific terms are registered in a domain glossary extension (Layer 2) but rendered using Layer 1 formatting rules. |

### 4.3 Safety Semantics

Safety-related information follows a strict semantic hierarchy:

| Severity | Keyword | Colour (display) | Icon | Condition |
|----------|---------|-------------------|------|-----------|
| **Danger** | DANGER | Red (#CC0000 on white) | ▲ solid | Immediate risk of death or catastrophic damage |
| **Warning** | WARNING | Orange (#E65100 on white) | ▲ outline | Potential risk of death or serious injury |
| **Caution** | CAUTION | Yellow (#F9A825 on white) | ◆ | Risk of equipment damage or degraded function |
| **Note** | NOTE | Blue (#1565C0 on white) | ℹ | Supplementary information aiding correct execution |

These four levels are **invariant**. Technology-domain extensions may **not**
add, remove, or reorder safety severity levels.

### 4.4 Visual Hierarchy and Display Rules

| Rule ID | Rule |
|---------|------|
| UF-VH-01 | Heading levels map 1:1 to document structure depth (H1 = publication title, H2 = chapter, H3 = section, H4 = sub-section). |
| UF-VH-02 | Step numbering is continuous Arabic within each procedural block. |
| UF-VH-03 | Tables are captioned with `Table [seq] — [title]` above the table. |
| UF-VH-04 | Minimum body text size: 10 pt print / 14 px screen (WCAG AA). |
| UF-VH-05 | Contrast ratio ≥ 4.5:1 for body text, ≥ 3:1 for large text (WCAG 2.1 AA). |
| UF-VH-06 | Night-mode palette is defined per UFATO colour scheme annex. |

### 4.5 Illustration Conventions

| Rule ID | Rule |
|---------|------|
| UF-IC-01 | Line weights: 0.25 mm (detail), 0.5 mm (outline), 1.0 mm (callout leader). |
| UF-IC-02 | Callout numbering follows the item/figure convention of the parent standard (S1000D ICN or ATA figure/item). |
| UF-IC-03 | Colour in illustrations is supplementary; the illustration must be legible in greyscale. |
| UF-IC-04 | Hotspots in IETP displays have a minimum touch target of 44 × 44 px (WCAG 2.5.5). |

### 4.6 Interaction Logic (IETP-Specific)

| Rule ID | Rule |
|---------|------|
| UF-IL-01 | Navigation shall provide breadcrumb trail reflecting the chapter/section hierarchy. |
| UF-IL-02 | Cross-references are always hyperlinked; dead links are a conformance violation. |
| UF-IL-03 | Filtering by applicability (effectivity) never hides safety-critical information. |
| UF-IL-04 | Undo is available for all user-state changes (filter, selection, annotation). |
| UF-IL-05 | Offline mode preserves the full publication baseline loaded at last sync. |

---

## 5. Layer 2 — Adaptive Technical Organisation (Controlled Flexibility)

Layer 2 defines **how content is decomposed into chapters, sections, and data
modules** for a specific technology domain. It provides controlled flexibility
under the constraints of Layer 1.

### 5.1 Governance of Structural Adaptation

| Rule ID | Rule |
|---------|------|
| AS-GOV-01 | Each technology domain declares a **Chapter Scheme** registered in the AGGIX registry under type `CFG`. |
| AS-GOV-02 | A Chapter Scheme must map every chapter to at least one CCTLS lifecycle phase (P000–P120). |
| AS-GOV-03 | A Chapter Scheme must undergo the CCTLS gate sequence: INTERPRET → CONFIRM → ACTIVATE → PUBLISH. |
| AS-GOV-04 | Chapter Schemes are versioned and traceable via AGGIX URI. |
| AS-GOV-05 | Cross-domain chapter references use stable AGGIX URIs, never positional chapter numbers. |

### 5.2 Reference Chapter Schemes

UFATO defines reference Chapter Schemes for the following technology domains.
These are starting points; each programme may refine them through AS-GOV-03.

#### 5.2.1 Conventional Aircraft (ATA-Based)

Follows ATA iSpec 2200 / S1000D SNS mapping. No structural changes required.

#### 5.2.2 Hydrogen Systems (LH₂)

| Chapter | Title | Rationale for Deviation |
|---------|-------|-------------------------|
| 28H | LH₂ Fuel System — Cryogenic Storage | Sub-chapters for tank insulation, boil-off management, cryo-valve maintenance |
| 28V | LH₂ Fuel System — Venting & Inerting | Hydrogen vent-stack procedures; no kerosene equivalent |
| 28R | LH₂ Fuel System — Refuelling Interface | Cryogenic coupling, purge sequences, leak detection |
| 73H | Fuel Cell Power Plant — Stack Assembly | PEM/SOFC stack removal/installation, MEA inspection |
| 73C | Fuel Cell Power Plant — Balance of Plant | Humidifiers, compressors, coolant loops |
| 73E | Fuel Cell Power Plant — Electrical Integration | DC bus coupling, power conditioning, load-sharing logic |

#### 5.2.3 High-Voltage Architecture

| Chapter | Title | Rationale for Deviation |
|---------|-------|-------------------------|
| 24E | Electrical Power — HV Distribution (> 270 VDC) | Arc-flash hazard procedures, HV interlock verification |
| 24B | Electrical Power — Battery Management System | Cell balancing, thermal runaway mitigation, SoH diagnostics |
| 24G | Electrical Power — Ground Power HV Interface | HV ground cart procedures, isolation verification |

#### 5.2.4 AI-Assisted Systems

| Chapter | Title | Rationale for Deviation |
|---------|-------|-------------------------|
| 45A | AI-Assisted System — Model Card & Boundary Doc | Decision-boundary specification, training-data provenance |
| 45X | AI-Assisted System — Explainability Audit | XAI output logs, confidence calibration records |
| 45M | AI-Assisted System — Monitoring & Drift Detection | Operational domain monitoring, retraining triggers |

### 5.3 Domain Glossary Extensions

Each technology domain maintains a **Domain Glossary Extension (DGE)** that:

1. Registers new terms not present in the base BREX dictionary.
2. Follows Layer 1 formatting rules (UF-CT-01 through UF-CT-04).
3. Is versioned alongside the Chapter Scheme.
4. Is traceable via AGGIX URI (`aggix://{domain}/{branch}/{programme}/CFG/DGE-{domain}@{version}`).

---

## 6. Conformance Model

### 6.1 Conformance Levels

| Level | Label | Meaning |
|-------|-------|---------|
| **C1** | Universal-Compliant | Full Layer 1 compliance. Layer 2 uses a registered Chapter Scheme. |
| **C2** | Universal-Compliant, Structure-Pending | Full Layer 1 compliance. Layer 2 Chapter Scheme is in INTERPRET or CONFIRM state. |
| **C3** | Partial | Layer 1 deviations documented and risk-assessed. |

### 6.2 Validation

| Check | Method | Gate |
|-------|--------|------|
| Layer 1 rules (UF-*) | Automated BREX / Schematron validation | CONFIRM |
| Safety semantics (§4.3) | Automated severity-keyword-to-display check | CONFIRM |
| Chapter Scheme registration | AGGIX registry lookup | ACTIVATE |
| Cross-reference integrity | Link-checker (IETP build pipeline) | PUBLISH |
| Accessibility (WCAG AA) | Automated + manual audit | PUBLISH |

---

## 7. Integration Points

### 7.1 With ESSA Governance

| ESSA Artefact | UFATO Binding |
|---------------|---------------|
| CCTLS gate sequence | Chapter Schemes follow INTERPRET → CONFIRM → ACTIVATE → PUBLISH |
| H-Pipeline (H_ENVELOPE) | Safety semantics (§4.3) derive severity rendering from H_ENVELOPE.safety_objective |
| AGGIX registry | Chapter Schemes and DGEs are PUB and CFG resources |
| SPEC-PELS-014 lifecycle | Publication state aligns with PELS engineering/product state pair |

### 7.2 With External Standards

| Standard | Relationship |
|----------|-------------|
| S1000D Issue 5.0+ | Layer 1 rules align with S1000D BREX and presentation rules. Layer 2 Chapter Schemes map to SNS extensions. |
| ATA iSpec 2200 | Conventional-aircraft Chapter Scheme is a direct mapping. |
| DO-178C / DO-330 | AI-Assisted Systems Chapter Scheme (§5.2.4) references model qualification as per DO-330 TQL. |
| WCAG 2.1 AA | Display and interaction rules (§4.4, §4.5, §4.6) enforce WCAG thresholds. |
| MIL-STD-38784 | Authoring rules (§4.1) incorporate readability constraints from MIL-STD-38784. |

---

## 8. What UFATO Is Not

1. **Not a replacement for S1000D or ATA iSpec 2200.** UFATO is a governance
   layer that constrains how these standards are applied and extended.
2. **Not a content authoring tool.** UFATO defines rules; CSDB and IETP
   platforms implement them.
3. **Not a monolithic chapter system.** The entire point is that technology
   domains define their own chapter decomposition under controlled governance.

---

## 9. Revision History

| Version | Date | Change |
|---------|------|--------|
| v0.1-draft | 2026-04-14 | Initial specification. |
