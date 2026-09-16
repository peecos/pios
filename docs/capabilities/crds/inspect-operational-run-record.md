# Inspect an operational run record

## Identity
- **Name:** Inspect an operational run record
- **Definition:** Retrieve and explain the canonical evidence for one workflow run, agent task, processing job, or import operation without changing its state.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let an owner or operator understand what ran, why, under whose authority, what changed, and what succeeded or failed.
- **Meaningful outcome:** A bounded operational explanation links the run's state, timing, inputs, outputs, errors, retries, actors, rules, and evidence.
- **Boundaries — includes:** run identity, source capability, status history, trigger, actor, authority, timing, inputs/outputs, retries, errors, linked updates/events, and evidence references.
- **Boundaries — excludes:** executing or retrying the run, changing canonical truth, broad data-health analysis, and client-side reconstruction of missing evidence.
- **Terms and concepts:** An `operational run record` is canonical or source-linked evidence; an inspector is a read projection over it.

## Interaction Contract MLEs
### Inspect one run
- **Actor:** An authorized owner, operator, auditor, or diagnostic agent.
- **Command / intent:** Explain one operational run and its outcome.
- **Current state:** A run identifier or bounded query and accessible source records exist.
- **Policies / invariants:** Inspection is read-only; displayed claims trace to source records; missing evidence is identified rather than inferred; sensitive details follow access policy; the inspection surface does not compute new canonical truth.
- **Transition:** No canonical run state changes; the capability assembles a bounded evidence projection.
- **Result:** An inspectable operational run explanation with links to authoritative records.
- **Events / effects:** May support incident review, retry authorization, remediation, or owner updates through separate capabilities.
- **Unknowns:** Minimum retention and redaction rules differ by run class and sensitivity.

## Rules and defaults
### Rules / invariants
- A missing log or evidence item must not be presented as successful execution.
- Inspection must not itself retry, cancel, or remediate the run.
### Recommended defaults
- Show status transitions, duration, trigger, authority, outputs, errors, and related events together.

## Unknown / unresolved
- Cross-system correlation identifiers and log-retention periods remain implementation-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Operational inspection reads run and import records to explain state and evidence without computing new truth. | rule/invariant | sourced | [C13](../evidence/statement-provenance.md). |
