# Maintain personal relationship context

## Identity
- **Name:** Maintain personal relationship context
- **Definition:** Preserve how the owner relates to another person or organization, including scope, role, trust, consent, origin, and time-bounded context.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Represent relationship meaning independently from identity, contact coordinates, individual interactions, and access grants.
- **Meaningful outcome:** A relationship context exists with participants, relationship type or label, Circle scope, trust and consent state where relevant, origin and evidence, validity, and lifecycle history.
- **Boundaries — includes:** participant identity references, relationship type, owner-specific label, Circle scope, trust context, consent state, origin story, source links, applicable roles, validity period, revision, dispute, and retirement.
- **Boundaries — excludes:** creating the person profile, maintaining contact points, recording each communication or event, assigning temporary with-whom context, granting data access, and publishing relationship information.
- **Terms and concepts:** `relationship context` links `person` or `organization` identities (`schema.org/Person`, `schema.org/Organization`) while preserving owner-specific meaning that may not map exactly to a public vocabulary.

## Interaction Contract MLEs
### Maintain relationship-context lifecycle
- **Actor:** The owner or an authorized relationship-knowledge process.
- **Command / intent:** Create, revise, confirm, dispute, or retire the owner's relationship context for another person or organization.
- **Current state:** Participant identities, prior relationship state, available evidence, consent constraints, and owner authority can be determined.
- **Policies / invariants:** Relationship identity is distinct from each participant; owner-specific interpretation and externally asserted facts remain distinguishable; changes are time-aware and attributable; relationship scope does not automatically grant access; individual interactions remain separate evidence.
- **Transition:** Validate participants and authority, preserve or revise relationship meaning and scope, attach source evidence, and record lifecycle and validity changes.
- **Result:** A current, disputed, superseded, retired, or rejected relationship-context record.
- **Events / effects:** May guide retrieval, active context, Circle grouping, sharing review, contact presentation, and future proposals without modifying those systems automatically.
- **Unknowns:** Universal consent, shared-history, reciprocal-relationship, and third-party correction rules are not established.

## Rules and defaults
### Rules / invariants
- Relationship scope and trust context must not be interpreted as an access-control grant.
- An inferred or imported relationship must retain its source and confidence until explicitly confirmed or corrected.
### Recommended defaults
- Keep relationship type, origin, current scope, source evidence, last-reviewed time, and material consent constraints explicit.

## Unknown / unresolved
- Cross-owner and reciprocal relationship records require consent and conflict-resolution profiles beyond this CRD.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Relationship context is a distinct owner-scoped record linking people or organizations with scope, consent, provenance, and lifecycle rather than replacing their identities or interactions. | rule/invariant | sourced | [I08–I10](../evidence/statement-provenance.md). |
