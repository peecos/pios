# Maintain an execution plan

## Identity
- **Name:** Maintain an execution plan
- **Definition:** Create and revise a governed source design describing how an intended outcome could be pursued before active execution begins.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve a reviewable execution design without confusing proposed work with active work.
- **Meaningful outcome:** A plan exists with purpose, proposed steps, relevant capabilities, source context, review state, and revision history.
- **Boundaries — includes:** creation, revision, review, approval or rejection, source references, and preservation after activation.
- **Boundaries — excludes:** executing steps, managing a project, defining a reusable routine, and deciding the underlying objective.
- **Terms and concepts:** A `plan` is a governed source design. Approval makes it eligible for activation but does not itself perform the work.

## Interaction Contract MLEs
### Maintain plan lifecycle
- **Actor:** An authorized owner, planner, or planning agent.
- **Command / intent:** Create or revise a plan for an intended outcome.
- **Current state:** A planning need and enough context to describe a possible path exist.
- **Policies / invariants:** Draft and active execution remain distinct; material revisions are attributable; approval or rejection is explicit where required; activation never erases the source plan.
- **Transition:** Record or revise the proposed structure, evaluate it, and persist its current lifecycle state.
- **Result:** A reviewable plan and revision history.
- **Events / effects:** Approval may enable a separate activation capability.
- **Unknowns:** Universal approval thresholds and plan schema are not established.

## Rules and defaults
### Rules / invariants
- A plan must not be represented as completed execution.
- Activating a plan must preserve its identity and provenance.
### Recommended defaults
- Keep purpose, proposed steps, capability needs, assumptions, and definition of success inspectable.

### Communication MLEs
#### Plan decision status
- **Purpose:** Surface when a plan needs review or has received a material disposition.
- **Trigger:** Review requested, approved, rejected, or materially revised.
- **Audience:** Owner and responsible participants.
- **Required meaning:** Identify the plan, current state, material change, and available next action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “The plan is approved and ready to activate.”
- **Possible realizations:** planning view, update, event, or API response.

## Unknown / unresolved
- The relationship among goals, objectives, and targets needs a separate terminology pass.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A plan remains a source design record rather than active execution. | rule/invariant | sourced | [B07](../evidence/statement-provenance.md). |
