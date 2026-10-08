# PIOS First-Party Mobile App Handoff — October 2, 2026

Public documentation projection: owner-specific measurements, device names and
local filesystem locations are omitted. The unabridged implementation records
are retained privately. Dated checkpoints are historical evidence, not current
activation instructions; use the [current alignment notice](pios-mobile-contract-alignment-2026-10-08.md)
and the implementation's current authorized roadmap.

Status: retained October 2 app-side handoff to the single end-to-end agent;
current contract adjustments are in the
[October 8 alignment notice](pios-mobile-contract-alignment-2026-10-08.md).
Read that notice first. The checkpoint evidence below is preserved; its
exclusive-routing and sequencing statements do not override the current profile
or deployment roadmap.

## Purpose

Centralize the relevant work completed in the mobile-app workstream before
Core, Notes and server-side testing continue under one agent. This record
distinguishes confirmed production behavior, completed device-local work,
installed development behavior, and deferred work. It does not authorize a new
deployment, source connection, migration, release or deletion.

The controlling architecture remains
`pios-first-party-mobile-apps-by-prifina.md`. The current server-side Notes
truth is the PIOS Solo bidirectional Notes production workflow in
the implementation's private decision records.

## Current higher-level state

The earlier all-local App Group milestone has been superseded for Notes only.
As of October 2, 2026, Notes has completed one bounded bidirectional production
workflow through Core and PIOS Solo: app-originated Notes reach canonical Solo
state, browser-created and browser-edited Notes reconcile to the installed
Notes app, stale writes refuse overwrite, accepted mutations create Events,
replay is exact-once, and isolated export/restore passed.

Voice Notes and Core-owned phone data have not inherited that activation. They
remain device-local or Core-local until separately selected, reviewed and
verified end to end.

## Product and architecture decisions established

- The product set is the **PIOS First-Party Mobile Apps by Prifina**.
- Core is the PIOS-native device and owner interface. It is the only
  first-party mobile app that carries the PIOS connection.
- Notes and Voice Notes remain independently useful local-first apps. They may
  also provide app-owned iCloud or owner-configured endpoint options, but have
  no separate Prifina-operated application backend.
- The earlier Personal Apps Cloud design is superseded and must not be revived
  as the default route.
- Core uses `group.com.valto.storageinbox` for private state and
  `group.com.prifina.reactjs` for first-party App Group exchange.
- LifeStory Indie preserves the existing product, bundle identity and data.
  Its direct runtime Notes and Voice Notes feeds are disabled for new data.
- The future new LifeStory is a separate Core-dependent application and is the
  last application milestone. It consumes Core-provided records rather than
  directly collecting phone sources.
- Automatic processing begins at the selected activation boundary. Imported
  or historical content never enters automatic processing merely because it
  was imported or connected. Historical backfill remains explicit, bounded and
  potentially separately priced.

## Completed app-side work

### Notes and Voice Notes local exchange

- Notes insert, update, pin/rating revision and archive flows use the versioned
  App Group envelope and acknowledgement contract.
- Voice Notes uses one stable recording identity across recording, transcript,
  generated metadata, rename and archive revisions.
- Voice Notes sends transcript and recording metadata by default, with
  `audio_included=false`; original audio remains Voice Notes-owned.
- Core maintains a private integrity-bound current inventory for accepted
  Notes and Voice Notes transcript records.
- Imported and historical records remain excluded from automatic-current
  admission.
- Core's local Notes and Voice Notes inventory/projection milestone passed 170
  tests, unsigned iOS/macOS builds and independent review on September 30.
- Subsequent server work added Notes-only forwarding and reconciliation. The
  current Core implementations in `CoreboxV1ProductionClient.swift` and
  `PIOSFirstPartyMobileHandoff.swift` include newer work and must not be
  replaced with the earlier local-only versions.

### Core-owned iPhone sources

The following were implemented with forward-only activation boundaries,
private local storage, source-specific status and no automatic historical
backfill:

| Source | App-side state and verified boundary |
| --- | --- |
| Notifications | Local permission flow and APNs registration are available; the token is retained on device. Provider sending is a separate server concern. |
| Photos | Metadata-only inventory from the activation day forward; no image bytes copied. Source-to-evidence parity was checked; owner counts remain private. |
| Calendar | Selected-calendar events from the activation day through the advancing current-day horizon. Source-to-evidence parity and delayed change observation were checked; owner counts remain private. |
| Current Location | Explicit foreground capture only. Raw-to-normalized identity mapping was checked. |
| Background Movement | Significant-location-change monitoring with explicit Always access and durable monitoring state; no continuous GPS. Actual retained movement evidence later supported the stay/place proof. |
| Visits | Separate low-power Visits monitoring with raw arrival/departure preservation and no place naming. Retained-record checks are documented privately. |
| Contacts | Explicit current-state inventory of names, organization fields and communication-channel counts only. Accessible, retained and normalized record parity was checked; owner counts remain private. No phone numbers, email addresses, photos, notes or inferred relationships are copied. |
| Motion and Routes | Motion transitions plus deterministic route candidates from qualifying movement evidence. A callback actor-isolation crash was repaired and reverified on device. |
| Stay and Place candidates | Deterministic, rebuildable candidates from Visits and Background Movement. Source-linked candidate derivation was checked; movement measurements remain private. No reverse geocoding, home/work inference or glossary promotion. |
| Health | Read-only daily aggregates from an exact activation boundary. Integrity-bound local evidence was checked; individual health settings and measurements remain private. No raw samples or upload. |

The source-specific contracts are in the Core app repository under `docs/`.
The normalized device evidence is rebuildable adapter output, not canonical
PIOS truth. Only Notes has subsequently crossed the PIOS-connected boundary.

### Core-to-LifeStory local projection

Core has a versioned factual projection for Photos, Calendar, derived stays,
routes, Health, Notes and Voice Notes transcript records. It preserves source
provenance, sensitivity, confidence, exact timestamps, monotonic revisions,
withdrawal tombstones and explicit `doNotClaim` rules. It does not write
first-person narrative, create visible memories or publish runtime envelopes.
Publication remains disabled until the new Core-dependent LifeStory exists.

### Core iOS capture actions

The installed Core development build exposes both iOS extension placements:

- **Save to Core** in the top application row through a Share Extension; and
- **Save to Core** in the lower Edit Actions list through an Action Extension.

Both accept text, web URLs, images and files and stage them into Core's private
pending-capture area. The Action Extension has bundle identifier
`com.valto.storageinbox.action`, uses the Core-private App Group and was signed
with a profile containing `group.com.valto.storageinbox`.

The lower Action icon is a monochrome three-concentric-outline-circle version
of the Core mark. The main Core application icon and the top-row Share icon
remain unchanged. The signed build succeeded and was installed on the owner
iPhone on October 1. The owner confirmed the Action appeared before the custom
icon was installed; final visual confirmation of the replacement icon remains
useful but is not a functional blocker.

### Other app work retained as context

- Notes gained archive behavior and bounded/lazy home-list loading to avoid
  rendering the complete store by default.
- Notes settings/profile placement was established for reminders and imports;
  Apple Notes and Google Keep remain the intended reusable import formats.
- The one-time LifeStory-to-Notes transfer served migration continuity but is
  not a future LifeStory Notes feature.
- LifeStory Indie retained old mirrored data while new Notes and Voice Notes
  runtime feeds were removed.
- Core branding uses the owner-facing name **Core**, a light teal visual system
  and the three-circle mark.

## Current repository and evidence state

At this checkpoint the Core app working tree contained a large set
of intentional uncommitted changes. Do not reset, clean, regenerate over, or
split them blindly. They include the complete mobile collectors, App Group
contracts, LifeStory projection, tests, visual identity, Share/Action
extensions and newer Notes production synchronization work.

In particular, `Shared/CoreboxV1ProductionClient.swift` and
`Shared/PIOSFirstPartyMobileHandoff.swift` were modified after the local-only
milestone for the production Notes workflow. Current behavior includes the
forwarding boundary, delivery receipts, Core-to-Notes command publication,
application acknowledgements and retained terminal-server resolution. Those
files are owned by the newer end-to-end work and must be reconciled as current,
not reverted to the earlier local implementation.

Primary app-side evidence remains in the implementation's private evidence
store. Personal payloads, per-owner measurements and local filesystem paths
are not part of this public documentation projection.

## Remaining work transferred to the main agent

Immediate work should be selected from the current Stage 8 roadmap and tested
end to end across app, Core device interface, Solo capability and browser. The
following items remain separate rather than implied by Notes completion:

1. preserve and commit/reconcile the current app working trees without losing
   the mixed local and newer Notes changes;
2. choose the next bounded first-party source or Import before activating it;
3. assess and document the local/cloud synchronization operating model,
   including triggers, cadence, background behavior, freshness, batching,
   retry/backoff, conflicts, offline operation, resource limits, controls,
   observability and recovery;
4. implement a sanitized, allowlisted LifeStory Indie migration export before
   any LifeStory snapshot or historical migration;
5. prepare historical migration fixtures and require a separate owner decision
   for real historical data;
6. prepare compatible releases for Core, Notes, Voice Notes and LifeStory
   Indie; and
7. create and release the new Core-dependent LifeStory last.

Voice Notes PIOS connectivity, phone-source forwarding, browser attachment
editing, reminder parity, permanent deletion, broader devices and historical
backfill remain unactivated unless separately selected.

## Agent ownership boundary

After this handoff, the main agent working across Core, Notes, browser and Solo
owns further implementation, testing and fixes. Other agents should limit
themselves to read-only analysis or explicitly assigned non-overlapping work.
This is an execution-coordination rule, not a change to PIOS authority or app
architecture.
