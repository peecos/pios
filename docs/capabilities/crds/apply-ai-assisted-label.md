# Apply an AI-assisted label

## Identity
- **Name:** Apply an AI-assisted label
- **Definition:** Attach an attributable, confidence-bearing, non-authoritative classification cue to an eligible governed object.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Enrich filtering, retrieval, and pattern analysis without presenting machine interpretation as owner-confirmed truth.
- **Meaningful outcome:** An active or archived assignment links a known assisted label to a target with provenance.
- **Boundaries — includes:** target eligibility, active vocabulary check, confidence, rationale, provenance, assignment, archive, and visibility state.
- **Boundaries — excludes:** creating label vocabulary, promoting labels, changing owner-confirmed taxonomy, and deciding retrieval policy.
- **Terms and concepts:** An `assignment` is derived metadata and remains distinguishable from confirmed labels.

## Interaction Contract MLEs
### Apply or archive an assisted label
- **Actor:** An authorized enrichment process or owner action.
- **Command / intent:** Add or remove a soft-semantic label on a target.
- **Current state:** The target exists; a governed assisted label and current assignment state are known.
- **Policies / invariants:** Label and target are owner-scoped; only active vocabulary entries are assigned; provenance is retained; removal archives rather than rewrites history; promotion requires a separate proposal and confirmation.
- **Transition:** Validate scope, create an active assignment or archive the active assignment, and record evidence.
- **Result:** An attributable active/archived assignment or reasoned rejection.
- **Events / effects:** Opted-in retrieval or analysis may use active assignments.
- **Unknowns:** Universal confidence thresholds are not established.

## Rules and defaults
### Rules / invariants
- Assisted assignments never silently become owner-confirmed labels.
### Recommended defaults
- Exclude assisted labels from filtering and retrieval unless the surface intentionally opts in.

## Unknown / unresolved
- Public operational realization is not confirmed.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Assisted labels are non-authoritative and separately governed. | rule/invariant | sourced | [K04](../evidence/statement-provenance.md). |
| Exclusion is the safe default. | recommended default | sourced | [K05](../evidence/statement-provenance.md). |
