# Maintain owner-authored profile knowledge

## Identity
- **Name:** Maintain owner-authored profile knowledge
- **Definition:** Preserve and revise the owner's explicit self-description as owner-authored living knowledge.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let the owner state what matters about themselves without conflating self-description with inferred observations.
- **Meaningful outcome:** Current owner-authored profile knowledge and its revision history are available for authorized use.
- **Boundaries — includes:** create, edit, organize, version, archive, and context-link owner-authored self-description.
- **Boundaries — excludes:** inferred profile assertions, observed patterns, automatic conversion to profile truth, and public sharing policy.
- **Terms and concepts:** `owner-authored profile knowledge` is self-description controlled directly by the profile subject.

## Interaction Contract MLEs
### Revise owner-authored profile knowledge
- **Actor:** The owner.
- **Command / intent:** Create or change an explicit self-description.
- **Current state:** A profile knowledge object may exist with a current revision.
- **Policies / invariants:** Owner edits take precedence over inference; changes are versioned; the content remains distinguishable from observed/evidence-backed assertions; conversion to another knowledge class requires a governed proposal.
- **Transition:** Apply the authorized change and append revision/provenance evidence.
- **Result:** Updated owner-authored profile knowledge with prior state recoverable.
- **Events / effects:** Authorized retrieval may use the current version; proposed interpretations may reference it as evidence.
- **Unknowns:** A universal category set is not required by current PIOS.

## Rules and defaults
### Rules / invariants
- Owner-authored profile content must not automatically become observed profile truth.
### Recommended defaults
- Prefer natural-language living knowledge over compulsory form fields.

## Unknown / unresolved
- Public operational realization is not confirmed.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Owner-authored and observed profile knowledge remain distinct. | rule/invariant | sourced | [K09](../evidence/statement-provenance.md). |
