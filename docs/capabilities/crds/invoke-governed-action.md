# Invoke a governed action

## Identity
- **Name:** Invoke a governed action
- **Definition:** Request one declared executable operation and mediate its execution under applicable identity, permission, confirmation, provenance, and logging requirements.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make action execution explicit and governable independently of the tool or provider that performs it.
- **Meaningful outcome:** A declared action is accepted and produces an attributable result, or is refused/fails with a reasoned outcome.
- **Boundaries — includes:** action identity, inputs, actor/runtime identity, authorization, confirmation, invocation, run record, result reference, and failure.
- **Boundaries — excludes:** defining domain-specific action semantics, standing-rule creation, workflow orchestration, and long-running coordination beyond handoff.
- **Terms and concepts:** An `Action` is an executable capability or operation; a `Tool` is an implementation primitive and a `Skill` is a reusable playbook.

## Interaction Contract MLEs
### Invoke an action
- **Actor:** An authorized owner, application, agent, rule, or workflow.
- **Command / intent:** Execute a named action with stated inputs and purpose.
- **Current state:** The action definition, caller identity, authority context, and inputs are available.
- **Policies / invariants:** Capability availability is discovered or declared; authorization and confirmation are checked before effects; provider internals do not redefine the contract; actor, inputs, effects, outputs, and failures are attributable.
- **Transition:** Validate the request, obtain any required confirmation, invoke the selected executor, and record the outcome.
- **Result:** A success result/reference, refusal, or failure record.
- **Events / effects:** Domain state may change only according to the invoked capability's own contract.
- **Unknowns:** Each domain action may require a more specific CRD.

## Rules and defaults
### Rules / invariants
- A UI affordance, endpoint, function, or tool is not authority by itself.
- Execution must not exceed the caller's granted operation and scope.
### Recommended defaults
- Prefer idempotent invocation and stable result references where the action permits them.

## Unknown / unresolved
- Generic cancellation semantics depend on execution mode.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Executable actions require permission, logs, and appropriate visibility. | rule/invariant | sourced | [B02–B03](../evidence/statement-provenance.md). |
