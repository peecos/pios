# Prepare an initial owner environment

## Identity
- **Name:** Prepare an initial owner environment
- **Definition:** Turn owner-provided onboarding inputs, supported defaults, and declared constraints into a reviewable first-use configuration.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make first entry useful and recognizable without requiring complete personalization or silently promoting guesses into owner-confirmed truth.
- **Meaningful outcome:** A bounded environment-preparation package and report identify what was applied, defaulted, inferred, omitted, or left for later review.
- **Boundaries — includes:** setup-depth choice, presentation preferences, candidate roles and modes, priorities, relevant tools, starter surfaces, source provenance, defaults, readiness, and preparation report.
- **Boundaries — excludes:** creating external connections or credentials, granting access, first-entry authorization, full long-term personalization, and treating inferred setup as confirmed owner knowledge.
- **Terms and concepts:** An `initial environment` is a revisable starting configuration, not a complete or permanent model of the owner.

## Interaction Contract MLEs
### Prepare first-use configuration
- **Actor:** The owner or an authorized onboarding/preparation agent.
- **Command / intent:** Build a viable first-use environment from the available onboarding inputs.
- **Current state:** Owner-provided responses, supported configuration targets, applicable defaults, and destination owner/Core context exist.
- **Policies / invariants:** Explicit answers, parsed values, inferences, and defaults remain distinguishable; sparse optional answers do not block a safe minimum; no unsupported role, mode, connection, or authority is invented; every prepared value remains revisable.
- **Transition:** Validate and map inputs, apply allowed defaults, create or propose supported initial settings, and produce readiness and exception evidence.
- **Result:** A ready, partially ready, blocked, or failed preparation package with an inspectable report.
- **Events / effects:** May create provisional or owner-authored configuration through the corresponding domain capabilities and enable first-entry authorization.
- **Unknowns:** The minimum viable preparation set varies by implementation and owner profile.

## Rules and defaults
### Rules / invariants
- Preparation must not silently convert weak inference into owner-confirmed identity, role, mode, preference, or authority.
- Missing optional personalization must be represented as missing or defaulted rather than fabricated.
### Recommended defaults
- Prefer a small coherent environment with visible provenance over broad speculative personalization.

### Communication MLEs
#### Initial environment summary
- **Purpose:** Let the owner understand and revise what has been prepared.
- **Trigger:** Preparation reaches a ready or partially ready state.
- **Audience:** The onboarding owner.
- **Required meaning:** Applied owner choices, defaults, provisional values, omitted items, and available revision actions.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Your first environment is ready with the choices you provided; two optional areas remain unset.”
- **Possible realizations:** pre-entry summary, first-entry panel, downloadable setup record, or owner update.

## Unknown / unresolved
- Which prepared settings should be durable Core state versus application-local presentation remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Initial environment preparation is a bounded, revisable outcome that distinguishes owner input, defaults, and inference. | rule/invariant | sourced | [D07 and D09](../evidence/statement-provenance.md). |
