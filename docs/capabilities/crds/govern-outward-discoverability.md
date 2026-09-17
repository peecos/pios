# Govern outward discoverability

## Identity
- **Name:** Govern outward discoverability
- **Definition:** Control whether and how an outward representation may be found beyond a direct reference or explicit access grant.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let public reachability and active discovery be governed independently.
- **Meaningful outcome:** A representation has an explicit hidden, index-eligible, promoted, or equivalent discoverability state with provenance and current enforcement intent.
- **Boundaries — includes:** discoverability state, index eligibility, listing and sitemap intent, promotion state, inheritance and override, effective time, revision, withdrawal, and audit evidence.
- **Boundaries — excludes:** granting access, defining usage rights, publishing content, search-ranking implementation, analytics, and guaranteeing removal from third-party indexes.
- **Terms and concepts:** `discoverability` describes whether a representation may be found beyond its direct locator; it is not the same as being accessible.

## Interaction Contract MLEs
### Change discoverability state
- **Actor:** The owner or an explicitly authorized publication actor.
- **Command / intent:** Hide, permit indexing of, promote, or withdraw promotion for an outward representation.
- **Current state:** The representation, current visibility/access state, discoverability state, inheritance, sensitivity, and authority can be determined.
- **Policies / invariants:** Discoverability cannot expand access or rights; hidden does not imply inaccessible; promotion requires sufficient publication authority; changes and inherited defaults remain traceable; third-party propagation limits are disclosed.
- **Transition:** Validate the requested state against exposure policy, update discoverability metadata and connected mechanisms, and record the result.
- **Result:** A current discoverability state or a reasoned rejection with any propagation limitations.
- **Events / effects:** May update sitemaps, indexes, listings, machine-readable directives, or promotion queues.
- **Unknowns:** Universal propagation times and verification requirements across search engines and agent indexes are not established.

## Rules and defaults
### Rules / invariants
- Publicly reachable content may remain unlisted.
- Discovery changes must not silently change audience access or usage permission.
### Recommended defaults
- Keep newly public material hidden or unlisted until promotion is explicitly intended.

## Unknown / unresolved
- Evidence needed to claim successful de-indexing or promotion across external systems remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Discoverability is independently governed from visibility and access, allowing a public representation to remain unlisted. | rule/invariant | sourced | [G05–G06](../evidence/statement-provenance.md). |
