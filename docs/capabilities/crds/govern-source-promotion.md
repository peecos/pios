# Govern source promotion

## Identity
- **Name:** Govern source promotion
- **Definition:** Control when retained source material advances from preservation through analysis, mapping, enrichment, and owner-facing History eligibility.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Prevent raw or weakly understood material from silently becoming canonical knowledge, retrieval context, profile implications, or owner-facing History.
- **Meaningful outcome:** A source or bounded subset has an explicit promotion state, evidence, authority basis, and allowed next processing scope.
- **Boundaries — includes:** parked, analyzed, mapped, enriched, and History-included dispositions; baseline-versus-deep processing distinction; confidence; cost/depth boundary; exclusion; and promotion provenance.
- **Boundaries — excludes:** retaining the original, executing every mapping/enrichment step, deciding domain-specific proposals, and authorizing an ingestion batch.
- **Terms and concepts:** `promotion` changes how source material may participate in Core; it does not erase source identity.

## Interaction Contract MLEs
### Change source-promotion state
- **Actor:** An authorized owner, source-governance agent, or intake workflow acting within policy.
- **Command / intent:** Advance, hold, exclude, or reverse a source-material promotion state.
- **Current state:** Retained source material and its current disposition, evidence, and applicable authority exist.
- **Policies / invariants:** Basic mapping and deeper enrichment remain distinct; promotion is staged and attributable; source provenance remains intact; History inclusion is explicit; depth must not silently exceed authority or budget.
- **Transition:** Evaluate evidence and authority, then record the new promotion state and permitted next actions.
- **Result:** A durable source-promotion disposition with rationale and scope.
- **Events / effects:** May enable mapping, enrichment, retrieval eligibility, proposals, summaries, or History compilation.
- **Unknowns:** Universal confidence and materiality thresholds are not established.

## Rules and defaults
### Rules / invariants
- Imported material must not silently become profile truth or public/shared information.
- Whole sources must not be bulk-promoted into owner-facing History merely because they were imported.
### Recommended defaults
- Permit baseline identity and timestamp mapping more readily than inferential or costly enrichment.

## Unknown / unresolved
- Source-specific trust and automation profiles require separate governance definitions.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Source material advances through explicit stages, with deeper processing and History inclusion separately governed. | rule/invariant | sourced | [C10](../evidence/statement-provenance.md). |
