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

<a id="assertion-and-lineage-profile"></a>

## 13. Optional assertion and lineage profile

Sections 13–15 are optional contract elaborations of the master's
[Knowledge Layer](../index.html#knowledge), [patterns](../index.html#patterns),
and [retrieval](../index.html#retrieval). Requirements in each section apply
only to implementations explicitly selecting that profile. They add no
mandatory Core capability, API/export field, or compatibility level. Capture
can proceed under existing rules without selecting any of these profiles.
Records reuse Originals, Events, Knowledge, Derived, and System; there is no
sixth zone, required graph database, or universal recomputation engine.

Canonical acceptance establishes the retained record and its provenance. A
canonical record of a claim is not proof that the claim is true. Consistent
with master §§14.2–14.3, an assertion profile must keep independent dimensions:

| Dimension | What the record distinguishes |
| --- | --- |
| Origin | Source statement, observation, owner statement, or model/rule inference; originating actor and source revision. |
| Evidential support | Supporting and contradicting references, coverage, uncertainty, and assessment basis. |
| Acceptance | Proposed, confirmed, rejected, or revised interpretation, with decision authority; distinct from acceptance of the containing record. |
| Temporal validity | Period asserted to apply, observation time, evaluation time, and review/expiry conditions. |
| Access | Current permitted purpose, operation, recipient, and enforcement boundary under existing grants. |

These are descriptive dimensions, not new universal enums. Confirmation does
not erase contradictory evidence; expired access does not negate a statement;
an accurate historical claim need not describe the present. Assertions retain
stable identities, subject and source-version references, and revision links.
Source-local claims and ambiguous entity matches remain distinguishable from
accepted cross-source interpretations.

A selected lineage profile must distinguish dependency kinds, recording the
dependent result, referenced revision/profile, relationship, and evaluation:

| Dependency | Meaning and change consequence |
| --- | --- |
| Evidential | A source or assertion supports or challenges another claim; correction or new evidence can require review. |
| Computational | A result was produced from particular inputs, parameters, and processor versions; changes can require recomputation for current use. |
| Policy | Use depends on a grant, terms, purpose, recipient, or retention condition; changes require authorization revalidation. |

Maintenance outcomes are independently recorded, with reason and time:

- `stale`: the result has not been reevaluated against relevant changes or its
  freshness window; it is not automatically false.
- `disputed`: evidence or an authorized review challenges the assertion;
  disagreement is retained pending resolution.
- `inaccessible`: the requested access is denied or the required evidence is
  unavailable; distinguish policy denial from retrieval failure.
- `superseded`: a later identified revision replaces this result for a stated
  scope; the earlier result remains historical under its retention rules.

These outcomes can coexist. A corrected source may leave a summary stale and
its interpretation disputed, while a revoked grant makes both inaccessible to
a caller. Revocation alone supplies no evidence that either claim was false.

Maintenance may flag affected dependants or propose recomputation. Execution
must revalidate current authority for inputs, processing, recipients, and
write-back through the existing [integration grants](integration-interoperability-and-governance-v0.1.md#4-enforceable-authorization).
A dependency edge or earlier successful run grants no permission to recompute.
Record a new result with lineage and a corrective or superseding Event where
canonical state changes, preserving the append-oriented Event history. Retain
historical results subject to retention/deletion rules; never present a
recomputation as the original historical output. Unsupported or blocked work
stays explicitly unresolved, without requiring re-ingestion of retained sources.

<a id="semantic-assessment-and-cluster-profile"></a>

## 14. Optional semantic assessment and cluster profile

A selected semantic-assessment profile must declare typed questions, such as
topic relevance, project association, Role/Mode relevance, or relationship
classification. Different question types need distinct score interpretations.
The profile declares whether an output is a transient routing/classification
signal, retained evidence, a Derived projection, or a proposed Knowledge object.
Transient signals need not become durable records or retain every intermediate
score. Existing required audit and provenance for consequential processing,
disclosure, canonical changes and applied decisions still apply; transient
treatment is not permission to omit that evidence.

Retained assessments declare their state treatment, retention and authorization
basis. Their records include:

- assessment identity/type, source references and revisions, evidence spans
  where available, and the requested context/purpose;
- candidate-set identity/version and the authorized subset actually considered,
  including versions of labels/descriptions and coverage limitations;
- processor/model/rule profile and version, parameters, input/output language,
  processing time, and applicable context or validity window;
- proposed matches, score meaning and scale, threshold/decision rule,
  uncertainty, and an explicit abstention or insufficient-evidence result;
- provenance, applicable grant/recipient boundary, review/expiry conditions,
  and revision or supersession relationship.

Candidate metadata is input data: project names, Role labels, descriptions,
examples, and candidate relationships can disclose sensitive information.
Authorize and minimize both source content and candidate metadata before model
or processor disclosure, using existing integration §§4, 14, 18, and 20.
Receipt/trace evidence identifies the evaluated candidate versions and scope
without copying excluded metadata into routine logs. Restricted candidates
mean limited coverage, not proof that no other relevant candidate exists.

A score may express similarity, relative ranking, or a declared calibrated
estimate; it is not inherently a probability of truth. State which meaning
applies and avoid comparison across incompatible types/profiles. High
confidence supplies neither correctness, access rights, nor authority to act.
Abstain when the declared evidence or decision conditions are unmet rather
than forcing the highest-scoring candidate into an accepted fact.

Multiple labels, Roles, and Modes may apply concurrently within stated scopes.
They remain context claims under section 11, never grants. Classification,
extraction, entity resolution, and canonical promotion are separate operations:
extracting a named participant does not identify a global person; classifying
a passage does not adopt a Cotton term or confirm Meaning. Preserve section 7's
source-local snapshot and proposed matches through any later resolution.
Classification within existing request-scoped or standing authority needs no
fresh owner confirmation merely because a model produced it. Retaining a result,
promoting Meaning/Learning, or changing behavior follows its applicable existing
authority path; a processing grant does not automatically authorize all three.
Meaning/Learning objects retain section 2.3's proposal/adoption controls.
Changes to retrieval ranking or other behavior likewise require the applicable
existing authority, not a new approval for every signal already within scope.

An implementation selecting cluster support within this profile must retain
cluster identity, versioned membership with source revisions, generating
profile/parameters, context, evidence, and proposed/accepted status. Clusters
may be unnamed, overlap, or have uncertain membership; a generated title is a
label proposal, not an entity identity. Membership changes create a revision.

Splits and merges record predecessor/successor references and the membership
transition. State explicitly whether an existing identity continues and why;
new branches or merged objects receive distinct identities unless a governed
continuity decision identifies the continuing object. Labels alone cannot
transfer identity, acceptance, permissions, or all predecessor claims. Retain
ancestry and earlier membership under the applicable retention rules.

Consolidation groups or summarizes existing material; concept induction
proposes a useful abstraction; rule induction proposes a generalization or
behavioral rule. These are separate operations. Promotion follows master
§14.8 and existing owner/standing-rule authority; no cluster size, recurrence,
or model score automatically adopts a concept, Learning, or operating rule.
Existing Base Week, routine, and pattern semantics remain unchanged. A selected
assessment may record seasonal or annual context in its validity window;
that does not create a schedule or convert observed recurrence into intention.

<a id="processing-result-reuse"></a>

## 15. Optional processing-result reuse profile

A selected reuse profile extends sections 4 and 8's derived records and the
[provider-result lifecycle](integration-interoperability-and-governance-v0.1.md#17-provider-result-lifecycle).
It must bind each retained result to source identity/revision, operation,
processor/model/rule version, parameters, input/output language, output type,
creation time, provenance, and freshness conditions. Record permitted purpose,
audience/recipient boundary, sensitivity, retention, and authorization basis.
Where assessments or clusters are inputs, include their relevant versions.

Reuse returns an existing result after checking input/version suitability,
freshness, and current permission for the requester, purpose, and audience.
An earlier processing grant or common application publisher does not authorize
every later reader. Multi-source results retain applicable source restrictions;
summarization does not by itself declassify their content. Record outward
disclosure through the existing Context Receipt or equivalent event/audit pair.

Reprocessing executes a processor again and needs current processing authority,
even for unchanged source bytes. A changed source revision, processor profile,
parameters, or language is a different processing request, not an identical
cached result. It produces a separately identified result with lineage; the
same inputs do not guarantee identical model output. Redaction or translation
for a different audience is also processing, not permission-free reuse.

Changing the audience requires a fresh disclosure decision even when bytes
remain unchanged. Denied reuse does not authorize fetching sources again or
switching models/providers. Missing, stale, or incompatible results remain
explicit until an authorized reuse, refresh, or recomputation is available.
This contract mandates no shared engine, storage product, or model provider.

Before claiming support for these selected profiles, validate source correction
without history loss, independent dispute/access states, denied recomputation,
candidate-metadata exclusion before disclosure, abstention and multi-label
results, split/merge continuity, and reuse across revision/language/audience
changes. Concrete score calibration, supported languages, retention enforcement,
and reproducibility remain implementation validation questions; this draft
establishes neither working support nor interoperable schemas.
