# Verify an onboarding contact channel

## Identity
- **Name:** Verify an onboarding contact channel
- **Definition:** Establish evidence that the onboarding participant controls the contact channel bound to a journey.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Prevent an onboarding flow from treating an unverified destination as a trusted continuation channel.
- **Meaningful outcome:** The journey records a verified, failed, expired, revoked, or still-unverified channel-control result at a declared assurance level.
- **Boundaries — includes:** channel identity, challenge or thread binding, response evidence, validity window, automation/bounce rejection, attempt state, manual-review evidence, and assurance level.
- **Boundaries — excludes:** proof of a person's legal identity, general account authentication, owner authorization for Core actions, first-entry credentials, and long-term account recovery.
- **Terms and concepts:** `verified contact channel` means evidence of channel control under a stated method; it specializes [Verify control of a contact point](verify-contact-point-control.md) by binding the result to an onboarding journey and does not by itself prove who the person is.

## Interaction Contract MLEs
### Verify control of an onboarding channel
- **Actor:** The onboarding participant and an authorized verification service or operator.
- **Command / intent:** Prove control of the channel associated with the journey.
- **Current state:** An active journey, declared channel, verification method, and unexpired challenge or eligible conversation thread exist.
- **Policies / invariants:** Evidence is bound to the same journey and channel; machine responses, bounces, replays, and mismatched senders are rejected; method and assurance are recorded; manual overrides are attributable and bounded.
- **Transition:** Evaluate the response evidence, consume or expire the challenge as applicable, and record the verification result.
- **Result:** A verified, failed, expired, revoked, or pending channel-verification record.
- **Events / effects:** May permit the journey to continue or make first-entry authorization eligible under a separate policy.
- **Unknowns:** Which verification methods satisfy each risk profile is not established.

## Rules and defaults
### Rules / invariants
- Channel verification must not be represented as full identity proof or general Core authority.
- Reused, expired, automated, or mismatched evidence must fail closed.
### Recommended defaults
- Use short-lived, replay-resistant evidence and record the exact assurance method.

## Unknown / unresolved
- Reply-based verification may be suitable for low-assurance onboarding but requires a separately approved threat model for higher-risk use.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Onboarding contact verification is an independently evidenced channel-control result and does not establish broader identity or authority. | rule/invariant | sourced with security qualification | [D08](../evidence/statement-provenance.md). |
