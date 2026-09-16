# Reconcile a pending capture

## Identity
- **Name:** Reconcile a pending capture
- **Definition:** Resolve locally retained or receiver-held capture work into accepted Core content, a retryable state, a preserved failure, or an explicitly authorized discard.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Protect unaccepted work that may contain the only copy while making its relationship to canonical Core state explicit.
- **Meaningful outcome:** Each pending capture has a verified accepted, retryable, failed-preserved, superseded, or authorized-discarded disposition.
- **Boundaries — includes:** pending identity, payload integrity, source/owner binding, acceptance evidence, retry state, conflict/duplicate detection, failure reason, preservation, and discard authority.
- **Boundaries — excludes:** initial capture submission, ordinary accepted-content caching, canonical content deletion, processing/enrichment, and treating cache clearing as reconciliation.
- **Terms and concepts:** `pending capture` means submitted or edited work not yet proven accepted by Core; it is not disposable cache.

## Interaction Contract MLEs
### Resolve pending capture state
- **Actor:** An authorized owner, device support component, receiver, or reconciliation agent.
- **Command / intent:** Determine and complete the correct disposition for pending work.
- **Current state:** A pending item and enough identity, integrity, destination, and prior-attempt evidence exist.
- **Policies / invariants:** The only copy is preserved until acceptance or authorized discard; acceptance is verified against canonical Core; retries are idempotent; owner/Core identity and grants are current; conflicts and duplicates remain visible.
- **Transition:** Compare local/receiver state with canonical acceptance evidence, retry or preserve as needed, and record the final or continuing disposition.
- **Result:** An accepted, retryable, failed-preserved, superseded, conflict, or authorized-discarded reconciliation record.
- **Events / effects:** May release temporary storage after verified acceptance or create owner attention for intervention.
- **Unknowns:** Universal retry limits and offline conflict resolution are not established.

## Rules and defaults
### Rules / invariants
- Pending work must not be deleted as cache merely because it is device-local or receiver-held.
- Clearing cache must not imply acceptance, deletion, or authorized discard of pending work.
### Recommended defaults
- Retain integrity and attempt history until the disposition is verified.

### Communication MLEs
#### Pending capture needs attention
- **Purpose:** Explain that submitted work is not yet safely accepted and identify the available recovery action.
- **Trigger:** Reconciliation fails, conflicts, or requires owner choice.
- **Audience:** Owner or responsible operator.
- **Required meaning:** Identify the pending item, current safety state, reason acceptance is unverified, and available retry/preserve/discard choices.
- **Representative example text:** *Example; illustrative, not shipped copy:* “This capture is still stored on your device and has not yet been accepted by Core.”
- **Possible realizations:** capture queue, update, device alert, or system inspection surface.

## Unknown / unresolved
- Maximum local retention and storage-pressure behavior require device-specific policy.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Pending captures may be the only copy and require explicit acceptance, retry, preservation, or authorized discard. | rule/invariant | sourced | [D02](../evidence/statement-provenance.md). |
