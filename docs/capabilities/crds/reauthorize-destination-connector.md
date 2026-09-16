# Reauthorize a destination connector

## Identity
- **Name:** Reauthorize a destination connector
- **Definition:** Establish new destination-scoped credentials, trust, owner consent, and synchronization authority for a restored connector definition.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Resume future source synchronization or source-side actions without copying source-host credentials or assuming restored definitions retain authority.
- **Meaningful outcome:** The connector is authorized, denied, disabled, or pending at the destination with validated scope and no implicit credential reuse.
- **Boundaries — includes:** connector identity, destination, owner consent, authentication, credential reference, scopes, source account, trust/device requirements, sync boundary, test result, and lifecycle state.
- **Boundaries — excludes:** restoring the connector description, importing historical data, copying secrets in a bundle, granting unrelated capabilities, and silently activating schedules.
- **Terms and concepts:** A portable connector definition describes intended integration; `reauthorization` establishes current destination authority.

## Interaction Contract MLEs
### Reauthorize connector
- **Actor:** The owner or explicitly authorized connector administrator.
- **Command / intent:** Connect the restored destination to the external source for future operation.
- **Current state:** A connector definition and destination exist, but destination credentials or trust are absent or invalid.
- **Policies / invariants:** Credentials are acquired through the destination's approved method; scopes are explicit and minimal; owner identity and source account are verified; activation and schedules remain separately controlled; failed authorization does not affect restored historical records.
- **Transition:** Complete destination authorization, validate the connection, and record scope and lifecycle state.
- **Result:** An authorized, denied, failed, disabled, or pending connector registration.
- **Events / effects:** May enable future sync sessions or source actions under declared policy.
- **Unknowns:** Provider-specific consent renewal and token-rotation behavior varies.

## Rules and defaults
### Rules / invariants
- Credentials, device trust, and source authority must not be inherited solely from imported configuration.
- Reauthorization must not retroactively change provenance of restored historical data.
### Recommended defaults
- Start with future synchronization disabled until connection validation and scope review complete.

## Unknown / unresolved
- Which connectors can support destination-side continuity without a full re-consent flow is provider-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Restored connector descriptions require separate destination validation, credentials, and owner authorization. | rule/invariant | sourced | [C24](../evidence/statement-provenance.md). |
