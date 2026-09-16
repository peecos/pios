# Collaboration and execution-workspace source context

This reference preserves cross-cutting context for collaboration channels, work-linked discussion threads, attributed messages, and task-scoped execution workspaces. It does not create requirements independently; binding statements are repeated in the applicable CRDs.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework | architecture authority | Circle as a replaceable collaboration layer, durable request and handoff state, actor identity, loop prevention, canonical work boundaries, and runtime-state separation | one chat product, channel taxonomy, bridge protocol, thread depth, or workspace technology |
| Historical PIOS Global at the selected revision | historical design and realization evidence | channel/thread/message models, collaboration states, hybrid work, chat boundaries, attribution, and execution-workspace lifecycle | current architecture authority, current deployment, or mandatory UI behavior |
| Restricted application evidence `RAS-01` | requirements and bounded static realization evidence | channel-like filters, grouped chat entries, message submission, and selected task assignment state | full Circle model, work-linked thread lifecycle, multi-agent attribution, task-scoped workspace, tests, deployment, or production behavior |

## Layer map

| Layer | Owns | Does not own |
|---|---|---|
| Collaboration channel | top-level participant and conversation organization | work, result, or knowledge truth |
| Discussion thread | focused communication around one root subject | source-object lifecycle or execution status |
| Collaboration message | one attributable communication envelope | authority contained in natural-language content |
| Execution workspace | temporary runtime files, context, intermediate state and output staging | canonical project/task identity or automatic promotion |
| Canonical work object | execution state, responsibility and resolution | conversational transcript or scratch workspace |

## Cross-cutting boundaries

- Circle-style collaboration is one possible harness. A compatible capability may be exposed through other chat, messaging, dashboard, command-line, or native interfaces.
- Channels, threads, and messages each pass the MLE test. A channel organizes conversations, a thread scopes one focused discussion, and a message preserves one attributable communication.
- Collaboration objects reference canonical tasks, projects, runs, results, notes, files, and decisions rather than cloning their state.
- Work delegation and assignment remain part of the relevant work object's lifecycle; multi-agent orchestration composes planning, assignment, runtime roles, execution, monitoring, handoff, and result collection rather than becoming one vague capability.
- An execution workspace is a runtime work area, not a project. Its temporary state crosses into canonical storage only through an explicit accepted-output or promotion path.
- Agent-to-agent communication uses true actor identity, explicit trigger permission, and bounded hop/turn controls so background posts cannot create autonomous reply loops.

## Documentation and realization reconciliation

The historical Circle model defines dedicated channel, thread, message, participant, reference, summary, and status objects. Current PIOS preserves the model as a replaceable collaboration harness and strengthens durable request queues, work handoff, identity integrity, loop prevention, and canonical-state separation.

The selected restricted application implements channel-like chat filters, explicit channel creation, grouping of chat entries under filters, session markers, and an owner-to-assistant message flow. The reviewed model exposes a `thread` kind but no source-entry anchor, dedicated thread status lifecycle, Circle participant/agent identity model, typed collaboration message model, handoff message, or task-scoped execution workspace. It therefore supports only partial channel/message realization evidence.

## Sequencing context

This tranche covers collaboration structure and execution workspace lifecycle. Task assignment, background operation, workflow runs, owner attention, completed-work publication, conversation consolidation, and agent runtime roles remain separate existing capabilities.
