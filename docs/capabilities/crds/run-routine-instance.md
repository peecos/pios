# Run a routine instance

## Identity
- **Name:** Run a routine instance
- **Definition:** Execute one attributable occurrence of a reusable routine while preserving its inputs, state, outputs, and relationship to the governing routine version.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Turn reusable structure into one concrete, auditable execution occurrence.
- **Meaningful outcome:** A routine run reaches a durable state with provenance, outputs or failure evidence, and no mutation of prior runs.
- **Boundaries — includes:** run creation, routine-version binding, input snapshot, participant attribution, lifecycle state, task instances, outputs, failure, cancellation, and completion.
- **Boundaries — excludes:** designing the routine, generic background infrastructure, and interpreting produced results.
- **Terms and concepts:** A `routine run` is a concrete occurrence; it is not the routine definition itself.

## Interaction Contract MLEs
### Execute one routine occurrence
- **Actor:** An authorized owner, scheduler, rule, or execution coordinator.
- **Command / intent:** Start or advance one occurrence of a routine.
- **Current state:** An eligible routine version, authority, and required inputs exist.
- **Policies / invariants:** The run binds to a specific routine definition; inputs and actors are attributable; state is durable; failure is distinct from completion; outputs link back to the run.
- **Transition:** Create the run, perform or coordinate its work, persist state transitions, and close with an explicit outcome.
- **Result:** A completed, failed, cancelled, paused, or intervention-required routine run record.
- **Events / effects:** Tasks, updates, results, or History events may be produced.
- **Unknowns:** Universal retry, overlap, and missed-run policies are not established.

## Rules and defaults
### Rules / invariants
- Repeated uses of a routine must have distinct run identities.
- A run must not silently change the reusable definition that produced it.
### Recommended defaults
- Snapshot the routine version and material inputs at run start.

### Communication MLEs
#### Routine-run outcome
- **Purpose:** Surface completion, failure, or required intervention.
- **Trigger:** The run reaches a material state.
- **Audience:** Owner or responsible operator.
- **Required meaning:** Identify the routine, run, state, result or failure, and next action if any.
- **Representative example text:** *Example; illustrative, not shipped copy:* “The routine run completed and produced one result.”
- **Possible realizations:** update, event, routine history, or API callback.

## Unknown / unresolved
- Whether all routine runs require owner-visible updates depends on relevance and policy.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A routine run is one concrete occurrence linked to its reusable routine. | rule/invariant | sourced | [B10](../evidence/statement-provenance.md). |
