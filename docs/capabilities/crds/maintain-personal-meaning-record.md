# Maintain a personal Meaning record

## Identity

- **Name:** Maintain a personal Meaning record
- **Definition:** Preserve a contextual, revisable interpretation of why governed evidence matters to the owner.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Let the owner retain significance and interpretation without converting observations, patterns, or generated analysis directly into profile truth, policy, or permission.
- **Meaningful outcome:** A source-linked Meaning record exists with a clear subject, statement, context, provenance, confidence, lifecycle status, and revision relationship.
- **Boundaries — includes:** subject and evidence references, source events, contextual interpretation, originator or model, confidence, applicable scope, proposal/confirmation/rejection/supersession state, review timing, revision, and provenance.
- **Boundaries — excludes:** recording the underlying observation, detecting a pattern, preserving a broad reflective assessment, creating a durable lesson, changing profile truth, granting authority, changing retrieval policy, and adapting agent or workflow behavior.
- **Terms and concepts:** `Meaning` answers why a source, event, decision, or experience matters to the owner. It is a Knowledge object, not a permission or an automatic statement of fact.

## Interaction Contract MLEs

### Preserve or revise Meaning

- **Actor:** The owner or an authorized knowledge process operating within declared scope.
- **Command / intent:** Record, confirm, revise, reject, or supersede an interpretation of why identified evidence matters.
- **Current state:** The subject and eligible evidence are identifiable; relevant prior Meaning records and the actor's authority are available.
- **Policies / invariants:** Meaning remains linked to evidence and context; machine-generated Meaning starts non-authoritative; confidence and origin remain visible; confirmation does not grant permission or silently change Cotton, profile truth, rules, skills, agent behavior, policy, or ranking; revisions preserve prior states.
- **Transition:** Validate subject and evidence references, record the interpretation and scope, assign its provenance and lifecycle state, and link any revision or supersession relationship.
- **Result:** A proposed, owner-confirmed, rejected, superseded, or reasoned-not-recorded Meaning outcome.
- **Events / effects:** Confirmed Meaning may become eligible for governed retrieval, reflection, review, or Learning creation without performing those later outcomes.
- **Unknowns:** Universal confirmation thresholds, confidence scales, review intervals, and retrieval-weight treatment are not established.

## Rules and defaults

### Rules / invariants

- Observation, pattern, Meaning, profile assertion, Learning, and authority must remain distinguishable.
- Context and Meaning must never be treated as authorization.
- A generated interpretation must not silently become owner-confirmed Meaning.

### Recommended defaults

- Preserve the narrowest useful subject and evidence scope.
- Record material counter-evidence, uncertainty, and a review time when significance may change.

## Unknown / unresolved

- See [U94–U96](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Meaning is a contextual, revisable, evidence-linked Knowledge object whose confirmation remains separate from authority and downstream adaptation. | rule/invariant | sourced | [T01–T08](../evidence/statement-provenance.md). |
