# Apply contextual classification

## Identity
- **Name:** Apply contextual classification
- **Definition:** Attach or remove a Role or Mode context for a governed object while preserving the classification's authority and lifecycle history.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve how an object relates to operating context without confusing context with ownership, access, or permanent identity.
- **Meaningful outcome:** A current contextual relation is established or archived with provenance and historical continuity.
- **Boundaries — includes:** target/context validation, apply, archive, reapply, provenance, temporal scope, and active/history views.
- **Boundaries — excludes:** creating Roles or Modes, setting session-wide active context, access control, and assigning an organizing label.
- **Terms and concepts:** `Role` and `Mode` are Cotton context concepts; an attachment expresses relevance, not permission.

## Interaction Contract MLEs
### Change an object's contextual classification
- **Actor:** The owner or a process acting under confirmed authority.
- **Command / intent:** Apply or remove a Role or Mode context on an object.
- **Current state:** The object, context value, authority, and active relation state are determinable.
- **Policies / invariants:** Context never grants access; owner scope is consistent; silent inferred tagging requires confirmed authority; removal preserves history; concurrent contexts are allowed; inferred context does not silently become persistent preference or truth.
- **Transition:** Validate target and context, create an active relation or archive the active relation, and record provenance/time bounds.
- **Result:** A traceable active or archived contextual relation, or reasoned rejection.
- **Events / effects:** Filtering, retrieval, and History may use the active or historical relation according to purpose.
- **Unknowns:** View-specific AND/OR filter behavior is not universal.

## Rules and defaults
### Rules / invariants
- Context classification and access authorization remain separate.
- Removing context does not erase its historical application.
### Recommended defaults
- Default views use active relations; history views may include archived relations.

## Unknown / unresolved
- Session-wide active-context selection remains a separate candidate.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Role/Mode context is non-authorizing and history-preserving. | rule/invariant | sourced | [K06](../evidence/statement-provenance.md). |
