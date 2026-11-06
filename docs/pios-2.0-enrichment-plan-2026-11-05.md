# PIOS 2.0 documentation enrichment — execution plan

Date: November 5, 2026.
Status: source documentation complete and locally verified; local commit authorized November 6, 2026. Push, website publication and runtime adoption remain separate.
Baseline: `ac00ace2153c051a63ef6b1ca00f421df32c6aa4`.

## Outcome and scope

Improve PIOS 2.0 with the useful results of the reviewed knowledge-maintenance,
semantic-classification, information-boundary and Apple/mixed-device proposals.
Keep the PIOS 2.0 name and architectural foundations. Produce one coherent,
tested, independently reviewed documentation package and a publication-ready
projection. Do not introduce new mandatory Core obligations by calling them
clarifications.

The owner selected this direction after a five-source assessment. The
conversations are research inputs, not framework authority or proof of working
software. Missing attachments, redacted tool results and unverified platform
claims remain evidence limitations. Keep private research and installation
details out of public documents; use original public-safe prose and synthetic
examples rather than republishing conversation transcripts.

This plan belongs to the official PIOS repository. Do not create another
capability-library repository, a competing master, or a large local source copy.
The website remains a projection of reviewed canonical source.

The work packages below are documentation execution steps, not new PIOS Solo
roadmap stages. Current implementation work continues independently.

## Authority and compatibility rules

Preserve:

- Five zones: Originals, Events, Knowledge, Derived and System.
- The append-oriented canonical Event log, stable logical identities and
  governed canonical acceptance; no re-ingestion requirement.
- Core-contract membership, PIOS-system membership, ecosystem participation,
  physical placement and state treatment as separate questions.
- The preferred complete Solo server package, native device-side PIOS and
  independently useful external consumers.
- Core app naming and purpose; LifeStory Indie versus the Core-dependent
  LifeStory; direct, brokered and hybrid integration.
- Source-owned working records, pending work and accepted-content caches as
  distinct states; existing Notes bidirectional reconciliation.
- Owner grants, proposal/adoption controls, explicit processing recipients,
  portability, recovery and independent upstream document authority.
- Existing API/export identifiers, compatibility levels and implementation
  version axes. Do not bump them or relabel the framework as 2.1 or 3.0.

Classify every substantive addition before drafting it:

| Class | Treatment |
| --- | --- |
| Existing principle clarified | Cite the existing rule; remove ambiguity without strengthening its obligation silently. |
| Optional contract elaboration | State its selection boundary and requirements for implementations choosing it; do not make it mandatory for every Core. |
| Named implementation profile | Keep platform/product choices outside the universal framework; declare proposed versus implemented status. |
| Unverified technical assertion | Verify against current primary sources or omit the specificity; do not promote a plausible claim into a requirement. |
| New mandatory obligation or incompatible change | Hold that item for an explicit decision; continue unaffected compatible work. |

## File and content map

Paths are relative to the official PIOS repository. Append short sections and
preserve existing anchors; do not rewrite whole documents to fit the proposals.

| File | Planned change |
| --- | --- |
| `index.html` | Brief clarifications near §§2.3–2.5, Knowledge/Meaning/patterns and retrieval: claim versus accepted interpretation, dependency maintenance, optional semantic assessment, authorization across processing/disclosure, and capability-led mixed-device adoption. Link detailed companions. |
| `docs/cognitive-memory-source-discovery-and-derived-representations-v0.1.md` | Optional assertion, typed-dependency, semantic-assessment, cluster and shared-result-reuse contracts. Preserve source-local ambiguity and existing Meaning/Learning semantics. |
| `docs/integration-interoperability-and-governance-v0.1.md` | Clarify authorization before processor disclosure, including candidate metadata; derived-output policy; controlled references versus disclosed copies; revalidation and model-fallback boundaries. Reuse existing grants and Context Receipts. |
| `docs/hosting-core-boundaries-and-portability-principles-v0.1.md` | Link the optional local/mixed-device profile without weakening Solo packaging or requiring every native service on one machine. |
| `docs/core-distribution-and-compatibility-spec-v0.1.md` | Explain owner-facing availability separately from conformance; preserve Local Core authority and existing version/discovery contracts. No new mandatory endpoint or wire field. |
| `docs/apple-local-and-mixed-device-profile-v0.1.md` — new | Proposed selectable profile for local PIOS, qualified Local Core, optional cloud replication, connectors, processing reuse, web access and remote Core integration. Include explicit authority, acceptance, recovery and unresolved platform questions. |
| `docs/pios-first-party-mobile-apps-by-prifina.md` | Bounded cross-reference and non-adoption statement: proposed Apple options do not silently replace current suite synchronization, routing, app roles or release priorities. |
| `docs/pios-2.0-enrichment-alignment-2026-11-05.md` — new | Concise implementer reading notice: what was clarified, what is optional, what remains unchanged, and what requires separate implementation selection. |
| `docs/capabilities/decisions/information-lifecycle-and-device-profile-candidates-2026-11-05.md` — new | Small coverage/gap map against existing library definitions. Candidates only; no accepted CRDs, inventory counts or adoption statuses change. |
| `README.md`, `docs/publication-notes.md` | Link the new profile and alignment notice; state publication and implementation status precisely. |
| `tests/test_pios_2_0_enrichment.py` — new; existing tests where necessary | Source-consistency, boundary, status, link and compatibility regressions. Preserve existing test coverage. |

Modify another file only to repair a direct conflict or broken link caused by
this package, recording the reason. Unrelated stale historical status is not a
license for broad documentation cleanup.

## Work package A — exact delta and source binding

Execution binding (November 5): baseline HEAD verified unchanged; the starting
worktree contained only this plan. Current master and companion coverage was
re-read before drafting. No new platform API or cost claim is needed: those
specifics remain validation questions in the proposed device profile.

| Existing coverage | Added detail | Class and destination | Acceptance check |
| --- | --- | --- | --- |
| Master §§14–15 and memory §§2, 11 preserve evidence and interpretations | Independent assertion dimensions and typed dependency impact | Clarification in master; optional memory profile | Correction versus access revocation produces different dispositions; canonical Events retained. |
| Master §16 and memory §10 permit scoped model assistance | Versioned candidate choices, abstention, cluster continuity and result reuse | Optional memory profiles | Candidate metadata scoped before transfer; no score-to-authority promotion or implicit reprocessing. |
| Master §9.6 and integration grants/Context Receipts distinguish exposure and rights | Controlled references, materialized copies, derived-output constraints | Clarification plus optional disclosure profile | Actual viewer and metadata considered; no retroactive recall promise. |
| Master §2.4–2.5 and hosting §7 allow native device roles | Useful local/mixed-device configurations and honest availability | General clarification; proposed Apple profile | Local operation is not outside PIOS; sync is not conformance or recovery proof. |
| Existing first-party app profile and October 8 alignment | Cross-reference without replacing selected suite behavior | Non-adoption clarification | Notes reconciliation, app-owned sync and LifeStory split unchanged. |
| Existing capability library | Narrow coverage/gap record | Candidate assessment only | Inventory and all existing CRD bytes unchanged. |

No mandatory/incompatible candidate was selected. Unverified Apple SDK,
entitlement, language, pricing and connector-access claims are excluded from
normative adoption, not blockers to the compatible documentation package.

1. Recheck repository instructions, HEAD and working-tree changes. Preserve
   concurrent work; do not require an unrelated worktree to be clean.
2. Re-read affected canonical sections, current mobile profile and existing
   capability definitions. Use the completed assessment; do not restart the
   full historical review chain.
3. Record a compact delta table in this plan: existing coverage, proposed
   wording/contract, classification, destination and acceptance check.
4. Verify only consequential platform facts needed by the proposed text using
   current primary sources. Keep unresolved API, entitlement, language, quota,
   pricing or browser-access specifics explicitly unverified or out of scope.

Exit: each useful assessed idea is mapped to existing coverage, an in-scope
addition, or a reasoned deferral. No new mandatory obligation is hidden.

## Work package B — knowledge and processing contracts

Draft the cognitive-memory changes first, then the corresponding short master
clarifications. Cover:

- Independent dimensions for origin, evidential support, acceptance, temporal
  validity and access. A canonical record of a claim is not proof it is true.
- Evidential, computational and policy dependencies. Define stale, disputed,
  inaccessible and superseded outcomes without collapsing them into one status.
- Authorized recomputation, retained historical results and corrective Events.
  No required graph database or universal automatic recomputation engine.
- Typed semantic assessments with source revisions, authorized candidate-set
  versions, model/rule profiles, score meaning, abstention, context and expiry.
- Candidate labels and descriptions as potentially sensitive processor inputs.
  Confidence does not establish correctness, privileges or permission to act.
- Multi-label context where appropriate; classification, extraction, identity
  resolution and canonical promotion remain distinct operations.
- Unnamed and overlapping clusters, membership versions, split/merge lineage
  and governed promotion. Consolidation, concept induction and rule induction
  are different operations.
- Reusable processing results bound to source revision, parameters, language,
  processor/version and permitted audience; reuse differs from reprocessing.
- Existing Base Week and routine semantics; only a brief optional seasonal or
  annual-context clarification if not already covered. No scheduling subsystem.

Exit: the contracts are technology-neutral and optional, preserve capture-first
operation, and introduce no opaque authoritative model memory or sixth zone.

## Work package C — disclosure and information boundaries

Extend existing integration governance rather than inventing another policy
engine. Cover access, processing, derivation, retention, disclosure and subsequent
viewing as distinct decisions. Enforce authorization before every relevant
processor transfer or action, not only after generating an answer.

Specify controlled references with viewer/current-policy checks separately
from materialized copies already disclosed. Include titles, previews and
notifications in the disclosure analysis. Do not promise recall of screenshots,
past observations or copies outside supported enforcement.

Describe constraints on outputs derived from multiple sources. Summarization,
aggregation or inferred anonymity does not automatically declassify information.
Role/Mode inference and Circle membership are context, not grants. State the
actual enforcement boundary; do not promise absolute isolation.

Exit: no new permission namespace, no model-issued authority and no claim that
policy metadata alone enforces third-party behavior.

## Work package D — useful local and mixed-device PIOS

Add a concise general principle to the master and detailed choices to the new
Apple profile. Distinguish:

1. Device-side PIOS with local sources, working state and selected capabilities.
2. A declared Local Core satisfying its selected canonical contract.
3. Device-side PIOS connected to a remote hosted or self-hosted Core.

Make remote hosting optional where the selected local behavior permits it;
never describe native Core app behavior as outside PIOS merely because no
server is connected. Do not equate Apple sync or five named containers with
Core conformance.

Cover iPhone-only, iPhone/PC and Mac/Android examples; existing-app connectors
and dedicated apps; portable IDs and extensible metadata; authority and
conflicts across replicas; account changes; pending work; independent recovery;
and declared browser/read/write limitations. Shared Apple storage is a proposed
profile choice, not a replacement for current app-owned synchronization.

Owner-visible availability distinguishes implemented, installed, enabled,
authorized, reachable and healthy. Explain prerequisites, processing location,
data disclosures and offline limits without turning these states into new
Core Compatibility Levels or a required product-upgrade ladder.

Exit: the profile is useful without unverified Apple promises. No selected
Solo topology, app identifier, entitlement, provider, connector, historical
backfill, OCR/data-collection choice or release sequence changes.

## Work package E — integration, guidance and candidate mapping

The lead agent integrates the master, cross-links, entry points and public-safe
alignment notice. Keep one concise statement of the non-breaking scope and
link it rather than copying entire contracts into every document.

Map candidate abilities to the existing library, especially evidence-backed
profile assertions, active personal context and outward usage rights. Record
genuine gaps for dependency maintenance, cluster lifecycle, controlled
presentation, processing-result reuse and availability only where not covered.
Do not write or adopt new CRDs in this package. Formal CRD authoring, if later
selected, follows the repository method and applicable CRD skill.

Prepare a short handoff for the main Solo agent identifying exact source
revision, changed sections, optional profiles and unchanged operating scope.
That agent retains implementation ownership. Coordinate any minimal internal
reading-pointer updates; do not overwrite its active source or mass-edit global
instructions. An alignment notice does not prove another agent has read it.

Exit: public and internal readers have an unambiguous entry point; pending
adoption is not presented as completed implementation or confirmed notification.

## Work package F — verification and one independent review

Run from the PIOS repository:

```sh
python3 -B -m unittest discover -s tests -v
git diff --check
```

Use the existing HTML/local-link checks and extend them for new Markdown links
and fragments. Add focused regressions for unchanged PIOS 2.0 naming, canonical
Events, five zones, optional profiles, local-versus-remote terminology,
pre-processing authorization and explicit non-implementation claims. Prefer
meaningful section and relationship checks over only counting phrases.

Exercise a small set of synthetic documentation scenarios:

| Scenario | Required interpretation |
| --- | --- |
| A source is corrected | Its dependent interpretation can become stale without erasing historical Events. |
| A grant is revoked | Future governed access is restricted; truth is not automatically negated and disclosed copies are not magically recalled. |
| A classifier is highly confident | No new permission or automatic canonical promotion follows. |
| A sensitive project name is a candidate | Authorization applies before sending that metadata to a processor. |
| A cluster splits | Membership/ancestry is explicit; unrelated cluster IDs do not inherit identity silently. |
| An iPhone has no remote connection | Device-side PIOS can remain useful; no unsupported complete-Core claim follows. |
| Cloud sync succeeds | Canonical acceptance and independently verified recovery remain separate. |
| A processing result is reused | Source/version and current audience permission still apply. |

Run the relevant existing Solo documentation/preflight regressions locally if
changed master semantics affect their bindings. Do not weaken tests simply to
make changed prose pass. Document tests establish source consistency, not
working runtime capabilities or production conformance.

Request one independent read-only review of the complete source package against
the baseline and this plan. The reviewer must look for hidden mandatory changes,
duplication, private material, unsupported claims and architecture drift—not
invent unrelated hardening. Remediate findings as one package. Re-review only
if a material unresolved finding requires it.

Exit: tests and links pass, material findings are resolved, and every new
obligation is explicitly confined to a selected optional contract/profile.

## Work package G — authorized publication and handoff

Publication is a separately authorized action; planning is not push/deployment
permission. Once authorized, commit only reviewed PIOS changes, record the exact
source revision and contribute them through the current repository workflow.

In `peecos/peecos-web`, use the existing projection scripts rather than editing
the embedded master by hand:

```sh
node scripts/sync-pios-master.mjs --source ../pios/index.html
node scripts/sync-pios-master.mjs --source ../pios/index.html --check
node scripts/sync-pios-capabilities.mjs --source-repo ../pios --revision <reviewed-commit>
node scripts/sync-pios-capabilities.mjs --source-repo ../pios --revision <reviewed-commit> --check
npm run lint
npm test
npm run build
git diff --check
```

Use committed canonical source for the final projection. Capability definitions
and accepted inventory count remain unchanged; a candidate decision document
may add supporting documentation. Verify companion links, navigation, rendered
status labels and the exact represented revision. Diagnose pre-existing check
failures separately rather than expanding this package into unrelated repairs.

Deploy only through the established authorized site workflow. Report source
commit, website commit and verified live content separately. A pushed website
commit is not proof that the public site changed. If publication requires an
unavailable human session, report that one specific remaining action; do not
alter browser security or claim success.

Deliver the revision-pinned implementer handoff. Record notification/acknowledgement
only where actually established. Preserve private sources and completed
implementation evidence; no runtime upgrade is implied.

## Execution ownership and interruption policy

Use one lead agent for the delta, master and integration. At most two workers
can draft non-overlapping companion changes: knowledge/processing and
disclosure/device-profile work. Workers do not independently edit shared master
sections, publish or touch production. One separate reviewer assesses the
integrated package. Avoid extra clones and unnecessary generated artifacts.

Within an authorized documentation execution package, continue through drafting,
tests and bounded remediation without owner micro-approvals. Ask only for a
genuinely new mandatory/product decision, incompatible contract change, broader
authority, or publication authorization. An unverified optional Apple detail
does not block the rest of the framework package.

No VM/device access, deployment, credentials, data migration, source release,
new paid service or model/provider selection is part of documentation execution.
No existing Solo stage exit or live recovery prerequisite changes.

## Completion checklist

- [x] Prepared this plan against the recorded official baseline.
- [x] Bound the exact delta and verified/qualified consequential source claims.
- [x] Drafted and integrated the master and companion improvements.
- [x] Mapped capability coverage without adopting new CRDs.
- [x] Passed documentation checks and resolved independent-review findings.
- [x] Prepared the implementer handoff bound to baseline plus exact working-tree hashes; replace with the containing commit at publication.
- [x] Obtained local commit authorization on November 6; this plan accompanies the reviewed source commit.
- [ ] Obtained authorization for remote push and website publication.
- [ ] Verified the website projection and actual authorized live publication.

Source verification on November 5: 38 official documentation tests, 18 Solo
delivery-policy tests and 28 Solo production-guidance tests passed (84 total).
Tracked diff whitespace checks passed. Existing CRDs and the accepted inventory
remain unchanged. These checks establish documentation consistency, not runtime
conformance or platform feasibility.

The independent review returned APPROVE WITH CONDITIONS with one bounded
clarification: distinguish transient classification from retained assessments,
and do not imply fresh owner confirmation for classification already within
existing authority. The clarification and a focused regression test are now
applied and passing. The reviewer explicitly considered a second review
unnecessary for that correction; this is recorded remediation, not a claim of
a new unqualified reviewer verdict. No remaining source blocker was identified.

The November 6 commit step preserves the reviewed source bytes; its exact
containing revision is recorded in the execution handoff after Git creates it.
No website projection, publication, runtime adoption or recipient acknowledgement
is claimed by this checklist.

Documentation readiness and public publication are separate completion states.
Neither establishes runtime adoption. Stages 0–7 remain complete as recorded;
Stage 8 remains current. This supporting framework work introduces no new
roadmap stage and is not a gate against unrelated authorized production use.
