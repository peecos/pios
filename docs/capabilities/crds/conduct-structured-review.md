# Conduct a structured review

## Identity
- **Name:** Conduct a structured review
- **Definition:** Evaluate a declared period, event, or subject through explicit review questions and preserve decisions, updates, open loops, and carry-forward outcomes.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Turn a bounded body of current evidence into an inspectable review outcome without silently mutating the objects being reviewed.
- **Meaningful outcome:** A review closes with its scope, inputs, questions, findings, decisions, updates, carry-forward items, unresolved matters, provenance, and next review state recorded.
- **Boundaries — includes:** review identity, cadence or trigger, scope, eligible inputs, review questions, findings, decisions, carry-forward, owner attention, completion state, provenance, and revision.
- **Boundaries — excludes:** neutral summarization, making every recommended downstream change, executing work, redefining source objects, and inferring unsupported truth.
- **Terms and concepts:** A `review` is a bounded evaluation process. It may contain summaries and reflections, but its defining outcome is a recorded disposition of what was examined and what follows.

## Interaction Contract MLEs
### Complete a bounded review
- **Actor:** The owner, an authorized reviewer, or a review agent operating within declared scope.
- **Command / intent:** Review a period, event, goal, project, knowledge area, or other eligible subject.
- **Current state:** The review scope, questions, source references, prior review state, and authority are available.
- **Policies / invariants:** Inputs and omissions remain visible; generated findings retain source provenance and uncertainty; proposed changes do not silently take effect; decisions identify their authority; unresolved and carried-forward items retain identity.
- **Transition:** Assemble the bounded input set, answer the declared questions, distinguish summary from interpretation, record decisions and unresolved items, and close or defer the review.
- **Result:** A completed, deferred, failed, or superseded review record with explicit follow-up disposition.
- **Events / effects:** May create updates, attention items, proposals, Work Starters, tasks, revised goals, or later review schedules through their own capabilities.
- **Unknowns:** Universal review templates, mandatory cadence, and materiality thresholds are not established.

## Rules and defaults
### Rules / invariants
- A review must identify what it considered and what material evidence was unavailable.
- Recommendations and carry-forward items must not be represented as completed downstream changes.
### Recommended defaults
- Record questions asked, inputs reviewed, decisions made, updates created, open loops, carry-forward items, and next review timing.

## Unknown / unresolved
- Domain-specific review templates and the boundary between automatic and owner-led review decisions require profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A structured review is a bounded evaluation with explicit inputs, questions, findings, decisions, updates, unresolved matters, and carry-forward outcomes. | rule/invariant | sourced | [H01–H04](../evidence/statement-provenance.md). |
