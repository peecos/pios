# Aggregate an owner History period

## Identity
- **Name:** Aggregate an owner History period
- **Definition:** Compose a closed weekly, monthly, quarterly, or yearly owner-facing summary from accepted lower-level History records while preserving drill-down provenance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make long-running personal history navigable and meaningful without repeatedly flattening all raw evidence.
- **Meaningful outcome:** A period summary captures themes, outcomes, changes, decisions, and unresolved threads and links to its contributing lower-level records.
- **Boundaries — includes:** period definition, lower-level input selection, gap checks, synthesis, source links, hierarchy, closure, regeneration, and confidence/review state.
- **Boundaries — excludes:** daily raw-evidence compilation, canonical event mutation, timeline UI rendering, and automatic promotion of inferred insights to truth.
- **Terms and concepts:** Higher-period History composes bottom-up from closed lower-level summaries.

## Interaction Contract MLEs
### Compose a higher-period summary
- **Actor:** An authorized History summarizer or owner.
- **Command / intent:** Summarize a completed time period from accepted lower-level History.
- **Current state:** Required lower-level periods are closed or their gaps are explicitly represented.
- **Policies / invariants:** Inputs are linked; missing periods are not fabricated; higher levels do not silently reprocess unrelated raw sources; exclusions and sensitivity remain respected; corrections are versioned or attributable.
- **Transition:** Validate period coverage, synthesize the lower-level records, and record hierarchy, provenance, confidence, and review state.
- **Result:** A closed or reviewable period summary with drill-down links.
- **Events / effects:** Supports temporal retrieval, reflection, planning, and later higher-level aggregation.
- **Unknowns:** Universal closure timing and regeneration policy are not established.

## Rules and defaults
### Rules / invariants
- Weekly and higher summaries should be composed from accepted lower-level summaries.
- Aggregation must preserve access to the contributing periods and source trail.
### Recommended defaults
- Increase abstraction with the period horizon while retaining decisions and unresolved themes.

## Unknown / unresolved
- Whether monthly summaries compose from days or weeks may vary by implementation.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Higher-period History is composed bottom-up from closed lower-level summaries with drill-down provenance. | rule/invariant | sourced | [C05](../evidence/statement-provenance.md). |
