# PIOS Portability Package v0.1

Status: draft companion specification for PIOS 2.0. This document expands the
portability model without changing the current Core distribution or migration
claims.

## 1. Purpose

PIOS 2.0 already defines a Core Template, full Core Export Bundle, and
Provisioning Manifest. Those remain the normative transfer model for a running
Core. A PIOS Portability Package adds a prior entry path: an owner or agent can
assemble a self-describing package from owner-controlled sources before a Core
exists.

The [hosting and boundary principles](hosting-core-boundaries-and-portability-principles-v0.1.md)
distinguish the Core contract, the complete PIOS system, and physical
deployment. PIOS is an information operating system, not only the state being
transferred. Rebuildable processing and retrieval components may belong to the
PIOS system and its Solo VM without being authoritative payload records.

## 2. Terms and hard boundary

| Term | Meaning |
| --- | --- |
| Full Core Export Bundle | The complete exportable Core payload at a stated export time: canonical originals, events, knowledge, glossary, system definitions, provenance, integrity records, and rebuild instructions for the declared Core. |
| Scoped Core Bundle | An export of a selected Core subset for sharing, testing, recovery, or transfer. It is not a Full Core Export Bundle and cannot imply complete-Core coverage. |
| PIOS Portability Package | An import/reconstruction package assembled from a Core export or independently from owner-controlled sources. |
| Provisioning Manifest | The current PIOS artifact binding a template/profile, security posture, and optional bundle hydration into a runnable Core. |
| PIOS service composition | The versioned runtime/install definition for Core and the selected PIOS-native services, with required external dependencies and reconstruction instructions. It is not owner data or a new state-bundle format. |

A source-composed PIOS Portability Package is not evidence of an existing Core
state. It cannot become a Full Core Export Bundle merely because it was imported
or renamed. Only governed import, validation, canonical event/provenance
creation, and a subsequent Core export can produce a Full Core Export Bundle.

Neither a Full Core Export Bundle nor a source-composed package is by itself a
runnable PIOS VM. A data-empty golden image or equivalent install composition
supplies the operating services; the bundle supplies governed owner state;
the Provisioning Manifest binds the destination and authorization gates.
Corebox device clients and independent applications reconnect separately.

## 3. Package requirements

A package must include a manifest, checksums, source-by-source provenance,
ownership basis, declared scope, source mapping, and uncertainty/loss report.
It may contain preserved raw takeouts and mapped canonical candidates, but it
must distinguish them.

It must not contain live credentials, private keys, OAuth refresh tokens,
private operator configuration, deployment secrets, or material with ambiguous
ownership. A validator fails closed for missing integrity data, unsupported
versions, prohibited secret material, or unresolved ownership boundaries.

## 4. Package classes

| Class | Contents | Import outcome |
| --- | --- | --- |
| Raw | Preserved takeouts/files plus source descriptors | parked/analyzed source material only |
| Mapped | Raw material plus candidate entities/events/mappings | governed mapping review required |
| Partial | Explicitly scoped subset of sources or domains | may not imply whole-Core completeness |
| Core-exported | A Full Core Export Bundle or a scoped Core Bundle | governed compatibility/import path, preserving the bundle's declared scope |

Unknown extension fields are preserved verbatim where their enclosing canonical
record is supported. Derived indexes, embeddings, graph exports, and caches are
rebuildable by default and must be declared when included.

Rebuildable does not mean external to PIOS. An index implementing PIOS retrieval
may live in Core's Derived zone and be rebuilt inside the Solo VM. Omitting its
payload from an export does not permit omitting the instructions and supported
execution needed to reconstruct a promised capability.

## 5. Import and operationalization

Import validates container structure, schema/version, checksums, encryption
metadata, ownership, canonical references, and source mappings. It produces an
Import/Operationalization Report covering:

- accepted, quarantined, rejected, and unresolved content;
- source-by-source provenance and loss/uncertainty;
- conflicts and proposed resolution path;
- generated Core records and rebuildable projections;
- connectors requiring separate reauthorization;
- any required owner approval before promotion, enrichment, or collection.

No import silently promotes raw material into History, owner profile truth,
personal meaning, public/shared content, or a Full Core Export Bundle.

Definitions for applications, agents, skills, connectors, and schedules may be
carried as portable descriptions. Import does not install, activate, connect,
or grant authority to them. Credentials, device trust, source connections, and
operational schedules require separate destination validation and owner
authorization.

For complete PIOS recovery, the report also distinguishes installed,
reconstructed, authorized, operational, and unavailable native services.
Validate the selected processing, retrieval, and PIOS-specific gateway behavior,
including any explicitly remote executors, rather than equating exact-byte
restore with recovery of the whole operating system. Corebox receiver state,
unregistered storage, and independent application caches do not become canonical
Core records merely because a service is part of PIOS or shares its VM.

## 6. Composition roles

- The **owner** defines purpose, scope, exclusions, sensitivity boundaries,
  destination intent, and acceptable external processing.
- An **agent or migration tool** may inventory, map, package, validate, explain
  uncertainty, and prepare review material within its authority.
- The **receiving implementation** verifies and operationalizes accepted
  content, rebuilds allowed projections, and reports what became operational.

The agent performs preparation work; it does not infer unlimited authority from
filesystem, account, or source access.

## 7. Validation stages

A package validator should report separately:

1. **Container validation:** safe paths, readable structure, required manifest,
   declared files, counts, and byte limits.
2. **Schema validation:** recognized versions, required identifiers, field
   types, references, and extension handling.
3. **Integrity validation:** digest and signature verification where applicable.
4. **Semantic validation:** coherent provenance, scope, chronology, ownership,
   and references without silent normalization.
5. **Capability validation:** destination support, required conversions,
   unsupported optional content, and owner-review points.

Technical validity does not constitute owner approval to transfer or import.

## 8. Partial, merge, and conflict handling

A package may target an empty Core, an existing Core belonging to the same
owner, a recovery environment, or an isolated review environment. Partial
packages declare selection criteria, exclusions, time boundaries, unresolved or
external references, and intended use.

Merge import must not silently overwrite canonical state. Conflicts may be
preserved side by side, represented as a new version, mapped to an existing
object, proposed for owner review, or retained as unresolved source material.
The Import/Operationalization Report records every resolution and loss.

## 9. Large-package and recovery profiles

The logical package may be one archive or multiple signed parts. Large-package
profiles may use segmented archives, resumable transfer, content-addressed
chunks, separate media volumes, manifest-first inspection, and incremental
validation without changing canonical package meaning.

A recovery package uses the same validation and import boundary while placing
additional emphasis on completeness, encryption, independent storage, key
separation, periodic creation, and tested restore behavior.

## 10. Security, third-party information, and uncertainty

Portability packages may be an owner's most sensitive aggregate artifact. The
package declares encryption and key-handling expectations, sensitivity,
external-processing boundaries, temporary retention, and required deletion.
Secret values and non-exportable credentials remain excluded.

Personal information may concern other people or organizations. Composition and
import must support exclusions, restricted sections, minimization, ownership or
authority review, and destination-side policy checks.

Unknown formats, ambiguous identities, missing timestamps, partial extraction,
possible duplicates, unsupported application state, and uncertain inferences
are recorded explicitly. Uncertainty is preserved rather than silently
discarded or converted into canonical truth.

## 11. Agent-guided portability skill

A separate, portable skill may guide an owner through selecting purpose,
sources, exclusions, preparation depth, destination, and continuing
connections. It may compose and validate packages, but the package
specification—not a particular agent runtime—defines validity.

The skill should generate a reviewable package summary, source-mapping report,
unresolved-item report, and proposed operationalization plan. Any cost estimate,
provider recommendation, converter marketplace, or managed processing offer is
optional ecosystem functionality rather than part of package validity.

## 12. Conformance fixtures

The first fixtures must be synthetic and include raw-only, mapped, partial,
unknown-extension, conflicting-source, invalid-ownership, and prohibited-secret
cases. The same fixture set should later validate source-composed-package and
Core-export-bundle paths across the managed and self-hosted profiles.

Fixture coverage should also include path traversal, malformed manifests,
digest mismatch, unsupported required capabilities, merge conflicts, segmented
packages, interrupted import, rollback, and the rule that imported definitions
remain inactive until separately authorized.

## 13. Non-goals

File extensions, managed migration quotes, conversion marketplaces, service
pricing, connector recommendations, and provider-specific storage are optional
operator/ecosystem matters. They are not normative requirements of this
specification.
