"""Source-contract regressions only; these do not prove a running capability."""

import unittest

from test_core_app_documentation import ROOT, normalized, parse_html


PROFILE = "docs/operating-document-authority-and-recovery-v0.1.md"


class OperatingDocumentAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = normalized((ROOT / PROFILE).read_text(encoding="utf-8"))
        cls.master_html = (ROOT / "index.html").read_text(encoding="utf-8")
        section = cls.master_html.split('id="agent-definition-governance"', 1)[1]
        section = section.split("<h3>21.11", 1)[0]
        cls.master = normalized(" ".join(parse_html(section).text))
        cls.integration = normalized((ROOT / "docs/integration-interoperability-and-governance-v0.1.md").read_text())
        cls.portability = normalized((ROOT / "docs/pios-portability-package-v0.1.md").read_text())

    def assert_phrases(self, text, phrases):
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_master_preserves_owner_definitions_and_external_authority(self):
        self.assert_phrases(self.master, (
            "Core retains the owner's adopted agent definitions",
            "may remain authoritative in their declared upstream repositories",
            "Runtime copies are not the primary truth",
            "within the owner's grants",
            "permission to edit a policy's text does not grant permission to activate",
            "not a claim of implemented support",
        ))
        self.assertNotIn("Agent definitions, skills, roles, and operational files are part of Core.", self.master)
        for source in ("index.html", "README.md", "docs/publication-notes.md"):
            self.assertIn("operating-document-authority-and-recovery-v0.1.md", (ROOT / source).read_text())

    def test_full_text_cannot_be_substituted_by_summary_or_projection(self):
        self.assert_phrases(self.profile, (
            "old archive Original does not demonstrate current full-document support",
            "complete accepted content, including meaningful metadata/frontmatter and links",
            "expected base revision",
            "preserves both accepted and proposed work",
            "Document-specific authorization must be enforceable",
            "change the agent's own grants",
            "do not re-ingest an already retained Original",
        ))

    def test_cutover_retains_evidence_and_one_authority(self):
        self.assert_phrases(self.profile, (
            "Scoped export and isolated reconstruction of full content",
            "one editing authority",
            "rollback is not silent restoration of an older policy or grant",
            "Explicit promotion under owner authority",
            "source deletion is a separate decision",
            "Existing archive, summary-edit or subset-recovery evidence retains its original scope",
            "without a whole vault migration or blocking unrelated authorized production work",
        ))

    def test_offline_bootstrap_does_not_create_freshness_or_authority(self):
        self.assert_phrases(self.profile, (
            "independently available, protected bootstrap",
            "Do not put secret values in that bundle",
            "Cached integrity proves retained bytes, not current authority",
            "unverified freshness must stop actions that require current policy",
            "exception must be approved beforehand",
            "Loss of connectivity never creates new permissions",
            "Keep offline edits/proposals pending",
            "revalidate source versions, authority and revocation",
        ))

    def test_recovery_separates_package_state_and_installability(self):
        self.assert_phrases(self.portability, (
            "Application package", "Private application state",
            "Shared-container and pending state", "Credentials and installation",
            "Functional recovery",
            "A version label or lone executable does not establish package equivalence",
            "a private-state backup or Core export does not prove their recovery",
            "change from an already required exact rollback needs explicit approval",
            "does not require exact old binaries for every PIOS deployment",
            "Restoration does not silently reactivate old grants",
        ))

    def test_response_loss_preserves_identity_and_uncertain_acceptance(self):
        self.assert_phrases(self.integration, (
            "A timeout or lost response does not prove that the operation was rejected",
            "Keep acceptance unproved until governed reconciliation",
            "Retain the original operation identity, destination and pending content",
            "not a required new wire-status name",
            "Increasing worker counts or timeouts is not proof of safety",
            "not a universal concurrency architecture or latency target",
        ))

    def test_profile_is_selectable_not_a_runtime_or_compatibility_claim(self):
        self.assert_phrases(self.profile, (
            "selectable full-document operating profile",
            "no sixth data zone",
            "does not add accepted CRDs or change Core Compatibility Levels 1–5",
            "Documentation regression tests prove source consistency, not runtime behavior",
            "Independent development agents",
            "without becoming PIOS-native services",
            "No particular manager, agent count, model, VM, Mac runner or task product",
        ))

    def test_profile_excludes_private_installation_details(self):
        for marker in ("/Users/", "~/", "owner_valto", "valto-agents-vm",
                       "Valtos-Ally-Mac", "ValtoAI/", "a55cea260a05f4db",
                       "25,066", "45,566", "730-file"):
            with self.subTest(marker=marker):
                self.assertNotIn(marker, self.profile)


if __name__ == "__main__":
    unittest.main()
