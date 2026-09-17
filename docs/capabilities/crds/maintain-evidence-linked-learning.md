# Maintain evidence-linked Learning

## Identity

- **Name:** Maintain evidence-linked Learning
- **Definition:** Preserve a revisable lesson, strategy, correction, preference, warning, or working method that may help future reasoning.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Turn eligible evidence and interpretation into a durable candidate lesson while keeping later recall and behavior change separately governed.
- **Meaningful outcome:** A Learning record exists with evidence, scope, confidence, provenance, lifecycle state, and revision history sufficient for later review or recall.
- **Boundaries — includes:** subject and evidence references, source events, lesson statement, originator or model, confidence, applicable context, proposal/confirmation/rejection/supersession state, review timing, and revision provenance.
- **Boundaries — excludes:** recording raw observations, detecting patterns, preserving Meaning, changing a profile assertion, creating a standing rule, modifying an agent definition or workflow, executing an adaptation, and selecting retrieval context.
- **Terms and concepts:** `Learning` is an evidence-linked proposal for future reasoning. A confirmed Learning remains revisable knowledge rather than self-executing policy.

## Interaction Contract MLEs

### Preserve or revise Learning

- **Actor:** The owner or an authorized learning process operating within declared scope.
- **Command / intent:** Record, confirm, revise, reject, or supersede a lesson that may be useful later.
- **Current state:** Eligible evidence and any relevant observation, pattern, Meaning, or prior Learning are available with provenance.
- **Policies / invariants:** Machine-generated Learning begins as proposed; the record identifies its evidence, context, confidence, and origin; frequency is not preference; confirmation does not rewrite behavior, policy, skills, workflow, or profile truth; revisions preserve history.
- **Transition:** Evaluate the lesson against its evidence, record the bounded statement and applicable context, assign lifecycle state, and link revisions or supersession.
- **Result:** A proposed, owner-confirmed, rejected, superseded, or reasoned-not-recorded Learning outcome.
- **Events / effects:** Confirmed Learning may be recalled into an authorized context or support a separate proposal, rule, preference, workflow, or agent-definition change.
- **Unknowns:** Universal evidence sufficiency, expiry, recall ranking, conflict resolution, and adaptation thresholds are not established.

## Rules and defaults

### Rules / invariants

- Learning must remain traceable to evidence and distinguishable from observation and Meaning.
- A Learning record must not grant itself behavioral or execution authority.
- Conflicting or outdated Learning must be revised, disputed, or superseded rather than silently overwritten.

### Recommended defaults

- State where the lesson applies, where it may not apply, and when it should be reviewed.
- Prefer owner confirmation before a Learning materially affects future recommendations.

## Unknown / unresolved

- See [U94–U97](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Learning is an evidence-linked, revisable lesson for future reasoning and remains separate from behavior adaptation and standing authority. | rule/invariant | sourced | [T02–T08](../evidence/statement-provenance.md). |
