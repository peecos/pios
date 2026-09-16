# Register a connected source

## Identity
- **Name:** Register a connected source
- **Definition:** Establish and maintain a governed source definition for an external account, service, stream, archive class, or other recurring origin of information.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let repeated intake preserve source identity, authority, expected structure, and change behavior independently from individual imports.
- **Meaningful outcome:** A source definition exists with owner consent, access boundary, expected data types, sync state, event mapping, and update/deletion policy.
- **Boundaries — includes:** source identity, category, account or origin reference, access method, consent, privacy boundary, expected data, sync/backfill state, stable IDs, change/deletion handling, and lifecycle status.
- **Boundaries — excludes:** storing individual items, running an import session, performing enrichment, and granting broad sharing or profile authority.
- **Terms and concepts:** A `source` is origin context; it is not an import session, storage item, or processing job.

## Interaction Contract MLEs
### Maintain source registration
- **Actor:** An authorized owner, connector administrator, or intake agent.
- **Command / intent:** Register or revise an external source definition.
- **Current state:** Source identity, intended access, and applicable owner authority are available.
- **Policies / invariants:** Consent and privacy scope are explicit; source-native IDs and timestamps remain attributable; change and deletion semantics are declared; disabling a source stops future intake without erasing prior history.
- **Transition:** Validate source details and persist its definition, lifecycle state, and processing boundary.
- **Result:** A registered, disabled, or retired source definition with inspectable sync policy.
- **Events / effects:** May enable bounded backfill or incremental import sessions.
- **Unknowns:** Universal credential custody and connector refresh policy are not established.

## Rules and defaults
### Rules / invariants
- A connected source is an input channel, not the long-term owner of the aggregated personal record.
- Registration does not authorize deeper enrichment or History inclusion by itself.
### Recommended defaults
- Record expected data classes, stable identifiers, source update behavior, and deletion/tombstone handling before sync.

## Unknown / unresolved
- Source-specific authentication and revocation mechanisms remain realization-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Source identity and lifecycle remain distinct from individual import sessions and processing jobs. | rule/invariant | sourced | [C07–C08](../evidence/statement-provenance.md). |
