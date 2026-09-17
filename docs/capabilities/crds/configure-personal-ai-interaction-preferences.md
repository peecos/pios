# Configure personal AI interaction preferences

## Identity
- **Name:** Configure personal AI interaction preferences
- **Definition:** Maintain owner-governed preferences for how a personal AI communicates, explains, proposes, and collaborates.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make interaction style explicit and revisable without confusing preference with truth, permission, or execution policy.
- **Meaningful outcome:** An active, versioned preference set can guide eligible interactions within its declared scope.
- **Boundaries — includes:** tone, response style, verbosity, formatting, ask-versus-assume posture, explanation depth, evidence presentation, proposal cadence, scope, provenance, and version.
- **Boundaries — excludes:** personal-AI identity, owner profile facts, execution permissions, standing rules, model routing, and request-specific instructions.
- **Terms and concepts:** An `interaction preference` shapes presentation or collaboration behavior; it does not authorize an action or make a statement true.

## Interaction Contract MLEs
### Set or revise interaction preferences
- **Actor:** The owner or an authorized interface acting on an explicit owner choice.
- **Command / intent:** Configure how the personal AI should communicate and collaborate in a defined scope.
- **Current state:** An owner/Core context, supported preference vocabulary, and current preference version exist.
- **Policies / invariants:** Changes are explicit and attributable; observation alone does not silently convert into a durable preference; preferences cannot broaden data access, execution authority, or truth status; narrower request-scoped instructions remain distinguishable.
- **Transition:** Validate the selected values and scope, record the decision and provenance, supersede prior values where applicable, and expose the active version.
- **Result:** An active, rejected, or superseded interaction-preference version.
- **Events / effects:** May influence response presentation, clarification behavior, proposal cadence, and evidence display.
- **Unknowns:** Universal precedence among global, role-scoped, mode-scoped, and request-scoped preferences is not established.

## Rules and defaults
### Rules / invariants
- Interaction preferences must not override execution policy, standing-rule authority, evidence requirements, or owner correction.
- Generated or inferred preference suggestions require an explicit governance path before becoming durable defaults.
### Recommended defaults
- Use a conservative, explainable baseline and allow later refinement.

## Unknown / unresolved
- The minimum portable preference vocabulary across personal-AI implementations remains undefined.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Personal-AI interaction preferences influence communication and collaboration but remain separate from truth and operational permission. | rule/invariant | sourced | [D06](../evidence/statement-provenance.md). |
