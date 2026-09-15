# Assemble governed retrieval context

## Identity

- **Name:** Assemble governed retrieval context
- **Definition:** Select and package relevant governed information for a requesting operation under explicit scope, policy, budget, and provenance constraints.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Make context selection governable and explainable independently of the model or consumer that uses it.
- **Meaningful outcome:** A bounded context package and receipt identify what was selected and why.
- **Boundaries — includes:** request purpose, active scope, authorization filters, candidate retrieval, ranking, limits, source references, graceful degradation, and receipt.
- **Boundaries — excludes:** answer generation, source-truth mutation, consolidation production, allocation changes, and provider routing.
- **Terms and concepts:** `context package` is selected information for a downstream consumer; `context receipt` records selection provenance and policy.

## Interaction Contract MLEs

### Assemble context

- **Actor:** An authorized application, agent, or workflow preparing a governed operation.
- **Command / intent:** Assemble relevant context for a stated purpose and scope.
- **Current state:** Governed sources and policy are available; the request has identity and purpose.
- **Policies / invariants:** Filter by authority before ranking; respect scope and exclusions; enforce bounded cost/size; preserve source references; record policy and rationale; missing optional sources do not cause fabricated context.
- **Transition:** Resolve policy, identify eligible candidates, rank and select them, package the result, and create the receipt.
- **Result:** A bounded context package and selection receipt, or a reasoned failure.
- **Events / effects:** A downstream generation or execution capability may consume the package.
- **Unknowns:** Universal ranking, tier count, and receipt-retention duration are not established.

## Rules and defaults

### Rules / invariants

- Context assembly remains separable from model generation.
- Ineligible content is excluded before semantic ranking or model exposure.
- Selected content remains attributable to source references.

### Recommended defaults

- Prefer deterministic ordering for equal inputs and policy versions.
- Prefer direct recent context before broader derived recall when both are eligible.

## Unknown / unresolved

- See [U02](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Retrieval assembly is separate from generation. | capability purpose | sourced | [Pilot provenance P04](../evidence/statement-provenance.md). |
| Selection is bounded and explainable. | rule/invariant | sourced | [Pilot provenance P05](../evidence/statement-provenance.md). |
| Tier count and ranking formula are realization choices. | reasonable inference | derived | Historical detail is narrower than the current PIOS retrieval model. |
