# Compile daily owner History

## Identity
- **Name:** Compile daily owner History
- **Definition:** Produce the owner-facing daily journal from structured updates, selected events, retained artifacts, and fallback traces with explicit day assignment and provenance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Create the primary readable daily account of meaningful activity without equating the full event log with the owner's narrative.
- **Meaningful outcome:** A daily History entry explains what mattered, what changed, decisions, open threads, and sources for one owner-defined day.
- **Boundaries — includes:** history-day selection, update-first inputs, selected events, gap filling, source attribution, grouping, owner relevance, open threads, and closure state.
- **Boundaries — excludes:** changing canonical events, higher-period aggregation, generic timeline browsing, and promoting every raw trace into the narrative.
- **Terms and concepts:** `daily History` is the operational anchor of owner-facing History; the event log remains the complete machine record.

## Interaction Contract MLEs
### Compile one daily History entry
- **Actor:** An authorized History compiler or owner.
- **Command / intent:** Build or revise the readable record for an owner-defined day.
- **Current state:** The day has eligible updates, events, retained sources, or an explicit no-activity state.
- **Policies / invariants:** Structured completed-work records are preferred; fallback traces fill genuine gaps; provenance remains visible; excluded material is omitted without being deleted; empty periods are represented honestly; day-cutoff rules are explicit.
- **Transition:** Select eligible evidence, group and summarize it, preserve decisions and open threads, and record source links and closure state.
- **Result:** A provenance-bearing daily History entry.
- **Events / effects:** Closed daily entries become inputs to higher-period aggregation and time-first retrieval.
- **Unknowns:** Universal day cutoff and closure/reopening policy are not established.

## Rules and defaults
### Rules / invariants
- Daily History is curated and must not claim that omitted event-log material did not occur.
### Recommended defaults
- Prefer structured completion records over raw traces when they already cover the work; use raw traces to fill genuine gaps.
- Include a concise summary, bottom line, meaningful work, decisions, open threads, and source statement when evidence supports them.

## Unknown / unresolved
- Required treatment of late-arriving events after a day is closed remains implementation-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Daily History preferably uses structured updates and selected evidence, with raw traces used for gap filling. | recommended default | sourced | [C04](../evidence/statement-provenance.md). |
