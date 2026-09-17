# Manage an import session

## Identity
- **Name:** Manage an import session
- **Definition:** Track one bounded owner-visible intake event for a defined set of source items from preparation through terminal outcome.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make a discrete intake operation inspectable without collapsing it into the persistent source or its processing jobs.
- **Meaningful outcome:** The session has a stable identity, bounded manifest, source links, progress, item dispositions, errors, and terminal status.
- **Boundaries — includes:** session creation, scope manifest, source association, item counts, progress, pause/resume where supported, errors, cancellation, completion, and produced-reference summary.
- **Boundaries — excludes:** source registration, content retention itself, individual parsing/enrichment jobs, source promotion decisions, and owner authorization for a future batch.
- **Terms and concepts:** An `import session` is one intake occurrence involving one or more source items.

## Interaction Contract MLEs
### Maintain import-session lifecycle
- **Actor:** An authorized owner, connector, intake workflow, or import operator.
- **Command / intent:** Start, track, or close one bounded intake session.
- **Current state:** A registered or identified source and a bounded candidate set exist.
- **Policies / invariants:** Scope remains attributable; duplicate items are detectable; progress and failures are durable; source identity is preserved; completion does not imply enrichment or History inclusion.
- **Transition:** Create the session, associate candidate items, persist progress and dispositions, and close with an explicit outcome.
- **Result:** A completed, failed, cancelled, paused, or intervention-required import-session record.
- **Events / effects:** May create retained items, baseline events, processing jobs, updates, or review requests through their own contracts.
- **Unknowns:** Universal retry and partial-completion semantics are not established.

## Rules and defaults
### Rules / invariants
- A session must not become the identity of the persistent source.
- Session completion must not be represented as approval for deeper processing.
### Recommended defaults
- Preserve exact scope, source, counts, failures, and produced references.

## Unknown / unresolved
- Cross-session duplicate and resume behavior depends on source-specific identity guarantees.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| An import session is a bounded intake event independent from its source and later promotion. | capability purpose | sourced | [C09](../evidence/statement-provenance.md). |
