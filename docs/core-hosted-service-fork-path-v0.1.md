# Core Hosted Service Fork Path v0.1

Status: planned future product path. It is not an active service, launch plan,
or authorization to accept tenant data.

Planned operator: **Prifina**. Prifina intends to make a hosted Core option
available soon. The launch date, regions, plans, eligibility, account-creation
process, and API access will be announced by Prifina. Until then, neither PIOS
nor its public templates provide hosted accounts, tenant onboarding, or
production API credentials.

## Purpose

PIOS defines portable Core contracts and public implementation templates. A
future multi-tenant hosted Core service may use those contracts, but it is a
separate product and operating model. It must not emerge implicitly from the
single-owner AWS reference or from publication of the templates.

The current priority is Valto's private owner Core: establish it as a durable,
governed, portable master for real normal work. The hosted-service path forks
only after that path has supplied enough operational evidence to make a
responsible product decision.

This document identifies Prifina as the planned operator, but does not set a
launch date, legal-service terms, pricing model, or availability claim. Those
require Prifina's separate service decision when the trigger is met.

## The Fork Decision

The decision point is an evidence gate, not a calendar milestone. A hosted
service discovery/foundation project may be proposed only when all of the
following are true:

1. **Private Core is genuinely operational.** At least one owner-approved,
   normal-sensitivity live flow has completed its parallel-run and canonical
   cutover criteria. It has reconciliation, audit, recovery, and owner-facing
   operating evidence; proof-only routes do not satisfy this condition.
2. **Portability is demonstrated.** The same representative fixture bundle has
   passed managed-to-self-hosted and self-hosted-to-managed conformance checks,
   including stable logical identifiers, canonical `core://` references,
   checksums, and preservation of an unknown extension field.
3. **The client contract is testable.** The mandatory v1 API profile,
   capability discovery, authentication/scopes, error shapes, idempotency,
   pagination, rate limits, and async-job semantics are published sufficiently
   for a cross-profile conformance client. A partial proof profile is not
   enough.
4. **Private operation has earned confidence.** The operator can show current
   monitoring, backup/restore, incident handling, cost visibility, access
   review, and evidence from sustained normal operation. The duration and
   evidence volume are set in the future fork decision rather than assumed
   here.
5. **There is a product reason.** At least one identified external-owner use
   case and a viable operator/support model have been assessed. Curiosity,
   public-template availability, or a deployable AWS stack alone are not a
   reason to create a tenant service.
6. **Prifina ratifies the service decision.** The decision names the intended
   customer, jurisdictions, data categories, commercial posture, initial
   service boundary, funding/cost authority, and named owners for security,
   support, and incidents.

Until all six conditions are met and ratified, work remains on the private
Core, framework, and self-setup templates. No prospective tenant is promised
access, support level, retention posture, or migration path.

## Required Separation

The hosted service starts in a separate AWS organization/account structure and
separate repositories, environments, credentials, telemetry, and support
operations. Valto's private Core remains a private tenant-like reference, not
the first production tenant or the service control plane.

The fork decision must choose and document:

- tenant isolation model: pooled data plane, per-tenant Core environment, or a
  justified hybrid;
- region and data-residency availability;
- encryption/key-custody model and operator access boundaries;
- identity provider and account-recovery model;
- tenancy, quota, metering, and commercial boundaries;
- export, deletion, suspension, and account-closure behavior;
- the compatibility level and provider-support status that may be claimed.

No tenant data, credentials, identity pools, audit streams, billing records, or
support tools may share Valto's private pilot environment merely for
convenience.

## Delivery Stages

### Stage 0: Product and Operating-Model Decision

Prifina creates the ratified service decision and threat model. Define the
initial owner profile, supported regions, prohibited data/classes, support
hours, service objectives, commercial hypothesis, and explicit non-goals.
Confirm that the hosted service is an independent Prifina product surface,
while PIOS remains the open framework.

### Stage 1: Hosted Foundation, No External Tenants

Build the separate cloud accounts, infrastructure pipelines, tenant registry,
identity boundary, isolated development/staging/production environments,
central audit/monitoring, backup/restore drills, cost controls, and an
operator-only provisioning path. Validate tenancy isolation with synthetic
tenants and publish no self-service sign-up.

### Stage 2: Closed Design-Partner Beta

Use invitation-only onboarding for a small, explicitly approved group. Each
tenant receives written terms, a documented data boundary, an account owner,
MFA, auditable access, export, suspension, and deletion paths. Support is
human-operated and the service may change with notice. Do not call this general
availability or broadly advertise production support.

### Stage 3: Self-Service Beta

Enable controlled account creation only after the closed beta has demonstrated
provisioning reliability, security operations, support handling, billing
reconciliation, and exit/portability behavior. Apply quotas, verified contact
methods, abuse controls, and an explicit beta service policy.

### Stage 4: General Availability Decision

Promote only through a separate release decision backed by measured service
objectives, security review, disaster-recovery evidence, support readiness,
commercial/legal readiness, current compatibility evidence, and a clear public
status claim.

## What a Hosted Service Must Include

Functional Core APIs and storage are necessary but insufficient. The initial
service plan must cover the following owner-facing and operator-facing areas.

| Area | Minimum hosted-service capability |
| --- | --- |
| Public website | Clear service description, deployment comparison, security and privacy summaries, current status, pricing or contact path, documentation, and an accurate beta/availability statement. |
| Account lifecycle | Invite or sign-up flow, verified contact method, terms/privacy acceptance records, organization/owner profile, MFA, recovery, account transfer rules, suspension, and closure. |
| Tenant onboarding | Eligibility check, region/data-residency choice where offered, consent and data-boundary confirmation, provisioning progress, first-admin setup, and an explicit completion record. |
| API access | Scoped API-key and/or OAuth-client creation, secret display-once behavior, rotation, revocation, expiration, usage/audit visibility, sandbox policy, rate limits, and quotas. |
| Authorization | Roles, least-privilege scopes, administrator changes, service accounts, break-glass procedure, and tenant-visible audit records. |
| Data lifecycle | Import policy, export/download, retention, legal-hold handling if applicable, deletion request, verified purge/closure process, and a documented exit path. |
| Security and privacy | Threat model, encryption/key posture, vulnerability and patch process, access reviews, audit retention, incident response, breach-notification process, privacy notice, data-processing terms, and subprocessor disclosure where applicable. |
| Reliability and operations | Service objectives, status page, monitoring/alerting, backup/restore and disaster-recovery tests, capacity planning, deployment/change process, incident communications, and cost guardrails. |
| Billing and commercial operations | Plan definitions, metering, invoices/payment handling, taxes, trials, credits/refunds, failed-payment handling, and cancellation effects. |
| Support and success | Documentation, support entry point, response expectations, onboarding assistance, known limitations, escalation path, and product-feedback handling. |
| Governance and trust | Acceptable-use policy, abuse prevention/reporting, consent records, operator access policy, transparency/change notices, and a process for high-risk or unsupported use cases. |
| Ecosystem and compatibility | Published API/version policy, SDK/client support policy, migration/import/export guides, integration review rules, and accurate provider/compatibility status claims. |

## Initial Hosted-Service Boundaries

The first hosted beta should be deliberately narrower than the private Core
ambition. It should not imply support for broad migration, connector sync,
sensitive/guarded intake, arbitrary third-party agents, delegated authority,
or operational migration compatibility until those have their own current,
published evidence and service controls.

## Relationship to Current Work

This path does not block private Core operation, portable distribution, or
self-hosted work. It gives them a clear downstream purpose: prove the contract
and operational discipline before exposing that contract as a service for other
owners. The current Core Distribution Roadmap remains the governing path for
those prerequisites. Once service availability is announced, Prifina's service
terms, privacy notice, support policy, and status communications govern the
hosted offering; the PIOS repository continues to govern the framework and
compatibility contract.
