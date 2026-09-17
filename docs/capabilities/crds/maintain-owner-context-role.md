# Maintain an owner context Role

## Identity
- **Name:** Maintain an owner context Role
- **Definition:** Create and revise an owner-governed life-context lens used to organize, filter, prioritize, and interpret personal information.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve meaningful capacities in which the owner acts without turning those contexts into access-control boundaries or fixed folders.
- **Meaningful outcome:** A versioned Role type or Role instance is active, archived, superseded, or rejected with its relationships and provenance preserved.
- **Boundaries — includes:** name, description, Role type/instance distinction, hierarchy or graph relationships, related project or organization, presentation metadata, status, provenance, and lifecycle.
- **Boundaries — excludes:** active-context selection, attaching a Role to an object, access control, outward publication, owner-profile truth, and runtime agent roles.
- **Terms and concepts:** A `Role` is an owner context lens such as founder, parent, advisor, or a specific role instance tied to an organization, project, responsibility, or period.

## Interaction Contract MLEs
### Create or revise a Role
- **Actor:** The owner or an authorized context-maintenance agent operating through owner governance.
- **Command / intent:** Define, relate, revise, archive, restore, or supersede an owner context Role.
- **Current state:** An owner/Core context, current Role vocabulary, related objects when applicable, and prior Role version or proposal exist.
- **Policies / invariants:** Roles are owner-scoped context and do not grant or restrict access; Role type, Role instance, runtime role, and profile assertion remain distinct; inferred Roles remain proposed until governed; archive preserves historical references.
- **Transition:** Validate identity and relationships, record provenance and owner decision, create a new version or lifecycle event, and update the active Role definition.
- **Result:** An active, archived, restored, rejected, or superseded Role definition and relationship state.
- **Events / effects:** May make the Role eligible for active-context selection, contextual classification, retrieval, and explicit outward-intent configuration.
- **Unknowns:** Universal Role hierarchy and cross-Core identifier rules are not established.

## Rules and defaults
### Rules / invariants
- A Role must not be treated as an access-control grant.
- Archiving or revising a Role must not erase historical context assignments.
- Several Roles may overlap or be active concurrently.
### Recommended defaults
- Prefer a small owner-authored definition and add hierarchy or presentation metadata only when useful.

## Unknown / unresolved
- Cross-owner and cross-Core mapping of semantically similar Roles requires an interoperability profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Roles are owner-governed context lenses with type/instance and lifecycle distinctions, not access-control or runtime-role definitions. | rule/invariant | sourced | [D12 and D13](../evidence/statement-provenance.md). |
