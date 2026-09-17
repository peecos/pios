# Source discovery and owner-knowledge source context

This reference preserves cross-cutting context for candidate-only source discovery, owner implementation documentation, and knowledge-layer integrity assessment. It does not make a particular wiki, vault, sync service, query plugin, crawler, or agent runtime mandatory.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework and cognitive-memory companion | architecture and lifecycle authority | candidate-only discovery, separation from registration/collection, discovery-record fields, Knowledge Compilation, source links, generated indexes, maintenance/lint boundaries, owner authority and projection status | shipped discovery crawlers, one wiki layout, one lint engine, or production availability |
| Historical PIOS Global at the selected revision | historical design and realization evidence | source categories/trust, source-vs-import distinctions, owner-editable implementation documentation, reference/implementation separation, local knowledge-environment patterns and Dataview checks | current architecture authority, master-data location, mandatory Obsidian/iCloud structure, or current runtime behavior |
| Restricted application evidence `RAS-01` | requirements and bounded realization evidence | existing source-registration/import and knowledge-related structures assessed in earlier tranches | source-discovery candidates, owner implementation-documentation lifecycle, knowledge linting, tests, deployment, or production behavior |

## Source lifecycle boundary

| Stage | Outcome | Reuse or capability |
|---|---|---|
| Discovery | Candidate locations and metadata only | discover a candidate information source |
| Candidate review | Evidence and suitability assessment | conduct a structured review |
| Permission decision | Owner/policy disposition | decide a governed proposal or applicable authorization |
| Registration | Governed recurring source definition | register a connected source |
| Backfill | Bounded historical intake | ingestion screening/readiness/authorization and import session |
| Incremental collection | Ongoing source intake | registered-source and connector profile |

Discovery never grants a later stage. Registration does not authorize backfill, and backfill does not authorize ongoing collection.

## Owner knowledge boundary

- Owner implementation documentation explains the actual system, decisions and configuration relationships. It remains distinct from neutral PIOS reference material, personal knowledge notes, canonical runtime definitions and source code.
- A wiki/vault arrangement is one realization. The reusable outcome is direct owner-readable, owner-editable, versioned implementation documentation with governed references.
- Agent behavior files and canonical agent definitions use their own lifecycle; implementation documentation may link to them but does not silently become their source of truth.
- Shared-folder synchronization, aliases, filesystem paths and specific applications are implementation choices. The historical master-location relationship between local knowledge and cloud/Core state remains unresolved.
- Generalizing an owner-specific implementation discovery into the public reference framework is a contribution/publication workflow, not automatic knowledge synchronization.

## Knowledge maintenance boundary

- Knowledge compilation creates and maintains source notes, concepts, entities, summaries, links, indexes, contradictions, synthesis and maintenance flags through several existing capabilities.
- Integrity assessment is the bounded read/evaluate outcome that finds structural, evidentiary, semantic, lifecycle and safety problems.
- Repair reuses note revision, contextual classification, proposal, concept lifecycle, access governance, index rebuild or other domain capabilities. An assessment does not gain mutation authority.
- Dataview queries, scripts and agent skills are realization tools. They are not capabilities merely because they produce useful maintenance views.

## Documentation and realization reconciliation

Current PIOS defines source discovery as a candidate-only stage with a normative separation from candidate review, permission review, registration, backfill and incremental collection. The historical source model starts from registered and imported origins, so source discovery is an architecture extension rather than a historical application feature.

The historical Knowledge Environment describes an owner-readable local documentation and file layer, a deliberate separation between framework and owner implementation documentation, multi-device vault patterns, configuration visibility, behavior-file aliases and an implementation-to-reference feedback loop. The reusable CRD narrows this to implementation documentation because storage, sync, agent definitions, setup, publication and arbitrary personal knowledge each have separate outcomes.

Current PIOS defines knowledge maintenance and linting as evidence-producing work that should normally generate flags, proposals and review tasks rather than silently rewriting important knowledge. Historical Dataview queries are implementation tools illustrating orphan, link, source and staleness checks. The bounded restricted application path search did not identify source-discovery, owner implementation-documentation, or knowledge-linting realizations.
