# Prepare a context-rich Work Starter

## Identity
- **Name:** Prepare a context-rich Work Starter
- **Definition:** Assemble a ready-to-start entry point that gives a person or agent enough purpose, context, next-step guidance, authority boundaries, and completion criteria to begin work.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Reduce the need to reconstruct a work situation before useful action can begin.
- **Meaningful outcome:** A Work Starter is available with a connected outcome, current context, best next step, execution fit, roles, decisions, and definition of done.
- **Boundaries — includes:** source-work linkage, current-context summary, proposed first action, working-mode/window metadata, participant roles, decision needs, readiness, and completion criteria.
- **Boundaries — excludes:** deciding which Work Starter should be first, executing the work, changing authority, and replacing the underlying task or project.
- **Terms and concepts:** A `Work Starter` is a prepared entry point over canonical work, not a second task system.

## Interaction Contract MLEs
### Prepare a ready-to-start entry point
- **Actor:** An authorized owner, planner, or assisting agent.
- **Command / intent:** Prepare existing work so it can be started with minimal context reconstruction.
- **Current state:** A goal, project, task, routine run, or other work object exists with enough source context.
- **Policies / invariants:** The Work Starter links to canonical work; summaries and recommendations are attributable; human decisions and agent permissions remain explicit; preparation does not mark work as started or done.
- **Transition:** Gather relevant context, identify the best next step and execution fit, and record a bounded ready-to-start representation.
- **Result:** A current Work Starter linked to its source work and readiness evidence.
- **Events / effects:** The Work Starter may become eligible for contextual ordering or execution.
- **Unknowns:** Universal freshness and invalidation rules are not established.

## Rules and defaults
### Rules / invariants
- Canonical work state remains on the underlying work object.
- A Work Starter must expose any human decision needed before execution.
### Recommended defaults
- Include purpose, current context, best next step, working mode, expected duration, and definition of done when known.

## Unknown / unresolved
- The minimum context required for different work classes remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A Work Starter is a ready entry point carrying enough context to begin without rebuilding the situation. | capability purpose | sourced | [B15](../evidence/statement-provenance.md). |
