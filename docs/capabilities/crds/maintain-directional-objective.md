# Maintain a directional objective

## Identity
- **Name:** Maintain a directional objective
- **Definition:** Create and revise an active, action-oriented statement of direction that can guide planning without itself prescribing or executing a plan.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give current pursuit a durable directional object between broad goals and execution designs.
- **Meaningful outcome:** An objective exists with an owner, statement, lifecycle state, provenance, and optional relationships to goals, targets, and plans.
- **Boundaries — includes:** creation, revision, activation or retirement, owner scope, provenance, and links to broader goals or downstream planning objects.
- **Boundaries — excludes:** maintaining a long-horizon goal, defining measurable success, documenting an execution approach, activating work, and tracking project or task progress.
- **Terms and concepts:** An `objective` expresses what is being pursued in an actionable planning horizon. It is direction, not a success measure or execution design.

## Interaction Contract MLEs
### Maintain objective lifecycle
- **Actor:** An authorized owner, planner, or planning agent.
- **Command / intent:** Create or change an objective for current pursuit.
- **Current state:** The intended direction and any existing objective state are known.
- **Policies / invariants:** Objective and goal semantics remain distinguishable; activation does not imply approval of a plan; links are explicit rather than inferred from display order; material revisions retain attribution.
- **Transition:** Validate and persist the objective statement, lifecycle state, provenance, and declared relationships.
- **Result:** A current objective that can guide target definition and plan creation.
- **Events / effects:** May make related planning or review actions available without creating plans or work automatically.
- **Unknowns:** Universal horizon boundaries between a goal and an objective are not established.

## Rules and defaults
### Rules / invariants
- An objective must not be represented as a completed outcome merely because it is active.
- A plan derived from an objective must preserve the source relationship without replacing the objective.
### Recommended defaults
- Keep the objective concise, action-oriented, reviewable, and explicitly linked when it refines a broader goal.

## Unknown / unresolved
- Implementations may use different planning horizons, but they should publish how goal and objective semantics differ.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| An objective is a distinct active direction that may inform a plan while remaining separate from goals, targets, and execution. | rule/invariant | sourced | [F03–F04](../evidence/statement-provenance.md). |
