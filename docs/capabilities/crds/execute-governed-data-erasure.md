# Execute governed data erasure

## Identity
- **Name:** Execute governed data erasure
- **Definition:** Remove, expire, or render inaccessible approved owner data and its derived projections when retention and authority conditions permit, with durable evidence of the outcome.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Complete an authorized erasure obligation across canonical, derived, cached, backup, and cryptographic representations without concealing retained exceptions.
- **Meaningful outcome:** Each affected representation has a verified deleted, expired, cryptographically inaccessible, retained-under-policy, failed, or unresolved disposition.
- **Boundaries — includes:** authority check, retention check, canonical and derived scope, cache/index cleanup, backup expiry behavior, physical deletion, approved crypto-shredding, tombstones, verification, and audit evidence.
- **Boundaries — excludes:** registering the request, unauthorized retention bypass, source decommissioning as a whole, and claiming deletion where retained readable copies remain.
- **Terms and concepts:** `crypto-shredding` is governed key destruction that renders protected ciphertext unreadable; it does not remove the need for explanatory tombstone metadata.

## Interaction Contract MLEs
### Perform approved erasure
- **Actor:** An authorized erasure executor or controlled system process.
- **Command / intent:** Complete an approved erasure request for its permitted scope.
- **Current state:** An accepted request, resolved retention posture, target inventory, and execution authority exist.
- **Policies / invariants:** Active retention is respected; all representations receive explicit dispositions; irreversible key deletion is separately authorized and delayed as required; failures remain visible; emergency bypass is narrowly scoped and logged.
- **Transition:** Delete, expire, tombstone, or cryptographically render inaccessible the approved representations and verify outcomes.
- **Result:** A complete, partial, blocked, or failed erasure report.
- **Events / effects:** Updates erasure-request status and may require remediation or owner notification.
- **Unknowns:** Verification methods for provider backups and replicas vary by implementation.

## Rules and defaults
### Rules / invariants
- Erasure completion must not be claimed while known readable in-scope copies remain without a documented retention exception.
- Derived projections and indexes require explicit cleanup or expiry behavior.
### Recommended defaults
- Preserve minimal non-content tombstone evidence needed to explain the erasure.

### Communication MLEs
#### Erasure outcome
- **Purpose:** Explain what was erased, retained, blocked, or failed.
- **Trigger:** An erasure execution reaches a terminal or intervention-required state.
- **Audience:** Requesting owner or authorized representative.
- **Required meaning:** Identify scope, completed actions, retained exceptions, failures, and any next step.
- **Representative example text:** *Example; illustrative, not shipped copy:* “The approved data was erased; one backup copy remains until its retention period expires.”
- **Possible realizations:** owner update, erasure report, dashboard, or API response.

## Unknown / unresolved
- Cross-provider proof standards for irreversible deletion remain profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Governed erasure separately handles physical deletion, derived cleanup, retention exceptions, and approved crypto-shredding. | rule/invariant | sourced | [C23](../evidence/statement-provenance.md). |
