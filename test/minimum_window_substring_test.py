import unittest
from leetcode.minimum_window_substring import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()
        print(s.minWindow("ADOBECODEBANC", "ABC"))
        # "ADOBECODEBANC", t = "ABC"
        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
