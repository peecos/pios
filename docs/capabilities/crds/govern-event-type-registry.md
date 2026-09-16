# Govern an event-type registry

## Identity
- **Name:** Govern an event-type registry
- **Definition:** Maintain the owner-scoped definitions that determine allowed event families, names, schemas, emitters, lifecycle transitions, evidence, approval requirements, and projection effects.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep the canonical event spine interpretable and prevent uncontrolled event-name or lifecycle drift.
- **Meaningful outcome:** An event type is registered, revised, deprecated, or rejected with a versioned contract and governance provenance.
- **Boundaries — includes:** family, name, schema version, required references, allowed emitters, source of truth, lifecycle semantics, evidence, projection effects, approval needs, versioning, and deprecation.
- **Boundaries — excludes:** recording individual events, storing physical event files, computing projections, and treating example event names as automatically registered.
- **Terms and concepts:** An `event-type registry` governs event semantics; it is not the event log itself.

## Interaction Contract MLEs
### Maintain event-type definition
- **Actor:** An authorized event-governance owner, steward, or system architect.
- **Command / intent:** Register, revise, or deprecate an event type.
- **Current state:** A proposed type definition and its intended family, emitters, and effects exist.
- **Policies / invariants:** Names are versioned and attributable; required fields and refs are explicit; emitters are constrained; state-machine transitions identify valid actors and evidence; incompatible changes do not silently reinterpret prior events.
- **Transition:** Evaluate the proposal and persist an accepted, revised, deprecated, or rejected registry entry.
- **Result:** A governed event-type definition and version history.
- **Events / effects:** Conforming emitters may record events of the accepted type; projections may adopt the declared effects.
- **Unknowns:** Universal compatibility rules for schema evolution are not established.

## Rules and defaults
### Rules / invariants
- Recording an event type that is not registered must not silently establish its semantics.
- Registry changes must not mutate historical event payloads.
### Recommended defaults
- Group types into stable families and use understandable composable names.

## Unknown / unresolved
- Emergency admission of previously unseen external event types requires a later policy.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Event-type governance defines family, schema, emitters, lifecycle, evidence, approval, and projection effects independently from event recording. | rule/invariant | sourced | [C12](../evidence/statement-provenance.md). |
