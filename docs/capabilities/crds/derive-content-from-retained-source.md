# Derive content from a retained source

## Identity

- **Name:** Derive content from a retained source
- **Definition:** Transform or analyze a governed source to produce a separately identifiable result with explicit provenance and processing state.
- **Status:** draft
- **Version:** 0.1

## Core meaning

- **Capability purpose:** Permit useful processing without losing source identity, integrity, or auditability.
- **Meaningful outcome:** A derivative, or a durable failure/cancellation outcome, is linked to its source and processing request.
- **Boundaries — includes:** operation request, authority check, processing state, derivative identity, source link, failure handling, and completion evidence.
- **Boundaries — excludes:** initial retention, context allocation, retrieval policy, provider selection, and downstream use of the derivative.
- **Terms and concepts:** `derivative` means a generated representation such as extracted text, summary, transcription, translation, classification, or conversion.

## Interaction Contract MLEs

### Produce a governed derivative

- **Actor:** An authorized owner or governed processing workflow.
- **Command / intent:** Apply a named transformation to a retained source.
- **Current state:** The source exists and the requested operation is known.
- **Policies / invariants:** Authority applies to the actual source; source identity remains intact; output provenance names source and operation; processing state is inspectable; retries do not create ambiguous success.
- **Transition:** Record the request, process under policy, preserve the derivative's identity and source link, and record terminal state.
- **Result:** A provenance-linked derivative or a reasoned failure/cancellation.
- **Events / effects:** Status communications may be emitted; the derivative may become eligible for later capabilities.
- **Unknowns:** Universal partial-result and human-correction semantics are not established.

## Rules and defaults

### Rules / invariants

- A derivative must not be represented as the unchanged source.
- Generated assertions remain attributable to their operation and source.

### Recommended defaults

- Preserve the original unchanged and create a separately identified derivative.
- Process asynchronously when completion is not predictably immediate.

### Communication MLEs

#### Processing state changed

- **Purpose:** Make meaningful processing progress or terminal state visible.
- **Trigger:** Processing reaches a reportable state.
- **Audience:** Owner or initiating actor.
- **Required meaning:** Identify the source, operation, state, and any required action without implying success prematurely.
- **Representative example text:** *Example; illustrative, not shipped copy:* “Processing completed and a linked result is available.”
- **Possible realizations:** event, update feed, inline status, notification, or API result.

## Unknown / unresolved

- See [U01](../unresolved-questions.md).

## Statement provenance

| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Source and derivative identities remain linked and distinct. | rule/invariant | sourced | [Pilot provenance P02](../evidence/statement-provenance.md). |
| Separate derivative output is preferred. | recommended default | sourced | Historical design and current PIOS state treatment. |
