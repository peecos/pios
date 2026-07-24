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

## 3. Project catalog

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

## 4. Claim states

| State | Meaning |
| --- | --- |
| Self-declared | Maintainer describes behavior; peecos has not independently verified it. |
| Reviewed | Listing or documentation was checked for clarity and obvious boundary issues; this is not a security certification. |
| Experimental | Limited, early, or synthetic evidence exists; not supported for general production use. |
| Supported | Current documented conformance, release, security/cost review, and support boundary exist for the stated scope. |

Listing never implies endorsement, security review, hosted availability,
compatibility beyond the stated capability, or commercial support.

## 5. Licensing and names

PIOS framework documentation is available under Creative Commons Attribution
4.0. Public implementation templates use their repository's permissive
open-source license. Names and logos are protected only to prevent confusion:
an independent project may accurately describe derivation or compatibility but
must not claim to be the official peecos/PIOS initiative or officially endorsed
without explicit authorization.

## 6. Public participation baseline

Public peecos materials should invite people to build, bring, test, and share
work while accurately describing current maturity. PIOS aims to earn, not
declare, de-facto-standard standing through open documentation, independent
implementation, demonstrable portability, and useful interoperability.
