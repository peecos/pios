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

## 2. Terms and hard boundary

| Term | Meaning |
| --- | --- |
| Full Core Export Bundle | The complete exportable Core payload at a stated export time: canonical originals, events, knowledge, glossary, system definitions, provenance, integrity records, and rebuild instructions for the declared Core. |
| Scoped Core Bundle | An export of a selected Core subset for sharing, testing, recovery, or transfer. It is not a Full Core Export Bundle and cannot imply complete-Core coverage. |
| PIOS Portability Package | An import/reconstruction package assembled from a Core export or independently from owner-controlled sources. |
| Provisioning Manifest | The current PIOS artifact binding a template/profile, security posture, and optional bundle hydration into a runnable Core. |

A source-composed PIOS Portability Package is not evidence of an existing Core
state. It cannot become a Full Core Export Bundle merely because it was imported
or renamed. Only governed import, validation, canonical event/provenance
creation, and a subsequent Core export can produce a Full Core Export Bundle.

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

## 6. Conformance fixtures

The first fixtures must be synthetic and include raw-only, mapped, partial,
unknown-extension, conflicting-source, invalid-ownership, and prohibited-secret
cases. The same fixture set should later validate source-composed-package and
Core-export-bundle paths across the managed and self-hosted profiles.

## 7. Non-goals

File extensions, managed migration quotes, conversion marketplaces, service
pricing, connector recommendations, and provider-specific storage are optional
operator/ecosystem matters. They are not normative requirements of this
specification.
