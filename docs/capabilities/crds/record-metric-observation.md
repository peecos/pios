# Record a metric observation

## Identity
- **Name:** Record a metric observation
- **Definition:** Preserve one attributable, time-scoped observed value against an existing measurement definition.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Record evidence of reality over time without silently converting an observation into a target decision, profile assertion, or aggregate conclusion.
- **Meaningful outcome:** One accepted, rejected, corrected, or superseded observation is recorded with metric identity, time, value, source, provenance, and quality state.
- **Boundaries — includes:** metric validation, observation time, numeric or declared value form, source, provenance, quality status, correction, supersession, and acceptance result.
- **Boundaries — excludes:** defining the metric, defining a target, deciding target attainment, aggregating a series, inferring a pattern, and confirming profile truth.
- **Terms and concepts:** A `metric observation` is one measured value or state at a declared time. It is evidence, not interpretation.

## Interaction Contract MLEs
### Record one observation
- **Actor:** An authorized owner, connector, sensor, application, or delegated agent.
- **Command / intent:** Record a value observed for a known measurement definition.
- **Current state:** The measurement definition, owner scope, source identity, observation time, and current duplicate/correction state can be determined.
- **Policies / invariants:** Source and time are retained; value conforms to the declared metric semantics; duplicate or corrected observations are reconciled explicitly; observations do not silently establish achievement, patterns, or profile assertions.
- **Transition:** Validate identity, scope, value, time, and provenance; append or explicitly supersede an observation; emit its disposition.
- **Result:** A durable observation or a reasoned rejection/conflict result.
- **Events / effects:** May feed progress views, summaries, target evaluation, observed-pattern analysis, or profile evidence through separate capabilities.
- **Unknowns:** Universal duplicate windows, quality grades, correction rules, and source precedence are not established.

## Rules and defaults
### Rules / invariants
- Observation time and record time must remain distinguishable when they differ.
- Corrections must preserve the prior observation or an equivalent audit trail.
### Recommended defaults
- Record source type, source reference, unit or value form, confidence or quality, and ingestion time when available.

## Unknown / unresolved
- Domain-specific validation and aggregation semantics belong in implementation or capability profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A metric observation is a time-scoped evidence record separate from its measurement definition, target, and later interpretation. | rule/invariant | sourced | [F08–F10](../evidence/statement-provenance.md). |
