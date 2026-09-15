# Detect a candidate glossary term

## Identity
- **Name:** Detect a candidate glossary term
- **Definition:** Identify a potentially owner-relevant term or alias in governed content and preserve it as reviewable evidence without accepting it as canonical meaning.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Surface useful vocabulary discoveries while keeping inference separate from owner-confirmed meaning.
- **Meaningful outcome:** A candidate, recognized occurrence, or ignored result is recorded with source evidence and confidence.
- **Boundaries — includes:** source-scoped detection, normalization, known-term matching, candidate evidence, confidence, ignore handling, and audit.
- **Boundaries — excludes:** confirming a glossary term, changing source content, globally resolving identity, and presenting a specific highlight UI.
- **Terms and concepts:** A candidate may map to a `DefinedTerm`; recognition is an evidence claim, not identity truth.

## Interaction Contract MLEs
### Detect term candidates
- **Actor:** An authorized owner or enrichment process.
- **Command / intent:** Examine a governed source for terms relevant to the personal glossary.
- **Current state:** Source content and the applicable glossary/ignore context are available.
- **Policies / invariants:** Source provenance is retained; ignored candidates are respected; known aliases resolve without creating duplicates; new candidates remain unconfirmed; uncertain identity matches are not silently globalized.
- **Transition:** Analyze the source, normalize candidates, compare known terms and exclusions, and record candidates or occurrences with evidence.
- **Result:** Evidence-linked candidates/occurrences or a reasoned no-result/failure.
- **Events / effects:** A new candidate may trigger the governed proposal capability.
- **Unknowns:** Detection model and threshold are realization choices.

## Rules and defaults
### Rules / invariants
- Detection must not silently create accepted glossary meaning.
### Recommended defaults
- Deduplicate against active terms and aliases before proposing a new term.

## Unknown / unresolved
- Public implementation evidence is absent.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Detected names remain candidates until governed confirmation. | rule/invariant | sourced | [K03](../evidence/statement-provenance.md). |
