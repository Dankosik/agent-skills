"""Resource integrity only; no model or infrastructure behavior is evaluated."""
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "auth-access-control", "cache-engineering", "concurrency-control",
    "distributed-system-design", "durable-background-jobs",
    "external-api-integration", "postgres-performance", "postgres-schema-design",
    "production-diagnosis", "reliable-messaging",
}


def prose(text):
    """Ignore examples inside fenced code, including Markdown templates."""
    result = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def anchors(text):
    counts = {}
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M):
        slug = re.sub(r"[^\w\s-]", "", heading.lower()).replace(" ", "-")
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        result.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return result


def local_target(source, target, root=ROOT):
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    path = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
    path.relative_to(root.resolve())  # Reject escaping the repository.
    return path, unquote(parsed.fragment)


class SkillResources(unittest.TestCase):
    def test_skill_inventory_and_entry_metadata(self):
        paths = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in paths}, SKILLS)
        for path in paths:
            with self.subTest(skill=path.parent.name):
                text = path.read_text(encoding="utf-8")
                # This pack deliberately uses a minimal, portable YAML subset.
                match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ("[^\n]+")\n---\n', text)
                self.assertIsNotNone(match)
                self.assertEqual(match[1], path.parent.name)
                description = json.loads(match[2])
                self.assertTrue(description.strip())
                self.assertLessEqual(len(description), 1024)
                self.assertTrue(text.endswith("\n"))
                self.assertNotIn("\r", text)

    def test_runtime_and_document_links_resolve(self):
        paths = [ROOT / "README.md"]
        paths += sorted((ROOT / "docs").rglob("*.md"))
        paths += sorted((ROOT / "evals/instruction-boundaries").glob("*.md"))
        paths += sorted((ROOT / "skills").glob("*/SKILL.md"))
        paths += sorted((ROOT / "skills").glob("*/references/*.md"))
        for source in paths:
            for target in re.findall(r"\]\(([^\s)]+)\)", prose(source.read_text(encoding="utf-8"))):
                with self.subTest(source=str(source.relative_to(ROOT)), target=target):
                    resolved = local_target(source, target)
                    if resolved is None:
                        continue
                    path, fragment = resolved
                    self.assertTrue(path.exists(), str(path))
                    if fragment and path.suffix == ".md":
                        self.assertIn(fragment, anchors(path.read_text(encoding="utf-8")))
                    if source.is_relative_to(ROOT / "skills"):
                        # Each skill's runtime links remain independently installable.
                        path.relative_to(ROOT / "skills" / source.relative_to(ROOT / "skills").parts[0])
                        self.assertNotIn("evals", path.relative_to(ROOT).parts)

    def test_existing_evaluation_suites_remain_present(self):
        for name in sorted(SKILLS):
            with self.subTest(skill=name):
                suite = json.loads((ROOT / "skills" / name / "evals/evals.json").read_text(encoding="utf-8"))
                self.assertEqual(suite["skill_name"], name)
                cases = suite["evals"]
                self.assertGreater(len(cases), 0)
                self.assertEqual(len({case["id"] for case in cases}), len(cases))
                for case in cases:
                    self.assertTrue(case["prompt"].strip())

    def test_boundary_inputs_and_grading_stay_separate(self):
        directory = ROOT / "evals/instruction-boundaries"
        prompts = json.loads((directory / "prompts.json").read_text(encoding="utf-8"))
        rubric = json.loads((directory / "rubric.json").read_text(encoding="utf-8"))
        self.assertEqual(prompts["status"], "NOT RUN")
        self.assertEqual(rubric["status"], "NOT RUN")
        ids = [item["id"] for item in prompts["cases"]]
        self.assertEqual(len(ids), 20)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), set(rubric["expectations"]))
        for item in prompts["cases"]:
            self.assertEqual(set(item), {"id", "prompt"})
            self.assertTrue(item["prompt"].strip())
            self.assertGreater(len(rubric["expectations"][item["id"]]), 0)
        for pair in rubric["contrast_pairs"]:
            self.assertEqual(len(pair), 2)
            self.assertEqual(len(set(pair)), 2)
            self.assertTrue(set(pair).issubset(ids))

    def test_link_helpers_distinguish_examples_and_anchors(self):
        text = "# Alpha\n```md\n[Example](missing.md)\n# Not an anchor\n```\n## Alpha\n"
        self.assertNotIn("missing.md", prose(text))
        self.assertEqual(anchors(text), {"alpha", "alpha-1"})
        self.assertIsNone(local_target(ROOT / "README.md", "https://example.com/x"))
        with self.assertRaises(ValueError):
            local_target(ROOT / "README.md", "../outside.md")


if __name__ == "__main__":
    unittest.main()
