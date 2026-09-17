# Maintain a human contact profile

## Identity
- **Name:** Maintain a human contact profile
- **Definition:** Create and revise an owner-held profile for another person with identity, descriptive context, source links, and lifecycle state.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve useful knowledge about a person in the owner's world without confusing that person with the owner, an agent, a glossary identity, or a stream of interactions.
- **Meaningful outcome:** A current human contact profile exists with stable identity, owner scope, selected descriptive attributes, provenance, lifecycle state, and links to contact points and relationship context.
- **Boundaries — includes:** profile creation, revision, activation or retirement, names and aliases, descriptive attributes, organization or role context, notes, source references, provenance, and related-object links.
- **Boundaries — excludes:** owner self-profile, agent profile, contact-point lifecycle, relationship/consent governance, communication events, access control, and public representation.
- **Terms and concepts:** A `human contact profile` is an owner-scoped projection about another `person` (`schema.org/Person`). It is not proof that every stored attribute is current or subject-confirmed.

## Interaction Contract MLEs
### Maintain contact-profile lifecycle
- **Actor:** The owner or an authorized relationship-knowledge process.
- **Command / intent:** Create, revise, activate, retire, correct, or merge a profile for another person.
- **Current state:** Candidate identity, existing profiles, source evidence, owner scope, and current lifecycle state can be determined.
- **Policies / invariants:** Owner and contact subjects remain distinct; uncertain attributes are not presented as verified facts; duplicate identities are reconciled explicitly; revisions preserve provenance; sensitivity, consent, and exposure rules apply independently.
- **Transition:** Resolve or create the person identity, validate the requested attributes, update the profile version and lifecycle state, and preserve source and merge relationships.
- **Result:** A current, merged, retired, disputed, or rejected human contact profile with traceable history.
- **Events / effects:** May support relationship context, communication lookup, contextual classification, retrieval, and Circle views without granting access or sending communication.
- **Unknowns:** Universal identity-resolution, subject-consent, retention, and sensitive-attribute policies are not established.

## Rules and defaults
### Rules / invariants
- A human contact profile must not be treated as the owner's profile or as an agent-definition record.
- Dynamic interactions remain linked events or records rather than silently overwriting slowly changing profile attributes.
### Recommended defaults
- Preserve only useful, attributable attributes and keep last-reviewed time and source references where staleness matters.

## Unknown / unresolved
- The authority model for maintaining inferred or sensitive facts about another person requires a relationship/privacy profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Human contact profiles are owner-scoped My World knowledge projections with distinct subject, authority, provenance, and lifecycle treatment. | rule/invariant | sourced | [I01–I04](../evidence/statement-provenance.md). |
