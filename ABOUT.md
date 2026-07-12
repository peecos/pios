# About PIOS and the peecos organization

This document covers everything *around* the PIOS framework — the organization, origin, naming, sibling frameworks, governance, licensing, and project structure. The framework itself lives in the [master documentation](index.html) (read online at [peecos.org/pios/master](https://www.peecos.org/pios/master)).

## The organization

**peecos** ("Personal Ecosystem", [peecos.org](https://www.peecos.org)) is the open organization behind **PIOS**, the Personal Information Operating System framework. PIOS is an open reference model for owner-controlled personal information infrastructure: preserved sources, canonical events, structured knowledge, retrieval surfaces, governance, and portable setup paths for agents and applications.

The goal: build computing around the person's durable information and authority, and let AI, interfaces, and runtime services operate inside that foundation rather than above or outside it.

The organization maintains one framework and its surrounding assets:

| Name | What it is |
| --- | --- |
| **peecos** | The open organization, website, and GitHub organization |
| **PIOS** | Personal Information Operating System — the open framework and master documentation (currently PIOS 2.0) |
| **Core** | The implementation running the personal information core |
| **Cotton** | The personal context blueprint: the organizing canon for how personal information is named, classified, and made understandable |
| **Core Self** | A person's own running instance and private source of truth |
| **Core Managed / Core Self-Hosted** | The two deployment profiles: managed service, or a portable VM/server package |

## Origin

PIOS is created and authored by [Valto Loikkanen](https://github.com/valto). PIOS 2.0 is the current generation: a consolidated master documentation covering the Core, Cotton, History, event-log, retrieval, governance, AWS, and self-hosted architecture model.

The older `peecos/pios-global` repository belongs to the pre-PIOS-2.0 documentation era and is archived historical material.

## Why the names

- **Core** is the durable center: one personal information core that preserves originals, records events, maintains living knowledge, and serves derived views. Everything else — agents, apps, interfaces — operates on top of it.
- **Cotton** is the personal fiber: the soft, human material of a life — words, meanings, habits, relationships — organized into a usable structure. Cotton defines how personal information is named, grouped, interpreted, and made understandable to both the owner and their agents.
- **Core Self** names the instance because its owner is the person: it is the person's own private source of truth.

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

**© 2026 Valto Loikkanen / peecos.** PIOS, Core, Cotton, and the peecos organization assets are created and authored by Valto Loikkanen.

| Artifact | License |
| --- | --- |
| Framework documentation (this repository) | [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — see [LICENSE.md](LICENSE.md) and [NOTICE](NOTICE) |
| Public implementation templates (`pios-core-aws-template`, `pios-core-self-hosted`) | Apache License 2.0 |

Recommended attribution: **PIOS 2.0 by Valto Loikkanen / peecos**.

Names and marks (`peecos`, `PIOS`, `PIOS Core`, `Cotton`, and associated logos) may be used for accurate reference but not to imply endorsement — see [TRADEMARKS.md](TRADEMARKS.md).

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

The [Core Distribution and Compatibility Specification v0.1](docs/core-distribution-and-compatibility-spec-v0.1.md) defines what a compatible Core deployment, portable export, and public support claim mean. The associated [roadmap](docs/core-distribution-roadmap-v0.1.md) distinguishes current evidence from future delivery goals.

## Boundary

The framework repositories are documentation and templates. They are not a hosted peecos account service, contain no owner data, and do not authorize any deployment, data migration, connector sync, or production use by themselves.

## Status

| Item | Status |
| --- | --- |
| PIOS 2.0 master documentation | **Published** ([peecos.org/pios/master](https://www.peecos.org/pios/master)) |
| Core Managed AWS template | Published source/template path; implementation readiness is governed separately |
| Core Self-Hosted VM template | Published source/template path; public release/support status is governed separately |
| pios-global reference wiki | Archived (pre-2.0 era) |
| EIOS sibling framework | Independent since 2026-07-08 ([entitycore.org](https://entitycore.org)) |
