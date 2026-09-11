# Hosting, Core Boundaries, and Portability Principles v0.1

Status: draft normative architecture companion for PIOS 2.0. This document
defines deployment-independent Core and PIOS system boundaries, placement, and
portability principles. Clarified September 11, 2026. It does not authorize
deployment, migration, hosted-service operation, app
networking, credentials, or personal-data processing.

## 1. Purpose

PIOS is the open Personal Information Operating System framework and
specification, not just a storage model. A running PIOS system supplies the
governed machinery to capture, preserve, organize, interpret, retrieve, and use
personal information. Core is its information and authority foundation,
including declared Core capabilities and their executors; Core Self is one
owner's running Core instance. The product names Core Managed and Core
Self-Hosted describe distributions that may also include PIOS-native services
outside the narrower Core contract.

PIOS system membership, Core contract membership, and physical placement are
separate decisions. **Outside PIOS Core does not automatically mean outside
PIOS or outside the PIOS Solo VM.**

A Core may run on local hardware, a dedicated virtual machine, an
owner-controlled cloud account, a managed single-owner environment, or a future
multi-tenant hosting service. Those deployment choices must not redefine the
logical Core contract.

The governing principle is:

> A Core remains the same logical kind of system across deployment profiles
> when it implements the same versioned Core contract and preserves equivalent
> owner-state, authority, interface, and portability semantics.

The shorter phrase **the Core as a Core is a Core** may be used as an
architectural reminder, but compatibility is established through declared
contracts and evidence rather than through the phrase itself.

## 2. Fundamental Promise

A person's Core should remain independently operable and portable while the
hosting provider, operator, applications, supporting services, processing
infrastructure, AI models, and other surrounding systems may change.

An owner should be able to move among compatible implementations, select Core
hosting independently from supporting services where practical, replace
applications and models, and continue operating without one provider becoming
the hidden definition of Core.

Portability is therefore a system architecture property, not only an export
feature.

## 3. Deployment-Independent Core Contract

PIOS defines the required information model, behavior, authority boundaries,
interfaces, portability requirements, and conformance expectations. A
PIOS-compatible Core implements them.

The normative architecture must not depend on:

- a cloud provider;
- a virtual-machine or serverless topology;
- a particular database, object store, queue, or search engine;
- a hosting company or operator;
- an application or device ecosystem;
- an AI model or model provider.

Different implementation profiles may use very different physical mechanisms
while satisfying the same logical contract.

## 4. Core Boundary Taxonomy

### 4.1 Three separate boundaries

| Boundary | Question | Rule |
| --- | --- | --- |
| Core contract | Does this implement declared Core behavior or govern Core state? | Core includes capabilities and execution, not only authoritative storage. |
| PIOS system | Does this implement PIOS itself, or an independent product that uses PIOS? | PIOS-native services and interfaces can belong to PIOS without belonging to the narrower Core contract. |
| Physical deployment | Where should this component run in the selected profile? | Being outside Core does not require another VM; being colocated does not confer Core membership or authority. |

State treatment is a further distinction: authoritative records, rebuildable
Derived representations, transient runtime state, and secrets have different
lifecycle and recovery rules. That distinction does not decide system
membership. Rebuildable does not mean outside PIOS; replaceable does not mean
an independent application.

### 4.2 Component roles

Classify components by the behavior they implement, not by labels such as
agent, application, connector, worker, index, or runtime. PIOS uses the
following categories.

| Category | Meaning | Portability rule |
| --- | --- | --- |
| Normative Core capability | Behavior required by a PIOS/Core compatibility profile. | Every implementation claiming that profile provides equivalent behavior. |
| Canonical Core state | Durable owner state and definitions governed by Core. | Exportable, reconstructable, and expressed without provider-specific meaning. |
| Core capability executor | A replaceable runtime that performs a Core capability. It may run locally, in shared infrastructure, or through an external processor. | Its durable inputs, authority, outputs, provenance, and failure semantics remain Core-scoped. |
| Core interface or adapter | A bounded API, protocol, connector, client adapter, or transport over Core behavior. | It does not become a second source of truth or expose provider internals as the Core contract. |
| PIOS-native supporting service | Implements the PIOS operating environment beyond the narrower declared Core contract, such as a PIOS-specific gateway or system inspection service. | Part of the selected PIOS distribution; preserve its portable definitions, dependencies, and reconstruction path without making all of its runtime state canonical. |
| PIOS-native interface | An owner interface whose product purpose is to operate PIOS, such as Corebox. | Part of PIOS but a client of Core; replaceable through defined interfaces and not a prerequisite for headless Core operation. |
| Independent application, agent, or service | Has a useful purpose apart from PIOS and integrates with Core for that purpose, such as a notes application or LifeStory. | Remains independently useful; connects through defined interfaces without becoming part of PIOS merely through integration. |
| Operator control plane | Provisioning, billing, fleet administration, support, abuse controls, service health, and deployment operations. | Required to operate a service at scale, but not automatically part of PIOS or an owner's portable Core. |
| External execution resource | A model, transcription engine, specialist API, or other replaceable processor. | It may execute approved work but does not define canonical Core meaning by itself. |

A capability belongs in the normative Core contract only when compatible Core
implementations reasonably need equivalent owner-facing behavior. Convenience,
colocation, or use by one application or operator is not enough. Conversely,
absence from the mandatory Core contract is not proof that a component is
outside the PIOS system. PIOS-native membership does not automatically make an
optional service mandatory for every compatibility profile.

## 5. Canonical State and Execution Are Different

PIOS is more than storage. Its native processing, orchestration, knowledge
maintenance, indexing, and retrieval are part of the operating system even
when their particular executors are replaceable. Not every process or runtime
belongs in canonical Core state, and not every PIOS-native service is a
mandatory Core capability.

Core may retain:

- originals, events, knowledge, and governed system records;
- owner guidance, policies, permissions, and approved rules;
- agent and workflow definitions;
- skills, routing rules, and retrieval definitions;
- processing manifests, provenance, and durable execution records;
- portable configuration and reconstruction instructions.

The Core Derived zone may hold governed, rebuildable text, indexes, embeddings,
graphs, and other projections. They are not independent canonical truth, but
they can be part of Core's retrieval implementation.

Replaceable execution may include:

- workers, queues, schedulers, and orchestration runtimes;
- model inference and model-provider APIs;
- indexes, caches, embeddings, and graph projections;
- deployment-local databases and runtime copies;
- application-specific processing services.

This list describes replaceability, not a placement rule. An index used to
provide PIOS retrieval belongs to the PIOS implementation; an independent
application's private index serves that application. A general-purpose engine
may implement either role, so the deployment must name which behavior it
provides and how it is governed.

Execution results become Core state only through the applicable provenance,
validation, authority, and promotion rules.

## 6. Intelligence and Models

PIOS defines how owner-governed intelligence is represented and controlled. A
Core may retain agent definitions, skills, guidance, policies, workflows,
retrieval rules, and the provenance of intelligent processing.

Models provide replaceable execution capacity. A Core capability may use local
models, hosted models, specialized processors, or combinations of them without
making one provider part of the PIOS definition.

This principle can be summarized as:

> PIOS defines and governs the owner's durable intelligence configuration;
> models and runtimes execute bounded work against it.

Application-specific intelligence remains outside the normative Core unless it
is deliberately adopted through the PIOS specification process. Running near
Core or using Core's model infrastructure does not make an application workflow
a Core capability.

Likewise, an agent implementing PIOS intake, knowledge maintenance, retrieval,
or system orchestration is not external to PIOS merely because it is an agent.
An independent assistant using those capabilities is a consumer. Both remain
subject to explicit authority; PIOS-native status is not unrestricted access.

## 7. Deployment Profiles

### 7.1 Core Self-Hosted

Core Self-Hosted is a portable distribution operated by the owner or a chosen
operator. It may run on local hardware or a virtual machine in a provider such
as AWS, Google Cloud, Azure, or another compatible environment.

The reference distribution should preserve the distinction among standard Core
behavior, PIOS-native supporting services and interfaces, independent
applications, and custom Core modifications.

For the single-owner **PIOS Solo** VM packaging model, the default is a complete
PIOS operating environment: place Core and the selected PIOS-native services
inside the Solo VM as far as practical. This includes native ingestion,
processing, orchestration, knowledge maintenance, indexing, retrieval,
projections, and PIOS-specific gateways needed by the selected profile. It is
not a requirement to install every optional capability or use a particular
database, model, or runtime.

A versioned data-empty golden image or equivalent install composition should
package those services and their reconstruction configuration, not merely
storage. Owner data and secrets are supplied separately through governed
initialization and recovery. A general Agent/Services VM is for independent
applications, assistants, and workflows that use PIOS, not the default home for
PIOS's own information-processing machinery.

Device interfaces necessarily run on owner devices. Selected models, external
source systems, independent recovery storage, or justified processing resources
may remain elsewhere. A split PIOS-native service must be documented as part
of the PIOS deployment, with its purpose, authority, dependencies, and recovery
or replacement path; it must not be relabelled an independent consumer merely
because it runs elsewhere.

Owners may choose another topology or colocate independent applications.
Colocation alone neither confers nor removes compatibility; changes to the
declared contract require matching conformance evidence. A complete single-VM
PIOS package is an intended architecture, not an exception to a Core-only-VM
rule.

### 7.2 Provider-Managed Single-Owner Deployment

A provider-native deployment may operate one owner's Core in a dedicated or
owner-controlled cloud environment. The current AWS reference is a one-owner
pilot/template path. This is an operating arrangement, not a third Core
compatibility profile, and it is not by itself a multi-tenant hosted account
service.

### 7.3 Multi-Tenant Core Host

A future multi-tenant host may share processing infrastructure while preserving
independently isolated owner Cores. Shared code and stateless processing are
compatible with this model; shared mutable owner context is not.

Shared workers may implement PIOS/Core capabilities for many independently
isolated Cores without belonging to any one owner's VM or exported payload.
They remain PIOS capability execution, not merely independent applications
using PIOS. This hosted topology does not require native services to be
externalized from a single-owner Solo VM.

Every work unit must identify:

- the exact Core and owner context;
- the authority and policy under which it runs;
- the information it may read;
- where outputs may be written;
- which guidance and skills apply;
- the lifetime and cleanup requirements for temporary context.

Provisioning, billing, fleet operations, tenant administration, and support are
operator control-plane capabilities rather than automatic additions to PIOS.

## 8. Logical and Physical Separation

Logical boundaries are mandatory. Physical separation is a deployment choice.

There is no universal rule that non-Core means non-PIOS, or that a PIOS service
outside the narrower Core contract must be outside the PIOS VM. The Solo
packaging default in Section 7.1 keeps PIOS-native services together while
preserving logical interfaces and separate authority.

A Core capability executor may run outside the machine or account holding
canonical Core state and still be logically part of the Core implementation.
This is possible in single-owner as well as multi-tenant deployments. A
PIOS-native gateway may be inside the Solo VM and outside the Core contract;
an independent application may be colocated without becoming part of PIOS.

The required question is not where a process runs, but what contract it
implements, what authority it receives, what state it can affect, and whether
the owner can replace it without redefining their Core.

## 9. Supporting Services and Applications

### 9.1 Corebox: a PIOS-native hub and gateway

Corebox's product purpose is to act as the owner's hub/gateway application for
PIOS, whether Solo or hosted. It is PIOS-dependent by purpose, not a typical
independently useful application that happens to integrate with PIOS.
Local-first capture, offline staging, and disconnected operation support that
purpose; they do not change its classification.

Corebox is part of PIOS while remaining a client outside the narrower Core
contract. Its device binaries and device state stay on owner devices. Its
PIOS-specific backend or receiver normally belongs inside the Solo VM, through
a bounded Core interface. Core must remain operable without the particular
Corebox UI or implementation; another authorized interface may replace it.

PIOS membership and VM colocation do not make receiver databases, device
caches, or synchronized folders canonical Core state. A receiver retaining
unregistered originals still requires a governed canonicalization path; moving
it to another VM is not a substitute for that correction. A PIOS-only gateway
is not a placement exception simply because it is outside Core proper.

### 9.2 Independently useful applications and agents

A notes application, LifeStory, or a general-purpose assistant has a useful
purpose without PIOS. Such products should retain meaningful independent
operation while offering deeper integration with Solo or hosted PIOS. Their
application-specific workflows and private processing normally run outside the
Solo VM and use defined Core interfaces, not provider storage, internal
databases, or operator-only access.

PIOS-native notification, projection, connector, or processing services are
not automatically in this class. Classify each by whether it implements PIOS
or an independent product. Shared publisher, branding, programming language,
or ability to execute standalone is not sufficient to decide.

Core hosting and supporting-service provision should remain independently
selectable where reasonably possible. A compatible service should be able to
follow an owner from one Core host to another through a bounded reconfiguration
and reauthorization process.

## 10. Three Dimensions of Portability

### 10.1 State portability

Canonical owner state can move between compatible implementations with stable
logical identifiers, provenance, integrity evidence, unknown-extension
preservation, and documented reconstruction rules.

### 10.2 Operational portability

The destination can operate the imported Core with equivalent behavior,
including required interfaces, authority semantics, processing definitions,
retrieval behavior, recovery, and auditability.

For a complete PIOS distribution, also identify the selected PIOS-native
services and prove their reconstruction or replacement. Restoring source bytes
without restoring the promised search, knowledge processing, or native gateway
does not prove that the full operating environment is recovered.

### 10.3 Ecosystem portability

Applications and supporting services can reconnect to the destination without
depending on the previous host's internal infrastructure.

Ecosystem portability does not mean that credentials, device trust, or owner
approval can always be copied. Security-sensitive integrations may require new
credentials, device enrollment, trust verification, or owner authorization.

## 11. Core Connection Profile

Applications should localize the information needed to connect to a compatible
Core rather than scatter deployment assumptions through their code.

A Core Connection Profile is a client-side abstraction over the existing Core
connectivity contract. It may identify:

- Core endpoint;
- supported protocol or API version;
- capability-discovery location;
- private owner or tenant context where required;
- authentication method and credential reference;
- locally selected capability profile.

The profile contains no secret values when a secure credential reference can be
used. Public capability discovery, private owner binding, device enrollment,
and authorization grants remain distinct. A connection profile does not grant
authority by itself.

The ideal migration changes only localized connection and trust configuration.
It must not require an application redesign around the destination provider.

## 12. Portability and Conformance Audit

Every major capability decision should answer:

1. Does this implement a declared Core capability, a PIOS-native supporting
   service/interface, an independent consumer, or operator/provider machinery?
2. What canonical state or definition must remain portable?
3. How can equivalent behavior exist in self-hosted and managed profiles?
4. Does an external client require provider-internal knowledge?
5. Can the capability executor, model, operator, or supporting service be
   replaced without changing the owner's Core identity?
6. What conformance evidence proves the claim?
7. Is physical placement explicit and consistent with the selected profile,
   including reasons and reconstruction paths for PIOS-native services split
   from the Solo VM?

Equivalent behavior does not require identical implementation. It requires a
versioned capability contract, stable authority and information semantics, and
repeatable evidence.

## 13. Architectural Views

PIOS documentation should keep separate views for:

- the PIOS system boundary, including Core, native services, and native interfaces;
- the narrower normative Core contract and canonical-state boundary;
- deployment profiles;
- provider-specific implementations;
- independent applications, agents, and integrations;
- operator control planes.

Do not collapse these views into a single inside/outside line. That makes
provider services look normative, native services look external to PIOS, or
every colocated product look like Core. Deployment diagrams should label
logical membership separately from machine boundaries.

## 14. Final Principle

Applications, services, operators, infrastructure, models, and implementation
technology may change. The owner's canonical state and authority remain bound
to their Core, and the Core remains intelligible through the same logical,
versioned, portable contract.
