# Register an owner-data erasure request

## Identity
- **Name:** Register an owner-data erasure request
- **Definition:** Record an attributable owner request to remove or make inaccessible defined data while preserving its scope, authority, retention constraints, and immediate exposure controls.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make erasure intent effective and auditable even when physical deletion cannot occur immediately.
- **Meaningful outcome:** A scoped erasure request exists with authority, affected records, retention blockers, immediate suppression actions, and expected completion path.
- **Boundaries — includes:** request scope, owner authority, reason where supplied, affected references, retention status, exposure suppression, tombstone/erasure-request event, deadlines, and status.
- **Boundaries — excludes:** physical deletion, cryptographic erasure, deleting required audit evidence, and broad account closure unless explicitly scoped.
- **Terms and concepts:** An `erasure request` records intent and governance state; it is not proof that physical deletion completed.

## Interaction Contract MLEs
### Register erasure intent
- **Actor:** The owner or explicitly authorized representative.
- **Command / intent:** Request erasure of a defined data scope.
- **Current state:** Target records can be identified and the requester's authority can be evaluated.
- **Policies / invariants:** Scope and authority are durable; active retention constraints are visible; affected content stops appearing in retrieval and derived views where required; request status is not misrepresented as completed deletion.
- **Transition:** Record the request, create the applicable tombstone or request event, and apply immediate exposure controls.
- **Result:** An accepted, denied, blocked, or clarification-required erasure request.
- **Events / effects:** May initiate derived cleanup and later physical or cryptographic erasure.
- **Unknowns:** Identity-verification strength varies by sensitivity and consequence.

## Rules and defaults
### Rules / invariants
- Retention-delayed deletion must remain distinguishable from completed erasure.
- The request and its authority evidence must remain auditable.
### Recommended defaults
- Provide a scoped status explaining what is hidden, deleted, retained, or pending.

## Unknown / unresolved
- Legal retention exceptions and appeal paths remain jurisdiction- and service-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Erasure intent is recorded immediately and can suppress exposure before physical deletion is permitted. | rule/invariant | sourced | [C22](../evidence/statement-provenance.md). |
