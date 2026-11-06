"""Documentation-contract checks; not runtime or conformance evidence."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

from test_core_app_documentation import ROOT, anchors, normalized, parse_html


MEMORY = "docs/cognitive-memory-source-discovery-and-derived-representations-v0.1.md"
INTEGRATION = "docs/integration-interoperability-and-governance-v0.1.md"
APPLE = "docs/apple-local-and-mixed-device-profile-v0.1.md"
COMPATIBILITY = "docs/core-distribution-and-compatibility-spec-v0.1.md"
NOTICE = "docs/pios-2.0-enrichment-alignment-2026-11-05.md"
CANDIDATES = "docs/capabilities/decisions/information-lifecycle-and-device-profile-candidates-2026-11-05.md"


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def after_anchor(relative, anchor):
    text = read(relative)
    marker = f'id="{anchor}"'
    if text.count(marker) != 1:
        raise AssertionError(f"Expected one {anchor} anchor in {relative}")
    # Do not let a later profile accidentally satisfy the current profile's checks.
    section = text.split(marker, 1)[1]
    section = re.split(r'<a id="[^"]+"></a>', section, maxsplit=1)[0]
    return normalized(section)


class PIOS20EnrichmentTests(unittest.TestCase):
    def assert_contract(self, text, clauses):
        for clause in clauses:
            with self.subTest(clause=clause):
                self.assertIn(clause, text)

    def test_master_keeps_foundations_and_links_optional_detail(self):
        master = parse_html(read("index.html"))
        text = normalized(" ".join(master.text))
        self.assert_contract(text, (
            "The event log is the canonical spine",
            "outside the narrower Core contract but part of PIOS",
            "PIOS-native, PIOS-dependent owner hub/gateway",
            "No new mandatory endpoint or wire field",
        ))
        for section, target in (
            ("assertions-and-information-lineage", f"{MEMORY}#assertion-and-lineage-profile"),
            ("emergent-cluster-lifecycle", f"{MEMORY}#semantic-assessment-and-cluster-profile"),
            ("governed-semantic-assessment", f"{MEMORY}#processing-result-reuse"),
            ("capability-led-adoption", APPLE),
            ("circle-context-and-disclosure", f"{INTEGRATION}#controlled-disclosure-profile"),
        ):
            with self.subTest(section=section):
                self.assertIn(section, master.ids)
                self.assertIn(target, master.links)
        self.assertEqual(master.errors, [])
        self.assertEqual(master.stack, [])
        self.assertEqual(len(master.ids), len(set(master.ids)))

    def test_assertion_dimensions_and_dependency_kinds_are_independent(self):
        text = after_anchor(MEMORY, "assertion-and-lineage-profile")
        for dimension in ("Origin", "Evidential support", "Acceptance", "Temporal validity", "Access"):
            self.assertIn(f"| {dimension} |", text)
        for dependency in ("Evidential", "Computational", "Policy"):
            self.assertIn(f"| {dependency} |", text)
        for state in ("stale", "disputed", "inaccessible", "superseded"):
            self.assertIn(f"`{state}`", text)
        self.assert_contract(text, (
            "A canonical record of a claim is not proof that the claim is true",
            "These outcomes can coexist",
            "Revocation alone supplies no evidence that either claim was false",
            "earlier successful run grants no permission to recompute",
            "preserving the append-oriented Event history",
        ))

    def test_optional_profiles_do_not_become_universal_core_requirements(self):
        memory = after_anchor(MEMORY, "assertion-and-lineage-profile")
        self.assert_contract(memory, (
            "only to implementations explicitly selecting that profile",
            "no mandatory Core capability, API/export field, or compatibility level",
            "Capture can proceed under existing rules",
            "no sixth zone, required graph database",
        ))
        disclosure = after_anchor(INTEGRATION, "controlled-disclosure-profile")
        self.assert_contract(disclosure, (
            "only to an implementation profile that explicitly selects it",
            "Selection does not issue grants or activate recipients",
            "no permission namespace, protocol, required endpoint, wire field",
        ))
        self.assertIn("not an adopted first-party implementation", normalized(read(APPLE)))

    def test_semantic_inputs_and_scores_do_not_establish_authority(self):
        text = after_anchor(MEMORY, "semantic-assessment-and-cluster-profile")
        self.assert_contract(text, (
            "candidate-set identity/version and the authorized subset actually considered",
            "Authorize and minimize both source content and candidate metadata before model",
            "without copying excluded metadata into routine logs",
            "High confidence supplies neither correctness, access rights, nor authority to act",
            "Multiple labels, Roles, and Modes may apply concurrently",
            "Classification, extraction, entity resolution, and canonical promotion are separate operations",
        ))

    def test_cluster_changes_preserve_identity_and_promotion_boundaries(self):
        text = after_anchor(MEMORY, "semantic-assessment-and-cluster-profile")
        self.assert_contract(text, (
            "Clusters may be unnamed, overlap, or have uncertain membership",
            "Membership changes create a revision",
            "Splits and merges record predecessor/successor references",
            "whether an existing identity continues and why",
            "Labels alone cannot transfer identity, acceptance, permissions",
            "Consolidation groups or summarizes existing material",
            "no cluster size, recurrence, or model score automatically adopts",
        ))

    def test_transient_assessments_do_not_force_retention_or_new_confirmation(self):
        text = after_anchor(MEMORY, "semantic-assessment-and-cluster-profile")
        self.assert_contract(text, (
            "transient routing/classification signal, retained evidence, a Derived projection, or a proposed Knowledge object",
            "Transient signals need not become durable records or retain every intermediate score",
            "transient treatment is not permission to omit that evidence",
            "Retained assessments declare their state treatment, retention and authorization basis",
            "Classification within existing request-scoped or standing authority needs no fresh owner confirmation",
            "a processing grant does not automatically authorize all three",
            "Meaning/Learning objects retain section 2.3's proposal/adoption controls",
        ))

    def test_reuse_differs_from_new_processing_and_disclosure(self):
        text = after_anchor(MEMORY, "processing-result-reuse")
        self.assert_contract(text, (
            "source identity/revision, operation, processor/model/rule version, parameters",
            "current permission for the requester, purpose, and audience",
            "Reprocessing executes a processor again and needs current processing authority",
            "same inputs do not guarantee identical model output",
            "Changing the audience requires a fresh disclosure decision",
            "Denied reuse does not authorize fetching sources again or switching models/providers",
        ))

    def test_controlled_disclosure_has_separate_decisions_and_copy_limits(self):
        text = after_anchor(INTEGRATION, "controlled-disclosure-profile")
        for decision in ("Access", "Use and process", "Derive", "Disclose", "Retain", "View later"):
            self.assertIn(f"| {decision} |", text)
        self.assert_contract(text, (
            "separate decisions do not require a new grant for every step",
            "before ranking, classification, extraction, summarization or embedding",
            "Do not silently choose the least restrictive source policy",
            "titles, filenames, thumbnails, previews",
            "checks the current viewer",
            "Possessing or forwarding the reference alone grants no access",
            "screenshot or remembered observation cannot be promised recall",
            "not proof of subsequent compliance",
            "fallback or retry must not widen input scope",
        ))

    def test_local_profile_preserves_acceptance_recovery_and_current_suite(self):
        text = normalized(read(APPLE))
        for arrangement in ("Device-side PIOS", "Conformant Local Core", "Device-side PIOS with remote Core"):
            self.assertIn(f"| {arrangement} |", text)
        self.assert_contract(text, (
            "Its PIOS-dependent purpose does not require every operation to contact a server",
            "cloud replica or five named containers alone is not a Local Core",
            "does not authorize blind historical backfill",
            "Successful synchronization proves neither canonical acceptance nor independent recovery",
            "do not rebind them automatically to the new account or destination",
            "bounded direct command/acknowledgement reconciliation path",
            "LifeStory Indie preserves its identity",
            "Proposed shared storage does not replace current app-owned synchronization",
            "makes no availability or pricing claim",
        ))

    def test_availability_is_not_a_new_connectivity_contract(self):
        compatibility = normalized(read(COMPATIBILITY))
        availability = normalized(read(COMPATIBILITY).split("### 4.1 Owner-Facing Availability", 1)[1].split("## 5.", 1)[0])
        for source in (availability, normalized(read(APPLE)), normalized(read("index.html"))):
            for state in ("implemented", "installed", "enabled", "authorized", "reachable", "healthy"):
                self.assertIn(state, source)
        self.assert_contract(availability, (
            "not a new mandatory endpoint, schema field or compatibility level",
            "Unknown or stale observations must not be presented as current availability",
            "Public views must not disclose private owner configuration or permissions",
        ))
        self.assert_contract(compatibility, (
            "versioned HTTPS API and a capability document at `/.well-known/core`",
            "core_version: 0.1.0", "api_versions: [v1]", "export_format_version: 1.0",
            "No implementation may claim Compatibility Level 2 or higher",
        ))

    def test_entrypoints_and_candidates_do_not_claim_adoption(self):
        for relative in ("index.html", "README.md", "docs/publication-notes.md", "docs/pios-first-party-mobile-apps-by-prifina.md"):
            self.assertIn(Path(NOTICE).name, read(relative))
        notice = normalized(read(NOTICE))
        self.assert_contract(notice, (
            "PIOS remains PIOS 2.0",
            "No existing mandatory Core requirement is removed",
            "no new mandatory Core capability is added",
            "There is no requirement to re-ingest completed domains",
            "does not prove that another agent received or acknowledged",
        ))
        candidates = normalized(read(CANDIDATES))
        self.assertIn("not finalized CRDs or inventory additions", candidates)
        self.assertIn("Before any formal extraction, pin the reviewed revision containing that delta", candidates)
        inventory = read("docs/capabilities/capability-inventory.md")
        self.assertNotIn(Path(CANDIDATES).name, inventory)

    def test_new_public_material_excludes_private_evidence_and_raw_shares(self):
        for relative in (APPLE, NOTICE, CANDIDATES):
            text = read(relative)
            for marker in ("/Users/", "~/", "owner_valto", "valto-agents-vm", "ValtoAI/", "chatgpt.com/share/", "25,066", "45,566"):
                with self.subTest(path=relative, marker=marker):
                    self.assertNotIn(marker, text)

    def test_package_links_and_fragments_resolve(self):
        for relative in (MEMORY, INTEGRATION, APPLE, NOTICE, CANDIDATES, COMPATIBILITY):
            path = ROOT / relative
            text = read(relative)
            links = parse_html(text).links + re.findall(r"(?<!!)\[[^\[\]]+\]\(([^)]+)\)", text)
            for link in links:
                target = urlsplit(link.strip("<>"))
                if target.scheme or target.netloc:
                    continue
                destination = (path.parent / unquote(target.path)).resolve() if target.path else path
                with self.subTest(path=relative, link=link):
                    self.assertTrue(destination.is_file(), str(destination))
                    if target.fragment:
                        self.assertIn(unquote(target.fragment), anchors(destination))


if __name__ == "__main__":
    unittest.main()
