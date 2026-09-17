# Estimate operation resource cost

## Identity
- **Name:** Estimate operation resource cost
- **Definition:** Produce an attributable forecast of the resources or internal cost units likely required for a bounded operation and scope.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give an owner or authorized policy evaluator enough cost information to choose whether and how deeply an operation should proceed.
- **Meaningful outcome:** A current estimate identifies the operation, scope, unit, range or class, assumptions, method/version, uncertainty, validity window, and available lower-cost scope choices.
- **Boundaries — includes:** operation and input scope, depth or effort class, estimated quantity or range, resource/cost unit, assumptions, uncertainty, estimate method/version, expiry, alternatives, and failure to estimate.
- **Boundaries — excludes:** approving the operation, reserving capacity or credits, recording actual consumption, billing, payment, selecting a provider, and executing the operation.
- **Terms and concepts:** An estimate may use a `schema.org/QuantitativeValue` or `schema.org/MonetaryAmount` where applicable. An internal credit is a comparison/control unit unless an adopted commercial profile gives it monetary meaning.

## Interaction Contract MLEs
### Estimate bounded operation cost
- **Actor:** The owner, an authorized planner, policy evaluator, workflow, or agent preparing a cost-governed operation.
- **Command / intent:** Estimate the likely resource cost for a declared operation and scope before execution.
- **Current state:** The intended operation, input scope, depth/options, applicable unit, available estimating method, and relevant constraints can be determined.
- **Policies / invariants:** The estimate remains distinct from approval, reservation, charge, and actual usage; uncertainty and assumptions are visible; false precision is avoided; alternative scopes do not become selected without a separate decision; materially stale estimates are not represented as current.
- **Transition:** Evaluate the declared scope using the current method and produce a versioned range, class, or bounded quantity with assumptions and validity.
- **Result:** A usable estimate, an explicit cannot-estimate result, or a requirement for additional scope information.
- **Events / effects:** May inform a proposal, execution policy, budget reservation, scope reduction, deferral, or owner-attention item.
- **Unknowns:** Universal units, confidence bands, expiry periods and acceptable estimation error are not established.

## Rules and defaults
### Rules / invariants
- An estimate must not be presented as actual consumption or permission to execute.
- The estimated operation and scope must be identifiable and reproducible enough to compare with later usage.
### Recommended defaults
- Prefer honest ranges or qualitative classes over unsupported exact values.

## Unknown / unresolved
- Domain-specific estimating methods and conversion among time, tokens, compute, credits, energy and money require profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Cost estimation is a distinct pre-execution outcome that supports informed scope and approval decisions without granting execution authority. | rule/invariant | sourced | [R01–R04](../evidence/statement-provenance.md). |
