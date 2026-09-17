# Maintain a contact point

## Identity
- **Name:** Maintain a contact point
- **Definition:** Create and revise a typed means of contacting or locating a person, preserving its label, provenance, lifecycle, and any separately established verification state.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep communication coordinates independently maintainable from a person's descriptive profile and relationship meaning.
- **Meaningful outcome:** A current contact point exists for an eligible person with type, value, optional label, verification status, provenance, and lifecycle state.
- **Boundaries — includes:** creation, normalization, revision, primary designation, linkage to verification evidence, invalidation, expiry, deletion or archival, provenance, and attachment to a person profile.
- **Boundaries — excludes:** establishing control of the contact point, sending messages, proving the person's legal identity, account authentication, relationship classification, and general authorization to use the channel.
- **Terms and concepts:** A `contact point` maps to `schema.org/ContactPoint` where applicable and may represent email, telephone, address, URL, social identifier, or another declared contact method.

## Interaction Contract MLEs
### Maintain contact-point lifecycle
- **Actor:** The owner, the contact subject where supported, or an authorized contact-management process.
- **Command / intent:** Add, correct, prioritize, invalidate, or remove a contact point for a known person.
- **Current state:** The person identity, current points, supplied value, type, source, and authority can be determined.
- **Policies / invariants:** Contact values remain owner-scoped and sensitivity-aware; normalization does not erase the supplied form; verification state is evidence-backed and cannot be inferred from successful storage; duplicates and conflicts are explicit; removal does not erase required provenance.
- **Transition:** Validate the point and subject link, normalize where safe, update its lifecycle state and any reference to separately established verification evidence, and record provenance and result.
- **Result:** A current, invalid, superseded, removed, or rejected contact point with its verification status represented accurately.
- **Events / effects:** May enable later communication, verification, deduplication, or relationship workflows without authorizing those actions.
- **Unknowns:** Universal verification methods, normalization rules, uniqueness scope, and retention periods are not established.

## Rules and defaults
### Rules / invariants
- Storing a contact point must not be represented as proof that it is controlled by or still belongs to the named person.
- A contact point must retain its person relationship and source provenance.
### Recommended defaults
- Preserve the supplied value, a normalized comparison value where appropriate, type, label, source, last-confirmed time, and verification status.

## Unknown / unresolved
- Verification assurance and reuse of onboarding channel-control evidence are defined by the separate contact-point-control capability and still require shared security profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A contact point is a typed, independently managed communication coordinate linked to a person profile while control verification remains a separate evidenced outcome. | rule/invariant | sourced | [I05–I07](../evidence/statement-provenance.md). |
