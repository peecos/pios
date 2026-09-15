# Manage AI-assisted label vocabulary

## Identity
- **Name:** Manage AI-assisted label vocabulary
- **Definition:** Govern the owner-scoped vocabulary of non-authoritative labels available for machine-assisted classification.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Prevent unbounded ad hoc machine labels while retaining useful soft semantics separately from confirmed taxonomy.
- **Meaningful outcome:** The active assisted-label vocabulary and each label's provenance/lifecycle are explicit and governable.
- **Boundaries — includes:** propose, deduplicate, confirm where required, rename, disable, deprecate, merge, and inspect vocabulary entries.
- **Boundaries — excludes:** assigning a label to an object, promoting it to an owner-confirmed organizing label, and using it in retrieval.
- **Terms and concepts:** `AI-assisted label` is a non-authoritative machine-usable classification cue.

## Interaction Contract MLEs
### Change assisted-label vocabulary
- **Actor:** An authorized owner or governed enrichment process.
- **Command / intent:** Propose or change an assisted-label definition or lifecycle state.
- **Current state:** Existing vocabulary, candidate label, provenance, and duplicate context are available.
- **Policies / invariants:** Only active known labels may be assigned; new labels are deduplicated and governed; assisted labels remain distinct from owner-confirmed labels; disabling prevents future automatic assignment.
- **Transition:** Validate authority and duplicates, record the proposed or approved change, and preserve lifecycle history.
- **Result:** A traceable active, disabled, deprecated, merged, rejected, or pending label definition.
- **Events / effects:** Active vocabulary constrains assisted-label assignment.
- **Unknowns:** Whether direct owner creation is allowed is profile-specific and not universalized here.

## Rules and defaults
### Rules / invariants
- Do not invent a new label per object when no governed vocabulary entry exists.
### Recommended defaults
- Keep the vocabulary owner-scoped and small enough to remain understandable.

## Unknown / unresolved
- Public operational realization is not confirmed.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Assisted labels use a controlled vocabulary distinct from owner taxonomy. | rule/invariant | sourced | [K04](../evidence/statement-provenance.md). |
