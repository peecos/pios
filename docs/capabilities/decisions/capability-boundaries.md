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

## Phase 2 actions-and-execution tranche B2a

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| B-M08 | Maintain an execution plan | passes | separate CRD | A plan has an independent proposal, review, revision, and retained source-design outcome. |
| B-M09 | Activate an execution plan | passes | separate CRD | Activation creates a derived execution object and provenance receipt without performing that object's work. |
| B-M10 | Manage a one-off project | passes | separate CRD | A bounded effort has independent context, progress, responsibility, resolution, and failure semantics. |
| B-M11 | Maintain a reusable routine | passes | separate CRD | The reusable definition has a lifecycle independent from any concrete occurrence. |
| B-M12 | Run a routine instance | passes | separate CRD | One occurrence has its own actor, input snapshot, execution state, outputs, and terminal result. |
| B-M13 | Manage an actionable task | passes | separate CRD | One action can be captured, assigned, advanced, completed, or reopened independently of a project or list. |
| B-M14 | Organize a task collection | passes | separate CRD | Ordered grouping has a meaningful result while member tasks retain independent identity and state. |
| B-M15 | Schedule a contextual reminder | passes | separate CRD | A trigger, recurrence, snooze, and enabled lifecycle can succeed or fail without changing the reminded object's state. |
| B-M16 | Plan + activation | both pass | keep separate | Combining them would blur proposed design with the governed transition into execution. |
| B-M17 | Project + task | both pass | keep separate | A project can exist before all tasks are known, and tasks can exist without a project. |
| B-M18 | Routine + routine run | both pass | keep separate | Definition changes and execution outcomes have different actors, lifecycles, and histories. |
| B-M19 | Task + task collection | both pass | keep separate | Membership and ordering do not replace the task's actionable state. |
| B-M20 | Task + reminder | both pass | keep separate | A reminder resurfaces attention; it does not complete or otherwise execute the task. |
| B-M21 | Planning, Projects, Routines, To-dos, or Results app | fails | audience projection | Each view groups several independently meaningful objects, transitions, and operations. |

## Phase 2 actions-and-execution tranche B2b

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| B-M22 | Prepare a context-rich Work Starter | passes | separate CRD | It produces a ready-to-start contextual entry point without selecting or executing the work. |
| B-M23 | Order ready work for the current context | passes | separate CRD | It produces an explainable time-bounded ordering and can be rerun as context changes. |
| B-M24 | Maintain a versioned workflow package | passes | separate CRD | A distributable process contract has independent authorship, version, safety, and deprecation outcomes. |
| B-M25 | Manage an installed workflow | passes | separate CRD | Owner-scoped installation, configuration, enablement, and version policy exist independently of package authorship and runs. |
| B-M26 | Run a governed workflow | passes | separate CRD | One triggered execution has its own snapshots, steps, authority, terminal state, and evidence. |
| B-M27 | Preserve an execution result | passes | separate CRD | Registering produced value with execution provenance is meaningful independently of doing the work. |
| B-M28 | Work Starter + contextual ordering | both pass | keep separate | Preparation makes work ready; ordering selects among already eligible work for a particular context. |
| B-M29 | Workflow package + installed workflow | both pass | keep separate | A distributable definition and an owner's configured instance have different actors, authority, and lifecycle. |
| B-M30 | Installed workflow + workflow run | both pass | keep separate | Configuration may exist without a run, and each run has independent input, state, output, and failure semantics. |
| B-M31 | Workflow run + result | both pass | keep separate | Execution may fail or yield several outputs; a retained result is a separately qualified provenance-bearing outcome. |
| B-M32 | Result object + Results view | only result object passes | CRD for result preservation; view is projection | The view combines discovery, installation, runs, outputs, and review rather than one outcome. |
| B-M33 | Routine + workflow package | both pass with relationship unresolved | keep separate | A Routine is owner-facing reusable execution structure; a Workflow Package is a distributable declared process contract. |

## Phase 2 events-and-History tranche C1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| C-M01 | Record a canonical event | passes | separate CRD | One occurrence can be durably and idempotently appended independently of any owner-facing projection. |
| C-M02 | Manage an owner attention item | passes | separate CRD | Attention state, response, pin/read/dismiss lifecycle, and source linkage are independently meaningful. |
| C-M03 | Publish a completed-work record | passes | separate CRD | Meaningful completion creates a coherent event/update/detail/manifest/evidence outcome beyond generic attention management. |
| C-M04 | Compile daily owner History | passes | separate CRD | Daily compilation uniquely selects and narrates structured and fallback evidence for an owner-defined day. |
| C-M05 | Aggregate an owner History period | passes | separate CRD | Higher-level composition has different inputs, abstraction, closure, and gap semantics from daily compilation. |
| C-M06 | Navigate time-indexed owner History | passes | separate CRD | Traversal and retrieval produce relevant historical context without creating or changing source records. |
| C-M07 | Event + Update | both pass | keep separate | The event is canonical occurrence truth; the Update is a resolvable attention projection. |
| C-M08 | Generic Update + completed-work publication | both pass | keep separate | Generic attention can surface decisions or warnings, while completed-work publication requires a provenance-linked evidence bundle. |
| C-M09 | Daily + higher-period summary | both pass | keep separate | Daily may inspect source evidence; higher levels compose from closed lower-level summaries. |
| C-M10 | Unified Timeline / History view | fails as one capability | source context and audience projection | It combines navigation, filtering, summaries, updates, events, and source drill-down. |
| C-M11 | Notification delivery | fails as standalone Capability MLE | Communication MLE owned by the attention source | Delivery loses purpose without the update, reminder, incident, or decision it communicates. |

## Phase 2 operations-and-portability tranche C2a

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| C-M12 | Register a connected source | passes | separate CRD | Source identity, access, consent, sync, event mapping, and change behavior form an independently governed lifecycle. |
| C-M13 | Manage an import session | passes | separate CRD | One bounded intake event has its own manifest, progress, items, errors, and outcome independently from the source. |
| C-M14 | Govern source promotion | passes | separate CRD | Moving material among parked, analyzed, mapped, enriched, and History-included states changes eligibility and authority without performing every processing step. |
| C-M15 | Screen an ingestion batch | passes | separate CRD | A technical reviewer can produce an evidence-based pass/fail result without authorizing upload. |
| C-M16 | Assess ingestion readiness | passes | separate CRD | Checklist closure produces an independent readiness result while preserving unresolved owner decisions. |
| C-M17 | Authorize an ingestion batch | passes | separate CRD | The owner can grant or deny authority for an exact manifest and boundary without performing the ingestion. |
| C-M18 | Govern an event-type registry | passes | separate CRD | Adding or revising an event type changes allowed semantics, emitters, schemas, and projection obligations independently from recording any event. |
| C-M19 | Inspect an operational run record | passes | separate CRD | An owner or operator can retrieve one run's state, evidence, outputs, errors, and authority trail without changing canonical state. |
| C-M20 | Source + import session | both pass | keep separate | A source persists across zero or many bounded intake sessions. |
| C-M21 | Import session + source promotion | both pass | keep separate | Intake scope and progress can complete while later mapping, enrichment, or History inclusion remains pending. |
| C-M22 | Technical screen + checklist + owner approval | all pass | keep separate | Each gate has a distinct actor, evidence standard, result, and expressly limited authority. |
| C-M23 | Event registry + event recording | both pass | keep separate | Registry governance defines allowed event semantics; recording appends one conforming occurrence. |
| C-M24 | System app | fails | audience projection | It groups independent inspection, governance, run, import, export, and health capabilities. |

## Phase 2 operations-and-portability tranche C2b1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| C-M25 | Compose a portable Core bundle | passes | separate CRD | Bundle creation has its own scope, identity, manifest, contents, exclusions, and completion result. |
| C-M26 | Validate a portability package | passes | separate CRD | Validation can accept, reject, or quarantine an existing package without creating or importing it. |
| C-M27 | Restore Core state from a bundle | passes | separate CRD | Import/hydration changes destination state and produces an operationalization report independently from validation. |
| C-M28 | Validate restored Core parity | passes | separate CRD | Destination evidence can pass or fail after restore and is not established by successful byte import alone. |
| C-M29 | Maintain a recoverable Core backup | passes | separate CRD | Backup creation, custody, retention, and restore testing form a recurring recovery outcome independent from owner portability exports. |
| C-M30 | Bundle composition + validation | both pass | keep separate | A package can be created but invalid, or an externally supplied package can be validated without being created locally. |
| C-M31 | Package validation + restore | both pass | keep separate | Technical validity does not authorize or perform destination state changes. |
| C-M32 | Restore + parity validation | both pass | keep separate | Restored bytes may exist while required protections, provenance links, retrieval, or service behavior remain unproven. |
| C-M33 | Export bundle + backup | both pass | keep separate | Portability export serves owner transfer/takeover; backup serves protected recovery and may use different retention and custody. |

## Phase 2 operations-and-portability tranche C2b2

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| C-M34 | Govern a Core cutover | passes | separate CRD | Canonical-side transfer has its own bounded scope, authority, final-delta, and completion decision. |
| C-M35 | Roll back a Core cutover | passes | separate CRD | Reverting an attempted transition has an independent actor, trigger, state restoration, and evidence outcome. |
| C-M36 | Decommission a source Core | passes | separate CRD | Retirement occurs after successful transition and has distinct retention, deletion, revocation, and closure evidence. |
| C-M37 | Register an owner-data erasure request | passes | separate CRD | The request immediately records intent and may suppress exposure even when physical deletion is delayed. |
| C-M38 | Execute governed data erasure | passes | separate CRD | Physical or cryptographic erasure and derived cleanup have independent authority, timing, proof, and failure semantics. |
| C-M39 | Reauthorize a destination connector | passes | separate CRD | Re-establishing source credentials and future-sync authority is meaningful independently from restoring connector descriptions. |
| C-M40 | Cutover + rollback | both pass | keep separate | One establishes destination canonical authority; the other restores or preserves the prior canonical path after a failed or reversed transition. |
| C-M41 | Cutover + decommissioning | both pass | keep separate | Cutover can complete while source retention and retirement remain intentionally deferred. |
| C-M42 | Erasure request + erasure execution | both pass | keep separate | Request and exposure suppression may succeed while retention prevents immediate physical deletion. |
| C-M43 | Restore + connector reauthorization | both pass | keep separate | Portable descriptions may be restored without importing credentials, device trust, or future-sync authority. |
