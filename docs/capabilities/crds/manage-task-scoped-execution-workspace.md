# Manage a task-scoped execution workspace

## Identity
- **Name:** Manage a task-scoped execution workspace
- **Definition:** Provision, govern, and close a bounded runtime work area for one task or execution scope while separating temporary state from canonical outcomes.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give active agent or service work an isolated, attributable place for temporary files, context, intermediate state, and outputs without turning scratch state into canonical truth.
- **Meaningful outcome:** A workspace is provisioned, active, suspended, cleaned, archived, or failed with task binding, actor/runtime identity, data boundaries, output disposition, and cleanup evidence.
- **Boundaries — includes:** task/run binding, workspace identity, actor and runtime, input references, temporary copies, local state, resource and data limits, lifecycle, output inventory, promotion/discard decisions by reference, cleanup, retention exceptions, and evidence.
- **Boundaries — excludes:** defining the task or project, executing domain logic, deciding whether outputs become canonical, maintaining source repositories, and treating runtime-local state as owner memory.
- **Terms and concepts:** An `execution workspace` is a bounded runtime environment for active work. It is not the user-facing project or the canonical home of accepted outputs.

## Interaction Contract MLEs
### Maintain workspace lifecycle
- **Actor:** An authorized execution coordinator, agent, service, or operator.
- **Command / intent:** Provision, inspect, suspend, resume, close, or clean a workspace for a bounded execution.
- **Current state:** The task/run, actor/runtime, required inputs, data classification, resource limits, existing workspace state, and authority are known.
- **Policies / invariants:** Inputs remain source-referenced; temporary copies and canonical objects are distinguishable; secrets and sensitive data follow explicit boundaries; cleanup waits for output disposition and required evidence; failures preserve enough state for diagnosis or governed recovery; workspace identity does not replace project or task identity.
- **Transition:** Create or update the isolated work area, track temporary and produced artifacts, enforce limits, reconcile output dispositions, and close or preserve the workspace according to policy.
- **Result:** An active, suspended, cleaned, archived, failed, or rejected workspace with disposition evidence.
- **Events / effects:** May supply execution status, promote outputs through separate capabilities, or trigger owner attention when cleanup or disposition is blocked.
- **Unknowns:** Universal isolation, retention, resource, snapshot, and secure-erasure profiles are not established.

## Rules and defaults
### Rules / invariants
- Runtime working copies, caches, scratchpads, and intermediate logs must not silently become canonical truth.
- Workspace cleanup must not discard the only copy of an unaccepted output or unresolved evidence.
### Recommended defaults
- Use one workspace per bounded execution scope and retain an output/disposition manifest before cleanup.

## Unknown / unresolved
- Workspace reuse, nested execution, crash recovery, and regulated-data cleanup require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A task-scoped execution workspace has its own lifecycle and keeps temporary runtime state separate from canonical projects, tasks, sources, and outputs. | rule/invariant | sourced | [L11–L13](../evidence/statement-provenance.md). |
