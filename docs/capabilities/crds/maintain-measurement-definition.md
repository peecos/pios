# Maintain a measurement definition

## Identity
- **Name:** Maintain a measurement definition
- **Definition:** Create and revise the governed definition used to observe a quantity or condition, including its unit and collection method.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve how reality is to be measured independently from desired success and individual observations.
- **Meaningful outcome:** A measurement definition exists with identity, subject or target context, unit or value form, tracking method, lifecycle state, and provenance.
- **Boundaries — includes:** creation, revision, activation or retirement, unit, value form, tracking method, subject linkage, provenance, and interpretation notes.
- **Boundaries — excludes:** defining a target, recording a measured value, deciding whether success was achieved, generating summaries, and rendering charts.
- **Terms and concepts:** A `measurement definition` describes what and how to measure. A `metric observation` records what was measured at a particular time.

## Interaction Contract MLEs
### Maintain measurement-definition lifecycle
- **Actor:** An authorized owner, analyst, planner, or delegated agent.
- **Command / intent:** Define or revise how an outcome-relevant quantity or condition is measured.
- **Current state:** The subject, intended interpretation, and any current measurement definition are known.
- **Policies / invariants:** Unit and value semantics are explicit; definition changes are versioned or time-bounded when they affect comparability; method does not fabricate observations; target and metric remain separately identifiable.
- **Transition:** Validate the measurement semantics and scope, persist the definition, and record lifecycle and provenance.
- **Result:** A current measurement definition suitable for later observations and review.
- **Events / effects:** May enable metric observation, aggregation, target evaluation, or display without performing those outcomes.
- **Unknowns:** Universal unit registries, validation rules, and definition-change compatibility are not established.

## Rules and defaults
### Rules / invariants
- A measurement definition must not be treated as observed reality.
- Material changes that break comparability must remain visible across observations.
### Recommended defaults
- Prefer an explicit unit or value type, tracking method, subject, expected cadence, and interpretation notes.

## Unknown / unresolved
- Cross-implementation unit normalization and semantic compatibility require a later interoperability profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A metric definition specifies how reality is tracked and remains separate from a success target and from recorded values. | rule/invariant | sourced | [F07–F08](../evidence/statement-provenance.md). |
