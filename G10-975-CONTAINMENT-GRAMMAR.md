---
schema_version: "1.0.0"
document_type: framework-reference
document_id: G10-975-CG-001
status: open-knot-specification
last_updated: "2026-04-24"
scope: |
  Normative specification for the G10.975 Containment Grammar — the
  load-bearing primitive of the G109 (QCSAA agentic-systems) sub-taxonomy.
companion_docs:
  - GLOSSARY_FOUNDATIONAL.md
  - AMPEL-ARTIFACT-LAYERS.md
  - AEROSPACEMODEL/OPT-INS/README.md
knot:
  id: KNOT-G10-975-001
  title: Containment Grammar undefined
  residual: 100
  state: open
---

# G10.975 — Containment Grammar (Specification)

**Status:** open `KNOT-G10-975-001` · **Date:** 2026-04-24 · **Scope:** the
load-bearing primitive of `G109-30 regent-ZetaGentz` within G10
(`QCSAA — Quantum Computing & Sentient Agency`, chapters 900–999).

> Without G10.975, "frontier agent" becomes a blanket exemption from
> auditability. Any `regent-ZetaGentz`-class agent that is **not**
> G10.975-compliant is unclassifiable under G109 and **SHALL NOT** be
> admitted as airworthiness evidence.

This document is the normative specification of the grammar. Companion
glossary entries (`G109`, `KNOT-G10-975-001`) are in
[`GLOSSARY_FOUNDATIONAL.md`](./GLOSSARY_FOUNDATIONAL.md).

---

## 1. Position in the G10 Taxonomy

The 970–979 chapter band of G10 (QCSAA) is reserved for **agentic
systems with containment semantics**. All entries in this band are
governed by this grammar.

| Code     | Name                          | Containment role                                              |
|----------|-------------------------------|---------------------------------------------------------------|
| G10.970  | ZGen Systems                  | Generators — emit candidate agents and KNUs                   |
| G10.971  | Zero-Gene Agents              | Stateless, single-purpose; trivially containable              |
| G10.972  | ZetaGentz classes             | Typed agent classes; require name-permissibility check        |
| G10.973  | regent-ZetaGentz              | Supervisory / regency governance; escalation target           |
| G10.974  | Generative Monsters           | *monstrum* — boundary-form; quarantinable by default          |
| **G10.975** | **Containment Grammar**    | **This specification — normative, load-bearing**              |
| G10.976  | Ethical Interface             | Outward-facing constraints; consumes G10.975 verdicts         |

The two G109 branches consume this grammar:

- **G109-10 SENTIENTIT** (known agents, certifiable, auditable; zGen
  outputs = KNUs, DO-178C-adjacent) — names and behaviours **MUST** be
  admissible by §2 and §3 below.
- **G109-30 regent-ZetaGentz** (frontier agents, boundary-forms) — every
  agent **MUST** carry a Containment Manifest per §5; absence ⇒
  unclassifiable (KNOT-G10-975-001 applies).

---

## 2. Permissible Names

The grammar restricts the set of agent names admissible into G109. No
name may appear in any classified artifact (CSP, FIDITA, OTAPC,
airworthiness submission) unless it satisfies **all** of the rules
below. Taxonomy creep — i.e. the introduction of a new agent name
without a formal entry — is a process failure.

### 2.1 Name shape

An agent name **SHALL** match the regular expression:

```
^(SENTIENTIT|regent-ZetaGentz)_(zGen|zeroGene|monstrum)_[A-Z][A-Za-z0-9]{2,31}-v[0-9]+(\.[0-9]+){1,2}$
```

Worked examples:

- `SENTIENTIT_zGen_AnomalyClassifier-v1.0.3` — admissible.
- `regent-ZetaGentz_monstrum_PlanScout-v0.2` — admissible.
- `frontier-agent-007` — **rejected**: missing branch, role, version.

### 2.2 Formal entry

A new name is admissible only after:

1. A glossary entry is appended to `GLOSSARY_FOUNDATIONAL.md` under
   the relevant letter, citing this document.
2. A row is added to the classifier register
   (`G10/970-979/REGISTER.csv` — see §6) with an entry timestamp,
   responsible regent, and chapter assignment in 970–979.
3. The name is referenced from at least one CSP that asserts the
   means-of-compliance argument in which the agent participates.

Any reference to a name that does not satisfy (1)–(3) is a finding
(class: *unregistered-name*) and **MUST** be rejected by upstream
review tooling.

### 2.3 Reserved namespaces

The following prefixes are reserved and **MUST NOT** be used outside
their defined scope:

| Prefix | Reserved for |
|--------|--------------|
| `SENTIENTIT_zGen_*` | Known, certifiable agents emitting KNUs |
| `SENTIENTIT_zeroGene_*` | Stateless agents with no learned parameters |
| `regent-ZetaGentz_monstrum_*` | Boundary-form / frontier agents under regency |
| `regent-ZetaGentz_zGen_*` | Frontier generators awaiting reclassification |

---

## 3. Containable vs. Quarantinable Behaviours

Every observed agent behaviour **SHALL** be classified into exactly one
of the three buckets below before the agent is admitted to any
airworthiness-relevant context.

### 3.1 Containable (admissible without escalation)

A behaviour is **containable** if **all** of the following hold:

- **Bounded effect.** The behaviour acts only on declared inputs and
  produces only declared outputs (interface contract is closed).
- **Reproducible.** Re-running the agent on the same inputs in the same
  environment yields identical outputs to within a declared tolerance.
- **Stationary.** No internal state evolves across invocations beyond
  what the manifest declares.
- **Observable.** Every output is captured by the H_EVIDENCE chain
  (see GLOSSARY: H-Pipeline) with a token-chain reference.

Containable behaviours flow through the SENTIENTIT (G109-10) branch
without further regency action.

### 3.2 Quarantinable (admissible only under regency)

A behaviour is **quarantinable** if it is observable and bounded but
violates one or more of: reproducibility, stationarity, or interface
closure. Quarantinable behaviours **SHALL**:

- Run inside a regency-controlled sandbox declared in the manifest;
- Emit no outputs to airworthiness-relevant artifacts (CSP, FIDITA,
  OTAPC) without a co-signature from the regent named in the manifest;
- Carry an active escalation token (§4) that names the trigger and the
  responsible regent.

Quarantinable behaviours are the only legitimate path through the
`regent-ZetaGentz` branch of G109.

### 3.3 Inadmissible (rejected)

A behaviour is **inadmissible** if any of the following holds:

- Effect crosses an undeclared interface (covert channel);
- Output cannot be captured by H_EVIDENCE;
- The agent's name fails §2;
- No Containment Manifest (§5) is present.

Inadmissible behaviours **MUST** be refused by upstream tooling and
**MUST NOT** be cited by any CSP or appear in any FIDITA. A CSP that
cites an inadmissible behaviour is itself inadmissible.

---

## 4. Regency Escalation Evidence

Reclassification from `SENTIENTIT_zGen` to `regent-ZetaGentz` is the
only sanctioned transition across G109 branches. The grammar requires
that the transition be evidence-driven and reversible.

### 4.1 Triggers

Escalation **SHALL** be initiated when one or more of the following
trigger conditions is observed and recorded:

| Trigger ID | Condition                                                                   |
|------------|-----------------------------------------------------------------------------|
| ESC-T1     | Reproducibility tolerance breached on ≥ 2 successive invocations            |
| ESC-T2     | Output observed outside declared interface (interface-closure violation)    |
| ESC-T3     | Internal state evolution detected beyond manifest declaration                |
| ESC-T4     | Regent-initiated escalation (e.g. anticipating a behavioural class change)  |
| ESC-T5     | External authority request (certification authority, safety board)          |

### 4.2 Evidence package

Each escalation **SHALL** produce an evidence bundle containing, at
minimum:

1. The agent name (per §2) and the chapter assignment (970–979).
2. The trigger ID(s) from §4.1 with timestamps and the originating
   H_EVIDENCE token references.
3. The Containment Manifest snapshot (§5) at the moment of trigger.
4. The regent identity (named, single individual, with PKI signature).
5. A new manifest declaring the post-escalation containment class
   (containable / quarantinable / inadmissible).
6. A `supersedes:` link to the prior manifest, satisfying the
   append-only discipline shared with the FIDITA layer
   (`AMPEL-ARTIFACT-LAYERS.md` §5).

An escalation without items (1)–(6) is a process failure and the
agent reverts to *inadmissible* until the bundle is complete.

### 4.3 De-escalation

A `regent-ZetaGentz`-class agent **MAY** be de-escalated back to
`SENTIENTIT_zGen` only when (a) every trigger that drove the original
escalation has been closed with a matching counter-evidence record,
and (b) two successive certification cycles have observed only
containable behaviour. De-escalation is itself an escalation event
(ESC-T4 with reversed direction) and produces its own evidence
bundle.

---

## 5. Containment Manifest

Every agent classified under chapters 970–979 **SHALL** carry a
Containment Manifest with at least the fields below. Absence of the
manifest is the triggering condition of `KNOT-G10-975-001`.

| Field            | Description                                                       |
|------------------|-------------------------------------------------------------------|
| `name`           | Agent name (per §2.1)                                             |
| `chapter`        | One of 970–979                                                    |
| `class`          | `containable` \| `quarantinable` \| `inadmissible`                |
| `interfaces`     | Declared inputs and outputs (closed set)                          |
| `tolerance`      | Reproducibility tolerance (numeric, per output)                   |
| `state`          | Declared internal state evolution rules (or `none`)               |
| `regent`         | Named individual + PKI key id (required if `class != containable`)|
| `escalation`     | Active trigger IDs (§4.1), or empty                               |
| `evidence_chain` | H_EVIDENCE token reference for the manifest itself                |
| `supersedes`     | Prior manifest id (for append-only history)                       |

The manifest **SHALL** be committed alongside the agent's source and
referenced from every CSP that depends on the agent.

---

## 6. Register and Tooling Hooks

The 970–979 chapter band is materialised as a register at
`G10/970-979/REGISTER.csv` (path is suggested; the directory is not
created by this specification). Each row corresponds to one admitted
agent name and carries: name, chapter, class, regent, manifest path,
evidence-chain token. Upstream review tooling **SHOULD** treat the
register as the single source of truth when checking CSPs and
FIDITAs for unregistered names.

---

## 7. Relationship to AMPEL Artifact Layers

| Artifact layer                               | Containment-grammar obligation                                        |
|----------------------------------------------|-----------------------------------------------------------------------|
| **Model** (`AMPEL-FAMILY-TAXONOMY.md`)       | A Model that uses agentic capability **MUST** name the agents in the register and cite their manifests. |
| **CSP** (`AMPEL-ARTIFACT-LAYERS.md` §3)      | A CSP **MUST NOT** cite an unregistered name; **SHALL** cite the manifest revision used in the means-of-compliance argument. |
| **OTAPC** (`AMPEL-ARTIFACT-LAYERS.md` §4)    | An OTAPC governing cross-Model agentic overlap **SHALL** declare a single regent and a shared manifest baseline. |
| **FIDITA** (`AMPEL-ARTIFACT-LAYERS.md` §5)   | A FIDITA snapshot **SHALL** record the manifest hash for every agent active in the digital-twin implementation at the freeze epoch. |

The `supersedes:` discipline shared with FIDITAs is non-negotiable:
manifests are append-only, and the chain **MUST** be reconstructable
from the artifacts alone.

---

## 8. Closure Criteria for KNOT-G10-975-001

`KNOT-G10-975-001` (residual 100, state *open*) is closed only when
**all** of the following are true:

1. Sections 2–6 above are accepted by the Principal Architect and the
   nominated regent for G109-30.
2. The 970–979 register exists and contains every agent referenced by
   any active CSP.
3. At least one full cycle of escalation and de-escalation (§4) has
   been demonstrated end-to-end with evidence bundles.
4. Upstream review tooling rejects unregistered names by default.
5. A KNU resolving the KNOT is filed in `KNU_PLAN.csv` citing this
   document and the closure evidence.

Until then, every `regent-ZetaGentz`-class artifact carries an
explicit "G10.975 open" annotation, and any attempt to use such an
artifact as airworthiness evidence is a finding.

---

## 9. References

- `GLOSSARY_FOUNDATIONAL.md` — entries for `G10`, `G109`,
  `KNOT-G10-975-001`, `QCSAA`, `KNOT`, `KNU`, `H-Pipeline`.
- `AMPEL-ARTIFACT-LAYERS.md` — Models / CSP / OTAPC / FIDITA layers.
- `AEROSPACEMODEL/OPT-INS/README.md` — companion index that links to
  this specification.
