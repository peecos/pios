# Apple Local and Mixed-Device Profile v0.1

Status: proposed, selectable implementation profile for PIOS 2.0. Requirements
below apply only to profiles explicitly selecting these behaviors. This is not
an adopted first-party implementation, a release claim or new mandatory Core
behavior. No provider, device source, cloud service or migration is activated.

## 1. Purpose and baseline

Support useful PIOS on selected devices, with optional remote Core integration,
without requiring every owner to adopt the same hardware or hosting topology.
Use the existing [hosting boundaries](hosting-core-boundaries-and-portability-principles-v0.1.md),
[Core compatibility contract](core-distribution-and-compatibility-spec-v0.1.md)
and [integration governance](integration-interoperability-and-governance-v0.1.md).
The five zones remain Originals, Events, Knowledge, Derived and System; canonical
Events remain append-oriented and canonical acceptance remains governed.

This profile adds no compatibility level, API/export version, endpoint or
required protocol. It does not alter Solo's preferred complete server package
or classify device-side PIOS as an independent external consumer.

## 2. Select behavior and authority separately

| Selected arrangement | Meaning and limit |
| --- | --- |
| Device-side PIOS | Local sources, working state and selected PIOS capabilities; useful without a remote server, with explicit limits and no implied complete-Core claim. |
| Conformant Local Core | A local deployment with named canonical authority and evidence for its declared existing Core compatibility contract, including the interfaces that contract requires. |
| Device-side PIOS with remote Core | Selected capture, retrieval, cache and reconciliation through a compatible hosted or self-hosted Core; local work and remote acceptance remain distinct. |

The Core app remains PIOS-native when operating selected local PIOS behavior
without a remote server. Its PIOS-dependent purpose does not require every
operation to contact a server. A cache, shared database, cloud replica or five
named containers alone is not a Local Core. Do not claim a particular build
implements any arrangement without evidence.

## 3. Common model, portable identity and state

Keep owner, Core, app, device and provider-account identities distinct. Bind
source records to stable source identities/revisions; bind accepted canonical
records to portable logical identities and `core://` references. Physical paths,
Apple record identifiers and account details remain adapter metadata, with
explicit mappings rather than replacements for portable canonical identity.
Preserve provenance, integrity, schema versions and unknown extension metadata
through supported transfer; reject unsupported records without silently dropping
fields. Shared meaning does not require a shared physical database.

Distinguish device-source records, app-owned working records, pending submissions,
accepted-content caches, selected offline content and Derived representations.
Source and working records may be the only copies; they are not evictable cache
or automatically pending upload. Declare retention, deletion and recovery per
class, including what remains local and what a transfer actually contains.

## 4. Sources, connectors and processing reuse

An existing application's connector can supply a selected source only where
its supported access/export contract and permissions have been qualified.
Declare actual read/write operations, source fidelity, attachment coverage,
revision mapping, deletions and freshness; do not assume arbitrary access to
another application's private store. A dedicated app is an alternative when
the selected workflow needs it, not a prerequisite for every source.

Start collection and automatic processing at the selected activation boundary.
Connection, import or a newly available device does not authorize blind
historical backfill. Historical import is separately selected, bounded and
reconciled; portable Core migration does not require re-ingesting source history.

Shared processing may reuse a retained transcript, extraction or other result
across authorized applications. Bind reuse to source revision, parameters,
language, processor/version, integrity and permitted audience; revalidate current
policy before use. Reuse is not permission to rerun processing or disclose the
result more widely. Local preprocessing and remote execution have separately
declared recipients, retention and failure behavior. Select the optional
[controlled-disclosure profile](integration-interoperability-and-governance-v0.1.md#controlled-disclosure-profile)
explicitly where its additional contract is wanted; existing grants always apply.

## 5. Replication, acceptance and recovery

Shared Apple storage or CloudKit replication is a proposed implementation choice,
not blanket canonical authority or a default new cloud. Before selection,
validate the mechanism and declare account ownership, readers, processing,
retention and export/recovery limits. App-owned synchronization stays separate.
Shared plaintext must be suitable for every actual reader; grant metadata alone
does not isolate it. Never distribute unrestricted owner credentials for reuse.

Name the canonical side for each writable flow. Local save, replica transfer,
handoff validation, canonical acceptance, local application and acknowledgement
are separate boundaries. Successful synchronization proves neither canonical
acceptance nor independent recovery. Use stable operation identities, expected
revisions, idempotent retries and declared conflict/merge rules; preserve
divergent edits and unresolved pending work. Corrections, revocation and deletion
must reconcile without silently replacing canonical history.

On an account/Core switch, isolate prior-owner data and pending operations;
do not rebind them automatically to the new account or destination. Re-establish
identity and grants explicitly. Before changing canonical authority, validate
the destination, reconcile accepted and pending revisions and define the final
delta, owner-approved cutover and rollback under the existing contract. Two
writable replicas must not become ambiguous canonical writers.

Recovery evidence separately covers accepted Core state, device-only sources,
app-owned working records, pending work and selected native services. Validate
export, integrity, identity preservation and retrieval/restoration independently
of normal synchronization, including loss of a device or account access.
Do not claim independent recovery from another synchronized replica alone.

## 6. Mixed-device examples and actual availability

These are selectable scenarios, not implemented product claims:

| Devices | Useful selection and explicit limit |
| --- | --- |
| iPhone only | Selected local capture, retained records and authorized local processing; remote hosting is optional where those capabilities permit it. No automatic Local Core claim. |
| iPhone and PC | Phone capture plus a qualified browser/client or portable exchange on the PC; declare which reads/writes and offline content exist on each device. Do not presume Apple replication supplies PC access. |
| Mac and Android | Selected Mac sources plus a qualified Android client, connector or browser path; common IDs and authority rules do not promise identical device APIs or source coverage. |

For each capability report separately whether it is implemented, installed,
enabled, authorized, reachable and healthy, with scope, freshness and evidence.
These are availability dimensions, not new Core Compatibility Levels or a
mandatory upgrade ladder. Explain prerequisites, processing location, recipient
disclosures and offline limits. A healthy local capability can coexist with an
unreachable remote Core; installed software alone is not available functionality.
Declare browser authentication, supported read/write operations, attachments,
pending/conflict behavior and unavailable paths; web access is not implied by
cloud synchronization or by the presence of a phone app.

## 7. Preserve the selected first-party profile

The [current first-party profile](pios-first-party-mobile-apps-by-prifina.md)
and [October 8 alignment](pios-mobile-contract-alignment-2026-10-08.md) retain
authority for the suite. Notes keeps Core-mediated handoff and its bounded
direct command/acknowledgement reconciliation path, with equivalent identities,
conflict rules and broker fallback. Notes and Voice Notes remain independently
useful, with any app-owned iCloud/custom-endpoint sync separately selected.
This proposal does not extend Notes activation to Voice Notes or device sources.

LifeStory Indie preserves its identity, data and independent behavior. The
separate new LifeStory remains Core-dependent, receiving authorized Core-provided
sources rather than silently acquiring its own collection or network route.
No app identifiers, entitlements, routing choices or release sequence change.
Proposed shared storage does not replace current app-owned synchronization.

## 8. Validation targets before implementation claims

Resolve platform API access, entitlements, supported OS/device combinations,
background behavior, language/model support, browser access, quotas and pricing
against current primary evidence when a mechanism is selected. This document
makes no availability or pricing claim for those mechanisms.

Prove the chosen flow with fixtures for local/offline use, authorized reuse,
duplicate/lost responses, conflicting edits, denied access, account separation,
cutover/rollback and recovery of device-only and pending records. Record actual
browser and mixed-device limits. Documentation checks do not prove runtime
capabilities, canonical acceptance, recovery or adoption of this proposal.
