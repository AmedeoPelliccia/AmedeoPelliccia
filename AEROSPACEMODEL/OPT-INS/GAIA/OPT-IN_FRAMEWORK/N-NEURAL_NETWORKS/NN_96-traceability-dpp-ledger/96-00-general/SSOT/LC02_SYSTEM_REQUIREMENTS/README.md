---
# DPP Schema Requirements — KNU-GAIA-DPP-96-REQ-001
# Artifact Class : SSOT
# KNOT           : KNOT-GAIA-DPP-96-001  (DPP schema definition)
# KNU            : KNU-GAIA-DPP-96-REQ-001
# Acceptance     : DPP schema field set baselined with mandatory/optional classification
# Verification   : Review
# Owner          : STK_SE
# Status         : BASELINED
# Baseline Date  : 2026-04-15
# Regulatory Ref : EU ESPR (Ecodesign for Sustainable Products Regulation)
# Internal Ref   : AMPEL360-ARCH-SPEC §12 (Circular axis — DPP requirements)

schema:
  name: "GAIA-DPP-SCHEMA"
  version: "1.0.0"
  uri_pattern: "aggix://gaia/nn96/dpp/{component_class}/{dpp_id}@{version}"
  obligation_semantics:
    mandatory: "Field MUST be present and non-null in every DPP record"
    optional: "Field MAY be omitted; when present it MUST conform to its type"
    conditional_mandatory: >
      Field is optional by default but becomes mandatory when the condition
      specified in the field's conditional_mandatory property evaluates to true
  description: >
    Canonical data schema for Digital Product Passports covering all GAIA
    component classes.  Each DPP record is an immutable, versioned entry in the
    NN-96 traceability ledger and carries the minimum field set required by EU
    ESPR and GAIA programme governance (KNOT-GAIA-GOV-001).

field_groups:

  # ── 1. Identity & Classification ──────────────────────────────────────
  - group: "identity"
    description: "Unique identification and component classification"
    fields:
      - name: dpp_id
        type: string
        format: "UUID-v4"
        obligation: mandatory
        description: "Globally unique DPP record identifier"

      - name: dpp_version
        type: integer
        obligation: mandatory
        description: "Monotonically increasing version counter (immutable per ledger entry)"

      - name: component_id
        type: string
        obligation: mandatory
        description: "GAIA component part number or assembly identifier"

      - name: component_class
        type: enum
        allowed_values:
          - STRUCTURE
          - MECHANISM
          - AVIONICS
          - ECLSS
          - PROPULSION
          - POWER
          - THERMAL
          - PAYLOAD
          - SOFTWARE
          - COTS
          - RAW_MATERIAL
          - CONSUMABLE
        obligation: mandatory
        description: "Component taxonomy class per GAIA subsystem allocation"

      - name: component_name
        type: string
        obligation: mandatory
        description: "Human-readable component designation"

      - name: serial_number
        type: string
        obligation: mandatory
        description: "Manufacturer serial number or lot identifier"

      - name: batch_lot_id
        type: string
        obligation: optional
        description: "Batch or lot identifier for bulk/consumable items"

  # ── 2. Manufacturer & Supply-Chain ─────────────────────────────────────
  - group: "manufacturer"
    description: "Manufacturer identity and supply-chain provenance"
    fields:
      - name: manufacturer_name
        type: string
        obligation: mandatory
        description: "Legal entity name of the manufacturer"

      - name: manufacturer_id
        type: string
        format: "DUNS or LEI"
        obligation: mandatory
        description: "Standardised manufacturer identifier (DUNS or LEI)"

      - name: manufacturing_site
        type: string
        obligation: mandatory
        description: "Facility location (city, country, site code)"

      - name: manufacturing_date
        type: date
        format: "ISO-8601"
        obligation: mandatory
        description: "Date of manufacture completion"

      - name: supplier_chain
        type: array
        items: { type: object, ref: "#/definitions/supplier_entry" }
        obligation: optional
        description: "Ordered list of tier-N suppliers contributing to this component"

  # ── 3. Material Composition ────────────────────────────────────────────
  - group: "material_composition"
    description: "Bill of materials and substance declarations"
    fields:
      - name: primary_material
        type: string
        obligation: mandatory
        description: "Dominant material (e.g., Ti-6Al-4V, CFRP T800)"

      - name: material_certificates
        type: array
        items: { type: string, format: "URI" }
        obligation: mandatory
        description: "References to mill/batch material test certificates"

      - name: substance_declarations
        type: array
        items: { type: object, ref: "#/definitions/substance_entry" }
        obligation: mandatory
        description: "REACH/RoHS substance-of-concern declarations"

      - name: recycled_content_pct
        type: number
        unit: "%"
        obligation: optional
        description: "Percentage of recycled content by mass"

      - name: critical_raw_materials
        type: array
        items: { type: string }
        obligation: optional
        description: "EU CRM list substances present in the component"

  # ── 4. Compliance & Regulatory ─────────────────────────────────────────
  - group: "compliance"
    description: "Regulatory compliance and export-control classification"
    fields:
      - name: regulatory_framework
        type: array
        items: { type: string }
        obligation: mandatory
        description: "Applicable regulatory frameworks (e.g., EU-ESPR, EASA-P21G)"

      - name: export_control_class
        type: enum
        allowed_values:
          - UNRESTRICTED
          - EAR99
          - ITAR_CAT_IV
          - ITAR_CAT_XV
          - DUAL_USE
        obligation: mandatory
        description: "Export-control classification per ITAR/EAR"

      - name: conformity_declarations
        type: array
        items: { type: string, format: "URI" }
        obligation: mandatory
        description: "URIs of conformity/certification documents"

      - name: itar_marking
        type: string
        obligation: optional
        description: "ITAR distribution statement when export_control_class ∈ {ITAR_CAT_IV, ITAR_CAT_XV}"
        conditional_mandatory: "export_control_class in [ITAR_CAT_IV, ITAR_CAT_XV]"

  # ── 5. Lifecycle Status ────────────────────────────────────────────────
  - group: "lifecycle"
    description: "Current lifecycle state and event linkage"
    fields:
      - name: lifecycle_phase
        type: enum
        allowed_values:
          - DESIGN
          - PRODUCTION
          - INSPECTION
          - INTEGRATION
          - OPERATIONAL
          - MAINTENANCE
          - DECOMMISSION
          - RECYCLED
        obligation: mandatory
        description: "Current lifecycle phase of the component"

      - name: installation_date
        type: date
        format: "ISO-8601"
        obligation: optional
        description: "Date of installation into parent assembly"

      - name: operational_hours
        type: number
        unit: "hours"
        obligation: optional
        description: "Cumulative operational hours at last ledger update"

      - name: lifecycle_events
        type: array
        items: { type: string, format: "URI" }
        obligation: optional
        description: "Ordered references to lifecycle event records (see KNU-GAIA-DPP-96-REQ-004)"

  # ── 6. Environmental & Circularity ─────────────────────────────────────
  - group: "environmental"
    description: "Environmental impact and end-of-life circularity data"
    fields:
      - name: carbon_footprint_kg_co2e
        type: number
        unit: "kg CO₂e"
        obligation: mandatory
        description: "Cradle-to-gate carbon footprint"

      - name: energy_consumption_kwh
        type: number
        unit: "kWh"
        obligation: optional
        description: "Total energy consumed in manufacturing"

      - name: recyclability_score
        type: number
        unit: "%"
        obligation: optional
        description: "Estimated mass-percentage recoverable at end-of-life"

      - name: disposal_instructions
        type: string
        obligation: optional
        description: "End-of-life handling and disposal guidance"

      - name: circularity_passport_ref
        type: string
        format: "URI"
        obligation: optional
        description: "Link to LC14_RETIREMENT_CIRCULARITY closure record"

  # ── 7. Provenance & Integrity ──────────────────────────────────────────
  - group: "provenance"
    description: "Ledger integrity and provenance chain anchoring"
    fields:
      - name: ledger_entry_hash
        type: string
        format: "SHA-256"
        obligation: mandatory
        description: "SHA-256 hash of this DPP record for ledger integrity verification"

      - name: previous_entry_hash
        type: string
        format: "SHA-256"
        obligation: mandatory
        description: "Hash of the preceding ledger entry (append-only chain link)"

      - name: created_timestamp
        type: datetime
        format: "ISO-8601"
        obligation: mandatory
        description: "UTC timestamp of DPP record creation"

      - name: created_by
        type: string
        obligation: mandatory
        description: "Identity (user or system) that created this record"

      - name: digital_signature
        type: string
        format: "base64"
        obligation: optional
        description: "Cryptographic signature over the record payload"

      - name: parent_assembly_dpp
        type: string
        format: "URI"
        obligation: optional
        description: "AGGIX URI of the parent assembly DPP for roll-up traceability"

# ── Shared Definitions ─────────────────────────────────────────────────
definitions:
  supplier_entry:
    type: object
    fields:
      - name: supplier_name
        type: string
        obligation: mandatory
      - name: supplier_id
        type: string
        format: "DUNS or LEI"
        obligation: mandatory
      - name: tier
        type: integer
        obligation: mandatory
        description: "Supply-chain tier (1 = direct supplier)"

  substance_entry:
    type: object
    fields:
      - name: substance_name
        type: string
        obligation: mandatory
      - name: cas_number
        type: string
        obligation: mandatory
        description: "CAS Registry Number"
      - name: concentration_pct
        type: number
        unit: "%"
        obligation: mandatory
      - name: svhc
        type: boolean
        obligation: mandatory
        description: "Substance of Very High Concern flag (REACH Art. 57)"

# ── Summary Statistics ──────────────────────────────────────────────────
summary:
  total_fields: 36
  mandatory_fields: 22
  optional_fields: 14
  conditional_mandatory_fields: 1
  field_groups: 7
  definition_sub_fields: 7
---

# LC02 — System Requirements (NN-96 Traceability / DPP / Ledger · 96-00-general)

System-level requirements for **NN_96 Traceability / Digital Product Passport / Ledger** within the GAIA programme.

## Scope

This lifecycle-phase folder captures baselined requirements for:

- DPP canonical data schema and field set (mandatory / optional classification)
- Ledger throughput, latency, and data-integrity requirements
- Component provenance data-capture points and mandatory attestation fields
- Cross-domain API contract requirements traced to the AGGIX URI scheme

## Files

| File | KNU | Description |
|------|-----|-------------|
| `DPP_SCHEMA_REQUIREMENTS.yaml` | KNU-GAIA-DPP-96-REQ-001 | DPP schema field set with mandatory/optional classification — primary deliverable for KNOT-GAIA-DPP-96-001 |

## Traceability

| KNU ID | KNOT | Acceptance Criteria | Status |
|--------|------|---------------------|--------|
| KNU-GAIA-DPP-96-REQ-001 | KNOT-GAIA-DPP-96-001 | DPP schema field set baselined with mandatory/optional classification | BASELINED |
| KNU-GAIA-DPP-96-REQ-002 | KNOT-GAIA-DPP-96-002 | Ledger throughput latency and integrity requirements specified | PLANNED |
| KNU-GAIA-DPP-96-REQ-003 | KNOT-GAIA-DPP-96-003 | Provenance data capture points and mandatory attestation fields specified | PLANNED |
| KNU-GAIA-DPP-96-REQ-004 | KNOT-GAIA-DPP-96-005 | API contract requirements traced to AGGIX URI scheme and subsystem manifest | PLANNED |

## Dependencies

| Direction | Target | Rationale |
|-----------|--------|-----------|
| Up | LC01_PROBLEM_STATEMENT | Problem scope and KNOT definitions |
| Up | KNOT-GAIA-GOV-001 | Governance framework sets DPP mandatory fields |
| Down | LC04_DESIGN_DEFINITION | Requirements flow down to design |
| Down | LC06_VERIFICATION | Requirements are verified against test procedures |
| Across | LC03_SAFETY_RELIABILITY | Safety-critical fields feed FMEA |
| External | EU ESPR Regulation | Digital Product Passport regulatory baseline |
| External | ITAR/EAR | Export-control classification overlay |
