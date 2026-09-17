# Maintain a collaboration channel

## Identity
- **Name:** Maintain a collaboration channel
- **Definition:** Create and revise a durable top-level collaboration container for a declared owner, participant set, purpose, and visibility scope.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Organize related human-agent discussions without making the communication container the canonical home of work or knowledge.
- **Meaningful outcome:** A collaboration channel exists with identity, purpose, participants, visibility, lifecycle state, provenance, and linked discussions.
- **Boundaries — includes:** creation, naming, description, type or purpose, participant scope, visibility, ordering, muting, archival, restoration, provenance, and thread membership.
- **Boundaries — excludes:** maintaining thread content, recording messages, owning task/project state, executing work, and replacing topical knowledge organization.
- **Terms and concepts:** A `collaboration channel` is an organizing container for conversations; individual focused conversations may map to `schema.org/Conversation` and remain separate objects.

## Interaction Contract MLEs
### Maintain channel lifecycle
- **Actor:** The owner or an authorized collaboration administrator.
- **Command / intent:** Create, revise, reorder, mute, archive, or restore a collaboration channel.
- **Current state:** Channel identity, current metadata, participants, visibility, linked threads, and authority can be determined.
- **Policies / invariants:** Channel organization does not become the information taxonomy or execution source of truth; participant and visibility changes follow applicable access governance; archival preserves references; naming changes retain stable identity.
- **Transition:** Validate the requested structural change, update channel metadata or lifecycle, and preserve affected membership and provenance.
- **Result:** A current, muted, archived, restored, or rejected collaboration channel.
- **Events / effects:** May alter conversation navigation and notifications without changing linked work or knowledge state.
- **Unknowns:** Universal channel types, inheritance, participant-role rules, and retention are not established.

## Rules and defaults
### Rules / invariants
- A collaboration channel must not become a competing task, project, result, or knowledge store.
- Archival must preserve stable references to retained threads and messages.
### Recommended defaults
- Keep channel taxonomies shallow and purpose-driven; use knowledge metadata and retrieval for deeper topical organization.

## Unknown / unresolved
- Cross-harness channel portability and participant synchronization require an interoperability profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Collaboration channels are durable organizing containers around work and conversation, not canonical execution or knowledge homes. | rule/invariant | sourced | [L01–L03](../evidence/statement-provenance.md). |
