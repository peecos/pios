# Prepare a Role-scoped outward representation

## Identity
- **Name:** Prepare a Role-scoped outward representation
- **Definition:** Create or revise a distinct owner-approved representation for outward use from eligible Role-scoped knowledge.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Support sharing or public presence without converting private source knowledge into outward content by implication.
- **Meaningful outcome:** A separate outward representation is created, revised, withdrawn, or rejected with source provenance and intended exposure preserved.
- **Boundaries — includes:** Role identity, source references, copied or directly authored outward content, transformation/redaction, intended audience or exposure, rights intent, version, and withdrawal state.
- **Boundaries — excludes:** changing the private source, configuring Role outward intent, enforcing audience access, publishing or sending, and granting outbound-action authority.
- **Terms and concepts:** An `outward representation` is a separate object or bundle suitable for later governed sharing; the private source remains unchanged.

## Interaction Contract MLEs
### Create or revise an outward representation
- **Actor:** The owner or an authorized preparation agent acting under explicit owner scope.
- **Command / intent:** Author, copy, summarize, redact, or revise Role-scoped knowledge for possible outward use.
- **Current state:** An active Role, eligible private source or direct outward content, declared outward intent, target exposure context, and owner authority exist.
- **Policies / invariants:** Private sources are never implicitly exposed or mutated; the outward representation has its own identity and lifecycle; source linkage and transformations remain traceable; publication and access remain separate decisions.
- **Transition:** Select eligible material, apply approved transformation or direct authorship, validate exposure and sensitivity constraints, and create a new outward-representation version.
- **Result:** A prepared, rejected, withdrawn, or superseded outward representation with explicit provenance and intended use.
- **Events / effects:** May become eligible for a later sharing, access-control, or publication capability.
- **Unknowns:** Universal redaction, rights, synchronization, and withdrawal propagation rules are not established.

## Rules and defaults
### Rules / invariants
- Copying or deriving outward material must not mutate the private source.
- Outward eligibility must not be represented as actual publication or audience access.
- Source-to-representation provenance must survive later revision and withdrawal.
### Recommended defaults
- Create a minimal separate representation and require review before any external exposure.

## Unknown / unresolved
- Whether later source changes should propose, require, or prohibit outward-representation updates depends on the sharing profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Outward Role knowledge is a distinct, traceable representation and must not expose or mutate its private source implicitly. | rule/invariant | sourced | [D17](../evidence/statement-provenance.md). |
