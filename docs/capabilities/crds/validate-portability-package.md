# Validate a portability package

## Identity
- **Name:** Validate a portability package
- **Definition:** Evaluate a portability package's container safety, schema compatibility, integrity, provenance, ownership, semantics, and destination capability requirements without importing it.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Determine whether a package is technically and semantically suitable for review or import while preserving all uncertainty and unsupported content.
- **Meaningful outcome:** A validation report classifies the package or its contents as accepted, rejected, quarantined, unsupported, or unresolved with evidence.
- **Boundaries — includes:** safe paths, manifest completeness, versions, identifiers, references, checksums/signatures, ownership, chronology, unknown extensions, prohibited secrets, required destination capabilities, and loss/uncertainty.
- **Boundaries — excludes:** composing the package, granting owner import approval, changing destination state, and silently converting unsupported data.
- **Terms and concepts:** `validation` establishes evidence and compatibility findings; it is not authorization or restore.

## Interaction Contract MLEs
### Validate package
- **Actor:** An authorized receiving implementation, validator, operator, or portability agent.
- **Command / intent:** Assess a package before transfer or import.
- **Current state:** A readable package and applicable format/capability rules exist.
- **Policies / invariants:** Missing integrity data, unsafe paths, unsupported required versions, prohibited secrets, or unresolved ownership fail closed; unknowns are retained; validation does not mutate destination canonical state.
- **Transition:** Inspect container, schema, integrity, semantics, and destination support and record findings.
- **Result:** A reproducible validation report with disposition and unresolved items.
- **Events / effects:** A valid package may become eligible for owner authorization and restore.
- **Unknowns:** Signature trust roots and acceptable partial-package thresholds are profile-specific.

## Rules and defaults
### Rules / invariants
- Technical validity does not constitute owner approval to transfer or import.
- Unsupported content must not be silently dropped.
### Recommended defaults
- Validate manifest-first before reading large payloads.

## Unknown / unresolved
- Cross-version converter selection and trust remain unresolved.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Package validation separately assesses structure, schema, integrity, semantics, and destination support. | rule/invariant | sourced | [C15](../evidence/statement-provenance.md). |
