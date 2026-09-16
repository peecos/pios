# Govern outward usage rights

## Identity
- **Name:** Govern outward usage rights
- **Definition:** Declare and revise what human and machine recipients may do with an outward representation after obtaining access.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Preserve explicit use conditions without treating access or public visibility as permission for every form of reuse.
- **Meaningful outcome:** An outward representation has an attributable, current rights policy covering applicable human and machine uses and any required conditions.
- **Boundaries — includes:** viewing, reuse, redistribution, attribution, commercial use, crawling, indexing, agent use, model-training use, custom terms references, effective time, revision, and withdrawal.
- **Boundaries — excludes:** granting access, controlling discoverability, publishing the representation, proving external compliance, and changing source ownership.
- **Terms and concepts:** `usage rights` state permitted uses after access. They are distinct from technical access and from whether a representation can be discovered.

## Interaction Contract MLEs
### Change outward usage rights
- **Actor:** The owner or an explicitly delegated rights authority.
- **Command / intent:** Establish, revise, or withdraw use conditions for an outward representation.
- **Current state:** The representation, current rights state, intended audiences and machine actors, applicable terms, provenance, and authority can be determined.
- **Policies / invariants:** Human and machine uses can differ; public availability does not imply open reuse or training permission; material expansions require sufficient authority; revisions retain effective time and prior terms; unsupported enforcement is not represented as guaranteed compliance.
- **Transition:** Validate authority and policy consistency, bind a new rights state or withdrawal, and record its effective scope and provenance.
- **Result:** A current rights declaration or reasoned rejection.
- **Events / effects:** May change machine-readable metadata, delivery behavior, compliance checks, or owner review requirements without changing access or discoverability.
- **Unknowns:** Universal rights vocabularies, legal interpretation, jurisdictional effects, and enforceability are not established.

## Rules and defaults
### Rules / invariants
- Access to content must not be represented as permission to reuse, redistribute, or train on it.
- Rights claims must distinguish declared intent from technically or legally enforced outcomes.
### Recommended defaults
- Express human viewing, human reuse, machine access, indexing, training, redistribution, attribution, and commercial-use terms separately when relevant.

## Unknown / unresolved
- Interoperable machine-readable rights standards and conflict resolution among embedded, linked, and platform terms require later profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Usage rights are separate from visibility, discovery, and access and may distinguish human, crawler, agent, and training uses. | rule/invariant | sourced | [G05 and G07](../evidence/statement-provenance.md). |
