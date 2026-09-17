# Maintain selected content for offline access

## Identity
- **Name:** Maintain selected content for offline access
- **Definition:** Retain an owner-selected, authorized version of accepted content on a device for use during a declared offline window.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep specifically chosen information available during disconnected use without representing the retained copy as canonical Core state or fresh authorization evidence.
- **Meaningful outcome:** Owner-selected content is available, unavailable, removed, or blocked for offline use with its source identity, retained version, and non-canonical status visible.
- **Boundaries — includes:** owner selection, device and Core binding, content/reference scope, local retention, declared offline operations, deselection, removal, and reconnect handling under an explicit profile.
- **Boundaries — excludes:** opportunistic recent-content caching, unaccepted pending work, whole-Core replication, offline authorization of new actions, canonical mutation while disconnected, and guaranteeing remote erasure before a device reconnects.
- **Terms and concepts:** `selected offline content` is an authorized retained local copy of an accepted `schema.org/CreativeWork` or other Core object; it remains subordinate to its canonical source and declared offline policy.

## Interaction Contract MLEs
### Maintain offline availability
- **Actor:** The owner or an authorized device client acting under an explicit offline-retention policy.
- **Command / intent:** Select, synchronize, inspect, refresh, deselect, expire, or remove content for offline use.
- **Current state:** Content identity and version, owner/Core/device binding, client authority, declared offline profile, connectivity, and local state can be determined.
- **Policies / invariants:** The retained copy remains non-canonical; offline availability does not prove a current policy check; ambiguous authority fails closed; writable disconnected behavior requires explicit conflict, idempotency, correction, revocation, deletion, and cutover semantics; retention remains distinct from automatic caching and pending-work preservation.
- **Transition:** Validate or record selection, retain the permitted local version, and remove or reconcile it according to the declared profile.
- **Result:** Content is available offline under the declared profile, or has an explicit unavailable, removed, blocked, or rejected state.
- **Events / effects:** May update device-status evidence, request refresh on reconnection, or surface an owner-visible limitation or conflict.
- **Unknowns:** Universal offline windows, conflict resolution, revocation grace periods, storage quotas and secure-removal guarantees are not established.

## Rules and defaults
### Rules / invariants
- Offline availability must not be represented as current authorization, freshness, or canonical acceptance evidence.
- Selected offline content must remain distinguishable from cache entries and pending captures or edits.
### Recommended defaults
- Prefer to expose the retained source reference and version together with any profile-defined validation state.

## Unknown / unresolved
- Cross-device synchronization and regulated-data retention need deployment-specific profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Deliberate offline retention is a proposed capability distinct from ordinary caching and pending capture; its detailed freshness, revocation and reconciliation profile remains unresolved. | reasonable inference | proposed from committed architecture constraints | [Q01–Q05](../evidence/statement-provenance.md). |
