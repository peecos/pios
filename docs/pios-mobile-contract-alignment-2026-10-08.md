# PIOS mobile contract alignment — October 8, 2026

Status: current documentation clarification; not a deployment, capability-adoption,
compatibility, or production-verification claim. Publication state is separate.

## Read this before continuing

This notice connects the [master](../index.html#core-app-and-independent-applications),
[integration contract](integration-interoperability-and-governance-v0.1.md#197-device-source-and-working-state),
[first-party profile](pios-first-party-mobile-apps-by-prifina.md), and
[local handoff contract](pios-first-party-mobile-local-handoff-v0.1.md).
It supersedes the earlier exclusive-Core-network-client rule for the named
Notes reconciliation path, not the retained evidence of earlier deployments.

## Architecture decisions

- Core-contract membership, PIOS-system membership, ecosystem participation,
  physical placement and state treatment are separate. Publisher identity and
  dependency on Core do not alone settle any other axis.
- Solo remains the preferred complete server-side package. Core app collection,
  immediate device preprocessing, local handoff and permitted cache support are
  device-side PIOS responsibilities, not independent-agent workloads merely
  because they run outside the VM.
- Independently useful Notes, Voice Notes, Browser and general assistants use
  PIOS. The new Core-dependent LifeStory is an explicitly dependent companion,
  not an independently useful product and not automatically part of the Core
  contract. LifeStory Indie remains independent.
- General direct, brokered and hybrid integration remains supported. In the
  named first-party profile, Core remains the integration/governance hub; Notes
  may additionally use its own bounded reconciliation identity for command
  retrieval and acknowledgements. This is not an owner-wide credential or a
  grant for general capture, collection or unrelated writes. Actual activation
  and availability are recorded by the implementation, not inferred here.
- Device-source records and app-owned working records are not ordinary cache.
  A source retained only on a device is not automatically pending upload.
  Normalized evidence remains distinct from its source and from canonical
  server acceptance.
- Local save, handoff validation, local semantic application, canonical Core
  acceptance, application of a canonical revision and acknowledgement delivery
  are separate evidence boundaries. Existing wire names remain unchanged;
  interpretation is bound to schema, direction, operation and authority.
- Browser's owner-enabled continuity and explicit content retention are separate
  future integration contracts. Neither is a claim about the current standalone
  beta. Incognito, website credentials, cookies and session stores are excluded
  from automatic continuity. Browser-local Roles are not automatically canonical
  Cotton Roles.

## What does not change

No mandatory Core capability, compatibility level, app identity, App Group,
endpoint or deployment is added by this clarification. Existing intake,
retrieval, revision and recovery evidence keeps its original scope. Source
release, broader collection and credential activation require their applicable
authority. No requirement to re-ingest or repeat completed domains follows.

Updates, History, Knowledge compilation, caching, offline selection and
source-linked derivation already have framework and library coverage. The
[candidate record](capabilities/decisions/mobile-interoperability-candidates-2026-10-08.md)
collects possible additional CRDs without adding them to the accepted inventory.

## Instructions for implementers and documentation agents

Read the linked current contracts before the next affected change. Preserve
local work, protocol compatibility and historical evidence. Reconcile stale
exclusive-routing and local-only descriptions; do not treat them as permission
to roll back newer bidirectional behavior. A dated handoff describes its
checkpoint, not perpetual runtime state.

Keep framework rules deployment-neutral, named-suite choices in the first-party
profile, and live status/authorization in implementation plans. Classify machine
functions before proposing migration: native server services belong in Solo by
default, independent assistants in their selected execution environment, and
device-bound collection/interfaces on the relevant device. Do not migrate all
background processes merely because they currently run on a Mac.

This file is a reading checkpoint, not evidence that an already-running agent
has read it. Public and remote consumers see changes only after their normal
publication or synchronization process; do not claim notification or deployment
from a local documentation edit.
