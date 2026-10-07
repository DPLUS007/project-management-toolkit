import tempfile
import unittest
from pathlib import Path
from readiness import assess

class ReadinessTests(unittest.TestCase):
    def assess_text(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sites.csv"
            path.write_text(text, encoding="utf-8")
            return assess(path)

    def test_blocker_overrides_green_and_amber_is_not_ready(self):
        rows = self.assess_text("site,data,uat,training,support,blocker\nA,green,green,green,green,Approval unresolved\nB,green,amber,green,green,\nC,green,green,green,green,\n")
        self.assertEqual([row["status"] for row in rows], ["red", "amber", "green"])

    def test_invalid_and_duplicate_inputs_fail(self):
        for text in (
            "site,data\nA,green\n",
            "site,data,uat,training,support,blocker\nA,unknown,green,green,green,\n",
            "site,data,uat,training,support,blocker\nA,green,green,green,green,\na,green,green,green,green,\n",
            "site,data,uat,training,support,blocker\n",
        ):
            with self.subTest(text=text):
                with self.assertRaises(ValueError):
                    self.assess_text(text)

if __name__ == "__main__":
    unittest.main()
