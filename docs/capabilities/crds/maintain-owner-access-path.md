# Maintain an owner access path

## Identity
- **Name:** Maintain an owner access path
- **Definition:** Register, govern, verify, prioritize, suspend, and retire a route through which the owner can access or steer a PIOS system.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve trustworthy day-to-day, secondary, administrative, recovery, or fallback access without binding PIOS to one interface product or device.
- **Meaningful outcome:** An owner access path has a stable identity, declared role, endpoint/interface, authentication and trust requirements, supported operations, availability state, priority, verification evidence, and lifecycle status.
- **Boundaries — includes:** path registration, owner/system binding, primary/secondary/master/fallback role, supported operation classes, required assurance, device or endpoint reference, priority, health/last verification, suspension, replacement, and retirement.
- **Boundaries — excludes:** designing the interface, granting domain permissions, performing an action, maintaining an external source connector, storing credentials in the path definition, and treating interface availability as proof that Core is healthy.
- **Terms and concepts:** An `owner access path` is the governed route to an interface or endpoint. The interface remains replaceable, and the path's role does not enlarge the owner's or client's underlying permissions.

## Interaction Contract MLEs
### Maintain access-path lifecycle
- **Actor:** The owner or an authorized system administrator acting within owner policy.
- **Command / intent:** Register, verify, reprioritize, suspend, restore, replace, or retire an owner access path.
- **Current state:** The owner and PIOS system, interface/endpoint identity, path role, supported operations, authentication requirements, current availability, verification evidence, and authority can be determined.
- **Policies / invariants:** The path does not become canonical Core; stronger administrative or recovery roles require commensurate assurance; path registration does not grant undeclared domain authority; fallback paths remain independently testable; unavailable or stale verification is shown honestly; secrets remain in governed credential stores.
- **Transition:** Validate the path identity and role, perform the required bounded verification, record status and evidence, and update routing priority or lifecycle state.
- **Result:** An active, degraded, suspended, replaced, retired, or rejected owner access path.
- **Events / effects:** May change interface routing or raise owner attention while leaving domain records and permissions unchanged.
- **Unknowns:** Universal assurance levels, health intervals, failover rules, offline guarantees, and break-glass profiles are not established.

## Rules and defaults
### Rules / invariants
- No single interface implementation may become the only undocumented route to owner control or recovery.
- Access-path state and underlying authorization remain separate; a reachable endpoint does not imply permission for every operation.
### Recommended defaults
- Maintain at least one independently verifiable fallback for deployments whose primary interface can fail without making Core unavailable.

## Unknown / unresolved
- Platform-specific authentication, offline behavior, recovery custody, and failover testing require deployment profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Owner access paths have distinct operating roles and remain replaceable interfaces over governed PIOS capabilities rather than canonical state. | rule/invariant | sourced | [N08–N10](../evidence/statement-provenance.md). |
