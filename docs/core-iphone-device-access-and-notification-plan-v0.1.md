# Core iPhone Device Access and Notification Plan v0.1

Public documentation projection: owner-specific measurements, device names and
local filesystem locations are omitted. The unabridged implementation records
are retained privately. Dated checkpoints are historical evidence, not current
activation instructions; use the [current alignment notice](pios-mobile-contract-alignment-2026-10-08.md)
and the implementation's current authorized roadmap.

Status: owner-selected client-side implementation plan; server activation deferred

Date: September 28, 2026

## Objective

Prepare Core to own the iPhone permissions and local source collection required
by the future Core-dependent LifeStory. Complete the device-side notification
foundation at the same time. PIOS server forwarding, APNs provider sending and
device-token upload are a final, separately activated integration step.

Core does not request a sensitive device-source permission until the matching
local collector is implemented and can provide immediate owner-visible value.
Each source remains visible, separately owner-triggered and activated
forward-only. Historical collection remains a separate manual operation.

## LifeStory Indie Source Inventory

| Source or capability | Current LifeStory Indie use | Target Core responsibility | Initial activation boundary |
| --- | --- | --- | --- |
| Photos / PhotoKit | Recent photo identity, timestamps, subtype/source hints, location, compact metadata and optional visual observations | Own photo-library permission and preserve stable PhotoKit identifiers plus provenance; do not duplicate originals by default | Start of activation day forward |
| Calendar / EventKit | Selected-calendar events and event metadata | Own full event-read permission, selected-calendar configuration and stable event identity | Start of activation day through the current day; the upper boundary advances with time |
| Current Location | Current location and reverse-geocoded place context | Own when-in-use permission first; collect only during explicit foreground checks | From explicit activation onward |
| Background movement | Approximate movement context outside active app use | Own a separately explained Always-location activation using the battery-efficient significant-change service; do not imply continuous GPS | From explicit monitoring activation onward |
| Visits | Low-power visit monitoring | Own separately explained Always-location escalation and visit provenance | From explicit monitoring activation onward |
| Route history | Significant location changes and movement-gated route points | Own separately explained background location and route collection | From explicit monitoring activation onward |
| Motion / Core Motion | Walking, running, cycling, automotive and stationary evidence for route confidence | Own motion permission and bounded activity queries; never infer unsupported activity | From explicit activation onward |
| HealthKit | Steps, walking/running distance, workouts, sleep, heart rate, resting heart rate, HRV and State of Mind count | Own read-only HealthKit authorization and source-specific provenance; no medical conclusions | From explicit activation onward; bounded query windows only |
| Contacts | Owner-selected profile/contact links and local person-resolution candidates | Own contacts permission only for owner-selected identity/glossary linking; contacts do not become memories | On explicit Connect Contacts action |
| Journaling Suggestions | Owner-selected Apple suggestion bundles | Support only through an owner-presented system picker; never background-harvest | Per owner selection |
| Weather | WeatherKit/FMI context near an authorized coordinate | Treat as derived external context, not device data; activate after location provenance exists | Current/future request only |
| Camera, microphone and speech | Owner-triggered photo and voice-memory creation | Keep as explicit capture capabilities in the relevant app experience; do not classify as automatic Core device collection | Per owner action |
| Notifications | Daily reminders and processing-completion alerts | Core owns local notification permission/status and later APNs client registration | Per owner action |

## Device-Side Sequence

The LifeStory reference assessment and the local-versus-PIOS processing split
are defined in
[LifeStory Reference Assessment For Core Mobile](lifestory-reference-assessment-for-core-mobile-2026-09-29.md).

1. **Permission center** — show truthful status for Photos, Calendar, Contacts,
   Location, Motion, Health and Notifications. A source permission appears only
   with its working local collector; requests never cascade automatically.
2. **Local notification readiness** — request alert/sound/badge permission and
   prove one owner-triggered local test notification.
3. **APNs client readiness** — add the push entitlement, register only after an
   owner action and visible-notification authorization, retain the token locally
   with its development/production environment, clear stale state on failure,
   and expose registration/error state. No token leaves the phone in this stage.
4. **Source collectors** — implement one source at a time, beginning with
   Photos, then Calendar, Current Location, Background Movement, Visits,
   Motion/Routes, Health and Contacts.
   Collectors emit typed source-neutral evidence envelopes; they do not create
   LifeStory-specific memories.
5. **Parity checks** — compare Core's bounded local results with LifeStory Indie
   while leaving LifeStory Indie unchanged as the continuity application.
6. **Local projection contract** — expose only authorized source records or
   projections to the future LifeStory through a versioned device-local
   contract.
7. **Final server activation** — only after the client-side sources and
   notifications pass local validation, separately authorize device-token
   upload, APNs provider sending, PIOS ingestion, retry and remote status.

## Notification Boundaries

- Local notifications require no Prifina or PIOS server.
- Registering with Apple Push Notification service is device-side readiness;
  it does not authorize uploading the device token or sending a notification.
- The APNs token is installation-specific and may rotate. Core stores it only
  as local operational state until the final server activation milestone.
- Remote notification payloads must not carry sensitive personal context.
  They should indicate that Core has something to review and let the app fetch
  authorized details after opening.
- Push delivery is opportunistic and cannot be the sole reliability mechanism.
  Local durable queues and foreground reconciliation remain authoritative.
- The `remote-notification` background mode remains disabled until a governed
  payload contract and background receiver exist.

## Data And Reliability Rules

- Forward-only automatic collection is the default.
- Forward-only does not preload future calendar years. Calendar collection
  begins on the activation day and advances through each current day as time
  passes; future schedule import is a separate capability if later needed.
- Calendar reconciliation refreshes and queries Core's retained EventKit store
  before creating a fresh-store snapshot. This is required for newly
  synchronized Google Calendar additions and removals to become visible
  reliably; a short source-sync delay is expected.
- Historical backfill is manual, separately scoped and potentially paid.
- Permission status, activation time, source identity, timestamps and
  provenance are retained locally.
- Denied, restricted, limited, unavailable and not-requested states remain
  distinct where iOS exposes them.
- Core must remain truthful when iOS does not disclose read authorization, as
  with some HealthKit access.
- Device-source records are not canonical PIOS records until a later governed
  ingestion succeeds.
- Device-only processing is limited to Apple-framework access, local privacy
  protection, source normalization, obvious-noise filtering and immediate
  owner-visible value. Cross-source correlation, canonical glossary state,
  History, Insights and model-assisted understanding belong to PIOS after
  explicit connection.
- No source collector may silently activate a different permission class.
- Permissions are not requested merely to prove future readiness; implementation
  and permission activation ship as one source-specific milestone.
- LifeStory Indie remains unchanged until each Core source reaches parity.

## Current Exit Condition

The common app-side foundation is ready when Core can display source readiness,
prove a local notification, register with APNs while keeping an
environment-bound token on-device, and keep all server forwarding disabled.
Each actual source then adds its permission, local collection and parity exit
condition together, beginning with Photos.

## Implementation Status — September 30, 2026

This retained checkpoint recorded completed local notification/APNs readiness,
source-specific collectors and structural parity against LifeStory Indie.
Tokens remained on device and server forwarding stayed separately gated.
Callback-isolation and source-query-window defects were corrected and tested.
The local projection contract preserved factual evidence, sensitivity,
provenance and explicit limits on unsupported claims.

Detailed owner-device observations, health/location/contact measurements,
installation identifiers and evidence locations are retained privately. This
public summary neither replaces those records nor authorizes current source
activation. Subsequent Notes behavior follows the current profile; other phone
sources do not inherit its server authority.
