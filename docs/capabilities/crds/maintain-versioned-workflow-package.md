# Maintain a versioned workflow package

## Identity
- **Name:** Maintain a versioned workflow package
- **Definition:** Define and version a distributable reusable process with declared inputs, outputs, triggers, parameters, permissions, steps, and safety constraints.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make reusable automation inspectable and distributable without treating the package as personal truth or a completed run.
- **Meaningful outcome:** A versioned workflow package exists with a declared contract and immutable published versions.
- **Boundaries — includes:** package identity, version, purpose, input/output declarations, triggers, parameters, required permissions, step structure, publisher, safety constraints, and deprecation.
- **Boundaries — excludes:** owner installation, run execution, tool implementation, personal configuration, and silent mutation of governed facts.
- **Terms and concepts:** A `workflow package` is a reusable definition. An `installed workflow` is an owner-configured instance of one package version.

## Interaction Contract MLEs
### Maintain package contract and versions
- **Actor:** An authorized package author or publisher.
- **Command / intent:** Create, revise, publish, or deprecate a reusable workflow definition.
- **Current state:** A repeatable process and its required contract information are known.
- **Policies / invariants:** Published versions are immutable; permissions and touched domains are declared; inputs and outputs are explicit; safety constraints are inspectable; a package cannot itself assert owner-specific truth.
- **Transition:** Validate the package contract and record a new draft, published version, or deprecation state.
- **Result:** A version-addressable workflow package with provenance and declared operating boundaries.
- **Events / effects:** Owners may inspect or install an eligible version through a separate capability.
- **Unknowns:** Universal signing, trust, compatibility, and publisher-verification requirements are not established.

## Rules and defaults
### Rules / invariants
- Updating a published package creates a new version.
- Package inclusion or discovery does not grant execution authority.
### Recommended defaults
- Expose what the package reads, writes, produces, triggers, and requires before installation.

## Unknown / unresolved
- The formal relationship between workflow packages, skills, and reusable routines needs further alignment.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Reusable workflows declare their contract and use immutable published versions. | rule/invariant | sourced | [B17](../evidence/statement-provenance.md). |
