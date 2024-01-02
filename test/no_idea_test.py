import unittest
from hackerrank import no_idea

class MyTestCase(unittest.TestCase):
    def test_happiness(self):
        self.assertEqual(1, no_idea.happiness("3 2", "1 5 3", "3 1", "5 7"))

if __name__ == '__main__':
    unittest.main()