"""Local documentation checks; no runtime or deployment evidence implied."""

import re
import unittest
from urllib.parse import unquote, urlsplit

from test_core_app_documentation import ROOT, anchors, normalized


NOTICE = "docs/pios-mobile-contract-alignment-2026-10-08.md"
CANDIDATES = "docs/capabilities/decisions/mobile-interoperability-candidates-2026-10-08.md"


class MobileContractAlignmentTests(unittest.TestCase):
    def test_public_mobile_documents_exclude_private_locations_and_measurements(self):
        paths = list((ROOT / "docs").glob("pios-first-party-mobile*.md"))
        paths += [ROOT / "docs/core-iphone-device-access-and-notification-plan-v0.1.md",
                  ROOT / "docs/lifestory-reference-assessment-for-core-mobile-2026-09-29.md"]
        for path in paths:
            text = path.read_text()
            with self.subTest(source=path.name):
                for marker in ("/Users/", "~/", "Storage-wiki/", "ValtoAI/", "owner iPhone `"):
                    self.assertNotIn(marker, text)
                self.assertNotRegex(text, r"Owner validation (?:showed|produced|aligned|passed at)\s+\d")

    def test_companions_distinguish_indie_from_dependent_lifestory(self):
        for name in (
            "hosting-core-boundaries-and-portability-principles-v0.1.md",
            "core-distribution-and-compatibility-spec-v0.1.md",
            "core-hosted-service-fork-path-v0.1.md",
        ):
            text = normalized((ROOT / "docs" / name).read_text())
            with self.subTest(source=name):
                self.assertIn("LifeStory Indie", text)
                self.assertIn("Core-dependent companion", text)
                self.assertNotIn("or LifeStory.", text)
                self.assertNotIn("LifeStory, or a general-purpose assistant", text)
                self.assertNotIn("LifeStory should retain useful operation", text)

    def test_source_working_and_cache_states_remain_distinct(self):
        text = normalized((ROOT / "docs/integration-interoperability-and-governance-v0.1.md").read_text())
        for phrase in (
            "Device-source record", "App-owned working record",
            "Normalized device evidence or local projection",
            "Cache eviction must not dispose of them",
            "not pending upload until selected for submission",
            "Both sides are part of PIOS",
            "Local save, handoff validation, local semantic application, canonical Core acceptance",
            "Direct and brokered paths must converge",
            "Do not rename them or silently give an older receipt stronger meaning",
        ):
            self.assertIn(phrase, text)

    def test_profile_limits_hybrid_exception_and_preserves_general_model(self):
        text = normalized((ROOT / "docs/pios-first-party-mobile-apps-by-prifina.md").read_text())
        self.assertIn("own least-privilege reconciliation identity", text)
        self.assertIn("not grant Notes general capture", text)
        self.assertIn("Actual activation and granted scopes", text)
        self.assertNotIn("Core is the only PIOS network client", text)
        self.assertIn("pios-mobile-contract-alignment-2026-10-08.md", (ROOT / "index.html").read_text())

    def test_historical_handoff_is_not_current_activation_authority(self):
        handoff = normalized((ROOT / "docs/pios-first-party-mobile-app-handoff-2026-10-02.md").read_text())
        self.assertIn("retained", handoff.lower())
        self.assertIn("pios-mobile-contract-alignment-2026-10-08.md", handoff)
        local = (ROOT / "docs/pios-first-party-mobile-local-handoff-v0.1.md").read_text()
        self.assertIn("Current Contract And Historical Activation Evidence", local)
        self.assertIn("canonical", local)

    def test_candidates_do_not_silently_enter_inventory(self):
        text = (ROOT / CANDIDATES).read_text()
        self.assertIn("candidate assessment, not finalized CRDs or inventory additions", text)
        rows = text.split("## Candidate boundaries", 1)[1].split("## Preliminary MLE checks", 1)[0]
        self.assertEqual(len(re.findall(r"^\| (?:Reconcile|Acquire|Evaluate) ", rows, re.MULTILINE)), 3)
        candidate_names = set(re.findall(r"^\| ((?:Reconcile|Acquire|Evaluate) [^|]+) \|", rows, re.MULTILINE))
        inventory = (ROOT / "docs/capabilities/capability-inventory.md").read_text()
        inventory_names = set(re.findall(r"^\| `[^`]+` \| ([^|]+) \|", inventory, re.MULTILINE))
        self.assertTrue(candidate_names.isdisjoint(inventory_names), "Candidate-only names must not be inventory entries")
        inventory_crds = set(re.findall(r"\]\(crds/([^/)]+\.md)\)", inventory))
        files = {path.name for path in (ROOT / "docs/capabilities/crds").glob("*.md")}
        self.assertEqual(inventory_crds, files, "Inventory and CRD files must agree, not merely have equal counts")
        for private_marker in ("/Users/", "owner_valto", "valto-agents-vm"):
            self.assertNotIn(private_marker, text)

    def test_notice_candidate_and_library_links_resolve(self):
        for name in (NOTICE, CANDIDATES, "docs/capabilities/README.md", "docs/capabilities/project-plan.md", "docs/capabilities/work-status.md"):
            path = ROOT / name
            for link in re.findall(r"(?<!!)\[[^\[\]]+\]\(([^)]+)\)", path.read_text()):
                target = urlsplit(link.strip("<>"))
                if target.scheme or target.netloc:
                    continue
                destination = (path.parent / unquote(target.path)).resolve() if target.path else path
                with self.subTest(source=name, link=link):
                    self.assertTrue(destination.exists(), str(destination))
                    if target.fragment and destination.suffix in {".html", ".md"}:
                        self.assertIn(unquote(target.fragment), anchors(destination))


if __name__ == "__main__":
    unittest.main()
