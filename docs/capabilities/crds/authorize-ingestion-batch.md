# Authorize an ingestion batch

## Identity
- **Name:** Authorize an ingestion batch
- **Definition:** Grant or deny owner authority for the exact manifest, retention posture, remediation posture, projections, and upload boundary of one ingestion batch.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Ensure owner-data ingestion proceeds only within an explicit, bounded owner decision.
- **Meaningful outcome:** The exact batch has a durable approval, denial, expiry, or revision-required disposition with scope and conditions.
- **Boundaries — includes:** manifest identity, owner decision, approved scope, retention/remediation posture, projection/export choices, conditions, expiry, and decision provenance.
- **Boundaries — excludes:** technical screening, checklist readiness, performing upload, future broad migration, and source decommissioning unless explicitly included.
- **Terms and concepts:** `authorization` grants bounded permission; notification or prior technical readiness is not permission.

## Interaction Contract MLEs
### Decide ingestion authority
- **Actor:** The owner or explicitly delegated authority permitted by the governance profile.
- **Command / intent:** Approve, deny, or require revision of one exact ingestion batch.
- **Current state:** A versioned manifest, technical-screen result, readiness assessment, and all material owner choices are available.
- **Policies / invariants:** Scope is exact; unresolved guarded issues block approval; approval does not extend to changed manifests or later batches; decision and conditions are durable and attributable.
- **Transition:** Review the evidence and record the bounded authorization disposition.
- **Result:** An authorized, denied, expired, or revision-required batch decision.
- **Events / effects:** Authorization may enable ingestion through a separate execution capability.
- **Unknowns:** Delegation rules and approval expiry vary by implementation profile.

## Rules and defaults
### Rules / invariants
- Owner approval is required for the exact governed batch where the ingestion gate applies.
- Approval must not be inferred from silence, notification delivery, or a passing technical screen.
### Recommended defaults
- Bind the decision to a manifest digest and make any conditions explicit.

### Communication MLEs
#### Ingestion authorization request
- **Purpose:** Present the exact batch and unresolved owner choices for a bounded decision.
- **Trigger:** Technical screening and readiness assessment allow owner review.
- **Audience:** Owner or authorized delegate.
- **Required meaning:** Identify scope, risks, retention/remediation posture, planned effects, and the fact that no ingestion occurs without approval.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Review and approve this exact ingestion batch before any owner data is uploaded.”
- **Possible realizations:** approval card, signed manifest, owner console, or API decision record.

## Unknown / unresolved
- The acceptable mechanisms for high-assurance owner approval remain implementation-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Owner authorization is bound to the exact ingestion manifest and does not authorize broader future work. | rule/invariant | sourced | [C11](../evidence/statement-provenance.md). |
