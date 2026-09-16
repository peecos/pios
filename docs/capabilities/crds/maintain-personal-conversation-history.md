# Maintain personal conversation history

## Identity
- **Name:** Maintain personal conversation history
- **Definition:** Preserve a continuous, source-aware record of the owner's conversations across sessions, contexts, interfaces, and admitted imported sources.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep conversational continuity available without making chat the canonical home of work, knowledge, approvals, results, or owner-facing History.
- **Meaningful outcome:** An eligible conversation occurrence is represented in one inspectable history with stable identity, actor and source provenance, time, context links, correction/deletion state, and continuity across interface views.
- **Boundaries — includes:** history identity, entry membership, chronological order, actor and source provenance, original and recorded time, native/imported distinction, context links, correction records, soft hiding or retention state, and source-aware filtering.
- **Boundaries — excludes:** generating a response, recording a generic collaboration message outside the owner's personal history, creating notes or profile truth, assembling retrieval context, consolidating conversations, and producing curated owner-facing History.
- **Terms and concepts:** `personal conversation history` is a logical continuity record. Its physical representation may use retained message originals and canonical events rather than a dedicated application table. It may map participating exchanges to `schema.org/Conversation` and individual communications to `schema.org/Message`.

## Interaction Contract MLEs
### Maintain conversation continuity
- **Actor:** The owner or an authorized communication, import, or Core intake process.
- **Command / intent:** Add, correct, hide, restore, or source-link an eligible conversation occurrence in the owner's continuing history.
- **Current state:** The owner, source interaction, actor identity, source and recorded times, origin, context links, retention state, and applicable authority can be determined.
- **Policies / invariants:** Conversation sources and actor identities remain visible; channels and threads organize or filter continuity without silently creating unrelated histories; corrections append attributable state rather than rewriting evidence; imported material is not represented as native; chat does not become canonical task, knowledge, result, approval, or History truth.
- **Transition:** Validate identity, origin, chronology and authority, then record the occurrence or a correction/hiding disposition with stable references.
- **Result:** A source-aware conversation-history entry, corrected/hiding state, or reasoned rejection.
- **Events / effects:** May support search, retrieval, consolidation, context classification, event recording, or explicit capture into another canonical object through separate capabilities.
- **Unknowns:** Universal exchange granularity, cross-source ordering, edit/redaction rules, retention, and federation profiles are not established.

## Rules and defaults
### Rules / invariants
- Conversation history must preserve source and actor provenance across native and imported interactions.
- A conversation-history entry must not silently become a note, profile assertion, task, approval, standing rule, or curated History entry.
### Recommended defaults
- Present one continuous owner history with source-aware views unless an implementation profile requires separately governed histories.

## Unknown / unresolved
- Cross-harness identity, ordering, export, redaction, and retention require an interoperability profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Personal conversation continuity is source-aware, append-oriented, and separate from canonical work, knowledge, retrieval derivatives, and owner-facing History. | rule/invariant | sourced | [N01–N07](../evidence/statement-provenance.md). |
