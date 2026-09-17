# Assign an agent runtime role

## Identity
- **Name:** Assign an agent runtime role
- **Definition:** Bind an agent runtime to a defined functional position for a bounded scope and duration without changing the agent's persistent identity.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make coordination responsibility, reporting relationships, and temporary execution posture explicit and attributable.
- **Meaningful outcome:** An agent has an active, expired, revoked, completed, or rejected runtime-role assignment with scope, authority, responsibilities, relationships, and time bounds.
- **Boundaries — includes:** agent and runtime identity, role definition, scope, duration, responsibilities, reporting or peer relationships, activation, reassignment, completion, revocation, and provenance.
- **Boundaries — excludes:** changing the agent's persistent identity, authoring the agent definition, granting undeclared permissions, executing assigned work, and treating recovery mode or peer relationship as a permanent identity.
- **Terms and concepts:** A runtime `role` may map to `schema.org/Role`: it qualifies how an agent participates in a bounded operational context and remains distinct from the agent itself.

## Interaction Contract MLEs
### Assign or end a runtime role
- **Actor:** The owner or an authorized coordinating agent.
- **Command / intent:** Assign, revise, complete, revoke, or reassign an agent's functional runtime role.
- **Current state:** Agent identity, runtime identity, role definition, current assignments, required authority, task scope, and time bounds can be determined.
- **Policies / invariants:** Role assignment cannot expand permissions beyond explicit grants; identity survives role changes; peer relationship and recovery mode are contextual rather than hidden hierarchy changes; overlapping roles and conflicts are explicit; temporary roles have terminal handling.
- **Transition:** Validate the role and authority, bind it to the agent/runtime and scope, record relationships and time bounds, and activate or reject the assignment.
- **Result:** A current or terminal runtime-role assignment with provenance.
- **Events / effects:** May inform orchestration, routing, visibility, handoff, and responsibility tracking without executing the assigned work.
- **Unknowns:** Universal role taxonomy, conflict precedence, delegation depth, and automatic expiry rules are not established.

## Rules and defaults
### Rules / invariants
- Runtime role and persistent agent identity must remain distinguishable.
- A role assignment must not grant permissions not already authorized through the applicable governance path.
### Recommended defaults
- Use the narrowest role, scope, and duration sufficient for the work and record who assigned it and why.

## Unknown / unresolved
- Cross-system role naming and delegation-chain interoperability require a later profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Director, manager, worker, peer, and recovery concepts describe runtime responsibility or mode rather than persistent agent identity. | rule/invariant | sourced | [J05–J06](../evidence/statement-provenance.md). |
