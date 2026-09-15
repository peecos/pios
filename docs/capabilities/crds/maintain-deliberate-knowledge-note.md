# Maintain a deliberate knowledge note

## Identity
- **Name:** Maintain a deliberate knowledge note
- **Definition:** Create and revise an owner-chosen, durable knowledge object while preserving identity, links, provenance, and revision history.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let the owner deliberately preserve knowledge without implying obligation or silently rewriting history.
- **Meaningful outcome:** A current knowledge note exists with reconstructable revisions and governed relationships.
- **Boundaries — includes:** create, edit, title/content revision, archive, restore, source links, and relationships.
- **Boundaries — excludes:** raw-source retention, chat history, attached task/reminder behavior, automatic profile promotion, and retrieval.
- **Terms and concepts:** A `knowledge note` may map to `CreativeWork` from Schema.org while retaining PIOS-specific provenance and lifecycle.

## Interaction Contract MLEs
### Create or revise a note
- **Actor:** The owner or an explicitly authorized knowledge-maintenance process.
- **Command / intent:** Preserve or change deliberate knowledge.
- **Current state:** New content or an existing note and its current revision are available.
- **Policies / invariants:** Owner scope and stable identity are preserved; meaningful edits are versioned; automated changes retain actor/source provenance; linked capabilities do not replace the note's identity.
- **Transition:** Validate authority, create a note or append a revision, update governed links, and record the result.
- **Result:** A current note with reconstructable history, or a reasoned failure.
- **Events / effects:** Knowledge indexes and retrieval projections may be refreshed.
- **Unknowns:** Universal merge and collaborative-edit semantics are not established.

## Rules and defaults
### Rules / invariants
- Silent content edits are prohibited.
- Capturing conversation as knowledge requires owner action, instruction, or established standing authority.
### Recommended defaults
- Keep capture low-commitment; add structure when it becomes useful.

## Unknown / unresolved
- Assignment of structured capabilities to notes remains separately documented as a realization pattern.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Notes are deliberate durable captures with version history. | rule/invariant | sourced | [K07–K08](../evidence/statement-provenance.md). |
