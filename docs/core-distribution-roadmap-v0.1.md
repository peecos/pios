# Core Distribution and Compatibility Roadmap v0.1

Status: planning roadmap. This document makes the PIOS 2.0 compatibility goals
and evidence thresholds explicit. It does not authorize deployments, migration,
or write-through.

The governing contract is [Core Distribution and Compatibility Specification
v0.1](core-distribution-and-compatibility-spec-v0.1.md).

## Goal A: Canonical Portability

Outcome: a full Core Export Bundle can be validated, restored, and hydrated
without provider identifiers becoming canonical meaning.

Complete or evidenced now:

- Core Template, Core Export Bundle, and Provisioning Manifest are defined;
- AWS export, checksums, local restore, selected retrieval, and limited
  destination hydration mechanics proofs exist;
- a private reference proof has produced a current bundle with canonical
  `core://` references, explicit provider provenance, managed hydration, and
  self-hosted conformance evidence. It remains a private proof artifact, not a
  public distribution or compatibility claim.

Next deliverables:

- publish the export manifest schema and import-report schema;
- publish generic fixture bundles and a fixture-based cross-profile
  export/import conformance test that third parties can reproduce;
- publish the public version and reference rules used by the private proof;
- repeat the evidence against release-candidate managed and self-hosted
  artifacts rather than an owner-specific pilot.

Done when: a clean self-hosted and managed destination both preserve stable ids,
references, counts, checksums, and selected retrieval evidence from the same
fixture bundle.

## Goal B: Stable Client Compatibility

Outcome: agents and applications use one Core API regardless of hosting model.

Next deliverables:

- publish OpenAPI for the mandatory v1 Core API;
- implement `/.well-known/core` capability discovery;
- define scopes, errors, pagination, idempotency, rate limits, and async jobs;
- build a minimal CLI/client conformance fixture before language-specific SDKs.

Done when: the same conformance client can capture, retrieve, export, and
discover capabilities against the managed reference and a self-hosted reference
by changing only endpoint and credentials.

Current proof progress: the AWS reference now exposes a machine-readable
OpenAPI proof profile and IAM-authorized capability discovery for two
proof-only write routes. Private reference deployment and live discovery proof
exist. This is an implementation starting point, not Level 2 compatibility
evidence: the mandatory v1 API surface and cross-profile conformance client
remain incomplete.

## Goal C: Installable, Verifiable Distribution

Outcome: public artifacts can be installed and verified without overclaiming
provider support.

Next deliverables:

- publish signed release metadata, checksums, SBOM/dependency record, and
  release notes;
- publish a data-empty VM release candidate and its verification guide;
- create a Docker Compose package and idempotent Linux installer from the same
  self-hosted runtime definition;
- publish a provider-support matrix using the status terms in the specification.

Done when: a user can verify a signed release, install a data-empty Core on the
supported generic VM path, run first-boot health checks, and prove no owner data
or secrets were bundled.

## Goal D: Provider Coverage Without Lock-In

Outcome: AWS, self-hosted VM, Azure, and Google Cloud are deployment profiles
behind the same contract, not different products.

Order:

1. Maintain AWS Managed and generic self-hosted VM as the reference profiles.
2. Repeat the Google Cloud experimental proof with public release artifacts and
   conformance checks before claiming support.
3. Complete Azure image conversion and synthetic import proof.
4. Add provider-native templates only after the API and portable bundle contract
   are stable.

Non-goal: matching each provider's internal services. Compatibility is measured
at the Core API, canonical package, and operational migration boundary.

## Goal E: Operational Migration Compatibility

Outcome: the owner can move a live Core with a controlled rollback path.

Prerequisites:

- Goals A and B conformance evidence;
- incremental export/delta specification;
- source read-only and final-delta procedure;
- migration audit records, import reports, and rollback proof;
- owner-ratified destination security, retention, key-custody, and cutover
  posture.

Done when: a controlled synthetic migration completes from one profile to
another with a final delta, endpoint/credential change, rollback window, and
no source re-download of historical information.

## Current Focus and Boundaries

The current immediate work is public Goal A/B contract hardening and
reproducible conformance fixtures. A private, owner-ratified write-through
parallel-run may provide implementation learning about bounded scope,
idempotency, verification, and reconciliation, but it is not a substitute for
API, export, or distribution conformance and does not change any compatibility
level claim.

Do not treat this roadmap as approval for broad migration, connector sync,
public provider support, production cutover, or sensitive-data transfer.

## Hosted Service Fork

A future multi-tenant hosted Core service is a separate Prifina product path,
not an automatic extension of the AWS reference or public templates. Prifina
intends to make the hosted option available soon; until its service announcement
there are no hosted accounts or production API credentials. Its evidence gate,
required separation from the private owner Core, delivery stages, and
account/service capabilities are defined in the [Core Hosted Service Fork Path
v0.1](core-hosted-service-fork-path-v0.1.md). It becomes suitable for a
separate ratified decision only after private operational, portability, and
client-contract evidence is materially complete; it does not block the current
Goals A-E work.
