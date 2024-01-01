import unittest
from leetcode.minimum_window_substring import Solution

class TestSolution(unittest.TestCase):
    def test_min_window(self):
        s = Solution()
        print(s.minWindow("ADOBECODEBANC", "ABC"))
        # "ADOBECODEBANC", t = "ABC"

        self.assertEqual("BANC", s.minWindow("ADOBECODEBANC", "ABC"))
        self.assertEqual("", s.minWindow("a", "aa"))
        self.assertEqual("a", s.minWindow("a", "a"))

if __name__ == '__main__':
    unittest.main()
