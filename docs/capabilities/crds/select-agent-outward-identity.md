# Select an agent's outward identity

## Identity
- **Name:** Select an agent's outward identity
- **Definition:** Choose and record the identity presentation, representation relationship, and disclosure posture an agent must use for a bounded outward action or action class.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Ensure external recipients receive an intentional identity signal rather than one selected implicitly by a channel or runtime.
- **Meaningful outcome:** An outward action has an owner-authorized identity mode specifying who is presented, whether AI involvement is disclosed, applicable scope, and escalation expectations.
- **Boundaries — includes:** action or action-class scope, represented party, agent identity, disclosure state, channel context, recipient context, authorization source, expiry, revision, revocation, and escalation framing.
- **Boundaries — excludes:** executing or sending the action, creating the agent identity, maintaining an AI representative, granting source access, and defining the content itself.
- **Terms and concepts:** `outward identity` is the identity and disclosure signal presented to an external audience. It is separate from internal agent identity and runtime role.

## Interaction Contract MLEs
### Select outward identity and disclosure
- **Actor:** The owner or an explicitly delegated identity-governance authority.
- **Command / intent:** Select how an agent may present itself for a specific outward action or governed action class.
- **Current state:** The acting agent, represented party, action, audience, channel, sensitivity, available identity modes, and authority can be determined.
- **Policies / invariants:** No mode is assumed from technical convenience; undisclosed AI action requires the strongest applicable explicit authority; disclosed representative modes identify their relationship to the owner; expiry and revocation are enforceable; selection does not itself execute the action.
- **Transition:** Evaluate identity, disclosure, audience, risk, and authority; record the selected mode or rejection for the bounded scope.
- **Result:** An active, expired, revoked, or rejected outward-identity selection.
- **Events / effects:** May authorize an outward action to proceed to its separate execution gate and supplies disclosure metadata to the delivery surface.
- **Unknowns:** Universal disclosure rules, prohibited contexts, jurisdictional requirements, and standing-authority thresholds are not established.

## Rules and defaults
### Rules / invariants
- The identity mode for an outward action must be explicit and attributable.
- Selecting an outward identity must not grant permission to send, publish, transact, or disclose additional information.
### Recommended defaults
- Prefer clear AI disclosure and owner escalation paths; require action-specific approval for undisclosed representation unless an exact standing rule applies.

## Unknown / unresolved
- Legal, professional, relational, and channel-specific restrictions on undisclosed AI representation require dedicated profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Outward identity and AI disclosure are explicit owner-governed choices separate from agent identity, runtime role, and action execution. | rule/invariant | sourced | [J07–J09](../evidence/statement-provenance.md). |
