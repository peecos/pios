# Compose a source-derived PIOS portability package

## Identity
- **Name:** Compose a source-derived PIOS portability package
- **Definition:** Assemble owner-controlled source material into a self-describing package for governed validation and later import when no existing Core export is the source.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let an owner prepare source material for PIOS reconstruction or import without falsely representing that material as existing canonical Core state.
- **Meaningful outcome:** A versioned package exists whose manifest identifies its source-composed class, scope, ownership basis, source-by-source provenance, mappings, integrity evidence, exclusions, and uncertainty or loss.
- **Boundaries — includes:** source inventory, ownership and authority basis, declared scope, preserved raw material, optional mapped candidates, source mapping, manifest creation, checksums, exclusions, uncertainty/loss reporting, and secret exclusion.
- **Boundaries — excludes:** exporting an existing Core, validating the completed package, importing or promoting its contents, creating canonical events, activating carried definitions, copying credentials, and claiming Full Core Export Bundle status.
- **Terms and concepts:** A `PIOS Portability Package` may be assembled from owner-controlled sources before a Core exists. Its contents are import candidates, not proof of prior Core state.

## Interaction Contract MLEs
### Compose package from owner-controlled sources
- **Actor:** The owner or an explicitly authorized migration agent or tool.
- **Command / intent:** Assemble a declared set of owner-controlled sources into a PIOS Portability Package.
- **Current state:** Source materials, ownership or authority basis, intended scope, known formats, exclusions, and destination intent can be determined.
- **Policies / invariants:** Raw and mapped material remain distinguishable; source provenance and uncertainty are preserved; ambiguous ownership and prohibited secrets fail closed; mappings do not silently create canonical truth; the package is not labelled as an existing Core export.
- **Transition:** Inventory the selected sources, preserve eligible raw material, create optional candidate mappings, record exclusions and uncertainty, generate the manifest and integrity evidence, and close the package.
- **Result:** A source-composed PIOS Portability Package ready for independent validation, or a failed/blocked composition report.
- **Events / effects:** May become eligible for package validation and owner review; it does not authorize import, promotion, activation, or deployment.
- **Unknowns:** Source-specific mapping profiles, acceptable ownership evidence, encryption containers, and maximum package sizes remain implementation-specific.

## Rules and defaults
### Rules / invariants
- A source-composed package must remain distinguishable from a Full or Scoped Core Export Bundle.
- Composition must preserve source identity, ownership basis, uncertainty, and all declared exclusions.
- Portable definitions and credentials must remain separate; package creation grants no destination authority.

### Recommended defaults
- Preserve raw source material alongside mapped candidates when policy and storage constraints permit.
- Generate a manifest and digest set before submitting the package for validation.

## Unknown / unresolved
- Common mapping profiles and minimum evidence thresholds vary by source type and destination capability.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A source-composed PIOS Portability Package is independently assembled from owner-controlled sources and must not be represented as existing Core state or a Core export. | rule/invariant | sourced | [C25](../evidence/statement-provenance.md). |
