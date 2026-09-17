# Manage an organizing label

## Identity
- **Name:** Manage an organizing label
- **Definition:** Establish and maintain an owner-confirmed label used to group, filter, and navigate governed information.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Provide consistent owner-defined organization without turning every label into a meaning object or access rule.
- **Meaningful outcome:** A stable label and its aliases/lifecycle are available for explicit assignment and filtering.
- **Boundaries — includes:** create, rename, alias, merge, describe, categorize, deprecate, and inspect usage.
- **Boundaries — excludes:** glossary referent meaning, AI-assisted assignments, Role/Mode context, access control, and applying a label to a particular item.
- **Terms and concepts:** `label` is an owner-confirmed organizational annotation; it may map to `keywords` where interoperating with Schema.org.

## Interaction Contract MLEs
### Maintain a label
- **Actor:** The owner or explicitly authorized curator.
- **Command / intent:** Create or change an organizing label.
- **Current state:** A candidate or existing label and possible duplicates are known.
- **Policies / invariants:** Owner confirmation is preserved; labels do not silently become glossary terms or access controls; aliases and merges retain traceability.
- **Transition:** Check authority and duplicates, apply the requested lifecycle change, and preserve prior references.
- **Result:** An active, merged, deprecated, or rejected label change.
- **Events / effects:** Filtering and organization surfaces may use active labels.
- **Unknowns:** Assignment behavior is a separate candidate capability for a later tranche.

## Rules and defaults
### Rules / invariants
- Labels and glossary meaning objects remain distinct.
### Recommended defaults
- Prefer a small understandable vocabulary and deduplicate before adding a new label.

## Unknown / unresolved
- No public operational realization is confirmed.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Organizing labels are distinct from named meaning objects. | rule/invariant | sourced | [K02](../evidence/statement-provenance.md). |
