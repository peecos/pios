# Resolve a disputed profile assertion

## Identity
- **Name:** Resolve a disputed profile assertion
- **Definition:** Produce an authorized, evidence-linked, versioned disposition when a profile assertion is challenged or contradicted.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Prevent stale or contradicted profile knowledge from retaining unexamined authority.
- **Meaningful outcome:** The dispute is resolved into an explicit retained, corrected, split, superseded, or deprecated state.
- **Boundaries — includes:** dispute evidence, owner review, decision options, version creation, supersession, and rationale.
- **Boundaries — excludes:** contradiction detection, notification delivery, general proposal handling, and silent automated correction.
- **Terms and concepts:** A `dispute` marks unresolved authority; it is not merely low confidence.

## Interaction Contract MLEs
### Resolve a dispute
- **Actor:** The profile subject or explicitly authorized human authority.
- **Command / intent:** Decide how a disputed assertion should be treated.
- **Current state:** A disputed assertion, its versions, and relevant evidence are available.
- **Policies / invariants:** An AI process cannot silently clear the dispute; evidence remains linked; the resolution creates a new version; prior assertions are not erased.
- **Transition:** Review evidence, choose a disposition, record rationale and authority, and create the resulting version/linkage.
- **Result:** Confirmed original, accepted correction, split assertions, deprecation, or an explicitly unresolved dispute.
- **Events / effects:** Current-state and retrieval projections are updated according to the disposition.
- **Unknowns:** Delegated human resolution rules beyond the profile subject are not established.

## Rules and defaults
### Rules / invariants
- Every material resolution is versioned and attributable.
### Recommended defaults
- Keep the assertion disputed when available evidence does not support a responsible resolution.

## Unknown / unresolved
- Public operational realization is not confirmed.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Disputes require owner resolution and versioned outcomes. | rule/invariant | sourced | [K11](../evidence/statement-provenance.md). |
