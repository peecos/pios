# People and relationships source context

This reference preserves cross-cutting context for human contact profiles, contact points, contact-point verification, and personal relationship context. It does not create requirements independently; binding statements are repeated in the applicable CRDs.

## Source roles and limits

| Source | Role | Can establish | Cannot establish alone |
|---|---|---|---|
| Current PIOS framework | architecture authority | separation of owner, human/contact, agent, and asset profiles; My World/Circle placement; relationship scope, consent, source-linked history, and dynamic interaction boundaries | one contact schema, contact application, verification method, or implementation |
| Historical PIOS Global at the selected revision | historical design and realization evidence | contact-profile fields, typed contact points, relationship labels, app projections, and distinction from glossary identities | current architecture authority, subject consent policy, or production availability |
| Restricted application evidence `RAS-01` | requirements and bounded static realization evidence | contact/profile and contact-point structures, owner-scoped CRUD paths, and declared relationship-origin fields | passing tests, deployment, production behavior, or complete relationship/verification lifecycle |

## Concept map

| Concept | Reusable meaning | Not equivalent to |
|---|---|---|
| Human contact profile | Living owner-held projection about another person | owner profile, agent profile, glossary identity, interaction stream |
| Contact point | Typed communication or location coordinate for a person | verified identity, permission to communicate, relationship meaning |
| Contact-point control verification | Evidence that a subject controls or receives through one contact point under a stated method | legal identity proof, account authentication, general authority |
| Relationship context | How the owner relates to a person or organization over time | participant identity, access grant, temporary event participation |
| With-whom context | Person/organization relevance to one event or active context | durable relationship record |
| Glossary person identity | Stable named-entity meaning and aliases | relationship profile or contact-management record |

## Cross-cutting boundaries

- A person identity, human contact profile, contact point, contact-point verification result, and relationship context are related but independently meaningful objects.
- Owner, other-human, agent, and asset profiles have different subjects and authority models and must not be merged into one profile capability.
- Slowly changing contact/profile attributes remain versioned and source-linked. Dynamic calls, messages, meetings, and activities remain events or interaction records rather than overwriting the profile.
- Circle scope, trust, and relationship labels help govern context and exposure but do not grant access by themselves.
- Contact-point verification is an evidence-backed capability and state. Successful storage, normalization, or use does not automatically prove control or continuing ownership. Onboarding verification specializes the same generic control result by binding it to a journey.
- Contacts, profile screens, filters, avatars, and contact lists are audience projections and realization patterns rather than independent capabilities.

## Documentation and realization reconciliation

The historical contact page describes behavior observed in the selected application rather than a separate requirements specification. The bounded static trace confirms owner-scoped listing, creation and revision of contact profiles, active/inactive state, Role/label filtering, and creation/deletion of typed contact points.

The selected schema declares contact-point verification, primary-contact-point, and relationship-origin structures. The reviewed hooks and UI do not establish a contact-point verification transition, explicit primary-point selection, or relationship-origin creation and maintenance. The visible relationship field is a free-text connection label, which is narrower than the current PIOS relationship profile expectations for scope, trust, consent, source-linked history, and interaction context.

## Evidence maturity

Public sources support all three reusable capability boundaries. Restricted evidence supports bounded static realization for contact-profile and contact-point management and declared structure only for richer relationship origin and verification. No app execution, passing tests, deployment, or production behavior is claimed.
