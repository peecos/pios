# Validate restored Core parity

## Identity
- **Name:** Validate restored Core parity
- **Definition:** Verify that a restored destination preserves the intended state, protection, provenance, owner boundary, and selected operational behavior of the source scope.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Establish what recovery or transfer actually reproduced rather than inferring equivalence from successful file import.
- **Meaningful outcome:** A parity report states which state, Core-contract behavior, and PIOS service behavior passed, failed, or remain unproven.
- **Boundaries — includes:** manifest counts, checksums, logical IDs, protection/retention posture, provenance links, owner isolation, selected retrieval/evidence paths, required native-service behavior, discrepancies, and rollback/cutover recommendation.
- **Boundaries — excludes:** creating or restoring the bundle, granting cutover authority, exhaustive application testing, and claiming untested compatibility levels.
- **Terms and concepts:** `state parity`, `Core contract conformance`, and `complete PIOS service recovery` are separate evidence dimensions.

## Interaction Contract MLEs
### Verify destination parity
- **Actor:** An authorized reviewer, recovery operator, or verification agent.
- **Command / intent:** Compare a restored destination against the declared source scope and required behavior.
- **Current state:** Restore has completed and source manifest plus expected behavior profile are available.
- **Policies / invariants:** Checks are reproducible; discrepancies remain visible; owner-boundary leakage fails validation; byte equality does not prove service behavior; untested dimensions remain unproven.
- **Transition:** Execute state, protection, provenance, and selected behavior checks and record findings.
- **Result:** A pass, partial, fail, or blocked parity report by evidence dimension.
- **Events / effects:** May support cutover, rollback, remediation, or renewed restore decisions.
- **Unknowns:** The minimum behavior suite for each PIOS implementation profile remains evolving.

## Rules and defaults
### Rules / invariants
- Successful hydration alone must not establish operational compatibility.
- Parity claims must identify the exact tested source revision, destination, scope, and evidence.
### Recommended defaults
- Test representative retrieval paths from knowledge to events to originals.

## Unknown / unresolved
- Acceptable variance for derived projections requires capability-specific profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Destination parity separately verifies state, protection, provenance, owner boundaries, and selected operational behavior. | rule/invariant | sourced | [C17](../evidence/statement-provenance.md). |
