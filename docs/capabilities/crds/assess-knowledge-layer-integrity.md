# Assess knowledge-layer integrity

## Identity
- **Name:** Assess knowledge-layer integrity
- **Definition:** Evaluate a bounded knowledge collection for structural, evidentiary, semantic, lifecycle, and safety defects without silently rewriting important knowledge.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Keep owner knowledge navigable, source-linked, current, and safe by producing inspectable maintenance findings and follow-up work.
- **Meaningful outcome:** An assessment identifies the checked scope, rules/profile, evidence, defects, severity, affected objects, proposed responses, review tasks, and unresolved limitations.
- **Boundaries — includes:** scope manifest, broken/orphan links, missing summaries or indexes, stale/duplicate concepts, missing or weak source references, unresolved contradictions, unconfirmed labels, visibility/sensitivity problems, review status, severity, and attributable findings.
- **Boundaries — excludes:** silently editing knowledge, deciding every proposal, merging duplicates, deleting sources, changing visibility, rebuilding indexes, and performing generic software-code linting.
- **Terms and concepts:** A finding may be represented as a `schema.org/Review`, `schema.org/Action`, or structured quality record linked to the affected `schema.org/CreativeWork` or knowledge object.

## Interaction Contract MLEs
### Assess a knowledge scope
- **Actor:** The owner, an authorized knowledge-maintenance process, or a review agent.
- **Command / intent:** Check a declared knowledge scope against a named integrity and safety profile.
- **Current state:** The target objects, links/indexes, source references, lifecycle states, visibility/sensitivity metadata, assessment profile/version, and authority can be determined.
- **Policies / invariants:** Findings preserve evidence and checked-time context; inferred defects remain distinguishable from confirmed errors; material changes require their own capability and authority; important knowledge is not silently rewritten; unavailable checks and coverage gaps remain visible; generated indexes are treated as rebuildable projections.
- **Transition:** Evaluate the bounded scope, record findings and severity, link affected objects and evidence, and create proposals or review tasks where appropriate.
- **Result:** A completed, partial, failed, or blocked integrity assessment with actionable findings and coverage evidence.
- **Events / effects:** May create review tasks, owner-attention items, proposals, source-link corrections, index rebuild requests, or concept-lifecycle evaluations through separate capabilities.
- **Unknowns:** Universal lint profiles, severity scales, scheduling, false-positive handling and auto-fix boundaries are not established.

## Rules and defaults
### Rules / invariants
- Integrity assessment must not silently rewrite, delete, merge, promote, or expose knowledge.
- Each finding must identify its checked scope, rule/profile, evidence and assessment time.
### Recommended defaults
- Produce flags, proposals and review tasks before applying material knowledge changes.

## Unknown / unresolved
- Which low-risk mechanical corrections may be standing-authorized requires a separate governance profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Knowledge integrity assessment produces evidence-linked structural, evidence, meaning and safety findings while material repair remains separately governed. | rule/invariant | sourced | [S11–S15](../evidence/statement-provenance.md). |
