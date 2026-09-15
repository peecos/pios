# Navigate time-indexed owner History

## Identity
- **Name:** Navigate time-indexed owner History
- **Definition:** Traverse owner-facing History across time levels and source-linked entries while preserving provenance and the distinction between projection and canonical records.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let an owner or authorized agent move from broad periods to specific updates, events, and originals to reconstruct sequence and change.
- **Meaningful outcome:** Relevant historical context is located through an explainable time path with source identity intact.
- **Boundaries — includes:** year-to-day drill-down, period summaries, filtering, source labels, linked updates/events/originals, and time-first retrieval rationale.
- **Boundaries — excludes:** creating canonical events, compiling summaries, treating the timeline UI as a second truth store, and automatically promoting insights to profile truth.
- **Terms and concepts:** Time-indexed History is a retrieval surface over linked records, not the complete event log itself.

## Interaction Contract MLEs
### Traverse History by time
- **Actor:** An authorized owner, interface, or retrieval agent.
- **Command / intent:** Locate relevant historical context for a time, sequence, change, decision, or completed-work question.
- **Current state:** History summaries or entries and their source links exist.
- **Policies / invariants:** Start at an appropriate summary level; narrow only as needed; preserve source/native/imported distinctions; do not represent derived insight as canonical fact; access controls apply at every linked level.
- **Transition:** Select a time range, traverse summary levels, filter and inspect linked entries, and follow provenance to canonical records or originals when needed.
- **Result:** A bounded set of relevant historical records and an explainable navigation path.
- **Events / effects:** May supply context to retrieval, review, reflection, or decision capabilities.
- **Unknowns:** Universal search and ranking behavior is not established.

## Rules and defaults
### Rules / invariants
- Timeline and History views must not duplicate or replace canonical source records.
- Source provenance must remain available through drill-down.
### Recommended defaults
- Begin summary-first and expand toward daily entries, updates, events, and originals only as required.

## Unknown / unresolved
- Cross-source deduplication and imported-history admission require separate capability contracts.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Time-indexed History supports progressive navigation from broad periods to events and originals without becoming a second truth store. | rule/invariant | sourced | [C06](../evidence/statement-provenance.md). |
