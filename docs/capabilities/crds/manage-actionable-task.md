# Manage an actionable task

## Identity
- **Name:** Manage an actionable task
- **Definition:** Maintain one actionable unit of work through context, responsibility, scheduling metadata, execution state, and resolution.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let work remain an independently manageable action whether standalone or contained by broader execution.
- **Meaningful outcome:** A task has a clear current state, context, responsible actor, and resolution record.
- **Boundaries — includes:** capture, clarification, assignment, parent/context linkage, due or schedule metadata, state transitions, completion, reopening, and archival.
- **Boundaries — excludes:** project management, routine definition, reminder triggering, task-list organization, and executing domain-specific action logic.
- **Terms and concepts:** A `task` is the general actionable unit. A `to-do` is a task surfaced in standalone context.

## Interaction Contract MLEs
### Maintain task lifecycle
- **Actor:** An authorized owner, participant, or coordinating agent.
- **Command / intent:** Create or update one actionable unit of work.
- **Current state:** A work need or existing task is available.
- **Policies / invariants:** Context and parentage are explicit; completion is attributable; detaching or moving a task preserves identity and history; a due date does not imply a reminder was delivered.
- **Transition:** Capture or revise action, context, responsibility, timing metadata, and execution state.
- **Result:** A current actionable task with durable lifecycle history.
- **Events / effects:** Completion may update a parent, create a result/update, or feed History.
- **Unknowns:** Universal task status vocabulary and subtask depth are not established.

## Rules and defaults
### Rules / invariants
- Standalone and contained tasks may share a model without losing their context.
- Completion and reopening must remain distinguishable.
### Recommended defaults
- Keep the action wording, responsible actor, parent/context, next state, and relevant time constraints explicit.

## Unknown / unresolved
- The minimum metadata for very lightweight capture may vary by surface.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Task is the general actionable unit; To-do is its standalone context. | rule/invariant | sourced | [B11](../evidence/statement-provenance.md). |
