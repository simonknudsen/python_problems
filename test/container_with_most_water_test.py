import unittest
from leetcode import container_with_most_water

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = container_with_most_water.Solution()
        self.assertEqual(49, s.maxArea([1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    unittest.main()