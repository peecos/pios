# Share a governed outward representation

## Identity
- **Name:** Share a governed outward representation
- **Definition:** Deliver or activate a distinct outward representation for a bounded audience under an applicable access policy and usage-rights declaration.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Support intentional controlled sharing without exposing the canonical private source or implying public availability.
- **Meaningful outcome:** A selected representation has a bounded share instance and delivery reference, or an explicit rejected, expired, withdrawn, or failed sharing disposition.
- **Boundaries — includes:** representation eligibility, intended audience and scope, applicable access-policy and rights references, approval, delivery or activation, expiry, withdrawal, and sharing evidence.
- **Boundaries — excludes:** preparing the representation, creating or revising access policy or audience grants, evaluating individual access requests, making the representation publicly available, configuring public discovery, mutating the private source, and granting unrelated Core access.
- **Terms and concepts:** `controlled sharing` provides bounded external access without making the representation a public-presence asset.

## Interaction Contract MLEs
### Share with a bounded audience
- **Actor:** The owner or an explicitly authorized sharing actor.
- **Command / intent:** Deliver or activate an eligible outward representation for a defined audience.
- **Current state:** The representation, owner, audience, current exposure state, sensitivity, applicable access policy, rights declaration, and sharing authority can be determined.
- **Policies / invariants:** Private source state remains private; audience and scope are explicit; guarded exposure fails closed without sufficient sharing authority; access evaluation and usage rights remain separate capabilities; withdrawal and expiry do not erase required evidence.
- **Transition:** Validate representation eligibility and sharing authority, bind the audience and applicable policy references, create or activate the share, and record the result.
- **Result:** A controlled share with a stable delivery reference, or a reasoned rejected, expired, withdrawn, or failed disposition.
- **Events / effects:** May notify recipients or create audit events; an enforcement point separately evaluates whether a recipient may open the representation.
- **Unknowns:** Universal recipient-verification and delegated-sharing assurance levels are not established.

## Rules and defaults
### Rules / invariants
- Sharing an outward representation must not expose its canonical private source by implication.
- A notification or sent link does not substitute for an applicable policy and access decision.
### Recommended defaults
- Use the smallest audience, shortest suitable duration, and least permissive rights consistent with the sharing purpose.

## Unknown / unresolved
- Cross-provider recipient identity, forwarding, and offline-copy revocation semantics require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Controlled sharing is a bounded delivery or activation transition distinct from representation preparation, access-policy maintenance, request evaluation, and public presence. | rule/invariant | sourced | [G01–G04 and G11](../evidence/statement-provenance.md). |
