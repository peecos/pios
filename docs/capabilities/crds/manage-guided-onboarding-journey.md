# Manage a guided onboarding journey

## Identity
- **Name:** Manage a guided onboarding journey
- **Definition:** Maintain a resumable, inspectable progression from onboarding initiation to an explicit completion, pause, abandonment, or failure state.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let an owner progress through staged setup without losing prior answers, provenance, or control when channels, pacing, or depth vary.
- **Meaningful outcome:** The journey has a current stage, completed-step evidence, an explicit next action, and a terminal or resumable disposition.
- **Boundaries — includes:** journey identity, stage and step state, selected setup depth, raw responses, parsed responses, pacing, pause/resume, override evidence, and completion state.
- **Boundaries — excludes:** contact-channel verification, personal-AI identity, durable environment configuration, first-entry authorization, permanent account lifecycle, and a particular email or screen sequence.
- **Terms and concepts:** A `journey` coordinates independently governed setup outcomes; completing a step does not imply that every adjacent capability succeeded.

## Interaction Contract MLEs
### Start or progress an onboarding journey
- **Actor:** An owner or an authorized onboarding orchestrator acting for the owner.
- **Command / intent:** Start, resume, answer, defer, or complete the next eligible onboarding step.
- **Current state:** A journey identity, current stage, prior responses, applicable setup profile, and owner/contact binding exist or can be created.
- **Policies / invariants:** Raw owner responses are preserved; parsed structure remains traceable to them; optional detail does not block a viable setup; automated progression follows declared policy; manual overrides are attributable and cannot fabricate owner input.
- **Transition:** Record the response or control action, evaluate the stage policy, preserve the resulting state, and identify the next step or terminal disposition.
- **Result:** An active, paused, completed, abandoned, or failed journey record with an explicit next action when applicable.
- **Events / effects:** May request contact verification, identity maintenance, preference configuration, environment preparation, or first-entry authorization.
- **Unknowns:** Universal stage definitions, channel choices, pacing, and abandonment rules are not established.

## Rules and defaults
### Rules / invariants
- Journey progress must not be represented as contact verification, identity proof, environment readiness, or authorized entry without the corresponding evidence.
- Resuming a journey must preserve prior source answers and supersession history.
### Recommended defaults
- Prefer progress over optional completeness while clearly marking defaults and unresolved setup items.

### Communication MLEs
#### Onboarding progress notice
- **Purpose:** Explain the current stage and what the owner can do next.
- **Trigger:** A step completes, pauses, fails, or awaits an owner response.
- **Audience:** The onboarding owner.
- **Required meaning:** Current stage, retained progress, next action, and whether any result is provisional.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Your progress is saved. Continue with the next setup step when you are ready.”
- **Possible realizations:** email, product screen, message, or owner update.

## Unknown / unresolved
- Which onboarding stages are required for each PIOS implementation or product profile remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Onboarding progression is staged, resumable, and distinct from the capabilities that create identity, prepare configuration, and authorize entry. | rule/invariant | sourced | [D04 and D07](../evidence/statement-provenance.md). |
