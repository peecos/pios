# Device continuity and reading source context

This reference preserves cross-cutting context for device-local caching, deliberate offline content, and personal reading queues. It does not make a device technology, shared container, browser extension, or Reader interface mandatory.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework and integration specification | architecture and interoperability authority | Core-app responsibility, device-cache state classes, identity/integrity/freshness requirements, shared-storage limits, offline authorization, revocation and reconciliation boundaries | a shipped mobile client, one cache technology, one eviction policy, or production availability |
| Historical PIOS Global at the selected revision | historical design and realization evidence | mobile-first interface intent and a reading workflow over retained captured articles | current architecture authority, universal reading-completion rules, or durable saved-state behavior |
| Restricted application evidence `RAS-01` | bounded static realization evidence | a Reader view over selected stored items, unread/read and saved views, source links, generated summaries and topic grouping | complete tag-based admission, durable portable reading state, offline device caching, tests, deployment, or production behavior |

## State separation

| State | Meaning | Governing capability |
|---|---|---|
| Accepted canonical content | Durable source or governed representation in Core | source retention and domain capability |
| Recent-content cache | Opportunistic authorized local copy | maintain an authorized device-local content cache |
| Selected offline content | Deliberately retained local copy for an offline window | maintain selected content for offline access |
| Pending capture or edit | Unaccepted work that may be the only copy | reconcile pending capture or another pending-work contract |
| Reading-queue state | Owner's unread/read/saved/archive relationship to retained content | manage a personal reading queue |

## Cross-cutting boundaries

- Cache reuse, deliberate offline retention and pending-work preservation are different outcomes and must not share destructive cleanup assumptions.
- A device cache or synchronized folder does not become canonical Core, a backup, or an authorization system.
- Shared-container membership is a technical trust boundary. It cannot create confidentiality among members that can read the same plaintext bytes.
- Offline access is limited to previously authorized content and declared offline operations. It cannot represent a fresh server policy check.
- Reader, feed, archive, typography, scroll behavior, app header and topic screens are audience or realization patterns over retained content and reading-queue state.
- AI-generated reading topics reuse contextual classification or assisted-label capabilities. Generated summaries and PDF exports reuse derivation and retention capabilities.

## Documentation and realization reconciliation

Current PIOS distinguishes recent cache, selected offline content, and pending captures or edits. It requires owner/Core identity, logical references, revision or integrity evidence, freshness and access boundaries; it also states that cache clearing does not delete canonical content and offline access cannot promise immediate revocation of already disclosed bytes.

The historical Reader model describes retained web-clipped articles admitted through a reading-intent label and presented through feed, unread, saved, archive, topic and settings views. The selected restricted application has a reachable static Reader path, but its behavior does not fully match that description: it selects retained items by capture origin rather than confirming the declared reading-intent label, treats a cleared inbox state as read state, stores saved identifiers only in local browser state, and does not establish durable topic membership in the reviewed path. These are realization limitations, not reusable CRD rules.

No complete restricted realization of the current PIOS device-cache or deliberate-offline contracts was confirmed.
