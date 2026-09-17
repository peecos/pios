# Organize a task collection

## Identity
- **Name:** Organize a task collection
- **Definition:** Group and order references to actionable tasks without requiring project semantics or changing the tasks' independent identities.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Provide lightweight organization for related actions when a full project is unnecessary.
- **Meaningful outcome:** A named or contextual task collection has an inspectable membership and ordering while member tasks remain independently manageable.
- **Boundaries — includes:** collection creation, naming, ordering, membership, contextual classification, archival, and task reference removal.
- **Boundaries — excludes:** task execution, project management, deleting a task when a membership is removed, and asserting that membership grants authority.
- **Terms and concepts:** A `task collection` or `task list` is an ordered grouping, not an execution container equivalent to a project.

## Interaction Contract MLEs
### Maintain task collection
- **Actor:** An authorized owner or organizing agent.
- **Command / intent:** Group, order, or remove task references in a lightweight collection.
- **Current state:** Tasks or an existing collection are available.
- **Policies / invariants:** Membership is distinct from task identity; removing a membership does not delete the task unless separately authorized; ordering changes are attributable where history matters; context tags do not grant access.
- **Transition:** Create or update collection identity, ordered membership, and context.
- **Result:** A current ordered task collection referencing its member tasks.
- **Events / effects:** A collection may later be promoted into a project through a separate governed transition.
- **Unknowns:** Whether one task may belong to multiple collections is realization-specific.

## Rules and defaults
### Rules / invariants
- A task collection must not silently become the canonical state of its member tasks.
- Collection archival must not imply task deletion or completion.
### Recommended defaults
- Preserve stable task references and explicit ordering.

## Unknown / unresolved
- Promotion from collection to project needs a later transition contract.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Task collections provide ordered grouping without requiring project structure. | capability purpose | sourced | [B12](../evidence/statement-provenance.md). |
