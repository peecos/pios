# Roll back a Core cutover

## Identity
- **Name:** Roll back a Core cutover
- **Definition:** Restore the previously authorized canonical operating path after a cutover is aborted, fails validation, or is explicitly reversed.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Return to a known governed operating state without hiding partial destination effects or creating dual authority.
- **Meaningful outcome:** The canonical side and client path are restored or explicitly stabilized, partial effects are reconciled, and the rollback evidence is durable.
- **Boundaries — includes:** rollback trigger, authority, write fencing, client reversion, delta reconciliation, destination disposition, unresolved effects, and rollback receipt.
- **Boundaries — excludes:** normal cutover, source decommissioning, destructive cleanup of evidence, and pretending failed destination writes never occurred.
- **Terms and concepts:** `rollback` is a governed transition outcome, not automatic deletion of the destination.

## Interaction Contract MLEs
### Revert canonical operating path
- **Actor:** An authorized owner or transition coordinator.
- **Command / intent:** Abort or reverse the cutover and restore the approved prior path.
- **Current state:** A cutover is in progress or completed within an allowed rollback boundary, and rollback authority exists.
- **Policies / invariants:** Only one canonical writer is active per governed flow; accepted writes are reconciled; partial destination effects remain traceable; rollback scope and data-loss risk are explicit.
- **Transition:** Fence writes, reconcile deltas, restore client routing and canonical authority, and record destination state.
- **Result:** A completed, partial, failed, or blocked rollback record.
- **Events / effects:** May create remediation work and a renewed parity/cutover plan.
- **Unknowns:** Rollback-window duration and automatic trigger conditions are profile-specific.

## Rules and defaults
### Rules / invariants
- Rollback must not create competing canonical histories.
- Evidence from the failed transition must remain available.
### Recommended defaults
- Prefer fail-closed write fencing when reconciliation is uncertain.

## Unknown / unresolved
- Conflict handling for writes accepted only by the destination requires implementation-specific policy.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Rollback is an explicit governed alternative to cutover and preserves transition evidence. | rule/invariant | sourced | [C20](../evidence/statement-provenance.md). |
