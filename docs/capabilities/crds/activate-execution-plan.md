# Activate an execution plan

## Identity
- **Name:** Activate an execution plan
- **Definition:** Derive an authorized one-off project or reusable routine from a plan while preserving the plan as its source design record.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Cross the governed boundary from proposed execution design to a selected execution form.
- **Meaningful outcome:** A project or routine is created with provenance to the approved plan, while the plan remains inspectable.
- **Boundaries — includes:** eligibility check, execution-form selection, derived-object creation, source linkage, attribution, and activation receipt.
- **Boundaries — excludes:** plan authoring, carrying out project work, running a routine instance, and silently replacing the plan.
- **Terms and concepts:** `activation` creates a new execution object; it is not a rename or destructive state conversion.

## Interaction Contract MLEs
### Activate plan into an execution form
- **Actor:** An authorized owner or execution coordinator.
- **Command / intent:** Activate an eligible plan as one-off or reusable execution.
- **Current state:** A plan exists and satisfies the applicable review and authority requirements.
- **Policies / invariants:** The selected form is explicit; the source plan remains durable; the derived object links back to the plan and activation decision; duplicate activation is detectable.
- **Transition:** Validate eligibility, select project or routine, create the derived object, and record provenance.
- **Result:** A new project or routine linked to its source plan.
- **Events / effects:** The derived object may enter its own active or configured lifecycle.
- **Unknowns:** Whether repeated activation of one plan is universally permitted is not established.

## Rules and defaults
### Rules / invariants
- Activation must not erase or rewrite the plan's historical meaning.
- One-off and reusable execution forms must remain distinguishable.
### Recommended defaults
- Record actor, time, selected execution form, source plan version, and resulting object.

## Unknown / unresolved
- Implementations may require plan approval before activation; the universal threshold remains profile-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Activation creates a project or routine and preserves the plan. | rule/invariant | sourced | [B08](../evidence/statement-provenance.md). |
