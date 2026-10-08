# Mobile interoperability CRD candidates — October 8, 2026

Status: candidate assessment, not finalized CRDs or inventory additions.
The 117 existing CRDs retain their current status, evidence and adoption scope.
No public realization or compatibility level is established by this record.

## Source roles and publication boundary

The [alignment notice](../../pios-mobile-contract-alignment-2026-10-08.md) and
[Integration sections 19.7–19.8](../../integration-interoperability-and-governance-v0.1.md#197-device-source-and-working-state)
are current documentation decisions and contracts, not deployed-code evidence.
Integration sections 3–6 already define manifests, agreements and grants.
The existing library is comparison evidence for candidate scope. Before final
extraction, pin the applicable published framework revision; do not silently
replace the source basis of the existing historical extraction. Unpublished
clarifications do not become published implementation evidence through this file.
Restricted operational evidence stays outside public library files.

## Candidate boundaries

All three rows are reasonable inferences from those contracts, not adopted
requirements. Names and final decomposition remain subject to the library's
normal statement-ledger and MLE pass.

| Candidate | Actor, intent and meaningful outcome | Closest existing CRDs and distinct scope |
| --- | --- | --- |
| Reconcile a canonical change into an application working copy | Authorized application reconciler applies a specified canonical revision, or preserves a conflict/rejection/retry state, with attributable acknowledgement | [Pending capture](../crds/reconcile-pending-capture.md) resolves work into Core; [knowledge note](../crds/maintain-deliberate-knowledge-note.md) governs the note itself. Candidate excludes canonical authoring, generic cache refresh and direct mutation of app-private storage. |
| Acquire authorized device-source evidence | Authorized device collector obtains a bounded source observation/snapshot, or reports unavailable/denied/failed acquisition, under declared collection scope | [Source registration](../crds/register-connected-source.md) defines the source; [capture submission](../crds/submit-governed-content-capture.md) begins with a payload; [metric observation](../crds/record-metric-observation.md) covers recording a measured value. Candidate excludes granting OS permission, server ingestion, enrichment and automatic History promotion. Source-specific acquisitions may require separate CRDs rather than one generic bucket. |
| Evaluate an integration manifest into an agreement | Authorized evaluator compares a versioned manifest with owner terms, capability and operator policy to produce an attributable agreement result or refusal | [Outward access policy](../crds/govern-outward-access.md) governs an outward representation; [first entry](../crds/authorize-first-entry.md) is bootstrap access. Candidate excludes grant issuance, credential provisioning, request-time enforcement and general onboarding. It fills possible library coverage of an existing framework concept, not a newly invented PIOS responsibility. |

## Preliminary MLE checks

| Candidate | Independently understandable | Meaningfully usable | Success/failure determinable | Further splitting loses this outcome's context |
| --- | --- | --- | --- | --- |
| Working-copy reconciliation | Yes: reconcile one specified change into a consumer | Yes: without creating a new canonical note | Yes: applied, conflict, refused or retryable | Identity/version checking, application and attributable result support this outcome; canonical editing remains separate |
| Device-source acquisition | Yes for a named source class | Yes: acquire without uploading | Yes: bounded evidence or reasoned non-acquisition | Collecting a source observation requires its scope and result; unrelated source classes must be tested individually before grouping |
| Manifest evaluation | Yes: evaluate one manifest/version | Yes: without issuing credentials | Yes: agreement result or refusal | Terms/capability comparison and recorded result support this outcome; owner approval and grant issuance must be tested separately, not silently absorbed |

Enlargement check: do not combine these into a “mobile integration” CRD.
Each has an independently meaningful result. A queue, endpoint, App Group,
receipt serializer or screen is a supporting element, not automatically a CRD.
Cross-context reuse and complete public realizations remain unconfirmed.

## Existing coverage — extend profiles or evidence, not duplicate CRDs

- [Device cache](../crds/maintain-authorized-device-content-cache.md) and
  [selected offline content](../crds/maintain-selected-offline-content.md).
- [Derivation](../crds/derive-content-from-retained-source.md),
  [representation lifecycle](../crds/govern-derived-representation-lifecycle.md)
  and [governed retrieval context](../crds/assemble-governed-retrieval-context.md).
- [Completed work](../crds/publish-completed-work-record.md),
  [owner attention](../crds/manage-owner-attention-item.md) and
  [daily History](../crds/compile-daily-history.md).

Statistics/coverage inspection remains a boundary question: first compare
[operational inspection](../crds/inspect-operational-run-record.md),
[measurement](../crds/maintain-measurement-definition.md) and
[knowledge integrity](../crds/assess-knowledge-layer-integrity.md). A new screen
or chart is not enough to justify a fourth CRD.

## Next library task

Perform one bounded candidate disposition against the then-current framework
and these nearest CRDs. Record each candidate as new CRD, existing-contract
extension, source-specific realization/profile, or unresolved, with statement
provenance and any remaining decomposition. Only accepted final CRDs enter the
inventory. Do not reopen the historical corpus, change its retained evidence,
or make this work a prerequisite for unrelated PIOS Solo implementation.
