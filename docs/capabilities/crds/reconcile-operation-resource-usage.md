# Reconcile operation resource usage

## Identity
- **Name:** Reconcile operation resource usage
- **Definition:** Compare attributable actual resource consumption with an operation's estimate, reservation, budget, and completed scope, then preserve the final disposition.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Close the resource-governance loop so the owner can see what was consumed, what completed, what remains, and whether further authority is required.
- **Meaningful outcome:** An operation has a final or interim resource account with actual usage, estimate/reservation variance, released or exceeded allowance, completed scope, remaining scope, and any next-decision requirement.
- **Boundaries — includes:** usage-observation references, estimate and reservation comparison, variance, partial/full completion linkage, remaining allowance, reservation release, remaining-work estimate, exception state, and final accounting record.
- **Boundaries — excludes:** measuring raw usage, estimating before execution, reserving resources, billing/invoicing, deciding whether to continue, and determining the domain quality of the result.
- **Terms and concepts:** Actual usage values may reuse a governed metric observation expressed as a `schema.org/QuantitativeValue`; reconciliation links those observations to the operation and its prior resource commitments.

## Interaction Contract MLEs
### Reconcile resource outcome
- **Actor:** An authorized execution coordinator, accounting process, workflow, or agent closing or checkpointing an operation.
- **Command / intent:** Reconcile actual resource use and completed scope against the applicable estimate, reservation, and budget.
- **Current state:** The operation/run, usage observations, estimate and reservation references where present, completion state, produced outputs, and authority context can be determined.
- **Policies / invariants:** Actual use remains distinguishable from estimates and reservations; partial completion is represented honestly; unused reservation is released; overruns and missing measurements are visible; accounting does not claim billing settlement; remaining work is not executed without its own authority.
- **Transition:** Aggregate eligible usage evidence, calculate or record variance, release or close reservations, associate completed and remaining scope, and persist the reconciliation state.
- **Result:** A reconciled final or interim resource account, or an explicit incomplete/conflicted accounting result.
- **Events / effects:** May update usage History, inform future estimates, create an attention item, or support a proposal for additional budget or scope.
- **Unknowns:** Universal usage aggregation, late-arriving measurement, currency conversion, adjustment and dispute rules are not established.

## Rules and defaults
### Rules / invariants
- Final accounting must preserve actual usage separately from forecast and reserved amounts.
- Partial completion must identify completed scope, remaining possible work, and the resource boundary that stopped or constrained execution.
### Recommended defaults
- Reconcile at terminal completion and at any budget-driven pause that requires an owner decision.

## Unknown / unresolved
- Commercial charging, refunds, taxation and invoice reconciliation remain outside this CRD.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Resource reconciliation closes the estimate/reservation/usage loop and preserves partial completion and remaining-work context without becoming billing. | rule/invariant | sourced | [R01–R03 and R08–R11](../evidence/statement-provenance.md). |
