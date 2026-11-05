# Operating Document Authority and Recovery v0.1

Status: draft companion specification for PIOS 2.0, November 5, 2026. This
defines a selectable full-document operating profile, not a shipped capability,
authority cutover, new mandatory Core API, or compatibility-level claim.

## 1. Purpose and existing boundaries

PIOS can be the owner's working home for selected current documents, not only
an archive of earlier copies or a source of summaries. This profile applies
the [master's agent-definition and source-authority model](../index.html#agent-definition-governance)
to full operating documents, governed edits and recovery guidance.

It composes existing Originals, Events, Knowledge, System definitions, Derived
projections and integration grants. It creates no sixth data zone, universal
document editor, new task platform, or obligation to migrate every repository
or wiki. Core-contract membership, PIOS-system membership, physical placement,
and state treatment remain separate.

## 2. Document authority and source ownership

Every selected object declares its authoritative source, accepted revision,
editing authority and permitted projection or runtime-copy roles. Authority
attaches to the object and applicable grant, not its Markdown extension,
directory, machine, publisher, or inclusion in an agent's context.

| Object role | Authority and treatment |
| --- | --- |
| Owner-adopted agent definition, role, grant or operating policy | Core retains the owner-specific definition and adoption history; effective authority follows the applicable approval and enforcement rules. |
| Selected living owner document | Core becomes its editing authority only after explicit adoption and verified full-document operation. Classify its subject through Cotton; not every operating document belongs in My System. |
| Repository-owned source, reusable skill, specification or repository instruction | The declared Git or other upstream source may remain authoritative. Core retains a version-bound reference and the owner's adoption/configuration record, not a competing editable master. |
| Official framework document | Its official repository remains authoritative. An owner's adopted version or local policy does not rewrite the shared framework. |
| Agent work record or completion report | Attributable operational evidence; acceptance of the report does not confirm its claims or turn it into owner direction. |
| Runtime or offline copy | A labelled derivative of its declared source, with revision, integrity, freshness and permitted-use limits; not an independently edited master. |

Governing an agent does not require transferring ownership of every source file
it uses to Core. Owner-specific adoption and grants are distinct from upstream
software authority. Repository instructions can govern repository work within
the delegated scope, but cannot enlarge owner permissions. Source updates do
not silently expand an adoption or grant.

Core's canonical records can include source-linked Knowledge, retained source
versions in Originals and adoption/policy definitions in System, with Events
recording changes and Derived views for use. Preserve the distinction between
source bytes, accepted document revisions, interpretations and active policy.
Where an external source remains authoritative, retain a reference or an
explicitly scoped snapshot with provenance; neither is an authority transfer.

## 3. Full-document operation

An implementation selecting this profile declares its supported document
format, fidelity, size limits and operations. A summary-only interface, search
hit, or old archive Original does not demonstrate current full-document support.
For each accepted document, bind:

- owner/Core and stable object identity, with prior-source identity mapping;
- complete accepted content, including meaningful metadata/frontmatter and links;
- source provenance, revision, integrity digest and relevant observation times;
- editing authority, authorized actor and permitted operations;
- revision ancestry and acceptance/Event references, including supersession.

Return the accepted full content through governed retrieval. Preserve exact
source bytes where claimed; if a supported transformation is required, retain
the source and declare the transformation and any loss. A rendered summary or
projection cannot substitute for exact-content verification.

Edits name the expected base revision. Refuse stale-base replacement or use an
explicit conflict/merge policy that preserves both accepted and proposed work.
Use stable operation identities for replay and interruption recovery. Record
new accepted revisions and their Events without silently rewriting history.
Document-specific authorization must be enforceable; a broadly named write
scope is not sufficient evidence of permission to edit a governing document.

Separate drafting, submitting a proposal, accepting content, adopting a policy,
and activating an authorization. Permission to edit text is not permission to
change the agent's own grants. An applicable owner-approved standing rule may
permit bounded changes; otherwise governing changes remain proposals awaiting
the required approval. Imported or retrieved instructions are data until the
declared adoption and enforcement boundary permits their use.

## 4. Bounded adoption and authority cutover

The implementation plan selects exact objects and records their current source
authority before transfer. Match existing identities and source versions; do not
re-ingest an already retained Original or create duplicate logical documents
merely because their editing surface changes.

Before claiming the selected set is Core-authoritative, demonstrate:

1. Full-content readback and source/provenance reconciliation for that set.
2. An authorized edit or proposal and exact accepted-revision readback.
3. Stale-base conflict handling and preservation of unaccepted work.
4. Scoped export and isolated reconstruction of full content, revision/Event
   history, required System definitions and Derived views, with exclusions stated.
5. A rollback plan preserving accepted and pending work and one editing
   authority; rollback is not silent restoration of an older policy or grant.
6. Explicit promotion under owner authority, naming accepted identities/revisions
   and any remaining external dependencies.

Former source files become labelled snapshots or managed projections after
cutover; source deletion is a separate decision. Git and official framework
authority remain unchanged unless separately and legitimately reassigned.
Consumers bind the declared source, identity, revision and hash rather than
assuming a fixed workstation path or that a retrieved copy is current.

Existing archive, summary-edit or subset-recovery evidence retains its original
scope. Test the new full-document boundary rather than claiming that those
earlier results prove it. A small selected set can be adopted without a whole
vault migration or blocking unrelated authorized production work.

## 5. Offline bootstrap and recovery guidance

A deployment relying on Core for operating instructions needs an independently
available, protected bootstrap for its declared outage/recovery scenarios.
Retain only the necessary approved guidance, source bindings, last-verified
revisions/digests, freshness limits and repair instructions. Do not put secret
values in that bundle; reference separately controlled key and credential
recovery procedures. Protect guidance against unauthorized modification.

Cached integrity proves retained bytes, not current authority. Report cached
revision and last validation explicitly. Previously authorized diagnostic or
recovery actions may continue only within their declared offline conditions;
unverified freshness must stop actions that require current policy. A recovery
exception must be approved beforehand, bounded and auditable, not invented by
the disconnected agent. Loss of connectivity never creates new permissions.

Allow safe local preparation within existing authority while live actions are
held. Keep offline edits/proposals pending and distinct from accepted guidance.
On reconnection, revalidate source versions, authority and revocation, reconcile
conflicts, and record resulting decisions. Do not silently promote an offline
copy to resolve disagreement.

This extends the [integration contract's offline limits](integration-interoperability-and-governance-v0.1.md#193-shared-container-authority-and-offline-limits)
to operating guidance without assuming that every bootstrap uses an App Group.
Test recovery when the normal guidance service is unavailable; merely storing
its repair instructions in that same unavailable service is insufficient.

## 6. Execution continuity and implementation boundaries

Independent development agents may use PIOS for scoped context, work records and
completion evidence without becoming PIOS-native services. Native PIOS
orchestration retains its declared system membership wherever it runs.
No particular manager, agent count, model, VM, Mac runner or task product is
mandated by this profile.

An implementation claiming work continues without the owner's workstation must
demonstrate durable execution and result retrieval across that disconnection.
Its local plan names assignment ownership, source/guidance revisions, granted
actions, checkpoints and handoff acceptance. Moving execution does not transfer
credentials, widen grants or prove a production capability.

## 7. Evidence and adoption status

Implementations report each boundary separately: proposed, implemented locally,
tested, deployed, authorized and accepted for owner use. Profile selection does
not imply full-document support or current authority. Documentation regression
tests prove source consistency, not runtime behavior or completed recovery.

Use synthetic fixtures for missing/full content, stale revisions, duplicate
operations, denied object edits, attempted self-authorization, externally
authoritative references, offline expiry/reconciliation and isolated recovery.
Retain explicit limitations and separately scoped live acceptance evidence.

Application recovery and response-loss examples are detailed in
[Portability section 9.1](pios-portability-package-v0.1.md#91-application-recovery-evidence)
and [Integration section 19.9](integration-interoperability-and-governance-v0.1.md#199-response-loss-and-service-progress).
They do not prescribe a debugger, release route, worker count or timeout.
This profile does not authorize migration, source release, deployment, new
grants, expenditure or publication, and does not add accepted CRDs or change
Core Compatibility Levels 1–5.
