# Restore Core state from a bundle

## Identity
- **Name:** Restore Core state from a bundle
- **Definition:** Hydrate accepted portable Core state into an authorized destination while preserving logical identity, provenance, version history, and explicit dispositions for unsupported or conflicting content.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Reconstruct owner-controlled Core state at a destination without silently changing meaning or authority.
- **Meaningful outcome:** Accepted canonical state is present under destination protection, rebuildable projections are identified or rebuilt, and an import/operationalization report records all dispositions.
- **Boundaries — includes:** authorization check, package/version binding, destination identity, accepted/quarantined/rejected content, stable references, provenance, conflict handling, re-encryption, projection rebuild, connector reauthorization list, and restore report.
- **Boundaries — excludes:** package validation, runtime deployment, automatic activation of imported agents/connectors/schedules, parity certification, and source decommissioning.
- **Terms and concepts:** `restore` or `hydrate` changes destination state; imported definitions remain inactive until separately authorized.

## Interaction Contract MLEs
### Restore accepted state
- **Actor:** An authorized destination operator or recovery workflow.
- **Command / intent:** Import validated bundle content into the designated Core.
- **Current state:** A validated package, destination, owner authorization, and compatible import path exist.
- **Policies / invariants:** Logical identifiers and provenance are preserved; conflicts do not silently overwrite canonical state; secrets are not imported as ordinary content; destination encryption and retention are explicit; imported definitions do not gain authority automatically.
- **Transition:** Hydrate accepted records, preserve or report unresolved content, rebuild allowed projections, and write the operationalization report.
- **Result:** Restored destination state with a complete disposition and rebuild report.
- **Events / effects:** Enables separate parity validation and later governed cutover.
- **Unknowns:** Merge semantics for every canonical object family are not universally specified.

## Rules and defaults
### Rules / invariants
- Restore success must not be equated with complete PIOS operational recovery.
- Unsupported or conflicting content must remain visible in the report.
### Recommended defaults
- Restore canonical state before rebuilding derived indexes and projections.

## Unknown / unresolved
- Rollback semantics for partially applied restores require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Restore preserves identity and provenance, separates inactive definitions, and reports every content disposition. | rule/invariant | sourced | [C16](../evidence/statement-provenance.md). |
