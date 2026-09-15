# Preserve an execution result

## Identity
- **Name:** Preserve an execution result
- **Definition:** Register and retain an output or outcome as a result linked to the execution, actors, sources, and time that produced it.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep produced value discoverable and auditable after active work ends without turning every saved file into a result.
- **Meaningful outcome:** A result record identifies the produced artifact or outcome and preserves provenance to its source execution and supporting evidence.
- **Boundaries — includes:** result qualification, registration, source-execution links, actor attribution, time, artifact/output references, summary, status, and retention lifecycle.
- **Boundaries — excludes:** active project management, workflow execution, generic file storage, owner-facing update presentation, and judging the result's substantive quality.
- **Terms and concepts:** A `result` is a produced output or outcome worth retaining as execution evidence, not a generic container for all stored content.

## Interaction Contract MLEs
### Register an execution result
- **Actor:** An authorized owner, project, routine run, workflow run, or execution coordinator.
- **Command / intent:** Preserve a completed or materially produced outcome as a result.
- **Current state:** An execution record and produced output or outcome evidence exist.
- **Policies / invariants:** Source execution, actors, time, and relevant inputs are attributable; the result does not overwrite its source execution history; retained artifacts follow storage and sensitivity policy; draft or partial status is not misrepresented as final.
- **Transition:** Qualify the output, create the result record, link its evidence and source execution, and persist lifecycle state.
- **Result:** A durable, retrievable result linked to what produced it.
- **Events / effects:** May create a completed-work update, History entry, review request, or later knowledge promotion.
- **Unknowns:** Universal qualification thresholds for notable versus routine outputs are not established.

## Rules and defaults
### Rules / invariants
- Every result must answer what produced it, when, and through which source execution.
- Result preservation must not collapse work-in-progress state into the outcome record.
### Recommended defaults
- Preserve a concise summary, artifact references, source execution, participants, completion state, and verification context.

### Communication MLEs
#### Result available
- **Purpose:** Tell the owner that a meaningful output is ready for review or use.
- **Trigger:** A result is registered or materially revised.
- **Audience:** Owner and authorized participants.
- **Required meaning:** Identify the result, source work, status, and review or use action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “The completed report is available with links to its source project and verification.”
- **Possible realizations:** update card, result view, History item, or API response.

## Unknown / unresolved
- Result retention and promotion into durable Knowledge depend on content class and policy.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Results are provenance-bearing produced outcomes distinct from active execution and generic storage. | rule/invariant | sourced | [B20](../evidence/statement-provenance.md). |
