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
