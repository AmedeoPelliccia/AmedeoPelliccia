---
schema_version: 1.0.0
document_type: ledger-index
document_id: LEDGER-INDEX-001
last_updated: 2026-05-06
status: controlled-baseline
parent: ../README.md
---

# Civilizational Ledger

Append-only, schema-validated registry of canonical principles, axioms, and corporate-imposition transactions referenced from the root `README.md` (notably §1.4.1 *Imposición Corporativa Primaria*).

This directory exists to make every `TX-*` identifier cited in governance text **resolvable, auditable, and machine-validatable**. No identifier referenced from a controlled document may remain a dangling string.

## Layout

```text
ledger/
├── README.md                                     # this file
├── schema/
│   └── tx-principle-imposition.v1.schema.json    # JSON Schema 2020-12
└── TX-PRINCIPLE-IMP-CORP-FIRST-001.json          # canonical TX entry
```

## Conventions

| Rule | Description |
|---|---|
| **Filename = TX ID** | A `TX-*.json` filename MUST equal its `tx_id` field, with `.json` suffix. |
| **Append-only** | Existing TX entries MUST NOT be mutated. Corrections require a new TX with `supersedes` referencing the prior `tx_id`. |
| **Schema binding** | Every TX MUST declare `"$schema"` pointing to a versioned schema in `ledger/schema/`. |
| **Anchor parity** | The `principle_anchor` of a TX MUST resolve to a principle declared in a controlled document (e.g., `README.md` §1.4.1). |
| **Glossary parity** | Per §1.4.1 Rule 5, every acronym used in a TX MUST appear in `README.md` Annex E. Otherwise the TX is `status: pending_glossary` and suspended. |

## Index

| TX ID | Principle Anchor | Effective | Status | File |
|---|---|---|---|---|
| `TX-PRINCIPLE-IMP-CORP-FIRST-001` | `PRINCIPLE-IMP-FOR-TODES-CORP-FIRST-001` | `2026-04-30` | `active` | [`TX-PRINCIPLE-IMP-CORP-FIRST-001.json`](TX-PRINCIPLE-IMP-CORP-FIRST-001.json) |

## Validation

JSON files in this directory MUST validate against their declared `$schema`. A minimal local check:

```bash
python -c "import json,sys; [json.load(open(p)) for p in sys.argv[1:]]" \
  ledger/schema/tx-principle-imposition.v1.schema.json \
  ledger/TX-PRINCIPLE-IMP-CORP-FIRST-001.json
```

For full schema validation, use any JSON Schema 2020-12 validator (e.g., `check-jsonschema`, `ajv`).
