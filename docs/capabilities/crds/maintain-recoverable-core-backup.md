# Maintain a recoverable Core backup

## Identity
- **Name:** Maintain a recoverable Core backup
- **Definition:** Create, protect, retain, and verify the integrity of independent recovery copies of Core state according to an explicit recovery policy.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve recoverability from loss, corruption, or operational failure independently from ordinary version history and portability exports.
- **Meaningful outcome:** Current backup sets exist under protected custody with attributable creation and integrity status and explicit references to any separately produced restore/parity evidence.
- **Boundaries — includes:** backup scope, schedule, independent storage, encryption, retention, immutability where chosen, credentials/key references, backup creation, integrity verification, backup status, and references to recovery evidence.
- **Boundaries — excludes:** executing a restore test, restoring Core state, validating restored parity, object versioning alone, owner portability export, live replication as sole proof, disaster declaration, and production cutover.
- **Terms and concepts:** A `backup` is an independently recoverable copy; versioning and replication may support it but do not replace tested recovery.

## Interaction Contract MLEs
### Maintain a protected backup set
- **Actor:** An authorized backup service, operator, or recovery agent.
- **Command / intent:** Create, retain, rotate, or verify the integrity of an independent recovery copy under the governing policy.
- **Current state:** Eligible Core state, backup policy, protected destination, and required authority exist.
- **Policies / invariants:** Backup custody is independent enough for the stated failure model; encryption and retention are explicit; failures are visible; credentials and keys are protected; restore and parity tests remain separately authorized operations.
- **Transition:** Create, rotate, retain, expire, or integrity-check the backup set and record its status.
- **Result:** A protected backup-set status with scope, custody, integrity, and retention evidence.
- **Events / effects:** May schedule a separate restore/parity exercise or create owner attention when backup protection or referenced recovery evidence is stale.
- **Unknowns:** Universal recovery-point and recovery-time objectives are not established.

## Rules and defaults
### Rules / invariants
- Versioning alone is not backup.
- A backup claim requires an identified restore path; a recovery claim requires separate restore and parity evidence.
### Recommended defaults
- Keep recovery credentials and copies separate from the primary failure domain.

### Communication MLEs
#### Backup protection failure
- **Purpose:** Alert the owner or operator that claimed recoverability is degraded.
- **Trigger:** Backup creation or integrity verification fails, or required external recovery evidence becomes stale.
- **Audience:** Owner or responsible operator.
- **Required meaning:** Identify the affected scope, failed protection step, last known good evidence, and required action.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Recovery protection is degraded because the backup or its required recovery evidence is not current.”
- **Possible realizations:** operational update, incident, dashboard, or alert.

## Unknown / unresolved
- Backup frequency, retention, immutability, and test cadence depend on the deployment profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Independent backup creation and custody are required; restore and parity testing provide separate recovery evidence. | rule/invariant | sourced | [C18](../evidence/statement-provenance.md). |
