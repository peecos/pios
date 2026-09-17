# Maintain outward access policy

## Identity
- **Name:** Maintain outward access policy
- **Definition:** Establish, revise, suspend, or revoke the policy and audience grants governing access to an outward representation.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep access conditions and audience grants explicit, versioned, revocable, and separate from sharing, request-time enforcement, discovery, and usage rights.
- **Meaningful outcome:** An outward representation has a current attributable access policy and grant state, or an explicit suspended, expired, revoked, rejected, or superseded policy disposition.
- **Boundaries — includes:** audience or recipient identity, open or gated access mode, credentials or grants by reference, expiry, inheritance and override, policy versioning, suspension, revocation, and policy-change evidence.
- **Boundaries — excludes:** evaluating one access request, activating or delivering a share, preparing content, deciding public discoverability, granting reuse rights, changing the private source, and authorizing unrelated Core operations.
- **Terms and concepts:** `access` answers what a requester must satisfy to open a representation; it does not answer whether the item is discoverable or what reuse is permitted after access.

## Interaction Contract MLEs
### Maintain access policy and grants
- **Actor:** The owner or an authorized access administrator.
- **Command / intent:** Establish, revise, suspend, expire, or revoke access policy or audience grants for an outward representation.
- **Current state:** The representation, current policy, intended audience, credential or grant references, expiry, inheritance, sensitivity, and owner authority can be determined.
- **Policies / invariants:** Grants remain explicitly scoped; inherited rules remain identifiable and overridable only where allowed; policy changes do not alter discoverability or usage rights; revocation preserves required evidence.
- **Transition:** Validate authority, create or revise the policy and grants, or record suspension, expiry, revocation, rejection, or supersession.
- **Result:** A current versioned access policy and attributable grant state or explicit non-active disposition.
- **Events / effects:** Enforcement points may use the current policy for separate request decisions; changes may trigger audit or recipient notices.
- **Unknowns:** Universal identity assurance, password handling, delegated administration, and offline enforcement profiles are not established.

## Rules and defaults
### Rules / invariants
- Policy or grant existence does not itself prove that any particular request was allowed.
- Revocation preserves required evidence and directs connected enforcement points to deny subsequent requests.
### Recommended defaults
- Prefer audience-specific, expiring grants over broadly shared credentials for sensitive representations.

## Unknown / unresolved
- Enforcement consistency and revocation latency across distributed caches and third-party delivery systems remain implementation-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Access-policy maintenance is independently meaningful from sharing, request evaluation, discoverability, and usage rights. | rule/invariant | sourced | [G04–G05, G08, and G11](../evidence/statement-provenance.md). |
