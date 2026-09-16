# Govern outward access

## Identity
- **Name:** Govern outward access
- **Definition:** Establish and enforce the conditions under which an audience may open a shared or public outward representation.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep access mechanisms and audience grants explicit, revocable, and separate from visibility, discovery, and usage rights.
- **Meaningful outcome:** An outward representation has a current access policy and attributable grant, denial, expiry, or revocation state.
- **Boundaries — includes:** audience or recipient identity, open or gated access mode, credentials or grants by reference, expiry, inheritance and override, enforcement decision, revocation, and access audit evidence.
- **Boundaries — excludes:** preparing content, deciding public discoverability, granting reuse rights, changing the private source, and authorizing unrelated Core operations.
- **Terms and concepts:** `access` answers what a requester must satisfy to open a representation; it does not answer whether the item is discoverable or what reuse is permitted after access.

## Interaction Contract MLEs
### Change and evaluate outward access
- **Actor:** The owner, an authorized access administrator, or an enforcement point evaluating a request.
- **Command / intent:** Establish, revise, revoke, or evaluate access to an outward representation.
- **Current state:** The representation, current policy, requester or audience, credential/grant state, expiry, inheritance, sensitivity, and owner authority can be determined.
- **Policies / invariants:** Access fails closed when required conditions are absent, expired, revoked, mismatched, or ambiguous; inherited rules remain identifiable and overridable where allowed; grants are scoped to the representation or declared collection; access evidence does not broaden rights.
- **Transition:** Validate authority and policy, create or revise access conditions, or evaluate one request and record allow/deny disposition.
- **Result:** A current access policy or one attributable access decision.
- **Events / effects:** May enable delivery, deny access, trigger review, or record audit evidence without changing discoverability or rights.
- **Unknowns:** Universal identity assurance, password handling, delegated administration, and offline enforcement profiles are not established.

## Rules and defaults
### Rules / invariants
- Visibility alone must not be treated as sufficient access authorization where an access mechanism is configured.
- Revocation stops new access at connected enforcement points while preserving required audit evidence.
### Recommended defaults
- Prefer audience-specific, expiring grants over broadly shared credentials for sensitive representations.

## Unknown / unresolved
- Enforcement consistency and revocation latency across distributed caches and third-party delivery systems remain implementation-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Access control is an independently governed outward axis that determines how an audience may open a representation. | rule/invariant | sourced | [G04–G05 and G08](../evidence/statement-provenance.md). |
