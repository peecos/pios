# Cost and resource-governance source context

This reference preserves cross-cutting context for estimating, reserving and reconciling resources used by AI-intensive, processing-heavy, background, import and generation work. It does not define a billing product or adopt one credit currency.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework and companion specifications | architecture and governance authority | explicit approval for costly actions, token/resource budgets, cost-aware service selection, measured-cost requirements, and separation of architecture from deployment cost models | one credit system, commercial pricing, billing behavior, or a shipped cost-control service |
| Historical PIOS Global at the selected revision | historical capability and interaction design | estimate, approval, reservation, spend, partial completion, final accounting, standing preferences, budget modes, and cost-aware scope options | current architecture authority, real monetary value, implementation availability, or transaction semantics |
| Restricted application evidence `RAS-01` | requirements and bounded realization evidence | token-budget fields and retrieval-budget requirements already assessed | a generic cost-estimate, reservation, spend, accounting or budget-governance realization |

## Resource-governance stages

| Stage | Reusable treatment |
|---|---|
| Estimate | independent capability producing a bounded forecast |
| Approval | reuse governed proposal, execution policy, explicit owner request, action intent, or standing rule according to scope |
| Reservation | independent capability holding an internal allowance for one operation |
| Usage measurement | reuse metric-observation recording or realization-specific metering |
| Partial completion | preserve in the underlying work/background-operation lifecycle |
| Final accounting | independent reconciliation capability over estimates, reservations, observations and completed scope |
| Billing/payment | separate commercial domain outside this tranche |

## Cross-cutting boundaries

- A cost estimate is information for a decision, not permission to execute.
- A reservation is a temporary internal hold, not actual use or a payment authorization.
- Actual consumption should be captured through attributable observations and remain distinguishable from estimated and reserved quantities.
- Cost approval reuses existing governance capabilities; it does not need a parallel proposal system.
- A budget-limited operation may stop partially and still produce a valid bounded result. Domain completion state remains in the work object or run.
- Most-relevant-first, sample-first, map-only and processing-depth choices are execution-scope or ordering profiles rather than standalone capabilities.
- Credits can remain an internal comparison unit. Monetary billing, invoices, taxes, refunds and payment processing require separate commercial capabilities and authority.

## Documentation and realization reconciliation

The historical cost-governance model describes estimate, approval, reservation, spend, partial/full completion and final accounting as a product control loop. Applying the symmetric MLE test separates estimation, reservation and reconciliation. Approval, standing preferences, actual measurement and partial execution reuse existing proposal, policy, rule, metric and execution capabilities.

Current PIOS requires explicit approval for costly guarded actions, logs token budgets for retrieval, tracks real infrastructure cost before adding optional services, and keeps deployment cost choices outside the generic architecture. These principles support the reusable contracts but do not establish a universal credit system.

The selected restricted application documents token budgets for retrieval, but the bounded file-name and admitted-document review did not identify a generic cost-estimate, reservation, spend-accounting or budget-governance implementation. No tests, deployment or production behavior are claimed.
