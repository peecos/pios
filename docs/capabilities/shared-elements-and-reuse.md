# Shared elements and approved reuse

This register records conceptual reuse, not proof that one shared software component exists.

| Shared element | Kind | Created-for context | Supported capabilities | Reuse status | Notes |
|---|---|---|---|---|---|
| Stable source reference | data/information MLE | governed retention | derivation, retrieval, consolidation, term detection | conceptually approved | Representation remains implementation-specific. |
| Governed proposal | domain/interaction MLE | proposal decisions | term promotion, assisted-label vocabulary, standing rules | approved by capability relationship | Uses `decide-governed-proposal`; does not duplicate its contract. |
| Glossary identity and aliases | data/information MLE | personal glossary | candidate detection, retrieval, Cotton application | conceptually approved | External standard mappings remain secondary. |
| Provenance record | data/operations MLE | cross-cutting | all evidence-producing capabilities | conceptually approved | Minimum fields depend on the governed object and risk. |
| Lifecycle history | data/operations MLE | proposals and context links | glossary, labels, contextual classification, rule governance | conceptually approved | History preservation does not imply one universal table. |
| Context receipt | data/operations MLE | governed retrieval | later context compilation and disclosure capabilities | conceptually approved | Retention period remains unresolved. |
| Version/revision relation | data/information MLE | knowledge notes | glossary terms, profile assertions, governed system definitions | conceptually approved | Exact storage representation is not fixed. |
| Evidence link | data/information MLE | profile assertions | proposals, term candidates, consolidations, derived content | conceptually approved | Evidence does not by itself grant authority. |
| Execution run record | data/operations MLE | governed action invocation | background operations, workflows, results, standing-rule applications | conceptually approved | Each domain capability defines its own success semantics. |
| Action declaration | API/system MLE | governed action invocation | execution policy, skills, workflows, capability discovery | conceptually approved | A declaration is not proof of availability. |
| Source-to-derived execution link | data/information MLE | plan activation | projects, routines, results, reusable structures derived from completed work | conceptually approved | Derivation preserves the source object and activation decision. |
| Canonical work-state record | data/operations MLE | projects and tasks | routine runs, workflows, background operations, Work Starters | conceptually approved | Communication wrappers may project state but are not canonical state stores. |
| Trigger and recurrence definition | data/operations MLE | reminders | routines, workflow triggers, scheduled operations | candidate for reuse | Each consuming capability retains its own authority and outcome semantics. |
| Work-source context link | data/information MLE | Work Starters | tasks, projects, plans, routine runs, results | conceptually approved | A projection never replaces the canonical source object. |
| Immutable execution snapshot | data/operations MLE | workflow runs | routine runs, background operations, governed actions | conceptually approved | Snapshot scope is capability- and risk-specific. |
| Result provenance bundle | data/information MLE | execution results | projects, routine runs, workflow runs, completed-work updates, History | conceptually approved | Result qualification remains distinct from generic retention. |
| Canonical event envelope | data/information MLE | event recording | work completion, processing, updates, History, governance, imports | conceptually approved | Event-family requirements extend the minimal stable envelope. |
| Owner-attention state | data/operations MLE | owner attention items | reminders, decisions, incidents, workflow outcomes, completed work | conceptually approved | Read/pin/dismiss state does not alter source truth. |
| History period link | data/information MLE | History aggregation | daily compilation, higher summaries, time-first retrieval | conceptually approved | Parent and child periods retain drill-down provenance. |
| Source definition | data/information MLE | connected-source registration | import sessions, mapping, event creation, promotion, export | conceptually approved | Source identity persists independently from sessions and jobs. |
| Versioned batch manifest | data/operations MLE | ingestion screening | readiness assessment, owner authorization, execution, parity proof | conceptually approved | Any material manifest change invalidates stale gate evidence. |
| Ingestion gate receipt | data/governance MLE | ingestion screening | readiness and authorization | conceptually approved | Each receipt records its limited authority and cannot substitute for another gate. |
| Event-type definition | data/system MLE | event registry governance | event recording, projection maintenance, lifecycle validation | conceptually approved | Registry acceptance does not record an occurrence. |
| Operational run evidence | data/operations MLE | run execution | inspection, incident review, retry decisions, completed-work publication | conceptually approved | Missing evidence remains visible rather than inferred. |
| Portability manifest | data/interoperability MLE | portable bundle composition | validation, restore, parity, cutover | conceptually approved | Records scope, versions, counts, integrity, exclusions, and compatibility notes. |
| Integrity digest set | data/verification MLE | portable bundle composition | package validation, backup verification, restored-state parity | conceptually approved | Algorithm and coverage remain explicit. |
| Import/operationalization report | data/operations MLE | bundle restore | parity validation, connector reauthorization, cutover review | conceptually approved | Separates accepted, rejected, quarantined, and unresolved content. |
| Recovery evidence receipt | data/verification MLE | backup restore testing | parity validation, incident recovery, owner assurance | conceptually approved | A receipt identifies tested scope and does not imply broader recovery. |
