# PIOS First-Party Mobile Local Handoff v0.1

Status: active device-local transport contract; Notes also uses a separately
governed server forwarding and bidirectional reconciliation path

Date: September 27, 2026

Contract clarification: October 8, 2026. Read the
[alignment notice](pios-mobile-contract-alignment-2026-10-08.md) and
[Integration sections 19.7–19.8](integration-interoperability-and-governance-v0.1.md#197-device-source-and-working-state).
The local transport does not itself confer server acceptance or authorize a
source connection. Historical verification below retains its original scope.

## Purpose

Provide a durable, versioned, device-local exchange between Core and the PIOS
First-Party Mobile Apps by Prifina without making a shared database the
application contract and without implying canonical PIOS acceptance.

## Participants

- `core`
- `notes`
- `voice_notes`
- `lifestory_indie`
- `lifestory`

Every participant retains its own bundle identity, app-local source of truth,
permissions and audit attribution.

The initial September 27 Notes flow was `notes -> core`. The subsequently
implemented Notes contract also supports `core -> notes` canonical revision
commands and application acknowledgements. It uses explicit registered flows,
a consumer-side application contract and expected-version conflict behavior;
it is not implied by App Group membership or generic envelope fields. Core must
not write the Notes private store directly. Other participants do not inherit
Notes server activation. Deployment-specific status remains in the current
implementation roadmap rather than this transport definition.

## Container Layout

The product realization selects `group.com.prifina.reactjs` as the shared
App Group for exchange. Core separately retains `group.com.valto.storageinbox` for its
private storage and share extension. Implementations
receive a container root and use this versioned subtree:

```text
PIOSFirstPartyMobile/v1/
  outbox/<producer>/<envelope-id>/
    envelope.json
    payload/                 optional referenced files
  acknowledgements/<producer>/<envelope-id>.json
```

Producers publish a complete envelope directory through an atomic staging
rename. Core scans only known producer directories. An acknowledgement is a
separate record and never modifies the producer envelope.

## Envelope

`envelope.json` contains:

| Field | Meaning |
| --- | --- |
| `schema_version` | Exactly `pios_first_party_mobile_handoff_v1` |
| `envelope_id` | Lowercase UUID identifying this immutable submission |
| `producer` | One participant identifier |
| `consumer` | One participant identifier; initially normally `core` |
| `data_class` | `note`, `voice_transcript`, `lifestory_migration`, `lifestory_projection`, or `device_source` |
| `operation` | `upsert`, `archive`, `delete`, `import`, or `project` |
| `source_record_id` | Stable producer-owned record identity |
| `source_revision` | Positive monotonically increasing producer revision |
| `selection` | `automatic_current` or `explicit_historical` |
| `occurred_at` | Source occurrence time when known |
| `created_at` | Envelope creation time |
| `payload` | JSON object containing the bounded data-class payload |
| `files` | Optional relative file references with media type, byte count and SHA-256 |

An automatic handoff may include only records inside the app's activated
current/future boundary. Historical or imported records require
`explicit_historical`. This preserves the rule that imports and past backfill
do not silently trigger processing.

## Acknowledgement

The consumer writes a separate acknowledgement containing:

- `schema_version`: `pios_first_party_mobile_ack_v1`;
- `envelope_id`, `producer` and `consumer`;
- `state`: `local_received`, `local_accepted`, `applied`, `conflict`, `retryable`,
  or `rejected`, as allowed by the registered flow;
- `recorded_at`; and
- an optional bounded reason.

`local_accepted` is the retained v1 wire value. It means only that Core
validated the envelope structure, registered flow and referenced-file
integrity in the shared App Group, then recorded an acknowledgement there. It
does not mean Core semantically understood the data-class payload, imported a
separate Core-owned copy, or sent the item to a PIOS server.

At the September 30, 2026 local-only checkpoint, Core upgraded eligible automatic-current Notes and
Voice Notes envelopes to `applied` only after exact payload parsing,
source-revision checks and atomic persistence in Core's private App Group
inventory. That checkpoint did not prove server acceptance. In the later
Notes source-forwarding flow, an `applied` acknowledgement is recorded after
canonical Notes acceptance; in the reverse flow it records application of a
Core command through the Notes write contract. Acknowledgement delivery to the
server has its own receipt. Interpret each result by schema, producer/consumer,
operation and authority boundary; do not reinterpret older local receipts as
canonical evidence. Historical envelopes require their separately selected
backfill scope rather than inheriting automatic-current authority.

## Invariants

- Unknown schema versions, participants, data classes and operations fail
  closed.
- Envelope IDs and source IDs cannot contain path separators or traversal.
- Referenced files remain beneath the envelope `payload` directory.
- Declared file size and SHA-256 must match before local acceptance.
- Repeating an identical envelope is idempotent; reusing its ID for different
  bytes is a conflict.
- Pending producer data may be the only copy and is not disposable cache.
- Core must not delete or rewrite producer-owned source data.
- Clearing cache must not remove pending envelopes or acknowledgements.
- No credential, endpoint, access token or server instruction belongs in the
  envelope or acknowledgement.

## Current Contract And Historical Activation Evidence

Current Notes forwarding and reconciliation build on this local contract.
Local validation, semantic application and server acceptance remain distinct.
The named Notes hybrid path may fetch commands and deliver acknowledgements
directly using its own bounded identity; this does not change envelope identity
or permit a second canonical writer. The dated statements below record the
initial local-only milestone and do not define current server connectivity.

The Core app now contains the reference Swift implementation using an injected
container root. It includes the allowed first-party flow registry, atomic
envelope publication, attachment integrity checks, idempotent replay, pending
item discovery, device-local App Group validation and acknowledgement status
listing.
The implementation is compiled by the Core iOS and macOS targets and covered by
harmless temporary-directory fixtures.

Live device-local personal-record exchange was verified on September 27, 2026.
At that September 27 checkpoint, PIOS server forwarding was inactive. No successful local acknowledgement
implies Core-owned ingestion or canonical PIOS acceptance.

The source configuration now names the exchange App Group in Core, Notes and Voice
Notes. Core validates unacknowledged pending envelopes on launch and whenever it
returns to the foreground, does not rewrite terminal acknowledgements during a
later scan, and exposes local availability and queue counts. Live device access
is now provisioned for all three applications. Core's signed September 27,
2026 generic iOS build contains both the private and exchange App Groups, while its
Share Extension contains only the private group. Installed Core, Notes and
Voice Notes builds then passed end-to-end local exchange on the owner iPhone.
This remains a development milestone rather than an App Store shipment claim.

The Notes producer implementation is also present and tested. It derives an
independent monotonically increasing handoff revision from prior immutable
envelopes, so pin, rating and archive changes remain safe even when the Notes
UI version does not increment. Automatic publication excludes imported records
and records before the saved activation day; explicit historical publication
is a separate non-UI operation. Notes configures `group.com.prifina.reactjs`
and has matching Apple profiles. Signed-device insert/update/archive exchange
passed on September 27, 2026.

The Voice Notes producer implementation is present and tested under the same
fail-closed activation rule. It publishes transcript text and recording
metadata as `voice_transcript` records, derives monotonically increasing
revisions from prior immutable envelopes, and represents archive, restore and
deletion changes without copying the recording file. Automatic publication
includes only native recordings on or after the activation day; imported and
older recordings require the separate explicit historical operation. The app
configures `group.com.prifina.reactjs` and has a matching Apple profile. Live
insert/transcription/rename/archive exchange passed on September 27, 2026. Its
earlier direct LifeStory writer is no longer called and its direct HTTPS Core
client is excluded from the application target.
