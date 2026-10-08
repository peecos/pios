# PIOS First-Party Mobile Apps by Prifina — Current Inventory

Public documentation projection: owner-specific measurements, device names and
local filesystem locations are omitted. The unabridged implementation records
are retained privately. Dated checkpoints are historical evidence, not current
activation instructions; use the [current alignment notice](pios-mobile-contract-alignment-2026-10-08.md)
and the implementation's current authorized roadmap.

Status: implementation inventory captured September 27, 2026

This inventory records the current source and identity baseline before local
handoff implementation. It is evidence of repository configuration, not proof
of installed-device entitlements or production behavior.

## Applications

| Application | Current source | Bundle ID | Source version/build | Current App Group | Current relevant behavior |
| --- | --- | --- | --- | --- | --- |
| Core | Core application source | `com.valto.storageinbox` | `1.0 (1)` | Core-private `group.com.valto.storageinbox`; exchange App Group `group.com.prifina.reactjs`; signed development profile verified September 27, 2026 | Core-private capture/share state remains isolated; live Notes and Voice Notes exchange is owner-confirmed; eligible current note/transcript envelopes now become revisioned Core-owned local records and factual LifeStory projection inputs, while historical content, note attachment bytes and Voice Notes audio remain excluded |
| Notes by Prifina | Notes application source | `org.reactjs.native.prifina.lifestorynotes` | `0.1.0 (3)` | Exchange App Group `group.com.prifina.reactjs` configured in source and Apple profiles | Tested Core-handoff producer present; direct LifeStory feed writer no longer called; live insert/update/archive exchange passed on September 27, 2026 |
| Voice Notes by Prifina | Voice Notes application source | `com.valto.VoiceNotes` | `1.0 (5)` in current source | Exchange App Group `group.com.prifina.reactjs` configured in source and Apple profile | Tested Core-handoff producer present; direct LifeStory writer is no longer called; direct server client is excluded from the target; live insert/transcription/rename/archive exchange passed on September 27, 2026 |
| LifeStory Indie baseline | LifeStory Indie application source | `org.reactjs.native.prifina.lifestoryai` | `0.0.1 (74)` in current source | `group.com.prifina.reactjs` | Source display name is LifeStory Indie while technical identity and storage remain unchanged; tested read-only migration export is present; it still owns its device sources but has no active Notes or Voice Notes connection; previously mirrored records remain locally retained |
| New LifeStory | Not yet created | Not selected | Not created | Not selected | Final application milestone; create only after Core, local App Group handoff, Core-owned device sources, migration readiness and existing-app release foundations are complete |

## Repository State

- Core has substantial pre-existing uncommitted work. The App Group exchange foundation
  must avoid rewriting unrelated files and should begin with additive shared
  contract code and tests.
- Notes, Voice Notes and LifeStory reported clean working trees at the initial
  inventory point. Notes and Voice Notes now contain the intentional local
  handoff implementation changes described below.
- LifeStory and Notes use Git metadata stored outside their iCloud working
  directories. Their working paths remain legacy sources and must not be
  deleted or bulk-moved during this milestone.

## Existing Feed Compatibility

The first local contract should wrap or translate the existing Notes and Voice
Notes feed semantics rather than silently reinterpret them:

- both feeds already preserve a stable source bundle identifier;
- both use an activation time and distinguish automatic current records from
  explicitly selected historical records;
- Notes represents thread versions, archive state and attachment references;
- Voice Notes represents recording identity, transcript metadata and deletion;
- LifeStory currently imports both feeds idempotently into its own projections.

The direct LifeStory consumer is transitional. The target is:

```text
Notes / Voice Notes -> versioned local App Group handoff -> Core
Core -> authorized local projection -> new LifeStory
```

## Identified Gaps

1. The exchange App Group, signing profiles and end-to-end Notes and Voice Notes
   handoffs are verified on the owner iPhone. Longer closed-app delivery and
   performance observation remain later reliability work.
2. The existing feed names and activation records are LifeStory-specific.
3. The common envelope, acknowledgement, retry and rejection model is defined
   and implemented for the current Notes and Voice Notes flows; future data
   classes still require registry additions and semantic validation.
4. The retained `local_accepted` v1 wire value explicitly means App Group
   structural/integrity validation and is distinct from Core-owned ingestion
   and later canonical PIOS acceptance.
5. The Voice Notes repository retains its earlier direct server connection
   source as historical compatibility code, but the generated target excludes
   it and the app contains no direct connection UI.
6. New LifeStory identity, repository and entitlements do not yet exist by
   design; owner direction places its creation last in the application sequence.

## LifeStory Indie continuity preparation

The existing app now has the owner-facing source name **LifeStory Indie** while
retaining its bundle ID, iCloud container, App Group, URL scheme, target name,
snapshot path and schema. Source review on September 29 found that the current
notes-migration ZIP includes the complete JSON snapshot and only Notes-related
attachments. Because the complete snapshot includes `exportSettings`, it may
also include a configured endpoint URL and token. The current ZIP must not be
used as a Core migration package. A purpose-built sanitized export with an
explicit field allowlist, credential exclusion and integrity manifest is
required before owner-data migration. Export remains read-only and does not
trigger historical processing or contact Core.

LifeStory Indie no longer calls the Notes or Voice Notes feed readers during
launch, foreground activation, background source scans or manual Feed refresh.
Previously mirrored records are not deleted or rewritten. Legacy readers remain
in source only for compatibility tests and possible explicit recovery tooling.

## Current Decision

Use `group.com.prifina.reactjs` for App Group exchange and retain
`group.com.valto.storageinbox` as Core-private. Apple capability/profile
activation and live Notes and Voice Notes exchange passed on the owner iPhone
on September 27, 2026. Later work must keep Core-owned ingestion and any PIOS
server forwarding distinct from this verified App Group validation layer.
