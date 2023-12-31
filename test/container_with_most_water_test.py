import unittest
from leetcode import container_with_most_water

class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = container_with_most_water.Solution()
        self.assertEqual(49, s.maxArea([1,8,6,2,5,4,8,3,7]))
        self.assertEqual(1, s.maxArea([1,1]))
        self.assertEqual(4, s.maxArea([1, 2, 4, 3]))
        self.assertEqual(17, s.maxArea([2,3,4,5,18,17,6]))
        self.assertEqual(62, s.maxArea([6,4,3,1,4,6,99,62,1,2,6]))
        self.assertEqual(14608, s.maxArea([75,21,3,152,13,107,163,166,32,160,41,131,7,67,56,5,153,176,29,139,61,149,176,142,64,75,170,156,73,48,148,101,70,103,53,83,11,168,1,195,81,43,126,88,62,134,45,167,63,26,107,124,128,83,67,192,158,189,149,184,37,49,85,107,152,90,143,115,58,144,62,139,139,189,180,153,75,177,121,138,4,28,15,132,63,82,124,174,23,25,110,60,74,147,120,179,37,63,94,47]))
        self.assertEqual(70, s.maxArea([0, 14, 6, 2, 10, 9, 4, 1, 10, 3]))


if __name__ == '__main__':
    unittest.main()