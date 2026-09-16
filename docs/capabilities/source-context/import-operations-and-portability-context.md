# Import, operations, and portability source context

This reference preserves cross-cutting context for the C2 tranches. It does not create requirements independently; binding statements are repeated in the applicable CRDs.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS master | architecture authority | inbound lifecycle, event governance, Core/PIOS boundaries, ingestion gates, inspection principles, portability and recovery expectations | a particular realization's tested or deployed state |
| Historical PIOS Global at the selected revision | historical design evidence | source/import distinctions, permissioned processing intent, historical system and portability concepts | current PIOS architecture authority or current availability |
| Restricted application evidence `RAS-01` | requirements and potential realization evidence | application-specific intended behavior and, where traced, static implementation evidence | public disclosure, tested behavior, deployment, or production availability without separate evidence |

## Cross-cutting context

- Source, import session, retained item, processing job, event, and owner-facing projection are distinct information roles.
- Source promotion is staged so preservation and baseline mapping do not silently authorize inference, profile effects, retrieval, summaries, sharing, or History inclusion.
- Technical screening, checklist readiness, and owner authorization are separate gates with deliberately limited authority.
- Operational inspection is read-first and projects canonical records and logs rather than computing truth in the interface.
- Portability requires more than downloading loose files: identity, provenance, event structure, system definitions, manifests, checksums, rebuild instructions, and compatibility evidence must remain coherent.
- Backup, restore, export, destination hydration, parity validation, and source decommissioning are different outcomes and must not be collapsed.

## Evidence maturity

Historical and current architecture sources support reusable capability definitions. Restricted requirements are recorded only as disclosure-safe assessment status. Unless a realization register says otherwise, implementation reachability, tests, deployment, and production behavior remain unknown.

## Sequencing context

C2a covers source registration, import sessions, source promotion, ingestion gates, event-type governance, and operational-run inspection. C2b will separately assess export creation, export verification, restore/import compatibility, recovery, parity, and decommissioning boundaries.
