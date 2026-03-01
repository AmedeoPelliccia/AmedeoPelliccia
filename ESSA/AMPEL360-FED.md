# AMPEL360 Federated Fleet Data Architecture

**AMPEL360 — Federated Fleet Data Integration (Manufacturer / Aircraft Model / Operator)**

| Metadata | Value |
|----------|-------|
| **Document ID** | ESSA-DOC-AMPEL360-FED-001 |
| **Version** | v0.1-draft |
| **Status** | Normative Method — Integration Component |
| **Parent** | ESSA-DOC-AMPEL360-001 ([AMPEL360.md](AMPEL360.md)) |
| **Companion** | [`ampel360-fed.yaml`](ampel360-fed.yaml) |
| **Related** | [`AMPEL360-Q100.md`](AMPEL360-Q100.md) · [`AMPEL360-PR.md`](AMPEL360-PR.md) · [`H-PIPELINE.md`](H-PIPELINE.md) |
| **Domain** | Civil Aviation — Fleet Data Federation (MRO / OEM / Operator) |
| **Regulatory Authority** | EASA / FAA (dual-authority operator context) |
| **Last Updated** | 2026-03-01 |

---

## Core Principle

> **Tag at source. Filter without copying. Govern without centralising.**
>
> The Federated Fleet Data Architecture does not aggregate fleet data into a single repository.
> It tags documents at the source with three canonical Global Tags — Manufacturer, Aircraft Model, Operator —
> and routes queries through the AMPEL-A7 RAG engine against those tags.
> Fleet data remains in its authoritative source system; AMPEL360 governs the query, not the data.

This component extends the AMPEL360 Q100 profile with a federated integration layer for fleet technical records, maintenance manuals, and compliance artefacts. It is inhibited by all H-pipeline gate invariants and the Safety-First doctrine.

---

## 1. Scope and Safety Boundary

This architecture applies to:

- **Technical Publications** (AMM, IPC, CMM, SRM, WDM) scoped by fleet segment
- **Compliance and Lease Records** scoped by operator regulatory environment
- **Fleet Maintenance Aggregates** scoped across operators within a lessor or MRO portfolio

**Safety boundary (non-negotiable):**

- The federated layer **SHALL NOT** modify source technical data; it queries and routes only.
- The federated layer **SHALL** enforce H-token linkage so every query result is traceable to an authoritative `H_EVIDENCE` record.
- No federated query result is activable until it carries an `H_SIGNOFF` from the responsible engineer and authority.
- Operator-specific variants **SHALL** be disambiguated by the Global Tag set before any result is surfaced.

---

## 2. Unified Metadata Schema — Global Tags

Each document or record ingested into the federation layer **SHALL** be tagged with the following three canonical Global Tags. These tags are registered as `H_CONSTRAINT` on the active query context and as `H_EVIDENCE` metadata on the retrieved record.

### 2.1 Global Tag: Manufacturer (OEM)

| Field | Definition |
|-------|-----------|
| **Tag name** | `manufacturer` |
| **Type** | Controlled vocabulary (ICAO designator or IATA-equivalent OEM code) |
| **Example values** | `AIRBUS`, `BOEING`, `EMBRAER`, `BOMBARDIER`, `ATR` |
| **Cardinality** | Exactly one per record |
| **H-token** | `H_CONSTRAINT` (constrains which OEM documentation set applies) |
| **Mandatory** | Yes — absence blocks AMPEL-A7 RAG engine routing |

### 2.2 Global Tag: Aircraft Model

| Field | Definition |
|-------|-----------|
| **Tag name** | `aircraft_model` |
| **Type** | String — ICAO type designator or OEM part-number prefix |
| **Example values** | `A321neo`, `737-MAX8`, `E195-E2`, `CRJ-900`, `ATR-72-600` |
| **Cardinality** | One or more (a document may span sub-variants; list all applicable) |
| **Relationship** | Child of `manufacturer` — cross-OEM model IDs are not permitted |
| **H-token** | `H_CONSTRAINT` (constrains model-specific data retrieval) |
| **Mandatory** | Yes — absence blocks Technical Publications Mode queries |

### 2.3 Global Tag: Operator

| Field | Definition |
|-------|-----------|
| **Tag name** | `operator` |
| **Type** | Controlled vocabulary (ICAO operator designator or internal fleet-management ID) |
| **Example values** | `BAW` (British Airways), `AFR` (Air France), `RYR` (Ryanair), `LESSOR-001` |
| **Cardinality** | One or more (a document may apply to multiple operators under a lessor) |
| **Relationship** | Linked to `aircraft_model` via fleet assignment record |
| **H-token** | `H_CONSTRAINT` (constrains operator regulatory environment — EASA/FAA) |
| **Mandatory** | Yes for Compliance/Lease Mode and Fleet Management Mode; optional for generic Technical Publications |

### 2.4 Composite Tag Validation Rules

| Rule ID | Check | Severity | Blocked Gate |
|---------|-------|----------|--------------|
| **FED-TAG-001** | `manufacturer` tag present on every ingested record | FAIL | ACTIVATE |
| **FED-TAG-002** | `aircraft_model` tag present and consistent with `manufacturer` | FAIL | ACTIVATE |
| **FED-TAG-003** | `operator` tag present for Compliance/Lease and Fleet Management queries | FAIL | ACTIVATE |
| **FED-TAG-004** | No cross-OEM `aircraft_model` tag (model must belong to declared manufacturer) | FAIL | CONFIRM |
| **FED-TAG-005** | Operator's regulatory authority (EASA/FAA) declared and consistent with `H_CONSTRAINT` | WARN (DAL C/D) / FAIL (DAL A/B) | CONFIRM |

---

## 3. Federated Integration Layer

### 3.1 Data Connectors

The AMPEL-A7 RAG engine connects to external document repositories via the **Integrations** interface. Each connector **SHALL** be configured to:

1. **Push Global Tags** — propagate `manufacturer`, `aircraft_model`, `operator` as metadata on every document indexed.
2. **Declare source authority** — identify the authoritative source system (OEM portal, MRO database, regulatory depository) as `H_EVIDENCE` metadata.
3. **Version-lock the index** — record the document revision and index timestamp as a `H_CONSTRAINT` to prevent stale data being returned without explicit staleness warning.
4. **Respect access controls** — each connector operates under the access rights of the requesting `H_SIGNOFF` authority; no connector may elevate privileges.

**Connector types supported:**

| Connector Type | Data Source Example | Tag Propagation Method |
|----------------|--------------------|-----------------------|
| OEM Portal API | Airbus AirbusWorld, Boeing Toolbox | Native metadata fields → Global Tags |
| MRO Database | AMOS, TRAX, OASES | Custom field mapping via adapter |
| Regulatory Depository | EASA EDOM, FAA DRS | Document type + model selector |
| CSV/JSON Fleet Upload | Operator-provided fleet schema | Schema mapping via field map config |

### 3.2 Federated Search and the AMPEL-A7 RAG Engine

The AMPEL-A7 RAG engine applies the three Global Tags as **pre-query filters** before semantic search. This prevents cross-fleet contamination in retrieval.

**Query routing logic:**

```
GIVEN  active_query_context = { manufacturer, aircraft_model, operator }
AND    all three tags are present and validated (FED-TAG-001 through FED-TAG-005)

FILTER index to records where:
  record.manufacturer == manufacturer
  AND record.aircraft_model ∈ aircraft_model_list
  AND (record.operator == operator OR record.operator == GENERIC)

THEN  apply semantic similarity ranking within filtered set
RETURN top-k results with H_EVIDENCE metadata (source, revision, index_ts)
```

**Inhibitor:** If any required tag is absent or fails validation, the RAG engine returns an `H_EXCEPTION` (empty result with exception reason) rather than an unscoped search result.

---

## 4. IA Modes — Optimised by Global Tags

Once the Global Tags are configured, the following AMPEL360 IA Modes operate with fleet-scoped context.

### 4.1 Technical Publications Mode

**Scope:** AMM (Aircraft Maintenance Manual), IPC (Illustrated Parts Catalogue), CMM (Component Maintenance Manual), SRM (Structural Repair Manual), WDM (Wiring Diagram Manual).

**Global Tag usage:**

- `manufacturer` + `aircraft_model` → narrows document retrieval to the exact aircraft type; eliminates cross-model chapter confusion (e.g., A320ceo vs A320neo task numbering differences).
- `operator` (optional) → applies operator-specific revision status if the operator has customised the base AMM.

**H-token linkage:**

- Query results are returned as `H_EVIDENCE` (type `technical_publication`) linked to the active `H_REQ` that initiated the query.
- Gaps (no matching document for a required task) are flagged as `H_EXCEPTION` until resolved.

### 4.2 Compliance / Lease Mode

**Scope:** Airworthiness Directives (ADs), Service Bulletins (SBs), lease return conditions, maintenance programme compliance.

**Global Tag usage:**

- `operator` → determines the regulatory authority (EASA or FAA) and associated AD/SB applicability.
- `aircraft_model` → scopes the applicable AD/SB set to the specific variant.
- `manufacturer` → resolves OEM service document numbering system.

**H-token linkage:**

- Compliance findings are registered as `H_EVIDENCE` (type `compliance_record`) linked to `H_REQ` (airworthiness requirement) and `H_CONSTRAINT` (operator regulatory environment).
- Non-compliant status generates `H_EXCEPTION` with mandatory escalation to `H_SIGNOFF` authority.

### 4.3 Fleet Management Mode

**Scope:** Cross-operator maintenance aggregates within a lessor or MRO portfolio.

**Global Tag usage:**

- Multiple `operator` values → aggregates maintenance events, component lifetimes, and compliance status across the fleet.
- `aircraft_model` → ensures only type-compatible records are aggregated.
- `manufacturer` → disambiguates OEM revision baselines across operators who may be at different service bulletin incorporation states.

**H-token linkage:**

- Aggregate results are registered as `H_UPDATE` records (fleet status update) linked to the lessor's `H_ENVELOPE`.
- Discrepancies between operator-specific and fleet-baseline records generate `H_EXCEPTION` for engineering review.

---

## 5. Schema Definition — Federated Fleet Record

The canonical schema for a federated fleet record (suitable for CSV/JSON upload or API response mapping):

```yaml
fleet_record:
  # Mandatory Global Tags
  manufacturer:       string  # ICAO OEM designator (e.g. "AIRBUS")
  aircraft_model:     string  # ICAO type designator (e.g. "A321")
  aircraft_variant:   string  # OEM sub-variant (e.g. "A321neo CFM LEAP-1A")
  operator:           string  # ICAO operator designator (e.g. "BAW")

  # Fleet Asset Identifier
  msn:                string  # Manufacturer Serial Number
  registration:       string  # Current aircraft registration (e.g. "G-TTNE")
  fleet_id:           string  # Operator internal fleet number

  # Configuration State
  configuration_baseline: string   # OEM mod/SB state identifier
  regulatory_authority:   string   # "EASA" or "FAA" (or both)

  # H-token Linkage
  h_evidence_ref:     string  # Linked H_EVIDENCE record ID
  h_constraint_ref:   string  # Linked H_CONSTRAINT record ID
  h_signoff_ref:      string  # Linked H_SIGNOFF (if activated record)
```

**Upload support:** Operators may upload a fleet CSV or JSON with at minimum `manufacturer`, `aircraft_model`, and `operator` columns. The AMPEL360 integration layer maps remaining fields from the source schema and registers the record as `H_CONSTRAINT` for the active session.

---

## 6. H-Pipeline Inhibitors

| ID | Inhibitor | Condition | Blocked Operation |
|----|-----------|-----------|-------------------|
| **FED-INH-001** | `¬Global_Tags_Valid` → BLOCKED | Missing or invalid `manufacturer`/`aircraft_model`/`operator` tags | All RAG engine federated queries |
| **FED-INH-002** | `¬H_EVIDENCE(source_authority)` → BLOCKED | Connector source not declared as authoritative | ACTIVATE gate (record activation) |
| **FED-INH-003** | `¬H_SIGNOFF(authority)` → BLOCKED | No engineer sign-off on activated compliance record | PUBLISH gate (fleet status release) |
| **FED-INH-004** | `Cross_OEM_tag_conflict` → BLOCKED | `aircraft_model` not consistent with declared `manufacturer` | All queries (hard validation failure) |

---

## 7. Gate Alignment (DO-178C / CCTLS × Fleet Federation)

| CCTLS Gate | Fleet Federation Action | Active H-tokens | Gate Pass Condition |
|------------|------------------------|-----------------|---------------------|
| **INTERPRET** | Global Tags validated; connectors declared; fleet schema registered | `H_CONSTRAINT` (tags), `H_ENVELOPE` | All three tags present and validated; source authority declared |
| **CONFIRM** | RAG engine filter verified against fleet record set; cross-OEM conflicts resolved | `H_REQ`, `H_CONSTRAINT` | FED-TAG-001–005 all PASS; no unresolved `H_EXCEPTION` |
| **ACTIVATE** | Compliance findings registered; fleet status records activated | `H_EVIDENCE`, `H_EXCEPTION_cleared` | All compliance records carry `H_EVIDENCE`; no open exceptions |
| **PUBLISH** | Fleet status bundle released to operators / lessor | `H_SIGNOFF` | Authority sign-off present on all activated records |

---

## 8. Relationship to Constitutional Instruments

| Instrument | FED Role |
|------------|---------|
| **ESSA-CONST-001** | Satisfies CI-003 (Deterministic Gates) via FED-TAG validation; CI-004 (Machine-Verifiable Conformance) via schema enforcement |
| **ESSA-DOC-AMPEL360-001** | FED is a functional integration sub-component of AMPEL360 |
| **ESSA-DOC-AMPEL360-Q100-001** | Q100 Aviation profile is the primary consumer of FED; activates Technical Publications and Compliance/Lease modes |
| **ESSA-DOC-AMPEL360-PR-001** | Profile Resolver generates C skeletons tagged with fleet context from FED |
| **ESSA-DOC-H-001** | FED query results are H-token-linked (`H_EVIDENCE`, `H_CONSTRAINT`, `H_EXCEPTION`) |
| **ESSA-DOC-SF-001** | Safety-first: FED queries are `H_ENVELOPE`-gated; no unscoped cross-fleet result is activable |
| **ESSA-STD-CCTLS-001** | FED gate alignment maps to CCTLS INTERPRET → CONFIRM → ACTIVATE → PUBLISH |
