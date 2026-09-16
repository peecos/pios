# Decommission a source Core

## Identity
- **Name:** Decommission a source Core
- **Definition:** Retire a former canonical Core deployment after validated cutover and owner sign-off while preserving required evidence, retention, and recovery obligations.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** End obsolete source operation without premature deletion, residual authority, or loss of required audit and recovery evidence.
- **Meaningful outcome:** Source writes, credentials, connectors, services, and retained data have explicit retired, retained, transferred, revoked, or pending dispositions.
- **Boundaries — includes:** prerequisites, owner sign-off, write disablement, credential/connector revocation, retention review, backup/export confirmation, data disposition, endpoint retirement, and closure evidence.
- **Boundaries — excludes:** cutover, destination parity validation, erasure execution itself, and deleting evidence required by policy.
- **Terms and concepts:** `decommissioning` retires the source deployment; it may precede, follow, or exclude physical erasure according to policy.

## Interaction Contract MLEs
### Retire source deployment
- **Actor:** An authorized owner or infrastructure operator.
- **Command / intent:** Decommission the former source Core after transition.
- **Current state:** Cutover is complete, parity evidence is accepted, rollback posture is decided, and owner sign-off exists.
- **Policies / invariants:** Required exports/backups are verified; active clients and connectors are accounted for; retained evidence is preserved; deletion follows separate erasure governance; residual write authority is removed.
- **Transition:** Disable source operation, revoke or retire access, apply approved data dispositions, and record closure.
- **Result:** A decommissioned, partially decommissioned, or blocked source-Core record.
- **Events / effects:** May initiate governed erasure or retained-archive monitoring.
- **Unknowns:** Minimum retention after cutover varies by legal and recovery policy.

## Rules and defaults
### Rules / invariants
- Source decommissioning must not begin solely because destination restore completed.
- Owner sign-off and accepted parity evidence precede irreversible retirement.
### Recommended defaults
- Preserve a final export, configuration record, and decommissioning manifest.

## Unknown / unresolved
- Treatment of provider-managed residual copies depends on provider and retention policy.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Source retirement follows accepted destination parity and owner sign-off and preserves retention/deletion governance. | rule/invariant | sourced | [C21](../evidence/statement-provenance.md). |
