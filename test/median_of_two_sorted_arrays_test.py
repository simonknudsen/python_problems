import unittest
from leetcode import median_of_two_sorted_arrays as m

class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = m.Solution()
        #self.assertEqual(2.0, a.findMedianSortedArrays([1, 3], [2]))
        #self.assertEqual(2.5, a.findMedianSortedArrays([1, 2], [3, 4]))
        #self.assertEqual(2.0, a.findMedianSortedArrays([1, 2, 3], []))
        #self.assertEqual(2.0, a.findMedianSortedArrays([], [1, 2, 3]))
        #self.assertEqual(70.0, a.findMedianSortedArrays([40], [1,100,200]))
        self.assertEqual(70.0, a.findMedianSortedArrays([1, 100, 200],[40]))

if __name__ == '__main__':
    unittest.main()
