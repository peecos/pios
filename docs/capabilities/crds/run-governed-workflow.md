# Run a governed workflow

## Identity
- **Name:** Run a governed workflow
- **Definition:** Execute one authorized workflow instance from a fixed package and configuration snapshot while preserving steps, state, outputs, errors, actors, and provenance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Carry reusable orchestration through one inspectable execution without allowing it to bypass domain governance.
- **Meaningful outcome:** A workflow run reaches a durable terminal or intervention state with immutable material inputs/settings and traceable outputs or errors.
- **Boundaries — includes:** trigger acceptance, authority check, input and configuration snapshots, step execution, state, logs, errors, cancellation, output links, and completion.
- **Boundaries — excludes:** package authoring, installation configuration, generic tool implementation, result interpretation, and silent changes to governed truth.
- **Terms and concepts:** A `workflow run` is one execution instance tied to a package version and installed configuration.

## Interaction Contract MLEs
### Execute one workflow run
- **Actor:** An authorized owner, trigger, rule, event handler, or workflow executor.
- **Command / intent:** Run an installed workflow against eligible inputs.
- **Current state:** An enabled installation, package version, valid trigger, required inputs, and sufficient authority exist.
- **Policies / invariants:** Material inputs and settings are snapshotted; every effect remains subject to its domain capability and authority; failures do not masquerade as success; durable outputs link to the run; retries prevent duplicate effects where required.
- **Transition:** Accept the trigger, create the run, execute declared steps, persist state and evidence, and close with an explicit outcome.
- **Result:** A succeeded, failed, cancelled, or intervention-required workflow-run record with linked outputs.
- **Events / effects:** May invoke retrieval, actions, proposals, updates, labels, note creation, or artifact retention through their own contracts.
- **Unknowns:** Universal retry, compensation, timeout, and partial-success semantics are not established.

## Rules and defaults
### Rules / invariants
- A workflow must not bypass proposal, rule, profile, glossary, sharing, or other governed domain contracts.
- Run evidence must identify the package version, installation, trigger, actors, inputs, and outputs.
### Recommended defaults
- Make step-level failures and material model/tool usage inspectable where available.

### Communication MLEs
#### Workflow-run outcome
- **Purpose:** Surface completion, failure, required decision, or meaningful partial outcome.
- **Trigger:** A run reaches a material state requiring owner or operator attention.
- **Audience:** Owner or responsible operator.
- **Required meaning:** Identify the workflow, run state, outputs or error, and required next action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “The workflow completed and produced two reviewable outputs.”
- **Possible realizations:** update, event, run history, callback, or API response.

## Unknown / unresolved
- Which step-level details are retained at each sensitivity level remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A workflow run snapshots material inputs and settings, logs execution, and preserves output provenance. | rule/invariant | sourced | [B19](../evidence/statement-provenance.md). |
