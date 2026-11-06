# Integration Interoperability and Governance v0.1

Status: draft companion specification for PIOS 2.0. This document defines a
future integration-governance contract. It does not authorize app networking,
personal-data intake, real device credentials, generic API keys, or any
deployment.

## 1. Purpose and boundary

PIOS Core is the durable owner-controlled information and authority foundation,
including declared capabilities and their execution, inside the complete PIOS
operating system. A PIOS-native service or client, independent application or
agent, source connector, AI service, or protocol adapter operates through
explicit, continuously evaluated authority. A manifest is a declaration of
requested behavior; it is not proof of behavior and it creates no authority by
itself. Being native to PIOS or sharing its VM never bypasses this governance.

This specification extends the PIOS 2.0 master's Core Service Interface,
agent-definition governance, privacy/access rules, and Core Compatibility
contract. It does not replace the mandatory Core API, `/.well-known/core`, or
Core Compatibility Levels 1–5.

The hosting-boundary taxonomy is defined in [Hosting, Core Boundaries, and
Portability Principles
v0.1](hosting-core-boundaries-and-portability-principles-v0.1.md). Integrations
must distinguish a normative Core capability, its replaceable executor, a Core
interface or adapter, PIOS-native supporting services and interfaces,
independent consumers, an operator control plane, and external model or
processing resources. Record Core contract membership, PIOS system membership,
and physical placement separately. Outside Core does not automatically mean
outside PIOS or outside its Solo VM.

## 2. Terms

| Term | Meaning |
| --- | --- |
| Integration Definition | A System-zone record describing one application, agent, connector, AI service, protocol adapter, or hosted Core provider. |
| Integration Manifest | A signed or otherwise attributable declaration of requested behavior and operational characteristics. It remains an untrusted claim until evaluated and enforced. |
| Personal Terms | The owner's reusable conditions for use of personal information. They are distinct from scopes and may restrict purpose, processing, retention, recipients, and model use. |
| Agreement Record | The durable result of a reviewed manifest against owner terms, Core capability, and operator policy. |
| Authorization Grant | The enforceable authorization for one bounded class of operations. |
| Technical Scope | A mechanism-level permission presented to a client, token, or runtime. It cannot exceed an Authorization Grant. |
| Runtime Policy | The current contextual rule evaluation applied when an operation is attempted. |

An independent **application** is not a PIOS **App View**. App Views are Core
surfaces; independent applications may remain useful without PIOS while
integrating through Core interfaces. A publisher may also define a named
Core-dependent companion when that dependency is explicit. The **Core app
(previously known as Corebox)** is a different case: a PIOS-native,
PIOS-dependent owner interface for capture, access, system visibility,
governance, and device-local support, still a Core
client rather than canonical Core state or a required Core runtime. Its device
UI runs on owner devices; its PIOS-specific backend normally belongs inside
the Solo VM. Native status and independent deployment are not synonyms.

Application-specific intelligence does not become Core intelligence because it
runs near Core, uses Core context, or shares a model provider. If an external
processor implements a normative Core capability, its durable inputs,
authority, outputs, provenance, and failure semantics remain Core-scoped even
when execution is physically external.

PIOS-native processing, indexing, retrieval, and orchestration normally belong
in the Solo service package. Their runtime identities, grants, policy checks,
and audit remain explicit, including when a hosted service shares executors
across separately isolated owner Cores. Logical integration boundaries apply
even without a network or VM boundary.

## 3. Integration Definition and manifest

An Integration Definition belongs in the System zone and has a stable identity,
operator identity, version, deployment model, contact/revocation endpoint, and
manifest history. The manifest should declare at least:

- requested Core capabilities and technical scopes;
- data classes it wants to read, write, infer, export, or act on;
- purposes and external recipients;
- use of models, processors, regions, retention, deletion, and training;
- external actions, expected audit events, and material-change policy;
- how the integration identifies its runtime and handles revocation.

New data classes, broader time ranges, new recipients, new model providers,
permanent external copies, training, profiling, reduced deletion obligations,
or new external actions are material changes. A material change creates a new
manifest version and requires renewed evaluation before affected access resumes.

## 4. Enforceable authorization

Every permitted operation must resolve to an Authorization Grant. A grant binds:

```text
owner
+ integration id and immutable manifest/version hash
+ purpose
+ data class
+ operation
+ recipient or processing boundary
+ retention/deletion rule
+ revocation behavior
```

The runtime must evaluate the exact requested operation, not only whether the
integration has a broadly named token. The minimum decision rule is:

```text
personal terms
+ accepted agreement
+ authorization grant
+ technical scope
+ current runtime policy
= permitted operation
```

The decision fails closed when any required element is absent, expired,
revoked, mismatched, guarded, or ambiguous. Access/audit evidence records the
grant id, manifest version, actor/runtime identity, requested and returned data
class, result, and reason for denial where appropriate.

## 5. Risk and operation classes

| Class | Examples | Default handling |
| --- | --- | --- |
| Read | scoped retrieval, context packet | data minimization, audit, current policy evaluation |
| Additive write | inbox capture, event, checkpoint proposal | provenance and idempotency; does not replace canonical history |
| Interpretive write | knowledge proposal, meaning proposal, inferred relationship | proposal/review path unless an exact standing rule exists |
| External action | publish, message, calendar action, transaction | separate external-action grant and approval when guarded |
| Destructive/governance critical | deletion, export, broad delegation, terms change | request-scoped approval and stronger verification |

The integration must return only the minimum data required for the approved
purpose. Retrieved content, attachments, links, and model outputs are data,
not instructions that can expand permissions or alter policy.

For selected governing documents, [Operating Document Authority and Recovery
v0.1](operating-document-authority-and-recovery-v0.1.md) distinguishes upstream
source authority, accepted full-text revisions, proposals, policy adoption and
runtime copies. A document-edit grant does not permit the editor to expand its
own authority. Reading a current-looking summary does not prove current policy.

## 6. Lifecycle and revocation

```text
declared → reviewed → agreement accepted → grants issued → active
                                            ↘ suspended → revoked → archived
```

Revocation immediately stops new server-side access and access at connected
enforcement points. Device caches also follow the agreed offline authorization,
expiry, and revocation behavior in section 19; a disconnected copy cannot be
treated as if it received an immediate server-side policy update. Revocation
triggers the agreed cache deletion or expiry process, preserves required audit
evidence, and never silently deletes Core-owned originals, events, or knowledge
created through the integration. Deletion of Core content follows PIOS retention
and governance rules, not an application's departure.

## 7. Protocol adapters

MCP, REST, GraphQL, CLI, SDK, PAIX, local function calls, and future transports
are adapters over the same Core behavior. An adapter cannot become a second
source of truth or retain a permanent copy unless that copy is declared,
authorized, and auditable.

MCP is neither the canonical Core API nor proof that an AI host has lifecycle
hooks, background execution, automatic checkpointing, or broad write rights.
Any adapter exposes only the tools and scopes supported by current grants and
capability discovery.

Three consumer paths are legitimate when explicitly declared:

| Path | Appropriate role | Contract |
| --- | --- | --- |
| Direct | An app, agent, or service calls a governed PIOS interface | Its own identity, discovered capabilities, grants, and Core references |
| Brokered | The Core app or another authorized adapter receives a handoff or exposes a file projection | Preserve originating actor/provenance, recipient, requested operation, and the applicable grant; never lend the app unrestricted owner credentials |
| Hybrid | Device-local capture or cache combined with direct authorized retrieval | Equivalent identity, version, authority, retry, and conflict semantics across both paths |

A compatible Core still supplies its required versioned API. Consumers are not
required to route every operation through a running Core app process, nor is
every consuming app required to implement its own direct network client.
Compatibility declarations identify actual supported integration capabilities;
ordinary file access through an OS projection does not itself establish
structured PIOS API compatibility.

## 8. Integration capability declarations

Applications and catalog entries must use explicit capability declarations,
not Core Compatibility Levels. Initial names may include:

```text
core_context_read
core_capture_write
core_checkpoint_propose
core_knowledge_propose
core_controlled_sync
core_native_backend
```

Each declaration must identify the supported data classes, direction, and
governance boundary. It is self-declared unless associated conformance evidence
states otherwise.

These names describe integration behavior, not PIOS system membership or
physical placement. In particular, `core_native_backend` alone does not prove
that the declaring application is a PIOS-native system component.

## 9. Conversation checkpoints

A conversation checkpoint is a source-linked event and knowledge proposal,
not a replacement for raw conversation history. It may contain a summary,
decision, insight, task, commitment, open question, or proposed learning.
It records source conversation/message references, originating actor/model,
confidence, evidence links, and promotion status.

An automated checkpoint enters through the inbox/update path. It does not
become canonical knowledge, personal meaning, a standing rule, or a behavioral
change without the appropriate existing PIOS proposal and approval path.

<a id="10-synthetic-example-corebox-boundary"></a>

## 10. Synthetic example: Core app boundary

The Core app is used here to show that even a PIOS-native owner interface needs an
explicit grant. It is not an example of an independently useful non-PIOS app.
Colocating its receiver with Core does not grant authority or make its receiver
database canonical; it must still use the governed Core interface.

An integration manifest may declare a `core_capture_write` capability for a
synthetic fixture profile. That declaration alone authorizes nothing. A valid
synthetic grant must bind the named synthetic integration/runtime, harmless
fixture data class, isolated prefixes, a bounded purpose, and revocation.

A synthetic selector, a real device credential, app networking, and personal
file intake are separate profiles and decisions. Passing synthetic evidence
does not grant any of the latter capabilities or convert a synthetic grant into
a personal-data grant.

## 11. Identity and account separation

An implementation must not collapse these identities into one implicit user
record:

- Core owner identity;
- ecosystem or hosted-service account;
- application identity;
- agent or workflow identity;
- device identity;
- operator identity;
- external processor or model-provider identity.

Each operation records the identities relevant to its authority and provenance.
Changing a Core host may require credentials or device trust to be established
again, but it must not silently replace stable owner, integration, or canonical
record identity with a provider account identifier.

## 12. Personal Terms exposure

Personal Terms and technical scopes are cumulative, not interchangeable. A
useful exposure model has four distinct surfaces:

1. a minimal public baseline suitable for pre-connection compatibility checks;
2. authenticated evaluation of an Integration Manifest;
3. owner review and approval of the integration-specific result; and
4. authorized retrieval of the resulting Agreement Record.

PIOS does not require an owner's complete policy, identity, or private terms to
be publicly discoverable.

## 13. Personal events and security audit

PIOS distinguishes the owner's meaningful event history from high-volume
security and access telemetry.

- The **personal event stream** records durable changes such as an integration
  registration, agreement replacement, permission change, checkpoint, or
  significant completed action.
- The **security/access audit stream** records attempted reads and writes,
  denials, authentication results, runtime identity, grant use, and operational
  anomalies.

Routine access logs should not overwhelm the personal event stream. Significant
incidents or owner-relevant summaries may be promoted into it with provenance.

## 14. Data minimization and untrusted content

An integration receives the minimum information needed for its approved
purpose. Minimization applies before application access, model access, external
processing, logging, and third-party export. Prefer filtered records, excerpts,
bounded context packets, redacted results, aggregates, and expiring references
over broad personal-history disclosure.

Email, web content, documents, messages, metadata, imported files, and model
outputs are untrusted data. Their contents cannot expand permissions, alter
policy, select additional tools, or authorize external actions. Implementations
separate system instructions from retrieved content, validate files and URLs,
restrict tool chaining, enforce policy outside the model, and require stronger
confirmation for sensitive or external actions.

## 15. Agent definition, runtime, memory, and activity

PIOS treats four related concepts separately:

| Concept | Meaning |
| --- | --- |
| Agent Definition | Portable role, purpose, skills, limits, model preferences, and operating instructions. |
| Agent Runtime | The process, machine, provider, or service executing the agent. |
| Agent Memory | Owner-governed information retained in Core for authorized future use. |
| Agent Activity | Events and audit records showing what the agent attempted and produced. |

The runtime may be replaced without replacing the definition or owner-governed
memory. Runtime-local caches, prompts, and service memory do not become
canonical merely because an agent used them.

Separately classify whether the agent implements PIOS or consumes it. A native
intake, knowledge-maintenance, or retrieval agent can be packaged inside Solo;
an independent assistant normally runs outside. Being replaceable, possessing
portable definitions, or retaining Core-governed memory alone does not decide
that classification.

## 16. PIOS Interoperability API Profiles

PIOS interoperability is organized as provider-neutral profiles under the
existing Core Service Interface. The profiles compose existing authority; they
do not create a second API standard or replace `/.well-known/core`, Core
Compatibility Levels, or the export format.

| Profile | Boundary |
| --- | --- |
| Core API profile | References the mandatory versioned Core API for supported capture, retrieval, event, knowledge, and other Core operations. |
| Integration and authorization profile | Defines manifests, agreements, grants, scopes, policy evaluation, revocation, and audit. |
| Agent Tool profile | Exposes named, typed, policy-checked tools over operations already permitted by a grant. |
| Provider Gateway profile | Normalizes a bounded external-provider capability while retaining provider, request, licence, freshness, and processing provenance. |
| Portability profile | References the Core package, export/import, validation, and operationalization contracts. |

The capability document advertises which profile names and versions an
implementation supports. Advertisement is not an authorization grant. A client
must degrade safely when an optional profile is unavailable.

## 17. Provider-result lifecycle

An external-provider response has an explicit Core lifecycle:

| State | Meaning |
| --- | --- |
| Transient response | Used for the current request only; it is not Core state and has no canonical `core://` identity. |
| Retained source evidence | Preserved through the inbound path with provider, request, licence/terms, freshness, integrity, and provenance facts. |
| Canonical event or object | Created only through the applicable event, proposal, confirmation, and authority rules. |
| Derived projection | A summary, normalized result, index, graph, vector, or other rebuildable representation linked to retained evidence and processing version. |

Provider URLs, account identifiers, cache keys, and physical storage references
remain provenance or implementation metadata. A normalized provider response
does not become canonical merely because an adapter returned it.

## 18. Context Receipt

When authorized personal context is returned to an application, agent runtime,
model, provider, or other recipient, Core should retain a Context Receipt or an
equivalent event/audit pair. It binds:

- owner and requesting integration/runtime;
- Authorization Grant and manifest version;
- purpose, recipient, model/provider, and processing boundary;
- requested classes and returned canonical references/versions;
- withheld classes or policy reasons;
- transformations, summaries, redactions, and processing profile versions;
- context-package digest and byte count where retained or transferred;
- retention/expiry and external-copy rule; and
- creation time, result, write-back reference, and revocation relationship.

The receipt records what Core disclosed and under which authority. It does not
prove that an external recipient complied after delivery, and it should not
duplicate raw sensitive context into routine audit records.

## 19. Same-publisher and local-substrate profiles

Applications from one publisher may share a library, app group, cache, staging
store, or projection as an implementation choice. Each application and runtime
still has a distinct identity, manifest version, grants, technical scopes,
audit attribution, and independently revocable access. Direct access to a
shared database is not the interoperability contract.

### 19.1 Core app device support and shared cache

The **Core app**, whose display name is **Core** and previous name is
**Corebox**, supplies PIOS-native device support as well as its owner-facing
interface. Shared caching is a key role on iPhone for participating applications
in the same App Group: keep permitted recently loaded files and projections
locally, support chosen offline content, and remain useful during flaky
connections. Reopening valid cached content should not require downloading the
same bytes again. Refresh or fetch missing/changed versions when connectivity,
freshness requirements, and policy permit; do not implicitly replicate the
owner's entire Core onto every device.

The selected device profile declares which support components, extensions, or
shared libraries perform this work. It must not depend on the foreground Core
app process being continuously available. An independent app using this support
retains its independent product purpose and a declared standalone/fallback path.
The Solo package remains responsible for its promised server-side native
retrieval, indexing, and processing; a device cache does not replace them.

### 19.2 State, freshness, and retention

| Device state | Meaning | Required treatment |
| --- | --- | --- |
| Recent-content cache | A local copy of accepted Core content or an authorized projection | Reuse within the freshness policy; ordinary eviction affects only the local copy |
| Selected offline content | Accepted content retained deliberately for offline use | Respect the declared offline-retention policy; report unavailable or expired content instead of promising a complete local Core |
| Pending capture or edit | Local work not yet accepted by Core, possibly the only copy | Preserve durably until acceptance/reconciliation or an explicit discard decision; never treat it as disposable cache |

Cached entries bind the Core and owner identity, stable logical reference,
revision and integrity information, source/provenance, fetched/validated time,
and permitted sharing/retention boundary. UI and API responses distinguish
cached/stale, pending, accepted, and unavailable state. Offline availability
does not imply freshness, successful Core acceptance, or a current online check.

Reconnection revalidates authority and reconciles versions using declared
idempotency and conflict rules; it does not silently overwrite canonical
records. A Core/account switch must not expose another owner's cache or send
pending work to a different Core. Clearing a cache does not delete Core
Originals, Events, or Knowledge. Selected offline content and pending writes
have separate retention rules from opportunistic recent-content eviction.

### 19.3 Shared-container authority and offline limits

An App Group is a shared trust boundary, not a per-app authorization system.
Any member entitled to read a shared plaintext container can access those bytes;
logical grant checks alone cannot create per-app confidentiality there. Put
only content authorized for every such member into shared plaintext. Data with
different access boundaries belongs in isolated storage or behind an actually
enforced mediated interface. Do not share owner-wide credentials merely to
enable cache reuse.

The profile names the approved shared data set, participating apps, operation
rights, cache lifetime, offline authorization window, and revocation behavior.
Offline access is limited to previously authorized cached content and the
declared offline operations; absent, expired, or ambiguous authority fails
closed. Do not describe a disconnected device as having performed a fresh
server policy check. Stop new server access immediately on revocation; apply
the declared local expiry/removal and reconciliation when the device learns
of the change. Immediate remote erasure of already disclosed bytes on an
offline device cannot be promised. If the authorized set of shared-container
readers changes, the retention/isolation design must address the raw shared
copy, not merely change an API grant while leaving the bytes accessible.

### 19.4 Platform mechanisms and evidence

Apple App Groups support sharing among apps from the same development team and
between an app and its extensions. They are not a universal third-party
interoperability mechanism. On iPhone, use supported extensions, App Groups,
OS-managed file transfers, and background opportunities; do not assume an
always-running cross-app router. A File Provider can expose a selected file
projection to other apps, but it does not expose the whole structured Core
contract. macOS may use separately declared resident helpers without making
that topology a requirement for mobile or for other Core clients.

Platform references: Apple's [Configuring app groups](https://developer.apple.com/documentation/xcode/configuring-app-groups),
[Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app),
and [File Provider](https://developer.apple.com/documentation/fileprovider).
These explain platform mechanisms, not PIOS authorization.

An implementation claims only the cache, handoff, offline, and synchronization
capabilities it has demonstrated. Before activating a shared-cache profile,
show repeated-open reuse, permitted offline reads, reconnect/version handling,
safe eviction without losing pending work, Core/account separation, and the
declared denied-access/expiry behavior. Broader SDK or device-node work is not
a prerequisite to a bounded, useful implementation.

### 19.5 Local Core is a separate claim

Reserve **Local Core** for a local deployment that implements a declared Core
compatibility contract and has explicitly named canonical authority. A local
cache, projection, inbox staging store, or app-group database is not a second
Core and must not create an ambiguous canonical writer. Any later offline sync
profile must define canonical-side, conflict, idempotency, correction,
revocation, deletion, and cutover behavior before writable operation.

### 19.6 PIOS First-Party Mobile Apps by Prifina

The **PIOS First-Party Mobile Apps by Prifina** profile uses a specific same-team
iPhone implementation choice under the general integration model, not a
PIOS-wide requirement. It applies only to applications deliberately admitted
to the shared exchange App Group:

This app profile is deployment-neutral. Core may connect it to a compatible
single-owner, hosted, multitenant, self-hosted or other PIOS implementation.
The mobile contract does not change according to the deployment profile.

- **Notes by Prifina** and **Voice Notes by Prifina** remain independently
  useful local-first products. They may separately offer app-owned iCloud or
  owner-configured custom-endpoint synchronization, but they use Core-mediated
  local handoff for PIOS exchange and do not require a Prifina-operated
  application backend.
- The existing LifeStory application continues as **LifeStory Indie**, keeping
  its existing application identity, installed-user continuity, local data and
  independent device-source behavior. Migration from it is explicit,
  versioned, owner-triggered and non-destructive.
- A separate new **LifeStory** is a Core-dependent companion with a new
  application identity. Core owns its PIOS connection and activated device
  source permissions; LifeStory receives authorized source records or
  projections and returns edits or outputs through the local mediated
  contract.

Core is the default PIOS integration and governance hub for this named profile.
Notes may additionally use its own bounded reconciliation identity to fetch
applicable canonical Note commands and return acknowledgements, while retaining
Core's brokered path. This hybrid exception does not confer general capture,
collection or owner-wide authority, and does not activate another app or source.
The implementation records its actual deployment and granted scopes separately.
The local flow
must use durable queues, stable identities, provenance, acknowledgement and
retry states and must not depend on Core remaining in the foreground. Every
application retains a distinct integration identity, grant and audit
attribution even when bytes use one App Group container. No unrestricted Core
credential is shared.

Third-party applications and other publishers are unaffected. They continue
to select declared direct, brokered or hybrid paths according to their own
capabilities and platform boundaries.

### 19.7 Device-source and working state

The three cache/offline/pending classes in section 19.2 are not an exhaustive
classification of device information. A selected device-support profile also
distinguishes:

| State | Authority and lifecycle |
| --- | --- |
| Device-source record | Source-specific locally retained observation or snapshot; not canonical Core merely through collection, and not pending upload until selected for submission |
| App-owned working record | The independent application's own durable record and revision history; shared transport does not authorize direct edits to its private store |
| Normalized device evidence or local projection | Rebuildable adapter output bound to source identity/version and processing profile; not the unchanged source or proof of canonical acceptance |

Source and working records may be the only retained copy. Cache eviction must
not dispose of them. Their explicit retention, deletion, export and recovery
policies remain separate from cache policy. A backup of accepted Core state
does not prove recovery of device-only sources or pending work.

Device permission, owner selection of collection scope, local use, server
transfer and downstream processing are separate authority decisions. Record
source/installation scope, stable identity, source version, observation and
collection times, activation boundary, adapter version, integrity and coverage
limits. An accessible metadata snapshot is not the original photo or the full
underlying device database. Retain the selected source representation before
deriving from it; declare omissions rather than expanding collection silently.

Core app collection and immediate device preprocessing remain device-side PIOS
functions where the selected profile needs them. Native server ingestion,
cross-source Knowledge compilation, History and retrieval remain server-side
PIOS functions. Both sides are part of PIOS; neither placement makes an output
canonical. Avoid using “PIOS-side” to mean only the server.

### 19.8 Bidirectional working-copy reconciliation

A profile supporting canonical changes back into an application must declare
the canonical side, participating app/device identity, stable object mapping,
source and canonical revisions, command identity, conflict behavior and recovery.
Local save, handoff validation, local semantic application, canonical Core
acceptance, application of a canonical revision and acknowledgement delivery
are separate evidence boundaries. Report only the boundary actually proven.

The application applies an authorized command through its own write contract;
Core must not mutate its private database. Bind the command to the intended
owner/Core, source object, expected source revision and canonical revision.
Duplicate delivery is idempotent. A divergent local edit remains preserved as
a conflict or follows an explicitly declared merge policy; it is not silently
overwritten. A resolution records the selected content and resulting revision.

Keep command, local result and acknowledgement-delivery evidence sufficient to
recover after interruption. A transport acknowledgement is not proof of semantic
application; an unavailable client is not a successful client. Notify/wake hints
do not replace durable reconciliation. Direct and brokered paths must converge
on the same identities, conflict rules and terminal results. Define cursors,
freshness and partial-coverage behavior without imposing one universal polling
interval, cache quota, background-runtime guarantee or merge algorithm.

Existing acknowledgement wire names, including `local_accepted` and `applied`,
must be interpreted by schema, direction, operation and authority boundary.
Do not rename them or silently give an older receipt stronger meaning.
Capability discovery and implementation evidence describe supported behavior;
these profile requirements do not themselves establish a compatibility level.

### 19.9 Response loss and service progress

A timeout or lost response does not prove that the operation was rejected or
that no state changed. Keep acceptance unproved until governed reconciliation
or attributable receipt/state evidence resolves the original operation. Retain
the original operation identity, destination and pending content; do not mint a
new identity merely to retry an uncertain submission. Any retry follows the
declared idempotency, authority and conflict contract, not a blind resubmission.
This is a semantic distinction, not a required new wire-status name.

Implementations should test that a slow or disconnected presentation client does
not indefinitely prevent essential synchronization from progressing. Bound
response work and declare isolation, cancellation and recovery behavior while
preserving write ownership and durable acceptance. Increasing worker counts or
timeouts is not proof of safety. Fault fixtures should cover lost responses
after acceptance, duplicate reconciliation, retained pending work and a stalled
reader alongside synchronization. This specifies observable behavior, not a
universal concurrency architecture or latency target.

## 20. Context compilation and model execution

Context and Meaning are governed information products, not permissions. A
context-compilation or model-execution request must identify the requesting
integration/runtime, purpose, grant, requested data classes, sensitivity
ceiling, freshness, recipient/model/provider, processing region, retention,
training and deletion terms, external-copy behavior, and required output
references.

Model routing is optional and provider-neutral. Cost and latency policy may
choose among otherwise authorized providers, but routing cannot broaden the
candidate context, recipient boundary, or permitted write-back. Caller-supplied
Role or Mode values remain input claims until confirmed through the applicable
Core lifecycle.

## 21. Required future evidence

Before this contract becomes normative, PIOS needs schema validation, an
allowed-operation and denied-operation fixture, revocation evidence, audit
readback, data-minimization evidence, hostile-content fixtures, Context Receipt
fixtures, provider-result lifecycle fixtures, profile-discovery tests, and
proof that a manifest or retrieved instruction cannot bypass runtime
enforcement.

<a id="controlled-disclosure-profile"></a>

## 22. Optional controlled-disclosure profile

Status: optional contract elaboration for PIOS 2.0, not a new mandatory Core
obligation or a claim of implemented enforcement. The requirements in this
section apply only to an implementation profile that explicitly selects it.
Selection does not issue grants or activate recipients. Existing normative
invariants remain unchanged; sections 4, 14, 18–20 and the master's privacy and
context-compilation rules supply the authority model.

This profile reuses Integration Definitions, Personal Terms, Agreement Records,
Authorization Grants, technical scopes, runtime policy and Context Receipts.
It introduces no permission namespace, protocol, required endpoint, wire field,
Core Compatibility Level, API version or export-format change. Its declarations
may be represented through the existing manifest and event/audit mechanisms.

### 22.1 Separate decisions across the information lifecycle

Each selected flow declares its source scope, purpose, actors, processors,
audience, transformations, retention, enforcement points and offline limits.
An existing grant may cover several decisions when its exact scope permits
them; separate decisions do not require a new grant for every step. Reusing a
grant still requires current evaluation, including its manifest binding.

| Decision | Required question within the selected profile |
| --- | --- |
| Access | May this actor retrieve these source revisions or candidate metadata? |
| Use and process | May the named processor receive and use those inputs for this purpose under the stated processing terms? |
| Derive | May this transformation create the proposed result, including cross-source inferences? |
| Disclose | May this representation and its accompanying metadata reach this recipient through this surface? |
| Retain | May each recipient or service keep inputs, outputs, logs or copies, for how long and under which deletion rules? |
| View later | May the current viewer obtain the retained representation now, under current policy or an explicitly bounded offline authorization? |

Permission to read or use content is not permission to disclose, retain or
publish it. Permission to disclose once does not establish perpetual viewing
rights. An integration's access to two sources does not itself authorize their
combination or delivery to a shared audience. Canonical acceptance of a result
does not establish its truth or enlarge its audience.

### 22.2 Authorization before processor disclosure

Evaluate authority before every relevant transfer or action, including local
processing across a logical trust boundary. Filter source records and candidate
metadata before ranking, classification, extraction, summarization or embedding.
Candidate labels, project names, descriptions, examples, relationship links and
candidate-set membership can reveal protected information even without source
bodies. A processor authorized for one document is not thereby authorized for
the complete taxonomy, candidate list or another application's context.

Bind the evaluation to the actual input revisions, purpose, processor/runtime,
model/provider where applicable, processing boundary and terms. Protect request
logs, traces and intermediate results under their own permitted retention and
audience. A final answer filter cannot undo an unauthorized input disclosure.
Instructions in source content, a model's request for more context or a high
classification score cannot authorize an additional transfer.

For example, a classifier permitted to read a synthetic public brief must not
receive a private project name merely because that name is a candidate label.
Use an authorized candidate set, an authorized reduced representation, another
already permitted processing path, or abstain. Record omissions without leaking
withheld names through an error, receipt or preview.

### 22.3 Combined outputs and presentation metadata

A result binds its contributing source revisions and applicable policy
dependencies. Evaluate all contributing constraints for the intended purpose,
recipient and representation: audience, processing, onward use, retention,
deletion, sensitivity and required approval. Select only an outcome satisfying
all applicable constraints; if they conflict or remain unresolved, withhold the
affected output or produce a separately authorized narrower result. Do not
silently choose the least restrictive source policy.

Summarization, aggregation, paraphrase or inferred anonymity does not
automatically declassify information. An authorized release or transformation
rule may permit a particular reduced representation; record that rule and the
result's remaining restrictions. A model's assurance of anonymity is not such
a rule. Excluding a source from the visible citations does not remove its
influence or policy obligations from a derived result.

Apply the same analysis to titles, filenames, thumbnails, previews, snippets,
search listings, notifications, link descriptions and existence indicators.
Generating a safe body while exposing a restricted title is still disclosure.
Receipts and provenance links also have an audience; use scoped references or
bounded explanations where revealing their details is not authorized.

Role and Mode inference, Circle membership and model confidence supply context
for evaluating existing policy; they are not grants or model-issued authority.
They do not authorize canonical promotion, external action or wider disclosure.

### 22.4 Controlled references and disclosed copies

A controlled reference resolves through an enforcement point that checks the
current viewer, requested representation and applicable current policy before
returning content. Possessing or forwarding the reference alone grants no
access. The selected implementation declares authentication, expiry, denial,
cache and offline behavior and where the checks actually occur. Reference
titles and previews require their own disclosure check before resolution.

A materialized copy delivered to another recipient is a disclosure at delivery,
even if it originated from a controlled reference. A downloaded document,
message, notification body, screenshot or remembered observation cannot be
promised recall merely by revoking its source reference. Stop future governed
access and apply the supported deletion/expiry obligations; state where remote
copies, offline devices or third-party behavior are outside enforcement.
Section 19's shared-plaintext and offline limits continue to apply.

Policy metadata describes obligations; it does not itself enforce third-party
behavior or guarantee absolute isolation. A Context Receipt or equivalent
event/audit pair records the actual recipient, representation, grant, source
versions, transformations, retention and external-copy boundary under section
18. It is evidence of the governed disclosure, not proof of subsequent compliance.

### 22.5 Revalidation, reuse and fallback

Revalidate at execution and disclosure, before reuse for another request or
audience, and on later governed access. Recheck relevant source/policy revisions,
grant expiry or revocation, manifest changes, purpose, recipient and retention.
Queued work cannot rely solely on an earlier scheduling decision. Where fresh
checks are unavailable, only the explicitly granted offline window and
operations remain usable; otherwise refuse or report unavailable.

Reuse of a retained processing result requires matching source revisions,
transformation parameters, language and processor/profile version as applicable,
plus currently permitted use and audience. It is different from authorization
to reprocess source data. Historical retention, current disclosure and factual
validity are separate: revocation can restrict a retained result without making
its claim false or erasing canonical Events. Corrections and deletions follow
existing governed lifecycle rules.

A model/provider fallback or retry must not widen input scope, recipients,
retention, training, region, permitted output or write-back authority. Compare
the actual fallback against current grants and terms before transfer; cost,
latency or failure does not waive them. If no authorized alternative exists,
withhold, narrow within existing authority, or seek the required new decision.
Record the actual path and denied boundary without exposing protected context.

Evidence for a selected implementation includes denied candidate-metadata
transfer, incompatible combined-source restrictions, a restricted preview,
grant revocation between queuing and execution, later-view denial, bounded
offline behavior, processing-result reuse and rejection of an unauthorized
fallback. These are validation targets, not completed runtime proofs.
