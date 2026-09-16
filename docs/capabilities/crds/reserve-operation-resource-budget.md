# Reserve an operation resource budget

## Identity
- **Name:** Reserve an operation resource budget
- **Definition:** Place a bounded, expiring hold on an internal resource allowance for one authorized operation before or during execution.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Prevent concurrent or long-running work from silently exceeding the resource amount available to its approved scope.
- **Meaningful outcome:** A reservation is active, adjusted, consumed, released, expired, denied, or failed with operation binding, unit, amount, authority basis, time bounds, and remaining allowance.
- **Boundaries — includes:** reservation identity, operation/run binding, budget owner or scope, resource unit, amount, approval/policy reference, expiry, adjustment, consumption linkage, release, denial, and conflict handling.
- **Boundaries — excludes:** estimating cost, granting action authority, measuring actual usage, billing/payment holds, executing the operation, and deciding domain completion.
- **Terms and concepts:** A `resource reservation` is an internal operational hold. It is not a financial authorization unless a separate commercial realization explicitly defines it that way.

## Interaction Contract MLEs
### Maintain reservation lifecycle
- **Actor:** An authorized execution coordinator, budget service, workflow, or agent acting under an accepted request or standing policy.
- **Command / intent:** Create, adjust, consume against, release, or expire a resource reservation for one operation.
- **Current state:** The operation identity, eligible budget scope, requested amount/unit, existing reservations, authority basis, expiry policy, and current availability can be determined.
- **Policies / invariants:** A reservation does not authorize an otherwise unauthorized action; operation and budget scope remain bound; the same allowance is not silently double-reserved; adjustments are attributable; expiry and release are explicit; actual usage remains separately observed and reconciled.
- **Transition:** Validate authority and availability, create or update the bounded hold, and record its new state and remaining allowance.
- **Result:** An active, adjusted, consumed, released, expired, denied, or failed reservation.
- **Events / effects:** May permit execution to begin or continue, pause work at a boundary, or trigger owner attention when capacity is insufficient.
- **Unknowns:** Universal reservation concurrency, overcommit, extension, expiry and recovery rules are not established.

## Rules and defaults
### Rules / invariants
- Reservation is neither spend nor billing and cannot substitute for action authorization.
- Reservation changes must retain operation, authority, amount, unit and time provenance.
### Recommended defaults
- Expire unused reservations and release their remaining allowance when the bound operation reaches a terminal state.

## Unknown / unresolved
- Distributed reservation consistency and recovery after partial failure require realization-specific profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A resource reservation is an expiring operational hold between authorization and measured use, with its own lifecycle and failure states. | rule/invariant | sourced | [R01–R03 and R05–R07](../evidence/statement-provenance.md). |
