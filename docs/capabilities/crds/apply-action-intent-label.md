# Apply an action-intent label

## Identity
- **Name:** Apply an action-intent label
- **Definition:** Attach or remove a reusable label that communicates intended handling for an item without executing that handling.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let an owner express what should happen next with minimal interaction while preserving the boundary between intent and execution.
- **Meaningful outcome:** An item has an attributable current handling intent, or that intent is removed with history preserved where required.
- **Boundaries — includes:** eligible item, intent-label selection, assignment provenance, removal, and lifecycle.
- **Boundaries — excludes:** performing the action, creating a standing rule, general categorization, and defining the label vocabulary.
- **Terms and concepts:** An `action-intent label` describes intended handling; it is not an executable Action or Skill.

## Interaction Contract MLEs
### Change action intent
- **Actor:** The owner or a process acting through a confirmed proposal or standing rule.
- **Command / intent:** Apply or remove a named handling intent on an item.
- **Current state:** The item, label, authority, and current assignment state are known.
- **Policies / invariants:** The label does not execute by itself; machine suggestions use governed proposal flow; automated assignment requires confirmed authority; provenance distinguishes user, proposal, rule, import, and system sources where supported.
- **Transition:** Validate scope and authority, create or remove/archive the assignment, and record provenance.
- **Result:** A current attributable intent assignment or reasoned rejection.
- **Events / effects:** A proposal or standing rule may separately recommend or invoke handling.
- **Unknowns:** Universal removal-history requirements for owner-confirmed labels are not established.

## Rules and defaults
### Rules / invariants
- Intent labels and executable actions remain distinct.
- No intent label silently grants autonomous execution.
### Recommended defaults
- Keep labels short, reusable, and understandable without implementation knowledge.

## Unknown / unresolved
- Managing Action Tag vocabulary is currently covered by `manage-organizing-label`; a later source may justify a specialization.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Action Tags express intent but do not execute. | rule/invariant | sourced | [B01–B02](../evidence/statement-provenance.md). |
