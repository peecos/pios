# PIOS 2.0

PIOS is the Personal Information Operating System framework: an open reference
model for owner-controlled personal information infrastructure.

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

These documents define the public compatibility target and the separately
gated path from a private owner Core to a future multi-tenant hosted service.
They distinguish published source/templates from proof artifacts, release
candidates, experimental providers, and supported providers.

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
