# Manage a one-off project

## Identity
- **Name:** Manage a one-off project
- **Definition:** Maintain the context, work state, responsibilities, progress, and resolution of a bounded one-off execution effort.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give a specific structured effort a durable execution home from activation or direct creation through resolution.
- **Meaningful outcome:** A project has an inspectable lifecycle, linked work and artifacts, accountable participants, and a resolved or archived disposition.
- **Boundaries — includes:** project creation, state changes, context, task and artifact links, progress, pause/resume, completion, cancellation, and execution history.
- **Boundaries — excludes:** authoring the source plan, defining reusable routines, performing every linked task, and storing outputs without provenance.
- **Terms and concepts:** A `project` is a one-off execution container, not a generic topic folder or task list.

## Interaction Contract MLEs
### Maintain project lifecycle
- **Actor:** An authorized owner, participant, or coordinating agent.
- **Command / intent:** Create or advance a bounded one-off effort.
- **Current state:** An intended outcome and sufficient project context exist.
- **Policies / invariants:** Project state is canonical outside chat wrappers; linked work retains its own identity; completion or cancellation is explicit; source plan and produced results remain traceable where present.
- **Transition:** Create or update project context, work links, responsibility, progress, and lifecycle state.
- **Result:** A current project record with accountable state and linked execution evidence.
- **Events / effects:** State changes may create updates, work starters, results, or History events.
- **Unknowns:** Universal project status vocabulary is not fixed.

## Rules and defaults
### Rules / invariants
- A project must represent a bounded one-off effort.
- A project must not become the sole identity of its tasks or results.
### Recommended defaults
- Preserve desired outcome, current state, next action, participants, source plan, and resolution evidence.

### Communication MLEs
#### Material project change
- **Purpose:** Surface completion, blocking, cancellation, or owner decision needs.
- **Trigger:** A project reaches a material state requiring attention.
- **Audience:** Owner and responsible participants.
- **Required meaning:** Identify the project, changed state, evidence, and required next action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “The project is blocked pending an owner decision.”
- **Possible realizations:** update card, event, project view, or API response.

## Unknown / unresolved
- Project sizing and decomposition thresholds remain context-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A project is an active one-off execution container rather than a generic folder. | rule/invariant | sourced | [B09](../evidence/statement-provenance.md). |
