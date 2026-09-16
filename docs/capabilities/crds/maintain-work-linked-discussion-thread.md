# Maintain a work-linked discussion thread

## Identity
- **Name:** Maintain a work-linked discussion thread
- **Definition:** Create and maintain a focused conversation linked to a source message, work object, run, result, file, or other eligible subject.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve focused clarification, progress, exception, escalation, and resolution context without replacing the linked object's canonical state.
- **Meaningful outcome:** A discussion thread exists with stable identity, root subject, participants, status, messages, provenance, and resolution or archival state.
- **Boundaries — includes:** creation, root link, channel membership, title, participants, open/waiting/blocked/resolved state, message membership, summary reference, movement, reopening, archival, and provenance.
- **Boundaries — excludes:** maintaining the linked work object, executing work, recording each message, owning approval state, and unrestricted nested-thread trees.
- **Terms and concepts:** A focused discussion may map to `schema.org/Conversation`; its linked task, project, run, result, or source remains authoritative for domain state.

## Interaction Contract MLEs
### Maintain thread lifecycle
- **Actor:** The owner, an authorized participant, or a system process creating an execution-linked thread.
- **Command / intent:** Open, link, move, mark waiting or blocked, resolve, reopen, summarize, or archive a focused discussion.
- **Current state:** The root subject, channel, participant set, current thread state, source references, and authority can be determined.
- **Policies / invariants:** The thread references rather than clones canonical work; status changes are attributable; participant access is enforced separately; nested depth follows the declared profile; resolution does not silently resolve the linked object; summaries do not replace messages.
- **Transition:** Validate the root and audience, create or update thread structure and status, retain message/source links, and record the result.
- **Result:** An open, waiting, blocked, resolved, reopened, archived, or rejected discussion thread.
- **Events / effects:** May surface owner attention, route clarification, or link completion evidence while leaving canonical work state unchanged unless its own capability accepts a separate action.
- **Unknowns:** Universal thread-depth, inactivity, auto-resolution, and cross-harness merge rules are not established.

## Rules and defaults
### Rules / invariants
- A discussion thread must not become the sole record of work state, approval, or produced results.
- Thread resolution and source-object resolution remain separate transitions.
### Recommended defaults
- Use one level of focused branching for work-specific discussion unless an implementation profile justifies deeper nesting.

## Unknown / unresolved
- Cross-system references and conflict handling when the linked execution system changes remain implementation-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A focused thread preserves discussion and status around a linked subject while canonical work and result state remain elsewhere. | rule/invariant | sourced | [L04–L06](../evidence/statement-provenance.md). |
