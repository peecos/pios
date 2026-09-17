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
| C-M25A | Compose a source-derived PIOS portability package | passes | separate CRD | An owner or migration actor can assemble non-Core source material into a validation-ready package without claiming that it is existing Core state. |
| C-M26 | Validate a portability package | passes | separate CRD | Validation can accept, reject, or quarantine an existing package without creating or importing it. |
| C-M27 | Restore Core state from a bundle | passes | separate CRD | Import/hydration changes destination state and produces an operationalization report independently from validation. |
| C-M28 | Validate restored Core parity | passes | separate CRD | Destination evidence can pass or fail after restore and is not established by successful byte import alone. |
| C-M29 | Maintain a recoverable Core backup | passes | separate CRD | Backup creation, custody, retention, rotation, and integrity status form a recurring protection outcome independent from owner portability exports and restore execution. |
| C-M30 | Bundle composition + validation | both pass | keep separate | A package can be created but invalid, or an externally supplied package can be validated without being created locally. |
| C-M31 | Package validation + restore | both pass | keep separate | Technical validity does not authorize or perform destination state changes. |
| C-M32 | Restore + parity validation | both pass | keep separate | Restored bytes may exist while required protections, provenance links, retrieval, or service behavior remain unproven. |
| C-M33 | Export bundle + backup | both pass | keep separate | Portability export serves owner transfer/takeover; backup serves protected recovery and may use different retention and custody. |
| C-M33A | Core-export composition + source-composed package creation | both pass | keep separate | One serializes existing Core state; the other prepares owner-controlled source material whose canonical Core status does not yet exist. |
| C-M33B | Backup maintenance + restore/parity testing | all pass | keep separate | A backup can be created and integrity-checked without restoring it; restore changes destination state, and parity separately evaluates the restored result. |

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

## Phase 2 capture-and-experience tranche D1a

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| D-M01 | Submit a governed content capture | passes | separate CRD | Submission has an independent actor, payload, source context, acceptance request, and receipt. |
| D-M02 | Reconcile a pending capture | passes | separate CRD | Pending work has a separate lifecycle and can end accepted, retryable, failed, preserved, or authorized-discarded. |
| D-M03 | Web clipping extension | fails as generic capability | realization and audience projection | Browser scraping, authentication, tag UI, and API transport implement capture and adjacent capabilities. |
| D-M04 | Capture + action-intent labeling | both pass | keep separate | Content can be captured without a handling label, and a label can be applied after capture. |
| D-M05 | Capture + processing instruction | both pass | keep separate | Intake does not itself authorize or perform the requested processing action. |
| D-M06 | Submit + reconcile pending capture | both pass | keep separate | Submission may complete before durable acceptance, and reconciliation may resume after device or network interruption. |

## Phase 2 capture-and-experience tranche D1b1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| D-M07 | Manage a guided onboarding journey | passes | separate CRD | The journey has durable stage, progress, pause/resume, response, override, and terminal outcomes independent from any one setup result. |
| D-M08 | Maintain a personal AI identity | passes | separate CRD | Owner-authored presentation identity has its own versioned lifecycle and remains distinct from owner profile, memory, runtime role, and authority. |
| D-M09 | Configure personal AI interaction preferences | passes | separate CRD | Communication and collaboration preferences can change without changing identity, truth, or execution permission. |
| D-M10 | Verify an onboarding contact channel | passes through a reusable capability | reuse `verify-contact-point-control` with an onboarding profile | Channel-control evidence has an independent assurance result, but binding it to onboarding does not change the generic contact-point verification outcome. |
| D-M11 | Prepare an initial owner environment | passes | separate CRD | Mapping owner input and explicit defaults into a reviewable first configuration has an independent readiness outcome. |
| D-M12 | Authorize first entry | passes | separate CRD | A bounded invitation credential has its own issue, expiry, replacement, validation, and consumption lifecycle. |
| D-M13 | Adaptive onboarding depth | fails independently | owned policy of guided onboarding | It changes which questions and defaults the journey uses but does not produce a separate durable owner outcome. |
| D-M14 | First-use orientation carousel | fails as generic capability | Communication MLE and realization pattern | A skippable/replayable explanatory surface communicates product concepts but does not establish onboarding identity, readiness, or authority. |
| D-M15 | Preserve onboarding dialogue as first conversation | fails independently | composition | Retention, conversation continuity, and first-entry presentation already own the durable outcomes. |
| D-M16 | Download onboarding data | fails independently in this tranche | specialization of portability | Onboarding scope specializes portable bundle composition rather than defining a second export capability. |
| D-M17 | Personal AI identity + interaction preferences | both pass | keep separate | Presentation identity can remain stable while communication behavior changes, and either may be revised independently. |
| D-M18 | Journey + environment preparation + first-entry authorization | all pass | keep separate | Progress coordination, configuration readiness, and access authorization have different actors, evidence, failure modes, and outcomes. |

## Phase 2 capture-and-experience tranche D1b2

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| D-M19 | Maintain an owner context Role | passes | separate CRD | Role definition, hierarchy, provenance, and lifecycle produce a durable owner-context outcome independently from activation or object tagging. |
| D-M20 | Maintain an owner operating Mode | passes | separate CRD | A reusable Mode definition can be created, revised, archived, or restored independently from whether it is currently active. |
| D-M21 | Set active personal context | passes | separate CRD | A temporary multi-dimensional context snapshot has its own source, timing, supersession, and inheritance outcome. |
| D-M22 | Configure a Role's outward intent | passes | separate CRD | An owner can declare or withdraw a Role's representation intent without publishing content or granting access. |
| D-M23 | Prepare a Role-scoped outward representation | passes | separate CRD | Creating a separate traceable outward object is meaningful before access or publication and protects the private source from implicit exposure. |
| D-M24 | Role definition + Mode definition | both pass | keep separate | Roles describe owner capacities and may form type/instance hierarchies; Modes describe situational operating context and are normally more transient. |
| D-M25 | Active context + contextual classification | both pass | keep separate | Active context is a temporary snapshot; contextual classification records a durable relationship to a particular object. |
| D-M26 | Role outward intent + outward representation | both pass | keep separate | Intent can exist with no prepared content, and a prepared representation remains unpublished and inaccessible until later governance permits use. |
| D-M27 | Outward representation + publication/access | passes only for preparation here | keep later exposure capabilities separate | Preparation does not establish visibility, discovery, access control, rights, delivery, or publication. |
| D-M28 | Role management screen or context picker | fails as generic capability | audience projection and realization pattern | Controls compose definition maintenance, active-context selection, and contextual classification. |
| D-M29 | Home, app navigation, layout, gestures, badges, and onboarding slides | fail as generic capabilities | audience/communication/realization patterns | These surfaces present or invoke several capabilities but do not produce independent domain outcomes. |

## Phase 2 patterns-and-learning tranche E1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| E-M01 | Detect an observed pattern | passes | separate CRD | Multi-evidence recurrence analysis can create or decline one emerging non-authoritative pattern with a determinate outcome. |
| E-M02 | Evaluate an observed pattern lifecycle | passes | separate CRD | A recurring evaluator can independently update status, strength, eligibility, and snapshots for an existing pattern. |
| E-M03 | Record one pattern-evidence row | fails as capability | shared data/information MLE | The record has purpose only inside detection/evaluation and does not deliver an independently meaningful owner outcome. |
| E-M04 | Maintain pattern-segment vocabulary | passes in generic form already represented | reuse `manage-organizing-label` | Pattern segments specialize owner-governed organizational vocabulary rather than requiring a second generic vocabulary capability. |
| E-M05 | Generate and decide a proposal from a stable pattern | passes in generic form already represented | reuse `decide-governed-proposal` | Pattern eligibility supplies evidence and rationale; proposal lifecycle and decision remain governed by the existing capability. |
| E-M06 | Detect + lifecycle-evaluate a pattern | both pass | keep separate | Initial creation and later recurring reassessment have different starting states, timing, and results. |
| E-M07 | Patterns inspector | fails as generic capability | audience projection | It presents pattern, evidence, status, and proposal history without owning their source lifecycles. |
| E-M08 | Pattern refresh action declaration | fails as realization proof | declared/disabled realization metadata | A declared disabled action is not evidence of a reachable recurring job or available capability. |

## Phase 2 direction-and-success tranche E2

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| F-M01 | Maintain an outcome goal | passes | separate CRD | A durable desired outcome has its own owner, lifecycle, horizon, relationships, and review context independently from current execution. |
| F-M02 | Maintain a directional objective | passes | separate CRD | Current actionable direction can be created, activated, retired, and used to source planning without becoming the plan itself. |
| F-M03 | Maintain a success target | passes | separate CRD | An observable success condition has an independent lifecycle and can exist without a measurement observation or achievement decision. |
| F-M04 | Maintain a measurement definition | passes | separate CRD | Unit, value semantics, tracking method, and comparability form a reusable definition independently from recorded values. |
| F-M05 | Record a metric observation | passes | separate CRD | One time-scoped value has its own actor, validation, source, provenance, correction, and acceptance result. |
| F-M06 | Goal + objective | both pass | keep separate | Long-horizon desired outcome and current action-oriented direction can change independently and may be linked without being merged. |
| F-M07 | Target + measurement definition | both pass | keep separate | Success can be described before deciding how it will be measured, and a measurement can serve monitoring without being a target. |
| F-M08 | Measurement definition + metric observation | both pass | keep separate | A stable definition may receive many observations, while definition changes require independent comparability handling. |
| F-M09 | Target + target-achievement evaluation | target passes; evaluation deferred | keep separate | Defining success and deciding whether evidence satisfies it have different inputs, authority, and outcomes; the latter contract is not yet complete. |
| F-M10 | Goals/Profile/Planning screens | fail as generic capabilities | audience projections | Multiple screens can present the same canonical direction and success objects without becoming independent realizations. |
| F-M11 | Goal → objective → target → plan chain | fails as mandatory combined capability | conceptual composition | The sequence helps explain flow, but sources explicitly do not enforce every link and each constituent MLE remains independently meaningful. |

## Phase 2 outward-exposure tranche E3

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| G-M01 | Share a governed outward representation | passes | separate CRD | Delivering or activating a representation for a bounded audience has its own share reference and lifecycle without creating access policy or making content public. |
| G-M02 | Publish a governed outward representation | passes | separate CRD | Public reachability is an externally visible transition with revision, locator, authority, withdrawal, and evidence independent from preparation or sharing. |
| G-M03 | Maintain outward access policy | passes | separate CRD | Access conditions and audience grants can be created, revised, suspended, expired, revoked, or superseded without evaluating a particular request. |
| G-M03A | Evaluate an outward access request | passes | separate CRD | One requester can receive an attributable allow, deny, challenge, or indeterminate decision under an unchanged policy. |
| G-M04 | Govern outward discoverability | passes | separate CRD | Hidden, index-eligible, and promoted states produce an independent findability outcome without changing who may open or reuse content. |
| G-M05 | Govern outward usage rights | passes | separate CRD | Human and machine use conditions remain meaningful after access and can change without altering reachability or discovery. |
| G-M06 | Controlled sharing + public publication | both pass | keep separate | Sharing is audience-bounded and non-public; publication establishes public reachability and may carry durable public-presence framing. |
| G-M07 | Visibility + access policy + access evaluation + discovery + rights | all meaningful; do not merge | keep separate concerns | Current and historical sources support independent state or outcomes for each concern. |
| G-M08 | Prepare + share/publish | both pass | keep separate | A representation can be safely prepared and reviewed without any audience gaining access; exposure is a later authorized transition. |
| G-M09 | Unpublish or revoke | fails as additional generic capability here | lifecycle transition | Withdrawal is an essential terminal transition of the corresponding publication or sharing capability, while cross-system erasure remains separate. |
| G-M10 | Public username, path, folder, domain, sitemap and SEO/GEO | fail as one generic capability | realization patterns and later candidates | They implement public presence, addressing, organization, discovery, and delivery but do not form one minimal reusable outcome. |
| G-M11 | Access-policy maintenance + access-request evaluation | both pass | keep separate | Policy changes are durable governance transitions; request evaluation applies the current policy to one request without changing it. |
| G-M12 | Controlled sharing + access policy + request evaluation | all pass | keep separate | A share can be activated under an existing policy, a policy can exist before any share request, and each access request can be decided independently. |

## Phase 2 reviews-and-reflection tranche E4

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| H-M01 | Conduct a structured review | passes | separate CRD | A bounded review has its own scope, questions, inputs, decisions, unresolved items, carry-forward disposition, and closure state. |
| H-M02 | Record a reflective assessment | passes | separate CRD | Interpretation with judgment, uncertainty, residue, and recommendations can be preserved independently from a formal review or neutral summary. |
| H-M03 | Structured review + reflection | both pass | keep separate | A review may be primarily factual or decisional, and a reflection may occur outside a scheduled review; either can exist without the other. |
| H-M04 | Daily, weekly, monthly, yearly, and event-triggered review | passes as one generic capability | use profiles, not separate CRDs | Cadence and question sets vary while the review interaction contract remains the same. |
| H-M05 | Review note or review screen | fails as generic capability | output/audience projection | A note or screen can present a review but does not own its evidence, decisions, and follow-up lifecycle. |
| H-M06 | Carry forward unresolved work | passes through existing capabilities | reuse composition | A review references existing tasks, Work Starters, attention items, goals, or projects rather than creating a second work identity. |
| H-M07 | Apply review recommendations | passes through existing governed capabilities | reuse composition | Recommendations may trigger proposals or updates to goals, targets, projects, tasks, knowledge, or policy only through their own authority paths. |

## Phase 2 people-and-relationships tranche E5

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| I-M01 | Maintain a human contact profile | passes | separate CRD | Another person's owner-held profile has a distinct subject, authority, provenance, lifecycle, and knowledge outcome. |
| I-M02 | Maintain a contact point | passes | separate CRD | A typed coordinate can be created, corrected, prioritized, invalidated, or removed independently from the wider profile and relationship. |
| I-M03 | Verify control of a contact point | passes | separate reusable CRD | Verification has its own actor, challenge/evidence state, assurance, expiry, and result and is reused by contact and onboarding contexts. |
| I-M04 | Maintain personal relationship context | passes | separate CRD | Relationship meaning, scope, trust, consent, origin, validity, and history change independently from participant identity and contact coordinates. |
| I-M05 | Person identity + contact profile | both pass | keep separate | A named person can exist in the glossary/world model without a maintained relationship profile, and profile knowledge can reference the identity without replacing it. |
| I-M06 | Contact profile + contact point | both pass | keep separate | One profile may have zero or many changing contact points; coordinates can be invalidated without retiring the person profile. |
| I-M07 | Contact point + control verification | both pass | keep separate | A value can be stored while unverified, and verification can expire or be revoked without deleting the value. |
| I-M08 | Relationship origin | fails independently at current evidence depth | shared information/provenance MLE | Origin date, place, introduction and story support relationship context but no separate recurring interaction contract is established. |
| I-M09 | With-whom event context + durable relationship context | both pass through existing capabilities | keep separate | Event participation is time-scoped contextual classification; durable relationship meaning has its own lifecycle and authority. |
| I-M10 | Contacts application, filters, avatar and list | fail as generic capabilities | audience projections and realization patterns | They present or edit contact, contact-point, Role and label capabilities without owning independent domain outcomes. |

## Phase 2 agents-and-outward-identity tranche E6

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| J-M01 | Maintain an agent definition | passes | separate CRD | A persistent agent's governed purpose, responsibilities, skills, limits, permissions, memory/source scopes, instructions, state, and versions form an independent durable outcome. |
| J-M02 | Synchronize an agent definition to runtime | passes | separate CRD | Applying and verifying one canonical version across runtime targets has independent source, target, transformation, failure, intentional-difference, and rollback states. |
| J-M03 | Assign an agent runtime role | passes | separate CRD | A bounded functional role has its own assigner, scope, duration, responsibility and terminal state without changing persistent identity. |
| J-M04 | Select an agent's outward identity | passes | separate CRD | Identity presentation and disclosure for an external action are independently governed before the action executes. |
| J-M05 | Conduct an owner-representative conversation | passes | separate CRD | One external conversational interaction has a distinct participant, identity, knowledge scope, policy, response/refusal, escalation, and evidence outcome. |
| J-M06 | Agent identity + runtime role | both pass | keep separate | One identity may occupy several roles over time, and the same role can be assigned to different agents without redefining either. |
| J-M07 | Agent definition + runtime synchronization | both pass | keep separate | A canonical definition can change without being deployed, and synchronization can fail or intentionally diverge without changing source truth. |
| J-M08 | Outward identity + external action | both pass | keep separate | Selecting who appears to act and what is disclosed does not itself authorize or deliver the external effect. |
| J-M09 | Personal-AI identity + outward identity | both pass | keep separate | A persistent private presentation identity can remain stable while each outward action uses a different represented party or disclosure posture. |
| J-M10 | AI Twin | fails as one generic Capability MLE | composed product realization | It bundles agent definition, identity, dedicated knowledge allocation, access, publication/sharing, retrieval, conversation, and governance capabilities. |
| J-M11 | Director/manager/worker hierarchy | fails as universal fixed taxonomy | implementation profile | Runtime-role assignment is reusable; named hierarchy levels are one orchestration vocabulary rather than mandatory PIOS roles. |

## Phase 2 collaboration-and-execution-workspace tranche E7

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| L-M01 | Maintain a collaboration channel | passes | separate CRD | A durable top-level conversation container has independently meaningful identity, audience, purpose, ordering, visibility and lifecycle outcomes. |
| L-M02 | Maintain a work-linked discussion thread | passes | separate CRD | A focused discussion has its own root reference, participants, state, summary and resolution lifecycle without owning the linked subject. |
| L-M03 | Record an attributed collaboration message | passes | separate CRD | One attributable communication has an independent sender, context, content, references, trust state, trigger eligibility and acceptance outcome. |
| L-M04 | Manage a task-scoped execution workspace | passes | separate CRD | A bounded runtime area has its own provisioning, isolation, temporary-state, output-disposition, cleanup and failure lifecycle. |
| L-M05 | Collaboration channel + discussion thread | both pass | keep separate | A channel can exist with zero or many threads, while a focused thread can move or be linked without redefining its containing channel. |
| L-M06 | Discussion thread + collaboration message | both pass | keep separate | A thread persists across many messages and lifecycle transitions; a message remains one attributable communication that can also exist without a work-linked thread. |
| L-M07 | Delegation or assignment | passes through existing work-object capabilities | reuse composition | Responsibility and assignee state belong to the applicable task, project, workflow, background operation or runtime-role contract rather than a second generic delegation object. |
| L-M08 | Multi-agent orchestration | fails as one generic Capability MLE | composed workflow/profile | Planning, assignment, role binding, execution, monitoring, communication, handoff, result preservation and escalation have separate actors and outcomes. |
| L-M09 | Execution handoff | fails independently at current evidence depth | shared transition and existing-capability reuse | Durable source/target/status/provenance fields support transitions among work and background-operation contracts, but no additional universal outcome is established. |
| L-M10 | Circle application | fails as one generic capability | audience projection and composed realization | Circle combines channel, thread, message, attention, agent, work-reference and navigation capabilities through one replaceable harness. |

## Phase 2 conversation-history-and-personal-interfaces tranche F1

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| N-M01 | Maintain personal conversation history | passes | separate CRD | Conversation continuity has independent admission, ordering, provenance, correction/hiding, source-awareness and lifecycle outcomes across many interactions and views. |
| N-M02 | Maintain an owner access path | passes | separate CRD | A route to owner control has independently meaningful identity, role, assurance, supported operations, priority, health, verification and retirement state. |
| N-M03 | One physical chat history per owner | fails as a universal requirement | implementation profile | One logical continuity outcome is supported, but current PIOS can preserve it through retained sources and events without requiring one table or stream. |
| N-M04 | Collaboration message + personal conversation history | both pass | keep separate | One message can be recorded independently, while history governs continuity, membership, ordering and provenance across many interactions and sources. |
| N-M05 | Personal conversation history + canonical event log | both pass with distinct scopes | keep separate | Conversation history is a communication-domain continuity record; the event log is the complete cross-domain canonical occurrence spine. |
| N-M06 | Imported-history integration | fails as one generic capability | reuse composition | It combines retention, import sessions, source promotion, history membership, retrieval allocation, summaries, pattern detection and proposal governance. |
| N-M07 | Persistent personal memory | fails as one generic Capability MLE | architecture composition | It names the cumulative outcome of sources, events, notes, conversations, knowledge, relationships, decisions, retrieval and derived representations. |
| N-M08 | Ally Panel, PIOS Panel, Home Panel and app navigation | fail as generic capabilities | audience projections and realization patterns | They arrange access to independently meaningful capabilities but do not own additional domain outcomes. |
| N-M09 | Execution Tracking Surface | passes through existing capabilities | audience projection | Operational-run inspection, work-object state, background-operation state, artifacts and results already provide the underlying outcomes. |
| N-M10 | Owner access path + domain authorization | both pass | keep separate | Registering or reaching an interface does not grant permission for every action exposed through it. |

## Phase 2 device-continuity-and-reading tranche F2

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| Q-M01 | Maintain an authorized device-local content cache | passes | separate CRD | Creating, reusing, inspecting, refreshing, or removing a permitted non-canonical local copy creates an independent availability outcome; detailed freshness and eviction profiles remain unresolved. |
| Q-M02 | Maintain selected content for offline access | passes | separate CRD | Deliberately retained local availability remains meaningful without opportunistic caching; detailed authorization, expiry, revocation, and reconnection profiles remain unresolved. |
| Q-M03 | Manage a personal reading queue | passes | separate CRD | Source-linked admission and unread, read, saved, archived or removed state create a coherent owner outcome independent of source storage and rendering. |
| Q-M04 | Recent cache + selected offline content | both pass | keep separate | One outcome supports automatic local-copy lifecycle management; the other records deliberate owner selection for disconnected availability. |
| Q-M05 | Device-local content + pending capture/edit | both pass through separate capabilities | keep separate | Accepted local copies and unconfirmed submitted work have different authority and disposition states; pending work requires explicit reconciliation rather than cache cleanup. |
| Q-M06 | Shared App Group or local database | fails as a capability | implementation mechanism and trust boundary | Shared storage supports cache or offline realization but cannot itself express per-app authorization or canonical truth. |
| Q-M07 | Reader application | fails as one generic capability | audience projection and composed realization | It combines queue state, source retrieval, presentation preferences, classification, summary display, derivation and export actions. |
| Q-M08 | Save-for-later and mark-read controls | fail independently at this evidence depth | interaction transitions inside reading-queue management | The source establishes lifecycle state changes within one reading purpose, not portable standalone capabilities with broader consumers. |
| Q-M09 | AI-organized reading topics | passes through existing capabilities | reuse contextual classification and assisted labels | Topic generation organizes queue items but does not require a new reading-specific classification capability. |
| Q-M10 | Generate or save a reading PDF | passes through existing capabilities | reuse derivation and retention | The output is a derived representation of retained content followed by ordinary governed retention. |
| Q-M11 | Reader layout and settings | fail as generic capabilities | audience and realization patterns | Typography, colors, scrolling, feed layout and app navigation affect presentation without owning the reading-state outcome. |

## Phase 2 cost-and-resource-governance tranche F3

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| R-M01 | Estimate operation resource cost | passes | separate CRD | A forecast has its own request, assumptions, method, scope, uncertainty, validity and success/failure outcome before execution. |
| R-M02 | Approve cost-governed work | passes through existing governance capabilities | reuse composition | The approval is a governed proposal or action decision evaluated through explicit owner intent, standing rules and execution policy. |
| R-M03 | Reserve an operation resource budget | passes | separate CRD | An expiring hold has independent operation binding, amount, availability, adjustment, release and denial states before actual use is known. |
| R-M04 | Record actual resource consumption | passes through an existing capability | reuse metric observation | One attributable measured value already fits the metric-observation contract; cost semantics are supplied by its measurement definition. |
| R-M05 | Reconcile operation resource usage | passes | separate CRD | Comparing actual use with estimate, reservation, budget and completed scope produces an independent final/interim accounting outcome. |
| R-M06 | Partial completion | passes through existing work/run capabilities | reuse lifecycle state | The domain operation or background run owns what completed and what remains; resource reconciliation records why and what allowance remains. |
| R-M07 | Cost-aware standing preference | passes through existing capabilities | reuse standing rule and execution policy | Thresholds, automatic allowance and depth limits are scoped authority/policy rather than a parallel cost-specific rule system. |
| R-M08 | Most-relevant-first processing | fails as a standalone capability at this evidence depth | execution-scope/ordering profile | It selects the order and bounded subset for another processing capability and has no independent domain outcome. |
| R-M09 | Cost and Credit Governance | fails as one generic Capability MLE | source context and composition | The umbrella joins three passing capabilities with approval, policy, observation, execution and commercial concerns that remain independently meaningful. |
| R-M10 | Credits | fails as a capability | shared unit/profile | Credits are an internal resource comparison unit unless a separate commercial profile defines monetary meaning. |
| R-M11 | Billing, payment, invoices, taxes and refunds | excluded from this tranche | separate commercial domain | The admitted source explicitly frames cost governance as product control rather than a billing system. |

## Phase 2 source-discovery-and-owner-knowledge tranche F4

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| S-M01 | Discover a candidate information source | passes | separate CRD | Candidate discovery has its own submitted subject, inspection boundary, findings, confidence, evidence and no-candidate/blocked/failed outcomes before registration. |
| S-M02 | Review a source candidate | passes through existing capabilities | reuse structured review | Suitability, evidence and unresolved risk can be assessed through the generic structured-review contract. |
| S-M03 | Decide source permission | passes through existing capabilities | reuse governed proposal/authorization | Owner or policy disposition is independently governed and must not be embedded into discovery. |
| S-M04 | Register, backfill, and collect incrementally | each passes or reuses existing source/import capabilities | keep separate | Registration, bounded historical intake and recurring collection have different authority, state and failure outcomes. |
| S-M05 | Maintain owner implementation documentation | passes | separate CRD | The owner can create, revise, supersede or archive a human-readable account of their actual system without modifying the framework or runtime configuration. |
| S-M06 | Synchronize a Knowledge Environment | fails as currently evidenced | unresolved implementation capability/profile | Historical sync technologies are examples, while source-of-truth, conflict, authority and durability relationships remain unresolved. |
| S-M07 | Maintain agent behavior files through aliases | fails as a separate capability | realization pattern and agent-definition reuse | Aliases expose system-required files; the governed agent definition/instructions retain their own lifecycle. |
| S-M08 | Promote implementation insight to reference documentation | fails as a PIOS owner-system capability at current scope | project contribution workflow | It is a framework-authoring/publication process rather than an operating capability of the owner's PIOS instance. |
| S-M09 | Assess knowledge-layer integrity | passes | separate CRD | A bounded read/evaluate operation has independent scope, rules, findings, severity, evidence, coverage and completion/failure outcomes. |
| S-M10 | Repair knowledge-integrity findings | fails as one generic capability | reuse domain capabilities | Repairs may require note revision, proposal decision, concept lifecycle, access governance, link correction or index rebuild, each with separate authority. |
| S-M11 | Dataview queries and lint scripts | fail as capabilities | realization tools | Query snippets and scripts support assessment but lack independent owner-domain purpose outside the assessment contract. |
| S-M12 | Knowledge Environment | fails as one generic Capability MLE | architecture composition and source context | It bundles implementation documentation, personal knowledge, storage, synchronization, agent definitions, setup, access and publication concerns. |

## Phase 2 cognitive-memory-and-derived-representations tranche F5

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| T-M01 | Maintain a personal Meaning record | passes | separate CRD | Subject-specific significance has its own evidence, context, confidence, confirmation, revision, rejection and supersession outcomes. |
| T-M02 | Maintain evidence-linked Learning | passes | separate CRD | A durable lesson has an independently useful lifecycle and may be recalled without executing an adaptation. |
| T-M03 | Meaning + reflective assessment | both pass | keep separate | Meaning answers why one bounded subject matters; reflection assesses a wider evidence set with open loops, residue, uncertainty and recommendations. |
| T-M04 | Meaning + profile assertion | both pass | keep separate | Significance does not establish a factual profile claim, and a profile claim need not explain why it matters. |
| T-M05 | Meaning + Learning | both pass | keep separate | Interpretation and durable lesson can be revised, rejected and recalled independently; either can exist without silently producing the other. |
| T-M06 | Learning + standing rule | both pass | keep separate | A lesson may inform future reasoning, while a standing rule is explicit reusable authority with separate scope and decision evidence. |
| T-M07 | Learning + reusable routine or workflow | both pass | keep separate | Knowledge about what may help later is not an executable repeated structure or installed process. |
| T-M08 | Adapt behavior from Learning | passes through existing capabilities | reuse proposal, rule, preference, workflow, agent-definition, and execution governance | Adaptation changes another governed object and requires that object's authority and rollback semantics. |
| T-M09 | Govern a derived-representation lifecycle | passes | separate CRD | Registry identity, replacement, rebuild, revocation, deletion and retrieval exclusion remain meaningful after a derivative is produced. |
| T-M10 | Produce derivative + govern retained representation | both pass | keep separate | Transformation can finish before lifecycle registration, and lifecycle changes can occur repeatedly without re-running the transformation. |
| T-M11 | Source-local graph snapshot | fails as a generic standalone capability | derived-representation profile | It specializes representation identity and evidence preservation while reusing derivation and registry lifecycle outcomes. |
| T-M12 | Embedding, OCR, summary, text chunk, or retrieval index | fail as generic standalone capabilities | representation types and processing profiles | Their technologies and output shapes vary while source-linked production and lifecycle contracts remain reusable. |
| T-M13 | Resolve proposed graph matches globally | excluded from this tranche | separate concept/entity-resolution capability | Confirming global identity changes the knowledge graph and requires a distinct evidence and authority contract. |
| T-M14 | Compile retrieval context from representations | passes through existing capability | reuse governed retrieval-context assembly | Registry eligibility does not select or disclose context for a particular caller and purpose. |
| T-M15 | Meaning service or application | fails as a generic capability | audience projection | It presents and queries Meaning records without becoming a new authority, data zone, or permission source. |

## Phase 2 historical-corpus closure tranche F6

| ID | Candidate | Individual MLE result | Decision | Reason |
|---|---|---|---|---|
| V-M01 | Promote a working artifact to canonical state | passes | separate CRD | Acceptance into durable authoritative state has independent review, approval, target, conflict, provenance, verification, and failure outcomes. |
| V-M02 | Artifact promotion + execution-result preservation | both pass | keep separate | A Result records a meaningful execution outcome, while promotion governs any accepted temporary artifact entering its canonical lifecycle; not every instance of either requires the other. |
| V-M03 | Artifact promotion + imported-source promotion | both pass | keep separate | Artifact promotion crosses a temporary-to-canonical boundary; source promotion controls staged participation in mapping, enrichment, retrieval, and History. |
| V-M04 | Canonical home | fails as a capability | architecture relationship/shared term | It names where authority resides; promotion, revision, retrieval, synchronization and deletion perform the interactions. |
| V-M05 | Shared Workspace | fails as one generic Capability MLE | architecture composition | It combines interfaces, shared information, conversation, attribution, visibility, retention, promotion, and owner authority. |
| V-M06 | Dedicated Agent Computer | fails as a capability | deployment profile | A machine may host runtimes, services and workspaces, but physical placement does not define the reusable outcomes. |
| V-M07 | Track agent capabilities and performance | passes through existing capabilities at current evidence depth | reuse agent definition, canonical events, metric definitions/observations, structured review, and policy | The source supplies desired measurements but not an additional universal lifecycle beyond those existing contracts. |
| V-M08 | Application/session state | fails as one generic Capability MLE | implementation state and multiple profiles | Identity, provider selection, onboarding, attention, navigation, filters and presentation preferences have different purposes and authorities. |
| V-M09 | Market surface and entry-page families | fail as owner-system capabilities | product/publication strategy | They describe how capabilities are communicated and discovered commercially, not a PIOS operating outcome. |
| V-M10 | Area indexes, repository index, source log, roadmap and inconsistency register | fail as capabilities | project/navigation/provenance records | They organize or explain the historical source set rather than define owner-domain interactions. |
| V-M11 | UI design standards and UI/backend terminology | fail as generic capabilities | implementation and presentation profiles | Layout, styling, component rules, and vocabulary mappings constrain realizations without owning an independent outcome. |
| V-M12 | Note-capability linking | fails as a generic capability | implementation composition pattern | A shared database identity and attachment pattern realizes several existing capabilities without creating a new domain outcome. |
