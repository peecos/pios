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

## Evidence maturity

Current and historical architecture sources support the D1a reusable definitions. Some supporting current-framework wording remains in the verified owner-approved clarification working set and is not represented as already published. Restricted capture and onboarding requirements have been assessed without publishing source details. Capture implementation reachability, tests, deployment, and production behavior remain unknown.

## Sequencing context

D1a covers governed capture submission and pending-capture reconciliation. D1b next evaluates onboarding journey, identity and verification, adaptive personalization, first-run preparation, first entry, owner-role context, and related experience surfaces independently.
