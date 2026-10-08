# PIOS First-Party Mobile Apps by Prifina

Public documentation projection: owner-specific measurements, device names and
local filesystem locations are omitted. The unabridged implementation records
are retained privately. Dated checkpoints are historical evidence, not current
activation instructions; use the [current alignment notice](pios-mobile-contract-alignment-2026-10-08.md)
and the implementation's current authorized roadmap.

Canonical scope: deployment-neutral PIOS first-party mobile application architecture.

Status: owner-selected deployment-neutral architecture; the first bounded
bidirectional Notes-to-PIOS workflow is operational. Voice Notes, Browser,
Voice Agent, device-source forwarding, historical migration and the new
LifeStory remain separately planned or deferred.

Date: October 2, 2026

## Integration Progress Vocabulary

Use these states precisely; completion at one layer does not imply completion
at the next:

1. **Device-local ready** — the application can collect or maintain the data on
   the device.
2. **Core-local handoff ready** — a stable, acknowledged App Group exchange
   exists, but Core has not necessarily delivered the record to PIOS.
3. **PIOS-connected** — governed PIOS intake, identity, provenance, Events and
   recovery have passed.
4. **Browser-visible** — the accepted records can be retrieved through the
   authenticated Core browser with truthful freshness and authority status.
5. **Browser-authorable** — the browser can create or edit the record through a
   governed revision and conflict contract.

Deployment-specific source status and sequencing belong in the deployment's
own roadmap. This profile does not promote a device-local collector or
Core-local App Group acknowledgement into proof of server connection, browser
visibility or browser authoring.

For independently useful writable applications such as Notes, local-first does
not authorize two ambiguous canonical writers. The application remains the
local source and working copy for app-originated pending work; the owner's Core
preserves cross-device information continuity after governed acceptance. Core
must never edit an application's private database directly. Any canonical edit
returning to the application uses an explicit immutable reconciliation command,
expected revision, idempotency identity and application acknowledgement. The
application applies it through its own persistence and versioning behavior or
reports a conflict. Canonical acceptance, local delivery and application are
separate states.

## Purpose

Define the iPhone architecture for the **PIOS First-Party Mobile Apps by
Prifina** before implementation begins. The applications are built and published by
Prifina and may connect through Core to any compatible owner-selected PIOS
implementation. The profile uses the shared Apple development team and App
Group to give these apps one governed device-side route to PIOS without
imposing that route on third-party applications.

This application-set definition is deployment-neutral. It does not depend on whether the
connected PIOS implementation is single-owner, hosted, multitenant, self-hosted
or supplied through another compatible deployment profile.

The profile covers:

- Core app;
- Notes by Prifina;
- Voice Notes by Prifina;
- Browser by Prifina;
- Voice Agent by Prifina;
- the existing LifeStory application, renamed **LifeStory Indie**; and
- a new **LifeStory** application forked from the existing product and rebuilt
  as a Core-dependent companion.

This is a first-party application profile under the open PIOS direct, brokered and
hybrid integration model. It does not change the integration choices available
to third-party applications.

## Selected Product Roles

Current contract clarification: read the
[October 8 alignment notice](pios-mobile-contract-alignment-2026-10-08.md).
Core-local means local to the Core app, not a Local Core deployment. The shared
state and bidirectional evidence rules are in Integration sections 19.7–19.8.

| Application | Product role | Works without Core | PIOS route | Other synchronization |
| --- | --- | --- | --- | --- |
| Core app | PIOS-native owner interface and device integration hub | No; its purpose is to operate PIOS | Direct governed connection to the owner's PIOS Core | Core-controlled cache, pending work and selected offline content |
| Notes by Prifina | Independent local-first notes product | Yes | Core-mediated handoff plus the selected bounded direct reconciliation path; activation evidence is deployment-specific | Optional app-owned iCloud or owner-configured custom endpoint; no Prifina app backend |
| Voice Notes by Prifina | Independent local-first recording and transcript product | Yes | Local Core-mediated handoff only | Optional app-owned iCloud or owner-configured custom endpoint; original-audio synchronization remains separately explicit; no Prifina app backend |
| Browser by Prifina | Independent local-first browser, Reader and reading-intention product | Yes | Planned owner-enabled continuity for normal history, bookmarks, Roles, Modes and selected reading state, plus explicit retention and PIOS-assisted browsing; Incognito is excluded | Browser-owned website sessions, credentials, cookies and ordinary WebKit networking |
| Voice Agent by Prifina | Independent owner voice interface to Ally and authorized agent capabilities | Yes, when its separately operated agent backend is available | Planned Core-mediated access to selected device context plus a separately scoped governed backend PIOS query/submission contract | Conversational backend and reusable tools currently remain external to PIOS; their Agent-VM migration is separate |
| LifeStory Indie | Continuing independent version of the existing LifeStory product | Yes | No new required PIOS dependency; it may export an owner-triggered migration package to Core | Preserve existing local behavior and any separately supported independent synchronization |
| LifeStory | New Core-dependent personal-memory and story companion | No | Local exchange with Core; Core owns this companion's PIOS connection | No separate LifeStory backend; Core supplies authorized source data and PIOS continuity |

“Indie” is the owner-facing short name for the independent LifeStory line. The
existing App Store record, bundle identifier, installed application and local
data remain with LifeStory Indie. The new LifeStory uses a new bundle
identifier and App Store Connect record.

## Target iPhone Architecture

```text
Apple device sources and permissions
                |
                v
         Core iPhone app <-----------------> PIOS Core
                |
       reviewed first-party local contracts
       /       /          |          \          \
      v       v           v           v          v
   Notes  Voice Notes   Browser   Voice Agent  LifeStory

Separate optional non-PIOS paths:
Notes       <-> iCloud or owner-configured custom endpoint
Voice Notes <-> iCloud or owner-configured custom endpoint

Existing product:
LifeStory Indie -> optional owner-triggered migration package -> Core
```

Core remains the device-side PIOS integration and governance hub. The diagram
shows the brokered path, not an exclusive routing requirement. Notes may also
hold its own least-privilege reconciliation identity for fetching applicable
canonical Note commands and returning acknowledgements. Core's existing
broker/background path remains available; both paths preserve the same object,
revision, command, conflict and acknowledgement semantics. This exception does
not grant Notes general capture, device-source collection or owner-wide access.
Actual activation and granted scopes are established by deployment evidence.

Voice Notes, Browser, Voice Agent mobile and the new LifeStory retain the
selected Core-mediated PIOS path unless their own profile is explicitly revised.
An independent Voice Agent backend may receive its own scoped PIOS integration
identity because it is an external consumer, not a substitute for Core. No
application receives unrestricted owner credentials through shared storage.

### Browser and Voice Agent planning addition — October 2, 2026

Browser and Voice Agent are selected additions to the first-party application
family. Their exact local transport remains subject to a trust-boundary review.
The existing App Group is not automatically extended merely because both apps
are first-party: Browser content and voice/conversation material broaden the
plaintext trust domain substantially. Pairwise Core App Groups, enforced
per-app isolation, or the existing Core-owned Share/Action route must be
compared before entitlements change.

Browser remains independent, but its owner-enabled normal-data flow is an
intentional product purpose: normal history, bookmarks, Roles, Modes and other
selected useful records should synchronize through Core, while Incognito,
website traffic, credentials and cookies remain excluded. Explicit durable
page/content retention remains a separate action. PIOS may return selected
context and capabilities through Core to improve browsing.

Voice Agent's mobile app should consume authorized Core-owned device records or
projections instead of duplicating each device permission and collector. Its
independent conversational backend, tools and public-data connectors remain
outside PIOS; its migration from the existing agent Mac to the selected Agent VM is
governed separately. That backend should query governed PIOS context, including
selected Myself, My World and My System information, and submit selected
session records and logs through scoped contracts. PIOS Solo owns the governed
context, submission, canonical Event, recovery and owner-visible integration
boundaries.

The Valto deployment's detailed current-state assessment is
the implementation's private Voice Agent and Codex Voice assessment.
It confirms that microphone and live audio remain intrinsic Voice Agent
responsibilities, while reusable device context such as location should
normally be supplied through a pairwise Core-mediated boundary. It also records
the current external backend and retained data as transitional implementation
state rather than a deployment-neutral requirement of this profile.

Core mediation is selective. Voice Agent keeps microphone/live-audio and other
immediate conversational capabilities where direct access is integral to the
experience, while reusable or longitudinal context can come from Core with
declared freshness and source. The Valto profile also distinguishes two backend
writes: ordinary Voice Agent Markdown documents enter governed PIOS intake and
Files with Voice Agent attribution, while an explicit Notes request uses the
canonical Notes capability and reconciles the resulting Note into Notes by
Prifina. These are separate tools and authority scopes.

The Notes interface is a reusable governed PIOS capability rather than a
Voice-Agent-specific endpoint. Other first-party or approved applications and
agents may use it through distinct integration identities and least-privilege
read/create/update/archive scopes. Universal Inbox remains the default for
general or ambiguous content; Organizer may suggest a Note destination but
must not silently create a canonical Note based only on content signals.

For the Valto deployment, the first Notes production proof did not establish
complete library parity. The current implementation plan is
the implementation's private Core mobile synchronization assessment.
It keeps each application local-first while Core provides durable queues,
incremental reconciliation, selected offline content, disposable recent cache
and opportunistic background synchronization. App-local save success and PIOS
acceptance remain distinct states.

The initial Notes device-materialization policy keeps complete selected-library
metadata, all pinned Note bodies and the 50 most recently created or edited
unpinned Note bodies. Older Note bodies and attachments load progressively from
PIOS as needed. Pending edits, conflicts, unverified canonical revisions,
incomplete attachments and explicit offline selections are never ordinary
cache. This policy applies only after canonical parity, exact retrieval and
recovery are proven for the selected Notes scope.

The design must not depend on the foreground Core app process being alive.
Participating apps use durable local handoff queues, App Group storage,
extensions and iOS-managed background opportunities. Core processes queued
work when the operating system permits, records validated/retryable/rejected
state, and exposes the result back to the originating app.

Core also maintains a private revisioned semantic inventory for accepted
automatic-current Notes and Voice Notes transcript records. It is written only
after envelope and payload validation and does not copy Notes attachment bytes
or Voice Notes audio. The device-local inventory does not itself activate a
server connection. Notes now has a separately governed PIOS forwarding and
reconciliation path; Voice Notes remains Core-local. Historical content remains
a separately owner-triggered backfill path.

## Device-Data Responsibility

The new LifeStory does not directly read the device sources currently used by
the existing LifeStory product. Relevant permissions and collection move to
Core in separately reviewed, source-specific increments. These may include
photos, calendar, location, motion and owner-authorized HealthKit evidence.

Core preserves source identity, permission state, timestamps, integrity and
raw/processed provenance. It supplies only the authorized data or projection
needed by LifeStory. LifeStory performs its memory-review and story experience
over that supplied material and returns owner edits, decisions and generated
outputs through the same Core-mediated boundary.

Voice Notes is transcript-first for PIOS continuity. Its default Core handoff
contains transcript and recording metadata without the audio bytes. Original
audio remains in Voice Notes unless the owner separately selects it for
retention or migration. PIOS preserves the verbatim transcript and may create a
cleaned Derived representation; glossary-supported name or term corrections
retain an attributable correction map and ambiguous changes remain proposals.

Moving a source into Core does not authorize broad historical collection.
Each source begins from the separately selected activation boundary. Historical
backfill or migration remains an explicit owner-triggered operation with its
own cost, scope and progress reporting.

## Shared App Group Boundary

### Selected two-group model

The first-party mobile apps use two distinct App Groups:

| App Group | Role | Members |
| --- | --- | --- |
| `group.com.valto.storageinbox` | Core-private storage and the Core share-extension boundary | Core and Core Share only |
| `group.com.prifina.reactjs` | Current PIOS first-party mobile App Group exchange | Core, Notes and Voice Notes; LifeStory Indie remains a temporary legacy member without runtime companion-feed reads. Browser and Voice Agent are planned Core-connected family members, but their same-group admission is not yet selected. |

Core must not place its private inbox, credentials, device identity, cache or
share-extension state in the shared exchange App Group. Notes and Voice Notes use
the exchange App Group only for versioned handoff envelopes and acknowledgements.
LifeStory Indie membership is retained temporarily for continuity but does not
authorize runtime ingestion; removal requires a later compatibility and
provisioning review.

This profile applies only to the PIOS First-Party Mobile Apps by Prifina,
signed by the same Apple development team and deliberately
admitted to the App Group. Third-party applications cannot use this mechanism
and continue to integrate through declared PIOS direct, brokered or hybrid
interfaces.

App Group membership is a shared trust boundary, not a permission grant. The
profile must define:

- a distinct integration identity and audit attribution for every app;
- per-app inbound and outbound directories, envelopes or mediated operations;
- the exact data classes every participating member may read;
- stable item identity, revision, provenance and originating application;
- idempotent delivery, acknowledgement, retry and conflict behavior;
- owner/Core binding and safe behavior when Core changes or is disconnected;
- expiry, revocation, deletion and cache-eviction behavior; and
- separation of disposable cache, selected offline content and pending work.

No owner-wide PIOS credential belongs in shared storage. Plaintext placed in a
shared container must be suitable for every application capable of reading
that container; otherwise use isolation or an enforced mediated interface.

## Independent Synchronization Boundary

Notes and Voice Notes may offer iCloud synchronization or an owner-configured
custom endpoint. Those are application-owned synchronization choices and do
not become PIOS interfaces, canonical Core state or a Prifina-operated shared
backend.

Prifina Personal Apps Cloud is therefore not part of the target architecture.
Its synthetic implementation and evidence remain historical development
material, but production adapters, app-content storage and activation are no
longer planned under this product direction.

## LifeStory Split And Migration

### LifeStory Indie

1. Preserve the current source history, bundle identifier, App Store Connect
   record, installed-app continuity and local data.
2. Release an update that changes the owner-facing name to **LifeStory Indie**.
3. Keep its existing direct device-source behavior and independent operation.
4. Add an explicit, versioned, owner-triggered export for migration through
   Core. Do not expose its private database as the migration contract.
5. Keep export copy-first and non-destructive. Nothing is removed until the
   owner separately confirms a verified migration and any cleanup.

### New LifeStory

1. Fork the existing LifeStory source while preserving source attribution and
   useful implementation history.
2. Create a new application identity, bundle identifier and App Store Connect
   record.
3. Remove direct ownership of device-source permissions and ingestion as each
   equivalent Core source path becomes available.
4. Require a compatible, configured Core app during onboarding and show a
   truthful unavailable state when Core is absent, disconnected or lacks a
   required permission.
5. Consume only versioned Core-provided source records or projections and
   return edits and generated outputs through durable local contracts.
6. Import historical LifeStory Indie data only through the reviewed migration
   package and Core reconciliation path.

The two applications may coexist indefinitely. Installing the new LifeStory
does not replace, mutate or delete LifeStory Indie or its data.

## Delivery Sequence

This sequence is non-normative to the reusable PIOS capabilities but controls
the current product implementation plan.

1. **Document and inventory** — align PIOS and application documentation;
   inventory current bundle IDs, App Groups, schemas, stores, device-source
   permissions and TestFlight/App Store identities.
2. **Define the local contract** — version the App Group envelope, app
   identities, queue states, acknowledgements, provenance and denial behavior;
   prove it with harmless fixtures.
3. **Prepare Core** — add the first-party app registry, per-app local queues,
   local acceptance/status behavior and a disabled outbound boundary. No PIOS
   server connection, credential or forwarding path is in scope until the owner
   explicitly activates a later milestone.
4. **Move Notes and Voice Notes feeds** — preserve standalone local operation,
   replace direct LifeStory feeds with Core-mediated handoff, and verify
   insert/update/archive behavior. Keep iCloud/custom endpoint work separate.
5. **Prepare LifeStory Indie** — rename the existing product and implement the
   non-destructive migration export.
6. **Activate the local App Group runtime** — select the final App Group, add
   truthful Core status UI, and verify Notes and Voice Notes
   insert/update/archive handoff end to end without server connectivity.
7. **Prepare Core-owned device sources and notifications incrementally** — use
   the [Core iPhone device-access and notification plan](core-iphone-device-access-and-notification-plan-v0.1.md). First expose separately owner-triggered permission and notification status, then implement one source class at a time, compare local results with LifeStory Indie, and keep LifeStory Indie unchanged as the continuity application. APNs provider sending, token upload and PIOS server forwarding are the final separately activated substep. The future new LifeStory will consume Core-provided records rather than collecting device sources itself.
7A. **Assess the local and cloud synchronization operating model** — before
   expanding or activating synchronization, assess the behavior currently
   implemented across the first-party applications, App Group exchange,
   application-owned iCloud/custom endpoints and the future Core-to-PIOS
   boundary. Document clear principles for what initiates synchronization,
   foreground and background cadence, freshness expectations, batching,
   retry/backoff, conflict handling, offline behavior, power and network
   constraints, owner controls, status visibility and recovery. This is a
   deferred assessment and documentation task only; it does not authorize a
   cloud connection or a synchronization behavior change.
8. **Prepare and optionally run historical migration** — first prove LifeStory
   Indie package intake, identity reconciliation, counts, hashes, revisions and
   rollback with fixtures. Core browser design may first use a bounded,
   owner-selected representative subset of LifeStory History, glossary,
   recognized-person candidates, Notes and Voice Notes transcripts as an
   explicit display-assessment Import. Run a complete owner export only through
   a separate explicit migration decision, before any cleanup is considered.
9. **Release the existing first-party mobile applications** — ship compatible Core, Notes,
   Voice Notes and LifeStory Indie updates separately; do not force migration
   or make standalone applications depend on Core.
10. **Create new LifeStory last** — only after the preceding Core and
   existing-app foundations pass, fork into a new application identity, require
   Core, operate exclusively on Core-provided data, verify isolation from
   LifeStory Indie, and release it as a separate App Store product.

### Progress at October 2, 2026

| Step | State | Evidence / exit condition |
| --- | --- | --- |
| 1. Document and inventory | Complete | Current repositories, identifiers, App Groups, direct feeds and device-source ownership are recorded in the [current inventory](pios-first-party-mobile-current-inventory-2026-09-27.md). |
| 2. Define the local contract | Complete for v0.1 | The [local handoff contract](pios-first-party-mobile-local-handoff-v0.1.md) defines envelopes, attachments, selection boundaries, acknowledgements and failure behavior. Harmless fixture tests pass. |
| 3. Prepare Core | Complete in source and signing | Core contains a tested allowed-flow registry, local envelope persistence, integrity validation, idempotent pending-item validation/acknowledgement and local status primitives. The iOS app checks pending App Group envelopes on launch and foreground activation. The two-group source configuration and truthful local App Group status UI are present. On September 27, 2026, Xcode created development profile `141896af-0a6f-47c5-86dc-95569ea148da` and a signed generic iOS build verified both groups for the main app while the Share Extension retained only Core's private group. The original disabled outbound boundary was later superseded for Notes only by the separately reviewed and activated Stage 8 bidirectional Notes milestone. |
| 4. Move Notes and Voice Notes feeds | Complete | Both apps have tested producer adapters, remain independently usable, no longer call their direct LifeStory writers, and select `group.com.prifina.reactjs` for App Group exchange. Voice Notes excludes original audio and its prior direct HTTPS Core client is excluded from the target. On September 27, 2026, live Notes insert/update/archive and Voice Notes insert/transcription/rename/archive handoffs were acknowledged locally by Core with nothing left waiting. |
| 5. Prepare LifeStory Indie | Needs migration-export correction; release pending | The existing app keeps its bundle ID, iCloud container, App Group, URL scheme, storage and schema while its source display name becomes LifeStory Indie. It has no runtime Notes or Voice Notes connection and preserves previously mirrored records. September 29 source review found that its notes-migration ZIP embeds the complete snapshot, including `exportSettings` and therefore potentially an endpoint token, while copying only Notes-related attachments. This ZIP must not be used for Core migration. A purpose-built sanitized, allowlisted export is required before installation/publication or owner-data migration. |
| 6. Activate the local App Group runtime | Complete | The existing `group.com.prifina.reactjs` is used for App Group exchange while `group.com.valto.storageinbox` stays Core-private. Signed Core, Notes and Voice Notes builds are installed on the owner iPhone. On September 27, 2026, the owner verified Notes insert/update/archive and Voice Notes insert/transcription/rename/recoverable-deletion flows. Each terminal check showed zero waiting items; Core recorded ten cumulative local acknowledgements. Voice Notes legitimately emitted recording, transcript and generated-metadata revisions under one stable recording identity. No PIOS server connection or server-side event was involved. |
| 7. Prepare Core-owned device sources and notifications incrementally | Complete at the retained app-side checkpoint | Notification/APNs readiness and the selected local collector classes were implemented and validated under their source-specific boundaries. Exact owner measurements and device diagnostics remain private. Continuous high-accuracy GPS, background Health delivery and server forwarding were deferred; this checkpoint is not current activation authority. |
| 7B. Assess source parity and define the local LifeStory projection | Complete and independently approved; runtime publication deferred | LifeStory Indie’s device models and processing boundary were compared with Core’s completed local evidence stores. Core now has a versioned factual projection for Photos, Calendar, derived stays/routes and Health, with source provenance, sensitivity, confidence, exact timestamps, monotonic revisions, fail-safe withdrawal tombstones, integrity and explicit `doNotClaim` rules. Raw location/movement, Motion and Contacts remain context-only; repeated places require owner review. The full projection maps to the registered Core-to-LifeStory App Group flow, but no envelopes are published until the separate new LifeStory consumer exists. The complete suite passed 155 tests, iOS/macOS builds passed and independent review approved the corrected milestone. |
| 7C. Retain Core-owned Notes and Voice Notes content | Complete locally; Notes subsequently PIOS-connected | Core's private, integrity-bound inventory accepts current Notes and Voice Notes transcript revisions only after App Group validation and durable persistence. Imported/historical content remains excluded, Notes attachment bytes remain Notes-owned and Voice Notes audio remains Voice-Notes-owned. The local milestone passed 170 tests and independent review. The later Stage 8 Notes milestone then added governed forwarding and reconciliation for Notes only and completed production end-to-end proof on October 2, 2026. |
| 7D. Complete the first bidirectional PIOS application workflow | Complete for Notes only | Notes now supports canonical Solo storage, browser read/create/edit, pin/archive/restore, conflict-safe revisions, canonical Events, iPhone reconciliation, exact-once replay and isolated recovery. Voice Notes and Core-owned device sources are not promoted by this result. The deployment-specific evidence is in the PIOS Solo bidirectional Notes production workflow. |
| 7A. Assess local/cloud synchronization behavior and principles | Deferred assessment | Review the behavior that actually exists before defining the operating model. The assessment must cover triggers, cadence, background execution, freshness, batching, retries, conflicts, offline operation, resource constraints, owner controls, observability and recovery across App Group, optional app-owned synchronization and the future Core-to-PIOS boundary. No implementation or cloud activation is included. |
| 8. Prepare and optionally run historical migration | Deferred | Fixture intake and reconciliation can proceed locally; any real owner-data migration requires a separate explicit decision and verified rollback. |
| 9. Release the existing first-party mobile applications | Deferred | App Store and TestFlight changes for Core, Notes, Voice Notes and LifeStory Indie require a later release milestone. |
| 10. Create new LifeStory last | Deferred by owner sequence | This is the final application milestone. Exit requires a separate identity, exclusive operation on Core-provided data, isolation from LifeStory Indie and separate release. |

## Current Connection Boundary

The earlier all-local implementation boundary is complete and remains the
baseline for every source that has not received a separate PIOS activation.
Notes is the sole current exception:

- Notes may use the separately reviewed Core-mediated PIOS forwarding and
  reconciliation contract documented by the Stage 8 Notes milestone, plus the
  bounded direct command/acknowledgement path where separately activated.
- Voice Notes and Core-owned Photos, Calendar, Location, Visits, Contacts,
  Motion, Routes, Stay/Place and Health data remain device-local or Core-local;
  none is PIOS-connected merely because Notes is connected.
- Participating applications continue to publish and consume through the
  versioned local App Group contract; they do not receive owner-wide PIOS
  credentials or write Core's private stores directly.
- The retained `local_accepted` v1 wire value means App Group validation only;
  it is neither Core-owned ingestion nor canonical PIOS acceptance.
- A source becomes PIOS-connected only after its own governed intake, identity,
  provenance, Events, conflict, recovery and owner-visible acceptance checks
  pass. Notes completion does not authorize another source or historical
  backfill.

## Acceptance Boundary

Implementation is complete only when:

1. Notes and Voice Notes remain fully usable with Core absent;
2. their PIOS-bound source data reaches Core through durable local handoff;
   the optional Notes direct reconciliation identity remains command/acknowledgement
   scoped, does not replace local-first operation or the broker fallback, and
   requires no Prifina app backend;
3. third-party PIOS clients remain unaffected;
4. new LifeStory clearly requires Core and cannot silently fall back to its
   own device-source or PIOS network path;
5. Core owns each activated device permission and exposes source provenance
   and collection status;
6. foreground termination or delayed iOS background execution does not lose
   pending work;
7. cached, offline-retained, pending, App Group-validated and Core-ingested
   states remain distinct;
8. LifeStory Indie and its existing data remain intact throughout coexistence
   and migration testing;
9. a migration dry run and one owner-selected real migration prove duplicate
   handling, identity reconciliation, rollback and non-destructive behavior;
10. no application-specific Prifina backend is required for browser or
    multi-device operation; those options are iCloud, an owner-configured
    endpoint, or PIOS through Core according to the product role above.

## Authority And Current Effect

This plan records owner-selected architecture and sequencing. The bounded
Stage 8 Notes production activation is complete under its own reviewed
authorization and evidence. It does not authorize Voice Notes or device-source
forwarding, historical migration, another device, source deletion, shared
editing, new App Store identities or the new LifeStory application.

Live impact: signed Core, Notes and Voice Notes development builds remain in
use on the owner iPhone. Notes has one active Core-mediated PIOS workflow;
other first-party mobile sources retain the boundaries stated above.

The consolidated app-side implementation and ownership handoff is recorded in
[PIOS First-Party Mobile App Handoff — October 2, 2026](pios-first-party-mobile-app-handoff-2026-10-02.md).

## Capability Documentation Assessment

No new reusable PIOS Capability MLE is introduced by this decision. The
profile composes already documented abilities: governed capture submission,
authorized device caching, selected offline retention, connected-source
registration, import-session management and governed Core access.

The individually meaningful product operations remain separate:

| Candidate | MLE result | Documentation treatment |
| --- | --- | --- |
| Hand app-owned data to Core | Passes: an originating app can submit one versioned item and receive a determinable acknowledgement | Existing governed-capture capability plus this operational profile |
| Maintain device-local Core content | Passes: Core can cache, refresh or remove an authorized non-canonical copy | Existing authorized-device-cache capability |
| Retain selected content offline | Passes: the owner can deliberately retain a bounded accepted version for offline use | Existing selected-offline-content capability |
| Migrate LifeStory Indie data | Passes: the owner can export and reconcile a bounded historical package with a determinable result | Product-specific migration operation to define before implementation; do not fold it into ordinary synchronization |
| Collect one device source through Core | Passes per source class because permission, current state, collection result and failure are independently meaningful | Define source-specific operational contracts during the incremental implementation stage |

The shared App Group envelope, queue directories and acknowledgements are
realization elements, not capabilities by themselves. No capability inventory
row changes until a new operational CRD is written for the LifeStory migration
or a device-source class.

### Statement provenance

| Statement | Semantic class | Source |
| --- | --- | --- |
| The profile applies only to the PIOS First-Party Mobile Apps by Prifina | owner choice / implementation requirement | Owner direction, September 27, 2026 |
| Notes and Voice Notes remain standalone and use Core for PIOS exchange | owner choice / implementation requirement | Owner direction, September 27, 2026 |
| Existing LifeStory becomes LifeStory Indie and remains intact | owner choice / implementation requirement | Owner direction, September 27, 2026 |
| New LifeStory is a separate Core-dependent application | owner choice / implementation requirement | Owner direction, September 27, 2026 |
| Core assumes new LifeStory device-source collection | owner choice / implementation requirement | Owner direction, September 27, 2026 |
| New LifeStory creation is the final application milestone, after Core and existing-app foundations | owner choice / delivery sequence | Owner direction, September 27, 2026 |
| Core keeps a private App Group and uses the existing Prifina App Group separately for App Group exchange | owner choice / security boundary | Owner direction, September 27, 2026 |
| App Groups are shared trust domains and cannot be always-running routers | rule/invariant | PIOS Integration Interoperability and Governance v0.1, section 19 |
| Personal Apps Cloud is no longer the target backend | owner choice / architecture disposition | Owner direction, September 27, 2026 |

### Unresolved questions

- New LifeStory bundle identifier, App Store metadata and repository location;
  decide these only when the final application milestone begins.
- Timing for removing LifeStory Indie from `group.com.prifina.reactjs` after its
  remaining share-extension and storage dependencies are reviewed.
- LifeStory Indie import reconciliation rules and Core acknowledgement behavior;
  the existing notes-migration ZIP is unsafe for this purpose because it may
  contain an endpoint token. Define and implement a sanitized allowlisted
  migration package before any Core import.
- Per-app plaintext versus encrypted/mediated data placement inside the shared
  trust boundary.
- Which iCloud capabilities, if any, Notes and Voice Notes will ship first.
- Which bounded first-party source follows Notes into PIOS-connected operation;
  no source is selected automatically by this document.
