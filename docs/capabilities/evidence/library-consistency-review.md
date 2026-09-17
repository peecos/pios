# Capability Library consistency review

**Review date:** September 17, 2026
**Review state:** self-review in progress; independent review pending

This review checks the CRD library as one system rather than validating only the latest tranche. It does not establish implementation, deployment, compatibility-level adoption, or website publication.

## Structural checks

| Check | Result | Notes |
|---|---|---|
| CRD file and inventory parity | pass | 115 CRD files and 115 inventory rows after duplicate consolidation |
| Inventory and architecture-alignment name parity | pass | every inventory capability has one alignment row and no extra alignment row remains |
| Required CRD sections and interaction fields | pass | every CRD contains Identity, Core meaning, Interaction Contract MLEs, Rules/defaults, Unknowns, provenance, and the required interaction fields |
| Ledger identifier uniqueness | pass | statement, boundary-decision, unresolved-question, and restricted-evidence identifiers are unique |
| Local Markdown links | pass | all relative links under `docs/capabilities/` resolve |
| Historical corpus disposition | pass | all 90 Markdown files at the selected historical revision appear exactly once in the disposition ledger |
| Restricted document disposition | pass | all 26 admitted restricted documents retain a bounded public-safe disposition; detailed evidence remains outside the public repository |
| Publication-safety token scan | pass | no restricted repository name, revision, local absolute path, or restricted evidence filename appears in public capability files |
| Repository tests | pass | all 10 available documentation tests pass |

## Duplicate and overlap review

The review compares capability purpose, meaningful outcome, actor, transition, and result rather than names alone.

| Related candidates | Disposition |
|---|---|
| Onboarding contact-channel verification / contact-point control verification | consolidated into `verify-contact-point-control`; onboarding is a profile because journey binding does not change the verification outcome |
| Controlled sharing / public publication / outward access / discoverability / usage rights | remain separate; each axis can change independently and has an explicit boundary decision |
| Workflow package / installed workflow / workflow run / routine / routine run | remain separate definitions, installations, and executions with independent state and outcomes |
| Goal / objective / target / measurement definition / metric observation | remain separate direction, success-condition, measurement-semantics, and evidence objects |
| Meaning / reflection / Learning / profile assertion / standing rule | remain separate interpretation, review, lesson, factual-claim, and authority lifecycles |
| Derivative production / derived-representation lifecycle / artifact promotion | remain separate transformation, projection-governance, and temporary-to-canonical transitions |
| Conversation message / conversation history / collaboration thread / channel | remain separate communication, continuity, focused-discussion, and container outcomes |
| Source discovery / source registration / import session / source promotion / artifact promotion | remain separate candidate, recurring-origin, bounded-intake, source-eligibility, and canonicalization transitions |

## Cross-cutting rule review

- Owner authority, delegated authority, or explicit policy remains visible in every CRD.
- Every CRD carries provenance, source linkage, or evidence expectations appropriate to its outcome.
- Canonical source, temporary state, derived projection, cache, offline copy, and outward representation remain distinguishable.
- PIOS-system membership, Core-contract membership, physical deployment, and state treatment are not collapsed in the alignment matrix.
- Applications, pages, panels, provider products, machines, schemas, tables, hooks, and files are treated as realizations or projections unless they independently pass the Capability MLE test.
- Requirements, static code-traced behavior, tested behavior, deployed behavior, and observed production behavior remain separate evidence levels.
- Communication is represented as an owned Interaction Contract MLE when it exists only to communicate another capability's state.

## Findings and corrections

1. The final historical gap pass identified canonical artifact promotion as a missing Capability MLE; it was added with separate boundaries from Result preservation and imported-source promotion.
2. The onboarding-specific verification CRD duplicated the generic contact-point-control outcome; it was removed and the onboarding relationship was retained as a profile and decision record.
3. The library README omitted one existing source-context document; the import/operations/portability context link was added.
4. No other high-similarity pair reviewed in this pass required consolidation. The strongest overlaps have explicit symmetric boundary decisions.

## Remaining limitations before publication

- Restricted implementation coverage is incomplete for many capabilities; absence of a confirmed realization is preserved rather than inferred as absence of all implementation.
- The unresolved-question register contains 103 active entries through `U105`; profile and interoperability decisions remain intentionally open.
- Independent review and repository merge clearance are still pending.
- Website implementation, route creation, rendering verification, deployment, and live publication have not started.
