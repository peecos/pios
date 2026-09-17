# Configure execution policy

## Identity
- **Name:** Configure execution policy
- **Definition:** Establish versioned rules governing which actions may execute, under whose authority, and when confirmation or escalation is required.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make operational permission and confirmation posture explicit rather than implicit in interfaces or agent behavior.
- **Meaningful outcome:** A current, attributable policy can be evaluated before action execution and its prior versions remain inspectable.
- **Boundaries — includes:** action allow/deny scope, actor/runtime scope, confirmation conditions, effect/risk classes, rule posture, activation, revision, and rollback.
- **Boundaries — excludes:** communication style preferences, granting source access, establishing a standing rule, and executing an action.
- **Terms and concepts:** `execution policy` is governing System information; it is not a user-interface preference or executable action.

## Interaction Contract MLEs
### Change execution policy
- **Actor:** The owner or explicitly delegated policy authority.
- **Command / intent:** Establish or revise action-execution constraints.
- **Current state:** Current policy, affected actions/actors, and requested change are available.
- **Policies / invariants:** Policy changes are versioned and attributable; lower-level settings cannot bypass proposal/rule governance; absence or ambiguity fails closed for guarded effects; rollback remains possible.
- **Transition:** Validate authority, evaluate the change, create a new policy version, and activate or reject it.
- **Result:** An active versioned policy or reasoned rejection.
- **Events / effects:** Future action invocations evaluate the new policy; material changes may require owner notification.
- **Unknowns:** Universal risk classes and confirmation thresholds are not fixed by this CRD.

## Rules and defaults
### Rules / invariants
- Behavior preferences do not grant execution authority.
- Policy does not override mandatory proposal, rule, provenance, or audit constraints.
### Recommended defaults
- Require explicit confirmation for destructive, externally visible, identity-affecting, or high-cost actions unless separately authorized.

## Unknown / unresolved
- Delegation and policy inheritance precedence require later governance work.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Execution permission is distinct from behavior preference and remains governed. | rule/invariant | sourced | [B05](../evidence/statement-provenance.md). |
