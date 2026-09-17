# PIOS Capability Library project plan

**Established:** September 15, 2026
**Status:** active, public-safe working plan

## Purpose

Build a versioned Capability Requirements Document (CRD) inventory inside `peecos/pios`. The library preserves useful capability logic from historical PIOS design and other admitted evidence while keeping PIOS architecture versioning separate from capability versioning.

The library is adjacent to the PIOS master. A CRD can be aligned with PIOS without being part of the Core contract, adopted by a compatibility level, implemented, deployed, or available.

## Contribution boundary

- Canonical library sources live under `docs/capabilities/` in this repository.
- The corresponding human-facing index and detail pages are published through the existing `peecos/peecos-web` workflow after review.
- PIOS Solo implementation and roadmap work remain independent.
- Source repositories are read-only evidence inputs.
- Restricted evidence is assessed only in an owner-approved private location. Private source names, links, commits, excerpts, paths, and implementation details are not copied into public files.
- Public CRDs contain only requirements supported by publishable evidence or clearly marked project decisions.
- No CRD is silently adopted into the PIOS Core contract or a compatibility profile.

## Method

The project uses CRD Draft 0.4 at methodological revision `8f24ab01b2bf30409b364df5fd6b77b7bf89c29d`.

For each bounded tranche:

1. Bind exact source revisions and classify source roles.
2. Read the relevant material and create a statement-provenance ledger.
3. Reconcile requirements, implementation evidence, tests, deployment evidence, conflicts, and unknowns without conflating them.
4. Apply the Minimum Logical Element test to every candidate and every proposed combined element.
5. Separate reusable capability meaning from source-specific realization evidence.
6. Draft one CRD per accepted Capability MLE and update the inventory in the same pass.
7. Record PIOS architecture alignment, adoption, realization evidence, and availability independently.
8. Validate semantics, structure, links, and publication safety.

## Source roles

- **Current PIOS:** architecture authority for the event spine, five Core zones, Cotton, knowledge, History, processing, retrieval, governance, portability, distribution, system membership, deployment role, and state treatment.
- **PIOS Global at `4f1498ce5c390555abfad877d8284736f94d200b`:** historical design evidence, not current architecture authority.
- **Restricted application evidence:** requirements and implementation evidence assessed under owner authorization. Its identifying and substantive details remain outside public files unless separately cleared.
- **CRD method at `8f24ab01b2bf30409b364df5fd6b77b7bf89c29d`:** normative documentation method.

The public framework baseline for this milestone is committed revision `d6c4ccbb55db98b63b8ad8d0e7bca57bb4a427dc`. A separately verified owner-approved clarification working set was assessed for future alignment, but unpublished bytes are not public evidence for this contribution. Public capability claims must resolve to the committed baseline, another publishable source, or an explicit public project decision.

## Delivery phases

### Phase 0 — Repository and source binding

Establish this plan, contribution boundary, source contexts, exact public pins, restricted-evidence policy, and work status.

**Exit:** the public repository is the only working authority and all evidence roles are reproducible without publishing restricted material.

### Phase 1 — Cross-source pilot

Use the historical storage, retrieval, proposals, and rules documents; current PIOS architecture; and a restricted application assessment. Produce the bounded ledger before drafting, trace relevant implementation paths privately, apply the MLE test, preserve disagreements, and register accepted capabilities.

**Exit:** traceable public-safe CRDs, inventory entries, boundary decisions, alignment records, explicit unknowns, and restricted-evidence dispositions pass the method checks.

### Phase 2 — Corpus expansion

Classify the complete selected historical corpus, all admitted application documents, and relevant authored implementation files in bounded domain tranches. Inventorying a path is not substantive assessment. Every source item receives a capability, shared-element, realization-pattern, cross-cutting-context, historical-only, excluded, or unresolved disposition.

Planned tranches:

1. Knowledge and context: notes, profile, naming, glossary, labels, and context organization.
2. Actions and execution: action declarations, background work, execution models, and capability applications.
3. Events, results, operations, and portability.
4. Capture interfaces, onboarding, roles, and experience context.

### Phase 3 — CRD drafting

Phases 2 and 3 proceed together per tranche. Draft only after that tranche's evidence and boundary decisions are complete. Maintain source contexts, inventory, unresolved questions, and realization status in the same change.

**Exit:** each accepted Capability MLE has one coherent CRD and inventory entry.

### Phase 4 — Alignment and review

Complete the PIOS alignment matrix, terminology review, cross-cutting-rule applicability check, source/provenance review, and publication-safety review. Confirm that no implementation artifact was mistaken for a capability.

**Exit:** the selected corpus is classified, the library is internally consistent, and unknowns remain visible.

### Phase 5 — Website publication and evolution

Publish reviewed index and detail projections through `peecos/peecos-web`. Report repository revision, review/merge state, represented source revision, actual route, rendering checks, and deployment status separately. Source contribution alone is never reported as a live website update.

## Deliverables

- `capability-inventory.md`
- `crds/<capability-id>.md`
- `source-context/`
- `evidence/statement-provenance.md`
- `evidence/source-coverage.md`
- `decisions/capability-boundaries.md`
- `alignment/pios-architecture-alignment.md`
- `realizations/` containing only publication-cleared realization information
- `unresolved-questions.md`
- `work-status.md`

## Review and publication

Drafting uses focused self-review and local checks. A coherent initial milestone receives independent review before merge and website publication. Publication must use the existing website mechanism; no new application, hosting stack, remote runner, or paid environment is introduced.
