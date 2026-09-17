# Publish a completed-work record

## Identity
- **Name:** Publish a completed-work record
- **Definition:** Convert a meaningful completed work outcome into durable, evidence-linked completion records and owner-facing projections.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Make completed work visible and historically usable without depending on later reconstruction from raw traces.
- **Meaningful outcome:** At least one durable completed-work record exists, remains traceable to source evidence, and links any additional projections produced for the same completion.
- **Boundaries — includes:** meaningful-done qualification, completion event, owner-facing abstract, detail representation, History manifest, evidence links, history-day assignment, session grouping, and publication status.
- **Boundaries — excludes:** doing the work, generic event capture, generic update lifecycle, raw-log retention, and public release when not authorized.
- **Terms and concepts:** `update-first History` publishes structured completion evidence before using raw traces as fallback reconstruction.

## Interaction Contract MLEs
### Publish meaningful completion
- **Actor:** An authorized work owner, agent, workflow, or completion publisher.
- **Command / intent:** Record and surface that a bounded meaningful work outcome reached done.
- **Current state:** Canonical work state and sufficient result or verification evidence establish meaningful completion.
- **Policies / invariants:** Completion is not claimed without evidence; records produced for the same completion remain linked; sensitive or private detail follows publication policy; repeated publication is idempotent.
- **Transition:** Validate completion, create the authorized completion record and projections, and bind retained evidence.
- **Result:** A durable completed-work publication bundle with traceable source and status.
- **Events / effects:** Feeds owner attention, daily History, higher summaries, retrieval, and dashboards.
- **Unknowns:** Universal materiality thresholds for mandatory publication are not established.

## Rules and defaults
### Rules / invariants
- Raw chat, command output, or session traces alone do not prove meaningful completion.
- Public or external publication requires authority independent from internal completion recording.
### Recommended defaults
- Lead with a short owner-readable abstract and put technical evidence behind a linked detail artifact.
- For meaningful completed work, prefer a linked canonical event, concise update, readable detail, History manifest, and retained evidence reference when those projections are supported.

## Unknown / unresolved
- Grouping several related completions into one versus several updates remains context-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Meaningful completed work should be published as a linked event, update, detail, manifest, and retained evidence set. | recommended default | sourced | [C03](../evidence/statement-provenance.md). |
