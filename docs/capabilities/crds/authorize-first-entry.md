# Authorize first entry

## Identity
- **Name:** Authorize first entry
- **Definition:** Issue and consume a bounded, expiring authorization for an onboarding owner to enter a prepared product environment for the first time.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Join onboarding completion to authenticated first access without treating an invitation as permanent or general authority.
- **Meaningful outcome:** A first-entry authorization is issued, consumed once, expired, revoked, replaced, or denied with attributable evidence.
- **Boundaries — includes:** journey and owner/contact binding, destination, credential reference, issue time, expiry, one-time use, resend/replacement, validation, consumption, denial, and entry event.
- **Boundaries — excludes:** contact-channel verification, environment preparation, general sign-in, account recovery, broad Core authorization, and the content of the onboarding journey.
- **Terms and concepts:** A `first-entry authorization` is a narrow bootstrap credential; its validity and scope end according to the declared entry policy.

## Interaction Contract MLEs
### Issue or consume first-entry authorization
- **Actor:** An authorized onboarding service issues the authorization; the onboarding owner presents it for entry.
- **Command / intent:** Create or use a bounded credential for the prepared environment's first authenticated entry.
- **Current state:** An eligible journey, required channel/identity evidence, destination binding, and applicable entry policy exist.
- **Policies / invariants:** Credentials are time-bounded, destination- and journey-bound, replay-resistant, revocable, and stored only as protected references; replacement invalidates prior authority according to policy; consumption cannot broaden later permissions.
- **Transition:** Issue, validate, consume, expire, revoke, replace, or deny the authorization and record the outcome.
- **Result:** An issued, consumed, expired, revoked, replaced, or denied first-entry authorization record and, on valid consumption, a bounded authenticated entry result.
- **Events / effects:** May mark the onboarding journey complete and present the prepared environment and retained continuity through owner-facing interfaces.
- **Unknowns:** Account-creation timing and assurance requirements differ across deployment and identity profiles.

## Rules and defaults
### Rules / invariants
- A first-entry invitation must not be treated as a reusable password, general API credential, or ongoing authorization grant.
- Expired, revoked, mismatched, or previously consumed credentials must fail closed.
### Recommended defaults
- Prefer single-use, short-lived credentials with an explicit resend or recovery path.

### Communication MLEs
#### First-entry invitation
- **Purpose:** Explain that the prepared environment is available and how to enter it safely.
- **Trigger:** A first-entry authorization is issued or replaced.
- **Audience:** The verified onboarding contact.
- **Required meaning:** Destination, expiry, single-use nature, safe failure/reissue path, and that later permissions remain separately governed.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Your first entry link is ready, expires soon, and can be used once. Request a new link if it expires.”
- **Possible realizations:** email, secure message, device handoff, or operator-assisted invitation.

## Unknown / unresolved
- The relationship between first-entry consumption, persistent account creation, and later authentication remains implementation-profile specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| First-entry authorization is a separate, expiring, single-use transition into a prepared environment. | rule/invariant | sourced | [D10](../evidence/statement-provenance.md). |
