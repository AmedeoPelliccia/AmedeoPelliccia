# AMPELSystem — Configuration Schemas

This directory holds the **schema definitions** for `AMPELSystem` configuration
documents used across the `AIRCRAFTMODEL/AMPEL360-Q100` configurations
(`WTW`, `BWB`).

## Files

| File | Purpose |
|------|---------|
| `ampel-system.schema.json` | JSON Schema (draft 2020-12) — canonical schema. |
| `ampel-system.xsd`         | XML Schema 1.0 — mirror of the JSON Schema for XML serializations. |
| `ampel-system.example.json`| Reference instance that validates against the JSON Schema. |

## Structure

```
AMPELSystem
├── ProjectInfo            (ProjectName, Description, StartDate, EndDate)
├── Mapping                (MapID, MapName, Industry, MapProperties, MappingAlgorithms)
├── Detection              (DetectionID, DetectionName, DetectionProperties, DetectionAlgorithms)
├── CaptureCapsules        (Capsule[]: CapsuleID, CapsuleName, CapsuleProperties, CaptureMechanisms)
├── Technologies           (Technology[]: TechnologyName, Description, IntegrationLevel)
├── Metrics                (Metric[]: MetricName, MetricValue)
├── FinancialBenefits      (Benefit[]: BenefitName, BenefitValue, StakeholderID, ClientID)
├── Stakeholders           (Stakeholder[]: StakeholderID, StakeholderName, StakeholderType, Contribution)
└── PotentialClients       (Client[]: ClientID, ClientName)
```

`Property`, `Algorithm`, and `Mechanism` are reusable record types defined once
in `$defs` (JSON) / global complexTypes (XSD) and referenced from each section
that needs them.

## Validation

JSON Schema (with any draft 2020-12 validator, e.g. `check-jsonschema`):

```bash
check-jsonschema \
  --schemafile AIRCRAFTMODEL/AMPEL360-Q100/CONFIGURATIONS/conf/ampel-system.schema.json \
  AIRCRAFTMODEL/AMPEL360-Q100/CONFIGURATIONS/conf/ampel-system.example.json
```

XML Schema (`xmllint`):

```bash
xmllint --noout --schema ampel-system.xsd <your-instance>.xml
```

## Scope

These schemas are shared by both sibling configurations (`WTW/`, `BWB/`) of
`AMPEL360-Q100`. Configuration-specific instance documents should live next to
the configuration they describe and reference this schema via `$schema` /
`xsi:schemaLocation`.
