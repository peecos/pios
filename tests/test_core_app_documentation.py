"""Local-only regression checks for Core app naming and device boundaries."""

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
INTEGRATION = ROOT / "docs/integration-interoperability-and-governance-v0.1.md"
HOSTING = ROOT / "docs/hosting-core-boundaries-and-portability-principles-v0.1.md"
GUIDANCE = (
    "README.md",
    "ABOUT.md",
    "docs/core-distribution-and-compatibility-spec-v0.1.md",
    "docs/core-distribution-roadmap-v0.1.md",
    "docs/core-hosted-service-fork-path-v0.1.md",
    "docs/ecosystem-participation-and-project-catalog-v0.1.md",
    "docs/hosting-core-boundaries-and-portability-principles-v0.1.md",
    "docs/integration-interoperability-and-governance-v0.1.md",
    "docs/pios-portability-package-v0.1.md",
    "docs/publication-notes.md",
)


class DocumentHTML(HTMLParser):
    VOID = {
        "area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr",
    }

    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.stack = []
        self.errors = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "a" and "href" in attributes:
            self.links.append(attributes["href"])
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected closing tag: {tag}")
        else:
            self.stack.pop()

    def handle_data(self, data):
        self.text.append(data)


def parse_html(text):
    document = DocumentHTML()
    document.feed(text)
    document.close()
    return document


def normalized(text):
    return " ".join(text.split())


def anchors(path):
    text = path.read_text(encoding="utf-8")
    found = set(parse_html(text).ids)
    if path.suffix == ".md":
        for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
            heading = re.sub(r"[^\w\s-]", "", heading.lower())
            found.add(re.sub(r"\s", "-", heading.strip()))
    return found


class CoreAppDocumentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.master = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.html = parse_html(cls.master)
        cls.master_text = normalized(" ".join(cls.html.text))
        cls.integration = normalized(INTEGRATION.read_text(encoding="utf-8"))

    def test_master_is_well_nested_and_preserves_boundary_links(self):
        self.assertEqual(self.html.errors, [])
        self.assertEqual(self.html.stack, [])
        self.assertEqual(len(self.html.ids), len(set(self.html.ids)))
        for anchor in (
            "system-core-and-deployment-boundaries",
            "corebox-and-independent-applications",
            "core-app-and-independent-applications",
            "core-app-device-cache",
        ):
            self.assertIn(anchor, self.html.ids)

    def test_master_distinguishes_name_role_and_core_contract(self):
        for phrase in (
            "Core app (previously known as Corebox)",
            "Its display name is Core",
            "outside the narrower Core contract but part of PIOS",
            "PIOS-native, PIOS-dependent owner hub/gateway",
            "not a claim that all features are shipped",
        ):
            self.assertIn(phrase, self.master_text)
        for responsibility in ("Capture", "Access", "Understand", "Govern"):
            self.assertIn(f"<td>{responsibility}</td>", self.master)

    def test_global_entrypoints_use_current_name_with_legacy_context(self):
        for relative in GUIDANCE:
            with self.subTest(path=relative):
                text = normalized((ROOT / relative).read_text(encoding="utf-8"))
                self.assertIn("Core app", text)
                self.assertIn("Corebox", text)
                self.assertNotIn("Corebox is a PIOS-native", text)

    def test_shared_cache_is_an_explicit_iphone_role(self):
        for phrase in (
            "Shared caching is a key role on iPhone",
            "in the same App Group",
            "recently loaded files",
            "flaky connections",
            "should not require downloading the same bytes again",
            "must not depend on the foreground Core app process",
        ):
            self.assertIn(phrase, self.integration)

    def test_pending_work_is_not_disposable_cache(self):
        for phrase in (
            "Recent-content cache",
            "Selected offline content",
            "Pending capture or edit",
            "never treat it as disposable cache",
            "A Core/account switch must not expose another owner's cache",
            "Clearing a cache does not delete Core Originals, Events, or Knowledge",
        ):
            self.assertIn(phrase, self.integration)

    def test_shared_storage_does_not_bypass_authority(self):
        for phrase in (
            "not a per-app authorization system",
            "logical grant checks alone cannot create per-app confidentiality",
            "Do not share owner-wide credentials",
            "absent, expired, or ambiguous authority fails closed",
            "Immediate remote erasure",
            "offline device cannot be promised",
            "Reserve **Local Core**",
        ):
            self.assertIn(phrase, self.integration)

    def test_routing_is_optional_and_capability_scoped(self):
        for path in ("Direct", "Brokered", "Hybrid"):
            self.assertIn(f"| {path} |", self.integration)
        self.assertIn("not required to route every operation", self.integration)
        self.assertIn("nor is every consuming app required", self.integration)
        self.assertIn("server-side native retrieval", self.integration)

    def test_statistics_and_rename_do_not_overclaim(self):
        for phrase in (
            "Statistics distinguish canonical records and original bytes",
            "unavailable or stale measurements are labelled",
            "An archive restore is not automatically complete PIOS recovery",
            "does not rename bundle identifiers, App Groups, protocol/schema fields",
            "Existing Corebox identifiers may remain compatibility names",
        ):
            self.assertIn(phrase, self.master_text)

    def test_old_companion_anchors_remain_available(self):
        self.assertIn("91-corebox-a-pios-native-hub-and-gateway", anchors(HOSTING))
        self.assertIn("10-synthetic-example-corebox-boundary", anchors(INTEGRATION))

    def test_local_document_links_resolve(self):
        files = [ROOT / "index.html", *ROOT.glob("*.md"), *sorted((ROOT / "docs").glob("*.md"))]
        for path in files:
            text = path.read_text(encoding="utf-8")
            links = parse_html(text).links
            if path.suffix == ".md":
                links += re.findall(r"(?<!!)\[[^\[\]]+\]\(([^)]+)\)", text)
            for link in links:
                target = urlsplit(link.strip("<>"))
                if target.scheme or target.netloc:
                    continue
                destination = (path.parent / unquote(target.path)).resolve() if target.path else path
                with self.subTest(path=str(path.relative_to(ROOT)), link=link):
                    self.assertTrue(destination.exists(), str(destination))
                    if target.fragment and destination.suffix in {".html", ".md"}:
                        self.assertIn(unquote(target.fragment), anchors(destination))


if __name__ == "__main__":
    unittest.main()
