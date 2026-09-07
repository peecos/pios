# Hosting, Core Boundaries, and Portability Principles v0.1

Status: draft normative architecture companion for PIOS 2.0. This document
defines deployment-independent Core boundaries and portability principles. It
does not authorize deployment, migration, hosted-service operation, app
networking, credentials, or personal-data processing.

## 1. Purpose

PIOS is the open framework and specification. Core is a concrete implementation
of that framework, and Core Self is one owner's running Core instance.

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

Physical location alone does not determine whether something is logically part
of Core. PIOS uses the following categories.

| Category | Meaning | Portability rule |
| --- | --- | --- |
| Normative Core capability | Behavior required by a PIOS/Core compatibility profile. | Every implementation claiming that profile provides equivalent behavior. |
| Canonical Core state | Durable owner state and definitions governed by Core. | Exportable, reconstructable, and expressed without provider-specific meaning. |
| Core capability executor | A replaceable runtime that performs a Core capability. It may run locally, in shared infrastructure, or through an external processor. | Its durable inputs, authority, outputs, provenance, and failure semantics remain Core-scoped. |
| Core interface or adapter | A bounded API, protocol, connector, client adapter, or transport over Core behavior. | It does not become a second source of truth or expose provider internals as the Core contract. |
| Supporting application or service | A capability that uses Core for an application-specific or operator-specific purpose. | It connects through defined interfaces and remains replaceable where practical. |
| Operator control plane | Provisioning, billing, fleet administration, support, abuse controls, service health, and deployment operations. | Required to operate a service at scale, but not automatically part of PIOS or an owner's portable Core. |
| External execution resource | A model, transcription engine, specialist API, or other replaceable processor. | It may execute approved work but does not define canonical Core meaning by itself. |

A capability belongs in the normative Core contract only when compatible Core
implementations reasonably need equivalent owner-facing behavior. Convenience,
colocation, or use by one application or operator is not enough.

## 5. Canonical State and Execution Are Different

PIOS is more than storage, but not every process or runtime belongs in canonical
Core state.

Core may retain:

- originals, events, knowledge, and governed system records;
- owner guidance, policies, permissions, and approved rules;
- agent and workflow definitions;
- skills, routing rules, and retrieval definitions;
- processing manifests, provenance, and durable execution records;
- portable configuration and reconstruction instructions.

Replaceable execution may include:

- workers, queues, schedulers, and orchestration runtimes;
- model inference and model-provider APIs;
- indexes, caches, embeddings, and graph projections;
- deployment-local databases and runtime copies;
- application-specific processing services.

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

## 7. Deployment Profiles

### 7.1 Core Self-Hosted

Core Self-Hosted is a portable distribution operated by the owner or a chosen
operator. It may run on local hardware or a virtual machine in a provider such
as AWS, Google Cloud, Azure, or another compatible environment.

The reference distribution should preserve the distinction among standard Core
behavior, supporting services, and custom Core modifications. An owner remains
free to colocate or modify software, but modifications may affect compatibility
claims and future portability.

### 7.2 Managed Single-Owner Core

A provider-native deployment may operate one owner's Core in a dedicated or
owner-controlled cloud environment. The current AWS reference is a one-owner
pilot/template path. It is not by itself a multi-tenant hosted account service.

### 7.3 Multi-Tenant Core Host

A future multi-tenant host may share processing infrastructure while preserving
independently isolated owner Cores. Shared code and stateless processing are
compatible with this model; shared mutable owner context is not.

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

A Core capability executor may run outside the machine or account holding
canonical Core state and still be logically part of the Core implementation. A
supporting application may run on the same machine as Core and still remain
outside the Core contract.

The required question is not where a process runs, but what contract it
implements, what authority it receives, what state it can affect, and whether
the owner can replace it without redefining their Core.

## 9. Supporting Services and Applications

Applications, device services, notifications, publishing, communication,
specialized transcription, product workflows, and third-party integrations
normally remain outside the Core boundary. They should use defined Core
interfaces rather than provider storage, queues, internal databases, or
operator-only services.

Corebox is one example: it may act as a local-first companion and Core client,
but its application binaries, device state, capture UI, and application
lifecycle are not Core runtime dependencies.

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

1. Is this behavior required by the PIOS/Core contract or only by one product,
   provider, or operating model?
2. What canonical state or definition must remain portable?
3. How can equivalent behavior exist in self-hosted and managed profiles?
4. Does an external client require provider-internal knowledge?
5. Can the capability executor, model, operator, or supporting service be
   replaced without changing the owner's Core identity?
6. What conformance evidence proves the claim?

Equivalent behavior does not require identical implementation. It requires a
versioned capability contract, stable authority and information semantics, and
repeatable evidence.

## 13. Architectural Views

PIOS documentation should keep separate views for:

- the normative PIOS/Core architecture;
- deployment profiles;
- provider-specific implementations;
- applications and supporting services;
- operator control planes.

One diagram should not attempt to represent all five. Combining them makes
provider services look normative and makes supporting products look like Core.

## 14. Final Principle

Applications, services, operators, infrastructure, models, and implementation
technology may change. The owner's canonical state and authority remain bound
to their Core, and the Core remains intelligible through the same logical,
versioned, portable contract.

