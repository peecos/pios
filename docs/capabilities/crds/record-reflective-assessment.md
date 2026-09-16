# Record a reflective assessment

## Identity
- **Name:** Record a reflective assessment
- **Definition:** Preserve an attributable interpretation of evidence that includes judgment, open loops, residue, uncertainty, and recommendations.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Capture what evidence may mean and what deserves attention without presenting interpretation as neutral summary or confirmed truth.
- **Meaningful outcome:** A reflection exists with scope, evidence references, interpretation, uncertainty, open loops, residue, recommendations, authorship, and time context.
- **Boundaries — includes:** subject or period, source evidence, interpretive findings, uncertainty, tensions, unresolved residue, recommendations, provenance, revision, and supersession.
- **Boundaries — excludes:** neutral summarization, observed-pattern detection, confirming profile assertions, deciding proposals, executing recommendations, and changing reviewed source state.
- **Terms and concepts:** A `reflection` is interpretive review material. A `summary` compresses known material; a reflection adds judgment and possible implications.

## Interaction Contract MLEs
### Preserve a reflection
- **Actor:** The owner, an authorized reviewer, or an interpretive agent operating within declared scope.
- **Command / intent:** Record an interpretation of a bounded evidence set or experience.
- **Current state:** The subject, evidence, relevant prior reflections, and authority to interpret are available.
- **Policies / invariants:** Interpretation is labelled as interpretation; source evidence and omissions remain traceable; uncertainty and disagreement are preserved; recommendations do not become authority or confirmed truth; later revision does not erase the prior assessment.
- **Transition:** Examine the evidence, distinguish observations from interpretation, record judgments, open loops, residue, recommendations, and confidence, and persist the assessment.
- **Result:** A versioned reflective assessment or a reasoned insufficient-evidence result.
- **Events / effects:** May inform a structured review, proposal, observed-pattern analysis, knowledge revision, or owner attention item without performing those outcomes.
- **Unknowns:** Universal confidence scales, reflection scopes, and expiry or review rules are not established.

## Rules and defaults
### Rules / invariants
- A reflection must not be represented as a neutral summary or verified fact.
- Recommendations require separate authority before changing canonical state or causing external action.
### Recommended defaults
- State the evidence window, material omissions, confidence, open loops, and whether the reflection is owner-authored or machine-assisted.

## Unknown / unresolved
- The minimum evidence and review needed before a reflection may support a proposal varies by domain and risk.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Reflection is an interpretive, attributable assessment with judgment and unresolved residue, distinct from neutral summary and downstream decisions. | rule/invariant | sourced | [H05–H07](../evidence/statement-provenance.md). |
