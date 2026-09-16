# Capture, onboarding, and experience source context

This reference preserves cross-cutting context for the D1 tranches. It does not create requirements independently; binding statements are repeated in applicable CRDs.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework, including the verified owner-approved clarification working set | architecture authority | Core app responsibility, governed inbound flow, device-state treatment, owner context, and PIOS-system boundaries | proof that clarification bytes are already published, or a particular realization's tested and deployed state |
| Historical PIOS Global at the selected revision | historical design evidence | web capture intent, capture-time metadata, onboarding stages, and experience concepts | current architecture authority or current availability |
| Restricted application evidence `RAS-01` | requirements and potential realization evidence | application-specific intended capture and onboarding behavior and, where traced, static implementation evidence | public disclosure, tested behavior, deployment, or production availability without separate evidence |

## Cross-cutting context

- A capture interface hands content into governed intake; it does not become another canonical Core or prove durable acceptance merely by sending a request.
- Pending captures and edits may be the only copy. They remain protected work until acceptance or another explicit authorized disposition is verified.
- Capture-time labels, action intent, and processing instructions are adjacent governed effects rather than implicit consequences of capture.
- Browser, mobile, desktop, voice, and other interfaces are possible realizations of capture capabilities, not separate capabilities solely because their controls differ.
- Onboarding is a journey and experience context that may compose several independently meaningful capabilities. It must not be drafted as one capability until identity, verification, personalization, preparation, and first-entry outcomes have each passed or failed the MLE test.
- Roles used to tailor onboarding or interfaces do not automatically establish access authority, identity truth, or Core-contract membership.
- A personal AI's presentation identity, interaction preferences, runtime roles, memory, and execution authority are separate concerns.
- Contact-channel verification proves only the declared assurance result; it is not automatically proof of person identity, account recovery authority, or Core permission.
- Initial environment preparation keeps explicit answers, defaults, inferred values, and omissions distinguishable and revisable.
- A first-use orientation is a Communication MLE and experience realization. Showing or completing it does not prove that identity creation, environment preparation, or first-entry authorization occurred.
- Role definitions, Mode definitions, active-context snapshots, and durable object classifications are separate states with separate lifecycles.
- Roles and Modes organize, filter, prioritize, and support retrieval; they do not grant access.
- A Role's outward intent, an outward representation, audience access, and publication are separate governance outcomes.
- Home panels, menus, layout systems, gestures, badges, and context pickers are audience and realization patterns over capabilities rather than capabilities by themselves.

## Evidence maturity

Current and historical architecture sources support the D1 reusable definitions. Some supporting current-framework wording remains in the verified owner-approved clarification working set and is not represented as already published. Restricted capture, onboarding, welcome, interface, identity, preference, Role, and Mode requirements have been assessed without publishing source details. Static review found bounded interface and context-management behavior but did not confirm the documented end-to-end onboarding journey or complete Core-backed active-context lifecycle. Tests, deployment, and production behavior remain unknown.

## Sequencing context

D1a covers governed capture submission and pending-capture reconciliation. D1b1 covers guided journey state, personal-AI identity and interaction preferences, contact verification, initial-environment preparation, and first-entry authorization. D1b2 covers owner Role and Mode definitions, active context, outward-role intent, outward representation preparation, and remaining interface concepts.
