# Verify control of a contact point

## Identity
- **Name:** Verify control of a contact point
- **Definition:** Establish bounded evidence that a subject controls or can receive through a declared contact point under a stated verification method.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Distinguish stored contact information from evidence that the declared channel is currently controlled.
- **Meaningful outcome:** A contact point has a verified, failed, expired, revoked, or still-unverified control result with method, assurance, time bounds, and evidence.
- **Boundaries — includes:** contact-point identity, subject or participant binding, challenge or method, response evidence, validity window, replay and mismatch handling, revocation, manual-review evidence, and assurance level.
- **Boundaries — excludes:** legal identity proof, maintaining the contact value itself, general account authentication, communication authorization, relationship classification, and first-entry authorization.
- **Terms and concepts:** A verified `contact point` (`schema.org/ContactPoint`) establishes evidence of channel control under a declared method; it does not prove all claims about the associated `person` (`schema.org/Person`).

## Interaction Contract MLEs
### Verify contact-point control
- **Actor:** The contact subject or onboarding participant and an authorized verification service or operator.
- **Command / intent:** Establish whether the actor controls the declared contact point.
- **Current state:** The contact point, claimed subject or journey participant, verification method, prior verification state, and unexpired evidence opportunity can be determined.
- **Policies / invariants:** Evidence is bound to the exact contact point and subject context; replayed, expired, automated, or mismatched evidence fails closed; method and assurance are recorded; revocation and re-verification remain explicit; success does not grant broader identity or action authority.
- **Transition:** Issue or identify the bounded verification challenge, evaluate returned evidence, consume or expire it as applicable, and record the result.
- **Result:** A verified, failed, expired, revoked, or pending contact-point-control record.
- **Events / effects:** May update the linked contact point's displayed verification state or satisfy a separate onboarding/account policy.
- **Unknowns:** Which methods and assurance levels are sufficient for each contact type, risk, and jurisdiction are not established.

## Rules and defaults
### Rules / invariants
- Contact-point verification must not be represented as legal identity proof or general authorization.
- Verification evidence must be scoped, time-bounded where appropriate, and replay-resistant.
### Recommended defaults
- Record the method, verifier, subject binding, challenge or evidence reference, verification time, expiry, and revocation state.

## Unknown / unresolved
- Portability and reuse of verification evidence across onboarding, contact management, authentication, and recovery require explicit profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Contact-point control verification is independently meaningful across contact management and onboarding and remains narrower than identity proof or authorization. | rule/invariant | sourced with security qualification | [I07 and D08](../evidence/statement-provenance.md). |
