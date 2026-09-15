# Allocate retained content to a context

## Identity

- **Name:** Allocate retained content to a context
- **Definition:** Grant, inspect, and revoke bounded eligibility for a named context to use governed retained content.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Keep possession of content separate from permission to use it in an AI, agent, role, or other consuming context.
- **Meaningful outcome:** An inspectable authorization relation states whether a named context may consider the target content.
- **Boundaries — includes:** grant, target, context, scope, revocation, inspection, and authorization provenance.
- **Boundaries — excludes:** retention, processing, retrieval, disclosure, inference, and general account permissions.
- **Terms and concepts:** `allocation` means eligibility for a named context, not copying, moving, guaranteed retrieval, or disclosure.

## Interaction Contract MLEs

### Change context allocation

- **Actor:** The owner or explicitly delegated authority.
- **Command / intent:** Grant or revoke a context's eligibility to use a retained target.
- **Current state:** The target, context, and current allocation state are determinable.
- **Policies / invariants:** No allocation is assumed; scope is explicit; revocation affects future selection; authority and change provenance are recorded; current allocations are inspectable.
- **Transition:** Validate authority and scope, create or end the allocation relation, and record the new state.
- **Result:** The requested allocation state is established or rejected with reason.
- **Events / effects:** Retrieval and other consumers may use the allocation as an eligibility constraint.
- **Unknowns:** A universal context-kind taxonomy is intentionally not fixed here.

## Rules and defaults

### Rules / invariants

- Retained content is unallocated unless a governing policy explicitly establishes otherwise.
- Allocation is necessary eligibility, not sufficient reason for actual use.
- Current allocations must be inspectable and removable by the authority that governs them.

### Recommended defaults

- Prefer target- and context-specific grants over broad implicit grants.

## Unknown / unresolved

- Time-bounded and purpose-bounded grant semantics require later profile work.

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| No allocation is assumed; allocation is inspectable and removable. | rule/invariant | sourced | [Pilot provenance P03](../evidence/statement-provenance.md). |
| Allocation does not itself retrieve content. | reasonable inference | derived | MLE separation from governed retrieval. |
