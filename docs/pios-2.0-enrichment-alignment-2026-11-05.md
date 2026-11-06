# PIOS 2.0 enrichment alignment — November 5, 2026

Status: documentation clarification and selectable draft extension guidance.
Not a runtime adoption, compatibility certification or publication receipt.
PIOS remains PIOS 2.0. No existing mandatory Core requirement is removed, and
no new mandatory Core capability is added by this package.

## Read before affected work

Start with the [master](../index.html#capability-led-adoption), then the relevant
contract below. The [execution plan](pios-2.0-enrichment-plan-2026-11-05.md)
records scope and completion separately; it is not another framework master.

| Subject | Current contract and interpretation |
| --- | --- |
| Claims and changing evidence | [Assertion and lineage profile](cognitive-memory-source-discovery-and-derived-representations-v0.1.md#assertion-and-lineage-profile): canonical retention, evidential support, owner acceptance, freshness and access remain distinct. |
| Classification and clusters | [Semantic-assessment and cluster profile](cognitive-memory-source-discovery-and-derived-representations-v0.1.md#semantic-assessment-and-cluster-profile): optional bounded interpretations, ambiguity, provenance and explicit identity continuity; no model-issued authority. |
| Shared processing outputs | [Result-reuse profile](cognitive-memory-source-discovery-and-derived-representations-v0.1.md#processing-result-reuse): source versions and audience permissions apply to reuse; reprocessing is a separate decision. |
| Disclosure and future viewers | [Controlled-disclosure profile](integration-interoperability-and-governance-v0.1.md#controlled-disclosure-profile): existing grants apply before processing and disclosure; controlled references differ from already disclosed copies. |
| Availability | [Owner-facing availability](core-distribution-and-compatibility-spec-v0.1.md#41-owner-facing-availability): installed, enabled, authorized, reachable and healthy are not synonyms or new compatibility levels. |
| Local and mixed-device use | [Proposed Apple profile](apple-local-and-mixed-device-profile-v0.1.md): native device-side PIOS, declared Local Core and remote Core integration are distinct configurations. |
| Candidate capabilities | [Coverage and gap map](capabilities/decisions/information-lifecycle-and-device-profile-candidates-2026-11-05.md): possible future definitions, not new accepted CRDs. |

## Existing principles clarified

- PIOS is a personal information operating system, not merely storage. Core
  contract, PIOS-system membership, ecosystem participation, physical placement
  and state treatment remain separate.
- The five zones and append-oriented canonical Event log remain. A particular
  event-sourcing database or graph engine is not mandated.
- A record of what someone asserted can be canonical without establishing the
  proposition as true. Owner acceptance does not prove an external fact.
- Grants apply before information reaches a processor, including sensitive
  candidate labels or definitions. Confidence, inferred context and Circle
  membership do not create permissions.
- Device-side PIOS may work without a remote PIOS connection. The Core app
  remains PIOS-native and PIOS-dependent. A cache, shared container or cloud
  replica is not automatically a Local Core.

## New detail is selectable, not silently mandatory

The assertion/dependency, semantic-assessment/cluster, result-reuse and
controlled-disclosure profiles elaborate behavior for implementations that
explicitly choose them. Their local requirements do not become universal
Core requirements. They reuse existing authority, intake, correction and
portability contracts, not a second enforcement system or protocol.

The Apple composition remains proposed. Named platform APIs, language coverage,
entitlements, cost assumptions and integration guarantees require primary-source
and implementation evidence before availability is claimed. No particular
classifier, symbolic engine, cloud provider or continuously running service
is selected. Existing capture and useful owner work need not wait for optional
processing or a full device suite.

## What implementation agents must preserve

Preserve existing API/export versions, identifiers, stable references, Events,
source bytes, pending work, accepted revisions and recovery evidence. There is
no requirement to re-ingest completed domains, repeat evidence, migrate a live
service or upgrade every implementation to claim its existing supported level.

The [October 8 mobile alignment](pios-mobile-contract-alignment-2026-10-08.md)
and [selected first-party profile](pios-first-party-mobile-apps-by-prifina.md)
remain in force: direct/brokered/hybrid integration, Notes reconciliation,
independent Notes/Voice Notes/Browser/LifeStory Indie, the new Core-dependent
LifeStory, and protected device-source/working/pending states. Do not replace
current app-owned synchronization with shared cloud storage by inference.
New historical backfill, data collection, routing, permissions and deployment
require the implementation's applicable selection and authorization.

Independently useful development agents remain consumers or external operators;
this package does not move native server services out of Solo or device-bound
functions onto a general agent machine. Live status and priorities remain in
the implementation's current roadmap, not in this framework notice.

## Handoff and source identity

At handoff, record the exact reviewed source revision or pre-commit file
manifest, identify this notice and relevant changed sections, and report
source publication, website projection and live publication separately.
Do not substitute the baseline revision for the revision containing these
changes. Preserve any immutable operating snapshot; reconcile updated guidance
through its existing controlled update path rather than editing it in place.

An implementer reading this notice should assess only its next affected work
against the clarified boundaries. Optional adoption is not an urgent cleanup
program or a new gate against unrelated authorized production use. A pointer
or published page does not prove that another agent received or acknowledged
the update.
