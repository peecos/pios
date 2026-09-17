# Schedule a contextual reminder

## Identity
- **Name:** Schedule a contextual reminder
- **Definition:** Maintain an enabled, disabled, snoozed, or recurring trigger that surfaces an attributable reminder for an eligible object or purpose.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Re-surface relevant information or action at an intended time or context without changing the underlying object's execution state.
- **Meaningful outcome:** A valid reminder trigger and lifecycle are preserved, and each material firing or suppression is attributable.
- **Boundaries — includes:** time or context trigger, recurrence, enable/disable, snooze, attachment, firing state, and cancellation/removal.
- **Boundaries — excludes:** task due dates, completing the reminded action, general dynamic scheduling, and notification-channel delivery mechanics.
- **Terms and concepts:** A `reminder` requests future attention. It can be attached to a task, goal, routine, note, or other eligible object without becoming that object.

## Interaction Contract MLEs
### Maintain reminder lifecycle
- **Actor:** An authorized owner, workflow, or planning agent.
- **Command / intent:** Create or change when and why an item should be resurfaced.
- **Current state:** A reminder purpose, eligible target or message, and valid trigger information exist.
- **Policies / invariants:** Trigger requirements match trigger type; recurrence and end conditions are explicit; snooze preserves the original reminder identity; disabled reminders do not fire; firing does not mark the target task complete.
- **Transition:** Validate and persist trigger, recurrence, enabled state, target, and lifecycle changes.
- **Result:** A current reminder definition with attributable state.
- **Events / effects:** A due reminder emits a communication effect through an allowed attention channel.
- **Unknowns:** Location-trigger authority and delivery guarantees are not universally established.

## Rules and defaults
### Rules / invariants
- A due date and a reminder are distinct.
- Reminder deletion or disabling must not delete or complete the attached object.
### Recommended defaults
- Make timezone, recurrence, next firing, and enabled/snoozed state inspectable.

### Communication MLEs
#### Reminder delivery
- **Purpose:** Bring the reminder's target or message back to the intended audience's attention.
- **Trigger:** The reminder becomes due under its trigger and policy.
- **Audience:** The owner or explicitly authorized recipient.
- **Required meaning:** Identify what requires attention, why now, and the relevant action or source.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Reminder: review the project plan today.”
- **Possible realizations:** update, push, inbox item, audible cue, or calendar surface.

## Unknown / unresolved
- Delivery retry, acknowledgement, and missed-reminder policy remain profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Reminders have their own trigger and recurrence lifecycle and remain separate from task state. | rule/invariant | sourced | [B13](../evidence/statement-provenance.md). |
