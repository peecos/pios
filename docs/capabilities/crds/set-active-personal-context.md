# Set active personal context

## Identity
- **Name:** Set active personal context
- **Definition:** Establish the currently applicable combination of owner context dimensions for filtering, prioritization, inheritance, and assistance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make current situational context explicit and time-bounded while preserving how it was selected or inferred.
- **Meaningful outcome:** An active-context snapshot is established, changed, expired, cleared, or rejected with source and scope evidence.
- **Boundaries — includes:** active Roles, operating Modes, location, with-whom relations, source type, confidence where inferred, time bounds, scope, supersession, and inheritance policy.
- **Boundaries — excludes:** defining Role or Mode vocabulary, permanently attaching context to an object, granting access, rewriting historical context, and task working-mode requirements.
- **Terms and concepts:** `active personal context` is a temporary state; objects may inherit it through a separate contextual-classification event.

## Interaction Contract MLEs
### Establish or change active context
- **Actor:** The owner, an authorized source, or a context agent operating under the applicable confirmation policy.
- **Command / intent:** Set, add, remove, expire, or clear one or more active context dimensions.
- **Current state:** An owner/Core context, eligible context values, current active snapshot, source evidence, and applicable time/scope policy exist.
- **Policies / invariants:** Multiple dimensions and values may coexist; explicit, inherited, inferred, and owner-corrected states remain distinguishable; caller-supplied values are not automatically owner-confirmed; incomplete context does not block capture.
- **Transition:** Validate the context values and source, record a new snapshot or change event, supersede or expire prior values as required, and expose the active state.
- **Result:** An active, partially active, cleared, expired, rejected, or superseded context snapshot.
- **Events / effects:** May influence filtering, prioritization, retrieval, scheduling, and later context inheritance without granting access.
- **Unknowns:** Universal automatic expiry, conflict resolution, and inheritance windows are not established.

## Rules and defaults
### Rules / invariants
- Active context must not become an access-control boundary.
- Inherited or inferred context must retain its source and confidence and remain correctable.
- Changing active context must not rewrite context already recorded for past events or objects.
### Recommended defaults
- Allow empty or partial active context and avoid blocking capture for missing dimensions.

## Unknown / unresolved
- Which active-context dimensions should synchronize across devices and applications requires a deployment profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Active personal context is a temporary, multi-dimensional, provenance-bearing state that may influence later inheritance without becoming access control. | rule/invariant | sourced | [D15](../evidence/statement-provenance.md). |
