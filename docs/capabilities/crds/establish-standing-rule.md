# Establish a standing rule

## Identity

- **Name:** Establish a standing rule
- **Definition:** Convert explicit authorized confirmation into a bounded, reviewable rule that can govern later matching situations.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Create reusable authority without silently inferring permission from repeated behavior.
- **Meaningful outcome:** A traceable rule defines its condition, permitted action, scope, confidence behavior, lifecycle, and authority source.
- **Boundaries — includes:** confirmation, condition and action scope, threshold, activation, review, suspension, revocation, and provenance.
- **Boundaries — excludes:** detecting a candidate pattern, presenting the proposal, applying the rule to a specific situation, and performing the domain action.
- **Terms and concepts:** A `standing rule` is reusable delegated authority, not merely executable code.

## Interaction Contract MLEs

### Establish or change a rule

- **Actor:** The owner or explicitly authorized rule governor.
- **Command / intent:** Confirm, edit, suspend, revoke, or supersede a bounded standing rule.
- **Current state:** A rule proposal or existing rule and its evidence are available.
- **Policies / invariants:** Creation requires explicit confirmation; condition, action, scope, and confidence behavior are explicit; changes retain provenance; revocation prevents future application.
- **Transition:** Validate authority, establish the requested rule state, and record review conditions.
- **Result:** A traceable active, suspended, revoked, or superseded rule.
- **Events / effects:** The state change affects later rule evaluations and may notify the owner.
- **Unknowns:** Universal review cadence is not established.

## Rules and defaults

### Rules / invariants

- No silent rule creation.
- Repeated confirmation alone does not create a rule without an explicit authorization transition.

### Recommended defaults

- Prefer narrow condition/action scope and periodic review.

### Communication MLEs

#### Rule needs confirmation or review

- **Purpose:** Obtain or renew authority for reusable action.
- **Trigger:** A proposed rule awaits confirmation or an active rule reaches review conditions.
- **Audience:** Authorized rule governor.
- **Required meaning:** State the condition, permitted action, scope, evidence, confidence behavior, and effect of approval.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Confirm whether this situation may be handled automatically in the future.”
- **Possible realizations:** update feed, approval UI, agent response, or API event.

## Unknown / unresolved

- No publicly confirmed operational realization is currently recorded.

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A standing rule requires confirmed authority. | rule/invariant | sourced | [Pilot provenance P08](../evidence/statement-provenance.md). |
