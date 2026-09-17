# Consolidate conversation history

## Identity

- **Name:** Consolidate conversation history
- **Definition:** Produce a compact, provenance-linked derivative representation of a bounded conversation range for later review or retrieval.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Reduce the cost of using long conversation histories while preserving traceability to original episodes.
- **Meaningful outcome:** A consolidation represents a defined range and links to the source entries that support it.
- **Boundaries — includes:** range and scope selection, source set, derivative creation, source links, revision, and terminal status.
- **Boundaries — excludes:** deleting original entries, turn-time context assembly, source-of-truth promotion, and generic note editing.
- **Terms and concepts:** A `consolidation` is a derivative, not a replacement for original conversation records.

## Interaction Contract MLEs

### Create or revise a consolidation

- **Actor:** An authorized owner, scheduler, or processing workflow.
- **Command / intent:** Consolidate a specified conversation range and scope.
- **Current state:** Eligible source entries and a determinable range/scope exist.
- **Policies / invariants:** Source entries remain intact; the derivative records range, scope, and source links; corrections are attributable; unsupported claims are not promoted as source truth.
- **Transition:** Select source entries, produce the compact representation, link its sources, and record completion or failure.
- **Result:** A traceable consolidation or a reasoned failure.
- **Events / effects:** Retrieval may use the consolidation as a lower-cost candidate.
- **Unknowns:** Scheduling cadence, compression method, and quality threshold are realization-specific.

## Rules and defaults

### Rules / invariants

- Every consolidation identifies its source range and supporting entries.
- Original conversation entries remain evidence of what occurred.

### Recommended defaults

- Prefer revisable derivative objects over destructive compaction.

## Unknown / unresolved

- No publicly confirmed operational realization is currently recorded.

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Consolidations are derivatives linked to source entries. | rule/invariant | sourced | [Pilot provenance P06](../evidence/statement-provenance.md). |
| A producer or scheduler exists. | unknown/unresolved | unknown | Restricted schema evidence does not establish reachability. |
