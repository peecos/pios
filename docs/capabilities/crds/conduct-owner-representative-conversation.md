# Conduct an owner-representative conversation

## Identity
- **Name:** Conduct an owner-representative conversation
- **Definition:** Participate in an external conversation as an owner-authorized AI representative using a bounded identity, audience, knowledge, and action scope.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make selected owner knowledge and perspective conversationally available to others without exposing the owner's private Core or granting the representative unrestricted authority.
- **Meaningful outcome:** A participant receives an attributable response from the configured representative, or the interaction is declined or escalated, with conversation and governance evidence preserved.
- **Boundaries — includes:** representative identity, AI disclosure, audience and access state, dedicated knowledge scope, retrieval boundaries, conversation context, response provenance, refusal, escalation, session lifecycle, and audit evidence.
- **Boundaries — excludes:** maintaining the agent definition, selecting the outward identity mode, populating the knowledge scope, granting publication/access rights, acting through the owner's undisclosed identity, and executing unrelated external actions.
- **Terms and concepts:** An owner-representative `conversation` may map to `schema.org/Conversation`; participants map to `schema.org/Person` or relevant organization identities. An `AI Twin` is one possible product realization, not the generic capability itself.

## Interaction Contract MLEs
### Respond as an owner-authorized representative
- **Actor:** An external participant and an owner-authorized representative agent.
- **Command / intent:** Ask, discuss, or request information within the representative's declared purpose and audience scope.
- **Current state:** The representative identity, disclosure posture, participant access, dedicated knowledge scope, conversation state, current policy, and escalation path can be determined.
- **Policies / invariants:** AI nature and owner relationship are disclosed for this representative mode; only explicitly allocated outward knowledge is available; private Core and private assistant conversations are excluded; unsupported, sensitive, or unauthorized requests are refused or escalated; responses and source use are attributable.
- **Transition:** Authenticate or admit the participant as required, assemble permitted context, generate or select a response, apply safety and authority checks, deliver or refuse it, and record the interaction.
- **Result:** A delivered representative response, clarification request, refusal, escalation, or failed interaction with provenance.
- **Events / effects:** May create conversation events, owner attention items, proposals, or follow-up work through separate capabilities.
- **Unknowns:** Universal disclosure wording, response-liability treatment, escalation timing, retention, and participant-consent requirements are not established.

## Rules and defaults
### Rules / invariants
- An outward representative must not inherit the owner's private Core or private-agent memory by default.
- Representative conversation authority does not imply authority to transact, publish new material, or act through the owner's undisclosed identity.
### Recommended defaults
- Use a purpose-specific knowledge scope, visible AI disclosure, bounded audience, source-aware responses, and an accessible owner-escalation path.

## Unknown / unresolved
- Multi-turn consent, correction, abuse handling, and cross-channel continuity require implementation and governance profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Owner-representative AI conversation uses a dedicated outward knowledge scope, explicit identity/disclosure, controlled audience, and owner governance. | rule/invariant | sourced | [J10–J12](../evidence/statement-provenance.md). |
