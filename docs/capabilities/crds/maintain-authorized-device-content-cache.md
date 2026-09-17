# Maintain an authorized device-local content cache

## Identity
- **Name:** Maintain an authorized device-local content cache
- **Definition:** Store, reuse, refresh, and evict permitted local copies of accepted content or projections for faster and more resilient access from an owner device.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Improve repeated and connectivity-constrained access without turning a device cache into canonical Core state or expanding client authority.
- **Meaningful outcome:** A permitted non-canonical local copy is available, unavailable, refreshed, removed, or rejected with its owner/Core binding, logical source reference, and local state identifiable.
- **Boundaries — includes:** cache eligibility, local copy creation, stable source binding, reuse, inspection, refresh where supported, removal, owner/Core switching, and state reporting.
- **Boundaries — excludes:** selecting content for durable offline retention, preserving pending captures or edits, deleting canonical content, granting application access, storing owner-wide credentials, and implementing server-side retrieval or processing.
- **Terms and concepts:** A cached item is a local copy of accepted content or an authorized projection, such as a `schema.org/DigitalDocument` or other `schema.org/CreativeWork`; the logical Core object remains authoritative.

## Interaction Contract MLEs
### Maintain one cache entry
- **Actor:** An authorized device client or PIOS-native device-support component.
- **Command / intent:** Cache, reuse, refresh, validate, or evict one eligible Core object or projection.
- **Current state:** Owner/Core identity, client authority, logical source reference, connectivity, and existing local state can be determined.
- **Policies / invariants:** The copy remains non-canonical; each client retains distinct identity, grants, scopes, and audit attribution; ambiguous authority fails closed; writable disconnected behavior requires an explicit synchronization profile; removal affects only the local copy.
- **Transition:** Validate eligibility and identity, create, inspect, reuse, refresh, or remove the local copy according to the declared implementation profile.
- **Result:** An available, unavailable, refreshed, removed, or rejected cache entry with an explainable non-canonical state.
- **Events / effects:** May reduce repeated transfer, report stale/unavailable content, or trigger re-fetch or owner attention without changing canonical content.
- **Unknowns:** Universal cache size, freshness, encryption, eviction, integrity and telemetry profiles are not established.

## Rules and defaults
### Rules / invariants
- A device cache is not a Local Core, canonical source, authorization grant, backup, or pending-work store.
- Shared local storage does not merge the identities, grants, scopes, or audit attribution of its clients.
### Recommended defaults
- Prefer reuse only when the active implementation profile can establish that the local copy remains eligible; fail closed when identity or authority is ambiguous.

## Unknown / unresolved
- Platform-specific isolation, background refresh, revocation timing, and secure-removal guarantees require implementation profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Authorized device caching remains non-canonical, preserves per-client identity and authority boundaries, and requires explicit synchronization semantics before writable offline operation. | reasonable inference | proposed from committed architecture constraints | [Q01–Q05](../evidence/statement-provenance.md). |
