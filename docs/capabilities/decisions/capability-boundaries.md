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
