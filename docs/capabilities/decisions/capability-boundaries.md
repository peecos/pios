# Pilot capability-boundary decisions

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| M01 | Retain governed content | passes | separate CRD | Retention has its own actor, command, durable result, and failure independent of processing or use. |
| M02 | Derive content from a retained source | passes | separate CRD | Transformation has independent authority, provenance, state, and failure semantics. |
| M03 | Allocate retained content to a context | passes | separate CRD | It changes authorization eligibility without performing retrieval or processing. |
| M04 | Assemble governed retrieval context | passes | separate CRD | It produces a bounded context package before and independently of generation. |
| M05 | Consolidate conversation history | passes | separate CRD | It creates a reusable derivative with its own lifecycle and source links. |
| M06 | Decide a governed proposal | passes | separate CRD | Proposal disposition is independently meaningful and auditable. |
| M07 | Establish a standing rule | passes | separate CRD | It creates reusable authority and can succeed without a particular later match. |
| M08 | Apply a standing rule | passes | separate CRD | It evaluates one governed situation and produces a logged action, fallback, or no-action result. |
| M09 | Status/decision notification | fails as Capability MLE | Communication MLE owned by the triggering capability | The message is an effect and loses purpose without the underlying outcome. |

The symmetric MLE test requires `establish-standing-rule` and `apply-standing-rule` to remain separate capabilities because each passes independently. Their relationship is expressed through authority provenance and shared elements rather than by combining them into a rule-management feature bucket.

## Phase 2 knowledge-and-context tranche A1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| K-M01 | Maintain a personal glossary term | passes | separate CRD | An owner can establish or revise one stable local meaning with a determinable lifecycle outcome. |
| K-M02 | Manage an organizing label | passes | separate CRD | A label organizes/filter items without carrying the referential meaning of a glossary term. |
| K-M03 | Detect a candidate glossary term | passes | separate CRD | Detection produces a reviewable candidate and evidence without accepting it as truth. |
| K-M04 | Manage AI-assisted label vocabulary | passes | separate CRD | The vocabulary has an independent lifecycle and constrains later assignments. |
| K-M05 | Apply an AI-assisted label | passes | separate CRD | One assignment has a target, confidence/provenance, and reversible active state. |
| K-M06 | Apply contextual classification | passes | separate CRD | Attaching a Role or Mode to an object has independent contextual and historical meaning. |
| K-M07 | Glossary application | fails as one capability | split into K-M01 through K-M03 | The app/view grouping combines independently meaningful abilities. |
| K-M08 | AI-assisted labeling | fails as one capability | split into K-M04 and K-M05 | Vocabulary governance and individual assignment can succeed or fail independently. |

## Phase 2 knowledge-and-context tranche A2

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| K-M09 | Maintain a deliberate knowledge note | passes | separate CRD | Durable owner-chosen knowledge capture has its own lifecycle and outcome. |
| K-M10 | Maintain owner-authored profile knowledge | passes | separate CRD | The owner can revise self-description independently of observed/evidence-backed assertions. |
| K-M11 | Maintain an evidence-backed profile assertion | passes | separate CRD | A sourced assertion has independent provenance, confidence, validity, and lifecycle. |
| K-M12 | Resolve a disputed profile assertion | passes | separate CRD | A dispute has a distinct actor, decision, versioned result, and failure state. |
| K-M13 | Profile app | fails | source context and audience projection | It groups independently meaningful knowledge, goal, review, and navigation capabilities. |
| K-M14 | Attach a capability row to a note | fails as currently evidenced | realization pattern | The source describes a database/hook composition pattern rather than one stable user outcome. |

## Phase 2 actions-and-execution tranche B1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| B-M01 | Apply an action-intent label | passes | separate CRD | It records intended handling and succeeds without executing that handling. |
| B-M02 | Invoke a governed action | passes | separate CRD | It mediates one declared executable operation under authority and audit. |
| B-M03 | Run a background operation | passes | separate CRD | Asynchronous handoff, progress, cancellation/failure, and terminal result form an independent outcome. |
| B-M04 | Configure execution policy | passes | separate CRD | Changing allowable actions and confirmation posture is independently meaningful from performing an action. |
| B-M05 | Action Tag + Action | both pass | keep separate | Combining intent with execution would make a label silently executable. |
| B-M06 | Skills and Actions screen | fails | audience projection | A visibility/configuration surface groups multiple capabilities and artifacts. |
| B-M07 | Execution Model | fails | source context | It is a domain model containing multiple independently meaningful capabilities and object lifecycles. |
