# Synchronize an agent definition to runtime

## Identity
- **Name:** Synchronize an agent definition to runtime
- **Definition:** Reconcile a selected canonical agent-definition version with one or more declared runtime targets and preserve verifiable synchronization state.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep deployed agent behavior traceable to canonical owner-governed definitions without treating runtime copies as primary truth.
- **Meaningful outcome:** Each target runtime has a current, pending, failed, intentionally divergent, or rolled-back synchronization result linked to exact source and deployed versions.
- **Boundaries — includes:** source definition version, target runtime identity, rendered artifacts, compatibility checks, planned differences, deployment, verification, failure, retry, rollback, status, and evidence.
- **Boundaries — excludes:** authoring the definition, operating the runtime, changing owner memory, granting permissions outside the definition process, and deploying unrelated application code.
- **Terms and concepts:** A `runtime target` is the process, machine, provider, service, or configuration surface that consumes an agent definition; it is not the canonical definition itself.

## Interaction Contract MLEs
### Synchronize one definition version
- **Actor:** An authorized coordinator, deployment process, or owner.
- **Command / intent:** Apply a canonical agent-definition version to declared runtime targets.
- **Current state:** The approved source version, target identities, current deployed versions, expected transformations, compatibility state, and authority are known.
- **Policies / invariants:** Source remains canonical; generated or adapted copies identify their source version and transformation; secrets are referenced rather than copied into portable definitions; partial failure is explicit; successful write without verification is not reported as current; rollback target is retained.
- **Transition:** Compare source and target state, render or transfer approved artifacts, apply them, verify the effective version, and record per-target results or rollback.
- **Result:** Verified current, pending, failed, intentionally different, or rolled-back synchronization state for each target.
- **Events / effects:** May update owner-facing agent status or block incompatible runtime activation without modifying the source definition.
- **Unknowns:** Universal rendering, signing, secret-binding, compatibility, and runtime-verification protocols are not established.

## Rules and defaults
### Rules / invariants
- Runtime copies must not silently override the canonical agent definition.
- Synchronization status must identify the source version and affected target.
### Recommended defaults
- Verify effective runtime configuration after application and preserve a reversible prior target version.

## Unknown / unresolved
- Multi-runtime conflict resolution and intentional-divergence governance require deployment-specific profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Canonical agent definitions and runtime copies are separate, and synchronization requires explicit target, version, state, history, and rollback evidence. | rule/invariant | sourced | [J03–J04](../evidence/statement-provenance.md). |
