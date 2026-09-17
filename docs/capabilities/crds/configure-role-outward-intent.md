# Configure a Role's outward intent

## Identity
- **Name:** Configure a Role's outward intent
- **Definition:** Declare whether and how an owner context Role is intended to support private-only, privately shared, or public representation.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make outward representation intent explicit without treating the declaration as access control, publication, or automatic exposure of private material.
- **Meaningful outcome:** A versioned outward-intent declaration is active, disabled, superseded, or rejected for one Role.
- **Boundaries — includes:** Role identity, intended exposure class, audience intent, outward framing, effective time, owner decision, status, and version.
- **Boundaries — excludes:** access-control enforcement, audience membership, publication, outbound action authority, content copying, and visibility changes to private source objects.
- **Terms and concepts:** `outward intent` describes the intended representation class; it does not itself make any content visible.

## Interaction Contract MLEs
### Set or revise outward intent
- **Actor:** The owner or an explicitly authorized governance interface.
- **Command / intent:** Set, disable, or revise the outward intent for one Role.
- **Current state:** An active Role definition, current outward-intent version, supported exposure classes, and owner authority exist.
- **Policies / invariants:** Private-only is the safe default; mutually exclusive intent states are explicit; changing intent does not expose private content; access, discovery, rights, publication, and outbound-action authority remain separately governed.
- **Transition:** Validate the Role and requested intent, record owner authorization and framing, and activate or reject a new version.
- **Result:** An active, disabled, rejected, or superseded outward-intent declaration.
- **Events / effects:** May make separately prepared outward representations eligible for later access or publication decisions.
- **Unknowns:** Supported audience classes and review cadence vary by implementation and jurisdiction.

## Rules and defaults
### Rules / invariants
- Enabling outward intent must never expose existing private Role-linked information.
- An outward-intent declaration is not a publication command or an access grant.
### Recommended defaults
- New Roles begin private-only with no outward representation eligibility.

## Unknown / unresolved
- How outward intent interacts with organization, relationship, and jurisdictional policy requires a sharing profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| A Role's outward intent is explicit, private-first, and separate from access control, publication, and private-content exposure. | rule/invariant | sourced | [D16](../evidence/statement-provenance.md). |
