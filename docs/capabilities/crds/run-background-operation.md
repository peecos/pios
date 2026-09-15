# Run a background operation

## Identity
- **Name:** Run a background operation
- **Definition:** Carry an accepted long-running operation through asynchronous execution to a durable terminal outcome without requiring the initiating interface to remain open.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let lengthy processing continue safely while preserving state, retry/failure semantics, and owner-visible completion.
- **Meaningful outcome:** The operation reaches a durable completed, failed, cancelled, or intervention-required state with output and provenance references.
- **Boundaries — includes:** handoff, run identity, queued/running state, progress, retry, cancellation where supported, terminal state, result links, and durable notification.
- **Boundaries — excludes:** domain-specific processing logic, initial action authorization, transient UI animation, and result interpretation.
- **Terms and concepts:** A `background operation` is an execution run whose lifecycle outlives the initiating interaction.

## Interaction Contract MLEs
### Execute asynchronously
- **Actor:** An authorized workflow, scheduler, or action executor.
- **Command / intent:** Run accepted work asynchronously and preserve its outcome.
- **Current state:** An authorized request, inputs, and execution policy exist.
- **Policies / invariants:** Handoff is acknowledged; run state is inspectable; retries are bounded and attributable; duplicate effects are prevented where required; terminal outcomes and outputs are durable; failure does not masquerade as completion.
- **Transition:** Create the run, release the initiating surface, process asynchronously, persist state transitions, and publish terminal outcome.
- **Result:** A terminal run record linked to outputs or failure evidence.
- **Events / effects:** Durable owner-facing updates may be emitted; downstream capabilities may consume successful outputs.
- **Unknowns:** Universal cancellation and retry limits are not established.

## Rules and defaults
### Rules / invariants
- The initiating interface need not remain active for work to complete.
- Durable completion/failure state must not depend only on a transient toast.
### Recommended defaults
- Acknowledge handoff promptly and route completion through the normal owner-attention surface.

### Communication MLEs
#### Background operation status
- **Purpose:** Tell the owner that work was accepted and later reached a meaningful terminal state.
- **Trigger:** Handoff, completion, failure, cancellation, or required intervention.
- **Audience:** Initiating owner or responsible operator.
- **Required meaning:** Identify the operation, current/terminal state, result or error, and any required action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Processing continues in the background. A result update will appear when it finishes.”
- **Possible realizations:** update feed, event, push, inline status, or API callback.

## Unknown / unresolved
- Communication channel and retry policy remain realization-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Long-running work releases the initiating surface and reports a durable outcome. | recommended default | sourced | [B04](../evidence/statement-provenance.md). |
