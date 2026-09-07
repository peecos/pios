# Ecosystem Participation and Project Catalog v0.1

Status: draft public-governance companion for peecos. This document describes
discoverability and accurate claims; it does not grant approval, endorsement,
or support to a listed project.

## 1. Principle

peecos connects independent work around PIOS; it does not absorb it. A project
keeps its own repository, maintainers, name, roadmap, reputation, license,
hosting model, and business model. Anyone may build with PIOS, for PIOS, or
around a compatible ecosystem without central permission.

## 2. Ways to participate

People may propose an idea, build an application or agent, adapt an existing
open-source project, create a connector/skill/importer, operate a compatible
Core or hosted service, contribute documentation/testing, or publish a
compatibility bridge. Ideas are invitations, not assigned work or exclusive
roadmap items.

## 3. Compatibility bridges

An existing project may add a deliberately limited PIOS path without replacing
its current architecture:

| Bridge | Declared behavior |
| --- | --- |
| Capture Bridge | Sends selected originals, events, or checkpoints into Core. |
| Context Bridge | Reads a bounded set of authorized Core context. |
| Sync Bridge | Exchanges a declared information set in both directions with conflict and retry semantics. |
| Archive Bridge | Preserves completed, historical, or important information in Core. |
| Agent Bridge | Exposes an application or service through a bounded PIOS-compatible agent or protocol adapter. |

Bridge names are plain-language capability descriptions, not Core Compatibility
Levels. A project states data direction, information classes, authority,
retention, and evidence for the exact bridge it claims.

## 4. Project catalog

A catalog entry should point outward and contain:

```text
project name and URL
repository and maintainers
project type and hosting model
license
integration capability declaration
claim/review status
security/privacy/retention notes
known limits and last-reviewed date
```

Integration capability declarations describe actual behavior such as Core
context read, Core capture write, checkpoint proposal, controlled sync, or
Core-native backend. They are not Core Compatibility Levels.

## 5. Project proposal and README baseline

A lightweight proposal should identify the problem, intended users, possible
PIOS relationship, project type, related work, open questions, first experiment,
maintainers, and current state. Ideas are invitations, not assigned work or
exclusive roadmap commitments.

An independent project's README should identify its maintainers, repository,
license, hosting model, supported PIOS capabilities, data directions, privacy
boundary, evidence status, and known limits. It should state that the project is
independently developed unless explicit authorization permits an official or
endorsed claim.

## 6. Claim states

| State | Meaning |
| --- | --- |
| Self-declared | Maintainer describes behavior; peecos has not independently verified it. |
| Reviewed | Listing or documentation was checked for clarity and obvious boundary issues; this is not a security certification. |
| Experimental | Limited, early, or synthetic evidence exists; not supported for general production use. |
| Supported | Current documented conformance, release, security/cost review, and support boundary exist for the stated scope. |

Listing never implies endorsement, security review, hosted availability,
compatibility beyond the stated capability, or commercial support.

## 7. Practical forkability and independent operation

Open licensing alone is insufficient when nobody outside the original project
can understand or continue the work. The public commons should progressively
include specifications, schemas, fixtures, validators, build and deployment
instructions, compatibility evidence, decision rationale, and enough source to
support an independent implementation.

peecos is a discovery and coordination surface, not a permission layer. Absence
from its catalog does not make an independent implementation invalid. Hosted
providers and compatible ecosystems may differ and compete without acquiring
exclusive rights to PIOS.

## 8. Licensing and names

PIOS framework documentation is available under Creative Commons Attribution
4.0. Public implementation templates use their repository's permissive
open-source license. Names and logos are protected only to prevent confusion:
an independent project may accurately describe derivation or compatibility but
must not claim to be the official peecos/PIOS initiative or officially endorsed
without explicit authorization.

## 9. Public participation baseline

Public peecos materials should invite people to build, bring, test, and share
work while accurately describing current maturity. PIOS aims to earn, not
declare, de-facto-standard standing through open documentation, independent
implementation, demonstrable portability, and useful interoperability.
