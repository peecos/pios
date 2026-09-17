# Submit a governed content capture

## Identity
- **Name:** Submit a governed content capture
- **Definition:** Send owner-selected content and its source context into a governed intake boundary for validation and canonical acceptance.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Let device and application interfaces hand content to PIOS without becoming alternate canonical stores or bypassing intake governance.
- **Meaningful outcome:** A capture request receives a stable receipt and is either accepted for intake or retained as pending with an explicit disposition.
- **Boundaries — includes:** payload, source reference, original time when known, owner context, capture identity, optional metadata, submission status, and receipt.
- **Boundaries — excludes:** durable Core acceptance, source processing, action-intent execution, AI instruction execution, cache eviction, and application-specific scraping UI.
- **Terms and concepts:** A `capture` is a submitted candidate; it is not canonical Core content until accepted through the governed intake path.

## Interaction Contract MLEs
### Submit capture
- **Actor:** An authorized owner, device interface, application, or capture agent.
- **Command / intent:** Submit selected content and source context for Core intake.
- **Current state:** A payload, owner context, source information, and authorized capture path exist.
- **Policies / invariants:** Submission identity is stable; source provenance is preserved; duplicate retries are detectable; optional handling labels or instructions remain separate effects; failed transmission does not silently discard the only copy.
- **Transition:** Package and transmit the capture, record its pending/received state, and return a receipt.
- **Result:** An accepted-for-intake, pending, rejected, or retryable capture receipt.
- **Events / effects:** May create a pending-capture record and later invoke retention through the inbox.
- **Unknowns:** Universal payload limits and supported media classes are not established.

## Rules and defaults
### Rules / invariants
- A capture interface must not represent local submission as canonical acceptance without evidence.
- Capture-time action labels and instructions do not silently execute.
### Recommended defaults
- Preserve URL/source, title, original timestamp, content type, and integrity metadata when available.

## Unknown / unresolved
- Offline capture packaging and encryption requirements vary by device profile.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Capture submits content through governed intake while remaining distinct from canonical acceptance and later processing. | rule/invariant | sourced | [D01 and D03](../evidence/statement-provenance.md). |
