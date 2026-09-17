# Maintain a reusable routine

## Identity
- **Name:** Maintain a reusable routine
- **Definition:** Create and govern a reusable execution structure that can produce distinct execution instances without rewriting prior runs.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve an intentional repeatable way of doing work independently from any one occurrence.
- **Meaningful outcome:** A routine definition exists with lifecycle, configuration, version, trigger or scheduling metadata where relevant, and activation history.
- **Boundaries — includes:** creation, revision, versioning, configuration, pause/reactivation, archival, and reusable step or capability references.
- **Boundaries — excludes:** observed habits, one-off project work, executing a particular run, and reminder delivery.
- **Terms and concepts:** A `routine` is reusable execution structure; a `routine run` is one use of that structure.

## Interaction Contract MLEs
### Maintain routine definition
- **Actor:** An authorized owner, planner, or coordinating agent.
- **Command / intent:** Create or revise a repeatable execution structure.
- **Current state:** A repeatable need or reusable structure has been identified.
- **Policies / invariants:** Definition and run state remain separate; material changes are versioned or otherwise attributable; prior runs retain the definition context they used; pausing prevents new automatic runs without erasing history.
- **Transition:** Record or revise the reusable structure, configuration, lifecycle, and activation conditions.
- **Result:** A governed routine definition available for future instantiation.
- **Events / effects:** A separate scheduler, reminder, rule, or explicit request may initiate a run.
- **Unknowns:** No universal trigger model or version-compatibility rule is established.

## Rules and defaults
### Rules / invariants
- A routine is intentional reusable structure, not inferred behavior alone.
- Definition changes must not silently alter the meaning of completed runs.
### Recommended defaults
- Preserve purpose, expected inputs and outcomes, authority requirements, and current version.

## Unknown / unresolved
- The boundary between a routine and a workflow package requires continued cross-tranche alignment.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A routine is reusable structure and remains separate from its run instances. | rule/invariant | sourced | [B10](../evidence/statement-provenance.md). |
