# Govern a derived-representation lifecycle

## Identity

- **Name:** Govern a derived-representation lifecycle
- **Definition:** Register, distinguish, supersede, rebuild, revoke, and dispose of source-linked non-canonical representations.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Keep generated text, graph, vector, summary, index, and multimodal projections inspectable and governable after their production.
- **Meaningful outcome:** Every retained representation has an identifiable source/version, representation identity, processing provenance, authority basis, lifecycle state, and replacement or deletion disposition.
- **Boundaries — includes:** registry identity, source and source-version links, logical Core reference, representation type, processing profile/model/version, format or dimensions, confidence, sensitivity, consent/authorization basis, retention, physical reference, lifecycle state, replacement, rebuild, revocation, and deletion evidence.
- **Boundaries — excludes:** producing the derivative, retaining the original source, defining provider technology, resolving graph entities globally, assembling retrieval context, and treating the representation as canonical meaning.
- **Terms and concepts:** A `derived representation` is a source-linked projection such as a text chunk, extracted metadata, OCR output, summary, graph snapshot, semantic or multimodal vector, or retrieval index. Provider paths and payload keys are implementation metadata.

## Interaction Contract MLEs

### Reconcile a representation's lifecycle

- **Actor:** An authorized processing, knowledge-maintenance, retrieval, retention, or deletion-governance process.
- **Command / intent:** Register or change the governed lifecycle state of a retained derived representation.
- **Current state:** The source/version and representation output or existing registry record are identifiable; applicable sensitivity, authorization, retention, and deletion rules are available.
- **Policies / invariants:** The representation remains linked to its exact source/version; incompatible models, dimensions, modalities, formats, or semantic spaces retain distinct identities; a replacement does not silently erase the sole historical representation; non-authoritative and rebuildable status remain explicit; revocation and deletion follow source and consent lifecycle; physical location does not define canonical meaning.
- **Transition:** Validate identity and provenance, register or reconcile metadata, apply the requested active/deprecated/superseded/rebuildable/deleted disposition, preserve replacement history, and record any failed or blocked cleanup.
- **Result:** An inspectable lifecycle record with the representation's current status, provenance, replacement relation, and retention/deletion disposition, or a reasoned failure.
- **Events / effects:** May trigger retrieval exclusion, rebuilding, index refresh, graph-resolution review, portability treatment, or governed deletion without performing the source transformation itself.
- **Unknowns:** Universal equivalence rules, lifecycle vocabulary, retention periods, provider cleanup proofs, and cross-index atomicity are not established.

## Rules and defaults

### Rules / invariants

- A derived representation must never silently replace its source or become canonical truth.
- Representation identity must distinguish incompatible processing spaces.
- Excluded, revoked, stale, or deleted representations must fail closed in retrieval and downstream processing according to their disposition.

### Recommended defaults

- Preserve an immutable source-local snapshot when global resolution could erase source-specific claims or ambiguity.
- Retain enough provenance to rebuild or explain the representation without making provider-specific keys canonical.

## Unknown / unresolved

- See [U98–U101](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Retained derived representations require source/version identity, processing provenance, lifecycle state, replacement history, and governed revocation/deletion while remaining non-canonical projections. | rule/invariant | sourced | [T09–T17](../evidence/statement-provenance.md). |
