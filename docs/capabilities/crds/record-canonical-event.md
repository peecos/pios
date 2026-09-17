# Record a canonical event

## Identity
- **Name:** Record a canonical event
- **Definition:** Append an idempotent, attributable, time-aware record of something that happened, was captured, inferred, corrected, or produced.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve a cross-source machine-readable event spine without making presentation surfaces canonical.
- **Meaningful outcome:** A valid event is durably recorded once with stable identity, type, actor, time, logical references, and required provenance.
- **Boundaries — includes:** envelope validation, event identity, idempotency, event and recorded time, actor, type, source/original links when required, append semantics, and registry conformance.
- **Boundaries — excludes:** owner-facing narration, mutable work state, source-object retention, and physical storage-adapter details.
- **Terms and concepts:** The `event log` is canonical event truth; `History` is a readable projection derived from selected evidence.

## Interaction Contract MLEs
### Append an event
- **Actor:** An authorized source, connector, application, agent, or Core component.
- **Command / intent:** Record one qualifying occurrence in the canonical event spine.
- **Current state:** An occurrence and enough required envelope information exist.
- **Policies / invariants:** Event identity is stable; duplicate retries do not overwrite or multiply the event; source time and recorded time remain distinct; required actor/type provenance is present; physical location is not part of conceptual identity.
- **Transition:** Validate the envelope and append the event through an idempotent write primitive.
- **Result:** One durable canonical event with a logical reference.
- **Events / effects:** Indexes, projections, updates, History, or downstream processing may consume the event.
- **Unknowns:** Event-family-specific required fields remain registry-defined.

## Rules and defaults
### Rules / invariants
- Canonical event records are append-oriented and must not be silently overwritten.
- Presentation or summary projections must retain links to contributing events.
### Recommended defaults
- Use time-sortable globally unique identifiers and preserve source-original timestamps when available.

## Unknown / unresolved
- Universal event retention and compaction policy is not established.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Events form the canonical append-oriented machine-readable spine and distinguish source time from record time. | rule/invariant | sourced | [C01](../evidence/statement-provenance.md). |
