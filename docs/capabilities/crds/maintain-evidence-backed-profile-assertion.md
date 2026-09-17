# Maintain an evidence-backed profile assertion

## Identity
- **Name:** Maintain an evidence-backed profile assertion
- **Definition:** Preserve a governed assertion about a profile subject with evidence, confidence, validity, provenance, and lifecycle.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make profile knowledge explainable, revisable, and time-aware instead of assumed or silently inferred.
- **Meaningful outcome:** A current assertion can be interpreted together with its authority, evidence, confidence, validity, and history.
- **Boundaries — includes:** proposal/confirmation lineage, statement, class, evidence links, confidence, validity period, revision, dispute, supersession, and deprecation.
- **Boundaries — excludes:** owner-authored profile documents, raw observations, pattern detection, dispute resolution itself, and presentation-specific profile screens.
- **Terms and concepts:** A profile `assertion` is a sourced claim about a subject, not an unqualified fact.

## Interaction Contract MLEs
### Establish or revise an assertion
- **Actor:** The profile subject or a process acting through governed proposal/standing authority.
- **Command / intent:** Establish, revise, supersede, or deprecate an evidence-backed profile assertion.
- **Current state:** Evidence and any prior assertion/version are available.
- **Policies / invariants:** Subject authority is explicit; evidence and provenance remain linked; model-generated claims begin non-authoritative; validity and confidence are not omitted when material; revisions do not erase prior state.
- **Transition:** Validate authority and evidence, record the new lifecycle state/version, and retain supersession links.
- **Result:** A traceable current or deprecated assertion, or a pending/rejected proposal.
- **Events / effects:** Retrieval may use assertions according to status, validity, purpose, and authorization.
- **Unknowns:** Exact confidence scales are profile-specific.

## Rules and defaults
### Rules / invariants
- Import or observation does not directly become confirmed profile knowledge.
- Owner-authored facts and owner review override inferred updates about the owner.
### Recommended defaults
- Begin with few assertions rather than populate an authoritative-looking profile from weak evidence.

## Unknown / unresolved
- Authority for profiles of people other than the owner requires later relationship/consent work.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Profile assertions preserve evidence, confidence, validity, provenance, and lifecycle. | rule/invariant | sourced | [K09–K10](../evidence/statement-provenance.md). |
