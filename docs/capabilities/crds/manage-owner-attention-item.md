# Manage an owner attention item

## Identity
- **Name:** Manage an owner attention item
- **Definition:** Create and resolve a durable owner-facing item that surfaces information, a decision, input request, warning, reminder, or completion requiring awareness or response.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Give owner-relevant attention needs a manageable lifecycle without treating them as canonical domain truth or chat messages.
- **Meaningful outcome:** An attention item is available with reason, source, priority, state, response options where needed, and durable resolution history.
- **Boundaries — includes:** creation, trigger reason, audience, priority, read/unread, pin, reveal/expiry, dismiss/archive, response, and source links.
- **Boundaries — excludes:** the underlying proposal or decision semantics, canonical event truth, chat conversation, push transport, and arbitrary notification spam.
- **Terms and concepts:** An `attention item` may be presented as an Update. It is durable enough to manage attention but is not the source of the fact it reports.

## Interaction Contract MLEs
### Maintain attention lifecycle
- **Actor:** An authorized capability, agent, system component, or owner.
- **Command / intent:** Surface and manage an owner-relevant attention need.
- **Current state:** A qualifying source event, state, decision need, reminder, or result exists.
- **Policies / invariants:** The source is linked; priority and reason are attributable; dismissal does not rewrite source truth; response is routed to the owning capability; transient delivery is not the sole durable record.
- **Transition:** Create or update the attention item and persist its presentation and resolution state.
- **Result:** A current or resolved owner attention item linked to its source.
- **Events / effects:** May trigger delivery through an allowed channel or route a response to another capability.
- **Unknowns:** Universal expiry and escalation rules are not established.

## Rules and defaults
### Rules / invariants
- Updates and chat remain separate domains.
- Resolving an attention item must not silently resolve its source object unless that source contract authorizes the transition.
### Recommended defaults
- Surface only owner-relevant state and preserve a human-readable reason.

## Unknown / unresolved
- Cross-device read, pin, and dismissal conflict resolution remains realization-specific.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Updates are a durable attention layer for owner awareness or response, not canonical truth or chat. | rule/invariant | sourced | [C02](../evidence/statement-provenance.md). |
