# Compose a portable Core bundle

## Identity
- **Name:** Compose a portable Core bundle
- **Definition:** Package a declared scope of owner-controlled Core state into a reconstructable, self-describing bundle with provenance, versions, integrity metadata, exclusions, and rebuild instructions.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let owner state move or be reconstructed without depending on the current provider's private storage or runtime internals.
- **Meaningful outcome:** A versioned bundle exists whose manifest identifies scope, contents, omissions, logical identities, integrity algorithm, compatibility information, and reconstruction needs.
- **Boundaries — includes:** scope selection, canonical originals/events/knowledge/system definitions, stable references, manifests, version declarations, checksums, file references, optional derived content, uncertainty/loss report, and secret exclusion.
- **Boundaries — excludes:** validating the finished bundle, restoring it, exporting live credentials or keys, deploying a runtime, and claiming destination compatibility.
- **Terms and concepts:** A `Core bundle` carries governed owner state; it is not by itself a runnable PIOS distribution.

## Interaction Contract MLEs
### Create a scoped portability bundle
- **Actor:** An authorized owner, export service, or portability agent.
- **Command / intent:** Export a declared scope of Core state for transfer, recovery, or takeover.
- **Current state:** Exportable source state, owner authority, scope, and format version are known.
- **Policies / invariants:** Logical IDs and provenance survive; scope reductions are declared; unknown supported extensions are preserved; secret material is excluded; optional/rebuildable content is identified; source records are not mutated.
- **Transition:** Select eligible state, serialize it, generate manifests and integrity metadata, and close the bundle.
- **Result:** A reconstructable portability bundle with declared scope and status.
- **Events / effects:** May create an export-history event and become eligible for independent validation.
- **Unknowns:** Universal encryption container and signing requirements are not established.

## Rules and defaults
### Rules / invariants
- A migration-grade bundle must contain enough structure to reconstruct relationships and provenance.
- Markdown-only or loose-file output must not be represented as a complete Core export.
### Recommended defaults
- Include binaries in full exports and clearly declare all exclusions.

## Unknown / unresolved
- Scope-specific bundle classes and maximum package sizes require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A complete export is a reconstructable state bundle, not merely a collection of files. | rule/invariant | sourced | [C14](../evidence/statement-provenance.md). |
