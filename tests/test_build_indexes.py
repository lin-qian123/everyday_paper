import unittest

from scripts import build_indexes


class BuildIndexesTests(unittest.TestCase):
    def test_explicit_categories_override_keyword_classification(self):
        item = {
            "title": "Inertial Confinement Fusion example",
            "categories": [
                "hedp-icf-laboratory-astrophysics",
                "ai-ml-plasma-physics",
            ],
        }

        self.assertEqual(
            build_indexes.classify(item),
            [
                "hedp-icf-laboratory-astrophysics",
                "ai-ml-plasma-physics",
            ],
        )

    def test_explicit_categories_reject_unknown_slug(self):
        item = {
            "title": "Plasma example",
            "categories": ["not-a-real-category"],
        }

        with self.assertRaisesRegex(ValueError, "Unknown category slug"):
            build_indexes.classify(item)


if __name__ == "__main__":
    unittest.main()
