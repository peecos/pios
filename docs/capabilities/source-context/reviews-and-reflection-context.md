# Reviews and reflection source context

This reference preserves cross-cutting context for structured reviews and reflective assessments. It does not create requirements independently; binding statements are repeated in the applicable CRDs.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework | architecture authority | reviews as Knowledge concepts, continuous reflect-and-adjust flow, review windows, summary/reflection distinction, and downstream information-object boundaries | one mandatory review cadence, template, model, or implementation |
| Historical PIOS Global at the selected revision | historical design evidence | weekly-review workflow intent, review-note outputs, stale-item review, and temporal summary context | current architecture authority or operational availability |
| Restricted application evidence `RAS-01` | requirements and bounded static realization evidence | a selected weekly-review workflow path and its recorded workflow output behavior | passing tests, scheduled operation, deployment, production use, or complete review semantics |

## Cross-cutting boundaries

- A structured review is a process and outcome covering a declared scope, questions, inputs, findings, decisions, updates, open loops, and carry-forward disposition.
- A reflection is an interpretive information object that may be created during or outside a structured review. It adds judgment, residue, and recommendations and is not a neutral summary.
- Period summaries, History aggregation, and review records may inform one another but retain distinct identities and provenance.
- Review recommendations may invoke existing proposal, goal, target, project, task, Work Starter, attention, or knowledge capabilities. The review does not silently perform those downstream changes.
- Daily, weekly, monthly, yearly, and event-triggered review are useful profiles of one capability rather than separate generic capabilities.
- A review workflow package and its run are realizations of existing workflow capabilities; the review outcome remains independently specified.

## Documentation and realization reconciliation

The selected application requirements describe a scheduled weekly review builder producing a review note and optional updates. The reviewed server function contains a manually dispatched weekly-review branch that reads bounded recent notes and chat entries, invokes a model, creates a note, and records a workflow output.

That static path supports a partial realization of review-note generation. It does not establish the documented scheduled trigger, production execution, passing tests, a canonical review object, structured questions and decisions, explicit carry-forward state, or statement-level source links in the produced note. The generated text is therefore not treated as proof that the full structured-review contract is implemented.

## Sequencing context

This tranche specifies review and reflection outcomes. Review scheduling, summary generation, workflow packaging/runs, owner attention, proposals, and downstream object changes remain separate capabilities.
