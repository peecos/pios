# Detect an observed pattern

## Identity
- **Name:** Detect an observed pattern
- **Definition:** Identify a recurring relationship or behavior from multiple governed evidence items and preserve it as a non-assertive observed pattern.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Create a statistically grounded intermediate object between individual signals and governed proposals or profile assertions.
- **Meaningful outcome:** An emerging observed pattern or a reasoned no-pattern result is recorded with evidence, scope, time range, and detection rationale.
- **Boundaries — includes:** evidence selection, owner scope, pattern identity, segment or category, recurrence, initial counts, time range, rationale, source links, duplicate handling, and creation threshold.
- **Boundaries — excludes:** declaring profile truth, deciding a proposal, evaluating later pattern strength/status, generating raw source signals, and a particular inspection screen or detection model.
- **Terms and concepts:** An `observed pattern` describes recurrence evidenced across time; it is an observation, not an assertion about the owner.

## Interaction Contract MLEs
### Detect a recurring pattern
- **Actor:** An authorized pattern-analysis process or owner-invoked analysis.
- **Command / intent:** Evaluate eligible evidence for a recurring behavior or relationship worth preserving as an observed pattern.
- **Current state:** Multiple owner-scoped evidence items, applicable time/scope boundaries, current pattern identities, and a declared creation threshold exist.
- **Policies / invariants:** Evidence and provenance are retained; one weak signal does not become a pattern; source bias and time range remain visible; duplicate or overlapping candidates are reconciled explicitly; created patterns remain non-authoritative observations.
- **Transition:** Analyze recurrence, compare existing patterns, apply the creation threshold, and create or link an emerging pattern when warranted.
- **Result:** A created or matched emerging pattern with evidence and rationale, or a no-pattern/insufficient-evidence/failure result.
- **Events / effects:** May schedule lifecycle evaluation and make the pattern eligible for owner inspection without creating a proposal or profile assertion.
- **Unknowns:** Universal detection methods, similarity rules, and evidence weighting are not established.

## Rules and defaults
### Rules / invariants
- A pattern must remain distinguishable from its evidence, a proposal, and a confirmed profile assertion.
- Pattern creation requires a declared multi-item evidence threshold and cannot rely on an unsupported single observation.
### Recommended defaults
- The historical application model used three evidence items as the initial creation threshold; implementations should declare and justify their threshold.

## Unknown / unresolved
- Cross-source evidence normalization and confidence calibration remain implementation-profile specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Observed patterns arise from multiple evidence items as non-assertive intermediate objects before proposals or profile truth. | rule/invariant | sourced | [E01–E03](../evidence/statement-provenance.md). |
