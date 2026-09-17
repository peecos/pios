# Maintain owner implementation documentation

## Identity
- **Name:** Maintain owner implementation documentation
- **Definition:** Preserve an owner-readable and directly editable account of a PIOS implementation's structure, configuration, decisions, machine roles, and relationship to the reference framework.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let the owner understand and revise how their personal system is actually configured without relying exclusively on an application interface or agent memory.
- **Meaningful outcome:** Current implementation documentation exists with stable scope, source and configuration references, revisions, machine/system relationships, owner-specific decisions, and explicit separation from neutral framework documentation.
- **Boundaries — includes:** implementation overview, structural and machine-role documentation, configuration visibility by reference, agent-definition/instruction references, decision rationale, reference-framework links, versioning, archive/supersession, owner editing, and scope separation.
- **Boundaries — excludes:** maintaining the neutral PIOS framework itself, storing secrets in documentation, replacing canonical configuration or agent definitions, synchronizing files across devices, maintaining arbitrary personal knowledge notes, and automatically publishing implementation discoveries.
- **Terms and concepts:** Implementation documentation is a collection of `schema.org/TechArticle`, `schema.org/CreativeWork`, or configuration-reference records describing one owner's operational system; it is not the runtime configuration itself unless a declared canonical format says so.

## Interaction Contract MLEs
### Maintain implementation documentation
- **Actor:** The owner or an explicitly authorized documentation-maintenance process.
- **Command / intent:** Create, revise, link, supersede, or archive documentation describing the owner's PIOS implementation.
- **Current state:** The affected system component or decision, current documentation revision, source/configuration references, owner scope, and edit authority can be determined.
- **Policies / invariants:** Owner-specific content remains separate from neutral reference material; secrets and credentials are referenced rather than copied; documentation does not silently override canonical configuration; meaningful revisions retain attribution; agent edits remain reviewable and correctable; unresolved authority/master-location questions stay visible.
- **Transition:** Validate scope and references, create or revise the implementation record, preserve its history and relationships, and record the result.
- **Result:** Current, superseded, archived, conflicted, or rejected implementation documentation with traceable revisions.
- **Events / effects:** May trigger knowledge-index refresh, a documentation review, a configuration reconciliation proposal, or a separately governed contribution to reference documentation.
- **Unknowns:** Universal document taxonomy, canonical-versus-projection status, collaborative editing and cross-device synchronization are not established.

## Rules and defaults
### Rules / invariants
- Neutral framework documentation and owner-specific implementation documentation must remain distinguishable.
- Documentation must not expose secrets or silently replace the system records it describes.
### Recommended defaults
- Prefer human-readable, version-friendly formats with stable links to the governed objects and configurations being described.

## Unknown / unresolved
- The authoritative relationship among local documentation, Core knowledge, runtime configuration and synchronized copies requires an implementation profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Owner implementation documentation provides direct human-readable visibility and editability while remaining separate from neutral framework material and canonical runtime state. | rule/invariant | sourced | [S06–S10](../evidence/statement-provenance.md). |
