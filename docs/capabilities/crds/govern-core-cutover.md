# Govern a Core cutover

## Identity
- **Name:** Govern a Core cutover
- **Definition:** Transfer canonical operating authority for a bounded Core flow or deployment from a validated source to a validated destination under explicit owner approval.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Complete a controlled transition without ambiguous dual authority, silent data loss, or premature source retirement.
- **Meaningful outcome:** The destination becomes canonical for the approved scope, clients use the approved connection, final-delta evidence is recorded, and rollback/decommissioning status remains explicit.
- **Boundaries — includes:** scope, canonical-side declaration, shadow/write-through constraints, destination tests, source read-only state, final delta, client endpoint transition, owner decision, and cutover receipt.
- **Boundaries — excludes:** export, restore, parity testing itself, rollback execution, source decommissioning, and credential reuse without validation.
- **Terms and concepts:** A `cutover` changes canonical operational authority; a successful shadow period is evidence, not cutover.

## Interaction Contract MLEs
### Complete bounded cutover
- **Actor:** The owner or explicitly authorized transition coordinator.
- **Command / intent:** Make the validated destination canonical for an exact scope.
- **Current state:** Destination restore and parity evidence pass; unresolved retries and reconciliation gaps are closed; owner approval exists.
- **Policies / invariants:** Canonical side is explicit for every flow; source is made read-only where required; final delta is bounded and verified; clients transition through declared endpoints and credentials; cutover does not imply source decommissioning.
- **Transition:** Freeze or bound source writes, apply and verify the final delta, switch approved clients, and record canonical authority.
- **Result:** A completed, aborted, or revision-required cutover record.
- **Events / effects:** May enable source decommissioning or trigger rollback.
- **Unknowns:** Incremental-delta requirements remain implementation-version-specific.

## Rules and defaults
### Rules / invariants
- Owner approval is required for the actual cutover boundary.
- A shadow destination must not be treated as canonical before cutover.
### Recommended defaults
- Preserve a rollback window until post-cutover checks pass.

## Unknown / unresolved
- Universal stabilization duration before source retirement is not established.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Governed cutover transfers canonical authority only after bounded validation and owner approval. | rule/invariant | sourced | [C19](../evidence/statement-provenance.md). |
