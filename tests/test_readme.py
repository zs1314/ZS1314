import pathlib
import unittest


class ReadmeQualityTests(unittest.TestCase):
    def test_readme_exists_with_standard_name(self):
        """Keep documentation discoverable with the conventional README.md filename."""
        self.assertTrue(pathlib.Path("README.md").exists())

    def test_research_interest_sentence_is_clear_and_consistent(self):
        """Ensure the main description is grammatically correct and terminology is consistent."""
        content = pathlib.Path("README.md").read_text(encoding="utf-8")
        self.assertIn("# Research Interests", content)
        self.assertIn("LLMs", content)
        self.assertIn("agents", content)
        self.assertNotIn("LLM, Agents", content)


if __name__ == "__main__":
    unittest.main()
