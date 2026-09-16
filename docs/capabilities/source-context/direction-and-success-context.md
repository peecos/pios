# Direction and success source context

This reference preserves cross-cutting context for goals, objectives, targets, measurement definitions, and metric observations. It does not create requirements independently; binding statements are repeated in the applicable CRDs.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework | architecture authority | direction-to-execution flow, information-object treatment, goals and targets as Knowledge concepts, and relationships to projects and Work Starters | one mandatory planning vocabulary, schema, or implementation |
| Historical PIOS Global at the selected revision | historical design evidence | long-horizon goal semantics, shorter-horizon objectives, target and metric distinctions, optional attachments, and profile projections | current architecture authority or current implementation |
| Restricted application evidence `RAS-01` | requirements and potential realization evidence | application-specific requirements, declared structures, and bounded static behavior at the selected revision | public disclosure, passing tests, deployment, production availability, or PIOS authority |

## Terminology map

| Concept | Reusable meaning | Not equivalent to |
|---|---|---|
| Goal | Durable desired outcome or longer-horizon direction | objective, target, plan, project, task, measured result |
| Objective | Active, action-oriented statement of current direction | broad goal, success condition, execution design |
| Target | Observable condition describing success | current observation, metric definition, automatic achievement decision |
| Measurement definition | Governed description of what and how to measure | observed value, target, chart, summary |
| Metric observation | One time-scoped measured value or state | metric definition, aggregate, pattern, profile assertion |

## Cross-cutting boundaries

- Goal, objective, target, measurement definition, and metric observation each produce a meaningful state independently and pass the symmetric MLE test.
- The common directional sequence is useful guidance, not proof that every implementation must enforce one hierarchy or require every link.
- A goal remains valid without a target or metric. A target may stand alone or attach to another eligible object. A metric definition may exist before any observations.
- Target achievement requires evidence and a separate evaluation rule; an active target or current observation does not by itself establish success.
- Plans describe approach, projects and tasks represent execution, and Work Starters prepare work. They remain separate from direction and success semantics.
- Goal and profile screens are audience projections over canonical objects, not additional realizations merely because they render the same data in different layouts.

## Documentation and realization reconciliation

The historical design states that a target can show whether it has been met. The bounded application trace at the selected revision exposes target creation, revision, activation, and deletion around a success description, but the reviewed target schema and interface do not establish a separate achievement state or evidence-backed evaluation path.

The selected application includes a declared time-series observation structure with time, value, source, and provenance fields. The reviewed goal interface and hooks manage only metric definitions such as unit and tracking method; no reachable metric-observation recording interface or hook was found in the bounded trace. This supports the capability distinction while leaving implementation availability unconfirmed.

Objectives have a distinct persisted lifecycle in the selected application, and plans can retain a source-objective reference. The broader historical goal-to-objective-to-target-to-plan sequence is explicitly conceptual rather than fully schema-enforced. Public CRDs therefore preserve explicit optional relationships instead of imposing that application model on PIOS.

## Evidence maturity

Public sources support the reusable direction and success definitions. Restricted requirements and static implementation evidence support bounded realization records. No local app execution, passing behavior test, deployment, or production availability is claimed.
