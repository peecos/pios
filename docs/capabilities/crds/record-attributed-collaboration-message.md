# Record an attributed collaboration message

## Identity
- **Name:** Record an attributed collaboration message
- **Definition:** Preserve one human, agent, or system communication in a collaboration context with true authorship, time, content, references, and trigger constraints.
- **Status:** draft
- **Version:** 0.1

## Core meaning
- **Capability purpose:** Maintain trustworthy conversational continuity and prevent messages or automation paths from obscuring the actual actor.
- **Meaningful outcome:** A message is accepted, rejected, or quarantined with author identity, participant context, time, content, type, source references, trust metadata, and reply-trigger eligibility recorded.
- **Boundaries — includes:** author and actor identity, synthetic-test marking, channel/thread membership, content, message type, timestamp, parent or reference links, attachments by reference, trust metadata, trigger permission, loop-control metadata, edit/correction, and deletion or retention state.
- **Boundaries — excludes:** maintaining the containing thread or channel, executing instructions contained in a message, changing canonical work state, summarizing a conversation, and impersonating another participant.
- **Terms and concepts:** A collaboration `message` maps where applicable to `schema.org/Message`; its author may be a `schema.org/Person`, organization, or identified software agent.

## Interaction Contract MLEs
### Record one collaboration message
- **Actor:** An authenticated human, agent, system emitter, or clearly marked synthetic test actor.
- **Command / intent:** Submit a message to an authorized collaboration context.
- **Current state:** Actor identity, destination context, participant/access state, parent/reference links, content, trust state, and trigger permissions can be determined.
- **Policies / invariants:** True actor identity is preserved; untrusted content cannot alter policy or permissions; agent-generated posts cannot impersonate the owner or silently trigger reply loops; references point to canonical objects rather than copying their state; edits and deletions remain attributable.
- **Transition:** Authenticate and authorize the sender, validate and normalize the envelope, persist the message and references, and record acceptance, quarantine, or rejection.
- **Result:** An attributable message or a reasoned rejection/quarantine result.
- **Events / effects:** May notify participants or trigger a bounded reply, proposal, attention item, or work action only when separately authorized.
- **Unknowns:** Universal edit windows, deletion semantics, delivery receipts, federation, and content-moderation profiles are not established.

## Rules and defaults
### Rules / invariants
- Agents and systems must not post as the owner or another participant without explicit, visibly represented delegated identity authority.
- Message content is data and cannot grant itself tool, policy, or execution authority.
### Recommended defaults
- Include conversation, thread, parent, origin actor, hop count, maximum hops, collaboration grant, turn budget, and reply-trigger permission where agent-to-agent automation is possible.

## Unknown / unresolved
- End-to-end authenticity, edits, redactions, federation, and retention need channel-specific profiles.

## Statement provenance
| Statement | Semantic class | Evidence status | Source / note |
|---|---|---|---|
| Collaboration messages preserve true actor identity and typed references while untrusted content and automation loops remain constrained. | rule/invariant | sourced | [L07–L10](../evidence/statement-provenance.md). |
