# Share a governed outward representation

## Identity
- **Name:** Share a governed outward representation
- **Definition:** Make a distinct outward representation available to a bounded audience under explicit access and usage conditions.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Support intentional controlled sharing without exposing the canonical private source or implying public availability.
- **Meaningful outcome:** A selected representation is shared, rejected, expired, or revoked for a defined audience with authority, access, rights, and provenance recorded.
- **Boundaries — includes:** representation eligibility, intended audience, sharing scope, access conditions, rights reference, approval, activation, expiry, revocation, and audit evidence.
- **Boundaries — excludes:** preparing the representation, making it publicly available, configuring public discovery, mutating the private source, and granting unrelated Core access.
- **Terms and concepts:** `controlled sharing` provides bounded external access without making the representation a public-presence asset.

## Interaction Contract MLEs
### Share with a bounded audience
- **Actor:** The owner or an explicitly authorized sharing actor.
- **Command / intent:** Grant a defined audience access to an eligible outward representation.
- **Current state:** The representation, owner, audience, current exposure state, sensitivity, access conditions, rights, and authority can be determined.
- **Policies / invariants:** Private source state remains private; audience and scope are explicit; guarded exposure fails closed without sufficient authority; access and rights are evaluated separately; revocation and expiry do not erase required evidence.
- **Transition:** Validate representation eligibility and authority, bind the intended audience and policy state, activate or reject the share, and record the result.
- **Result:** A controlled share with a stable reference and current access state, or a reasoned rejection.
- **Events / effects:** May notify recipients, create audit events, or later expire or revoke access without changing source ownership.
- **Unknowns:** Universal recipient-verification and delegated-sharing assurance levels are not established.

## Rules and defaults
### Rules / invariants
- Sharing an outward representation must not expose its canonical private source by implication.
- A notification or sent link does not substitute for an enforceable access state.
### Recommended defaults
- Use the smallest audience, shortest suitable duration, and least permissive rights consistent with the sharing purpose.

## Unknown / unresolved
- Cross-provider recipient identity, forwarding, and offline-copy revocation semantics require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Controlled sharing is a bounded audience transition distinct from public presence and from preparation of the outward representation. | rule/invariant | sourced | [G01–G04](../evidence/statement-provenance.md). |
