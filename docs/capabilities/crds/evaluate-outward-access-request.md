# Evaluate an outward access request

## Identity
- **Name:** Evaluate an outward access request
- **Definition:** Decide whether one requester may open a governed outward representation under the currently applicable access policy and request context.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Enforce outward access conditions at request time without changing the access policy, discoverability, or usage rights.
- **Meaningful outcome:** One access request receives an attributable allow or deny decision with the evaluated policy and reasons recorded.
- **Boundaries — includes:** requester or audience identity, representation reference, current policy version, credential or grant evidence, expiry, contextual conditions, fail-closed evaluation, decision reason, and audit evidence.
- **Boundaries — excludes:** creating or revising access policy, activating a share, publishing content, changing discoverability, granting usage rights, and mutating the private source.
- **Terms and concepts:** An `access decision` applies a current policy to one request; it is not the policy itself and does not determine permitted reuse after access.

## Interaction Contract MLEs
### Evaluate one access request
- **Actor:** An outward-access enforcement point acting for an identified requester.
- **Command / intent:** Determine whether the requester may open the referenced outward representation now.
- **Current state:** The representation, requester identity or audience evidence, current access-policy version, grant or credential state, expiry, and applicable context can be determined.
- **Policies / invariants:** Evaluation uses the current applicable policy; missing, expired, revoked, mismatched, or ambiguous authority fails closed; the decision does not broaden usage rights or discovery state; reasons and policy version remain attributable.
- **Transition:** Evaluate the request against the applicable policy and record its disposition without changing that policy.
- **Result:** An allow or deny access decision with reasons and evidence references.
- **Events / effects:** An allow may permit delivery; denial may create audit or owner-attention evidence.
- **Unknowns:** Universal identity-assurance levels, any intermediate challenge profile, and distributed enforcement-latency guarantees are not established.

## Rules and defaults
### Rules / invariants
- No access request may be allowed solely because a representation is visible or discoverable.
- An access decision must identify the policy and evidence evaluated.

### Recommended defaults
- Deny when required identity, grant, policy, or freshness evidence is ambiguous.

## Unknown / unresolved
- Offline and third-party delivery profiles may require separately declared enforcement limitations.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Per-request access evaluation is independently meaningful from maintaining access policy and from activating a controlled share. | rule/invariant | sourced | [G08 and G11](../evidence/statement-provenance.md). |
