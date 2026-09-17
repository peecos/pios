# Decide a governed proposal

## Identity

- **Name:** Decide a governed proposal
- **Definition:** Preserve an evidence-backed suggestion through an explicit authorized decision and retain the decision's provenance.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Permit suggestions without silently converting inference into accepted truth or authority.
- **Meaningful outcome:** A proposal has a durable disposition and traceable relationship to its evidence and any resulting object.
- **Boundaries — includes:** creation, rationale, evidence, confidence, decision authority, confirmation, rejection, editing, expiry, supersession, and result linkage.
- **Boundaries — excludes:** notification delivery, pattern detection, rule establishment, and executing a standing rule.
- **Terms and concepts:** A `proposal` is the decision object; an Update or notification is only a presentation channel.

## Interaction Contract MLEs

### Submit and decide a proposal

- **Actor:** A proposer and an authorized decider, which may be different actors.
- **Command / intent:** Record a suggestion and decide whether and how it should take effect.
- **Current state:** A candidate change, rationale, and available evidence exist without a terminal decision.
- **Policies / invariants:** Proposal precedes governed effect; rationale and evidence are captured at creation; only authorized decisions cause effect; rejection and expiry remain in history; resulting objects link to the decision.
- **Transition:** Create the pending proposal, expose it for decision, record the disposition, and create or link any approved result.
- **Result:** A confirmed, rejected, edited, expired, or superseded proposal with provenance.
- **Events / effects:** Confirmation may invoke another governed capability; rejection history may constrain later similar suggestions.
- **Unknowns:** A universal similarity policy for consulting rejection history is not established.

## Rules and defaults

### Rules / invariants

- A durable governed change requires an authorized decision unless existing standing authority covers it.
- Rejection remains recorded even when no reason is supplied.
- The proposal record remains distinct from its presentation.

### Recommended defaults

- Expire stale proposals rather than deleting them.

### Communication MLEs

#### Proposal requires decision

- **Purpose:** Inform an authorized decider that a proposal awaits action.
- **Trigger:** A proposal enters a decision-needed state.
- **Audience:** Authorized decider.
- **Required meaning:** Identify the proposed change, rationale, evidence or confidence, and available dispositions.
- **Representative example text:** *Example; illustrative, not shipped copy:* “A proposed change is ready for review.”
- **Possible realizations:** update feed, inbox item, push, email, agent response, or API event.

## Unknown / unresolved

- No publicly confirmed operational realization is currently recorded.

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Proposal rationale/evidence precedes decision and dispositions persist. | rule/invariant | sourced | [Pilot provenance P07](../evidence/statement-provenance.md). |
