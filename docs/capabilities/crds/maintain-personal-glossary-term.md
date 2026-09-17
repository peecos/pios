# Maintain a personal glossary term

## Identity
- **Name:** Maintain a personal glossary term
- **Definition:** Establish and revise an owner-specific term with stable identity, meaning, aliases, relationships, and lifecycle.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give people and agents a shared, durable interpretation of vocabulary whose local meaning matters.
- **Meaningful outcome:** A governed term can be resolved and interpreted consistently while preserving aliases and history.
- **Boundaries — includes:** candidate review, definition, aliases, relationships, status, revision, merge, and deprecation.
- **Boundaries — excludes:** general dictionary capture, item labeling, automatic acceptance of extracted terms, and access control.
- **Terms and concepts:** `term` maps where useful to `DefinedTerm` from Schema.org; personal meaning remains authoritative over an external vocabulary mapping.

## Interaction Contract MLEs
### Establish or revise a term
- **Actor:** The owner or an explicitly governed knowledge-maintenance process.
- **Command / intent:** Create, correct, merge, or deprecate a personal glossary term.
- **Current state:** A candidate or existing term and its evidence are available.
- **Policies / invariants:** Stable identity and provenance are preserved; aliases do not silently create separate meanings; model-detected candidates require governed promotion; external standards are mappings, not masters.
- **Transition:** Validate authority and duplicates, apply the lifecycle change, retain prior identity/revision links, and update relationships.
- **Result:** A traceable candidate, active, merged, or deprecated term, or a reasoned rejection.
- **Events / effects:** Retrieval and knowledge compilation may use active terms and aliases.
- **Unknowns:** Universal merge-conflict resolution is not established.

## Rules and defaults
### Rules / invariants
- Do not promote every mention into a durable term.
- Preserve owner-specific nuance and source evidence.
### Recommended defaults
- Start with stable IDs, plain-language definitions, aliases, status, and relationships.

## Unknown / unresolved
- No public operational realization is confirmed.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Personal glossary terms preserve local meaning and lifecycle. | rule/invariant | sourced | [K01–K03](../evidence/statement-provenance.md). |
