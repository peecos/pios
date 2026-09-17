# Manage a personal reading queue

## Identity
- **Name:** Manage a personal reading queue
- **Definition:** Organize eligible retained reading material through unread, saved, read, archived, and removed states without changing its canonical source content.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Help the owner intentionally defer, consume, revisit, and complete reading material drawn from governed sources.
- **Meaningful outcome:** A reading item has source-linked queue membership, owner-visible reading state, ordering/context metadata, and an attributable state transition.
- **Boundaries — includes:** admitting an eligible retained item, unread/read state, saved-for-later state, archive/removal, ordering, source link, progress or completion evidence when supported, and source-aware filtering.
- **Boundaries — excludes:** capturing the original, storing or editing source content, rendering a particular reader interface, generating summaries, AI topic clustering, assigning generic labels, exporting a PDF, and deleting the canonical source.
- **Terms and concepts:** A reading item references a retained `schema.org/Article`, `schema.org/DigitalDocument`, or other `schema.org/CreativeWork`; a completed reading interaction may be represented as a `schema.org/ReadAction`.

## Interaction Contract MLEs
### Change reading-queue state
- **Actor:** The owner or an authorized process applying an explicit reading rule.
- **Command / intent:** Add, order, mark read or unread, save for later, archive, restore, or remove an eligible reading item.
- **Current state:** The retained source reference, owner, queue membership, current reading/save state, provenance, and authority can be determined.
- **Policies / invariants:** Queue state does not alter or delete canonical source content; automatic state changes are attributable and reversible where policy permits; source references remain available; AI grouping or summaries do not silently change reading state; removal from the queue is not source erasure.
- **Transition:** Validate eligibility and authority, update the queue membership or reading state, and record the resulting status and provenance.
- **Result:** An unread, read, saved, archived, restored, removed, or rejected reading-queue item.
- **Events / effects:** May update reading views, reminders, progress summaries, or contextual recommendations through separate capabilities.
- **Unknowns:** Universal read-completion thresholds, ordering policy, progress model, retention, and cross-device synchronization are not established.

## Rules and defaults
### Rules / invariants
- Reading-state transitions must not mutate the retained source or imply that generated summaries and classifications are source truth.
- Queue removal, archive, read completion, and source deletion remain separate outcomes.
### Recommended defaults
- Require an explicit owner action or declared rule to admit material to the queue; do not infer completed reading from brief visibility alone.

## Unknown / unresolved
- Reading progress, automatic completion, duplicate-source handling and durable saved-state portability require profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A personal reading queue manages source-linked reading state while content storage, rendering, AI organization and derived exports remain separate concerns. | rule/invariant | sourced | [Q06–Q11](../evidence/statement-provenance.md). |
