# Publication Notes

This repository is a curated public publication of the PIOS 2.0 master
documentation.

Source used for the initial publication: the current PIOS 2.0 master
documentation maintained in the owner's working documentation environment.

The initial public-facing adjustments were limited to neutral source/provenance
wording and links around the standalone HTML document. This repository is now
the canonical PIOS 2.0 framework source, as described in [ABOUT.md](../ABOUT.md),
and receives ongoing architecture and specification clarifications. Website
renders and summaries are downstream publication surfaces, not competing
architecture authorities.

The September 11, 2026 clarification distinguishes Core contract membership,
PIOS system membership, and physical placement. It makes complete Solo VM
packaging, native processing, and Corebox's PIOS-native hub/gateway role explicit
without upgrading implementation, compatibility, or migration-readiness claims.
Editing these source documents does not itself publish the website or authorize
deployment or migration.

The September 13, 2026 update names the **Core app (previously known as
Corebox)** as the PIOS-native owner interface, with **Core** as its display
name. The master and companion documents define capture, access, system
statistics, governance, and device-local support. Shared App Group caching on
iPhone is an explicit role for authorized recent/offline content, including
intermittent connectivity and avoiding repeated downloads. Pending submissions
are protected separately from disposable cache; shared-container access,
offline authority, expiry, and revocation limits remain explicit.

This is a framework documentation update, not evidence that the new app
features are shipped. It preserves the narrower Core contract, independent
consumer roles, Solo server-side placement, and existing compatibility levels.
Legacy Corebox anchors and identifiers remain for continuity. No bundle ID,
App Group, protocol/schema field, endpoint, storage path, installed app, owner
data, or historical evidence is renamed by this update. The website render,
app implementation, and owner-specific plans require their own scoped updates;
source editing alone does not publish them.

The September 27, 2026 clarification records the **PIOS First-Party Mobile
Apps by Prifina** profile without narrowing the open PIOS integration model.
The profile is deployment-neutral and may connect through Core to any compatible
PIOS implementation. Notes and Voice Notes remain independently usable and
may use app-owned iCloud or custom endpoints, while their PIOS exchange is
mediated locally by Core. The existing LifeStory product continues as
**LifeStory Indie**; a new **LifeStory** is defined as Core-dependent, with
Core owning activated device-source collection and PIOS connectivity.
Third-party applications retain direct, brokered and hybrid choices. This
documentation change does not create app identities, alter entitlements, move
data or authorize a release.

The [October 8, 2026 mobile contract alignment](pios-mobile-contract-alignment-2026-10-08.md)
distinguishes device-source and application working records from caches and
separates local handoff, canonical acceptance, reverse application and
acknowledgement delivery. The first-party profile now permits Notes' bounded
direct reconciliation alongside Core mediation; the September 27 description
above records the earlier profile, not an exclusive-routing rule for current
work. Three possible library additions remain candidate assessments, not
accepted CRDs. These local source changes do not by themselves establish a
GitHub publication, website update, running-agent acknowledgement or deployment.

The November 5, 2026 source clarification distinguishes owner-adopted agent
definitions and operating policies from repository-owned instructions, reusable
software and official framework authority. The master's section 21.10 links the
[Operating Document Authority and Recovery profile](operating-document-authority-and-recovery-v0.1.md)
for full-document revisions, explicit adoption, conflict handling and protected
offline bootstrap. Portability and integration companions add application
recovery evidence boundaries and uncertain-acceptance/service-progress examples.

These are framework semantics and a draft selectable profile, not evidence of a
documentation cutover, remote execution handoff, application recovery, live
timeout correction or new mandatory Core capability. Existing evidence retains
its original scope; implementation roadmaps and authorization remain separate.
No accepted CRDs or compatibility levels change. Local edits do not themselves
publish GitHub or the website or notify already-running agents.

The public documentation is licensed under CC BY 4.0 with attribution to
Valto Loikkanen / peecos. Project names and logos are handled separately in
`TRADEMARKS.md`.
