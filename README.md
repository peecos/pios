# PIOS 2.0

PIOS is the Personal Information Operating System framework: an open reference
model for owner-controlled personal information infrastructure.

It is an operating system for personal information, not just storage. A running
PIOS system includes its Core, native processing and retrieval services, and
owner interfaces. **Outside Core does not automatically mean outside PIOS or
outside the PIOS Solo VM.**

The current master documentation is published as a standalone HTML document:

```text
index.html
```

Read it online:

```text
https://www.peecos.org/pios/master
```

Everything around the framework — the organization, naming rationale, the EIOS
sibling framework, licensing, and project structure — is in
[ABOUT.md](ABOUT.md).

## What This Repository Contains

- the PIOS 2.0 master documentation;
- the Core, Cotton, History, event-log, retrieval, governance, AWS, and
  self-hosted architecture model;
- the Core distribution, portability, and compatibility contract;
- links to the public implementation template repositories.

## Core Compatibility

- [Core Distribution and Compatibility Specification v0.1](docs/core-distribution-and-compatibility-spec-v0.1.md)
- [Core Distribution and Compatibility Roadmap v0.1](docs/core-distribution-roadmap-v0.1.md)
- [Core Hosted Service Fork Path v0.1](docs/core-hosted-service-fork-path-v0.1.md)
- [Hosting, Core Boundaries, and Portability Principles v0.1](docs/hosting-core-boundaries-and-portability-principles-v0.1.md)

These documents define the public compatibility target, deployment-independent
Core boundaries, and the separately gated path from a private owner Core to a
future multi-tenant hosted service.

The [master's boundary model](index.html#system-core-and-deployment-boundaries)
separates Core contract membership, PIOS system membership, and physical
placement. Solo normally packages Core and selected PIOS-native services
together in its VM as far as practical. Independent applications and assistants
that use PIOS normally run outside it; native device interfaces and declared
external resources have explicit deployment roles.

[Core app (previously known as Corebox)](index.html#core-app-and-independent-applications)
is the PIOS-native owner interface for capture, access, system visibility, and
governance. Its display name is **Core**; it remains a client of the narrower
Core contract. A key iPhone role is shared App Group caching for authorized
apps: reuse recently accessed files, retain selected offline content, and
handle unreliable connections without repeatedly downloading the same bytes.
Pending submissions are protected separately from disposable cache. Shared
storage does not grant access or create another canonical Core.

Independent applications may remain useful without PIOS while integrating
through direct, brokered, or hybrid paths; a running Core app is not a
framework-wide mandatory relay. A named same-publisher app set may
choose a stricter Core-mediated profile when its apps share an Apple App Group.
The **PIOS First-Party Mobile Apps by Prifina** profile keeps Notes and Voice
Notes independently usable, preserves the
existing LifeStory product as **LifeStory Indie**, and defines a new
**LifeStory** as Core-dependent. In that profile Core remains the integration
and governance hub; Notes may additionally use its own bounded direct
reconciliation identity with a brokered fallback. Core owns the new LifeStory's
PIOS connection and device-source collection; third-party integration
choices are unchanged. See the
[device-cache and local-substrate profile](docs/integration-interoperability-and-governance-v0.1.md#19-same-publisher-and-local-substrate-profiles).
These are framework targets, not shipped-feature claims or an identifier/data
migration. Native membership, VM placement, canonical-state authority, and
compatibility claims are not interchangeable.

Prifina intends to make that hosted option available soon. Until Prifina
announces service availability, the framework and templates do not provide
hosted accounts or production API credentials. These documents distinguish
published source/templates from proof artifacts, release candidates,
experimental providers, and supported providers.

## Draft Extension Contracts

These draft companion specifications extend PIOS 2.0 without changing the
current Core compatibility or deployment claims:

- [Integration Interoperability and Governance v0.1](docs/integration-interoperability-and-governance-v0.1.md)
- [Cognitive Memory, Source Discovery, and Derived Representations v0.1](docs/cognitive-memory-source-discovery-and-derived-representations-v0.1.md)
- [PIOS Portability Package v0.1](docs/pios-portability-package-v0.1.md)
- [Ecosystem Participation and Project Catalog v0.1](docs/ecosystem-participation-and-project-catalog-v0.1.md)

Named deployment-neutral product profile:

- [Current mobile contract alignment and implementer reading checkpoint](docs/pios-mobile-contract-alignment-2026-10-08.md)

- [PIOS First-Party Mobile Apps by Prifina](docs/pios-first-party-mobile-apps-by-prifina.md)
- [Current mobile app inventory (September 27, 2026)](docs/pios-first-party-mobile-current-inventory-2026-09-27.md)
- [Local mobile handoff contract v0.1](docs/pios-first-party-mobile-local-handoff-v0.1.md)

They are design contracts, not authorization for app networking, personal-data
intake, generic API credentials, collection, migration, or hosted accounts.

## Implementation Repositories

- AWS template path:
  `https://github.com/peecos/pios-core-aws-template`
- Self-hosted VM path:
  `https://github.com/peecos/pios-core-self-hosted`
- Public website:
  `https://github.com/peecos/peecos-web`

## Boundary

This repository is framework documentation. It is not a hosted peecos account
service, does not include owner data, and does not authorize any deployment,
data migration, connector sync, or production use by itself.

The older `peecos/pios-global` repository belongs to the pre-PIOS-2.0
documentation era and should be treated as archived historical material.

## Local Documentation Checks

Run the naming, device-cache boundary, HTML, and local-link regression checks
without network access or a deployed Core:

```sh
python3 -B -m unittest discover -s tests -v
```

## Open by Design

This is open work. You are welcome to read it, share it, adapt it, translate
it, build independent implementations from it, and fork it. The framework
documentation uses Creative Commons Attribution 4.0 International, so reuse is
welcome with attribution. Names, logos, and claims of official endorsement are
handled separately only to prevent confusion.

See [OPENNESS.md](OPENNESS.md) for a plain-language guide, attribution example,
and the boundary for independent implementations and official identity.

Want to help? See [peecos.org/get-involved](https://www.peecos.org/get-involved)
and [CONTRIBUTING.md](https://github.com/peecos/.github/blob/main/CONTRIBUTING.md).

## License and Attribution

The PIOS 2.0 framework documentation in this repository is licensed under
Creative Commons Attribution 4.0 International (`CC BY 4.0`).

Attribution should be given as:

```text
PIOS 2.0 by Valto Loikkanen / peecos
```

Copyright (c) 2026 Valto Loikkanen / peecos.

The names `peecos`, `PIOS`, `PIOS Core`, `Cotton`, and associated logos or
marks are not licensed under CC BY 4.0. See `TRADEMARKS.md`.
