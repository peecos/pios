# LifeStory Reference Assessment For Core Mobile

Public documentation projection: owner-specific measurements, device names and
local filesystem locations are omitted. The unabridged implementation records
are retained privately. Dated checkpoints are historical evidence, not current
activation instructions; use the [current alignment notice](pios-mobile-contract-alignment-2026-10-08.md)
and the implementation's current authorized roadmap.

Status: Stage 8 architecture input; local source parity assessed and Core-to-LifeStory projection v0.1 implemented with fixtures

Date: September 29, 2026

Scope: read-only assessment of LifeStory Indie source commit
`9e664a84c68e268eee232519f049446f58960db3`, its documented real-use captures,
data model, processing pipeline and glossary implementation. This document
does not authorize server connectivity, historical processing, biometric-data
transfer or migration of the full owner snapshot.

## Outcome

LifeStory contains valuable source-specific implementation knowledge, but Core
should not inherit its application-shaped architecture. Core should reuse the
proven collection semantics, evidence fields, review interactions and privacy
rules while separating device capture from reusable PIOS processing.

The intended boundary is:

```text
iPhone frameworks and first-party apps
  → Core app device adapters and protected source/working records
  → normalized, source-neutral evidence envelopes
  → governed PIOS ingestion and processing
  → candidate glossary/knowledge/history records
  → explicit owner review and promotion
  → authorized projections back to Core and LifeStory
```

Core remains useful on-device before a PIOS connection exists: it can collect,
display, export and delete its local source records. Cross-device processing,
canonical glossary state and multi-source understanding belong to PIOS once a
connection is explicitly activated.

## What LifeStory Proves

### Useful data architecture

LifeStory schema 18 already distinguishes:

- raw source evidence;
- processed evidence;
- visible or hidden memories;
- daily and weekly History;
- Insights;
- glossary items and glossary suggestions;
- visual entity observations and owner-confirmed cluster links;
- source cursors and horizons; and
- durable processing jobs and status.

The strongest reusable idea is the three-stage pipeline:

1. capture exact source evidence;
2. create deterministic or model-assisted Derived evidence; and
3. publish owner-facing narrative or knowledge only after processing succeeds.

This prevents incomplete source records from appearing as finished memories
and allows later reprocessing without asking the original device API to return
the same data again.

### Useful source models

LifeStory provides concrete starting fields for Core collectors:

| Source | Proven useful fields | Core treatment |
| --- | --- | --- |
| Location point | coordinate, captured time, accuracy and reverse-geocoded description | Private local source record; exact coordinates remain protected |
| Visit | coordinate, arrival, departure, recorded time, place description and city | Local observed event; later place/stay processing is Derived |
| Route point | coordinate, captured time, accuracy, speed and motion activity | Local raw series; never directly equivalent to a journey |
| Health window | bounded time range, steps, walking/running distance, workouts, sleep segments, heart-rate measures and State of Mind count | Local read-only observation with metric-level provenance; no medical or emotional inference |
| Contact candidate | stable Contacts identifier, names, nickname, organization and counts of contact channels | Identity hint only; contacts do not become memories or confirmed people automatically |
| Photo observation | PhotoKit identifier, timestamp, location, provenance classification, Vision observations and local cluster identifiers | Local metadata and privacy-sensitive Derived evidence; original bytes remain in Photos unless deliberately retained |
| Calendar event | stable identifiers, selected calendar identity, start/end, notes and location | Local observed event under the current-day advancing boundary |

### Useful glossary behavior

LifeStory’s Personal Glossary provides a strong interaction pattern:

- suggestion cards state the proposed type, alias, evidence and source;
- photo suggestions show source images and face highlights;
- place suggestions show map context and an adjustable radius;
- suggestions can define a new item, merge into an existing item or be ignored;
- confirmed people and pets retain visual-cluster links;
- individual false memory/photo links can be excluded; and
- a badge/update indicates that review is waiting.

The important trust rule is correct: visual analysis may propose an
unidentified person or pet, but only the owner may assign a real identity.

### Useful presentation patterns

The documented July 2026 real-use captures show effective patterns worth
retaining:

- chronological, text-first records;
- compact source headers and timestamps;
- maps, routes and photos embedded only where relevant;
- day-part and date grouping;
- progressively loaded History rather than opening every period at once;
- source details available behind the primary presentation; and
- review badges for glossary or processing attention.

These are presentation references, not a requirement to reproduce LifeStory’s
Feed inside Core.

## What Core Should Not Copy

LifeStory also exposes legacy architecture that should not be repeated:

- `MemoryStore` combines persistence, collection, processing, AI writing,
  migration, scheduling, glossary logic and UI state in one very large actor;
- `MemoriesView` directly orchestrates multiple device APIs and processing;
- the complete product state is serialized into one mutable JSON snapshot;
- many source payloads and processor outputs use loosely typed string maps;
- source collection, glossary generation and visible narrative publication are
  coupled to app foreground activity;
- app-specific `LifeMemory` objects act as both evidence and presentation;
- some glossary suggestions rely on English/Finnish word heuristics and random
  suggestion identifiers rather than stable source-derived identities;
- background modes are opportunistic and cannot guarantee processing; and
- the Feed/Profile surface accumulated operational, creative and governance
  controls, contributing to the clutter and performance problems already seen.

Core should therefore reuse behavior selectively, not move LifeStory’s store or
view hierarchy wholesale.

## Processing Placement Decision

### Keep in Core on iPhone

These capabilities require Apple frameworks, immediate owner control, offline
operation or a privacy-preserving device boundary:

- permission requests and revocation status;
- PhotoKit, EventKit, Core Location, Core Motion, HealthKit and Contacts reads;
- forward-only activation boundaries and source cursors;
- stable source identifiers, timestamps and source-specific provenance;
- local durable buffering, idempotency and pending-handoff state;
- lightweight validation, normalization and exact duplicate detection;
- location accuracy filtering and motion-gated sampling needed to avoid storing
  obvious GPS noise;
- local Vision face/animal detection and local visual feature extraction by
  default;
- thumbnails or evidence previews needed for owner review;
- immediate local source browsing, status, export and deletion; and
- owner-triggered manual capture and check-in UI.

These are device-side PIOS functions. Core should not require server
connectivity for these local capabilities; outside the server is not outside PIOS.

### Put in server-side PIOS processing

These capabilities gain value from durable execution, cross-source context,
larger history windows and reuse across devices and connectors:

- canonical source registration, Originals and Events;
- durable processing manifests, retries, scheduling and observability;
- place/stay/journey correlation across phone location, photos, calendar,
  workouts, imports and other devices;
- term and entity candidate extraction from Notes, Voice Notes transcripts,
  documents, messages and future connectors;
- source-neutral duplicate detection and entity resolution proposals;
- glossary candidate ranking, evidence aggregation and lifecycle;
- owner-confirmed glossary, alias and relationship state;
- Knowledge, Meaning, Learning, History and Insights generation;
- model-assisted summaries and writing with recorded model/profile/version;
- cross-device retrieval, search, graphs and projections; and
- rebuilding Derived representations when processors or models change.

These are PIOS functions even when their executor is replaceable or physically
colocated with Core in a Solo deployment.

### Hybrid or profile-dependent capabilities

| Capability | Default | Optional PIOS profile |
| --- | --- | --- |
| Face/person grouping | Detect, embed and cluster on-device; retain no global identity claim | Upload only explicitly authorized Derived representations or selected images for owner-private cross-source clustering |
| OCR and image understanding | Lightweight Apple-framework extraction may run locally | Approved multimodal processing over a retained/authorized Original, with model and sensitivity provenance |
| Speech transcription | Voice Notes may produce the source transcript locally or through its selected endpoint | PIOS stores the verbatim transcript and may create a corrected readable Derived version |
| Reverse geocoding | Local result supports immediate display | PIOS may normalize places across sources and time while preserving the original coordinate evidence |
| Glossary suggestions | Core may produce deterministic local candidates for immediate review | PIOS combines candidates across all authorized sources and owns canonical proposal/review state |
| Feed preview | Core may show factual source summaries | Narrative memories, History and Insights are generated as governed PIOS projections for the future Core-dependent LifeStory |

Face embeddings and other biometric representations require a separately
reviewed elevated authorization before leaving the device. Confirmed person
identity, evidence references and exclusions can synchronize without exporting
the original biometric vector.

## Source-Neutral Processing Contract

Processing should consume normalized evidence rather than PhotoKit, EventKit
or LifeStory-specific objects. A minimum envelope needs:

```yaml
record_id: stable source-owned id
source_definition_id: stable registered source
source_record_id: provider or device record id
source_version: version or modification marker
kind: photo | calendar_event | location_point | visit | route_point | health_window | note | transcript
occurred_at: source event time
captured_at: device capture time
collected_at: adapter collection time
activation_boundary: forward-only collection boundary
payload_schema: typed schema name and version
payload: source-specific typed body
sensitivity: declared class
integrity: hash or equivalent evidence
provenance: device, app, account/profile and adapter version
```

For the current Core iPhone implementation, `device` is represented by a
private persistent installation-scope identifier and Calendar's local EventKit
source identifier is represented by a one-way identifier. Any later PIOS enrollment binds
that local installation scope to the governed device and owner identities; it
must not assume source-library identifiers are globally unique.

Every processor output should reference this identity and add:

- processor/profile/model version;
- input record versions;
- confidence and evidence/support type;
- explicit `do_not_claim` constraints;
- processing state and failure reason;
- created/replaced/superseded timestamps; and
- retention and deletion behavior.

This lets the same place, terminology, person-candidate and History processors
work over phone records, browser uploads, takeout imports, wearables and future
third-party connectors.

## Glossary And Suggestions Target

Core/PIOS should separate three objects:

1. **Evidence signal** — a term occurrence, face cluster, contact hint, repeated
   place, organization name or other source-linked observation.
2. **Glossary proposal** — a stable candidate combining one or more signals,
   with type, proposed alias/meaning, confidence, source coverage and status.
3. **Glossary entry** — owner-confirmed personal vocabulary with aliases,
   relationships, evidence links, exclusions, revisions and lifecycle.

Initial reusable suggestion processors:

| Processor | Inputs | Output rule |
| --- | --- | --- |
| People in photos | Local visual clusters and source-image references | Propose unidentified person clusters; never assign a name automatically |
| Pets in photos | Local animal clusters and source-image references | Propose unidentified pet clusters; owner names or merges |
| Note/transcript terminology | Owner-authored Notes and verbatim Voice Notes transcripts | Rank repeated or high-signal terms; preserve excerpts/evidence references, not only frequency |
| Repeated places | Visits, stays, routes, photo locations and check-ins | Propose a place only after repeated/coherent evidence; show map/radius and source coverage |
| Contact-assisted identity | Owner-selected Contacts records plus an existing person proposal | Suggest a possible match; never auto-link based on a name alone |
| Projects/organizations/products | Notes, transcripts, calendar, files and manually confirmed context | Cross-source proposal with typed evidence and ambiguity handling |

Suggested lifecycle:

```text
detected → proposed → owner_confirmed
                    ↘ ignored
owner_confirmed → merged | superseded | archived
link → excluded | corrected
```

Suggestion IDs must be deterministic from processor version, candidate type and
source evidence identities so the same rejected suggestion does not reappear.

## Core iPhone Presentation

Core should not add another dense LifeStory-style feed. The mobile UI should
use three clear layers:

### Device Sources

One source card per permission/collector showing:

- permission and activation state;
- collection boundary;
- last successful check and freshness;
- local record count and pending handoff count;
- concise attention reason; and
- a detail screen with source records and deletion/export controls.

Location and Visits should be separate activation decisions even if shown in
one Location family section. Always-location escalation must explain its value
before requesting permission.

### Review

A compact “Needs review” card on Overview links to a dedicated review queue.
Glossary candidates use evidence-first cards with:

- proposed type and alias;
- why it was suggested;
- source badges and evidence count;
- a photo strip, transcript/note excerpt or map preview where relevant;
- primary actions `Define` and `Link existing`;
- secondary actions `Ignore` and `Not this evidence`; and
- no automatic promotion.

The profile/status icon may carry the numeric badge, but the review content
should open as a full page rather than a deeply nested settings form.

### Glossary

The local Core surface should show a cache of active entries and pending
proposals. Once connected, PIOS is authoritative for glossary lifecycle and
Core displays synchronized state. Entry detail exposes aliases, meaning,
relationships, evidence, exclusions and revision status without exposing raw
coordinates or biometric vectors by default.

## Existing LifeStory Data

LifeStory Indie remains untouched and its historical data stays usable there.
Core should not depend on reading LifeStory’s live mutable JSON snapshot. The
current notes-migration ZIP is also not safe for this purpose: source review
found that it embeds the complete snapshot, including `exportSettings` and its
potential endpoint token, while copying only Notes-related attachments. It must
be replaced by a purpose-built sanitized export before any owner snapshot is
moved.

Recommended first import:

1. LifeStory creates a new allowlisted migration bundle that excludes endpoint
   URLs, tokens, model credentials, transient processing state and unrelated
   settings while retaining an exact source export and integrity manifest for
   the declared record scope.
2. Core presents counts by category before import.
3. The owner selects a small representative set: several records from each
   source type, existing owner-authored glossary entries and a few unresolved
   suggestions.
4. Core retains the exact bundle as an Import and creates a read-only local
   presentation projection.
5. Existing memories, History and Insights remain identified as LifeStory
   application outputs, not canonical observations.
6. Owner-authored glossary entries may be proposed for import with their
   existing confirmation provenance; inferred suggestions remain candidates.
7. No historical processing starts automatically. Any backward processing is
   a separate explicit operation and later may be a paid capability.

The source review also used LifeStory’s committed July 2026 real-use captures.
They contain real photo, route, location, calendar and narrative examples and
are sufficient for initial layout/design reference. A current owner snapshot
was not copied during this assessment because the iPhone data-container service
was unavailable; this does not block the architecture decision.

## Ordered Implementation Recommendation

1. **Complete:** define typed
   source-neutral Core mobile evidence envelopes before adding more collectors.
   The first contract is documented in the Core app repository at
   `docs/core-mobile-evidence-contract-v0.1.md`.
2. **Complete:** project the
   existing Photos and Calendar inventories through those types without
   changing their source-specific collection behavior.
3. **Implemented, independently reviewed and owner-device validated:**
   foreground Current Location as an explicit one-shot local source record and
   source detail view. Source-to-evidence mapping was validated; owner
   measurements remain private.
4. **Implemented, independently reviewed and activation-validated:** add low-power Background Movement as a
   separate Always-location activation using significant location changes.
   Retain raw approximate movement points; do not run continuous high-accuracy
   GPS or generate narrative memories locally. First real significant-change
   delivery remains an observational follow-up after qualifying travel.
5. **Implemented, independently reviewed and owner-device activation validated:**
   Visits as a separate Always-location activation retaining raw arrival,
   departure, coordinate and accuracy; no narrative memory or named place.
   First actual iOS Visit delivery remains observational.
6. **Completed September 29, 2026:** Contacts with separate permission, a
   local current-state inventory and normalized identity-hint evidence.
   Record parity was checked; owner measurements remain private.
   Core does not infer relationships, confirm people, or
   auto-link records.
7. Add deterministic local stay/place preprocessing with explicit confidence
   and `do_not_claim` fields.
8. Add a local glossary proposal store and evidence-first Review UI, initially
   supporting repeated places and existing photo clusters.
9. Add Motion/Routes, then Health, each with separate permissions, local
   records and source detail.
10. Correct LifeStory’s migration exporter, then add the bounded migration
   preview/import so real existing data can populate Core views without
   starting historical processing.
11. Define and activate PIOS ingestion only after the complete local source and
   review contracts pass owner validation.
12. Move cross-source glossary generation, canonical promotion, History,
   Insights and reusable model processing to PIOS.
13. Create the new Core-dependent LifeStory application last, consuming only
   authorized Core projections.

## Decision

Use LifeStory as implementation evidence and migration source, not as Core’s
domain model. Build collection and privacy-sensitive preprocessing in the Core
iPhone app; build source-neutral multi-source understanding and canonical
review state in PIOS. Keep the interface between them versioned, idempotent,
provenance-rich and independent of any single phone API.

## September 30 Source-Parity Result

The completed Core local collectors now cover the device-source classes that
LifeStory Indie used directly for Photos, Calendar, location/visits,
motion/routes, Contacts-assisted context and Health. The parity is structural,
not a claim that Core reproduces every LifeStory heuristic or visible memory:

| LifeStory Indie source/output | Core-local status | Projection decision |
| --- | --- | --- |
| Photo metadata | Available as integrity-bound normalized evidence | Project factual photo observations; no photographer/person/activity claim |
| Calendar events | Available as integrity-bound normalized evidence | Project as planned context, not proof of attendance |
| Location points and Visits | Available as raw local evidence | Withhold raw points from the LifeStory projection; use conservative stay candidates |
| Motion and route points | Motion evidence and derived route candidates available | Withhold raw motion; project routes only as bounded candidates |
| Health windows | Available in a rollback-safe evidence inventory | Project factual aggregates with sensitive-health classification |
| Contacts | Available as identity-hint evidence | Keep context-only; never bulk-create memories or confirmed people |
| Repeated places | Available as derived candidates | Reserve for owner-reviewed glossary proposals, not automatic timeline records |
| Notes and Voice Notes | App Group producer/acknowledgement flow works | Core-owned source inventories and projection lifecycle still need implementation |
| Weather | No Core device collector | Later external/PIOS context, not required for the local device contract |
| Links/manual entries | Owner/app-authored rather than device evidence | Belong to future LifeStory or other first-party app capture flows |
| Finished Feed, History and Insights | LifeStory application outputs | Must not be copied into Core’s device evidence model |

Core now implements `core_lifestory_projection_record_v1` and
`core_lifestory_projection_inventory_v1`. The contract carries factual fields,
source versions, sensitivity, confidence, monotonic revisions, integrity and
explicit `doNotClaim` constraints. It maps to the registered Core-to-LifeStory
App Group flow but runtime publication remains disabled until the separate new
LifeStory consumer exists. The implementation contract is documented at
`docs/core-lifestory-local-projection-v0.1.md` in the implementation repository.
The corrected implementation passed the complete 155-test Core suite, generic
iOS and macOS builds, and independent milestone review on September 30, 2026.
