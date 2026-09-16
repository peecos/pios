# Assess ingestion readiness

## Identity
- **Name:** Assess ingestion readiness
- **Definition:** Determine whether a screened ingestion batch satisfies its governing checklist and is ready to be presented for owner authorization.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep technical evidence, policy readiness, and owner authority as separate gates.
- **Meaningful outcome:** A checklist assessment records pass, fail, or blocked readiness and identifies unresolved retention, remediation, scope, or proof conditions.
- **Boundaries — includes:** bounded-scope check, technical-screen status, stop conditions, retention/remediation posture, planned proof, open decisions, and readiness disposition.
- **Boundaries — excludes:** repeating the technical screen, granting owner authority, performing ingestion, and silently resolving policy decisions.
- **Terms and concepts:** `readiness` means the batch can be presented for authorization; it does not mean authorization has been granted.

## Interaction Contract MLEs
### Determine checklist readiness
- **Actor:** An authorized reviewer or governance agent.
- **Command / intent:** Evaluate whether the screened batch satisfies its governing ingestion checklist.
- **Current state:** A versioned candidate manifest and technical-screen result exist.
- **Policies / invariants:** Unresolved authority, sensitivity, retention, remediation, or source-of-truth questions fail closed; open owner choices remain explicit; readiness cannot expand the manifest scope.
- **Transition:** Evaluate checklist evidence and record pass, fail, or blocked status with outstanding decisions.
- **Result:** A durable ingestion-readiness assessment.
- **Events / effects:** A passing assessment may enable an owner-authorization request.
- **Unknowns:** Checklist profiles for different source classes are not yet universal.

## Rules and defaults
### Rules / invariants
- Readiness assessment cannot replace owner approval.
- A blocked result is valid evidence, not a failed attempt to force progress.
### Recommended defaults
- State exactly which unresolved item prevents readiness.

## Unknown / unresolved
- Who may approve checklist exceptions remains governance-profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Checklist readiness is a separate fail-closed gate between technical screening and owner authorization. | rule/invariant | sourced | [C11](../evidence/statement-provenance.md). |
