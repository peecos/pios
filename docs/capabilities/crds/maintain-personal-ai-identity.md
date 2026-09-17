# Maintain a personal AI identity

## Identity
- **Name:** Maintain a personal AI identity
- **Definition:** Create and revise the owner-authored presentation identity through which a personal AI represents itself to its owner.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give a personal AI a stable, owner-governed identity without inventing separate memory, world truth, authority, or runtime identity.
- **Meaningful outcome:** A versioned personal-AI identity is active, attributable, and available to authorized communication and interface surfaces.
- **Boundaries — includes:** display name, short owner-authored description, presentation assets, relational framing, language, identity status, provenance, and revision history.
- **Boundaries — excludes:** the owner's profile, personal-AI interaction preferences, execution policy, model/provider selection, runtime agent roles, independent long-term memory, and factual claims about the world.
- **Terms and concepts:** `personal AI identity` is a behavior and presentation identity; it is not a separate store of owner information.

## Interaction Contract MLEs
### Create or revise personal AI identity
- **Actor:** The owner or an authorized setup process presenting changes for owner control.
- **Command / intent:** Establish or revise how the personal AI is named and presented.
- **Current state:** An owner/Core context and either no identity, a provisional identity, or an existing versioned identity exist.
- **Policies / invariants:** Owner authorship is preserved; defaults and generated suggestions are identified as provisional; revisions are traceable; identity fields do not grant execution authority or create a separate memory store.
- **Transition:** Validate the proposed identity fields, record provenance and owner decision, create a new version, and activate or reject it.
- **Result:** An active, provisional, rejected, or superseded personal-AI identity version.
- **Events / effects:** May update authorized interface presentation and sender identity without changing owner knowledge or runtime permissions.
- **Unknowns:** Cross-implementation identity portability and asset formats are not established.

## Rules and defaults
### Rules / invariants
- Personal-AI identity and owner profile must remain distinct.
- A generated name, image, or description remains provisional until accepted under the applicable owner-governance profile.
- Identity changes must not silently change behavior preferences or execution authority.
### Recommended defaults
- Keep the initial identity small and editable rather than requiring complete characterization.

## Unknown / unresolved
- Whether one owner may maintain several concurrently active personal-AI identities requires a separate profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A personal AI may have an owner-authored presentation identity while remaining separate from runtime roles, owner profile, memory, and authority. | rule/invariant | sourced | [D05](../evidence/statement-provenance.md). |
