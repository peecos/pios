# Retain governed content

## Identity

- **Name:** Retain governed content
- **Definition:** Accept supplied content and preserve it as a durable source object whose identity, ownership, origin, and lifecycle remain governable.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Make content durably available without silently turning intake into permission for processing or use.
- **Meaningful outcome:** A governed source object exists and can be identified, inspected, and acted on later.
- **Boundaries — includes:** intake validation, source identity, owner association, origin, durable reference, lifecycle state, and result reporting.
- **Boundaries — excludes:** semantic processing, derived outputs, context allocation, retrieval, generation, and presentation-specific file organization.
- **Terms and concepts:** `source object` means the retained original or authoritative supplied representation.

## Interaction Contract MLEs

### Retain supplied content

- **Actor:** An authorized owner, client, or ingestion process.
- **Command / intent:** Retain supplied content under owner governance.
- **Current state:** Content and available provenance are presented for intake.
- **Policies / invariants:** Owner and source identity are explicit; retry behavior is deterministic; retention does not imply processing, allocation, or disclosure; failure is not reported as success.
- **Transition:** Validate the request, preserve the content or durable reference, establish governed identity, and record the result.
- **Result:** A retained source object and receipt, or a reasoned failure.
- **Events / effects:** Success may trigger separately governed processing or organization.
- **Unknowns:** Universal duplicate-detection and retention-period policies are not established.

## Rules and defaults

### Rules / invariants

- Later derivatives must not erase or masquerade as the source.
- Retention alone must not authorize a consumer to use the content.

### Recommended defaults

- Preserve original bytes when feasible.
- Use an inbox-like initial state when no destination was selected.

## Unknown / unresolved

- Whether deletion and retention periods belong here or in a separate lifecycle capability.

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Retention is distinct from later use. | rule/invariant | sourced | [Pilot provenance P01](../evidence/statement-provenance.md). |
| Preserve original bytes when feasible. | recommended default | sourced | Historical source-preservation design and current PIOS Originals/Derived distinction. |
