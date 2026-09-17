# Maintain an agent definition

## Identity
- **Name:** Maintain an agent definition
- **Definition:** Create and revise the canonical, owner-governed definition of a persistent software agent independently from any runtime instance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make each persistent agent's intended role and operating boundaries inspectable, portable, versioned, and owner-controlled.
- **Meaningful outcome:** A current agent definition exists with stable identity, purpose, responsibilities, skills, limits, permissions, memory scope, source access, operating instructions, model preferences, lifecycle state, and version history.
- **Boundaries — includes:** definition creation, revision, owner approval, identity reference, purpose, responsibilities, skills, limits, permissions, memory and source scopes, operating instructions, model preferences, status, versioning, rollback, and deployment-target references.
- **Boundaries — excludes:** running the agent, synchronizing runtime copies, assigning a temporary runtime role, storing owner memory, executing work, and choosing outward identity for a specific action.
- **Terms and concepts:** An `agent definition` describes a software agent as a governed system actor. Where useful, it may map to `schema.org/SoftwareApplication`; runtime roles may map separately to `schema.org/Role`.

## Interaction Contract MLEs
### Maintain definition lifecycle
- **Actor:** The owner or an explicitly delegated agent-governance authority.
- **Command / intent:** Create, revise, activate, suspend, restore, or retire a persistent agent definition.
- **Current state:** The current definition, version history, affected scopes, runtime targets, and change authority can be determined.
- **Policies / invariants:** Canonical definition and runtime copies remain distinguishable; permissions and memory scope are explicit; material changes are versioned and attributable; runtime-local prompts or service memory do not silently become canonical; rollback remains possible.
- **Transition:** Validate the requested changes, create a new definition version or lifecycle state, preserve prior versions and rationale, and record affected runtime targets.
- **Result:** A current, suspended, retired, restored, or rejected versioned agent definition.
- **Events / effects:** May make runtime synchronization, capability discovery, permission review, or deployment actions eligible without performing them.
- **Unknowns:** Universal agent-definition schema, signing, compatibility, and delegation policy are not established.

## Rules and defaults
### Rules / invariants
- Agent identity, definition, runtime, memory, activity, and outward representation must not be collapsed into one record.
- A definition change must not be represented as active in a runtime until synchronization is verified.
### Recommended defaults
- Keep purpose, responsibilities, skills, limits, permissions, memory scope, source access, operating instructions, current state, and evolution history owner-readable.

## Unknown / unresolved
- Portable compatibility rules for agent definitions across runtimes and providers require a later profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Persistent agents require canonical, human-visible and agent-readable definitions distinct from runtime, memory, and activity. | rule/invariant | sourced | [J01–J03](../evidence/statement-provenance.md). |
