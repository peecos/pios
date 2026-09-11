# Cognitive Memory, Source Discovery, and Derived Representations v0.1

Status: draft companion specification for PIOS 2.0. This document defines
future object and lifecycle boundaries. It does not authorize collection,
inference, biometric processing, external model use, or personal-data transfer.

## 1. Purpose

PIOS 2.0 already preserves originals and events, maintains living Knowledge
Objects, infers derived patterns, and treats vectors and graph exports as
rebuildable projections. This companion defines three additions without
creating a second Core or an opaque model-memory layer:

1. Cognitive Memory: governed Meaning and Learning knowledge objects.
2. Source Discovery: a candidate-only phase before connector registration.
3. Derived Representations: source-linked projections for graph, text, and
   multimodal processing.

These are PIOS information-system functions, not automatically external
application work. Follow the [hosting and boundary principles](hosting-core-boundaries-and-portability-principles-v0.1.md):
Core contract membership, PIOS system membership, and physical placement are
separate. Native knowledge processing, context compilation, and retrieval
normally run with Core in the Solo VM for the selected profile. Replaceable
agents, models, or index engines do not by themselves change that membership.

## 2. Cognitive Memory

### 2.1 Object families

| Object | Question it answers | Boundary |
| --- | --- | --- |
| Meaning | Why does this source, event, decision, or experience matter to the owner? | contextual, revisable interpretation |
| Learning | What durable lesson, preference, strategy, correction, warning, or working method may help later? | evidence-linked proposal for future reasoning |

Meaning and Learning are Knowledge Layer objects. They are not a sixth data
zone, agent-private memory, profile truth, or automatic policy.

### 2.2 Required fields

Each object records stable subject references, evidence references, source
events, statement, originator/model where relevant, confidence, context,
creation time, and revision relationship. Types remain Cotton/glossary-
extensible rather than a fixed universal enum.

### 2.3 Non-authoritative lifecycle

```text
proposed → owner_confirmed
         ↘ rejected
owner_confirmed → superseded
```

Model- or agent-generated objects start as `proposed`. They may improve
retrieval as explicitly labelled candidates, but they cannot alter Cotton,
owner profile truth, rules, skills, agent behavior, policy, or retrieval
ranking merely because a model generated them. Such a change needs an existing
proposal/standing-rule or request-scoped approval path.

Observation, interpretation, and learning remain separate. For example:

```text
observation: three projects slipped after scope changes
interpretation: unclear ownership may contribute to the slips
learning: confirm one accountable owner before delivery begins
```

## 3. Source Discovery is not collection

Source Discovery may inspect a submitted domain, page, organization, or service
for potential feeds, APIs, sitemaps, public release channels, or other update
sources. It produces candidates with source type, URL, confidence, terms/robots
notes, expected frequency, security state, and likely cost.

Its normative state machine is:

```text
discover_candidate
  → candidate_review
  → permission_review
  → registered
  → backfill_authorized
  → incremental_collection_authorized
  → paused | revoked
```

Discovery never collects. Registration does not authorize backfill. Backfill
does not authorize ongoing collection. Each transition uses the PIOS inbound,
source-registration, consent, source-trust, and processing-governance rules.

## 4. Derived Representation record

Derived representations remain projections. A generic record must identify:

```text
representation_type
source_ref and source_version
core:// logical reference
processing profile/model/version
confidence and processing status
sensitivity, consent, retention, deletion/revocation behavior
created_at and provenance
```

Possible types include text chunks, extracted metadata, graph snapshots, OCR,
semantic vectors, visual vectors, region vectors, summaries, and retrieval
indexes. Provider paths, embedding payloads, service identifiers, and vector
store keys are implementation metadata, never canonical meaning.

The representation may be governed in Core's Derived zone while remaining
rebuildable and non-authoritative. Its executor may run inside the Solo VM or
in an explicitly declared external processing resource. Neither rebuildability
nor non-authoritative status requires a separate machine. An independent
application's private projection remains a different role and must not be
presented as the PIOS retrieval implementation merely because it cites Core
sources.

## 5. Optional future profiles

Document-local graph snapshots may be used when global entity resolution would
lose source-specific claims, relationships, or evidence. They remain source
version projections and must never silently establish global identity matches.

Multimodal retrieval can be added only for a concrete owner benefit and a
reviewed profile. Image, audio, video, OCR, region, and face processing each
need explicit sensitivity, consent, model/provider, retention, deletion, cost,
and access treatment. Face representations require separate elevated review.

S3 Vectors or any equivalent is an implementation-profile choice. It belongs in
an AWS or other provider profile after this technology-neutral record and
contract are proven.

## 6. Meaning and Learning record contracts

A future schema should require the following common fields without fixing every
Cotton vocabulary value permanently:

```text
id and object_type
subject_refs and evidence_refs
statement
originator and model/profile where relevant
confidence
context and applicable scope
created_at
status
supersedes or revision relationship
review_after where applicable
```

Meaning records explain why information matters to the owner. Learning records
describe an evidence-linked lesson, strategy, correction, preference, warning,
or working method that may help later. Their types remain glossary-extensible.

A Meaning profile or service may answer governed personal-semantic questions
over these objects. It is an interface over Core knowledge and evidence, not a
new authoritative layer, data zone, or permission source.

Recall conditions may make confirmed Meaning or Learning relevant to a later
task. Adaptation remains a separate governed action: a confirmed learning does
not silently rewrite an agent definition, workflow, preference, or policy.

## 7. Source-local graph snapshots

When graph extraction is useful, PIOS should preserve an immutable graph
snapshot for a specific source version before attempting global entity
resolution. The snapshot records:

- snapshot id, source reference, and source version;
- extraction profile, model/version, time, and status;
- source-local nodes and relationships;
- confidence and evidence references, including page, paragraph, timestamp, or
  media-region references where available;
- proposed canonical matches separately from confirmed resolutions.

A changed source or extraction profile creates a new snapshot. The original
snapshot remains evidence of what that source and extraction produced. Global
graphs are evolving projections and must not erase source-local ambiguity.

## 8. Derived-representation registry and lifecycle

Each retained derived representation should be discoverable through a registry
record containing its canonical subject, source version, representation type,
model and model version, output format or dimensions, creation time, sensitivity
and authorization basis, lifecycle status, replacement relationship, and
provider-specific physical reference.

Representation identity must separate incompatible models, dimensions,
modalities, and semantic spaces. Creation of a new model output does not
silently overwrite the only historical representation. Representations may be
active, deprecated, superseded, rebuildable, or deleted according to source and
consent lifecycle.

## 9. Source Discovery record

A discovery result should retain the submitted URL or subject, discovered
candidate type and location, confidence, expected update frequency, security
state, authentication need, terms/robots notes, and the discovering actor and
time. It remains a candidate record until the separate review, registration,
backfill, and incremental-collection transitions are authorized.

## 10. Context compilation profiles

Context compilation answers: what may this authorized caller know for this
purpose now? It has two distinguishable modes:

- **deterministic selection** uses explicit filters, canonical references,
  time bounds, confirmed tags, declared ranking rules, and reproducible packing;
- **model-assisted compilation** summarizes, ranks, or selects within an
  already authorized candidate set and records model identity/version,
  confidence, source coverage, omissions, and a non-authoritative projection
  status.

A request identifies integration/runtime identity, purpose, Authorization
Grant, requested data classes, sensitivity ceiling, freshness, recipient and
processing boundary, retention, and output-reference requirements. Context and
Meaning never imply authorization. Outward disclosure uses the Context Receipt
defined by the integration-governance companion.

## 11. Role, Mode, and epistemic lifecycle

Role type, Role instance, and temporary relevance to one event or session are
separate claims. Role and Mode records should retain source, evidence,
confidence, scope, status, applicable time range, expiry or review time, and
supersession. Multiple Roles and Modes may be relevant concurrently.

Modes normally describe ephemeral operating context. Repeated or inferred Mode
use does not become a persistent preference, rule, or owner fact without
explicit confirmation and versioned evidence.

PIOS preserves the following distinctions:

```text
Event → observed pattern → proposed Meaning → owner-confirmed Meaning → Learning
```

Each arrow is a governed interpretation or confirmation step, not automatic
promotion. Frequency is not importance, and recurrence is not preference. A
Learning may later be recalled as context, but changing behavior remains a
separate adaptation decision.

## 12. Required future evidence

Before a representation profile is supported, prove source linkage, versioning,
retrieval provenance, revocation/deletion behavior, and fail-closed handling
for an excluded or guarded source. Before Cognitive Memory changes behavior,
prove owner-confirmation and rollback behavior. Publish harmless fixtures for
Meaning, Learning, source-local graph snapshots, source discovery, and
representation-registry lifecycle before declaring interoperable schemas. Add
deterministic and model-assisted context fixtures, Role/Mode expiry cases, and
Context Receipt linkage before claiming those profiles interoperable.
