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
surfaces; independent applications such as notes or LifeStory should remain
useful without PIOS while integrating through Core interfaces. **Corebox** is
a different case: a PIOS-native, PIOS-dependent owner hub/gateway, still a Core
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

## 6. Lifecycle and revocation

```text
declared → reviewed → agreement accepted → grants issued → active
                                            ↘ suspended → revoked → archived
```

Revocation immediately stops new access. It triggers the agreed cache deletion
or expiry process, preserves required audit evidence, and never silently
deletes Core-owned originals, events, or knowledge created through the
integration. Deletion of Core content follows PIOS retention and governance
rules, not an application's departure.

## 7. Protocol adapters

MCP, REST, GraphQL, CLI, SDK, PAIX, local function calls, and future transports
are adapters over the same Core behavior. An adapter cannot become a second
source of truth or retain a permanent copy unless that copy is declared,
authorized, and auditable.

MCP is neither the canonical Core API nor proof that an AI host has lifecycle
hooks, background execution, automatic checkpointing, or broad write rights.
Any adapter exposes only the tools and scopes supported by current grants and
capability discovery.

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

## 10. Synthetic example: Corebox boundary

Corebox is used here to show that even a PIOS-native hub/gateway needs an
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

Reserve **Local Core** for a local deployment that implements a declared Core
compatibility contract and has explicitly named canonical authority. A local
cache, projection, inbox staging store, or app-group database is not a second
Core and must not create an ambiguous canonical writer. Any later offline sync
profile must define canonical-side, conflict, idempotency, correction,
revocation, deletion, and cutover behavior before writable operation.

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
