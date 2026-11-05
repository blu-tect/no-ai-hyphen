import unittest
from no_ai_hyphen import violations

class CheckerTests(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(violations("Hello, world."), [])

    def test_em_dash(self):
        self.assertEqual(violations("a\u2014b"), [(1, 2, "em dash")])

    def test_en_dash(self):
        self.assertEqual(violations("a\u2013b"), [(1, 2, "en dash")])

if __name__ == "__main__":
    unittest.main()
