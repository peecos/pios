# Promote a working artifact to canonical state

## Identity

- **Name:** Promote a working artifact to canonical state
- **Definition:** Move an accepted output from temporary or operational state into its designated durable source-of-truth lifecycle with preserved review and provenance.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Prevent drafts, working copies, intermediate outputs, and operational shadow state from silently becoming durable owner truth while allowing accepted value to enter its correct canonical home.
- **Meaningful outcome:** The candidate artifact is either promoted into a named canonical object/version with review and provenance, or receives an explicit rejected, deferred, conflicted, or failed disposition.
- **Boundaries — includes:** candidate artifact identity, source workspace/run, target canonical class/home, review state, approval state, validation, transformation, conflict handling, promoted-object identity/version, provenance, and disposition evidence.
- **Boundaries — excludes:** producing the artifact, deciding that an execution output qualifies as a Result, governing imported-source enrichment stages, maintaining the workspace, publishing outward, and deleting temporary state before promotion is verified.
- **Terms and concepts:** A `working artifact` is a non-canonical output or copy produced during work. `Canonical state` is the governed durable source-of-truth lifecycle appropriate to the object's information class; it need not be one physical location.

## Interaction Contract MLEs

### Promote an accepted artifact

- **Actor:** The owner or an explicitly authorized promotion process.
- **Command / intent:** Accept a bounded working artifact into its designated canonical lifecycle.
- **Current state:** The artifact, source work or workspace, proposed canonical class/home, review state, approval state, current canonical version, and authority are identifiable.
- **Policies / invariants:** Temporary state never becomes canonical implicitly; the target is selected by information type and governance rather than interface; source work and prior canonical versions remain traceable; conflicts and transformations are explicit; failed promotion leaves the only copy protected; approval does not imply outward publication.
- **Transition:** Validate the artifact and authority, resolve or record conflicts, create or revise the canonical object, bind provenance to the source artifact/work, verify durable acceptance, and record the disposition.
- **Result:** A verified promoted canonical object/version or an explicit rejected, deferred, conflicted, or failed promotion record.
- **Events / effects:** May make workspace cleanup, result linking, knowledge compilation, History inclusion, sharing, or publication eligible through separate capabilities.
- **Unknowns:** Universal review thresholds, conflict strategies, atomicity requirements, and temporary-copy retention periods are not established.

## Rules and defaults

### Rules / invariants

- No temporary, cached, model-generated, or operational artifact may become canonical merely because it exists or was used.
- Promotion must identify the resulting canonical object/version and preserve source-work provenance.
- The only remaining copy must not be discarded until durable acceptance is verified.

### Recommended defaults

- Prefer an explicit review and approval state for human-significant or high-impact artifacts.
- Keep working copies until promotion verification and any required rollback window complete.

## Unknown / unresolved

- See [U102–U105](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Temporary work becomes durable owner truth only through an explicit, attributable promotion into the appropriate canonical lifecycle. | rule/invariant | sourced | [V01–V08](../evidence/statement-provenance.md). |
