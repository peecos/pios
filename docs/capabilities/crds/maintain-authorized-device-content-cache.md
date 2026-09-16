# Maintain an authorized device-local content cache

## Identity
- **Name:** Maintain an authorized device-local content cache
- **Definition:** Store, reuse, refresh, and evict permitted local copies of accepted content or projections for faster and more resilient access from an owner device.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Improve repeated and connectivity-constrained access without turning a device cache into canonical Core state or expanding client authority.
- **Meaningful outcome:** A cache entry is available, refreshed, stale, unavailable, evicted, or rejected with owner/Core identity, logical source reference, revision or integrity evidence, freshness, and permitted access boundary.
- **Boundaries — includes:** cache eligibility, local copy creation, stable source binding, revision/integrity tracking, freshness, reuse, refresh, ordinary eviction, owner/Core switching, revocation response, and state reporting.
- **Boundaries — excludes:** selecting content for durable offline retention, preserving pending captures or edits, deleting canonical content, granting application access, storing owner-wide credentials, and implementing server-side retrieval or processing.
- **Terms and concepts:** A cached item is a local copy of accepted content or an authorized projection, such as a `schema.org/DigitalDocument` or other `schema.org/CreativeWork`; the logical Core object remains authoritative.

## Interaction Contract MLEs
### Maintain one cache entry
- **Actor:** An authorized device client or PIOS-native device-support component.
- **Command / intent:** Cache, reuse, refresh, validate, or evict one eligible Core object or projection.
- **Current state:** Owner/Core identity, client authority, logical reference, expected revision or integrity value, freshness policy, connectivity, and existing local state can be determined.
- **Policies / invariants:** Only content authorized for every reader of the selected storage boundary may be cached there; cached, stale, pending, accepted and unavailable states remain distinguishable; cache reuse respects freshness; a Core/account switch cannot expose or submit another owner's data; eviction affects only the local copy; cache presence does not prove current server policy or Core health.
- **Transition:** Validate eligibility and identity, fetch or reuse the permitted version, update freshness and integrity evidence, or safely remove the local copy.
- **Result:** A usable, refreshed, stale, unavailable, evicted, or rejected cache entry with an explainable state.
- **Events / effects:** May reduce repeated transfer, report stale/unavailable content, or trigger re-fetch or owner attention without changing canonical content.
- **Unknowns:** Universal cache size, freshness, encryption, eviction, integrity and telemetry profiles are not established.

## Rules and defaults
### Rules / invariants
- A device cache is not a Local Core, canonical source, authorization grant, backup, or pending-work store.
- Shared plaintext storage must contain only data authorized for every member able to read it.
### Recommended defaults
- Reuse a verified fresh copy before downloading the same revision again, and fail closed when identity or authority is ambiguous.

## Unknown / unresolved
- Platform-specific isolation, background refresh, revocation timing, and secure-removal guarantees require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Authorized device caching preserves source identity, integrity, freshness and access boundaries while remaining non-canonical and safely evictable. | rule/invariant | sourced | [Q01–Q05](../evidence/statement-provenance.md). |
