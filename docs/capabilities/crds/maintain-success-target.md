# Maintain a success target

## Identity
- **Name:** Maintain a success target
- **Definition:** Create and revise an explicit condition describing what success would look like for an eligible outcome or effort.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make success inspectable without confusing the desired condition with current reality or execution activity.
- **Meaningful outcome:** A target exists with a success condition, lifecycle state, provenance, and optional relationship to a goal, objective, project, or other eligible subject.
- **Boundaries — includes:** creation, revision, activation or retirement, success description, subject linkage, provenance, and criteria needed to evaluate achievement.
- **Boundaries — excludes:** defining the underlying goal or objective, defining how observations are measured, recording observations, declaring achievement without evidence, and executing work.
- **Terms and concepts:** A `target` describes a success condition. It is not a current measured value and does not prove that the condition has been met.

## Interaction Contract MLEs
### Maintain target lifecycle
- **Actor:** An authorized owner, planner, or delegated agent.
- **Command / intent:** Define or revise the condition by which success can be recognized.
- **Current state:** An eligible subject or standalone planning need and any existing target state are known.
- **Policies / invariants:** The condition remains distinct from observations and achievement decisions; subject links are explicit; ambiguous or non-observable criteria remain visible; activation does not imply attainment.
- **Transition:** Validate the success condition and scope, persist or revise the target, and update lifecycle and provenance.
- **Result:** An active, inactive, retired, or revised success target with an inspectable condition.
- **Events / effects:** May inform measurement definitions, reviews, and progress projections without changing the linked goal or work state.
- **Unknowns:** Universal evidence thresholds for declaring a target met are not established.

## Rules and defaults
### Rules / invariants
- Target state and target achievement are different claims.
- A target may be maintained independently or linked to an eligible subject; presentation inside one app does not redefine its identity.
### Recommended defaults
- Prefer observable success conditions and explicit scope, time horizon, and evidence expectations where they matter.

## Unknown / unresolved
- The reusable contract for evaluating and reversing target achievement requires a later governance pass.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A target describes measurable or observable success and remains distinct from goals, metrics, and current achievement evidence. | rule/invariant | sourced | [F05–F06](../evidence/statement-provenance.md). |
