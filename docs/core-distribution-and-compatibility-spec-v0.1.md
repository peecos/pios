# Core Distribution and Compatibility Specification v0.1

Status: draft normative specification for PIOS 2.0 Core implementations.

This specification defines when independently deployed Core installations are
compatible. It applies to Core Managed, Core Self-Hosted, and future provider
or managed-service implementations. It does not authorize a deployment, data
migration, connector sync, or production use.

## 1. Goal

The infrastructure may change while the Core interface and canonical
information model remain stable. An application or agent should connect to a
compatible Core through its endpoint, credentials, owner context, API version,
and discovered capabilities. It must not depend on a cloud provider's storage,
database, queue, or AI service.

## 2. Compatibility Boundary

A compatible deployment must preserve these boundaries:

- Canonical content uses open, documented formats.
- Stable logical identifiers survive export, import, and deployment change.
- Canonical references use `core://` logical references, not provider URIs or
  local filesystem paths.
- Provider-specific paths, object versions, headers, ARNs, database keys, and
  indexes are adapter metadata or provenance, not canonical meaning.
- Derived indexes, embeddings, search stores, graph projections, caches, and
  provider-native pointer tables are rebuildable unless explicitly included as
  optional derived export content.
- Clients use the Core API and discovered capabilities, never direct S3,
  DynamoDB, Blob Storage, Cloud Storage, local storage, or provider queues.

Examples:

```text
core://originals/original_01J...
core://events/event_01J...
core://knowledge/project_openclaw_workshop
core://glossary/agentic_ai
```

An implementation may retain a physical storage reference in provenance, for
example an S3 URI or a local object path, but a client must not require it to
interpret or migrate canonical content.

## 3. Version Model

Every release and export declares three independent versions:

```yaml
core_version: 0.1.0
api_versions: [v1]
export_format_version: 1.0
```

- `core_version` identifies the implementation release and follows semantic
  versioning where practical.
- `api_versions` identifies supported external API contracts.
- `export_format_version` identifies the portable bundle structure and
  manifest semantics.

Minor releases must not break a supported API version or silently discard
unknown metadata. Major migrations require documented conversion tooling.
Imports must fail clearly, rather than silently dropping unsupported content.
An importer must preserve unknown extension fields verbatim when their enclosing
canonical record is otherwise supported.

Idempotency keys are opaque portable strings. They must be stable for retries
of the same logical source item and must not contain provider resource
identifiers. Use the first applicable form:

1. `source-native:<source>:<source_record_id>`;
2. `source-record:<source>:<source_record_id>:<source_original_time_utc>`;
3. `content:<source>:sha256:<checksum>:occurred:<source_original_time_utc>:original:<core_ref>`.

Times are normalized to UTC RFC 3339 form. `core_ref` is a `core://` logical
reference, never an S3 URI or other physical path. A new logical item requires
a new idempotency key. The v1 API and export schemas must preserve the key
verbatim; until their conformance evidence exists, an implementation may claim
only storage-level compatibility, not API or operational compatibility.

## 4. Required Connectivity Contract

Every API-compatible Core exposes a versioned HTTPS API and a capability
document at `/.well-known/core`.

The capability document declares at least:

```json
{
  "core_version": "0.1.0",
  "api_versions": ["v1"],
  "export_format_version": "1.0",
  "owner_id": "owner_example",
  "capabilities": {
    "capture": true,
    "events": true,
    "knowledge": true,
    "search": true,
    "export_import": true
  },
  "endpoints": {
    "capture": "/v1/capture",
    "events": "/v1/events",
    "search": "/v1/search",
    "export": "/v1/export"
  }
}
```

The v1 API specification must define request and response schemas,
authentication scopes, error shapes, pagination, idempotency behavior,
rate-limit responses, upload limits, and asynchronous-job semantics. Optional
capabilities must be discoverable and clients must degrade safely when one is
not available.

No implementation may claim Compatibility Level 2 or higher until the v1 API
specification and a matching capability document are published and tested.

Deployment-specific configuration provided to clients is limited to values such
as `CORE_BASE_URL`, API version, owner context, and credentials. Provider
configuration remains inside the deployment.

## 5. Portable Canonical Package

A full Core Export Bundle is a normal product capability, not an emergency-only
recovery mechanism. It contains the selected canonical originals, events,
knowledge, glossary, schemas, system definitions, pointer state, provenance,
connector metadata without secrets, integrity records, and rebuild
instructions.

The bundle manifest records:

- bundle id and creation time;
- source `core_version`, supported API versions, and `export_format_version`;
- owner identity and export scope;
- included zones and object counts;
- integrity algorithm and checksums;
- encryption information without secret material;
- optional derived content and compatibility notes.

Secrets, private keys, OAuth refresh tokens, and provider-only credentials are
not ordinary export content. A destination reports which connectors need
reauthorization.

## 6. Import, Migration, and Cutover

A compatible destination must verify manifest compatibility and checksums,
preserve logical identifiers, import canonical records, restore provenance and
pointer state, rebuild required projections, and produce an import report.

Migration does not require historical data to be fetched again from original
sources. Source reconnection is only needed for future synchronization or
source-side actions.

Operationally compatible deployments support a governed cutover sequence:

1. Prepare and validate the destination Core.
2. Perform full export and import.
3. Rebuild projections and validate identifiers, counts, checksums, and
   retrieval evidence.
4. Run incremental synchronization or a governed shadow/write-through period.
5. Test clients against the destination using only endpoint and credential
   changes.
6. Put the source flow into read-only mode, apply a final delta, and complete
   owner-approved cutover or rollback.

Incremental export and final-delta behavior are a later v1.1 deliverable. Until
then, an implementation must not claim operational migration compatibility.

## 7. Compatibility Levels

| Level | Name | Minimum result |
| --- | --- | --- |
| 1 | Storage compatible | Preserves/imports originals, events, knowledge, glossary, schemas, and provenance with stable logical ids. |
| 2 | API compatible | Implements the mandatory versioned Core API and capability discovery. |
| 3 | Portable | Produces and consumes validated full export bundles with stable ids and integrity verification. |
| 4 | Agent compatible | Supports scoped agent authentication, capture, retrieval, capability discovery, and controlled writes with repeatable conformance evidence for each claimed operation. |
| 5 | Operationally compatible | Supports incremental migration, read-only cutover, final delta, rollback, and endpoint transition; unavailable before the Section 6 v1.1 delta specification and proof. |

An implementation may claim only the highest level for which it has current,
published conformance evidence. Provider proof alone does not establish a
compatibility level.

## 8. Distribution Status and Release Requirements

Use these terms precisely:

| Status | Meaning |
| --- | --- |
| Source/template | Public source or template exists; no installability claim. |
| Proof artifact | Locally or privately verified artifact; not a public release. |
| Release candidate | Versioned package suitable for evaluation; not yet supported for production. |
| Experimental provider | One documented synthetic proof passed: package verification, image import, VM boot, synthetic first-boot initialization, Core-zone health check, no-owner-data check, and cleanup proof. Repeatability and public-release checks remain. |
| Supported provider | Repeatable conformance evidence, security/cost review, documentation review, and signed public release are available. |

A public release must identify its version, supported architecture, supported
API and export versions, provider status, minimum requirements, known limits,
release notes, migration notes, checksums, SBOM or equivalent dependency record,
and signature or attestation verification instructions.

## 9. Initial Distribution Order

The initial portable distribution sequence is:

1. Public source, normative specification, schemas, conformance tests, and
   signed release metadata.
2. Official container images, Docker Compose package, and an idempotent Linux
   installer.
3. Data-empty VM image and a supported generic VM deployment guide.
4. Managed AWS template and service profile.
5. Provider-specific Azure and Google Cloud templates or image-import paths.
6. Advanced packaging such as native packages, marketplace images, or Helm.

Kubernetes, cloud marketplaces, and native OS packages are optional advanced
distribution forms; they are not prerequisites for a personal Core.

## 10. Conformance Evidence

The conformance suite must create sample canonical content, export it, import
it into a clean compatible deployment, rebuild projections, exercise the
standard API, and compare stable identifiers, counts, checksums, references,
and selected structured and semantic retrieval evidence.

Fixtures must include at least one unknown extension field and prove it survives
export and import unchanged.

At minimum, the suite will cover local/self-hosted to managed and managed to
self-hosted paths. Azure and Google Cloud claims require their own evidence
once implementations exist. This specification does not treat an untested
provider path as compatible merely because its VM image can boot.

## 11. Current PIOS Boundary

PIOS 2.0 defines this compatibility target. The current AWS pilot and
self-hosted VM work are reference implementation proofs, not a completed
general-purpose Core distribution. Their live readiness and authorization gates
remain governed by their implementation repositories and owner decisions.
