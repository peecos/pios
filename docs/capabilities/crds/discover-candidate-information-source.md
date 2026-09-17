# Discover a candidate information source

## Identity
- **Name:** Discover a candidate information source
- **Definition:** Inspect a submitted subject or location for potential information sources and preserve reviewable candidates without collecting their content.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Help the owner identify possible feeds, APIs, sitemaps, release channels, services, archives, or other origins before deciding whether any source should be registered or accessed.
- **Meaningful outcome:** A discovery attempt produces zero or more candidate records with submitted subject, candidate type/location, confidence, update expectation, security/authentication state, terms or robots notes, likely cost, actor, method, and time.
- **Boundaries — includes:** submitted domain/page/organization/service, candidate probing within allowed discovery scope, candidate type, location/reference, confidence, expected update frequency, authentication need, security state, public-policy notes, likely cost, duplicate handling, and discovery provenance.
- **Boundaries — excludes:** collecting source content, registering a connector, authenticating to the source, authorizing backfill or ongoing collection, importing data, accepting terms, and treating a candidate as endorsed or trusted.
- **Terms and concepts:** A candidate may identify a `schema.org/DataFeed`, `schema.org/WebAPI`, `schema.org/Dataset`, website, archive, service, or other origin. Candidate identity remains provisional until governed review and registration.

## Interaction Contract MLEs
### Discover source candidates
- **Actor:** The owner or an authorized source-discovery process.
- **Command / intent:** Inspect a declared subject or location for potential information sources without collecting their substantive content.
- **Current state:** The submitted subject/location, allowed inspection scope, actor identity, network and policy boundary, and existing candidate/source records can be determined.
- **Policies / invariants:** Discovery never grants collection authority; authentication is not attempted without separate authority; terms, robots and security observations remain notes rather than legal conclusions; confidence and method are visible; duplicates link to prior candidates; no candidate becomes registered automatically.
- **Transition:** Perform the permitted inspection, normalize and deduplicate candidate findings, and persist the discovery result and evidence.
- **Result:** A set of reviewable source candidates, no candidates found, or a reasoned blocked/failed discovery result.
- **Events / effects:** May initiate a structured candidate review, permission review, source registration proposal, cost estimate, or owner-attention item through separate capabilities.
- **Unknowns:** Universal inspection depth, robots/terms interpretation, active probing, rate limits and candidate expiry are not established.

## Rules and defaults
### Rules / invariants
- Source discovery must not collect source content or silently register, backfill, or begin incremental collection.
- Candidate confidence and security/access observations must remain distinguishable from owner confirmation and source trust.
### Recommended defaults
- Prefer passive public metadata inspection and record why deeper inspection was not attempted.

## Unknown / unresolved
- Source-class-specific discovery methods and legal/policy review requirements need profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Source discovery produces candidate-only records before review, registration, backfill, or incremental collection authority. | rule/invariant | sourced | [S01–S05](../evidence/statement-provenance.md). |
