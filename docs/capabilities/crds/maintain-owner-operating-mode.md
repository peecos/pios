# Maintain an owner operating Mode

## Identity
- **Name:** Maintain an owner operating Mode
- **Definition:** Create and revise an owner-governed vocabulary for situational operating contexts that may shape filtering, prioritization, and assistance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Represent how the owner is operating in a situation without confusing that context with identity, access, or the working mode required by a task.
- **Meaningful outcome:** A versioned operating Mode definition is active, archived, superseded, or rejected.
- **Boundaries — includes:** name, meaning, optional presentation metadata, intended scope, provenance, status, version, archive, and restoration.
- **Boundaries — excludes:** activating a Mode, attaching it to an object, access control, task working-mode requirements, inferred current context, and notification policy.
- **Terms and concepts:** An `operating Mode` describes the owner's situational state, such as focused, traveling, learning, or recovering; it is normally more transient than a Role.

## Interaction Contract MLEs
### Create or revise an operating Mode
- **Actor:** The owner or an authorized context-maintenance agent acting through explicit governance.
- **Command / intent:** Define, revise, archive, restore, or supersede an operating Mode.
- **Current state:** An owner/Core context, current Mode vocabulary, and prior definition or proposal exist.
- **Policies / invariants:** Persistent definitions require explicit confirmation and versioned evidence; observation alone does not create a durable Mode; Mode and Role remain distinct; archive preserves historical references.
- **Transition:** Validate the proposed definition, record provenance and owner decision, and create the resulting version or lifecycle event.
- **Result:** An active, archived, restored, rejected, or superseded operating Mode definition.
- **Events / effects:** May make the Mode eligible for active-context selection, contextual classification, retrieval, and scheduling support.
- **Unknowns:** Universal Mode vocabularies and expiry defaults are not established.

## Rules and defaults
### Rules / invariants
- A Mode must not be treated as an identity, permission, or task requirement.
- Repeated observation may create a proposal but must not silently create a durable Mode definition.
### Recommended defaults
- Keep Mode definitions lightweight and let active-context state carry situation-specific timing.

## Unknown / unresolved
- The boundary between a reusable Mode definition and an ephemeral unregistered context value remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Operating Modes are owner-governed situational context definitions whose durable creation is separate from current activation and inference. | rule/invariant | sourced | [D14](../evidence/statement-provenance.md). |
