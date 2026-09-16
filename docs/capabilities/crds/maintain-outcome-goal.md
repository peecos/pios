# Maintain an outcome goal

## Identity
- **Name:** Maintain an outcome goal
- **Definition:** Create and revise a durable statement of a desired longer-horizon outcome without turning it into execution work or evidence of success.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve what the owner is aiming toward over time so planning, projects, work selection, and review can remain connected to durable direction.
- **Meaningful outcome:** A goal exists with an owner, desired outcome, lifecycle state, optional time horizon and focus context, and links to related success or execution objects.
- **Boundaries — includes:** creation, revision, activation or retirement, time horizon, focus context, provenance, review context, and links to targets, metrics, projects, or other relevant work.
- **Boundaries — excludes:** defining a near-term objective, specifying a success condition, recording measurements, authoring an execution plan, and performing the work.
- **Terms and concepts:** A `goal` is a durable desired outcome or direction. It remains valid without a target, metric, project, or task.

## Interaction Contract MLEs
### Maintain goal lifecycle
- **Actor:** An authorized owner or delegated planning agent.
- **Command / intent:** Create, revise, activate, pause, retire, or reconnect a longer-horizon outcome goal.
- **Current state:** The intended outcome and current goal state can be determined.
- **Policies / invariants:** The goal remains distinct from evidence that it has been achieved; linked targets and work retain their own identities; material changes are attributable; inferred direction is not silently treated as owner-confirmed intent.
- **Transition:** Validate the requested change, preserve the goal statement and context, update lifecycle state or links, and record provenance.
- **Result:** A current, inspectable goal definition with explicit lifecycle and relationships.
- **Events / effects:** May inform objectives, targets, projects, Work Starters, reviews, and contextual work ordering without creating or changing them automatically.
- **Unknowns:** Universal review cadence and goal-status vocabulary are not established.

## Rules and defaults
### Rules / invariants
- A goal must not be represented as a plan, project, task, target, or measured result.
- A missing target or metric must not invalidate an otherwise meaningful goal.
### Recommended defaults
- Preserve a concise outcome statement, rationale, time horizon, review cadence, and links to related direction, success, and execution objects when available.

## Unknown / unresolved
- The portable relationship contract for connecting goals to objectives, targets, projects, and reviews remains open.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A goal preserves longer-horizon direction and remains meaningful without attached target, metric, or execution work. | rule/invariant | sourced | [F01–F02](../evidence/statement-provenance.md). |
