# Maintain selected content for offline access

## Identity
- **Name:** Maintain selected content for offline access
- **Definition:** Retain an owner-selected, authorized version of accepted content on a device for use during a declared offline window.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep specifically chosen information usable without connectivity while preserving authority, freshness, revocation, and reconciliation limits.
- **Meaningful outcome:** Selected content is available, stale, expired, revoked, removed, or unavailable offline with its source identity, retained revision, authorization window, and last validation visible.
- **Boundaries — includes:** owner selection, device and Core binding, content/reference scope, local retention, allowed offline operations, freshness and expiry, deselection, revocation response, reconnection validation, conflict detection, and safe removal.
- **Boundaries — excludes:** opportunistic recent-content caching, unaccepted pending work, whole-Core replication, offline authorization of new actions, canonical mutation while disconnected, and guaranteeing remote erasure before a device reconnects.
- **Terms and concepts:** `selected offline content` is an authorized retained local copy of an accepted `schema.org/CreativeWork` or other Core object; it remains subordinate to its canonical source and declared offline policy.

## Interaction Contract MLEs
### Maintain offline availability
- **Actor:** The owner or an authorized device client acting under an explicit offline-retention policy.
- **Command / intent:** Select, synchronize, inspect, refresh, deselect, expire, or remove content for offline use.
- **Current state:** Content identity and version, owner/Core/device binding, client authority, offline-retention policy, allowed operations, connectivity, last validation, and local state can be determined.
- **Policies / invariants:** Only previously authorized accepted content is usable offline; offline availability does not imply freshness or a current policy check; absent, expired, revoked, or ambiguous authority fails closed; reconnection revalidates authority and reconciles versions without silent canonical overwrite; retention differs from ordinary cache eviction and pending-work preservation.
- **Transition:** Validate or record selection, maintain the permitted local version during the offline window, and reconcile, expire, or remove it according to policy.
- **Result:** Content is available offline under a declared scope, or has an explicit stale, expired, revoked, removed, unavailable, or rejected state.
- **Events / effects:** May update device-status evidence, request refresh on reconnection, or surface an owner-visible limitation or conflict.
- **Unknowns:** Universal offline windows, conflict resolution, revocation grace periods, storage quotas and secure-removal guarantees are not established.

## Rules and defaults
### Rules / invariants
- Offline availability must never be represented as proof of current server authorization, freshness, or successful canonical acceptance.
- Selected offline content must remain distinguishable from cache entries and pending captures or edits.
### Recommended defaults
- Show the retained revision and last successful validation whenever an offline copy may be stale.

## Unknown / unresolved
- Cross-device synchronization and regulated-data retention need deployment-specific profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Deliberate offline retention has its own selection, authorization-window, freshness, revocation and reconciliation lifecycle distinct from ordinary caching. | rule/invariant | sourced | [Q01–Q05](../evidence/statement-provenance.md). |
