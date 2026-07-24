# Integration Interoperability and Governance v0.1

Status: draft companion specification for PIOS 2.0. This document defines a
future integration-governance contract. It does not authorize app networking,
personal-data intake, real device credentials, generic API keys, or any
deployment.

## 1. Purpose and boundary

PIOS Core is the durable owner-controlled information foundation. An external
application, agent, source connector, AI service, or protocol adapter can only
operate around that foundation through explicit, continuously evaluated
authority. A manifest is a declaration of requested behavior; it is not proof
of behavior and it creates no authority by itself.

This specification extends the PIOS 2.0 master's Core Service Interface,
agent-definition governance, privacy/access rules, and Core Compatibility
contract. It does not replace the mandatory Core API, `/.well-known/core`, or
Core Compatibility Levels 1–5.

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

An external **application** is not a PIOS **App View**. App Views are Core
surfaces; an application is an independently operated capability that may
integrate with Core.

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

An integration manifest may declare a `core_capture_write` capability for a
synthetic fixture profile. That declaration alone authorizes nothing. A valid
synthetic grant must bind the named synthetic integration/runtime, harmless
fixture data class, isolated prefixes, a bounded purpose, and revocation.

A synthetic selector, a real device credential, app networking, and personal
file intake are separate profiles and decisions. Passing synthetic evidence
does not grant any of the latter capabilities or convert a synthetic grant into
a personal-data grant.

## 11. Required future evidence

Before this contract becomes normative, PIOS needs schema validation, an
allowed-operation and denied-operation fixture, revocation evidence, audit
readback, and proof that a manifest cannot bypass runtime enforcement.
