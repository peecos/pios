# Evaluate an observed pattern lifecycle

## Identity
- **Name:** Evaluate an observed pattern lifecycle
- **Definition:** Reassess an observed pattern's evidence, recurrence, strength, and temporal status and preserve the resulting lifecycle snapshot.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep pattern observations current and explainable as supporting evidence accumulates, changes, or stops.
- **Meaningful outcome:** The pattern has a current evaluated status, strength, evidence-eligibility result, and timestamped snapshot without silently becoming a proposal or profile assertion.
- **Boundaries — includes:** evidence recount, recurrence and interval assessment, time-window comparison, strength, status transition, minimum-evidence eligibility, snapshot, rationale, and stale/weakening handling.
- **Boundaries — excludes:** initial pattern detection, proposal creation or decision, profile mutation, owner-facing presentation, and one specific statistical model or scheduler.
- **Terms and concepts:** Pattern lifecycle states may include `emerging`, `stable`, `weakening`, and `inactive`; their exact calculations are implementation-profile specific.

## Interaction Contract MLEs
### Refresh pattern lifecycle state
- **Actor:** An authorized recurring analysis process or owner-invoked evaluator.
- **Command / intent:** Re-evaluate an existing observed pattern against its current eligible evidence and time window.
- **Current state:** An observed pattern, linked evidence, prior lifecycle state, applicable thresholds, and evaluation policy exist.
- **Policies / invariants:** Evaluation remains owner-scoped and reproducible from recorded inputs; eligibility and status are not profile truth; absence of recent evidence may weaken or inactivate rather than erase history; proposal eligibility does not itself create a proposal.
- **Transition:** Recount and assess evidence, calculate the declared measures, record rationale, update lifecycle fields, and append a timestamped snapshot.
- **Result:** An evaluated emerging, stable, weakening, inactive, unchanged, or failed lifecycle result with evidence and snapshot references.
- **Events / effects:** A stable eligible result may invoke governed proposal creation separately; an informative owner-facing projection may be produced separately.
- **Unknowns:** Universal decay windows, strength formulae, and stable/weakening thresholds are not established.

## Rules and defaults
### Rules / invariants
- Only a stable pattern that satisfies the declared evidence gate may become eligible to generate a proposal.
- Lifecycle evaluation must preserve prior snapshots and must not delete weakening or inactive history.
- A status change must not directly create or modify a confirmed profile assertion.
### Recommended defaults
- Prefer periodic evaluation over noisy per-event status mutation.
- The historical application model used five evidence items as the default surfacing/proposal-eligibility threshold; implementations should declare and justify their threshold.

## Unknown / unresolved
- Owner dismissal, suppression, or “not meaningful” feedback semantics are not yet defined as a reusable lifecycle contract.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Pattern status is periodically reassessed from evidence and remains separate from proposal and profile lifecycles. | rule/invariant | sourced | [E04–E06](../evidence/statement-provenance.md). |
