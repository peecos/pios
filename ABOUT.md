# About PIOS and the peecos organization

This document covers everything *around* the PIOS framework — the organization, origin, naming, sibling frameworks, governance, licensing, and project structure. The framework itself lives in the [master documentation](index.html) (read online at [peecos.org/pios/master](https://www.peecos.org/pios/master)).

## The organization

**peecos** ("Personal Ecosystem", [peecos.org](https://www.peecos.org)) is the open organization behind **PIOS**, the Personal Information Operating System framework. PIOS is an open reference model for owner-controlled personal information infrastructure: preserved sources, canonical events, structured knowledge, retrieval surfaces, governance, and portable setup paths for agents and applications.

The goal: build computing around the person's durable information and authority. PIOS is the operating system that preserves, organizes, interprets, retrieves, and governs that information, not merely a storage foundation for unrelated computation.

Core contract membership, membership in the complete PIOS system, and physical placement are separate. PIOS-native services and interfaces can be outside the narrower Core contract while remaining part of PIOS and its Solo VM. Solo normally packages Core and selected native services together as far as practical; independent applications and assistants that use PIOS normally run outside it. See the [master's boundary model](index.html#system-core-and-deployment-boundaries).

The organization maintains one framework and its surrounding assets:

| Name | What it is |
| --- | --- |
| **peecos** | The open organization, website, and GitHub organization |
| **PIOS** | Personal Information Operating System — the open framework and master documentation (currently PIOS 2.0) |
| **Core** | The implementation running the personal information core |
| **Cotton** | The personal context blueprint: the organizing canon for how personal information is named, classified, and made understandable |
| **Core Self** | A person's own running instance and private source of truth |
| **Core Managed / Core Self-Hosted** | The two deployment profiles: managed service, or a portable VM/server package |
| **PIOS Solo** | A complete single-owner PIOS operating environment, normally packaging Core and selected native services together in its VM |
| **Corebox** | The PIOS-native owner hub/gateway application for Solo or hosted PIOS; part of PIOS but a client of Core |

## Origin

PIOS is created and authored by [Valto Loikkanen](https://github.com/valto). PIOS 2.0 is the current generation: a consolidated master documentation covering the Core, Cotton, History, event-log, retrieval, governance, AWS, and self-hosted architecture model.

The older `peecos/pios-global` repository belongs to the pre-PIOS-2.0 documentation era and is archived historical material.

## Why the names

- **Core** is the durable center: one personal information core that preserves originals, records events, maintains living knowledge, and serves derived views through declared capabilities and their executors. Native PIOS services and interfaces complete the operating environment; independent applications use its governed interfaces. Replaceable execution does not mean non-PIOS execution.
- **Cotton** is the personal fiber: the soft, human material of a life — words, meanings, habits, relationships — organized into a usable structure. Cotton defines how personal information is named, grouped, interpreted, and made understandable to both the owner and their agents.
- **Core Self** names the instance because its owner is the person: it is the person's own private source of truth.

Corebox is PIOS-dependent by product purpose, unlike independently useful notes
applications, LifeStory, or general-purpose assistants. Its device interface
runs on owner devices; its PIOS-specific backend can live inside Solo without
making its receiver state canonical Core. Core itself remains operable without
the particular Corebox implementation. See [Corebox and independent applications](index.html#corebox-and-independent-applications).

## Sibling framework: EIOS

On **2026-07-08**, **EIOS** (Entity Information Operating System, [entitycore.org](https://entitycore.org), [github.com/entity-core](https://github.com/entity-core)) was founded as an independent sibling framework, forked from PIOS 2.0 with permission and attribution. Where PIOS is centered on an individual person, EIOS is centered on an entity — a company, cooperative, association, or other structured organization.

The relationship is governed by four rules:

1. **Copy at fork, not shared dependency.** Principles, terms, and patterns inherited from PIOS were copied into EIOS at fork point. Neither framework references the other as a live dependency.
2. **Attribution carries lineage.** EIOS credits PIOS as its origin; recognition flows through attribution, not name matching.
3. **No backwards compatibility.** Neither framework constrains the other; inherited terms may be redefined on either side without coordination.
4. **Divergence is documented.** EIOS records inherited terms and their divergences in its own naming and terminology mapping.

EIOS's names extend PIOS metaphors into entity scale: Core became **Keel** (the structural spine of a vessel), Cotton became **Weave** (personal fiber, woven into entity fabric).

## Canonical source and document policy

- **The [peecos/pios](https://github.com/peecos/pios) repository is the canonical source of the PIOS 2.0 framework documentation.** The master documentation is published as a standalone HTML document (`index.html`), readable online at [peecos.org/pios/master](https://www.peecos.org/pios/master).
- Derived renders and summaries (including the website's overview pages) never diverge intentionally; if they disagree with this repository, this repository wins.

## Licensing

**© 2026 Valto Loikkanen / peecos.** PIOS, Core, Cotton, and the peecos organization assets are created and authored by Valto Loikkanen, and made open on purpose — use them, share them, build on them.

| Artifact | License |
| --- | --- |
| Framework documentation (this repository) | [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE.md](LICENSE.md) and [NOTICE](NOTICE) |
| Public implementation templates (`pios-core-aws-template`, `pios-core-self-hosted`) | Apache License 2.0 |

A simple credit is appreciated: **PIOS 2.0 by Valto Loikkanen / peecos**.

The `peecos`, `PIOS`, `PIOS Core`, `Cotton` names and logos are yours to use for talking about or building on the project — see [TRADEMARKS.md](TRADEMARKS.md) for the one boundary (not implying official status you don't have).

## Open participation

peecos connects independently developed work around PIOS; it does not absorb
it. People may build applications, agents, skills, connectors, Core
implementations, hosting services, research, or compatibility bridges in their
own repositories and under their own licenses and business models.

**Want to get involved?** See [peecos.org/get-involved](https://www.peecos.org/get-involved)
for ways to contribute, propose a project, or plug in — and
[CONTRIBUTING.md](https://github.com/peecos/.github/blob/main/CONTRIBUTING.md)
for repository-level contribution guidelines.

The [Ecosystem Participation and Project Catalog v0.1](docs/ecosystem-participation-and-project-catalog-v0.1.md)
sets the public participation baseline. A listing may be self-declared,
reviewed, experimental, or supported, but listing never implies endorsement,
security review, hosted availability, or support beyond the exact stated scope.

## Project structure

| Where | What |
| --- | --- |
| [peecos.org](https://www.peecos.org) | Public home of the framework: overview, start path, and the navigable master documentation |
| [github.com/peecos/pios](https://github.com/peecos/pios) | This repository — the canonical PIOS 2.0 framework documentation |
| [github.com/peecos/pios-core-aws-template](https://github.com/peecos/pios-core-aws-template) | Core Managed AWS self-setup template for one-owner Core infrastructure |
| [github.com/peecos/pios-core-self-hosted](https://github.com/peecos/pios-core-self-hosted) | Core Self-Hosted VM template and release tooling |
| [github.com/peecos/brand](https://github.com/peecos/brand) | Visual design guide: logo, typography, colors, component conventions |
| [github.com/peecos/media](https://github.com/peecos/media) | Overview media: video, audio, and the architectural manifesto |
| valto@valtoai.com | Contact |

The [Core Distribution and Compatibility Specification v0.1](docs/core-distribution-and-compatibility-spec-v0.1.md) defines what a compatible Core deployment, portable export, and public support claim mean. The [Hosting, Core Boundaries, and Portability Principles v0.1](docs/hosting-core-boundaries-and-portability-principles-v0.1.md) distinguishes Core capabilities, state and executors; PIOS-native supporting services and interfaces; independent consumers; and operator/provider machinery. It separates these logical roles from physical placement. The associated [roadmap](docs/core-distribution-roadmap-v0.1.md) distinguishes current evidence from future delivery goals. A possible hosted multi-tenant service is governed separately by the [Core Hosted Service Fork Path v0.1](docs/core-hosted-service-fork-path-v0.1.md). Prifina intends to make that hosted option available soon; it is not supplied by the templates.

## Boundary

The framework repositories are documentation and templates. They are not a hosted peecos account service, contain no owner data, and do not authorize any deployment, data migration, connector sync, or production use by themselves. Prifina will announce when hosted accounts, production API credentials, and service terms become available. Any hosted service requires a separately ratified product, security, support, and operations path.

## Status

| Item | Status |
| --- | --- |
| PIOS 2.0 master documentation | **Published** ([peecos.org/pios/master](https://www.peecos.org/pios/master)) |
| Core Managed AWS template | Published source/template path; implementation readiness is governed separately |
| Core Self-Hosted VM template | Signed data-empty ARM64 Starter v0.1.0 published; provider support and owner-operation status remain separately governed |
| pios-global reference wiki | Archived (pre-2.0 era) |
| EIOS sibling framework | Independent since 2026-07-08 ([entitycore.org](https://entitycore.org)) |
