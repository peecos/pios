# Publish a governed outward representation

## Identity
- **Name:** Publish a governed outward representation
- **Definition:** Make an eligible outward representation publicly reachable under explicit visibility, discovery, access, rights, and owner-authority conditions.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Establish an auditable public presence transition without converting private canonical information into public truth by implication.
- **Meaningful outcome:** A representation is published, republished, rejected, unpublished, or archived with a stable outward identity, current policy state, provenance, and revision history.
- **Boundaries — includes:** publication eligibility, owner authority, public locator, version, visibility state, access-policy reference, discovery state, usage-rights state, activation, revision, unpublishing, archival, and audit evidence.
- **Boundaries — excludes:** preparing or redacting source content, controlled private sharing, domain registration, search optimization work, and mutating the canonical private source.
- **Terms and concepts:** `publication` makes a separate representation publicly reachable. Public reachability and public discoverability remain different claims.

## Interaction Contract MLEs
### Publish or withdraw a representation
- **Actor:** The owner or an explicitly authorized publishing actor.
- **Command / intent:** Publish, revise, republish, unpublish, or archive an eligible representation.
- **Current state:** The representation, source provenance, sensitivity, current exposure state, policy axes, public locator, and action authority can be determined.
- **Policies / invariants:** Publication is an external action; guarded publication requires request-scoped approval or applicable standing authority; the private source is not implicitly exposed; each public revision and withdrawal is attributable; access, discovery, and rights remain independently governed.
- **Transition:** Validate authority and exposure conditions, bind the publication revision and policy state, change public reachability, and record the outcome.
- **Result:** A reachable public representation with a stable locator, a withdrawn or archived revision, or a reasoned rejection.
- **Events / effects:** May update indexes, public listings, caches, notifications, or History according to separate policy and realization behavior.
- **Unknowns:** Universal propagation, cache invalidation, archival, and public-locator reuse rules are not established.

## Rules and defaults
### Rules / invariants
- Preparing a representation or setting outward intent must not be represented as publication.
- Public access must not silently imply indexing, promotion, reuse, AI training, or redistribution permission.
### Recommended defaults
- Require explicit owner review for first publication and material expansion of audience, discovery, or usage rights.

## Unknown / unresolved
- Publication profiles must define how withdrawals propagate to external caches, mirrors, archives, and indexes.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Publication is an authorized external transition over a separate outward representation and does not collapse access, discovery, or rights into one state. | rule/invariant | sourced | [G01–G03 and G05–G07](../evidence/statement-provenance.md). |
