# Maintain a recoverable Core backup

## Identity
- **Name:** Maintain a recoverable Core backup
- **Definition:** Create, protect, retain, and periodically test independent recovery copies of Core state according to an explicit recovery policy.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve recoverability from loss, corruption, or operational failure independently from ordinary version history and portability exports.
- **Meaningful outcome:** Current backup sets exist under protected custody and at least one applicable restore path has recent, attributable test evidence.
- **Boundaries — includes:** backup scope, schedule, independent storage, encryption, retention, immutability where chosen, credentials/key references, backup status, restore tests, and recovery evidence.
- **Boundaries — excludes:** object versioning alone, owner portability export, live replication as sole proof, disaster declaration, and production cutover.
- **Terms and concepts:** A `backup` is an independently recoverable copy; versioning and replication may support it but do not replace tested recovery.

## Interaction Contract MLEs
### Maintain backup and recovery evidence
- **Actor:** An authorized backup service, operator, or recovery agent.
- **Command / intent:** Create or verify an independent recoverable copy under the governing policy.
- **Current state:** Eligible Core state, backup policy, protected destination, and required authority exist.
- **Policies / invariants:** Backup custody is independent enough for the stated failure model; encryption and retention are explicit; failures are visible; restore tests do not overwrite production; credentials and keys are protected.
- **Transition:** Create or update the backup set, verify integrity, and periodically execute a bounded restore test.
- **Result:** A protected backup status and current restore-test evidence.
- **Events / effects:** Failures or stale recovery evidence may create owner attention or remediation work.
- **Unknowns:** Universal recovery-point and recovery-time objectives are not established.

## Rules and defaults
### Rules / invariants
- Versioning alone is not backup.
- A backup claim requires an identified restore path; a recovery claim requires tested evidence.
### Recommended defaults
- Keep recovery credentials and copies separate from the primary failure domain.

### Communication MLEs
#### Backup or restore-test failure
- **Purpose:** Alert the owner or operator that claimed recoverability is degraded.
- **Trigger:** Backup creation, integrity verification, or restore testing fails or becomes stale.
- **Audience:** Owner or responsible operator.
- **Required meaning:** Identify the affected scope, failed protection step, last known good evidence, and required action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Recovery protection is degraded because the latest restore test failed.”
- **Possible realizations:** operational update, incident, dashboard, or alert.

## Unknown / unresolved
- Backup frequency, retention, immutability, and test cadence depend on the deployment profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Independent backup and periodic restore testing are required; versioning alone does not establish recoverability. | rule/invariant | sourced | [C18](../evidence/statement-provenance.md). |
