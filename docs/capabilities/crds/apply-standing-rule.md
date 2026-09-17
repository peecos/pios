# Apply a standing rule

## Identity

- **Name:** Apply a standing rule
- **Definition:** Evaluate an active standing rule against a specific situation and produce a logged authorized action, governed fallback, or reasoned no-action result.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Reuse confirmed authority in matching situations while preserving scope, confidence, auditability, and owner control.
- **Meaningful outcome:** One candidate situation receives an attributable rule decision and any authorized downstream action.
- **Boundaries — includes:** rule selection, condition match, scope and confidence evaluation, authority validation, action invocation, fallback, and execution evidence.
- **Boundaries — excludes:** creating or changing the rule, defining the domain action, and silently expanding authority from outcomes.
- **Terms and concepts:** A `rule application` is one evaluation and outcome; a `fallback proposal` requests authority when the standing rule is insufficient.

## Interaction Contract MLEs

### Evaluate and apply a rule

- **Actor:** A governed execution process.
- **Command / intent:** Evaluate an active rule for a candidate situation and act only within its authority.
- **Current state:** An active rule and candidate facts exist.
- **Policies / invariants:** Scope and confidence are evaluated before action; insufficient confidence falls back to a proposal; every rule fire is attributable; the downstream capability enforces its own constraints.
- **Transition:** Match the rule, verify authority and confidence, invoke the permitted action or fallback, and record the outcome.
- **Result:** A logged authorized action, a proposal fallback, or a reasoned no-action result.
- **Events / effects:** An authorized downstream capability may change domain state.
- **Unknowns:** Whether every non-match requires durable logging depends on risk and volume.

## Rules and defaults

### Rules / invariants

- Rule application must not exceed the confirmed condition, action, or scope.
- Every rule fire is logged.
- Low confidence is not treated as confirmed authority.

### Recommended defaults

- Record material fallback and override reasons.

## Unknown / unresolved

- See [U04](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Rule fires are logged and insufficient confidence falls back. | rule/invariant | sourced | [Pilot provenance P08](../evidence/statement-provenance.md). |
