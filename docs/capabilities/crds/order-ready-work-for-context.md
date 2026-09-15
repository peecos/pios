# Order ready work for the current context

## Identity
- **Name:** Order ready work for the current context
- **Definition:** Produce an explainable, revisable ordering of eligible work against the owner's current time, commitments, operating context, energy, tools, dependencies, and risk.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Help the owner choose suitable work now without reducing planning to permanent priority labels.
- **Meaningful outcome:** An ordered set of currently relevant Work Starters or actionable work exists with reasons for inclusion, ordering, deferral, or exclusion.
- **Boundaries — includes:** eligibility, context fit, available windows, commitments, readiness, dependencies, pinned visibility, reordering, and rationale.
- **Boundaries — excludes:** preparing missing work context, executing selected work, modifying commitments without authority, and treating ranking as objective truth.
- **Terms and concepts:** `dynamic ordering` is a context-sensitive recommendation that changes when relevant conditions change.

## Interaction Contract MLEs
### Produce a contextual work ordering
- **Actor:** An authorized owner, scheduler, or time-planning agent.
- **Command / intent:** Order eligible work for a current or forecast window.
- **Current state:** Candidate work and sufficient context about the window and owner constraints exist.
- **Policies / invariants:** Ineligible or unauthorized work is excluded; pinned means visible rather than universally highest priority; material ordering factors are explainable; changes preserve their reason where review matters.
- **Transition:** Evaluate fit, constraints, readiness, and commitments, then produce or revise the ordered set.
- **Result:** A time-bounded ordered work view with rationale and unresolved constraints.
- **Events / effects:** The owner or an authorized executor may select work; changed context may trigger reordering.
- **Unknowns:** No universal scoring weights or refresh interval are established.

## Rules and defaults
### Rules / invariants
- Ordering must not silently change task, project, or commitment state.
- Pinned status must not imply universal execution priority.
### Recommended defaults
- Prefer transparent fit factors over opaque fixed priority labels.

## Unknown / unresolved
- The authority to automatically move, split, delegate, or defer work remains policy-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Ready work is ordered by transparent contextual fit and can be revised as conditions change. | recommended default | sourced | [B16](../evidence/statement-provenance.md). |
